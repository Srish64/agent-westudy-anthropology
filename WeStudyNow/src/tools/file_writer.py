from pathlib import Path
import json
OUT = Path("output")
OUT.mkdir(exist_ok=True)

def write_session_files(session_id: str, summary: str, flashcards: list, qa_answer: str, meta: dict = None):
    sfn = OUT / f"session_{session_id}_summary_clean.txt"
    ffn = OUT / f"session_{session_id}_flashcards_norm.json"
    qfn = OUT / f"session_{session_id}_qa_clean.txt"
    mfn = OUT / f"session_{session_id}_meta.json"
    sfn.write_text(summary or "", encoding="utf-8")
    ffn.write_text(json.dumps(flashcards, ensure_ascii=False, indent=2), encoding="utf-8")
    qfn.write_text(qa_answer or "", encoding="utf-8")
    mfn.write_text(json.dumps(meta or {}, indent=2), encoding="utf-8")
    return {"summary": str(sfn), "flashcards": str(ffn), "qa": str(qfn), "meta": str(mfn)}