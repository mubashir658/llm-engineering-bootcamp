# Concept 2 — List comprehensions
# This is one of the most useful Python features for AI work. It's a compact way to build a list from another list.
# Normal way:
# pythonnumbers = [1, 2, 3, 4, 5]
# doubled = []
# for n in numbers:
#     doubled.append(n * 2)
# # doubled = [2, 4, 6, 8, 10]
# List comprehension way — same result, one line:
# pythondoubled = [n * 2 for n in numbers]
# You can also add a condition:
# pythoneven = [n for n in numbers if n % 2 == 0]
# # even = [2, 4]
# The pattern is always: [do_something for item in list if condition]

# Your turn:
# You have this list of sentences:
pythonsentences = [
    "AI is amazing",
    "Hi",
    "Large language models can generate text",
    "Okay",
    "Python is great for machine learning projects"
]

# Use a list comprehension to create a new list called long_sentences that contains only the sentences with more than 3 words.


def word_count(sent):
    return len(sent.split())
def filter_arr(pythonsentence,minLength):
    outputArr=[i for i in pythonsentence if word_count(i)>minLength]
    return outputArr


minLength=3
print(filter_arr(pythonsentences,minLength))

