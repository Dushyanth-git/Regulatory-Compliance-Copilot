import requests
import numpy as np
import os

print("USING EMBEDDER:", __file__)

JINA_API_URL = "https://api.jina.ai/v1/embeddings"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('JINA_API_KEY')}",
    "Content-Type": "application/json"
}

def embed_texts(texts):
    payload = {
        "model": "jina-embeddings-v2-base-en",
        "input": texts
    }

    r = requests.post(JINA_API_URL, headers=HEADERS, json=payload)
    if r.status_code != 200:
        print("STATUS:", r.status_code)
        print("RESPONSE:", r.text)
    r.raise_for_status()

    return np.array([x["embedding"] for x in r.json()["data"]])
