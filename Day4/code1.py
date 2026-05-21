class AIModel:
    def __init__(self,name,max_tokens):
        self.name=name
        self.max_tokens=max_tokens
    # def describe(self):
    #     return "Model: gpt-4o-mini | Max tokens: 128000"
    def describe(self):
        return f"Model:{self.name},max_tokens:{self.max_tokens}"

model1=AIModel("model1",150000)
model2=AIModel("model2",120000)

print(model1.describe())
print(model2.describe())