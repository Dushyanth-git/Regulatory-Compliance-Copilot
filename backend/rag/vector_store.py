import numpy as np

class VectorStore:
    def __init__(self, embeddings, metadata):
        self.embeddings = embeddings
        self.metadata = metadata

    def search(self, query_embedding, k=3):
        scores = np.dot(self.embeddings, query_embedding)
        idx = np.argsort(scores)[::-1][:k]
        return [self.metadata[i] for i in idx]
