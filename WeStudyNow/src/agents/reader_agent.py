from pathlib import Path
from src.tools.pdf_reader import extract_text_from_pdf_path
from src.utils.cleaning import clean_text
from src.utils.chunking import chunk_text
from src.tools.embeddings import embed_texts
import logging

log = logging.getLogger(__name__)

class ReaderAgent:
    def __init__(self):
        pass

    def read_and_chunk(self, pdf_path: str, chunk_size:int=400, overlap:int=80):
        log.info("ReaderAgent: reading PDF %s", pdf_path)
        raw = extract_text_from_pdf_path(pdf_path)
        cleaned = clean_text(raw)
        chunks = chunk_text(cleaned, chunk_size=chunk_size, overlap=overlap)
        embeddings = embed_texts(chunks) if chunks else []
        log.info("ReaderAgent: produced %d chunks", len(chunks))
        return {"raw": raw, "cleaned": cleaned, "chunks": chunks, "embeddings": embeddings}