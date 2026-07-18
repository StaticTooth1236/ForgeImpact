import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def continue_drawing_tree_firefighting():
    print("\n" + "="*70)
    print("Continuing: maap1_drawing_tree_firefighting.md (16k token limit)")
    print("="*70)

    with open("data/maap1_drawing_tree_firefighting.md", "r") as f:
        existing_content = f.read()

    with open("data/maap1_program_requirements_baseline.md", "r") as f:
        prb = f.read()
    try:
        with open("data/maap1_program_requirements_baseline_continuation.md", "r") as f:
            prb += "\n\n" + f.read()
    except FileNotFoundError:
        pass

    try:
        with open("data/maap1_key_specifications.md", "r") as f:
            key_specs = f.read()
    except FileNotFoundError:
        key_specs = ""

    prompt = f"""You are continuing a technical Drawing Tree / Configuration Breakdown document.

The document below is truncated. Continue writing the **Drawing Tree for the Firefighting variant** from where it left off.

Maintain consistency with the Program Requirements Baseline and Key Specifications. Use professional aerospace terminology.

Do not repeat content that is already complete. Just continue from the last unfinished section.

Existing (truncated) Firefighting Drawing Tree:
{existing_content}

Program Requirements Baseline (Source of Truth):
{prb}

Key Specifications:
{key_specs}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace systems engineer. Continue the document professionally and maintain consistency with the provided source documents.",
            max_tokens=16000
        )

        with open("data/maap1_drawing_tree_firefighting.md", "a") as f:
            f.write("\n\n" + response)

        print("✅ Successfully appended continuation to maap1_drawing_tree_firefighting.md")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    continue_drawing_tree_firefighting()