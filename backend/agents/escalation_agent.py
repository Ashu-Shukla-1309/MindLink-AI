class EscalationAgent:
    def check(self, intent, urgency, message):
        if urgency == "high":
            return {"escalate": True, "note": "High urgency – escalate"}
        return {"escalate": False, "note": "No escalation"}
