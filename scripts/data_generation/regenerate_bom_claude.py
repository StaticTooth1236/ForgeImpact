import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def generate_bom():
    filename = "maap1_bill_of_materials.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)

    prompt = """Create a detailed and professional Bill of Materials (BOM) for the AetherForge MAAP-1 program.

Structure it with clear hierarchy aligned to the Drawing Trees (Airframe, Rotor Systems, Propulsion, Flight Controls, Mission Systems, etc.).

For each major assembly and subassembly include:
- Part number / Drawing reference
- Description
- Quantity per aircraft
- Make vs Buy decision
- Material / Key specifications
- Estimated unit cost range (where reasonable)
- Lead time category (long-lead, standard, etc.)

Focus especially on the common core platform and the variant-specific mission systems. Reference the Program Requirements Baseline and Drawing Trees for consistency. Output the full document in clean, professional markdown."""

    try:
        response = claude.chat(
            prompt,
            system_prompt="You are a senior aerospace manufacturing engineer. Create detailed, realistic Bills of Materials aligned with drawing trees and program requirements. Output only clean markdown."
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    generate_bom()