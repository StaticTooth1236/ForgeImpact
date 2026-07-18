import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag

llm = ClaudeClient(model="claude-sonnet-4-6")

def analyze_cost_margin_impact(change_description: str) -> str:
    """
    Analyzes cost, margin, and cash flow impact.
    Targets: Financial & Contract Management, IMS, Vertical Integration, BOM, Customer Demand.
    """
    financial_context = query_rag(f"financial and contract management impact of: {change_description}", top_k=5)
    ims_context       = query_rag(f"integrated master schedule cost impact of: {change_description}", top_k=4)
    vertical_context  = query_rag(f"vertical integration and make buy strategy impact of: {change_description}", top_k=4)
    bom_context       = query_rag(f"bill of materials cost impact of: {change_description}", top_k=4)
    demand_context    = query_rag(f"customer demand forecast impact of: {change_description}", top_k=3)

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

Analyze the financial impact of the proposed change. Draw from all provided context sections and avoid over-relying on any single source.

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