# Concept 1 — Functions
# A function is a reusable block of code. Here's the anatomy:
# pythondef greet(name):        # 'def' starts it, 'name' is the input
#     message = "Hello, " + name
#     return message      # 'return' sends the result back

# result = greet("Riya")
# print(result)           # Hello, Riya
# Your turn — write this yourself:
# Write a function called word_count that takes a sentence (string) and returns how many words are in it.
# Hint: strings have a .split() method that splits by spaces.
# python
# sentence = "Large language models are really powerful"
# # your function should return 6


def word_count(sentence):
    return len(sentence.split())
sentence = "Large language models are really powerful"
print(word_count(sentence))

