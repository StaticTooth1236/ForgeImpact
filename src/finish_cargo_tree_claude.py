import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def finish_cargo_tree():
    filename = "maap1_drawing_tree_cargo.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Final Cleanup Continuation: {filename}")
    print('='*70)

    with open(filepath, "r", encoding="utf-8") as f:
        existing_content = f.read()

    # Only take the very end so Claude knows exactly where to pick up
    context = existing_content[-2000:]

    continuation_prompt = f"""Finish the MAAP-1 Cargo Variant Drawing Tree cleanly from where it currently ends. Do not repeat anything.

Here is the end of the current document:

{context}

Instructions:
- Continue directly from the last incomplete line ("276200  Maintenance Step").
- Complete the Ground Support Equipment section and add any logical final subsections if needed.
- Keep the exact same numbering style and professional formatting.
- Output ONLY the continuation in clean markdown. No extra text or explanations.

Finish the document from this point:"""

    try:
        new_content = claude.chat(
            continuation_prompt,
            system_prompt="You are a senior aerospace systems engineer. Complete the drawing tree cleanly and professionally. Output only the final markdown continuation."
        )

        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n" + new_content)

        print(f"✅ Cargo tree finished and cleaned up: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    finish_cargo_tree()