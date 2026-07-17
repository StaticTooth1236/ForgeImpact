import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm_client import LLMClient

llm = LLMClient()

def generate_document(prompt: str, filename: str, context: str = ""):
    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)
    
    full_prompt = prompt
    if context:
        full_prompt = f"""Use the following summarized context from previously generated program documents to ensure consistency:

{context}

---

Now generate the requested document while maintaining logical alignment with the context above:

{prompt}"""

    try:
        response = llm.chat(
            full_prompt,
            system_prompt="You are a senior aerospace program manager. Create detailed, logically consistent program documentation."
        )
        filepath = f"data/{filename}"
        with open(filepath, "w") as f:
            f.write(response)
        print(f"✅ Successfully created: {filepath}")
        return response
    except Exception as e:
        print(f"❌ Error generating {filename}: {e}")
        return ""


if __name__ == "__main__":
    print("=== MAAP-1 Program Document Generator v2 ===\n")
    generated_context = ""

    # 1. Program Requirements Baseline (Improved)
    baseline = generate_document(
        prompt="""Create a detailed and authoritative Program Requirements Baseline for the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter program.

This document is the single source of truth. Clearly define:
- Overall program vision and strategic priorities
- Key performance parameters and constraints
- Differentiation between the three variants (Firefighting, ISR, Cargo)
- High-level manufacturing and design philosophy
- Make vs Buy direction
- Major certification and regulatory considerations

Write in a formal tone that supports high-quality downstream documents.""",
        filename="maap1_program_requirements_baseline.md"
    )
    summary = llm.chat(f"Summarize the key points of this document in 5-7 sentences:\n\n{baseline}")
    generated_context += f"\n\n=== Program Requirements Baseline Summary ===\n{summary}\n"

    # 2. Key Specifications
    specs = generate_document(
        prompt="""Write a detailed Key Specifications document. Reference the Program Requirements Baseline.""",
        filename="maap1_key_specifications.md",
        context=generated_context
    )
    summary = llm.chat(f"Summarize the key points of this document in 5-7 sentences:\n\n{specs}")
    generated_context += f"\n\n=== Key Specifications Summary ===\n{summary}\n"

    # 3. Integrated Master Schedule
    ims = generate_document(
        prompt="""Create a detailed Integrated Master Schedule. Reference the Program Requirements Baseline and Key Specifications.""",
        filename="maap1_integrated_master_schedule.md",
        context=generated_context
    )
    summary = llm.chat(f"Summarize the key points of this document in 5-7 sentences:\n\n{ims}")
    generated_context += f"\n\n=== Integrated Master Schedule Summary ===\n{summary}\n"

    # 4. Supply Chain Procurement Plan
    supply = generate_document(
        prompt="""Create a Supply Chain Procurement Plan. Reference the Program Requirements Baseline, Key Specifications, and Bill of Materials.""",
        filename="maap1_supply_chain_procurement_plan.md",
        context=generated_context
    )
    summary = llm.chat(f"Summarize the key points of this document in 5-7 sentences:\n\n{supply}")
    generated_context += f"\n\n=== Supply Chain Procurement Plan Summary ===\n{summary}\n"

    # 5. Manufacturing Ramp Plan
    mfg = generate_document(
        prompt="""Create a Manufacturing Rate Ramp-up Plan. Reference the Program Requirements Baseline, Integrated Master Schedule, and Bill of Materials.""",
        filename="maap1_manufacturing_ramp_plan.md",
        context=generated_context
    )
    summary = llm.chat(f"Summarize the key points of this document in 5-7 sentences:\n\n{mfg}")
    generated_context += f"\n\n=== Manufacturing Ramp Plan Summary ===\n{summary}\n"

    print("\n✅ Core supporting documents generated successfully!")