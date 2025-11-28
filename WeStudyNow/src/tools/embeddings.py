from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

EMB_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

# load LLM utilities lazily
_LLM = None
_TOKENIZER = None

def embed_texts(texts):
    if not texts:
        return np.zeros((0, EMB_MODEL.get_sentence_embedding_dimension()))
    return EMB_MODEL.encode(texts, convert_to_numpy=True, show_progress_bar=False)

def embed_query(q):
    return EMB_MODEL.encode([q], convert_to_numpy=True)

def cosine_topk(query_emb, embeddings, texts, k=4):
    sims = cosine_similarity(query_emb.reshape(1,-1), embeddings)[0]
    idx = sims.argsort()[::-1][:k]
    return [texts[i] for i in idx], idx.tolist()

def get_llm_generate():
    global _LLM, _TOKENIZER
    if _LLM is None:
        _TOKENIZER = AutoTokenizer.from_pretrained("google/flan-t5-base")
        _LLM = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
        device = "cpu"
        if torch.cuda.is_available():
            device = "cuda"
            _LLM.to(device)
    def _gen(prompt, max_new_tokens:int=160):
        inputs = _TOKENIZER(prompt, return_tensors="pt", truncation=True, max_length=1024)
        device = next(_LLM.parameters()).device
        inputs = {k:v.to(device) for k,v in inputs.items()}
        out = _LLM.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
        return _TOKENIZER.decode(out[0], skip_special_tokens=True).strip()
    return _gen