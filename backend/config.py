# backend/config.py
import os
from dotenv import load_dotenv

# Load configuration from environment variables or default values.
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'your_openai_api_key')
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', 'your_pinecone_api_key')
PINECONE_ENV = os.environ.get('PINECONE_ENV', 'us-west1-gcp')
PINECONE_INDEX_NAME = os.environ.get('PINECONE_INDEX_NAME', 'medical-compliance-index')

# App settings
DEBUG = os.environ.get('DEBUG', 'true').lower() in ['true', '1', 'yes']
