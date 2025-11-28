from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.coordinator import CoordinatorWithPolicy
from dotenv import load_dotenv
import os

load_dotenv(".env.local")

app = FastAPI(title="MindLink AI (Groq)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

coord = CoordinatorWithPolicy()

class Ask(BaseModel):
    message: str

@app.post("/api/ask")
def ask(req: Ask):
    return coord.ask(req.message)
