import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def expand_customer_demand():
    print("\n" + "="*70)
    print("Expanding: maap1_customer_demand_forecast.md (16k token limit)")
    print("="*70)

    with open("data/maap1_program_requirements_baseline.md", "r") as f:
        prb = f.read()
    try:
        with open("data/maap1_program_requirements_baseline_continuation.md", "r") as f:
            prb += "\n\n" + f.read()
    except FileNotFoundError:
        pass

    try:
        with open("data/maap1_integrated_master_schedule.md", "r") as f:
            ims = f.read()
    except FileNotFoundError:
        ims = ""

    try:
        with open("data/maap1_manufacturing_ramp_plan.md", "r") as f:
            mfg = f.read()
    except FileNotFoundError:
        mfg = ""

    prompt = f"""You are a senior aerospace program and business development manager.

Create a comprehensive **Customer Demand Forecast** document for the AetherForge MAAP-1 program.

Use the Program Requirements Baseline, Integrated Master Schedule, and Manufacturing Ramp Plan as the source of truth for consistency.

The document should include:
- Overall market and demand overview
- Primary customer segments (wildfire response agencies and military logistics/ISR customers)
- Demand forecast by variant (Firefighting, ISR, Cargo)
- Demand by year aligned with production ramp
- Key assumptions driving the forecast
- Relationship between customer demand and production quantities in the IMS
- Risks and uncertainties in the demand forecast
- Strategic implications for the program

Write in a professional, structured format suitable for a real aerospace program.

Program Requirements Baseline:
{prb}

Integrated Master Schedule:
{ims}

Manufacturing Ramp Plan:
{mfg}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace program and business development manager. Create detailed, consistent, and professional demand forecast documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_customer_demand_forecast.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully expanded: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    expand_customer_demand()