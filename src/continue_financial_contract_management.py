import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def continue_financial_contract_management():
    print("\n" + "="*70)
    print("Continuing: maap1_financial_and_contract_management.md (16k token limit)")
    print("="*70)

    # Load existing (possibly truncated) document
    with open("data/maap1_financial_and_contract_management.md", "r") as f:
        existing_content = f.read()

    # Load source of truth documents
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

    prompt = f"""You are continuing a technical Financial and Contract Management document.

The document below is truncated. Continue writing the **Financial and Contract Management** document from where it left off.

Maintain the same professional style and ensure consistency with the Program Requirements Baseline and Key Specifications. Focus on Firm Fixed Price realities, margin protection, cash flow, and practical KPIs.

Do not repeat content that is already complete. Just continue from the last unfinished section.

Existing (truncated) Financial and Contract Management document:
{existing_content}

Program Requirements Baseline (Source of Truth):
{prb}

Key Specifications:
{key_specs}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace Program Vice President experienced in Firm Fixed Price programs. Continue the document professionally and maintain consistency with the provided source documents.",
            max_tokens=16000
        )

        # Append the continuation
        with open("data/maap1_financial_and_contract_management.md", "a") as f:
            f.write("\n\n" + response)

        print("✅ Successfully appended continuation to maap1_financial_and_contract_management.md")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    continue_financial_contract_management()