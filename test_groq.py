import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def test_groq():
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Fast and free-tier friendly
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "Say hello and tell me you're ready for ForgeImpact!"}
        ],
        temperature=0.7,
        max_tokens=150
    )
    
    print("✅ Groq API Test Successful!")
    print("Response:", completion.choices[0].message.content)

if __name__ == "__main__":
    test_groq()