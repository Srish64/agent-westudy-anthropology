from pathlib import Path
from src.pipeline_demo import demo_run

if __name__ == "__main__":
    # Run a simple demo reading samples/sample_input.pdf if present
    sample_pdf = Path("samples/sample_input.pdf")
    if not sample_pdf.exists():
        print("Put a PDF at samples/sample_input.pdf or change the path in src/main.py")
    demo_run(str(sample_pdf))