import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def generate_isr_tree():
    filename = "maap1_drawing_tree_isr.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)

    prompt = """Create a detailed and realistic Drawing Tree / Configuration Breakdown for the ISR variant of the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter.

Reference the improved Program Requirements Baseline for variant-specific requirements (sensor suite, data links, mission computers, edge processing, etc.). Use the common tandem-rotor core (forward + aft rotors, lightweight composite body, advanced turboshaft propulsion).

Go down to at least Level 4 (and Level 5 where useful). Focus heavily on ISR mission systems such as:
- Multi-spectral EO/IR sensor suites
- Synthetic Aperture Radar (SAR)
- SIGINT / COMINT / ELINT equipment
- Mission computers and data processing
- Data links (LOS + BLOS)
- Edge computing and storage
- ISR operator consoles and interfaces

Keep the structure consistent with the Cargo Drawing Tree style (clear hierarchy, professional aerospace naming, common core vs variant-specific split). Output ONLY the final detailed drawing tree in clean markdown format."""

    try:
        response = claude.chat(
            prompt,
            system_prompt="You are a senior aerospace systems engineer. Create detailed, realistic drawing trees with proper hierarchy and professional terminology. Output only the final markdown."
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    generate_isr_tree()