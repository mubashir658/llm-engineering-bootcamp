from google import genai
import os 
from dotenv import load_dotenv
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
while True:
    inp=input("user input :")
    if inp.strip().lower()=="quit":
        break
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=inp,
        config={
            "system_instruction":"you are a helpful GenAI interview coach .gives short, interview-ready answers",
            "temperature":0

        }
    )
    print(response.text)