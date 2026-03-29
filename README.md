# Course Planning Assistant

This repository contains an Agentic RAG (Retrieval-Augmented Generation) system designed to help students plan their courses by strictly grounding responses in university catalog data . Built for the Purple Merit AI/ML Engineer Intern Assessment, the assistant handles complex prerequisite chains, degree requirements, and handles policy ambiguity through a multi-agent workflow .

---

## Features

- Grounded Prerequisite Reasoning: Solves multi-hop prerequisite chains (A->B->C) with 100% grounding in source
- documents .Agentic Orchestration: Uses a 4-agent crew (Intake, Retriever, Planner, and Verifier) to normalize
- student profiles and audit plans for accuracy .Verifiable Citations: Every claim includes a mandatory URL and
- Section Heading/Page Number.Safe Abstention: Strictly refuses to guess on information not present in the curated
- catalog (e.g., professor "easiness" or exam times)

---

## 🛠️ Tech Stack

- Orchestration: CrewAI
- Retrieval: LangChain
- Vector Store: FAISS (Local)
- Embeddings: HuggingFace (BAAI/bge-small-en)
- LLM: Google Gemini (via crewai[google-genai])

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SaketSingh404/AI-ML_Engineer_Intern_Saket_Kumar_Singh-_March2026.git
cd Project_folder
```

### 2️⃣ Install UV & Crew-AI

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv tool install crewai
```

### 3️⃣ Create crew-ai virtual environment
Inside your directory run
**Windows**
```bash
crewai install
```
dependencies will be installed automatically
### 4️⃣ Provide API KEY
inside .env , enter
MODEL = MODEL_NAME
MODEL_API_KEY = 'YOUR_API_KEY'

### 5️⃣ Run crew
Inside project directory
```bash
crewai run
```
You will be asked for query

---

## 📈 Future Improvements

- Can use Paid embedding models for better accuracy
- Deploy to cloud (AWS / Azure)
- Improve UI/UX

---

## 👨‍💻 Author

Saket Kumar Singh

---
