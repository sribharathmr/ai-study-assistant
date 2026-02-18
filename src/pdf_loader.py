from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    # split into paragraphs
    chunks = text.split("\n\n")
    return chunks
