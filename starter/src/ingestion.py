"""Read and normalize source data using Docling with OCR enabled.

Supports:
- Docling DocumentConverter with RapidOCR + Table Transformer
- Exporting full Markdown corpus (artifacts/parsed_corpus.md, data/parsed_document.md)
- Exporting per-page Markdown files (artifacts/pages_markdown/page_XX.md)
- Caching parsed pages to artifacts/parsed_pages.json
"""
import json
import os
import re
import unicodedata
from pathlib import Path
from typing import List, Optional

try:
    from .models import DocumentPage
except ImportError:
    from starter.src.models import DocumentPage


def normalize_text(text: str) -> str:
    """Normalize Unicode (NFKC), clean table cells, and collapse excess whitespace."""
    if not text:
        return ""
    text = text.replace("\xa0", " ").replace("\u200b", "").replace("\ufeff", "")
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            cleaned_lines.append("")
            continue

        # Table row normalization: compact cell padding
        if line_stripped.startswith("|") and line_stripped.endswith("|"):
            cells = [c.strip() for c in line_stripped.split("|")[1:-1]]
            if all(re.match(r"^-+$", c) for c in cells if c):
                cleaned_lines.append("| " + " | ".join(["---"] * len(cells)) + " |")
            else:
                cleaned_lines.append("| " + " | ".join(cells) + " |")
        else:
            cleaned_lines.append(re.sub(r"[ \t]+", " ", line_stripped))

    cleaned = "\n".join(cleaned_lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def get_section_for_page(page: int) -> str:
    """Assign reliable section metadata based on SEC Form 10-Q structure."""
    if 1 <= page <= 5:
        return "Financial Statements"
    elif 6 <= page <= 16:
        return "Notes to Consolidated Financial Statements"
    elif 17 <= page <= 28:
        return "Management’s Discussion and Analysis"
    elif page == 29:
        return "Market Risk"
    else:
        return "Other Information"


def load_pdf(
    path: Path,
    document_id: str = "netflix-2023q2-10q",
    source: str = "NETFLIX_2023Q2_10Q-3-33.pdf",
    force_reparse: bool = False
) -> List[DocumentPage]:
    """Parse document using Docling (OCR ON + Table Structure) and return DocumentPage list.

    Checks artifacts/parsed_pages.json cache first unless force_reparse=True.
    """
    cache_path = Path("artifacts/parsed_pages.json")
    if cache_path.exists() and not force_reparse:
        print(f"--> [Ingestion] Loading cached parsed pages from {cache_path}...")
        with open(cache_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        pages = [
            DocumentPage(
                document_id=p["document_id"],
                source=p["source"],
                page=p["page"],
                doc_page=p["doc_page"],
                section=p["section"],
                text=p["text"],
                metadata=p.get("metadata", {})
            )
            for p in data
        ]
        print(f"--> [Ingestion] Loaded {len(pages)} pages from cache.")
        return pages

    print(f"--> [Ingestion] Parsing PDF: {path} using Docling (OCR ON + Table Transformer)...")
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True

    converter = DocumentConverter(
        format_options={"pdf": PdfFormatOption(pipeline_options=pipeline_options)}
    )

    conv_res = converter.convert(str(path))
    doc = conv_res.document

    # 1. Export full Markdown
    full_md = doc.export_to_markdown(
        escape_html=False,
        escape_underscores=False,
        page_break_placeholder="\n\n<!-- PAGE_BREAK -->\n\n"
    )
    corpus_header = (
        "# NETFLIX, INC. — Form 10-Q (Q2 2023)\n"
        f"**Parser: Docling (OCR ON + Table Structure)** | Total Pages: {len(doc.pages)}\n\n"
        "---\n\n"
    )
    full_corpus = normalize_text(corpus_header + full_md)
    os.makedirs("artifacts", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    Path("artifacts/parsed_corpus.md").write_text(full_corpus, encoding="utf-8")
    Path("data/parsed_document.md").write_text(full_corpus, encoding="utf-8")

    # 2. Export per-page markdown and build DocumentPage objects
    os.makedirs("artifacts/pages_markdown", exist_ok=True)
    os.makedirs("data/pages_markdown", exist_ok=True)
    pages: List[DocumentPage] = []
    page_numbers = sorted(doc.pages.keys())

    for pno in page_numbers:
        page_md = doc.export_to_markdown(
            page_no=pno,
            escape_html=False,
            escape_underscores=False
        ).strip()
        clean_page_md = normalize_text(page_md)

        page_filename = f"page_{pno:02d}.md"
        page_header = (
            f"<!-- PAGE_START: {pno} (Form 10-Q Page {pno + 2}) -->\n"
            f"## [Trang PDF {pno:02d} / Form 10-Q Trang {pno + 2:02d}] — {get_section_for_page(pno)}\n\n"
        )
        page_content = page_header + clean_page_md + f"\n\n<!-- PAGE_END: {pno} -->\n"
        Path(f"artifacts/pages_markdown/{page_filename}").write_text(page_content, encoding="utf-8")
        Path(f"data/pages_markdown/{page_filename}").write_text(page_content, encoding="utf-8")

        pages.append(
            DocumentPage(
                document_id=document_id,
                source=source,
                page=pno,
                doc_page=pno + 2,
                section=get_section_for_page(pno),
                text=clean_page_md,
                metadata={
                    "parser": "docling_ocr_normalized",
                    "char_length": len(clean_page_md),
                    "page_no": pno
                }
            )
        )

    # 3. Cache JSON
    serializable = [
        {
            "document_id": p.document_id,
            "source": p.source,
            "page": p.page,
            "doc_page": p.doc_page,
            "section": p.section,
            "text": p.text,
            "metadata": p.metadata
        }
        for p in pages
    ]
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=2)
    with open("data/parsed_pages.json", "w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=2)

    print(f"✅ [Ingestion] Successfully parsed {len(pages)} pages with Docling OCR and saved to {cache_path}")
    return pages


if __name__ == "__main__":
    pdf_file = Path("NETFLIX_2023Q2_10Q-3-33.pdf")
    print(f"--> [Test Ingestion] Testing load_pdf on {pdf_file}...")
    loaded_pages = load_pdf(pdf_file)
    print(f"--> Loaded {len(loaded_pages)} pages, total chars: {sum(len(p.text) for p in loaded_pages):,}")

