import os
from src.pdf_loader import load_pdf

def load_all_notes(folder_path="data/notes"):
    documents = []

    for file in os.listdir(folder_path):

        path = os.path.join(folder_path, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                documents.extend(f.read().split("\n\n"))

        elif file.endswith(".pdf"):
            documents.extend(load_pdf(path))

    return documents
