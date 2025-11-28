from agents.intent_agent import IntentAgent
from agents.urgency_agent import UrgencyAgent
from agents.escalation_agent import EscalationAgent
from agents.policy_agent import PolicyAgent
from agents.memory import Memory
from reply.groq_reply import GroqReplyAgent

class CoordinatorWithPolicy:
    def __init__(self):
        self.intent_agent = IntentAgent()
        self.urgency_agent = UrgencyAgent()
        self.reply_agent = GroqReplyAgent()
        self.escalation_agent = EscalationAgent()
        self.policy_agent = PolicyAgent()
        self.memory = Memory()
        self.sessions = None

    def ask(self, message):
        self.memory.add("user", message)

        intent = self.intent_agent.classify(message)
        urgency = self.urgency_agent.detect(message)
        policy = self.policy_agent.check(message)

        # Tool integration placeholder (to be patched)
        if intent == 'billing':
            import re
            m = re.search(r"(INV|ORD)[- ]?\d+", message, flags=re.I)
            if m:
                order_id = m.group(0)
                try:
                    from tools.custom_tools import lookup_order
                    tool_res = lookup_order(order_id)
                    message = message + "\n\n[tool_lookup_order_result]\n" + str(tool_res)
                except Exception:
                    pass

        if not policy["allowed"]:
            reply="I'm sorry, I cannot help with that request."
            return {
                "intent": intent,
                "urgency": urgency,
                "reply": reply,
                "escalation": {"escalate": True, "note":"Policy blocked"},
                "policy": policy
            }

        reply = self.reply_agent.reply(message)
        # No metrics here in minimal version
        escalation = self.escalation_agent.check(intent, urgency, message)

        self.memory.add("agent", reply)

        return {
            "intent": intent,
            "urgency": urgency,
            "reply": reply,
            "escalation": escalation,
            "policy": policy
        }
