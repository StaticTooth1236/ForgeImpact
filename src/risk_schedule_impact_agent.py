import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag

llm = ClaudeClient(model="claude-3-5-sonnet-20241022")

def analyze_risk_schedule_impact(change_description: str) -> str:
    """
    Analyzes risk and schedule impact.
    Targets: Risk Register, IMS, Financial & Contract Management, TEMP, Safety Requirements, Program Overview.
    """
    risk_context      = query_rag(f"risk register impact of: {change_description}", top_k=5)
    ims_context       = query_rag(f"integrated master schedule impact of: {change_description}", top_k=5)
    financial_context = query_rag(f"financial and contract management risk impact of: {change_description}", top_k=4)
    temp_context      = query_rag(f"test evaluation master plan impact of: {change_description}", top_k=3)
    safety_context    = query_rag(f"safety requirements impact of: {change_description}", top_k=3)
    overview_context  = query_rag(f"program overview risk context of: {change_description}", top_k=3)

    combined_context = f"""
=== Risk Register ===
{risk_context}

=== Integrated Master Schedule ===
{ims_context}

=== Financial & Contract Management ===
{financial_context}

=== Test & Evaluation Master Plan ===
{temp_context}

=== Safety Requirements ===
{safety_context}

=== Program Overview ===
{overview_context}
"""

    prompt = f"""You are a senior aerospace Risk and Schedule Manager.

Analyze the proposed change with focus on new or elevated risks, schedule impact, critical path, and mitigation options. Draw from all provided context and avoid over-relying on any single source.

Proposed Change:
{change_description}

Relevant Program Context:
{combined_context}
"""

    response = llm.chat(
        prompt,
        system_prompt="You are a senior aerospace risk and schedule manager. Balance your analysis across all provided document context.",
        max_tokens=5000
    )
    return response