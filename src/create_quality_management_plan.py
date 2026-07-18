import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def create_quality_management_plan():
    print("\n" + "="*70)
    print("Creating: maap1_quality_management_plan.md (16k token limit)")
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
        with open("data/maap1_configuration_management_plan.md", "r") as f:
            cm = f.read()
    except FileNotFoundError:
        cm = ""

    prompt = f"""You are a senior aerospace Quality Assurance manager with extensive experience on complex development and production programs.

Create a comprehensive **Quality Management Plan** for the AetherForge MAAP-1 program.

Use the Program Requirements Baseline, Key Specifications, Manufacturing Ramp Plan, and Configuration Management Plan as the source of truth for consistency.

The document should include:
- Quality policy, objectives, and organizational structure
- Quality management system framework (aligned with AS9100 / ISO 9001)
- Quality planning across program phases (development vs production)
- Design assurance and design verification/validation processes
- Manufacturing quality controls and process control
- Supplier quality management and incoming inspection
- Non-conformance management and corrective/preventive action
- Quality audits (internal and external)
- Quality records and documentation requirements
- Metrics and Key Performance Indicators (KPIs) for quality
- How quality integrates with Configuration Management and risk management

Write in a professional, structured format suitable for a real aerospace program.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}

Manufacturing Ramp Plan:
{mfg}

Configuration Management Plan:
{cm}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace Quality Assurance manager. Create detailed, consistent, and professional quality management documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_quality_management_plan.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_quality_management_plan()