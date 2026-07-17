import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-5")

def continue_document(existing_file: str, new_content_filename: str = None):
    print(f"\n{'='*70}")
    print(f"Continuing document: {existing_file}")
    print('='*70)

    # Read the existing document
    with open(existing_file, "r", encoding="utf-8") as f:
        existing_content = f.read()

    # Take the last ~2500 characters as context so Claude knows where to continue
    context_snippet = existing_content[-2500:] if len(existing_content) > 2500 else existing_content

    continuation_prompt = f"""Continue writing the Program Requirements Baseline document exactly from where it left off.

Here is the end of the current document:

{context_snippet}

Instructions:
- Continue exactly from where the previous section ended.
- Maintain the exact same professional tone, formatting style, and level of detail.
- Keep the same structure and heading hierarchy.
- Do not repeat or summarize what was already written.
- Continue developing the document logically and completely until you reach a natural stopping point or complete the full document.

Begin continuing from this point:"""

    try:
        new_content = claude.chat(
            continuation_prompt,
            system_prompt="You are a senior aerospace program manager. Continue technical program documentation with precision, consistency, and professional structure."
        )

        # Append the new content to the existing file
        with open(existing_file, "a", encoding="utf-8") as f:
            f.write("\n" + new_content)

        print(f"✅ Successfully appended continuation to: {existing_file}")

        if new_content_filename:
            with open(new_content_filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ Also saved new content to: {new_content_filename}")

        return new_content

    except Exception as e:
        print(f"❌ Error during continuation: {e}")
        return ""


if __name__ == "__main__":
    print("=== Continuing MAAP-1 Program Requirements Baseline with Claude ===\n")

    # Path to the current (cut-off) baseline document
    baseline_file = "data/maap1_program_requirements_baseline.md"

    continue_document(
        existing_file=baseline_file,
        new_content_filename="data/maap1_program_requirements_baseline_continuation.md"  # Optional backup of just the new part
    )

    print("\n✅ Continuation complete. Please review the updated baseline document.")