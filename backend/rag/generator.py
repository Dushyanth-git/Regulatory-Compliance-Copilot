import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",   
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a banking compliance assistant. "
                    "Answer ONLY using the provided context. "
                    "If information is missing, say it is not available."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=400,
    )

    return completion.choices[0].message.content.strip()
