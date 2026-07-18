import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def continue_ims():
    filename = "maap1_integrated_master_schedule.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Continuation: {filename}")
    print('='*70)

    with open(filepath, "r", encoding="utf-8") as f:
        existing_content = f.read()

    context = existing_content[-3500:] if len(existing_content) > 3500 else existing_content

    continuation_prompt = f"""Continue the Integrated Master Schedule (IMS) for the AetherForge MAAP-1 program exactly from where the current document ends.

Here is the end of the existing document:

{context}

Instructions:
- Continue directly from the last incomplete section.
- Maintain the same professional tone, formatting, and level of detail.
- Include realistic timelines, dependencies, and key milestones.
- Do not repeat anything that was already written.
- Output ONLY the continuation in clean markdown.

Continue from this point:"""

    try:
        new_content = claude.chat(
            continuation_prompt,
            system_prompt="You are a senior aerospace program manager. Continue program schedules professionally and logically. Output only the final markdown continuation."
        )

        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n" + new_content)

        print(f"✅ Continuation appended to: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    continue_ims()