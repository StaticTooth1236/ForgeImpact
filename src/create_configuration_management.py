import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def create_configuration_management():
    print("\n" + "="*70)
    print("Creating: maap1_configuration_management_plan.md (16k token limit)")
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
        with open("data/maap1_bill_of_materials.md", "r") as f:
            bom = f.read()
    except FileNotFoundError:
        bom = ""

    prompt = f"""You are a senior aerospace configuration management (CM) expert with experience on complex development and production programs.

Create a comprehensive **Configuration Management Plan** for the AetherForge MAAP-1 program.

Use the Program Requirements Baseline, Key Specifications, and Bill of Materials as the source of truth for consistency.

The document should include:
- CM organization and responsibilities
- Configuration identification (how items are identified and named)
- Baseline management (Functional, Allocated, and Product Baselines)
- Change control process (including Engineering Change Requests and how they flow through the CCB)
- Configuration status accounting and reporting
- Configuration verification and audits (FCA and PCA)
- Interface control and management
- How CM supports modular design and rapid iteration
- Relationship between CM and the drawing tree / BOM
- Tools and systems used for CM
- CM requirements during development vs production phases

Write in a professional, structured format suitable for a real aerospace program.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}

Bill of Materials:
{bom}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace Configuration Management expert. Create detailed, consistent, and professional CM documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_configuration_management_plan.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_configuration_management()