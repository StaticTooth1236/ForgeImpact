import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def continue_temp():
    print("\n" + "="*70)
    print("Continuing: maap1_test_evaluation_master_plan.md (16k token limit)")
    print("="*70)

    # Load existing (possibly truncated) document
    with open("data/maap1_test_evaluation_master_plan.md", "r") as f:
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

    try:
        with open("data/maap1_integrated_master_schedule.md", "r") as f:
            ims = f.read()
    except FileNotFoundError:
        ims = ""

    prompt = f"""You are continuing a technical Test & Evaluation Master Plan document.

The document below is truncated. Continue writing the **Test & Evaluation Master Plan** from where it left off.

Maintain the same professional style and ensure consistency with the Program Requirements Baseline, Key Specifications, and Integrated Master Schedule.

Do not repeat content that is already complete. Just continue from the last unfinished section.

Existing (truncated) TEMP:
{existing_content}

Program Requirements Baseline (Source of Truth):
{prb}

Key Specifications:
{key_specs}

Integrated Master Schedule:
{ims}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace Test & Evaluation manager. Continue the document professionally and maintain consistency with the provided source documents.",
            max_tokens=16000
        )

        # Append the continuation
        with open("data/maap1_test_evaluation_master_plan.md", "a") as f:
            f.write("\n\n" + response)

        print("✅ Successfully appended continuation to maap1_test_evaluation_master_plan.md")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    continue_temp()