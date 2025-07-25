import re

def chunk_text(text, max_words=80):
    paragraphs = re.split(r'\n+', text)
    chunks = []
    for para in paragraphs:
        if len(para.split()) > 5:
            chunks.append(para.strip())
    return chunks
