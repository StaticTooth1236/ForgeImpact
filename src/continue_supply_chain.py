import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def continue_supply_chain():
    print("\n" + "="*70)
    print("Continuing: maap1_supply_chain_procurement_plan.md (16k token limit)")
    print("="*70)

    with open("data/maap1_supply_chain_procurement_plan.md", "r") as f:
        existing_content = f.read()

    with open("data/maap1_program_requirements_baseline.md", "r") as f:
        prb = f.read()
    try:
        with open("data/maap1_program_requirements_baseline_continuation.md", "r") as f:
            prb += "\n\n" + f.read()
    except FileNotFoundError:
        pass

    prompt = f"""You are continuing a technical Supply Chain & Procurement Plan document.

The document below is truncated. Continue writing it from where it left off.

Maintain the same professional style and ensure consistency with the Program Requirements Baseline.

Do not repeat content that is already complete. Just continue from the last unfinished section.

Existing (truncated) Supply Chain Plan:
{existing_content}

Program Requirements Baseline (Source of Truth):
{prb}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace supply chain and procurement manager. Continue the document professionally and maintain consistency with the provided source documents.",
            max_tokens=16000
        )

        with open("data/maap1_supply_chain_procurement_plan.md", "a") as f:
            f.write("\n\n" + response)

        print("✅ Successfully appended continuation to maap1_supply_chain_procurement_plan.md")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    continue_supply_chain()