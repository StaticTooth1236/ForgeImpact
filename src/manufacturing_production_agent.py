import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag

llm = ClaudeClient(model="claude-sonnet-4-6")

def analyze_manufacturing_impact(change_description: str) -> str:
    """
    Analyzes manufacturing, producibility, and production impact.
    Targets: Manufacturing Ramp Plan, IMS, BOM, Configuration Management, Quality Management, Drawing Trees.
    """
    mfg_context     = query_rag(f"manufacturing ramp plan impact of: {change_description}", top_k=5)
    ims_context     = query_rag(f"integrated master schedule manufacturing impact of: {change_description}", top_k=4)
    bom_context     = query_rag(f"bill of materials producibility impact of: {change_description}", top_k=4)
    config_context  = query_rag(f"configuration management plan impact of: {change_description}", top_k=3)
    quality_context = query_rag(f"quality management plan impact of: {change_description}", top_k=3)
    drawing_context = query_rag(f"drawing tree configuration impact of: {change_description}", top_k=3)

    combined_context = f"""
=== Manufacturing Ramp Plan ===
{mfg_context}

=== Integrated Master Schedule ===
{ims_context}

=== Bill of Materials ===
{bom_context}

=== Configuration Management Plan ===
{config_context}

=== Quality Management Plan ===
{quality_context}

=== Drawing Trees & Configuration ===
{drawing_context}
"""

    prompt = f"""You are a senior aerospace Manufacturing and Production Engineer.

Analyze the proposed change with focus on producibility, manufacturing processes, ramp plan, tooling, and quality implications. Draw from all provided context and avoid over-relying on any single source.

Proposed Change:
{change_description}

Relevant Program Context:
{combined_context}
"""

    response = llm.chat(
        prompt,
        system_prompt="You are a senior aerospace manufacturing engineer. Balance your analysis across all provided document context.",
        max_tokens=5000
    )
    return response