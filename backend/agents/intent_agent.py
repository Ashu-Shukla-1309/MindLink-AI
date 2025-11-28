class IntentAgent:
    def classify(self, message:str):
        m = message.lower()
        if "cancel" in m or "unsubscribe" in m:
            return "cancellation"
        if "refund" in m:
            return "refund"
        if "invoice" in m or "bill" in m:
            return "billing"
        if "help" in m or "support" in m:
            return "general_help"
        return "general"
