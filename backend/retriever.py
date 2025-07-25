from .embedder import VectorStore

def get_top_clauses(query, chunks, vector_store):
    if vector_store.index is None:
        vector_store.build_index(chunks)
    return vector_store.search(query)
