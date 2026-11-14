"""Shared data contracts; keep traceability from chunk back to source."""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class DocumentPage:
    document_id: str
    source: str
    page: int          # Physical page in PDF (1 to 31)
    doc_page: int      # Document page number printed on 10-Q (3 to 33)
    section: str       # High-level section (e.g. Notes, MD&A, Financial Statements)
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Chunk:
    chunk_id: str
    document_id: str
    source: str
    page: int
    doc_page: int
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)
