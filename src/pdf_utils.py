import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "pdfs")

def get_pdf_paths():
    """Return paths to all PDFs already in data/pdfs/"""
    pdf_files = [
        os.path.join(DATA_DIR, f)
        for f in os.listdir(DATA_DIR)
        if f.endswith(".pdf")
    ]
    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in {DATA_DIR}. Please add PDFs to the data/pdfs/ folder.")
    return pdf_files