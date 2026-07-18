import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def generate_manufacturing_ramp():
    filename = "maap1_manufacturing_ramp_plan.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)

    prompt = """Create a detailed and professional Manufacturing Rate Ramp-up Plan for the AetherForge MAAP-1 program.

Include:
- Phased production ramp strategy (LRIP → Full Rate Production)
- Production rate targets by year/phase
- Key enablers and constraints (facilities, tooling, workforce, supply chain)
- Learning curve assumptions
- Risk mitigation for rate increases
- Linkage to the Integrated Master Schedule and customer demand forecast

Reference the Program Requirements Baseline and the Integrated Master Schedule for overall timelines and quantities. Output the full document in clean, professional markdown."""

    try:
        response = claude.chat(
            prompt,
            system_prompt="You are a senior aerospace manufacturing program manager. Create detailed, realistic manufacturing ramp plans aligned with program schedules. Output only clean markdown."
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    generate_manufacturing_ramp()