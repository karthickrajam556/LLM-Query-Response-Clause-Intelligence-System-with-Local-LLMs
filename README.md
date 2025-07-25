# LLM-Query-Response-Clause-Intelligence-System-with-Local-LLMs

# 🧠 LLM Query Response – Intelligent Clause Answering System

LLM Query Response is a local, privacy-preserving document intelligence system that answers user queries based on the contents of PDF or DOCX documents. Built using Python, Streamlit, FAISS, and local LLMs via Ollama, this tool enables natural language interaction with complex documents like policies, contracts, or HR manuals.

---

## 🚀 Features

- 📄 Upload PDF or DOCX documents
- 🔍 Ask questions in natural language
- 📚 Extract, chunk, and embed document content
- 🧠 Retrieve the most relevant clauses using vector similarity
- 💬 Generate clause-specific answers using local LLM (Gemma:2b)
- 🎛️ Streamlit-based interactive user interface
- 💻 100% Local – No API keys, no internet dependency

---

## 🏗️ Project Architecture

[PDF/DOCX Upload]
↓
[Text Extraction]
↓
[Chunking]
↓
[Sentence Embedding]
↓
[FAISS Index]
↓
[Similarity Search (Top Clauses)]
↓
[LLM Query Prompting via Ollama]
↓
[Final Answer]


---

## 🛠️ Technologies Used

- Python
- Streamlit
- FAISS
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Ollama (with `gemma:2b` model)
- PyMuPDF & docx for document parsing

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/llm-query-response.git
cd llm-query-response
2. Install Requirements
Make sure you have Python 3.8+ installed.

bash
Copy
Edit
pip install -r requirements.txt
3. Install & Run Ollama
Download and install Ollama: https://ollama.com/download

Pull the model used (e.g., gemma:2b):

bash
Copy
Edit
ollama pull gemma:2b
4. Run the App
bash
Copy
Edit
streamlit run app.py

