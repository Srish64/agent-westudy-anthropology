from src.agents.orchestrator_agent import Orchestrator

def demo_run(pdf_path: str):
    orch = Orchestrator()
    res = orch.run_pipeline_from_path(pdf_path, question="What is anthropology?")
    print("Session:", res["session_id"])
    print("--- Summary ---")
    print(res["summary"][:1000])
    print("--- Flashcards (preview) ---")
    for i,fc in enumerate(res["flashcards"][:8],1):
        print(f"{i}. Q: {fc.get('Q')}")
        print(f"   A: {fc.get('A')}")