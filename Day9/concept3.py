# Concept 3 — Conversation memory
# Right now every question is independent — Gemini forgets what you asked before. Ask it "explain more" and it has no idea what to expand on.
# This is where your ChatHistory class from Day 4 becomes real. Gemini needs the full conversation history passed every time:


from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

history=[]
while True:
    inp=input("user input:")
    if inp.strip().lower()=="quit":
        break
    history.append({"role":"user","parts":[{"text":inp}]})

    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history,
        config={
            "system_instruction":"you are a helpful GenAI interview coach .gives short, interview-ready answers",
            "temperature":2
        }
    )
    reply=response.text
    history.append({"role":"model","parts":[{"text":reply}]})
    print(f"Coach: {reply}\n")



