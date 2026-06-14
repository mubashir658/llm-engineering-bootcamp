from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
#user input 
#inp=input("user input")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is RAG in one sentence?"           #here we can also take user input instead of hardcoding the question. For example, we can use inp=input("user input") and then pass inp as contents=inp
)

print(response.text)

