import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag, format_context

llm = ClaudeClient(model="claude-sonnet-4-6")

def analyze_manufacturing_impact(change_description: str) -> str:
    """
    Analyzes manufacturing, producibility, and production impact.
    Targets: Manufacturing Ramp Plan, IMS, BOM, Configuration Management,
    Quality Management, Drawing Trees.

    Note: there is no standalone configuration management document in data/ —
    the CM process (CM-0001, change classes, ICD control) lives in
    maap1_program_requirements_baseline_continuation.md, so that's where the
    configuration retrieval points. The "drawing_tree" filter intentionally
    matches all three variant files (cargo, firefighting, isr).
    """
    mfg_context     = format_context(query_rag(change_description, top_k=5, file_filter="manufacturing_ramp_plan"))
    ims_context     = format_context(query_rag(change_description, top_k=4, file_filter="integrated_master_schedule"))
    bom_context     = format_context(query_rag(change_description, top_k=4, file_filter="bill_of_materials"))
    config_context  = format_context(query_rag(change_description, top_k=3, file_filter="program_requirements_baseline_continuation"))
    quality_context = format_context(query_rag(change_description, top_k=3, file_filter="quality_management_plan"))
    drawing_context = format_context(query_rag(change_description, top_k=3, file_filter="drawing_tree"))

    combined_context = f"""
=== Manufacturing Ramp Plan ===
{mfg_context}

=== Integrated Master Schedule ===
{ims_context}

=== Bill of Materials ===
{bom_context}

=== Configuration Management (Requirements Baseline Continuation) ===
{config_context}

=== Quality Management Plan ===
{quality_context}

=== Drawing Trees & Configuration ===
{drawing_context}
"""

    prompt = f"""You are a senior aerospace Manufacturing and Production Engineer.

Analyze the proposed change with focus on producibility, manufacturing processes, ramp plan, tooling, and quality implications. Draw from all provided context and avoid over-relying on any single source. If a section reports no relevant content, note it briefly and move on — do not invent content for it.

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