import os
from pathlib import Path
from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env
load_dotenv(BASE_DIR / ".env")

# Paths
DOCS_DIR = BASE_DIR / "data" / "docs"
VECTOR_STORE_DIR = BASE_DIR / "data" / "vector_store"

# Google Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LLM_MODEL = "gemini-2.5-flash"

# Document chunking settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retriever settings
RETRIEVER_K = 4