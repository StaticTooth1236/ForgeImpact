import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm_client import LLMClient

llm = LLMClient()

def generate_document(prompt: str, filename: str):
    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)
    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace program manager with deep experience in complex rotorcraft and autonomous systems programs. Create clear, authoritative, and detailed program documentation."
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
    print("=== Regenerating MAAP-1 Program Requirements Baseline ===\n")

    generate_document(
        prompt="""Create a detailed and authoritative Program Requirements Baseline for the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter program.

This document is the single source of truth for the entire program. It should clearly and specifically define:

- Overall program vision, objectives, and strategic priorities
- Key performance parameters and constraints (including range, payload, endurance, speed, operating environment, etc.)
- Clear differentiation between the three variants:
  - Firefighting variant (focused on water/retardant operations)
  - ISR variant (intelligence, surveillance, and reconnaissance)
  - Cargo variant (military logistics and transport)
- High-level manufacturing and design philosophy (e.g., extensive use of advanced composites, modular architecture, maintainability, and producibility)
- Overall Make vs Buy strategy and philosophy at the program level
- Major certification, airworthiness, regulatory, and export control considerations
- High-level approach to risk, cost, and schedule management

Write in a formal, professional tone suitable for program management and engineering leadership. The level of detail and clarity should directly support the creation of high-quality downstream documents, such as multi-level Drawing Trees and detailed Bills of Materials.""",
        filename="maap1_program_requirements_baseline.md"
    )

    print("\n✅ Program Requirements Baseline regenerated successfully!")