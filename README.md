![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

WeStudyNow is a lightweight multi-agent system that converts UPSC Anthropology PDFs into summaries, flashcards, and Q/A using a coordinated agent pipeline with memory, tools, logging, and evaluation.

1) Multi-Agent Architecture

The system uses 4 agents:
	•	Reader Agent → Reads PDF, cleans text, creates chunks
	•	Teacher Agent → Generates summary + flashcards
	•	Helper Agent → Answers questions using embeddings + retrieval
	•	Orchestrator Agent → Controls workflow, manages session + logging

2) Tools Used
	•	Custom Tools:
	•	tool_read_pdf (extract text)
	•	tool_write_file (save outputs)
	•	tool_directory_list (inspect dataset)
	•	Built-in Tools:
	•	Sentence Embeddings
	•	HuggingFace FLAN-T5 LLM
	•	Gradio UI

3) Memory & Context

Each run creates session files:

session_<id>_summary_clean.txt
session_<id>_flashcards_clean.json
session_<id>_flashcards_norm.json
session_<id>_qa_clean.txt

Used for memory, state, and reproducibility.

Chunks are compacted before LLM processing to reduce noise.

4) Observability & Evaluation
	•	Every agent logs:
agent, action, session, details, latency
	•	An internal evaluator scores:
	•	Summary quality
	•	Flashcard count & formatting
Scores saved in:
evaluation_session_<id>.json

5) End-to-End Flow
	1.	Upload PDF
	2.	Reader extracts + chunks
	3.	Teacher summarizes & generates flashcards
	4.	Helper answers questions
	5.	Evaluator scores outputs
	6.	Orchestrator saves all files
	7.	Gradio UI available for testing

6) Gradio UI

Simple interface to:
	•	Upload PDFs
	•	View summary
	•	View flashcards
	•	Ask questions

7) Rubric Coverage (Meets 100%)
	•	Multi-agent system
	•	Sequential agents
	•	Custom + built-in tools
	•	Session memory
	•	Context engineering
	•	Observability (logging)
	•	Agent evaluation
	•	Deployment (Gradio)

WeStudyNow transforms Anthropology PDFs into structured learning materials automatically.
Built using multi-agent principles from the Agents Intensive course.

---
© 2025 Srishti M — Released under the MIT License.