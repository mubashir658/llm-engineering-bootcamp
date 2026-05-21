import json

# Imagine this came from an API call
responses = [
    '{"model": "gpt-4o-mini", "choices": [{"message": {"role": "assistant", "content": "Paris is the capital of France."}}], "usage": {"prompt_tokens": 8, "completion_tokens": 7}}',
    '{"model": "gpt-4o-mini", "choices": [{"message": {"role": "assistant", "content": "Python was created by Guido van Rossum."}}], "usage": {"prompt_tokens": 9, "completion_tokens": 8}}',
    '{"model": "gpt-4o-mini", "choices": [{"message": {"role": "assistant", "content": "The sun is approximately 93 million miles from Earth."}}], "usage": {"prompt_tokens": 10, "completion_tokens": 11}}'
]



def DictionaryCreate(responses):
    Final=[]
    output=[json.loads(i) for i in responses]
    for j in output:
        total_tokens=j["usage"]["prompt_tokens"]+j["usage"]["completion_tokens"]
        Final.append({"answer":j["choices"][0]["message"]["content"],"tokens":total_tokens})
    return Final

print(DictionaryCreate(responses))