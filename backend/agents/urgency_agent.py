class UrgencyAgent:
    def detect(self, message:str):
        m = message.lower()
        if "urgent" in m or "immediately" in m or "hacked" in m:
            return "high"
        if "now" in m:
            return "medium"
        return "low"
