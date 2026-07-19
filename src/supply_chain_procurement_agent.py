import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag, format_context

llm = ClaudeClient(model="claude-sonnet-4-6")

def analyze_supply_chain_impact(change_description: str) -> str:
    """
    Analyzes supply chain, procurement, and supplier impact.
    Targets: Supply Chain Procurement Plan, Vertical Integration, BOM,
    Manufacturing Ramp, Security Requirements.
    """
    supply_context   = format_context(query_rag(change_description, top_k=5, file_filter="supply_chain_procurement_plan"))
    vertical_context = format_context(query_rag(change_description, top_k=4, file_filter="vertical_integration"))
    bom_context      = format_context(query_rag(change_description, top_k=4, file_filter="bill_of_materials"))
    mfg_context      = format_context(query_rag(change_description, top_k=4, file_filter="manufacturing_ramp_plan"))
    security_context = format_context(query_rag(change_description, top_k=3, file_filter="security_requirements"))

    combined_context = f"""
=== Supply Chain Procurement Plan ===
{supply_context}

=== Vertical Integration & Make/Buy Strategy ===
{vertical_context}

=== Bill of Materials ===
{bom_context}

=== Manufacturing Ramp Plan ===
{mfg_context}

=== Security Requirements ===
{security_context}
"""

    prompt = f"""You are a senior aerospace Supply Chain and Procurement Manager.

Analyze the proposed change with focus on suppliers, procurement, lead times, make/buy strategy, and supply chain risk. Draw from all provided context and avoid over-relying on any single source. If a section reports no relevant content, note it briefly and move on — do not invent content for it.

Proposed Change:
{change_description}

Relevant Program Context:
{combined_context}
"""

    response = llm.chat(
        prompt,
        system_prompt="You are a senior aerospace supply chain manager. Balance your analysis across all provided document context.",
        max_tokens=5000
    )
    return response