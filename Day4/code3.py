class ChatHistory:
    def __init__(self):
        self.messages=[]
    def add(self,role,content):
        self.messages.append({"role":role,"content":content})
    def get_all(self):
        return self.messages
    def last(self,n):
        return self.messages[-n:]
    def clear(self):
        self.messages.clear()
    def count(self):
        return len(self.messages)
history=ChatHistory()
history.add("user1","this is message 1 of conentent")
history.add("system","system message")
history.add("user","user 2 message")
history.add("system","system 2 message")
print(history.get_all())
print(history.last(1))
print(history.count())
history.clear()
print(history.count())
