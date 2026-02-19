import ollama
from src.memory import add_to_memory, get_memory
from src.commands import build_prompt

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

    # detect command
    if question.startswith("/"):
        parts = question.split(" ", 1)
        command = parts[0]
        topic = parts[1] if len(parts) > 1 else ""

        custom_prompt = build_prompt(command, topic, context)

        if custom_prompt:
            messages.append({"role": "user", "content": custom_prompt})
        else:
            messages.append({"role": "user", "content": question})
    else:
        messages.append({"role": "user", "content": question})

    response = ollama.chat(
        model="phi3",
        messages=messages
    )

    answer = response["message"]["content"]

    add_to_memory(question, answer)

    return answer



