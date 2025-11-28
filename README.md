

# MindLink AI - Intelligent Multi-Agent Customer Support Assistant

**MindLink AI** is a cutting-edge, multi-agent customer support system designed to automate and enhance customer service interactions. Built as the capstone project for the **Google × Kaggle 5-Day AI Agents Intensive Course and is developed by Ashutosh Shukla**, this system provides efficient, intelligent, and context-aware support for an imaginary company, XYZ Company.

The system integrates advanced **multi-agent architecture**, **LLM-powered replies**, **dynamic escalation mechanisms**, and **real-time observability**, all aimed at providing a seamless and responsive user experience.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Deployment](#deployment)
- [Agent Evaluation](#agent-evaluation)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

MindLink AI is a fully-featured, multi-agent customer support system that simulates a real-world enterprise-level customer service experience. The system includes several intelligent agents that manage tasks such as:

- **Intent Detection**: Identifying user intent (e.g., billing, refund, cancellation).
- **Urgency Detection**: Analyzing and categorizing the urgency of requests.
- **Response Generation**: Generating professional, context-aware replies using the **Groq Llama-3.3-70B** LLM.
- **Escalation Handling**: Deciding when a request requires human intervention.
- **Safety Enforcement**: Blocking PII and inappropriate content.

The system also features **memory capabilities**, allowing it to remember context within a session and retain conversation logs for future reference.

---

## Features

### 🧠 Multi-Agent System
MindLink AI uses a multi-agent architecture to manage different aspects of the customer support process. The agents communicate sequentially or in parallel, enabling smart, dynamic decision-making.

- **IntentAgent**: Detects customer intent (e.g., billing, refund, cancellation).
- **UrgencyAgent**: Detects the urgency level of requests (low, medium, high).
- **ReplyAgent**: Uses the **Groq Llama-3.3-70B** LLM to generate context-specific replies.
- **PolicyAgent**: Ensures compliance by blocking PII and inappropriate content.
- **EscalationAgent**: Determines when a human agent is required.
- **SessionMemoryAgent**: Manages conversation memory, including short-term and long-term memory storage.

### 🔧 Tool Integration
MindLink AI supports the use of custom tools to enhance interactions, such as:

- **lookup_order(order_id)**: A custom tool to retrieve order status or billing issues, improving response accuracy by providing relevant data directly within the conversation.

### 🧬 Memory System
The system employs both short-term and long-term memory capabilities:
- **Short-term memory** is tracked within the current session to maintain conversation context.
- **Long-term memory** is stored in a persistent memory bank (JSON file), improving the system’s ability to provide accurate, contextually rich responses over time.

### 📊 Observability
MindLink AI features comprehensive logging and metrics for performance monitoring:
- Latency tracking (in milliseconds).
- Error and request counters.
- Detailed logs after every LLM call, enabling real-time observability.

### 🧪 Agent Evaluation
The system includes an automated evaluation harness to test:
- **Agent latency** and response time.
- **Correctness** of agent replies.
- **Policy compliance** (e.g., blocking PII).
- **Escalation logic**.

---

## Architecture

The system follows a modular architecture, consisting of a **frontend** built with **React** and **Vite**, a **backend** powered by **FastAPI**, and an AI layer driven by **Groq Llama-3.3-70B**.

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

### Frontend:
- **React** (for building the UI components)
- **Vite** (fast, modern bundler for React)
- **TailwindCSS** (utility-first CSS framework)
- **Glassmorphic UI** (sleek, modern design with glass-like effects)

### Backend:
- **FastAPI** (asynchronous, fast web framework)
- **Uvicorn** (ASGI server for FastAPI)
- **Python 3.10+**
- **Groq Llama-3.3-70B** (LLM for generating contextual replies)
- **python-dotenv** (for environment variable management)

### Tools & Infrastructure:
- **Custom tools** for enhanced functionality (e.g., order lookup).
- **Session & Memory Services** for managing conversation history and state.
- **Logging and metrics** to track system health.

---

## Installation & Setup

To get started with **MindLink AI**, follow these steps:

### 1. Clone the Repository:
```bash
git clone https://github.com/Ashu-Shukla-1309/MindLink-AI.git
cd MindLink-AI
```

### 2. Backend Setup (FastAPI):
Navigate to the **backend** directory:
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On MacOS/Linux
pip install -r requirements.txt
```

Create the `.env.local` file with your **Groq API Key**:
```plaintext
GROQ_API_KEY=YOUR_KEY
GROQ_MODEL=llama-3.3-70b-versatile
```

Start the backend server:
```bash
uvicorn app:app --reload --port 8000
```

### 3. Frontend Setup (React):
Navigate to the **frontend** directory:
```bash
cd frontend
npm install
npm run dev
```

The app will be accessible at [http://localhost:5173](http://localhost:5173).

---

## Deployment

### Frontend:
- **Vercel**: Deploy the frontend by importing the `frontend/` folder and building with `npm run build`.

### Backend:
- **Render / Railway**: Deploy the backend as a Python web service. The start command should be:
  ```bash
  uvicorn app:app --host 0.0.0.0 --port $PORT
  ```

Update the frontend `.env` to use the correct backend URL:
```plaintext
VITE_BACKEND_URL=https://your-backend-url.onrender.com
```

---

## Agent Evaluation

MindLink AI includes an **evaluation harness** for testing various aspects of the system, including:

- **Latency**: Measures the response time of agents.
- **Correctness**: Ensures that agent responses are accurate and relevant.
- **Policy Safety**: Verifies that sensitive information is blocked appropriately.
- **Escalation Logic**: Tests the correct triggering of escalations when necessary.

---

## License

This project is licensed under the **MIT License**, allowing you to freely use, modify, and distribute the code.

---

## Acknowledgements

- **Google** & **Kaggle AI Agents Team** for their comprehensive course and mentorship.
- **Groq LLM** for their ultra-fast inference model.
- The **FastAPI** community for their high-performance web framework.
- The **Vite + React** ecosystem for modern, fast web development tools.

---

### **MindLink AI** - Making Customer Support Smarter and More Efficient



