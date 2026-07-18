import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-5")

def generate_document(prompt: str, filename: str):
    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)
    try:
        response = claude.chat(
            prompt,
            system_prompt="You are a senior aerospace program manager. Create detailed, authoritative, and logically consistent program documentation."
        )
        filepath = f"data/{filename}"
        with open(filepath, "w") as f:
            f.write(response)
        print(f"✅ Successfully created: {filepath}")
        return response
    except Exception as e:
        print(f"❌ Error generating {filename}: {e}")
        return ""


if __name__ == "__main__":
    print("=== Regenerating MAAP-1 Program Requirements Baseline with Claude ===\n")

    generate_document(
        prompt="""Create a detailed and authoritative Program Requirements Baseline for the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter program.

This document is the single source of truth. It should clearly and specifically define:

- Overall program vision, objectives, and strategic priorities (make them specific and measurable where possible)
- Key performance parameters and constraints with clear thresholds and rationale (range, payload, endurance, speed, operating environment, etc.)
- Clear differentiation between the three variants (Firefighting, ISR, and Cargo), including unique systems, weight impacts, certification considerations, and production implications
- High-level manufacturing and design philosophy (focus on producibility, modularity, use of advanced composites, and maintainability)
- Make vs Buy strategy direction at the program level
- Major certification, regulatory, airworthiness, and export control requirements
- Overall approach to risk, cost, and schedule management

Write in a formal, professional tone suitable for program management and engineering leadership. The level of detail should support the creation of high-quality downstream documents such as multi-level Drawing Trees and detailed Bills of Materials.""",
        filename="maap1_program_requirements_baseline.md"
    )

    print("\n✅ Program Requirements Baseline regenerated successfully with Claude!")