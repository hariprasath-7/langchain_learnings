import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("Google_API_Key") or os.getenv("GOOGLE_GENAI_API_KEY")

if not api_key:
    raise ValueError("API Key not found in .env file!")

# Updated to the required current model
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key,
    temperature=0.7
)

prompt = "Write a short poem about the beauty of nature."
result = model.invoke(prompt)

print("\n--- Output ---")
print(result.text)