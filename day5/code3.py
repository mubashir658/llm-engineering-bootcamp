from dotenv import load_dotenv
import os
load_dotenv()


def load_config():
        key=os.getenv("OPENAI_API_KEY")
        if not key:
                raise ValueError("OPENAI_API_KEY missing from .env file")
       
        name=os.getenv("MODEL_NAME")
        try:
                max_tokens=int(os.getenv("MAX_TOKENS"))
        except ValueError:
                print("max_tokens invalid,using default 1000")
                max_tokens=1000
            
        response={"key":key,"name":name,"max_tokens":max_tokens}
        return response
config=load_config()
print(config)

