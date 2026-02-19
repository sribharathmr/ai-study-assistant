import nltk
from src.load_notes import load_all_notes


nltk.download('punkt')
nltk.download('stopwords')

from src.semantic_search import semantic_search
from src.llm import generate_answer
from src.chunker import chunk_text



# Load notes
notes = load_all_notes()

# Ask user
question = input("Enter your question: ")

# Retrieve context
context = semantic_search(question, notes)

# Generate AI answer
answer = generate_answer(question, context)

print("\nAI Answer:\n")
print(answer)





