# backend/utils.py
import openai
from backend.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_embedding(text: str) -> list:
    """Generate vector embedding for text using OpenAI."""
    # Adjust parameters based on your embedding model
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    embedding = response['data'][0]['embedding']
    return embedding


def preprocess_text(text: str) -> str:
    """Preprocess the text, e.g., lowercasing, removing extra whitespace."""
    return " ".join(text.lower().strip().split())