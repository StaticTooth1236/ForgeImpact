import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm_client import LLMClient

llm = LLMClient()

def generate_document(prompt: str, filename: str):
    print(f"\n{'='*60}")
    print(f"Generating: {filename}")
    print('='*60)
    
    response = llm.chat(
        prompt, 
        system_prompt="You are a senior aerospace program manager with 20+ years of experience writing professional, detailed, and interconnected program documentation."
    )
    
    filepath = f"data/{filename}"
    with open(filepath, "w") as f:
        f.write(response)
    
    print(f"✅ Successfully created: {filepath}")
    return response


if __name__ == "__main__":
    print("=== MAAP-1 Program Document Generator ===\n")
    
    # ============================================================
    # DOCUMENT 1: Program Overview (Foundation)
    # ============================================================
    generate_document(
        prompt="""Write a comprehensive but high-level Program Overview for the AetherForge MAAP-1 Modular Autonomous Aerial Platform Swarm System.

Include:
- Overall program purpose and vision
- Key capabilities (modular payloads, swarm operations, mobile base)
- Dual-use nature (wildfire response + military logistics/ISR)
- High-level system architecture
- Strategic importance

Write in a professional tone suitable for program managers and executives.""",
        filename="maap1_program_overview.md"
    )

        # ============================================================
    # DOCUMENT 2: Key Specifications (UPDATED - More Realistic)
    # ============================================================
    generate_document(
        prompt="""Write a detailed and realistic Key Specifications document for the AetherForge MAAP-1 heavy-lift autonomous helicopter.

Use the following guidelines for realism:
- Propulsion: Advanced turboshaft engine (modern, fuel-efficient turboshaft)
- Range: Significantly longer than 200 nm — aim for something more operationally useful for trailer-based operations, water scooping, and logistics missions (suggest 300–450 nm range with reserves)
- Payload capacity: 5,000–8,000 lbs depending on mission and configuration
- Max Takeoff Weight: In the 18,000–25,000 lb class
- Endurance: 5–8 hours depending on payload and mission profile
- Cruise speed: 140–160 knots
- Service ceiling: 10,000–15,000 ft
- Designed for frequent operations from modified 18-wheeler trailers (mobile forward operating base)

Include realistic values for:
- Dimensions and weights
- Propulsion system and performance
- Payload capacity (by module type: firefighting, logistics, ISR)
- Range, endurance, and speed
- Key subsystems and avionics
- Environmental operating limits

Reference the Program Overview where appropriate. Make the specifications feel credible for a next-generation heavy-lift autonomous helicopter.""",
        filename="maap1_key_specifications.md"
    )

    print("\n✅ Updated Key Specifications generated!")

        # ============================================================
    # DOCUMENT 3: Integrated Master Schedule (REALISTIC VERSION)
    # ============================================================
    generate_document(
        prompt="""Create a realistic and detailed Integrated Master Schedule (IMS) for the AetherForge MAAP-1 program.

Use conservative but credible production rates for a new heavy-lift autonomous helicopter program.

Include:
- Major program phases with realistic timelines
- Key milestones (PDR, CDR, First Flight, IOC, etc.)
- Low-Rate Initial Production (LRIP) quantities (suggest 8–12 aircraft total)
- Full Rate Production ramp that starts conservatively and grows gradually over several years
- Realistic mature production rate (suggest peaking around 80–120 aircraft per year)
- Clear breakdown between Firefighting and Military variants
- Number of aircraft allocated to flight test, structural test, and qualification
- How customer demand influences the schedule and production quantities

Make the ramp feel believable for a complex rotorcraft program. Reference the Program Overview, Key Specifications, and Customer Demand Forecast.""",
        filename="maap1_integrated_master_schedule.md"
    )

    print("\n✅ Realistic Integrated Master Schedule generated!")

    # ============================================================
    # DOCUMENT 4: Bill of Materials (with Make vs Buy)
    # ============================================================
    generate_document(
        prompt="""Create a high-level Bill of Materials (BOM) for the MAAP-1 system with clear Make vs Buy categorization.

Structure the BOM by major subsystems (e.g., Airframe, Propulsion, Avionics, Modular Payload Interface, etc.).

For each major item, indicate:
- Make or Buy decision
- Brief rationale for the decision
- Criticality to the program

Reference the Key Specifications document. Focus on major assemblies rather than every single part.""",
        filename="maap1_bill_of_materials.md"
    )

    print("\n" + "="*60)
    print("✅ First batch of core documents generated successfully!")
    print("="*60)

    # ============================================================
    # DOCUMENT 5: Supply Chain Procurement Plan
    # ============================================================
    generate_document(
        prompt="""Create a Supply Chain Procurement Plan for the AetherForge MAAP-1 program.

Focus on the 'Buy' items from the Bill of Materials. Include:
- Key suppliers / supplier strategy
- Long-lead items and risk mitigation
- Qualification requirements for critical suppliers
- How procurement timelines connect to the Integrated Master Schedule
- Impact of potential engineering changes on the supply chain

Reference the Bill of Materials and Integrated Master Schedule documents.""",
        filename="maap1_supply_chain_procurement_plan.md"
    )

        # ============================================================
    # DOCUMENT 6: Manufacturing Ramp Plan (Aligned to IMS)
    # ============================================================
    generate_document(
        prompt="""Create a Manufacturing Rate Ramp-up Plan that is aligned with the quantities and timeline in the Integrated Master Schedule.

Use the following production quantities as guidance:
- LRIP: 8–12 aircraft total
- Year 1 of Full Rate: ~20 aircraft
- Year 2: ~30 aircraft
- Year 3: ~40 aircraft
- Year 4: ~60 aircraft
- Year 5: ~80 aircraft
- Mature rate: 80–120 aircraft per year

Include:
- How the 'Make' items from the Bill of Materials scale with production rate
- Key manufacturing processes and facility requirements
- Workforce and tooling ramp-up needs
- How engineering changes would impact the manufacturing ramp and schedule

Reference the Integrated Master Schedule and Bill of Materials.""",
        filename="maap1_manufacturing_ramp_plan.md"
    )

    print("\n✅ Manufacturing Ramp Plan regenerated and aligned with IMS!")

    # ============================================================
    # DOCUMENT 7: Safety Requirements
    # ============================================================
    generate_document(
        prompt="""Create a Safety Requirements document for the AetherForge MAAP-1 program.

Include:
- Top-level safety objectives and safety-critical functions
- Key safety requirements for flight, ground operations, and payload handling (especially firefighting and military logistics)
- How safety requirements flow down to subsystems and the Bill of Materials
- Safety considerations during manufacturing and ramp-up
- Relationship to airworthiness certification and customer (military vs civilian) requirements

Reference the Key Specifications, Bill of Materials, and Manufacturing Ramp Plan where relevant.""",
        filename="maap1_safety_requirements.md"
    )

    # ============================================================
    # DOCUMENT 8: Security Requirements
    # ============================================================
    generate_document(
        prompt="""Create a Security Requirements document for the AetherForge MAAP-1 program.

Include:
- Classification levels and handling of proprietary / sensitive information
- ITAR / export control considerations (especially for military logistics and ISR modules)
- Cybersecurity requirements for the autonomous systems and swarm operations
- Physical security and supply chain security requirements
- How security requirements impact the Bill of Materials, suppliers, and manufacturing

Reference the Bill of Materials, Supply Chain Procurement Plan, and Key Specifications where relevant.""",
        filename="maap1_security_requirements.md"
    )

    print("\n" + "="*60)
    print("✅ Safety and Security Requirements documents generated!")
    print("="*60)

    # ============================================================
    # DOCUMENT 9: Customer Demand Forecast
    # ============================================================
    generate_document(
        prompt="""Create a Customer Demand Forecast document for the AetherForge MAAP-1 program.

Include multiple customer types:
- Civilian / Wildfire Response agencies (federal, state, and commercial)
- Military / Defense customers (logistics and ISR missions)
- Potential international customers

For each customer segment, describe:
- Expected demand drivers
- How demand affects the Integrated Master Schedule and production ramp
- Key requirements or constraints from each customer type
- How changes in one customer segment could impact the overall program (e.g., surge in wildfire demand affecting military delivery timelines)

Reference the Integrated Master Schedule and Manufacturing Ramp Plan.""",
        filename="maap1_customer_demand_forecast.md"
    )

    print("\n✅ Customer Demand Forecast generated!")

    # ============================================================
    # DOCUMENT 10: Risk Register
    # ============================================================
    generate_document(
        prompt="""Create a Risk Register for the AetherForge MAAP-1 program.

Include 12–15 realistic program risks across different categories:
- Technical risks
- Schedule risks
- Supply chain / manufacturing risks
- Customer / demand risks
- Safety and certification risks
- Security / export control risks

For each risk include:
- Risk description
- Likelihood and consequence
- Risk owner
- Mitigation strategy
- How the risk connects to other program elements (e.g., IMS, BOM, Supply Chain, Manufacturing Ramp, or Customer Demand)

Make the risks feel realistic for a complex autonomous aerospace program with both civilian and military applications.""",
        filename="maap1_risk_register.md"
    )

    print("\n✅ Risk Register generated successfully!")

    # ============================================================
    # DOCUMENT 11: Test & Evaluation Master Plan (TEMP)
    # ============================================================
    generate_document(
        prompt="""Create a high-level Test & Evaluation Master Plan (TEMP) for the AetherForge MAAP-1 program.

Include:
- Overall test strategy and philosophy
- Major test phases (ground test, flight test, payload integration, swarm testing, environmental qualification)
- Key milestones tied to the Integrated Master Schedule
- How testing supports both civilian (wildfire) and military certification paths
- Relationship between testing and risk reduction

Reference the Integrated Master Schedule and Risk Register.""",
        filename="maap1_test_evaluation_master_plan.md"
    )

    print("\n✅ Test & Evaluation Master Plan generated!")

    # ============================================================
    # DOCUMENT 12: Drawing Tree / Configuration Breakdown
    # ============================================================
    generate_document(
        prompt="""Create a Drawing Tree / Configuration Breakdown document for the AetherForge MAAP-1 program.

Show how the top-level system breaks down into major subsystems and components. Include:
- Top-level system drawing
- Major subsystem breakdown (Airframe, Propulsion, Avionics, Modular Payload Interface, etc.)
- How configuration control works across the drawing tree
- How an engineering change (especially to a material or interface) would propagate through the drawing tree

Reference the Bill of Materials and Key Specifications.""",
        filename="maap1_drawing_tree.md"
    )

    print("\n✅ Drawing Tree document generated!")