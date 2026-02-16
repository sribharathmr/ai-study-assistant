import nltk
import time

nltk.download('punkt')
nltk.download('stopwords')

from src.semantic_search import semantic_search
from src.llm import generate_answer


# Load notes
with open("data/sample_notes.txt", "r") as file:
    notes = file.read().split("\n\n")

# Ask user
question = input("Enter your question: ")

# Retrieve context
context = semantic_search(question, notes)

# Generate AI answer
answer = generate_answer(question, context)

print("\nAI Answer:\n")
print(answer)





