
# MindLink AI - Intelligent Multi-Agent Customer Support Assistant

**MindLink AI** is a cutting-edge multi-agent customer support system designed to enhance and automate customer service interactions. Developed as the capstone project for the **Google × Kaggle 5-Day AI Agents Intensive Course** by **Ashutosh Shukla**, this system provides efficient, intelligent, and context-aware support for an imaginary company, XYZ Company.

It integrates advanced **multi-agent architecture**, **LLM-powered replies**, **dynamic escalation mechanisms**, and **real-time observability**, all aimed at providing a seamless and responsive user experience.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Deployment](#deployment)
- [Agent Evaluation](#agent-evaluation)
- [Repository Structure](#repository-structure)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

MindLink AI simulates a real-world, enterprise-level customer service experience, featuring several intelligent agents that handle tasks such as:

- **Intent Detection**: Identifying user intent (e.g., billing, refund, cancellation).
- **Urgency Detection**: Analyzing and categorizing the urgency of requests.
- **Response Generation**: Generating professional, context-aware replies using the **Groq Llama-3.3-70B** LLM.
- **Escalation Handling**: Deciding when a request requires human intervention.
- **Safety Enforcement**: Blocking PII and inappropriate content.

The system includes **memory capabilities**, retaining conversation context and logs for future reference.

---

## Features

### 🧠 Multi-Agent System

- **IntentAgent** — Detects customer intent (e.g., billing, refund, cancellation).
- **UrgencyAgent** — Detects the urgency level of requests.
- **ReplyAgent** — Uses the **Groq Llama-3.3-70B** LLM to generate contextual replies.
- **PolicyAgent** — Enforces safety and PII policies.
- **EscalationAgent** — Determines when to escalate to a human.
- **SessionMemoryAgent** — Manages session memory.

### 🔧 Tool Integration

- Custom tools (e.g., `lookup_order(order_id)`) for fetching real-time data like order details.

### 🧬 Memory System

- Short-term memory for active sessions and long-term persistent storage for user/context retention.

### 📊 Observability

- Metrics for latency, error/request counters, and detailed logs for each LLM call.

### 🧪 Agent Evaluation

- Automated testing for agent latency, correctness, policy compliance, and escalation.

---

## Architecture

```
MindLink AI
│
├── frontend (React + Vite + Tailwind)
│     ├── Chat UI (chat bubbles)
│     ├── Avatar icons
│     ├── Glassmorphic design
│     └── REST API → backend
│
├── backend (FastAPI)
│     ├── /api/ask endpoint
│     ├── Multi-agent pipeline
│     ├── GroqReplyAgent (LLM)
│     ├── Policy & escalation agents
│     ├── Custom tools (e.g., order lookup)
│     └── Metrics + memory storage
│
└── Groq Llama-3.3-70B (LLM engine)
```

---

## Tech Stack

### Frontend

- React, Vite, TailwindCSS, Framer-motion (animations)

### Backend

- FastAPI, Uvicorn, Python 3.10+, python-dotenv, Groq Llama integration

### Tools & Infra

- Custom tools, session & memory services, logging/metrics

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ashu-Shukla-1309/MindLink-AI.git
cd MindLink-AI
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt
# create .env.local with your GROQ_API_KEY and GROQ_MODEL
uvicorn app:app --reload --port 8000
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
# Open http://localhost:5173
```

---

## Deployment

- **Frontend**: Deploy on Vercel (build with `npm run build`).
- **Backend**: Deploy on Render, Railway, or any containerized environment. Start with `uvicorn app:app --host 0.0.0.0 --port $PORT`.
- Set `VITE_BACKEND_URL` in the frontend `.env` file to point to your deployed backend.

---

## Agent Evaluation

The repository includes automated evaluation scripts to test:

- Latency & throughput
- Correctness of replies
- Policy enforcement
- Escalation triggers

---

## Repository Structure

Here’s an overview of the folder structure and the purpose of each major file/folder in the repository:

```
MindLink-AI/
├─ .git/                         # Git metadata (hooks, logs, objects)
├─ backend/                       # Python backend (agents, reply logic, tools)
│  ├─ app.py                      # FastAPI entrypoint
│  ├─ agents/                     # Multi-agent orchestration and logic
│  ├─ evaluation/                 # Automated agent evaluation
│  ├─ observability/              # Metrics helpers
│  ├─ reply/                      # LLM integration
│  └─ tools/                      # Custom tools callable by agents
├─ frontend/                      # React frontend (UI, chat components)
│  ├─ index.html                  # HTML entrypoint
│  ├─ package.json                # npm scripts & dependencies
│  └─ src/                        # React components & styles
├─ LICENSE                        # MIT License
├─ README.md                      # Project overview (this file)
├─ start_app.bat                  # Windows helper to start both backend & frontend
└─ structure.txt                  # Listing of project structure
```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **Google** & **Kaggle AI Agents Team** — Course & mentorship.
- **Groq** — LLM model used for generating intelligent responses.
- **FastAPI** — High-performance backend framework.
- **Vite + React** — Modern frontend tooling.
