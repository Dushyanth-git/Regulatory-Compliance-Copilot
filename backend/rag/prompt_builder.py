def build_prompt(query: str, chunks: list) -> str:
    context = "\n\n".join(
        [f"[Page {c['page']}]\n{c['text']}" for c in chunks]
    )

    return f"""
You are a banking compliance assistant.
Answer ONLY using the context below.
If the answer is not present, say "Information not available in provided documents."

Context:
{context}

Question:
{query}

Answer:
""".strip()
