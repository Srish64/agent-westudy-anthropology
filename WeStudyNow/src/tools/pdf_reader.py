import pdfplumber
from pathlib import Path
from typing import Optional

def extract_text_from_pdf_path(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    text_pages = []
    with pdfplumber.open(str(p)) as pdf:
        for page in pdf.pages:
            text_pages.append(page.extract_text() or "")
    return "\n\n".join(text_pages)