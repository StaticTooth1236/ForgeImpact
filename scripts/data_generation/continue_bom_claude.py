import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-4-5-20250929")

def continue_bom():
    filename = "maap1_bill_of_materials.md"
    filepath = f"data/{filename}"

    print(f"\n{'='*70}")
    print(f"Continuation: {filename}")
    print('='*70)

    with open(filepath, "r", encoding="utf-8") as f:
        existing_content = f.read()

    context = existing_content[-3500:] if len(existing_content) > 3500 else existing_content

    continuation_prompt = f"""Continue the Bill of Materials (BOM) for the AetherForge MAAP-1 program exactly from where the current document ends.

Here is the end of the existing document:

{context}

Instructions:
- Continue directly from the last incomplete section.
- Maintain the same professional formatting and hierarchy aligned with the Drawing Trees.
- Add more detail on subassemblies, Make vs Buy decisions, materials, and lead time categories.
- Include variant-specific items where relevant.
- Do not repeat anything already written.
- Output ONLY the continuation in clean markdown.

Continue from this point:"""

    try:
        new_content = claude.chat(
            continuation_prompt,
            system_prompt="You are a senior aerospace manufacturing engineer. Continue Bills of Materials with consistent structure and detail. Output only the final markdown continuation."
        )

        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n" + new_content)

        print(f"✅ Continuation appended to: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    continue_bom()