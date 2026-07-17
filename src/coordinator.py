import sys
import os
from datetime import datetime
from typing import List, Dict

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.change_impact_agent import analyze_change_impact
from src.risk_schedule_impact_agent import analyze_risk_schedule_impact
from src.supply_chain_procurement_agent import analyze_supply_chain_impact
from src.manufacturing_production_agent import analyze_manufacturing_impact
from src.synthesis_agent import synthesize_change_analysis

# ====================== AVAILABLE AGENTS ======================
AVAILABLE_AGENTS = {
    "Change Impact": analyze_change_impact,
    "Risk & Schedule": analyze_risk_schedule_impact,
    "Supply Chain & Procurement": analyze_supply_chain_impact,
    "Manufacturing & Production": analyze_manufacturing_impact,
}


def run_selected_agents(change_description: str, selected_agents: List[str]) -> Dict[str, str]:
    results = {}
    for agent_name in selected_agents:
        if agent_name in AVAILABLE_AGENTS:
            print(f"\n{'='*60}")
            print(f"Running: {agent_name} Agent")
            print('='*60)
            try:
                result = AVAILABLE_AGENTS[agent_name](change_description)
                results[agent_name] = result
                print(f"✅ {agent_name} completed.")
            except Exception as e:
                results[agent_name] = f"Error: {str(e)}"
                print(f"❌ Error in {agent_name}")
        else:
            results[agent_name] = "Agent not found."
    return results


def save_combined_detailed_report(change_description: str, results: Dict[str, str]):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/combined_reports/Combined_Detailed_Analysis_{timestamp}.md"
    os.makedirs("outputs/combined_reports", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# MAAP-1 Multi-Agent Change Impact Analysis (Detailed)\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**Proposed Change:** {change_description}\n\n")
        f.write("---\n\n")
        for agent_name, result in results.items():
            f.write(f"## {agent_name} Agent\n\n")
            f.write(result)
            f.write("\n\n---\n\n")
    return filename


# ====================== MAIN COORDINATOR ======================
if __name__ == "__main__":
    print("\n=== MAAP-1 Multi-Agent Coordinator with Synthesis ===\n")

    change = input("Enter the proposed engineering change: ").strip()
    if not change or change.lower() in ["quit", "exit", "q"]:
        print("Exiting...")
        exit()

    print("\nAvailable Agents:")
    for i, name in enumerate(AVAILABLE_AGENTS.keys(), 1):
        print(f"  {i}. {name}")

    print("\nEnter numbers (comma separated) or type 'all':")
    selection = input("Selection: ").strip().lower()

    if selection == "all":
        selected = list(AVAILABLE_AGENTS.keys())
    else:
        try:
            indices = [int(x.strip()) for x in selection.split(",")]
            selected = [list(AVAILABLE_AGENTS.keys())[i-1] for i in indices]
        except:
            print("Invalid input. Running all agents.")
            selected = list(AVAILABLE_AGENTS.keys())

    # Step 1: Run selected agents
    print(f"\nRunning selected agents: {selected}")
    agent_results = run_selected_agents(change, selected)

    # Step 2: Save detailed combined report
    detailed_path = save_combined_detailed_report(change, agent_results)
    print(f"\n✅ Detailed agent reports saved to: {detailed_path}")

    # Step 3: Run Synthesis Agent
    print("\n" + "="*60)
    print("Running Synthesis Agent (Executive Summary + Project Plan)")
    print("="*60)

    try:
        synthesis_report = synthesize_change_analysis(change, agent_results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        synthesis_path = f"outputs/synthesis_reports/Synthesis_Report_{timestamp}.md"
        os.makedirs("outputs/synthesis_reports", exist_ok=True)

        with open(synthesis_path, "w", encoding="utf-8") as f:
            f.write(f"# MAAP-1 Change Analysis - Executive Synthesis\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"**Proposed Change:** {change}\n\n")
            f.write("---\n\n")
            f.write(synthesis_report)

        print(f"\n✅ Synthesis Report saved to: {synthesis_path}")

        # Show preview of synthesis
        print("\n" + "="*70)
        print("EXECUTIVE SYNTHESIS PREVIEW")
        print("="*70)
        print(synthesis_report[:1500] + "\n... (full report saved)")

    except Exception as e:
        print(f"❌ Error during synthesis: {e}")

    print("\n" + "="*70)
    print("COORDINATION COMPLETE")
    print("="*70)
    print(f"Detailed Reports: {detailed_path}")
    print(f"Synthesis Report:  {synthesis_path}")
    