import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMClient:
    def __init__(self, model: str = "openai/gpt-oss-120b"):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = model
        self.max_tokens = 5000

    def chat(self, user_message: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 0.7) -> str:
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=temperature,
                max_tokens=self.max_tokens
            )
            response = completion.choices[0].message.content.strip()
            return response
        except Exception as e:
            print(f"❌ Error: {e}")
            return str(e)

    def get_model_name(self):
        return self.model


if __name__ == "__main__":
    llm = LLMClient()
    print(f"Using model: {llm.get_model_name()}")
    response = llm.chat("Say hello and confirm the model name.")
    print(response)