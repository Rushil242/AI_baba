from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PDF_DIR = DATA_DIR / "pdfs"
VECTOR_DIR = DATA_DIR / "vector_store"

PDF_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_DIR.mkdir(parents=True, exist_ok=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-3.1-flash-lite"   # ✅ FIXED: was "gemini-3.5-flash" (doesn't exist)

APP_TITLE = "AI Fortune Teller"
APP_SUBTITLE = "Zodiac RAG Fortune Studio with Gemini + FAISS"