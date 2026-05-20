import os
from typing import List
from PyPDF2 import PdfReader

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "pdfs")


def get_pdf_paths() -> List[str]:
    """Return paths to all PDFs already in data/pdfs/"""
    if not os.path.exists(DATA_DIR):
        raise FileNotFoundError(f"PDF directory not found: {DATA_DIR}")

    pdf_files = [
        os.path.join(DATA_DIR, f)
        for f in os.listdir(DATA_DIR)
        if f.endswith(".pdf")
    ]

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in {DATA_DIR}. Please add PDFs to the data/pdfs/ folder."
        )

    return pdf_files


def extract_text_from_pdfs(pdf_paths: List[str] = None) -> List[str]:
    """
    Extract text from all PDFs.
    If pdf_paths is not provided, it auto-loads from data/pdfs/.
    Returns a list of strings, one per PDF.
    """
    if pdf_paths is None:
        pdf_paths = get_pdf_paths()

    texts = []
    for path in pdf_paths:
        try:
            reader = PdfReader(path)
            pages_text = []
            for page in reader.pages:
                page_text = page.extract_text() or ""
                pages_text.append(page_text)
            texts.append("\n".join(pages_text))
        except Exception as e:
            print(f"[pdf_utils] Warning: Could not read {path}: {e}")

    return texts