from pathlib import Path
import json
from .evaluate_summary import evaluate_summary_text
from .evaluate_flashcards import evaluate_flashcards

def evaluate_session(summary_path: str, flashcards_path: str):
    p1 = Path(summary_path)
    p2 = Path(flashcards_path)
    summary = p1.read_text(encoding="utf-8") if p1.exists() else ""
    flash = json.loads(p2.read_text(encoding="utf-8")) if p2.exists() else []
    s_eval = evaluate_summary_text(summary)
    f_eval = evaluate_flashcards(flash)
    out = {"summary_eval": s_eval, "flashcards_eval": f_eval}
    ev_file = p1.parent / f"evaluation_{p1.stem}.json"
    ev_file.write_text(json.dumps(out, indent=2), encoding="utf-8")
    return out