import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient

llm = ClaudeClient()

def expand_financial_contract_management():
    print("\n" + "="*70)
    print("Creating: maap1_financial_and_contract_management.md (16k token limit)")
    print("="*70)

    # Load key source documents
    with open("data/maap1_program_requirements_baseline.md", "r") as f:
        prb = f.read()
    try:
        with open("data/maap1_program_requirements_baseline_continuation.md", "r") as f:
            prb += "\n\n" + f.read()
    except FileNotFoundError:
        pass

    try:
        with open("data/maap1_key_specifications.md", "r") as f:
            key_specs = f.read()
    except FileNotFoundError:
        key_specs = ""

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

    prompt = f"""You are a senior aerospace program vice president with extensive experience running Firm Fixed Price (FFP) development and production programs.

Create a professional **Financial and Contract Management** document for the AetherForge MAAP-1 program.

The document must reflect modern defense/aerospace thinking (especially relevant to companies like Anduril):
- Focus on **Firm Fixed Price** contract structures
- Emphasize margin protection, cash discipline, and risk management rather than traditional EVMS
- Include both high-level KPIs that Program Vice Presidents care about and practical KPIs that mid-level program managers use day-to-day

Document should cover:
- Contract type and key assumptions (FFP with potential incentives/penalties)
- Milestone payment structure and cash flow profile
- Target gross margin and sensitivity analysis
- How engineering changes and risks impact program margin and cash
- Key Financial KPIs for Program Vice Presidents (margin, cash flow, working capital, risk reserve usage)
- Key Program Execution KPIs for mid-level managers (cost/schedule performance at control account level, change order margin impact, supplier cost performance, etc.)
- Risk and opportunity management from a financial perspective
- Reporting and governance cadence with the customer

Write in a clear, professional tone suitable for both executive and working-level audiences.

Program Requirements Baseline:
{prb}

Key Specifications:
{key_specs}

Integrated Master Schedule:
{ims}

Manufacturing Ramp Plan:
{mfg}
"""

    try:
        response = llm.chat(
            prompt,
            system_prompt="You are a senior aerospace Program Vice President experienced in Firm Fixed Price programs. Create clear, realistic, and high-value financial and contractual documentation.",
            max_tokens=16000
        )

        filepath = "data/maap1_financial_and_contract_management.md"
        with open(filepath, "w") as f:
            f.write(response)

        print(f"✅ Successfully created: {filepath}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    expand_financial_contract_management()