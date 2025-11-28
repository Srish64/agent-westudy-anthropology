def chunk_text(text: str, chunk_size: int = 400, overlap: int = 80):
    toks = text.split()
    chunks = []
    i = 0
    while i < len(toks):
        chunks.append(" ".join(toks[i:i+chunk_size]))
        i += chunk_size - overlap
    return chunks