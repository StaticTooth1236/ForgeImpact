import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag, format_context

llm = ClaudeClient(model="claude-sonnet-4-6")

def analyze_change_impact(change_description: str) -> str:
    """
    Analyzes the technical and programmatic impact of a proposed change.
    Strongly targets: Program Requirements Baseline, Key Specifications, IMS,
    Risk Register, and TEMP.

    Retrieval notes:
    - file_filter GUARANTEES chunks come from the intended document instead of
      hoping the query phrasing steers retrieval there.
    - format_context() turns the structured results into clean, labeled
      excerpts. Never interpolate query_rag()'s raw return into a prompt —
      it's a list of dicts, not text.
    - If any section below comes back as "(no relevant content found...)",
      the file_filter string doesn't match a real file in data/ — run
      `ls data/` and adjust the filter to match the actual filename.
    """
    prb_context   = format_context(query_rag(change_description, top_k=5, file_filter="program_requirements_baseline"))
    specs_context = format_context(query_rag(change_description, top_k=4, file_filter="key_specifications"))
    ims_context   = format_context(query_rag(change_description, top_k=5, file_filter="integrated_master_schedule"))
    risk_context  = format_context(query_rag(change_description, top_k=4, file_filter="risk_register"))
    temp_context  = format_context(query_rag(change_description, top_k=4, file_filter="test_evaluation_master_plan"))

    combined_context = f"""
=== Program Requirements Baseline ===
{prb_context}

=== Key Specifications ===
{specs_context}

=== Integrated Master Schedule ===
{ims_context}

=== Risk Register ===
{risk_context}

=== Test & Evaluation Master Plan ===
{temp_context}
"""

    prompt = f"""You are an experienced Aerospace Change Impact Analyst.

Analyze the proposed change using the context below. You must draw from **all** the document sections provided and avoid over-relying on any single source (especially the Risk Register). If a section reports no relevant content, note it briefly and move on — do not invent content for it.

Focus on:
- Technical impact (design, systems, interfaces)
- Programmatic impact (schedule, testing, certification)
- Cross-functional ripple effects
- Key risks introduced by the change

Be specific and reference the source documents where relevant.

Proposed Change:
{change_description}

Relevant Program Context:
{combined_context}
"""

    response = llm.chat(
        prompt,
        system_prompt="You are a senior aerospace change impact analyst. Balance your analysis across all provided document context. Do not over-rely on the Risk Register.",
        max_tokens=5000
    )
    return response


if __name__ == "__main__":
    test_change = "Change the primary battery supplier from Samsung SDI to LG Energy Solution. Assess the impact on certification timeline, unit cost, and supply chain risk."
    result = analyze_change_impact(test_change)
    print("\n=== CHANGE IMPACT AGENT OUTPUT ===\n")
    print(result)
