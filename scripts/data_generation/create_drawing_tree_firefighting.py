import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def create_drawing_tree_firefighting():
    print("\n" + "="*70)
    print("Creating: maap1_drawing_tree_firefighting.md (16k token limit)")
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

    prompt = f"""You are a senior aerospace systems engineer creating detailed configuration documentation.

Create a comprehensive and professional **Drawing Tree / Configuration Breakdown** for the **Firefighting variant** of the AetherForge MAAP-1 Tandem-Rotor Heavy-Lift Autonomous Helicopter.

Base configuration: Tandem rotors (forward + aft), lightweight composite drone-style body, advanced turboshaft propulsion.

Go down to at least **Level 4** (and Level 5 where useful). Focus heavily on firefighting mission systems such as water/retardant tanks, scooping mechanisms, retardant delivery systems, and specialized wildfire sensors.

Use the Program Requirements Baseline and Key Specifications below as the source of truth for consistency. Maintain professional aerospace terminology.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace systems engineer. Create detailed, realistic, and professional drawing trees using proper aerospace terminology.",
            max_tokens=16000
        )

        filepath = "data/maap1_drawing_tree_firefighting.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_drawing_tree_firefighting()