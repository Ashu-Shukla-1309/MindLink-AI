class Memory:
    def __init__(self):
        self.logs=[]
    def add(self, role, text):
        self.logs.append({"role":role,"text":text})
