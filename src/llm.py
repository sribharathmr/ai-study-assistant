import ollama

def generate_answer(question, context):

    prompt = f"""
You are a helpful teacher.

Answer ONLY using the context below.
If answer not found in context, say "Not found in notes".

Context:
{context}

Question:
{question}

Explain in simple words:
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


