# Final task — put it all together
# This is the one from the plan — the actual text chunking logic used in RAG pipelines:
pythonsentences = [
    "AI is amazing",
    "Hi",
    "Large language models can generate text",
    "Okay",
    "Python is great for machine learning projects"
]
# Write a single function called process_sentences that does both steps in one go:

# Filter sentences longer than min_words
# Return each surviving sentence in UPPERCASE

# Expected output with min_words=3:
# ['LARGE LANGUAGE MODELS CAN GENERATE TEXT', 'PYTHON IS GREAT FOR MACHINE LEARNING PROJECTS']
# Hint: strings have a .upper() method.

def filter_sentences(pythonsentences,minLength):
    output=[i.upper() for i in pythonsentences if len(i.split())>minLength]
    return output
print(filter_sentences(pythonsentences,3))

