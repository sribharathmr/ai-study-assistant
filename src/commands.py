def build_prompt(command, topic, context):

    if command == "/summary":
        return f"Give a clear short summary of the topic using this context:\n{context}"

    elif command == "/short":
        return f"Explain in 2-3 lines only:\n{context}"

    elif command == "/teach":
        return f"Teach this topic step-by-step for a beginner:\n{context}"

    elif command == "/quiz":
        return f"""
You are a strict examiner.

Ask exactly ONE short question from the topic.

Output format rules:
- Only one sentence
- No options
- No explanation
- No answer
- No extra text
- Do not repeat the topic

Topic:
{context}

Your output must look like:
Question: <one line question>
"""


    return None
