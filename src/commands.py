def build_prompt(command, topic, context):

    if command == "/summary":
        return f"Give a clear short summary of the topic using this context:\n{context}"

    elif command == "/short":
        return f"Explain in 2-3 lines only:\n{context}"

    elif command == "/teach":
        return f"Teach this topic step-by-step for a beginner:\n{context}"

    elif command == "/quiz":
        return f"Create 3 quiz questions from this topic. Do NOT give answers:\n{context}"

    return None
