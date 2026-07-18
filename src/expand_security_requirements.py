import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def expand_security_requirements():
    print("\n" + "="*70)
    print("Expanding: maap1_security_requirements.md (16k token limit)")
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
        with open("data/maap1_supply_chain_procurement_plan.md", "r") as f:
            supply = f.read()
    except FileNotFoundError:
        supply = ""

    prompt = f"""You are a senior aerospace cybersecurity and program security engineer.

Create a comprehensive **Security Requirements** document for the AetherForge MAAP-1 program.

Use the Program Requirements Baseline and Key Specifications as the source of truth for consistency.

The document should include:
- Overall security philosophy and objectives
- Cybersecurity requirements for the air vehicle, ground control station, and datalinks
- Autonomy and mission systems security
- Supply chain security and trusted supplier requirements
- Export control considerations (ITAR/EAR)
- Information security and data handling requirements
- Physical security considerations for mobile bases and ground support equipment
- Relationship to certification and operational security (OPSEC)
- Key security milestones and compliance activities

Write in a professional, structured format suitable for a real aerospace / defense program.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}

Supply Chain Procurement Plan (for context):
{supply}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace cybersecurity and program security engineer. Create detailed, consistent, and professional security requirements documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_security_requirements.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully expanded: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    expand_security_requirements()