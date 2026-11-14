"""Embedding provider implementation using BGE-M3."""
import time
from typing import List, Protocol
import torch


class Embedder(Protocol):
    model_name: str
    dimensions: int

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Return one vector per input text, in the same order."""
        ...

    def embed_query(self, question: str) -> List[float]:
        """Return a query vector compatible with the stored document vectors."""
        ...


class BGEM3Embedder:
    """Production BGE-M3 embedder using FlagEmbedding with GPU acceleration."""

    def __init__(self, model_name: str = "BAAI/bge-m3", device: str | None = None) -> None:
        self.model_name = model_name
        self.dimensions = 1024

        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        print(f"--> [Embedder] Initializing {self.model_name} on device='{self.device}' (FP16={self.device=='cuda'})...")
        t0 = time.time()
        from FlagEmbedding import BGEM3FlagModel

        self.model = BGEM3FlagModel(
            self.model_name,
            use_fp16=(self.device == "cuda"),
            devices=self.device
        )
        print(f"✅ [Embedder] {self.model_name} ready in {round(time.time() - t0, 2)}s (dim={self.dimensions})")

    def embed_documents(self, texts: List[str], batch_size: int = 16) -> List[List[float]]:
        """Encode a batch of documents into dense 1024-dim vectors with GPU memory management."""
        if not texts:
            return []
        if self.device == "cuda" and torch.cuda.is_available():
            torch.cuda.empty_cache()
        res = self.model.encode(
            texts,
            batch_size=batch_size,
            max_length=512,
            return_dense=True
        )
        dense_vecs = res["dense_vecs"]
        if self.device == "cuda" and torch.cuda.is_available():
            torch.cuda.empty_cache()
        # Convert numpy to list of float lists
        return [vec.tolist() for vec in dense_vecs]

    def embed_query(self, question: str) -> List[float]:
        """Encode a single query string into a dense 1024-dim vector."""
        res = self.model.encode(
            [question],
            batch_size=1,
            max_length=512,
            return_dense=True
        )
        return res["dense_vecs"][0].tolist()
