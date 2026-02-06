from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()  # loads .env if present

key = os.getenv("OPENAI_API_KEY")
print("Key present:", bool(key))
if not key:
    print("OPENAI_API_KEY not set")
else:
    try:
        client = OpenAI(api_key=key)
        models = client.models.list()
        print("OpenAI reachable, models count:", len(models.data))
    except Exception as e:
        print("OpenAI error:", type(e).__name__, e)
