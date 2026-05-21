import json

raw = '{"id": "chatcmpl-123", "model": "gpt-4o-mini", "choices": [{"message": {"role": "assistant", "content": "Hyderabad is known as the City of Pearls."}}], "usage": {"prompt_tokens": 12, "completion_tokens": 10}}'
dictionary=json.loads(raw)
print(dictionary["choices"][0]["message"]["content"])
total_tokens=dictionary["usage"]["prompt_tokens"]+dictionary["usage"]["completion_tokens"]
print(total_tokens)