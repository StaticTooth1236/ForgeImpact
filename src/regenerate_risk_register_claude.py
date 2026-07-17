import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def generate_risk_register():
    filename = "maap1_risk_register.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)

    prompt = """Create a detailed and professional Risk Register for the AetherForge MAAP-1 program.

Include:
- Risk ID
- Risk Title / Description
- Category (Technical, Schedule, Cost, Supply Chain, Manufacturing, Certification, etc.)
- Likelihood (Low / Medium / High)
- Consequence / Impact (Low / Medium / High)
- Risk Score / Priority
- Risk Owner
- Mitigation / Response Strategy
- Contingency Plan (if applicable)
- Status (Open / Monitoring / Closed)

Focus on realistic risks tied to the Program Requirements Baseline, Integrated Master Schedule, and Manufacturing Ramp Plan (e.g. production rate ramp-up risks, long-lead items, certification challenges, autonomy development risks, supply chain risks, etc.). Output the full document in clean, professional markdown."""

    try:
        response = claude.chat(
            prompt,
            system_prompt="You are a senior aerospace program risk manager. Create detailed, realistic risk registers aligned with program documentation. Output only clean markdown."
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    generate_risk_register()