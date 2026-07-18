import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def generate_key_specifications():
    print("\n" + "="*70)
    print("Expanding: maap1_key_specifications.md (using PRB as source of truth)")
    print("="*70)

    # Load the source of truth
    try:
        with open("data/maap1_program_requirements_baseline.md", "r") as f:
            prb_content = f.read()
        with open("data/maap1_program_requirements_baseline_continuation.md", "r") as f:
            prb_content += "\n\n" + f.read()
    except FileNotFoundError:
        print("⚠️ Warning: Could not find Program Requirements Baseline files.")
        prb_content = ""

    prompt = f"""You are a senior aerospace systems engineer.

Using the Program Requirements Baseline below as the **source of truth**, create a detailed and professional **Key Specifications** document for the AetherForge MAAP-1.

Focus especially on extracting and expanding performance-related specifications such as:
- Maximum Takeoff Weight (MTOW)
- Payload capacity (internal and external)
- Range (ferry and mission range)
- Endurance
- Cruise speed and maximum speed
- Service ceiling
- Rate of climb
- Hover performance
- Fuel system and consumption rates

Make the specifications realistic for a heavy-lift tandem-rotor helicopter while staying consistent with the requirements and constraints defined in the Program Requirements Baseline.

Program Requirements Baseline (Source of Truth):
{prb_content}

Write the Key Specifications document in a clear, technical format."""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace systems engineer. Maintain strict consistency with the provided Program Requirements Baseline."
        )

        filepath = "data/maap1_key_specifications.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully created/expanded: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_key_specifications()