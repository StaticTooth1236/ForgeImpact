import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

class ClaudeClient:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = model

    def chat(self, prompt: str, system_prompt: str = None, max_tokens: int = 4000) -> str:
        messages = [{"role": "user", "content": prompt}]
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system_prompt if system_prompt else "You are a helpful assistant.",
            messages=messages
        )
        return response.content[0].text