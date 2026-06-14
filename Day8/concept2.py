#post requests
import requests
url="https://httpbin.org/post"
payload={
    "prompt": "What is RAG?",
    "model": "gpt-4o-mini"
}
response=requests.post(url,json=payload)
print(response.status_code)
data=response.json()
print(data['json']) 