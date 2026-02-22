"""
Smart Contract Assistant - Document Ingestion
Loads documents from the docs folder, splits them into chunks,
and stores them in a FAISS vector store using Google Gemini embeddings.
"""

from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import DOCS_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from app.vector_store import create_vector_store


# Supported file types and their loaders
LOADER_MAP = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
    ".md": TextLoader,   # Markdown files loaded as plain text
    ".sol": TextLoader,  # Solidity files loaded as plain text
}


def ingest() -> int:
    """
    Load all supported documents from DOCS_DIR, split into chunks,
    and store in the FAISS vector store.

    Returns:
        int: Number of chunks created and stored.
    """
    docs_path = Path(DOCS_DIR)
    if not docs_path.exists():
        raise FileNotFoundError(
            f"Documents directory not found: {DOCS_DIR}\n"
            "Please create it and add your documents."
        )

    all_documents = []

    for file_path in sorted(docs_path.iterdir()):
        if not file_path.is_file():
            continue

        ext = file_path.suffix.lower()
        loader_class = LOADER_MAP.get(ext)

        if loader_class is None:
            print(f"⚠️ Skipping unsupported file: {file_path.name}")
            continue

        try:
            loader = loader_class(str(file_path))
            documents = loader.load()
            all_documents.extend(documents)
            print(f"📄 Loaded: {file_path.name} ({len(documents)} page(s))")
        except Exception as e:
            print(f"❌ Error loading {file_path.name}: {e}")

    if not all_documents:
        raise ValueError(
            "No documents were loaded. "
            "Please add .pdf, .txt, .md, or .sol files to the docs folder."
        )

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(all_documents)
    print(f"✂️ Split into {len(chunks)} chunks")

    # Store in FAISS vector store
    create_vector_store(chunks)

    return len(chunks)