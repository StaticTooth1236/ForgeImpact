import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

class ClaudeClient:
    def __init__(self, model: str = "claude-3-5-sonnet-20241022"):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = model
        self.max_tokens = 7000

    def chat(self, user_message: str, system_prompt: str = "You are a helpful assistant.", 
             temperature: float = 0.7, max_tokens: int = None) -> str:
        try:
            tokens = max_tokens if max_tokens is not None else self.max_tokens

            message = self.client.messages.create(
                model=self.model,
                max_tokens=tokens,
                temperature=temperature,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )
            return message.content[0].text.strip()
        except Exception as e:
            print(f"❌ Claude Error: {e}")
            return str(e)

    def get_model_name(self):
        return self.model