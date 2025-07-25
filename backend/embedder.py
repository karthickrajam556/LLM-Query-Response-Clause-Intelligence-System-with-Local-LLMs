import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load a compact & fast model
model = SentenceTransformer("all-MiniLM-L6-v2")

class VectorStore:
    def __init__(self):
        self.texts = []
        self.embeddings = []
        self.index = None

    def embed_text(self, text):
        embedding = model.encode(text, convert_to_numpy=True)
        return embedding.astype("float32")

    def build_index(self, chunks):
        self.texts = chunks
        self.embeddings = [self.embed_text(c) for c in chunks]
        self.index = faiss.IndexFlatL2(len(self.embeddings[0]))
        self.index.add(np.array(self.embeddings))

    def search(self, query, top_k=3):
        q_embed = self.embed_text(query)
        D, I = self.index.search(np.array([q_embed]), top_k)
        return [self.texts[i] for i in I[0]]
