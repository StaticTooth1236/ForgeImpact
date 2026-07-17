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
            system_prompt="You are a senior aerospace systems engineer with experience in complex rotorcraft programs. Create detailed, realistic, and professional drawing trees using proper aerospace terminology and clear subsystem hierarchy."
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
    print("=== Regenerating MAAP-1 Drawing Trees ===\n")

    # Firefighting Variant
    generate_document(
        prompt="""Create a detailed and realistic Drawing Tree / Configuration Breakdown for the Firefighting variant of the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter.

Base configuration: Tandem rotors (forward + aft), lightweight composite drone-style body, advanced turboshaft propulsion.

Reference the improved Program Requirements Baseline for variant-specific mission requirements. Go down to at least Level 4 (and Level 5 where useful). Focus on firefighting mission systems such as water/retardant tanks, scooping mechanisms, delivery systems, pumps, and specialized sensors. Use professional aerospace naming and clear subsystem hierarchy.""",
        filename="maap1_drawing_tree_firefighting.md"
    )

    # ISR Variant
    generate_document(
        prompt="""Create a detailed and realistic Drawing Tree / Configuration Breakdown for the ISR variant of the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter.

Base configuration: Tandem rotors (forward + aft), lightweight composite drone-style body, advanced turboshaft propulsion.

Reference the improved Program Requirements Baseline for variant-specific mission requirements. Go down to at least Level 4 (and Level 5 where useful). Focus heavily on ISR mission systems such as sensor suites, mission computers, data links, EO/IR, SAR, SIGINT/ELINT, and associated processing equipment. Use professional aerospace naming and clear subsystem hierarchy.""",
        filename="maap1_drawing_tree_isr.md"
    )

    # Cargo Variant
    generate_document(
        prompt="""Create a detailed and realistic Drawing Tree / Configuration Breakdown for the Cargo variant of the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter (military logistics).

Base configuration: Tandem rotors (forward + aft), lightweight composite drone-style body, advanced turboshaft propulsion.

Reference the improved Program Requirements Baseline for variant-specific mission requirements. Go down to at least Level 4 (and Level 5 where useful). Focus on cargo handling systems such as internal cargo systems, external sling/load systems, reinforced structure, tie-downs, and military communications. Use professional aerospace naming and clear subsystem hierarchy.""",
        filename="maap1_drawing_tree_cargo.md"
    )

    print("\n✅ All three Drawing Trees regenerated successfully!")