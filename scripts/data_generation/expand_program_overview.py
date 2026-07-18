import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def expand_program_overview():
    print("\n" + "="*70)
    print("Expanding: maap1_program_overview.md (16k token limit)")
    print("="*70)

    # Load source of truth
    with open("data/maap1_program_requirements_baseline.md", "r") as f:
        prb = f.read()
    try:
        with open("data/maap1_program_requirements_baseline_continuation.md", "r") as f:
            prb += "\n\n" + f.read()
    except FileNotFoundError:
        pass

    # Also load the newly expanded Key Specifications for consistency
    try:
        with open("data/maap1_key_specifications.md", "r") as f:
            key_specs = f.read()
    except FileNotFoundError:
        key_specs = ""

    prompt = f"""You are a senior aerospace program manager.

Create a comprehensive and professional **Program Overview** document for the AetherForge MAAP-1 Tandem-Rotor Heavy-Lift Autonomous Helicopter program.

Use the Program Requirements Baseline and Key Specifications below as the source of truth for consistency.

The document should include:
- Program vision and strategic purpose
- High-level system description
- Key capabilities (modular payloads, swarm operations, dual-use missions)
- Performance highlights (range, payload, speed, endurance)
- Variants (Firefighting, ISR, Cargo)
- Program status and key milestones
- Strategic importance and intended customers

Write in a clear, professional style suitable for both technical and non-technical stakeholders.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace program manager. Create detailed, consistent, and professional program documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_program_overview.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully expanded: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    expand_program_overview()