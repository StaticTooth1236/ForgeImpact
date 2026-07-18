import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def create_vertical_integration_strategy():
    print("\n" + "="*70)
    print("Creating: maap1_vertical_integration_and_make_buy_strategy.md (16k token limit)")
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

    try:
        with open("data/maap1_bill_of_materials.md", "r") as f:
            bom = f.read()
    except FileNotFoundError:
        bom = ""

    prompt = f"""You are a senior aerospace executive with deep experience in vertical integration strategy for defense and aerospace programs (similar to companies like Anduril, SpaceX, and Lockheed Martin).

Create a strategic **Vertical Integration and Make vs Buy Strategy** document for the AetherForge MAAP-1 program.

Use the Program Requirements Baseline, Key Specifications, Manufacturing Ramp Plan, and Bill of Materials as the source of truth.

The document should include:
- Overall vertical integration philosophy and strategic rationale
- Core competencies the company should own internally
- Make vs Buy decision framework and criteria
- Key systems and components recommended for in-house development vs outsourcing
- Strategic benefits of vertical integration (speed, cost control, IP protection, quality)
- Risks and mitigation strategies of vertical integration
- Alignment with the manufacturing ramp plan and production strategy
- How vertical integration supports Firm Fixed Price contract execution and margin protection
- Phased approach to vertical integration over the program lifecycle
- Key decision points and governance for future make/buy decisions

Write in a clear, executive-level tone that would resonate with program vice presidents and business leaders.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}

Manufacturing Ramp Plan:
{mfg}

Bill of Materials:
{bom}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace executive experienced in vertical integration strategy. Create strategic, realistic, and high-value documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_vertical_integration_and_make_buy_strategy.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_vertical_integration_strategy()