import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm_client import LLMClient

llm = LLMClient()

print("=== Prompt Engineering Tests ===\n")

# Test 1: Basic
print("1. Basic prompt:")
response = llm.chat("What is one key challenge in aerospace engineering change management?")
print(response, "\n")

# Test 2: Role prompting
print("2. Role prompting:")
response = llm.chat(
    "Explain the impact of a material change on manufacturing.",
    system_prompt="You are an experienced Aerospace Program Manager with 15 years in development-to-manufacturing transitions."
)
print(response, "\n")