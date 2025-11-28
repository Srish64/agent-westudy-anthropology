import logging
from src.tools.embeddings import embed_texts, embed_query, cosine_topk
from src.tools.embeddings import get_llm_generate

log = logging.getLogger(__name__)

class HelperAgent:
    def __init__(self):
        self.generate = get_llm_generate()

    def answer_question(self, question:str, chunks:list, embeddings, k:int=4):
        if not chunks or len(chunks)==0:
            return "No context available to answer."
        q_emb = embed_query(question)
        top_chunks, idx = cosine_topk(q_emb, embeddings, chunks, k=k)
        context = "\n\n".join(top_chunks)
        prompt = f"Answer concisely and cite context. Question: {question}\nContext:\n{context}\n\nAnswer:"
        log.info("HelperAgent: answering question")
        return self.generate(prompt, max_new_tokens=140)