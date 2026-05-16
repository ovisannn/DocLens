from sentence_transformer import SentenceTransformer
from typing import List
import numpy as py

class embedder:

    _instance = None

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dim = self.model.get_sentence_embedding_dimension()
        pass

    @classmethod
    def get_instance(cls) -> "Embedder":
        if cls._instance is None:
            cls._instance = cls()
            return cls._instance
        
    def encode(self, texts: List[str]) -> np.ndarray:
        """Encode list of texts into normalized embeddings (float32)."""
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return embeddings.astype("float32")

    def encode_one(self, text: str) -> np.ndarray:
        """Encode a single text. Returns 1D vector."""
        return self.encode([text])[0]