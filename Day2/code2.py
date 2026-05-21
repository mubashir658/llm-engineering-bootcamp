response={
    "model":"gpt-4o-mini",
    "choices":[
        {"message":{
            "role":"assistant",
            "content":"python is great"
        }
         }
    ]
}

print(response.get("model"))
print(response["choices"][0]["message"]["role"])
print(response["choices"][0]["message"]["content"])