from typing import List, Dict

def chunk_pages(
        pages: List[Dict],
        chunk_size: int = 500,
        overlap: int =500
) -> List[Dict]:
    """
    Split page texts into overlapping word-based chunks.
    Each chunk keeps a reference to its source page.

    Returns: [{"page": int, "chunk_id": int, "text": str}, ...]
    """

    chunks = []
    chunk_id = 0

    for page in pages:
        words = page["text"].split()
        if not words:
            continue

        step = chunk_size - overlap
        for i in range(0, len(words), step):
            chunk_words = words[i : i + chunk_size]
            if not chunk_words:
                break
            chunks.append({
                "page": page["page"],
                "chunk_id": chunk_id,
                "text": " ".join(chunk_words)
            })
            chunk_id += 1

            if i+chunk_size >= len(words):
                break
        
    return chunks