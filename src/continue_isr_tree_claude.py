import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def continue_isr_tree():
    filename = "maap1_drawing_tree_isr.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Focused Continuation: {filename}")
    print('='*70)

    with open(filepath, "r", encoding="utf-8") as f:
        existing_content = f.read()

    context = existing_content[-3500:] if len(existing_content) > 3500 else existing_content

    continuation_prompt = f"""Continue and significantly expand the MAAP-1 ISR Variant Drawing Tree exactly from where the current document ends.

Here is the end of the existing document:

{context}

Instructions:
- Continue directly from the last section. Do not repeat any existing content.
- Keep the exact same numbering style, hierarchy, and professional aerospace formatting.
- Significantly expand all shallow sections, especially ISR-specific systems (sensor suites, mission computers, data links, edge processing, SIGINT/COMINT/ELINT, operator interfaces, etc.).
- Add any missing supporting subsystems (HUMS integration, detailed data distribution, mission kit interfaces, etc.).
- Maintain full consistency with the Program Requirements Baseline and the style of the Cargo Drawing Tree.
- Output ONLY the continuation in clean markdown. No extra text or thinking.

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
    continue_isr_tree()