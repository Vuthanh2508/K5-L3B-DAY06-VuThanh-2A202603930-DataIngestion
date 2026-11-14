"""Store and search vectors using local Qdrant Vector Store."""
import os
import uuid
from typing import Any, Dict, List, Optional

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    VectorParams,
)
from .models import Chunk


class QdrantVectorStore:
    """Persistent local Qdrant vector store supporting cosine search and metadata filtering.

    Collections:
      - collection_strategy_a (Fixed-size)
      - collection_strategy_b (Recursive)
      - collection_strategy_c (Section-based)
      - collection_strategy_d (Paragraph-based, no filter)
      - collection_strategy_e (Paragraph-based, with metadata filter)
    """

    def __init__(
        self,
        url: Optional[str] = None,
        host: str = "localhost",
        port: int = 6333,
        db_path: str = "./data/qdrant_db",
        dimensions: int = 1024
    ) -> None:
        self.dimensions = dimensions
        self.db_path = db_path
        target_url = url or os.environ.get("QDRANT_URL", f"http://{host}:{port}")
        self.url = target_url
        self.is_server = False

        # Try connecting to Qdrant Docker Server first
        try:
            client = QdrantClient(url=target_url, timeout=5)
            client.get_collections()
            self.client = client
            self.is_server = True
            print(f"✅ [VectorStore] Connected to Qdrant Docker Server at '{target_url}' (dim={self.dimensions})")
        except Exception as e:
            print(f"⚠️ [VectorStore] Qdrant server at '{target_url}' not reachable ({e}).")
            print(f"--> [VectorStore] Falling back to local embedded disk storage at '{self.db_path}'...")
            os.makedirs(db_path, exist_ok=True)
            self.client = QdrantClient(path=self.db_path)
            self.is_server = False
            print(f"✅ [VectorStore] Connected to local embedded Qdrant (dim={self.dimensions})")

    def create_collection(self, strategy: str) -> None:
        """Create or reset collection for a specific ingestion strategy."""
        collection_name = f"collection_{strategy.lower()}"
        if self.client.collection_exists(collection_name):
            print(f"--> [VectorStore] Collection '{collection_name}' already exists. Recreating...")
            self.client.delete_collection(collection_name)

        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=self.dimensions,
                distance=Distance.COSINE
            )
        )
        print(f"✅ [VectorStore] Created collection '{collection_name}' with Cosine metric.")

    def upsert(self, strategy: str, chunks: List[Chunk], vectors: List[List[float]]) -> None:
        """Insert or update chunks with deterministic UUIDs to avoid duplication."""
        if len(chunks) != len(vectors):
            raise ValueError(f"Mismatch: {len(chunks)} chunks vs {len(vectors)} vectors")

        collection_name = f"collection_{strategy.lower()}"
        points = []
        for chunk, vector in zip(chunks, vectors):
            point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, chunk.chunk_id))
            payload = {
                "chunk_id": chunk.chunk_id,
                "document_id": chunk.document_id,
                "source": chunk.source,
                "page": chunk.page,
                "doc_page": chunk.doc_page,
                "section": chunk.metadata.get("section", "Unknown"),
                "text": chunk.text,
                "char_length": len(chunk.text),
                "strategy": strategy
            }
            points.append(PointStruct(id=point_id, vector=vector, payload=payload))

        batch_size = 64
        for i in range(0, len(points), batch_size):
            batch = points[i : i + batch_size]
            self.client.upsert(collection_name=collection_name, points=batch)

        print(f"✅ [VectorStore] Upserted {len(points)} chunks into '{collection_name}'.")

    def search(
        self,
        strategy: str,
        query_vector: List[float],
        top_k: int = 3,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Search top-k chunks by Cosine similarity, with optional metadata filtering."""
        collection_name = f"collection_{strategy.lower()}"
        qdrant_filter = None
        if filters:
            must_conditions = []
            for k, v in filters.items():
                must_conditions.append(FieldCondition(key=k, match=MatchValue(value=v)))
            if must_conditions:
                qdrant_filter = Filter(must=must_conditions)

        search_result = self.client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=top_k,
            query_filter=qdrant_filter
        )

        results: List[Dict[str, Any]] = []
        for pt in search_result.points:
            results.append({
                "chunk_id": pt.payload.get("chunk_id"),
                "score": round(pt.score, 4),
                "page": pt.payload.get("page"),
                "doc_page": pt.payload.get("doc_page"),
                "section": pt.payload.get("section"),
                "text": pt.payload.get("text"),
                "source": pt.payload.get("source"),
                "metadata": pt.payload
            })
        return results

    def close(self) -> None:
        """Close Qdrant client connection cleanly."""
        try:
            self.client.close()
        except Exception:
            pass
