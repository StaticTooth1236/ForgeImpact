import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

claude = ClaudeClient(model="claude-sonnet-5")

def generate_document(prompt: str, filename: str):
    print(f"\n{'='*70}")
    print(f"Generating: {filename}")
    print('='*70)
    try:
        response = claude.chat(
            prompt,
            system_prompt="You are a senior aerospace systems engineer. Create detailed, realistic, and professional drawing trees using proper aerospace terminology and clear subsystem hierarchy. Output ONLY the final markdown drawing tree. Do not include any internal thinking, reasoning steps, or explanations outside the final structured response."
        )
        filepath = f"data/{filename}"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response)
        print(f"✅ Successfully created: {filepath}")
        return response
    except Exception as e:
        print(f"❌ Error generating {filename}: {e}")
        return ""


if __name__ == "__main__":
    print("=== Regenerating MAAP-1 Drawing Trees with Claude ===\n")

    # Firefighting Variant
    generate_document(
        prompt="""Create a detailed and realistic Drawing Tree / Configuration Breakdown for the Firefighting variant of the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter.

Reference the improved Program Requirements Baseline for variant-specific requirements. Use the common tandem-rotor core (forward + aft rotors, lightweight composite body, advanced turboshaft propulsion).

Output ONLY the final detailed drawing tree in clean markdown format. Go down to at least Level 4 (and Level 5 where useful). Focus on firefighting mission systems (water/retardant tanks, scooping mechanisms, delivery systems, pumps, valves, specialized sensors, etc.). Use professional aerospace naming and clear subsystem hierarchy. Do not add any extra text, explanations, or thinking outside the drawing tree itself.""",
        filename="maap1_drawing_tree_firefighting.md"
    )

    # ISR Variant
    generate_document(
        prompt="""Create a detailed and realistic Drawing Tree / Configuration Breakdown for the ISR variant of the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter.

Reference the improved Program Requirements Baseline for variant-specific requirements. Use the common tandem-rotor core.

Output ONLY the final detailed drawing tree in clean markdown format. Go down to at least Level 4 (and Level 5 where useful). Focus heavily on ISR mission systems (sensor suites, mission computers, data links, EO/IR, SAR, SIGINT/ELINT, edge processing, etc.). Use professional aerospace naming and clear subsystem hierarchy. Do not add any extra text, explanations, or thinking outside the drawing tree itself.""",
        filename="maap1_drawing_tree_isr.md"
    )

    # Cargo Variant
    generate_document(
        prompt="""Create a detailed and realistic Drawing Tree / Configuration Breakdown for the Cargo variant of the AetherForge MAAP-1 tandem-rotor heavy-lift autonomous helicopter (military logistics).

Reference the improved Program Requirements Baseline for variant-specific requirements. Use the common tandem-rotor core.

Output ONLY the final detailed drawing tree in clean markdown format. Go down to at least Level 4 (and Level 5 where useful). Focus on cargo handling systems (internal cargo systems, external sling/load systems, reinforced structure, tie-downs, military communications, etc.). Use professional aerospace naming and clear subsystem hierarchy. Do not add any extra text, explanations, or thinking outside the drawing tree itself.""",
        filename="maap1_drawing_tree_cargo.md"
    )

    print("\n✅ All three Drawing Trees regenerated successfully with Claude!")