import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def continue_key_specifications():
    print("\n" + "="*70)
    print("Continuing: maap1_key_specifications.md (16k token limit)")
    print("="*70)

    # Load existing (truncated) document
    with open("data/maap1_key_specifications.md", "r") as f:
        existing_content = f.read()

    # Load source of truth (Program Requirements Baseline)
    with open("data/maap1_program_requirements_baseline.md", "r") as f:
        prb = f.read()
    try:
        with open("data/maap1_program_requirements_baseline_continuation.md", "r") as f:
            prb += "\n\n" + f.read()
    except FileNotFoundError:
        pass

    prompt = f"""You are continuing a technical document.

The document below is truncated. Continue writing the **Key Specifications** document from where it left off.

Focus on completing any missing performance specifications (range, payload, speed, endurance, hover performance, fuel system, etc.) while staying consistent with the Program Requirements Baseline.

Existing (truncated) Key Specifications:
{existing_content}

Program Requirements Baseline (Source of Truth):
{prb}

Continue the document in the same professional style. Do not repeat content that is already complete."""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace systems engineer. Continue the document professionally and maintain consistency with the Program Requirements Baseline.",
            max_tokens=16000   # Increased to 16k tokens
        )

        # Append the continuation
        with open("data/maap1_key_specifications.md", "a") as f:
            f.write("\n\n" + response)

        print("✅ Successfully appended continuation to maap1_key_specifications.md")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    continue_key_specifications()