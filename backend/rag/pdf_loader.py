import fitz  # PyMuPDF
import os

def extract_pdf_pages(pdf_path: str):
    doc = fitz.open(pdf_path)
    pages = []

    source_name = os.path.basename(pdf_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")

        text = text.replace("\n", " ").strip()

        if len(text) > 50:
            pages.append({
                "text": text,
                "page": page_num + 1,
                "source": source_name
            })

    return pages
