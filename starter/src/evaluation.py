"""Evaluate retrieved evidence and record per-query benchmark traces."""
import re
from typing import Any, Dict, List


def normalize_for_match(text: str) -> str:
    """Helper to remove punctuation and extra spaces for resilient evidence matching."""
    if not text:
        return ""
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return " ".join(text.split())


def is_chunk_hit(question: Dict[str, Any], hit: Dict[str, Any]) -> bool:
    """Check if a retrieved chunk matches the gold source page and contains the required evidence."""
    gold_page = question.get("gold_page")
    hit_page = hit.get("page")

    # 1. Page match check (accepts exact physical page, doc_page, or adjacent page boundary for cross-page paragraphs)
    doc_page = question.get("doc_page")
    page_match = (
        (hit_page == gold_page)
        or (doc_page is not None and hit.get("doc_page") == doc_page)
        or (gold_page is not None and abs(hit_page - gold_page) <= 1)
    )
    if not page_match:
        return False

    # 2. Evidence match check
    evidence = question.get("evidence_quote", "")
    chunk_text = hit.get("text", "")

    spans = [s.strip() for s in evidence.split("...") if s.strip()] if "..." in evidence else [evidence]

    all_spans_hit = True
    for span in spans:
        clean_span = " ".join(span.split()).lower()
        clean_chunk = " ".join(chunk_text.split()).lower()
        if clean_span in clean_chunk:
            continue
        norm_span = normalize_for_match(span)
        norm_chunk = normalize_for_match(chunk_text)
        if norm_span in norm_chunk:
            continue
        tokens = [w for w in norm_span.split() if len(w) > 3]
        if tokens:
            overlap = sum(1 for w in tokens if w in norm_chunk) / len(tokens)
            if overlap >= 0.7:
                continue
        all_spans_hit = False
        break

    if all_spans_hit:
        return True

    # Fallback to key target data span (the last span usually contains the target metric and number)
    target_span = spans[-1]
    norm_target = normalize_for_match(target_span)
    target_tokens = [w for w in norm_target.split() if len(w) > 3]
    if target_tokens:
        overlap = sum(1 for w in target_tokens if w in normalize_for_match(chunk_text)) / len(target_tokens)
        if overlap >= 0.8:
            return True

    return False


def evaluate_query(question: Dict[str, Any], hits: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Check top-3 hits against gold page and evidence; return full trace record."""
    qid = question.get("id")
    split = question.get("split")
    qtype = question.get("type")
    gold_page = question.get("gold_page")
    filter_req = question.get("filter")

    hit_details = []
    has_hit_1 = False
    has_hit_3 = False
    filter_compliant = True

    for rank, hit in enumerate(hits, start=1):
        is_hit = is_chunk_hit(question, hit)
        if rank == 1 and is_hit:
            has_hit_1 = True
        if is_hit:
            has_hit_3 = True

        # Check filter compliance
        if filter_req:
            for fk, fv in filter_req.items():
                if hit.get(fk) != fv and hit.get("metadata", {}).get(fk) != fv:
                    filter_compliant = False

        hit_details.append({
            "rank": rank,
            "chunk_id": hit.get("chunk_id"),
            "score": hit.get("score"),
            "page": hit.get("page"),
            "doc_page": hit.get("doc_page"),
            "section": hit.get("section"),
            "is_hit": is_hit,
            "snippet": (hit.get("text") or "")[:200].replace("\n", " ") + "..."
        })

    return {
        "id": qid,
        "split": split,
        "type": qtype,
        "question": question.get("question"),
        "expected_answer": question.get("expected_answer"),
        "gold_page": gold_page,
        "gold_doc_page": question.get("doc_page"),
        "evidence_quote": question.get("evidence_quote"),
        "filter": filter_req,
        "filter_compliant": filter_compliant if filter_req else None,
        "hit_at_1": has_hit_1,
        "hit_at_3": has_hit_3,
        "hits": hit_details
    }


def summarize(traces: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Aggregate Hit@1 and Evidence Hit@3 by strategy and dev/test split."""
    dev_traces = [t for t in traces if t["split"] == "dev"]
    test_traces = [t for t in traces if t["split"] == "test"]

    def calc_metrics(subset: List[Dict[str, Any]]):
        total = len(subset)
        if total == 0:
            return {"total": 0, "hit1": "0/0", "hit1_pct": 0.0, "hit3": "0/0", "hit3_pct": 0.0}
        h1 = sum(1 for t in subset if t["hit_at_1"])
        h3 = sum(1 for t in subset if t["hit_at_3"])
        return {
            "total": total,
            "hit1_count": h1,
            "hit1_str": f"{h1}/{total}",
            "hit1_pct": round(h1 / total * 100, 1),
            "hit3_count": h3,
            "hit3_str": f"{h3}/{total}",
            "hit3_pct": round(h3 / total * 100, 1),
        }

    # Filter compliance
    filter_traces = [t for t in traces if t.get("filter") is not None]
    if filter_traces:
        comp_count = sum(1 for t in filter_traces if t.get("filter_compliant"))
        filter_summary = f"{comp_count}/{len(filter_traces)}"
    else:
        filter_summary = "N/A"

    return {
        "overall": calc_metrics(traces),
        "dev": calc_metrics(dev_traces),
        "test": calc_metrics(test_traces),
        "filter_compliance": filter_summary,
        "total_queries": len(traces)
    }
