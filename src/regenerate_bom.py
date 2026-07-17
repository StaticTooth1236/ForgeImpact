import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm_client import LLMClient

llm = LLMClient()

def generate_document(prompt: str, filename: str):
    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)
    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace manufacturing engineer. Create a detailed, realistic Bill of Materials using proper aerospace terminology and clear Make vs Buy decisions."
        )
        filepath = f"data/{filename}"
        with open(filepath, "w") as f:
            f.write(response)
        print(f"✅ Successfully created: {filepath}")
        return response
    except Exception as e:
        print(f"❌ Error: {e}")
        return ""

if __name__ == "__main__":
    print("=== Regenerating Detailed Bill of Materials ===\n")

    generate_document(
        prompt="""Create a detailed and realistic Bill of Materials (BOM) for the AetherForge MAAP-1 program.

Structure it to clearly show:
- Common core items shared across all variants
- Variant-specific items for Firefighting, ISR, and Cargo

Base the structure on the three Drawing Trees. Organize by major subsystems. Include Make vs Buy decisions with rationale. Go down to major assemblies and key LRUs. Make it detailed enough to support manufacturing planning and engineering change impact analysis.""",
        filename="maap1_bill_of_materials.md"
    )

    print("\n✅ Detailed Bill of Materials regenerated successfully!")