import logging
from src.tools.embeddings import get_llm_generate

log = logging.getLogger(__name__)

class TeacherAgent:
    def __init__(self):
        self.generate = get_llm_generate()

    def summarize(self, context:str, bullets:int=6):
        prompt = (
            "You are StudyMate. Produce EXACTLY %d concise bullet points for exam revision. "
            "Each bullet on one line. No extra commentary.\n\nContext:\n%s\n\nBulleted summary:\n"
        ) % (bullets, context[:4000])
        log.info("TeacherAgent: generating summary")
        out = self.generate(prompt, max_new_tokens=180)
        return out.strip()

    def generate_flashcards(self, context:str, n:int=8):
        prompt = (
            "You are StudyMate. Produce EXACTLY %d flashcards, one per line, format:\n"
            "Q<number>: <question> || A<number>: <answer>\n"
            "Questions <=12 words; answers <=25 words.\n\nContext:\n%s\n\nFlashcards:\n"
        ) % (n, context[:4000])
        log.info("TeacherAgent: generating flashcards")
        out = self.generate(prompt, max_new_tokens=300)
        return out.strip()