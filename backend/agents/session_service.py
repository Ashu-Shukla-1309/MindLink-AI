import json
from pathlib import Path
from datetime import datetime

MEM_FILE = Path("memory_bank.json")

class InMemorySessionService:
    def __init__(self):
        self.sessions = {}
        self._load()

    def _load(self):
        if MEM_FILE.exists():
            try:
                data = json.loads(MEM_FILE.read_text(encoding="utf-8"))
                self.sessions = data
            except Exception:
                self.sessions = {}

    def _save(self):
        MEM_FILE.write_text(json.dumps(self.sessions, indent=2), encoding="utf-8")

    def add_message(self, session_id: str, role: str, text: str):
        now = datetime.utcnow().isoformat()
        self.sessions.setdefault(session_id, []).append({"time": now, "role": role, "text": text})
        self._save()

    def get_session(self, session_id: str):
        return self.sessions.get(session_id, [])
