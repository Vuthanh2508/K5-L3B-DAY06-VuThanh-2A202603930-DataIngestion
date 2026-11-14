"""Strict validator for Netflix Q2 2023 Form 10-Q Gold Benchmark.

Read-only validator: Does NOT modify or overwrite any files.
Validates the actual benchmark/gold_qa.json against NETFLIX_2023Q2_10Q-3-33.pdf.
Also checks parity with artifacts/gold_qa.json if present.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

import fitz

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_PDF = BASE_DIR / "NETFLIX_2023Q2_10Q-3-33.pdf"
DEFAULT_GOLD = BASE_DIR / "benchmark" / "gold_qa.json"
ARTIFACTS_GOLD = BASE_DIR / "artifacts" / "gold_qa.json"


def check_evidence(quote: str, page_text: str) -> bool:
    """Verify quote or ellipsis-separated spans exist in order on the page text."""
    if not quote or not page_text:
        return False
    norm_page = " ".join(page_text.split())

    if "..." in quote:
        spans = [s.strip() for s in quote.split("...") if s.strip()]
        last_idx = 0
        for span in spans:
            norm_span = " ".join(span.split())
            idx = norm_page.find(norm_span, last_idx)
            if idx == -1:
                return False
            last_idx = idx + len(norm_span)
        return True
    else:
        norm_quote = " ".join(quote.split())
        return norm_quote in norm_page


def validate(gold_path: Path, pdf_path: Path) -> bool:
    print(f"=== Validating Gold Benchmark ===")
    print(f"Gold File : {gold_path}")
    print(f"Source PDF: {pdf_path}")

    # 1. Check file existence
    if not gold_path.exists():
        print(f"❌ ERROR: Gold file does not exist at {gold_path}")
        return False
    if not pdf_path.exists():
        print(f"❌ ERROR: PDF file does not exist at {pdf_path}")
        return False

    # 2. Load JSON
    try:
        with open(gold_path, "r", encoding="utf-8") as f:
            questions: List[Dict[str, Any]] = json.load(f)
    except Exception as e:
        print(f"❌ ERROR: Failed to parse JSON: {e}")
        return False

    # 3. Structural checks
    if len(questions) != 20:
        print(f"❌ ERROR: Expected exactly 20 questions, found {len(questions)}")
        return False

    required_keys = {
        "id", "split", "type", "question", "expected_answer",
        "gold_source_id", "gold_page", "doc_page", "evidence_quote", "filter"
    }

    type_counts = {"truc_tiep": 0, "dien_dat_lai": 0, "dieu_kien_ngoai_le": 0, "metadata_filter": 0}
    split_counts = {"dev": 0, "test": 0}
    filter_counts = {"dev": 0, "test": 0}
    seen_ids = set()

    for q in questions:
        # Check required fields
        missing = required_keys - set(q.keys())
        if missing:
            print(f"❌ ERROR in {q.get('id', 'unknown')}: Missing required keys {missing}")
            return False

        qid = q["id"]
        if qid in seen_ids:
            print(f"❌ ERROR: Duplicate question ID '{qid}'")
            return False
        seen_ids.add(qid)

        split = q["split"]
        if split not in split_counts:
            print(f"❌ ERROR in {qid}: Invalid split '{split}'")
            return False
        split_counts[split] += 1

        qtype = q["type"]
        if qtype not in type_counts:
            print(f"❌ ERROR in {qid}: Invalid type '{qtype}'")
            return False
        type_counts[qtype] += 1

        if q["filter"] is not None:
            filter_counts[split] += 1

    # Check distribution targets
    expected_types = {"truc_tiep": 7, "dien_dat_lai": 3, "dieu_kien_ngoai_le": 5, "metadata_filter": 5}
    if type_counts != expected_types:
        print(f"❌ ERROR: Question type distribution mismatch: {type_counts} vs expected {expected_types}")
        return False

    if split_counts != {"dev": 15, "test": 5}:
        print(f"❌ ERROR: Split distribution mismatch: {split_counts} vs expected {{'dev': 15, 'test': 5}}")
        return False

    if filter_counts != {"dev": 3, "test": 2}:
        print(f"❌ ERROR: Filter distribution mismatch: {filter_counts} vs expected {{'dev': 3, 'test': 2}}")
        return False

    print("✅ Schema, split, and type distribution checks PASSED.")

    # 4. Check PDF content and page mapping
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    failures = 0

    for q in questions:
        qid = q["id"]
        gold_page = q["gold_page"]
        doc_page = q["doc_page"]

        if not (1 <= gold_page <= total_pages):
            print(f"❌ [{qid}] Invalid gold_page {gold_page} (PDF has {total_pages} pages)")
            failures += 1
            continue

        if doc_page != gold_page + 2:
            print(f"❌ [{qid}] Inconsistent page mapping: gold_page={gold_page}, doc_page={doc_page} (expected {gold_page + 2})")
            failures += 1
            continue

        page_text = doc[gold_page - 1].get_text()
        if not check_evidence(q["evidence_quote"], page_text):
            print(f"❌ [{qid}] FAIL: Evidence not found on PDF page {gold_page}")
            print(f"    Evidence snippet: {repr(q['evidence_quote'][:100])}")
            failures += 1
        else:
            print(f"  [{qid}] PASS (Page {gold_page:2d} / Doc {doc_page:2d} | {q['split']:4s} | {q['type']})")

    # 5. Check Parity with artifacts/gold_qa.json
    if ARTIFACTS_GOLD.exists():
        gold_hash = hashlib.md5(gold_path.read_bytes()).hexdigest()
        art_hash = hashlib.md5(ARTIFACTS_GOLD.read_bytes()).hexdigest()
        if gold_hash == art_hash:
            print(f"✅ Parity check PASSED: benchmark and artifacts gold_qa.json are identical ({gold_hash[:8]}).")
        else:
            print(f"⚠️ WARNING: Hash mismatch between {gold_path} and {ARTIFACTS_GOLD}")

    print(f"\nValidation finished: {20 - failures}/20 questions verified against PDF source.")
    return failures == 0


def main():
    parser = argparse.ArgumentParser(description="Validate gold QA dataset against PDF source.")
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD, help="Path to gold_qa.json")
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF, help="Path to source PDF")
    args = parser.parse_args()

    success = validate(args.gold, args.pdf)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
