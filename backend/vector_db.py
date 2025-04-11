# backend/vector_db.py
import pinecone
from backend.config import PINECONE_API_KEY, PINECONE_ENV, PINECONE_INDEX_NAME

# Initialize the Pinecone environment.
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

def get_index():
    # Connect to the index – create or update as needed.
    if PINECONE_INDEX_NAME not in pinecone.list_indexes():
        # Assume a dimension of 768 (or adjust depending on your embedding model)
        pinecone.create_index(PINECONE_INDEX_NAME, dimension=768)
    return pinecone.Index(PINECONE_INDEX_NAME)

def query_vector(embedding: list, top_k: int = 5):
    index = get_index()
    results = index.query(vector=embedding, top_k=top_k, include_metadata=True)
    return results
