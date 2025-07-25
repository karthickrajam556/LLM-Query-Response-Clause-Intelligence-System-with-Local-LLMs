import streamlit as st
from backend.loader import load_document
from backend.splitter import chunk_text
from backend.embedder import VectorStore
from backend.retriever import get_top_clauses
from backend.responder import answer_query
import base64
import os

st.set_page_config(page_title="LLM Clause Assistant", layout="wide")

# Banner image loader
def load_image(path):
    with open(path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return f'<img src="data:image/png;base64,{encoded}" width="100%" style="margin-bottom:20px;">'

# Display banner (make sure banner.png is in /assets/)
st.markdown(load_image("assets/banner.png"), unsafe_allow_html=True)

# Sidebar for dark/light toggle
theme = st.sidebar.radio("Choose Theme", ["🌞 Light", "🌙 Dark"])
if theme == "🌙 Dark":
    st.markdown("<style>body { background-color: #1e1e1e; color: white; }</style>", unsafe_allow_html=True)

st.title("📄 LLM-Powered Intelligent Query Assistant")

uploaded_file = st.file_uploader("Upload a document (PDF or DOCX)", type=["pdf", "docx"])
query = st.text_input("🔎 Ask a question about the document:")

# Function to export answer to .txt
def export_response_to_txt(response):
    with open("llm_answer.txt", "w", encoding="utf-8") as f:
        f.write(response)
    with open("llm_answer.txt", "rb") as f:
        st.download_button("📤 Export Answer", f, file_name="LLM_Answer.txt")

if uploaded_file and query:
    with st.spinner("Processing document..."):
        path = f"documents/{uploaded_file.name}"
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        raw_text = load_document(path)
        chunks = chunk_text(raw_text)
        vector_store = VectorStore()
        vector_store.build_index(chunks)
        top_clauses = get_top_clauses(query, chunks, vector_store)
        response = answer_query(query, top_clauses)

        st.subheader("🔍 Most Relevant Clauses")
        for i, clause in enumerate(top_clauses):
            st.markdown(f"**Clause {i+1}** <span title='Relevant to query'>{clause}</span>", unsafe_allow_html=True)

        if response:
            st.subheader("🧠 Answer from LLM")
            st.success(response)
            export_response_to_txt(response)
