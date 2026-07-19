# TinyScholar

TinyScholar is an AI-powered learning platform designed to make learning engaging, personalized, and interactive for children.

The platform combines modern backend technologies with Retrieval-Augmented Generation (RAG) and game-based learning to help children learn from their own study materials while allowing parents to monitor progress.

> **Project Status:** 🚧 Under active development

---

## Vision

TinyScholar aims to become an intelligent learning companion rather than a traditional question-answering application.

The long-term goals include:

- 📚 Learning from uploaded books and study materials
- 🤖 AI-assisted tutoring and explanations
- 🎮 Game-based learning experiences
- 📝 Quiz and assessment generation
- 📈 Personalized learning analytics
- 👨‍👩‍👧 Parent-focused learning dashboards

---

## Technology Stack

### Backend

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic

### AI

- LlamaIndex
- ChromaDB / pgvector (planned)
- Ollama / OpenAI

### Frontend

- React (planned)

---

## Documentation

Project documentation is organized under the `docs/` directory.

### Architecture

The architecture documentation describes the system design, domain model, and engineering decisions.

```
docs/architecture/
```

### Development Log

The development log records implementation progress, milestones, engineering decisions, and lessons learned.

```
docs/development-log/
```

---

## Repository Structure

```text
TinyScholar/
├── backend/
├── docs/
│   ├── architecture/
│   └── development-log/
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL

### Backend

```bash
cd backend

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

python -m alembic upgrade head

uvicorn app.main:app --reload
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## Project Philosophy

This repository follows a documentation-first approach.

Features are developed using the following workflow:

1. Design the architecture.
2. Review the design.
3. Implement in small feature branches.
4. Review generated code before merging.
5. Merge through Pull Requests.

This approach emphasizes maintainability, incremental development, and clear engineering decisions.

---

## License

This project is currently intended for learning and personal development.