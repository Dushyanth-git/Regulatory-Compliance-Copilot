from backend.rag.pdf_loader import extract_pdf_pages
from backend.rag.chunker import chunk_pages
from backend.rag.embedder import embed_texts
from backend.rag.vector_store import VectorStore
from backend.rag.prompt_builder import build_prompt
from backend.rag.generator import generate_answer

pdf = "backend/data/customer/customer_rights.pdf"

pages = extract_pdf_pages(pdf)
chunks = chunk_pages(pages, audience="customer")

texts = [c["text"] for c in chunks][:30]
chunks = chunks[:30]

embeddings = embed_texts(texts)
store = VectorStore(embeddings, chunks)

query = "Why can a bank restrict transactions if KYC is not completed?"

q_emb = embed_texts([query])[0]
results = store.search(q_emb, k=3)

prompt = build_prompt(query, results)
answer = generate_answer(prompt)

print("\n=== ANSWER ===")
print(answer)

print("\n=== SOURCES ===")
for r in results:
    print(f"Page {r['page']} | {r['source']}")
