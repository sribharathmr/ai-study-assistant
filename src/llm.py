import ollama
from src.memory import add_to_memory, get_memory

def generate_answer(question, context):

    system_prompt = f"""
You are a helpful teacher.

Answer ONLY using the context below.
If answer not found, say "Not found in notes".

Context:
{context}
"""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(get_memory())
    messages.append({"role": "user", "content": question})

    response = ollama.chat(
        model="phi3",
        messages=messages
    )

    answer = response["message"]["content"]

    add_to_memory(question, answer)

    return answer


