import os
 
from dotenv import load_dotenv
import anthropic
 
load_dotenv()
 
 
class ClaudeClient:
    """Thin wrapper around the Anthropic API used by the specialized agents."""
 
    def __init__(self, model: str = "claude-sonnet-4-6"):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = model
        self.max_tokens = 7000
 
    def chat(
        self,
        user_message: str,
        system_prompt: str = "You are a helpful assistant.",
        temperature: float = 0.7,
        max_tokens: int = None,
    ) -> str:
        tokens = max_tokens if max_tokens is not None else self.max_tokens
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=tokens,
                temperature=temperature,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
            )
            return message.content[0].text.strip()
        except Exception as e:
            # Log AND re-raise. Never return an error string as if it were a
            # real answer — that silently poisons every downstream prompt.
            print(f"❌ Claude API error ({self.model}): {e}")
            raise
 
    def get_model_name(self):
        return self.model
 