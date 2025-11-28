class PolicyAgent:
    def check(self, message:str):
        msg=message.lower()
        reasons=[]
        allowed=True
        if any(x in msg for x in ["bomb","kill","crime","ssn","social security"]):
            allowed=False
            reasons.append("Harmful intent detected")
        else:
            reasons.append("OK")
        return {"allowed": allowed, "reasons": reasons}
