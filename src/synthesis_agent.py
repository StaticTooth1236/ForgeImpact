import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import concurrent.futures
import anthropic

from src.claude_client import ClaudeClient
from src.rag_system import query_rag

from src.change_impact_agent import analyze_change_impact
from src.cost_margin_impact_agent import analyze_cost_margin_impact
from src.manufacturing_production_agent import analyze_manufacturing_impact
from src.supply_chain_procurement_agent import analyze_supply_chain_impact
from src.risk_schedule_impact_agent import analyze_risk_schedule_impact

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def get_relevant_documents(change_description: str, top_k: int = 8) -> list:
    results = query_rag(change_description, top_k=top_k * 2)
    high_priority = [
        "maap1_integrated_master_schedule.md",
        "maap1_risk_register.md",
        "maap1_program_requirements_baseline.md",
        "maap1_financial_and_contract_management.md",
        "maap1_manufacturing_ramp_plan.md",
        "maap1_supply_chain_procurement_plan.md",
        "maap1_bill_of_materials.md",
    ]
    prioritized = []
    seen = set()
    for doc_name in high_priority:
        matches = [r for r in results if doc_name.lower() in r.lower()]
        for m in matches[:2]:
            if m not in seen:
                prioritized.append(m)
                seen.add(m)
    remaining = [r for r in results if r not in seen]
    prioritized.extend(remaining[:top_k - len(prioritized)])
    return prioritized[:top_k]

def analyze_document_impact(document_name: str, change_description: str) -> str:
    context = query_rag(f"how does this change affect {document_name}: {change_description}", top_k=5)
    prompt = f"""You are an expert aerospace program analyst.

Analyze the impact of the following proposed change on the document: **{document_name}**

Proposed Change:
{change_description}

Relevant content from {document_name}:
{context}

Provide a structured assessment with:
- Impact Level (High / Medium / Low / None)
- Key Sections Affected
- Specific Impacts
- New or Modified Risks
- Recommended Updates

Be specific."""
    message = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=3500,
        system="You are a precise aerospace program analyst.",
        messages=[{"role": "user", "content": prompt}]
    )
    return f"=== Impact on {document_name} ===\n{message.content[0].text}"

def synthesize_pmp(change_description: str, specialized_outputs: dict, document_impacts: list) -> str:
    impacts_text = "\n\n".join(document_impacts)
    specialized_text = "\n\n".join([f"**{k}:**\n{v}" for k, v in specialized_outputs.items()])

    prompt = f"""You are a senior aerospace Program Manager creating a Project Management Plan update.

**Proposed Change:**
{change_description}

**Specialized Agent Analysis:**
{specialized_text}

**Document-Level Impact Assessments:**
{impacts_text}

Produce a Project Management Plan update. For missing sections write: "Data not yet available – placeholder section"

Use this structure:
1. Introduction
2. Project Scope
3. Milestone List & Schedule Baseline
4. Change Management Plan
5. Cost Management Plan & Cost Baseline
6. Risk Management Plan & Risk Register
7. Procurement / Supply Chain Management Plan
8. Quality Management Plan
9. Staffing & Resource Management (Data not yet available – placeholder section)
10. Overall Assessment & Recommended Path Forward
"""
    message = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=10000,
        system="You are a senior aerospace Program Manager. Produce clear Project Management Plan content.",
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def synthesize_change_analysis(change_description: str) -> str:
    print(">>> RUNNING LATEST VERSION OF synthesis_agent.py <<<")
    print("Running specialized agents in parallel...")

    specialized_agents = {
        "change_impact": analyze_change_impact,
        "cost_margin": analyze_cost_margin_impact,
        "manufacturing": analyze_manufacturing_impact,
        "supply_chain": analyze_supply_chain_impact,
        "risk_schedule": analyze_risk_schedule_impact,
    }

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(func, change_description): name for name, func in specialized_agents.items()}
        specialized_outputs = {name: future.result() for future, name in futures.items()}

    print("Identifying relevant documents...")
    relevant_docs = get_relevant_documents(change_description, top_k=8)

    print("Running parallel document impact analysis...")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(analyze_document_impact, doc, change_description) for doc in relevant_docs]
        document_impacts = [f.result() for f in concurrent.futures.as_completed(futures)]

    print("Synthesizing into Project Management Plan...")
    return synthesize_pmp(change_description, specialized_outputs, document_impacts)

if __name__ == "__main__":
    test_change = "Change the primary battery supplier from Samsung SDI to LG Energy Solution. Assess the impact on certification timeline, unit cost, and supply chain risk."
    result = synthesize_change_analysis(test_change)
    print("\n" + "="*80)
    print("PROJECT MANAGEMENT PLAN OUTPUT")
    print("="*80 + "\n")
    print(result)