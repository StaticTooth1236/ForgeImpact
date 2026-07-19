import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag, format_context

llm = ClaudeClient(model="claude-sonnet-4-6")

def analyze_risk_schedule_impact(change_description: str) -> str:
    """
    Analyzes risk and schedule impact.
    Targets: Risk Register, IMS, Financial & Contract Management, TEMP,
    Safety Requirements, Program Overview.
    """
    risk_context      = format_context(query_rag(change_description, top_k=5, file_filter="risk_register"))
    ims_context       = format_context(query_rag(change_description, top_k=5, file_filter="integrated_master_schedule"))
    financial_context = format_context(query_rag(change_description, top_k=4, file_filter="financial_and_contract_management"))
    temp_context      = format_context(query_rag(change_description, top_k=3, file_filter="test_evaluation_master_plan"))
    safety_context    = format_context(query_rag(change_description, top_k=3, file_filter="safety_requirements"))
    overview_context  = format_context(query_rag(change_description, top_k=3, file_filter="program_overview"))

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

Analyze the proposed change with focus on new or elevated risks, schedule impact, critical path, and mitigation options. Draw from all provided context and avoid over-relying on any single source. If a section reports no relevant content, note it briefly and move on — do not invent content for it.

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