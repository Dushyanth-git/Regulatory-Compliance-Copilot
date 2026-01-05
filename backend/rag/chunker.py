def chunk_pages(pages, chunk_size=500, overlap=100, audience="customer"):
    chunks = []

    for page in pages:
        words = page["text"].split()
        start = 0

        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]

            chunk_text = " ".join(chunk_words)

            chunks.append({
                "text": chunk_text,
                "page": page["page"],
                "source": page["source"],
                "audience": audience
            })

            start = end - overlap

    return chunks
