import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_GENAI_API_KEY")

print(f"Loaded key starting with: {api_key[:6] if api_key else 'None'}...")

client = genai.Client(api_key=api_key)

try:
    print("\nModels available to your API key:")
    for model in client.models.list():
        actions = getattr(model, "supported_actions", []) or []
        if "generateContent" in actions:
            print(f" -> {model.name}")
except Exception as e:
    print(f"Error fetching models: {e}")