import os
from dotenv import load_dotenv
from google import genai

# Load key-value pairs from .env into operating system environment variables
load_dotenv()

# Read the key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client using your loaded API key
client = genai.Client(api_key=api_key)

# Generate text with Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Hello! Tell me a fun fact about programming."
)

print(response.text)
