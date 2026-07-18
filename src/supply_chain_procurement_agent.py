import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag

llm = ClaudeClient(model="claude-sonnet-4-6")

def analyze_supply_chain_impact(change_description: str) -> str:
    """
    Analyzes supply chain, procurement, and supplier impact.
    Targets: Supply Chain Procurement Plan, Vertical Integration, BOM, Manufacturing Ramp, Security Requirements.
    """
    supply_context   = query_rag(f"supply chain procurement plan impact of: {change_description}", top_k=5)
    vertical_context = query_rag(f"vertical integration and make buy strategy impact of: {change_description}", top_k=4)
    bom_context      = query_rag(f"bill of materials supplier impact of: {change_description}", top_k=4)
    mfg_context      = query_rag(f"manufacturing ramp plan supply chain impact of: {change_description}", top_k=4)
    security_context = query_rag(f"security requirements impact of: {change_description}", top_k=3)

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

Analyze the proposed change with focus on suppliers, procurement, lead times, make/buy strategy, and supply chain risk. Draw from all provided context and avoid over-relying on any single source.

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