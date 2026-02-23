import os
from dotenv import load_dotenv
import google.generativeai as genai

# Explicitly load the .env in the same directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

print("API Key loaded:", bool(os.getenv("GOOGLE_API_KEY")))

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available models supporting generateContent:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(" -", m.name)
