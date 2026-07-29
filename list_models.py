## File for show AI models

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

print("All available models:\n")
for model in genai.list_models():
    print(f"Имя: {model.name}")
    print(f"    Description: {model.description[:100] if model.description else "Nothing"}")
    print(f"    Model supports text generation: {'generateContent' in model.supported_generation_methods}")
    print(f"    Model supports embeddings: {'embedContent' in model.supported_generation_methods}")
    print()