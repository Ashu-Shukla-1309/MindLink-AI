# reply/groq_reply.py
import os, traceback
from groq import Groq
from dotenv import load_dotenv

load_dotenv(".env.local")

class GroqReplyAgent:
    def __init__(self):
        key = os.getenv("GROQ_API_KEY")
        if not key:
            raise Exception("GROQ_API_KEY missing in .env.local")
        self.client = Groq(api_key=key)
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        self.system_prompt = (
            "You are MindLink AI, the official customer-support assistant for XYZ Company. "
            "Represent XYZ Company: be professional, concise, helpful, and polite. "
            "Always respond as an XYZ Company support representative and never mention you are an AI model. "
            "Signature: '— MindLink AI (XYZ Company)'. Built by Ashutosh Shukla."
        )

    def _extract_text(self, choice):
        try:
            msg = getattr(choice, 'message', None)
            if msg is not None:
                if hasattr(msg, 'content'):
                    return msg.content
                if hasattr(msg, 'text'):
                    return msg.text
            if hasattr(choice, 'text'):
                return choice.text
            if isinstance(choice, dict):
                return choice.get('message', {}).get('content') or choice.get('text')
        except Exception:
            try:
                return str(choice)
            except:
                return ''
        return ''

    def reply(self, message: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": message}
                ],
                temperature=0.2,
            )
            choices = getattr(response, "choices", None) or response.get("choices", [])
            if not choices:
                return "LLM returned no choices."
            first = choices[0]
            return self._extract_text(first) or "LLM returned empty content."
        except Exception as e:
            print("Groq call error:", e)
            traceback.print_exc()
            return "Internal LLM error — the request could not be completed at this time."
