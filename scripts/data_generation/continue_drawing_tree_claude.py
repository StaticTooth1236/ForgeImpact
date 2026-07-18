import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-5")

def continue_document(filename: str):
    print(f"\n{'='*70}")
    print(f"Continuing: {filename}")
    print('='*70)

    filepath = f"data/{filename}"

    with open(filepath, "r", encoding="utf-8") as f:
        existing_content = f.read()

    # Take the last ~3000 characters so Claude knows exactly where to continue
    context = existing_content[-3000:] if len(existing_content) > 3000 else existing_content

    continuation_prompt = f"""Continue the Drawing Tree document exactly from where it left off. 

Here is the end of the current document:

{context}

Instructions:
- Continue exactly from the last incomplete section.
- Maintain the exact same professional tone, formatting, and level of detail.
- Keep the same structure and heading hierarchy.
- Do not repeat anything that was already written.
- Reference the Program Requirements Baseline for consistency where relevant.
- Output ONLY the continuation in clean markdown. Do not add any extra explanations or thinking.

Continue from this point:"""

    try:
        new_content = claude.chat(
            continuation_prompt,
            system_prompt="You are a senior aerospace systems engineer. Continue technical drawing tree documentation with precision and consistent structure."
        )

        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n" + new_content)

        print(f"✅ Successfully appended continuation to: {filepath}")

    except Exception as e:
        print(f"❌ Error continuing {filename}: {e}")


if __name__ == "__main__":
    print("=== MAAP-1 Drawing Tree Continuation ===\n")

    # === Choose which file(s) to continue ===
    # You can run one at a time or uncomment multiple

    continue_document("maap1_drawing_tree_cargo.md")
    # continue_document("maap1_drawing_tree_isr.md")
    # continue_document("maap1_drawing_tree_firefighting.md")