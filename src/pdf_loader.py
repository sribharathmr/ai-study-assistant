from pypdf import PdfReader
from src.chunker import chunk_text

def load_pdf(file_path):
    reader = PdfReader(file_path)
    full_text = ""

    for page in reader.pages:
        if page.extract_text():
            full_text += page.extract_text() + " "

    return chunk_text(full_text)
