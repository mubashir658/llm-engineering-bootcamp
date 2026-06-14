#get request
import requests
response=requests.get("https://httpbin.org/get")
print(response.status_code)
data=response.json()
print(data['url'])
