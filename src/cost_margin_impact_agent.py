import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag, format_context

llm = ClaudeClient(model="claude-sonnet-4-6")

def analyze_cost_margin_impact(change_description: str) -> str:
    """
    Analyzes cost, margin, and cash flow impact.
    Targets: Financial & Contract Management, IMS, Vertical Integration, BOM, Customer Demand.
    """
    financial_context = format_context(query_rag(change_description, top_k=5, file_filter="financial_and_contract_management"))
    ims_context       = format_context(query_rag(change_description, top_k=4, file_filter="integrated_master_schedule"))
    vertical_context  = format_context(query_rag(change_description, top_k=4, file_filter="vertical_integration"))
    bom_context       = format_context(query_rag(change_description, top_k=4, file_filter="bill_of_materials"))
    demand_context    = format_context(query_rag(change_description, top_k=3, file_filter="customer_demand_forecast"))

    combined_context = f"""
=== Financial & Contract Management ===
{financial_context}

=== Integrated Master Schedule ===
{ims_context}

=== Vertical Integration & Make/Buy Strategy ===
{vertical_context}

=== Bill of Materials ===
{bom_context}

=== Customer Demand Forecast ===
{demand_context}
"""

    prompt = f"""You are a senior aerospace Cost and Margin Analyst experienced with Firm Fixed Price programs.

Analyze the financial impact of the proposed change. Draw from all provided context sections and avoid over-relying on any single source. If a section reports no relevant content, note it briefly and move on — do not invent content for it.

Focus on:
- Estimated cost impact
- Effect on program margin
- Cash flow implications
- Risk to target margins
- Potential mitigation strategies

Be direct and business-oriented.

Proposed Change:
{change_description}

Relevant Program Context:
{combined_context}
"""

    response = llm.chat(
        prompt,
        system_prompt="You are a senior aerospace cost and margin analyst. Balance your analysis across all provided document context.",
        max_tokens=5000
    )
    return response