import fitz  # PyMuPDF
from typing import List, Dict


def extract_text_from_pdf(file_bytes: bytes) -> List[Dict]:
    """
    Extract text from PDF bytes, page by page.
    Returns a list of dicts: [{"page": int, "text": str}, ...]
    """
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    pages = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()
        if text:
            pages.append({"page": page_num, "text": text})

    doc.close()
    return pages


def extract_full_text(file_bytes: bytes) -> str:
    """Concatenate all page text into one string (used for classification)."""
    pages = extract_text_from_pdf(file_bytes)
    return "\n\n".join(p["text"] for p in pages)
