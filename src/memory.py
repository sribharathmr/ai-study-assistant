chat_history = []

def add_to_memory(question, answer):
    chat_history.append({"role": "user", "content": question})
    chat_history.append({"role": "assistant", "content": answer})

def get_memory():
    return chat_history[-6:]  # last 3 exchanges only
