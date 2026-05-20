import requests
from pypdf import PdfReader
from pathlib import Path
from src.config import PDF_DIR
from src.pdf_sources import PDF_SOURCES

def download_pdfs():
    downloaded = []
    for item in PDF_SOURCES:
        file_path = PDF_DIR / item["name"]
        if not file_path.exists():
            r = requests.get(item["url"], timeout=60)
            r.raise_for_status()
            file_path.write_bytes(r.content)
        downloaded.append(file_path)
    return downloaded

def extract_text_from_pdfs(pdf_paths):
    texts = []
    for path in pdf_paths:
        reader = PdfReader(str(path))
        all_text = []
        for page in reader.pages:
            txt = page.extract_text() or ""
            if txt.strip():
                all_text.append(txt)
        texts.append("\n".join(all_text))
    return texts