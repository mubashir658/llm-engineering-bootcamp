class TokenTracker:
    def __init__(self):
        self.total_tokens=0
    def add(self,tokens):
        self.total_tokens+=tokens
    def get(self):
        return self.total_tokens
    def reset(self):
        self.total_tokens=0
tracker=TokenTracker()
tracker.add(50)
tracker.add(25)
print(tracker.get())
tracker.reset()
print(tracker.get())