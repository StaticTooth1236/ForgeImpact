import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def expand_safety_requirements():
    print("\n" + "="*70)
    print("Expanding: maap1_safety_requirements.md (16k token limit)")
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
        with open("data/maap1_manufacturing_ramp_plan.md", "r") as f:
            mfg = f.read()
    except FileNotFoundError:
        mfg = ""

    prompt = f"""You are a senior aerospace safety engineer.

Create a comprehensive **Safety Requirements** document for the AetherForge MAAP-1 program.

Use the Program Requirements Baseline and Key Specifications as the source of truth for consistency.

The document should include:
- Overall safety philosophy and objectives
- System safety requirements (airworthiness, crashworthiness, fire protection)
- Autonomy-related safety requirements (detect-and-avoid, lost-link behavior, fail-safe modes)
- Hazard identification and risk mitigation approach
- Safety-critical systems and DAL (Design Assurance Level) allocation guidance
- Ground and flight safety considerations
- Relationship to certification (civil and military paths)
- Key safety milestones tied to the program schedule

Write in a professional, structured format suitable for a real aerospace program.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}

Manufacturing Ramp Plan (for context):
{mfg}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace safety engineer. Create detailed, consistent, and professional safety requirements documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_safety_requirements.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully expanded: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    expand_safety_requirements()