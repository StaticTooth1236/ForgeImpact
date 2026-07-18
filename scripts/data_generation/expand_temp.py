import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def expand_temp():
    print("\n" + "="*70)
    print("Expanding: maap1_test_evaluation_master_plan.md (16k token limit)")
    print("="*70)

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

    prompt = f"""You are a senior aerospace test & evaluation manager.

Create a comprehensive **Test & Evaluation Master Plan (TEMP)** for the AetherForge MAAP-1 program.

Use the Program Requirements Baseline, Key Specifications, and Integrated Master Schedule as the source of truth for consistency.

The document should include:
- Overall test philosophy and strategy
- Major test phases (ground test, flight test, payload integration, swarm testing, environmental qualification)
- Key test objectives tied to KPPs and program milestones
- Relationship between testing and risk reduction
- How testing supports both civilian (wildfire) and military certification paths
- High-level test assets and resource needs
- Success criteria for major test events

Write in a professional, structured format suitable for a real aerospace program.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}

Integrated Master Schedule:
{ims}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace Test & Evaluation manager. Create detailed, consistent, and professional TEMP documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_test_evaluation_master_plan.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully expanded: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    expand_temp()