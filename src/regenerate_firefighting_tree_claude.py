import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def generate_firefighting_tree():
    filename = "maap1_drawing_tree_firefighting.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)

    prompt = """Create a detailed and realistic Drawing Tree for the Firefighting variant of the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter.

Reference the Program Requirements Baseline. Use the common tandem-rotor core.

Focus on firefighting systems (water/retardant tanks, scooping mechanisms, delivery systems, pumps, valves, and firefighting sensors). Go to Level 4 and Level 5 where useful.

Keep the same style and structure as the Cargo and ISR drawing trees. Output the full drawing tree in clean markdown."""

    try:
        response = claude.chat(
            prompt,
            system_prompt="You are a senior aerospace systems engineer. Create detailed drawing trees. Output only the final markdown document."
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    generate_firefighting_tree()