import gradio as gr
from src.agents.orchestrator_agent import Orchestrator
from src.tools.file_writer import OUT

def launch_ui(share=False):
    orch = Orchestrator()
    def run(pdf, q, k):
        if pdf is None:
            return "Upload a PDF", "", "", ""
        pdf_bytes = pdf.read()
        r = orch.run_pipeline(pdf_bytes, question=q or "", k=int(k))
        # prepare flashcards text
        fc_text = "\n\n".join([f"Q{i+1}: {c['Q']}\nA{i+1}: {c['A']}" for i,c in enumerate(r["flashcards"])])
        files_json = r["files"]
        return r["summary"], fc_text, r["answer"], str(files_json)
    with gr.Blocks() as demo:
        gr.Markdown("# StudyMate — WeStudyNow")
        with gr.Row():
            pdf_in = gr.File(label="Upload PDF")
            q_in = gr.Textbox(label="Optional question")
            k_in = gr.Dropdown(["2","4","6"], value="4", label="Top-k")
        run_btn = gr.Button("Run")
        s_out = gr.Textbox(label="Summary", lines=8)
        f_out = gr.Textbox(label="Flashcards", lines=12)
        a_out = gr.Textbox(label="Answer", lines=4)
        files_out = gr.Textbox(label="Saved files", lines=4)
        run_btn.click(run, [pdf_in, q_in, k_in], [s_out, f_out, a_out, files_out])
    demo.launch(share=share)