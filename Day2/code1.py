'''Let's go! Day 2 — Dictionaries & JSON.
This is arguably the most important day for AI work. Every single API response you ever get — from OpenAI, from any service — comes back as JSON. You need to be completely comfortable pulling data out of it.

Concept 1 — Dictionaries
A dictionary stores data as key-value pairs, like a real dictionary where the word is the key and the definition is the value.
pythonperson = {
    "name": "Ravi",
    "age": 22,
    "city": "Hyderabad"
}

print(person["name"])      # Ravi
print(person["age"])       # 22
You can also use .get() — safer because it won't crash if the key doesn't exist:
pythonprint(person.get("name"))      # Ravi
print(person.get("salary"))    # None  (no crash!)
print(person.get("salary", 0)) # 0     (default value)

Your turn:
Create a dictionary called model_info that stores these details about an AI model:

name: "gpt-4o-mini"
company: "OpenAI"
max_tokens: 128000
is_free: False

Then print the name and max_tokens using both [] and .get().
Try it and paste your code!'''

model_info={
    "name":"gpt-4o-mini",
    "company":"OpenAI",
    "max_tokens":128000,
    "is_free":False
}

print(model_info["name"])
print(model_info["max_tokens"])
print(model_info.get("name"))
print(model_info.get("max_tokens",0))




