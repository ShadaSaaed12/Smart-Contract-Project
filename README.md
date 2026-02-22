# 📄 Smart Contract Summary & Q&A Assistant

## 📌 Project Overview

Smart Contract Summary & Q&A Assistant is a Retrieval-Augmented Generation (RAG) based web application that allows users to upload contract documents (PDF/DOCX) and interact with them through a conversational interface.

The system extracts text from uploaded documents, processes and embeds the content into a vector database, and enables users to ask questions grounded in the uploaded document. The assistant generates answers with contextual awareness based only on the provided file.

---

## 🎯 Project Objectives

- Demonstrate understanding of LLM inference workflows  
- Build an end-to-end RAG (Retrieval-Augmented Generation) pipeline  
- Implement document ingestion and semantic search  
- Integrate vector databases for similarity retrieval  
- Expose the system as an API using LangServe  
- Provide a user-friendly interface using Gradio  

---

## 🏗 System Architecture

User → Gradio UI → LangServe API → RetrievalQA Chain → Vector Store → LLM → Response  

### 🔹 Main Components

- Frontend: Gradio (Upload & Chat Interface)  
- Backend: FastAPI + LangServe  
- Pipeline: Document ingestion + RetrievalQA  
- Vector Store: Chroma (or FAISS)  
- LLM: OpenAI Chat Model  
- Embeddings: OpenAI Embeddings  

---

## ⚙️ Technologies Used

- Python  
- LangChain  
- LangServe  
- FastAPI  
- Gradio  
- Chroma (Vector Database)  
- OpenAI API  
- PyPDF / document loaders  

---

## 🔄 How the System Works

1️⃣ User uploads a contract (PDF)  
2️⃣ The document is parsed and converted to text  
3️⃣ Text is split into smaller chunks  
4️⃣ Chunks are converted into embeddings  
5️⃣ Embeddings are stored in a vector database  
6️⃣ User submits a question  
7️⃣ The system retrieves the most relevant document chunks  
8️⃣ The LLM generates an answer based on retrieved context  
9️⃣ The response is displayed in the chat interface  

---

## 📂 Project Structure
smart_contract_assistant/
│
├── ingestion.py      # Handles PDF loading, chunking, and embedding
├── chain.py          # Builds RetrievalQA chain
├── server.py         # Exposes the chain via LangServe API
├── ui.py             # Gradio user interface
├── requirements.txt  # Dependencies
└── README.md         # Project documentation

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
pip install langchain langserve fastapi uvicorn gradio chromadb pypdf openai

---

### 2️⃣ Set OpenAI API Key (Windows)
setx OPENAI_API_KEY "your_api_key_here"

Restart terminal after setting the key.

---

### 3️⃣ Run Ingestion

Place your contract file in the project folder and run:
python run_ingest.py

This creates the vector database.

---

### 4️⃣ Start Backend Server
python server.py

---

### 5️⃣ Launch Gradio UI

Open a new terminal:
python ui.py

Open the provided link in your browser.

---

## 📊 Evaluation

### 📈 Metrics Considered

- Relevance of retrieved chunks  
- Answer grounding in document  
- Response latency (< 5 seconds for medium contracts)  

### ⚠️ Limitations

- Supports English documents only  
- Depends on OpenAI API availability  
- Large documents may increase processing time  
- Not production-grade deployment  

---

## 🚀 Future Enhancements

- Multi-document support  
- Local LLM integration  
- Role-based access control  
- Cloud deployment (Docker/Kubernetes)  
- Improved evaluation metrics
