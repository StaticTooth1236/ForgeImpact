import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")   # More stable model

def continue_cargo_drawing_tree():
    filename = "maap1_drawing_tree_cargo.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Focused Continuation: {filename}")
    print('='*70)

    with open(filepath, "r", encoding="utf-8") as f:
        existing_content = f.read()

    context = existing_content[-3500:] if len(existing_content) > 3500 else existing_content

    continuation_prompt = f"""Continue and significantly expand the MAAP-1 Cargo Variant Drawing Tree exactly from where the current document ends.

Here is the end of the existing document:

{context}

Instructions:
- Continue directly from the last section. Do not repeat existing content.
- Keep the exact same numbering style, hierarchy, and professional aerospace formatting.
- Significantly expand all shallow common-core systems (Rotor System, Propulsion, Drive/Transmission, Flight Controls, Avionics, Fuel, Hydraulic, etc.).
- Add missing subsystems (Vehicle Health Management/HUMS, detailed electrical distribution & wiring, structural interfaces for mission kits, expanded cargo bay ECS, etc.).
- Stay fully consistent with the Program Requirements Baseline and the existing structure.
- Output ONLY the continuation in clean markdown. No extra text or thinking outside the drawing tree.

Continue and expand from this point:"""

    try:
        new_content = claude.chat(
            continuation_prompt,
            system_prompt="You are a senior aerospace systems engineer. Expand technical drawing tree documentation with high detail and consistent structure. Output only the final markdown continuation."
        )

        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n" + new_content)

        print(f"✅ Focused continuation appended to: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    continue_cargo_drawing_tree()