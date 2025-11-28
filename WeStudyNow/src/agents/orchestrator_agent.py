import json, uuid
from pathlib import Path
from src.agents.reader_agent import ReaderAgent
from src.agents.teacher_agent import TeacherAgent
from src.agents.helper_agent import HelperAgent
from src.tools.file_writer import write_session_files
from src.eval.evaluator import evaluate_session
import logging

log = logging.getLogger(__name__)
OUT_DIR = Path("output")
OUT_DIR.mkdir(exist_ok=True)

class Orchestrator:
    def __init__(self):
        self.reader = ReaderAgent()
        self.teacher = TeacherAgent()
        self.helper = HelperAgent()

    def run_pipeline(self, pdf_bytes: bytes, question: str = "", k:int=4, session_id: str = None):
        sid = session_id or uuid.uuid4().hex[:8]
        tmp_pdf = OUT_DIR / f"{sid}_tmp.pdf"
        tmp_pdf.write_bytes(pdf_bytes)
        return self.run_pipeline_from_path(str(tmp_pdf), question=question, k=k, session_id=sid)

    def run_pipeline_from_path(self, pdf_path: str, question: str = "", k:int=4, session_id: str = None):
        sid = session_id or uuid.uuid4().hex[:8]
        log.info("Orchestrator: starting session %s", sid)
        r = self.reader.read_and_chunk(pdf_path)
        # select centroid-based top-k as context
        chunks = r["chunks"]
        embeddings = r["embeddings"]
        context = " ".join(chunks[:k]) if chunks else r["cleaned"][:4000]
        summary = self.teacher.summarize(context)
        fc_raw = self.teacher.generate_flashcards(context)
        # normalize flashcards (simple parse)
        flashcards = []
        for ln in fc_raw.splitlines():
            if "||" in ln:
                q,a = ln.split("||",1)
                flashcards.append({"Q": q.strip(), "A": a.strip()})
        if not flashcards:
            # fallback: put first sentences as Q/A stub
            for i,c in enumerate(chunks[:8]):
                flashcards.append({"Q": f"Q{i+1}: {c[:60]}", "A": f"A{i+1}: {c[:140]}"})
        answer = ""
        if question:
            answer = self.helper.answer_question(question, chunks, embeddings, k=k)
        files = write_session_files(sid, summary, flashcards, answer, meta={"pdf_path": pdf_path})
        eval_res = evaluate_session(files["summary"], files["flashcards"])
        log.info("Orchestrator: finished session %s", sid)
        return {"session_id": sid, "summary": summary, "flashcards": flashcards, "answer": answer, "files": files, "evaluation": eval_res}