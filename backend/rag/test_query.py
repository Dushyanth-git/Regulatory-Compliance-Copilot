from .embedder import embed_texts
from .pdf_loader import extract_pdf_pages
from .chunker import chunk_pages
from .vector_store import VectorStore


pdf = "backend/data/customer/customer_rights.pdf"

pages = extract_pdf_pages(pdf)
chunks = chunk_pages(pages, audience="customer")

texts = [c["text"] for c in chunks][:30]   # limit for testing
chunks = chunks[:30]

embeddings = embed_texts(texts)

store = VectorStore(embeddings, chunks)

query = "Why can a bank restrict transactions if KYC is not completed?"
q_emb = embed_texts([query])[0]

results = store.search(q_emb, k=3)

print("\n=== CUSTOMER RESULTS ===")
for r in results:
    print(f"Page {r['page']} | {r['source']}")
    print(r['text'][:300], "\n")
