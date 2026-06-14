import requests

def make_request(url, payload, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    
    print("Status code:", response.status_code)
    print("Raw response:", response.text[:200])  # first 200 chars
    
    if response.status_code != 200:
        return {"status": response.status_code, "data": None}
    
    return {"status": response.status_code, "data": response.json()}

payload = {"role": "user", "prompt": "what is RAG?"}
url = "https://httpbin.org/post"

res = make_request(url, payload, "my_api_key")
# print(res["status"])
# print(res["data"]["headers"]["Authorization"])