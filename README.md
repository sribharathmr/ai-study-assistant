# 🧠 Personal AI Study Assistant

An AI-powered study companion that can read notes & PDFs, answer questions, and generate quizzes using Retrieval Augmented Generation (RAG).

Built completely from scratch while learning AI, NLP, and LLM engineering.

---

## 🚀 Features

- Ask questions from your OS / DBMS notes
- Works with TXT and PDF files
- Semantic search using embeddings
- Quiz generation mode
- Memory-aware responses
- Prompt injection protection
- Local model / API model support
- Git version tracked daily progress

---

## 🏗️ Project Architecture

User Question → Semantic Search → Context Builder → LLM → Final Answer

---

## 🧰 Tech Stack

- Python
- Sentence Transformers (Embeddings)
- PyPDF (PDF Reader)
- Local LLM / API LLM
- RAG Pipeline
- VS Code

---

## 📂 Folder Structure

src/
load_notes.py
semantic_search.py
llm.py
memory.py
quiz.py
data/
notes.txt
notes.pdf
main.py

---

## ▶️ Run the Project

Create virtual environment:
python -m venv .venv

Activate:
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run:
python main.py

---

## 💬 Example Commands

what is deadlock
/quiz deadlock

---

## 📚 What I Learned

- Retrieval Augmented Generation (RAG)
- Embeddings & semantic similarity
- Prompt engineering
- Context safety (prompt injection prevention)
- LLM integration
- AI system design

---

## 👨‍💻 Author

Sribharath Ravindranath
