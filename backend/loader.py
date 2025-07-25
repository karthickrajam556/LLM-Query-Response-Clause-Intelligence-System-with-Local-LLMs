import pdfplumber
import docx
import os

def load_pdf_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def load_docx_text(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_document(file_path):
    if file_path.endswith(".pdf"):
        return load_pdf_text(file_path)
    elif file_path.endswith(".docx"):
        return load_docx_text(file_path)
    else:
        raise ValueError("Unsupported file type.")
