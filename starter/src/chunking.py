"""Implement 5 Token-Based Chunking Strategies for Day 06 Data Ingestion Engineering.

All chunking strategies utilize the BAAI/bge-m3 tokenizer for precise token boundary alignment:
- Strategy A: Fixed-size token windows (500 tokens, overlap 50)
- Strategy B: Recursive token chunking (separators [\\n\\n, \\n, . , ' '], max 500 tokens, overlap 50)
- Strategy C: Section-based token chunking (aligned with SEC Form 10-Q Notes/Items, max 500 tokens, overlap 50)
- Strategy D: Paragraph-based token chunking (natural paragraphs and tables, max 500 tokens, overlap 50, no filter)
- Strategy E: Paragraph-based token chunking + Metadata Filter (max 500 tokens, overlap 50, filter by 'section')
"""
import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from .models import Chunk, DocumentPage
except ImportError:
    from starter.src.models import DocumentPage, Chunk

# Lazy-loaded BGE-M3 Tokenizer instance
_TOKENIZER = None


def get_tokenizer():
    """Retrieve or initialize cached HuggingFace tokenizer for BAAI/bge-m3."""
    global _TOKENIZER
    if _TOKENIZER is None:
        from transformers import AutoTokenizer
        try:
            _TOKENIZER = AutoTokenizer.from_pretrained("BAAI/bge-m3", local_files_only=True)
        except Exception:
            _TOKENIZER = AutoTokenizer.from_pretrained("BAAI/bge-m3")
    return _TOKENIZER


def get_tokens(text: str) -> List[int]:
    """Encode string into token IDs without special tokens."""
    if not text:
        return []
    tokenizer = get_tokenizer()
    return tokenizer.encode(text, add_special_tokens=False)


def decode_tokens(tokens: List[int]) -> str:
    """Decode token IDs back into string without special tokens."""
    if not tokens:
        return ""
    tokenizer = get_tokenizer()
    return tokenizer.decode(tokens, skip_special_tokens=True).strip()


def count_tokens(text: str) -> int:
    """Count exact BGE-M3 tokens for a string."""
    return len(get_tokens(text))


# ==============================================================================
# STRATEGY A: Fixed Token Window Chunking
# ==============================================================================
def fixed_token_chunking(
    page: DocumentPage,
    token_size: int = 500,
    overlap: int = 50,
    strategy: str = "strategy_a"
) -> List[Chunk]:
    """Strategy A: Split text into fixed token windows using BGE-M3 tokenizer."""
    tokens = get_tokens(page.text)
    if not tokens:
        return []

    chunks: List[Chunk] = []
    step = token_size - overlap if token_size > overlap else token_size
    start = 0
    idx = 0

    while start < len(tokens):
        end = min(start + token_size, len(tokens))
        c_toks = tokens[start:end]
        c_text = decode_tokens(c_toks)
        if c_text:
            chunk_id = f"stra_p{page.page:02d}_{idx:03d}"
            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    document_id=page.document_id,
                    source=page.source,
                    page=page.page,
                    doc_page=page.doc_page,
                    text=c_text,
                    metadata={
                        "strategy": strategy,
                        "document_id": page.document_id,
                        "source": page.source,
                        "page": page.page,
                        "doc_page": page.doc_page,
                        "section": page.section,
                        "token_count": len(c_toks),
                        "char_length": len(c_text),
                        "chunk_index": idx
                    }
                )
            )
            idx += 1
        if end >= len(tokens):
            break
        start += step

    return chunks


# Alias for backward compatibility
fixed_size = fixed_token_chunking


# ==============================================================================
# STRATEGY B: Recursive Token Chunking
# ==============================================================================
def _split_recursive_tokens(
    text: str,
    max_tokens: int,
    overlap_tokens: int,
    separators: List[str]
) -> List[str]:
    """Helper for recursive splitting bounded by token budget."""
    curr_tokens = count_tokens(text)
    if curr_tokens <= max_tokens:
        return [text]

    chosen_sep = ""
    for sep in separators:
        if sep == "":
            chosen_sep = ""
            break
        if sep in text:
            chosen_sep = sep
            break

    if chosen_sep != "":
        splits = text.split(chosen_sep)
    else:
        # Fall back to token slicing
        tokens = get_tokens(text)
        step = max_tokens - overlap_tokens if max_tokens > overlap_tokens else max_tokens
        return [decode_tokens(tokens[i : i + max_tokens]) for i in range(0, len(tokens), step)]

    recombined: List[str] = []
    current_piece: List[str] = []
    current_tokens = 0
    remaining_seps = separators[separators.index(chosen_sep) + 1 :] if chosen_sep in separators else [""]

    for s in splits:
        if not s.strip():
            continue
        s_tokens = count_tokens(s)
        if s_tokens > max_tokens and remaining_seps:
            if current_piece:
                recombined.append(chosen_sep.join(current_piece).strip())
                current_piece = []
                current_tokens = 0
            sub_splits = _split_recursive_tokens(s, max_tokens, overlap_tokens, remaining_seps)
            recombined.extend(sub_splits)
        elif current_tokens + s_tokens > max_tokens:
            if current_piece:
                recombined.append(chosen_sep.join(current_piece).strip())
                current_piece = [s]
                current_tokens = s_tokens
            else:
                recombined.append(s.strip())
        else:
            current_piece.append(s)
            current_tokens += s_tokens

    if current_piece:
        recombined.append(chosen_sep.join(current_piece).strip())

    return [r for r in recombined if r.strip()]


def recursive_token_chunking(
    page: DocumentPage,
    chunk_size: int = 500,
    overlap: int = 50,
    strategy: str = "strategy_b"
) -> List[Chunk]:
    """Strategy B: Recursive token chunking using hierarchical separators bounded by max_tokens."""
    text = page.text
    if not text:
        return []

    separators = ["\n\n", "\n", ". ", " ", ""]
    raw_pieces = _split_recursive_tokens(text, max_tokens=chunk_size, overlap_tokens=overlap, separators=separators)

    chunks: List[Chunk] = []
    for idx, piece in enumerate(raw_pieces):
        tok_cnt = count_tokens(piece)
        chunk_id = f"strb_p{page.page:02d}_{idx:03d}"
        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                document_id=page.document_id,
                source=page.source,
                page=page.page,
                doc_page=page.doc_page,
                text=piece,
                metadata={
                    "strategy": strategy,
                    "document_id": page.document_id,
                    "source": page.source,
                    "page": page.page,
                    "doc_page": page.doc_page,
                    "section": page.section,
                    "token_count": tok_cnt,
                    "char_length": len(piece),
                    "chunk_index": idx
                }
            )
        )
    return chunks


# Alias for backward compatibility
recursive_chunking = recursive_token_chunking


# ==============================================================================
# STRATEGY C: Section-Based Token Chunking
# ==============================================================================
def section_token_chunking(
    page: DocumentPage,
    max_size: int = 500,
    overlap: int = 50,
    strategy: str = "strategy_c"
) -> List[Chunk]:
    """Strategy C: Section-based chunking aligned with Note, Item, and Header boundaries, bounded by tokens."""
    text = page.text
    if not text:
        return []

    header_regex = re.compile(
        r"(?=(?:\n|^)(?:Note \d+|Item \d+|Part [I|V|X]+|Consolidated Statements|### Tables|[A-Z][A-Za-z\s]{3,30}:))",
        re.MULTILINE
    )
    raw_sections = [s.strip() for s in header_regex.split(text) if s.strip()]
    if not raw_sections:
        raw_sections = [text]

    chunks: List[Chunk] = []
    idx = 0
    current_block: List[str] = []
    current_tokens = 0

    def flush_block(parts: List[str]):
        nonlocal idx
        joined = "\n\n".join(parts).strip()
        if not joined:
            return
        tok_cnt = count_tokens(joined)
        chunk_id = f"strc_p{page.page:02d}_{idx:03d}"
        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                document_id=page.document_id,
                source=page.source,
                page=page.page,
                doc_page=page.doc_page,
                text=joined,
                metadata={
                    "strategy": strategy,
                    "document_id": page.document_id,
                    "source": page.source,
                    "page": page.page,
                    "doc_page": page.doc_page,
                    "section": page.section,
                    "token_count": tok_cnt,
                    "char_length": len(joined),
                    "chunk_index": idx
                }
            )
        )
        idx += 1

    for sec in raw_sections:
        sec_tokens = count_tokens(sec)
        if sec_tokens > max_size:
            if current_block:
                flush_block(current_block)
                current_block = []
                current_tokens = 0
            # Token window slice oversized section
            s_toks = get_tokens(sec)
            step = max_size - overlap if max_size > overlap else max_size
            start = 0
            while start < len(s_toks):
                end = min(start + max_size, len(s_toks))
                flush_block([decode_tokens(s_toks[start:end])])
                if end >= len(s_toks):
                    break
                start += step
        elif current_tokens + sec_tokens > max_size:
            flush_block(current_block)
            current_block = [sec]
            current_tokens = sec_tokens
        else:
            current_block.append(sec)
            current_tokens += sec_tokens

    if current_block:
        flush_block(current_block)

    return chunks


# Alias for backward compatibility
section_chunking = section_token_chunking


# ==============================================================================
# STRATEGY D & E: Paragraph-Based Token Chunking
# ==============================================================================
def paragraph_token_chunking(
    page: DocumentPage,
    max_size: int = 500,
    overlap: int = 50,
    strategy: str = "strategy_d"
) -> List[Chunk]:
    """Strategy D (No Filter) & Strategy E (With Metadata Filter): Group paragraphs bounded by token budget."""
    raw_text = page.text
    if not raw_text:
        return []

    raw_paras = [p.strip() for p in raw_text.split("\n\n") if p.strip()]
    if not raw_paras:
        raw_paras = [raw_text]

    chunks: List[Chunk] = []
    idx = 0
    current_block: List[str] = []
    current_tokens = 0
    prefix = "strd" if strategy == "strategy_d" else "stre"

    def flush_paras(paras: List[str]):
        nonlocal idx
        joined = "\n\n".join(paras).strip()
        if not joined:
            return
        tok_cnt = count_tokens(joined)
        chunk_id = f"{prefix}_p{page.page:02d}_{idx:03d}"
        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                document_id=page.document_id,
                source=page.source,
                page=page.page,
                doc_page=page.doc_page,
                text=joined,
                metadata={
                    "strategy": strategy,
                    "document_id": page.document_id,
                    "source": page.source,
                    "page": page.page,
                    "doc_page": page.doc_page,
                    "section": page.section,
                    "token_count": tok_cnt,
                    "char_length": len(joined),
                    "chunk_index": idx
                }
            )
        )
        idx += 1

    for para in raw_paras:
        p_toks = count_tokens(para)
        if p_toks > max_size:
            if current_block:
                flush_paras(current_block)
                current_block = []
                current_tokens = 0
            tokens = get_tokens(para)
            step = max_size - overlap if max_size > overlap else max_size
            start = 0
            while start < len(tokens):
                end = min(start + max_size, len(tokens))
                flush_paras([decode_tokens(tokens[start:end])])
                if end >= len(tokens):
                    break
                start += step
        elif current_tokens + p_toks > max_size:
            flush_paras(current_block)
            current_block = [para]
            current_tokens = p_toks
        else:
            current_block.append(para)
            current_tokens += p_toks

    if current_block:
        flush_paras(current_block)

    return chunks


# Alias for backward compatibility
by_paragraph = paragraph_token_chunking


# ==============================================================================
# PIPELINE INTEGRATION: Execute All 5 Chunking Strategies & Export Artifacts
# ==============================================================================
def run_all_chunking(
    pages: List[DocumentPage],
    export_artifacts: bool = True
) -> Dict[str, List[Chunk]]:
    """Execute all 5 token-based chunking strategies across pages.

    Exports:
    - artifacts/chunks/chunks_strategy_[a-e].json
    - artifacts/chunks_markdown/strategy_[a-e]*.md & README.md
    - artifacts/chunking_summary.json
    - artifacts/CHUNKING_REPORT.md
    """
    t0 = time.time()
    print("--> [Chunking] Executing 5 Token-Based chunking strategies (BGE-M3 Tokenizer)...")

    # Preload tokenizer once
    get_tokenizer()

    # 1. Generate chunks
    chunks_a = []
    chunks_b = []
    chunks_c = []
    chunks_d = []
    chunks_e = []

    for p in pages:
        chunks_a.extend(fixed_token_chunking(p, token_size=500, overlap=50, strategy="strategy_a"))
        chunks_b.extend(recursive_token_chunking(p, chunk_size=500, overlap=50, strategy="strategy_b"))
        chunks_c.extend(section_token_chunking(p, max_size=500, overlap=50, strategy="strategy_c"))
        chunks_d.extend(paragraph_token_chunking(p, max_size=500, overlap=50, strategy="strategy_d"))
        chunks_e.extend(paragraph_token_chunking(p, max_size=500, overlap=50, strategy="strategy_e"))

    chunk_time = round(time.time() - t0, 2)
    print(f"⏱️ [Chunking] Created token chunks (max 500 tokens, overlap 50) in {chunk_time}s:")
    print(f"   - Strategy A (Fixed 500 tokens): {len(chunks_a)} chunks")
    print(f"   - Strategy B (Recursive 500 tokens): {len(chunks_b)} chunks")
    print(f"   - Strategy C (Section max 500 tokens): {len(chunks_c)} chunks")
    print(f"   - Strategy D (Paragraph max 500 tokens - No Filter): {len(chunks_d)} chunks")
    print(f"   - Strategy E (Paragraph max 500 tokens - With Filter): {len(chunks_e)} chunks")

    result = {
        "A": chunks_a,
        "B": chunks_b,
        "C": chunks_c,
        "D": chunks_d,
        "E": chunks_e,
    }

    if not export_artifacts:
        return result

    # 2. Export Artifacts
    os.makedirs("artifacts/chunks", exist_ok=True)
    os.makedirs("data/chunks", exist_ok=True)
    os.makedirs("artifacts/chunks_markdown", exist_ok=True)
    os.makedirs("data/chunks_markdown", exist_ok=True)

    configs = {
        "A": {
            "name": "Strategy A: Fixed-Size Token Window",
            "desc": "Cửa sổ trượt cố định 500 tokens, overlap 50 tokens, định biên chính xác theo BGE-M3 Tokenizer.",
            "params": {"token_size": 500, "overlap": 50},
            "json_file": "chunks_strategy_a.json",
            "md_file": "strategy_a_fixed.md",
            "chunks": chunks_a
        },
        "B": {
            "name": "Strategy B: Recursive Token Chunking",
            "desc": "Phân chia đệ quy theo thứ tự phân cấp [\\n\\n, \\n, . , ' '], giới hạn 500 tokens, overlap 50 tokens.",
            "params": {"max_tokens": 500, "overlap": 50, "separators": ["\\n\\n", "\\n", ". ", " "]},
            "json_file": "chunks_strategy_b.json",
            "md_file": "strategy_b_recursive.md",
            "chunks": chunks_b
        },
        "C": {
            "name": "Strategy C: Section-Based Token Chunking",
            "desc": "Cắt theo ranh giới Section/Note/Item của SEC Form 10-Q, trần tối đa 500 tokens, overlap 50 tokens.",
            "params": {"max_tokens": 500, "overlap": 50, "header_boundary_aware": True},
            "json_file": "chunks_strategy_c.json",
            "md_file": "strategy_c_section.md",
            "chunks": chunks_c
        },
        "D": {
            "name": "Strategy D: Paragraph-Based Token Chunking (No Filter)",
            "desc": "Nhóm theo đoạn văn bản tự nhiên (\\n\\n) và bảng biểu, tối đa 500 tokens, overlap 50 tokens, không lọc.",
            "params": {"max_tokens": 500, "overlap": 50, "filter": False},
            "json_file": "chunks_strategy_d.json",
            "md_file": "strategy_d_paragraph.md",
            "chunks": chunks_d
        },
        "E": {
            "name": "Strategy E: Paragraph-Based Token Chunking + Metadata Filter",
            "desc": "Nhóm theo đoạn văn bản tự nhiên tối đa 500 tokens, overlap 50 tokens, kết hợp bộ lọc metadata section trên Qdrant.",
            "params": {"max_tokens": 500, "overlap": 50, "filter": True, "filter_field": "section"},
            "json_file": "chunks_strategy_e.json",
            "md_file": "strategy_e_paragraph_filter.md",
            "chunks": chunks_e
        }
    }

    # Load Gold QA if available
    gold_qa = []
    gold_path = Path("benchmark/gold_qa.json")
    if gold_path.exists():
        try:
            with open(gold_path, "r", encoding="utf-8") as f:
                gold_qa = json.load(f)
        except Exception:
            gold_qa = []

    try:
        from .evaluation import is_chunk_hit
    except ImportError:
        try:
            from starter.src.evaluation import is_chunk_hit
        except ImportError:
            is_chunk_hit = None

    summary_stats = {}
    report_lines = [
        "# Báo cáo Phân Tích Thực Nghiệm 5 Chiến Lược Token-Based Chunking (BGE-M3)",
        f"**Thời gian sinh:** {time.strftime('%Y-%m-%d %H:%M:%S')} | **Trang nguồn:** {len(pages)} | **Tổng ký tự chuẩn hóa:** {sum(len(p.text) for p in pages):,}\n",
        "---",
        "## 1. Bảng So Sánh Tổng Hợp 5 Chiến Lược Token\n",
        "| Chiến lược | Thuật toán & Tham số | Số Chunks | Tokens Min/Max/TB | Ký tự Min/Max/TB | Độ phủ Evidence Gold (20 câu) | Tệp Chunk JSON | Tệp Markdown Trực Quan |",
        "|---|---|:---:|:---:|:---:|:---:|---|---|"
    ]

    readme_markdown_lines = [
        "# Thư Mục Các Bản Markdown Tách Theo Chunk (5 Cấu Hình Token BGE-M3)",
        "Tài liệu văn bản **Netflix Form 10-Q (Q2 2023)** sau khi chuẩn hóa khoảng trắng, được tách theo Tokenizer của BGE-M3.\n",
        "| Tệp Markdown | Chiến Lược | Thuật toán & Tham số | Số Chunks | Độ dài Tokens (TB) | Độ dài Ký tự (TB) |",
        "|---|---|---|:---:|:---:|:---:|"
    ]

    for key, data in configs.items():
        ch_list = data["chunks"]
        tok_lens = [c.metadata.get("token_count", 0) for c in ch_list]
        char_lens = [c.metadata.get("char_length", 0) for c in ch_list]

        avg_tok = round(sum(tok_lens) / len(tok_lens), 1) if tok_lens else 0
        min_tok = min(tok_lens) if tok_lens else 0
        max_tok = max(tok_lens) if tok_lens else 0

        avg_char = round(sum(char_lens) / len(char_lens), 1) if char_lens else 0
        min_char = min(char_lens) if char_lens else 0
        max_char = max(char_lens) if char_lens else 0

        # Evidence coverage
        covered = 0
        missed_ids = []
        if is_chunk_hit and gold_qa:
            for q in gold_qa:
                hit = any(is_chunk_hit(q, {"page": c.page, "doc_page": c.doc_page, "text": c.text}) for c in ch_list)
                if hit:
                    covered += 1
                else:
                    missed_ids.append(q["id"])
            cov_pct = round(covered / len(gold_qa) * 100, 1)
            coverage_str = f"{covered}/{len(gold_qa)} ({cov_pct}%)"
        else:
            coverage_str = "N/A"
            cov_pct = 0.0

        # Save JSON
        serializable = [
            {
                "chunk_id": c.chunk_id,
                "document_id": c.document_id,
                "source": c.source,
                "page": c.page,
                "doc_page": c.doc_page,
                "text": c.text,
                "metadata": c.metadata
            }
            for c in ch_list
        ]
        with open(f"artifacts/chunks/{data['json_file']}", "w", encoding="utf-8") as f:
            json.dump(serializable, f, ensure_ascii=False, indent=2)
        with open(f"data/chunks/{data['json_file']}", "w", encoding="utf-8") as f:
            json.dump(serializable, f, ensure_ascii=False, indent=2)

        # Save Markdown visual file
        md_lines = [
            f"# [{data['name']}] Văn Bản Báo Cáo Netflix Form 10-Q Tách Theo Chunks",
            f"> **Tài liệu nguồn:** `NETFLIX_2023Q2_10Q-3-33.pdf` (31 trang nội dung chuẩn hóa)",
            f"> **Thuật toán & Tham số Token:** `{data['params']}`",
            f"> **Mô tả:** {data['desc']}",
            f"> **Thống kê:** Tổng cộng **{len(ch_list)} chunks** | Tokens: Min {min_tok} - Max {max_tok} - TB {avg_tok} | Ký tự: Min {min_char} - Max {max_char} - TB {avg_char}",
            "",
            "---",
            ""
        ]
        curr_page = None
        for idx, c in enumerate(ch_list, 1):
            if c.page != curr_page:
                curr_page = c.page
                md_lines.append(f"\n# 📄 [Trang PDF {c.page:02d} / Form 10-Q Trang {c.doc_page:02d}] — Mục: *{c.metadata.get('section', '')}*\n")
            md_lines.append(f"### 🔹 [Chunk {idx:03d}/{len(ch_list):03d}] `{c.chunk_id}` | Trang PDF: {c.page:02d} (Doc Page: {c.doc_page:02d}) | {c.metadata.get('token_count', 0)} tokens ({c.metadata.get('char_length', 0)} ký tự)")
            md_lines.append(f"> **Metadata:** `section = \"{c.metadata.get('section', '')}\"` | `tokens = {c.metadata.get('token_count', 0)}` | `strategy = \"{c.metadata.get('strategy', '')}\"`\n")
            md_lines.append("```markdown")
            md_lines.append(c.text)
            md_lines.append("```\n")
            md_lines.append("---\n")

        md_content = "\n".join(md_lines)
        Path(f"artifacts/chunks_markdown/{data['md_file']}").write_text(md_content, encoding="utf-8")
        Path(f"data/chunks_markdown/{data['md_file']}").write_text(md_content, encoding="utf-8")

        summary_stats[key] = {
            "name": data["name"],
            "params": data["params"],
            "chunk_count": len(ch_list),
            "tokens": {"min": min_tok, "max": max_tok, "avg": avg_tok},
            "chars": {"min": min_char, "max": max_char, "avg": avg_char},
            "gold_coverage": coverage_str,
            "gold_coverage_pct": cov_pct,
            "missed_question_ids": missed_ids
        }

        report_lines.append(
            f"| **{data['name']}** | `{data['params']}` | **{len(ch_list)}** | {min_tok}/{max_tok}/{avg_tok} | {min_char}/{max_char}/{avg_char} | **{coverage_str}** | [`{data['json_file']}`](file:///c:/HUST/VIN/lab6/K5-L3-Day06-DataIngestionEngineering/artifacts/chunks/{data['json_file']}) | [`{data['md_file']}`](file:///c:/HUST/VIN/lab6/K5-L3-Day06-DataIngestionEngineering/artifacts/chunks_markdown/{data['md_file']}) |"
        )
        readme_markdown_lines.append(
            f"| [`{data['md_file']}`](./{data['md_file']}) | **{data['name']}** | `{data['params']}` | **{len(ch_list)}** | {avg_tok} tokens | {avg_char} ký tự |"
        )

        print(f"  ✓ {data['name']}: {len(ch_list)} chunks (TB {avg_tok} tokens / {avg_char} chars) - Coverage {coverage_str}")

    report_text = "\n".join(report_lines)
    readme_text = "\n".join(readme_markdown_lines)
    Path("artifacts/CHUNKING_REPORT.md").write_text(report_text, encoding="utf-8")
    Path("data/CHUNKING_REPORT.md").write_text(report_text, encoding="utf-8")
    Path("artifacts/chunks_markdown/README.md").write_text(readme_text, encoding="utf-8")
    Path("data/chunks_markdown/README.md").write_text(readme_text, encoding="utf-8")
    with open("artifacts/chunking_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_stats, f, ensure_ascii=False, indent=2)
    with open("data/chunking_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_stats, f, ensure_ascii=False, indent=2)

    print("✅ [Chunking] Successfully exported Token-Based JSON chunks, Markdown views, and Chunking Report.")
    return result


if __name__ == "__main__":
    from pathlib import Path
    try:
        from .ingestion import load_pdf
    except ImportError:
        from starter.src.ingestion import load_pdf

    pdf_file = Path("NETFLIX_2023Q2_10Q-3-33.pdf")
    loaded_pages = load_pdf(pdf_file)
    run_all_chunking(loaded_pages, export_artifacts=True)
