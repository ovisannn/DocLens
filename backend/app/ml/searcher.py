import faiss
import numpy as np
from typing import List, Dict

from app.ml.embedder import Embedder


class Searcher:
    """
    Builds a FAISS index from document chunks and runs semantic search.
    One Searcher instance per uploaded document.
    """

    def __init__(self, chunks: List[Dict]):
        """
        chunks: [{"page": int, "chunk_id": int, "text": str}, ...]
        """
        self.chunks = chunks
        self.embedder = Embedder.get_instance()
        self.index = None
        self._build_index()

    def _build_index(self):
        texts = [c["text"] for c in self.chunks]
        embeddings = self.embedder.encode(texts)

        # IndexFlatIP = inner product. Since embeddings are normalized,
        # this gives cosine similarity.
        self.index = faiss.IndexFlatIP(self.embedder.dim)
        self.index.add(embeddings)

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Returns top_k most relevant chunks for the query.
        Each result: {"page", "chunk_id", "text", "score"}
        """
        query_vec = self.embedder.encode_one(query).reshape(1, -1)
        scores, indices = self.index.search(query_vec, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue
            chunk = self.chunks[idx]
            results.append({
                "page": chunk["page"],
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "score": float(score),
            })

        return results