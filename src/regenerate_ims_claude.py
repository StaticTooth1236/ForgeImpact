import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def generate_ims():
    filename = "maap1_integrated_master_schedule.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)

    prompt = """Create a detailed and professional Integrated Master Schedule (IMS) for the AetherForge MAAP-1 program.

Include:
- Major program phases and timelines (from Program Requirements Baseline)
- Key milestones (PDR, CDR, First Flight, LRIP, FRP, IOC, etc.)
- Phased development, testing, qualification, and production ramp-up
- Clear linkage between engineering, manufacturing, and customer demand
- Realistic durations and dependencies

Reference the Program Requirements Baseline for overall program timeline and production quantities. Output the full document in clean, professional markdown."""

    try:
        response = claude.chat(
            prompt,
            system_prompt="You are a senior aerospace program manager. Create detailed, realistic, and professional program schedules in clean markdown format."
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    generate_ims()