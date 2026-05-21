from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
MODEL_NAME=os.getenv("MODEL_NAME")
MAX_TOKENS=os.getenv("MAX_TOKENS")
print(OPENAI_API_KEY)
print(MODEL_NAME)

print(MAX_TOKENS)
