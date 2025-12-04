import google.generativeai as genai
import os

# Use the same key from app.py (or set GOOGLE_API_KEY env var)
api_key = os.getenv('GOOGLE_API_KEY', 'AIzaSyDHUFzYKTcOt_DN22aWh4HT2RQ7ybn6wQc')
genai.configure(api_key=api_key)

print('Available models:')
for m in genai.list_models():
    print(m)
