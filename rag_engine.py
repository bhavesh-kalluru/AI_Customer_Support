import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class RAGEngine:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # embedding size for this model
        self.docs = []

    def add_documents(self, docs):
        self.docs = docs
        embeddings = self.model.encode(docs, convert_to_numpy=True)
        self.index.add(embeddings.astype("float32"))

    def query(self, question, top_k=2):
        q_embed = self.model.encode([question], convert_to_numpy=True).astype("float32")
        D, I = self.index.search(q_embed, top_k)
        results = [self.docs[i] for i in I[0]]
        return results
