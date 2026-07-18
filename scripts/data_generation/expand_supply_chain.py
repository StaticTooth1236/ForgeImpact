import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def expand_supply_chain():
    print("\n" + "="*70)
    print("Expanding: maap1_supply_chain_procurement_plan.md (16k token limit)")
    print("="*70)

    with open("data/maap1_program_requirements_baseline.md", "r") as f:
        prb = f.read()
    try:
        with open("data/maap1_program_requirements_baseline_continuation.md", "r") as f:
            prb += "\n\n" + f.read()
    except FileNotFoundError:
        pass

    try:
        with open("data/maap1_bill_of_materials.md", "r") as f:
            bom = f.read()
    except FileNotFoundError:
        bom = ""

    try:
        with open("data/maap1_manufacturing_ramp_plan.md", "r") as f:
            mfg = f.read()
    except FileNotFoundError:
        mfg = ""

    prompt = f"""You are a senior aerospace supply chain and procurement manager.

Create a comprehensive **Supply Chain & Procurement Plan** for the AetherForge MAAP-1 program.

Use the Program Requirements Baseline, Bill of Materials, and Manufacturing Ramp Plan as the source of truth for consistency.

The document should include:
- Overall supply chain strategy and objectives
- Make-versus-buy philosophy
- Critical suppliers and long-lead items
- Procurement strategy by major subsystem (airframe, propulsion, avionics, mission systems)
- Risk mitigation for single-source and high-risk suppliers
- Export control and trusted supplier considerations
- Alignment with the manufacturing ramp and IMS
- Key procurement milestones

Write in a professional, structured format suitable for a real aerospace program.

Program Requirements Baseline:
{prb}

Bill of Materials:
{bom}

Manufacturing Ramp Plan:
{mfg}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace supply chain and procurement manager. Create detailed, consistent, and professional procurement documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_supply_chain_procurement_plan.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully expanded: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    expand_supply_chain()