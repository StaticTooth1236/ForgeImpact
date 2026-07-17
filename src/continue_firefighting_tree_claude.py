import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def continue_firefighting_tree():
    filename = "maap1_drawing_tree_firefighting.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Aggressive Continuation: {filename}")
    print('='*70)

    with open(filepath, "r", encoding="utf-8") as f:
        existing_content = f.read()

    context = existing_content[-3000:] if len(existing_content) > 3000 else existing_content

    continuation_prompt = f"""Significantly expand and continue the MAAP-1 Firefighting Variant Drawing Tree from where it currently ends. Do not repeat existing content.

Here is the end of the current document:

{context}

Instructions:
- Heavily expand all firefighting-specific systems (water/retardant tanks, scooping mechanisms, delivery systems, pumps, valves, plumbing, sensors, monitoring, and modular payload interfaces).
- Add proper Level 4 and Level 5 detail where it is currently shallow.
- Keep the exact same numbering style and professional formatting as the Cargo and ISR trees.
- Maintain consistency with the Program Requirements Baseline.
- Output ONLY the continuation in clean markdown. No extra explanations.

Continue and significantly expand the firefighting systems from this point:"""

    try:
        new_content = claude.chat(
            continuation_prompt,
            system_prompt="You are a senior aerospace systems engineer. Expand technical drawing tree documentation with high detail, especially on mission-specific systems. Output only the final markdown continuation."
        )

        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n" + new_content)

        print(f"✅ Aggressive continuation appended to: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    continue_firefighting_tree()