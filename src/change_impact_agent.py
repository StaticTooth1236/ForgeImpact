import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.claude_client import ClaudeClient
from src.rag_system import query_rag

llm = ClaudeClient(model="claude-3-5-sonnet-20241022")

def analyze_change_impact(change_description: str) -> str:
    """
    Analyzes the technical and programmatic impact of a proposed change.
    Strongly targets: Program Requirements Baseline, Key Specifications, IMS, Risk Register, and TEMP.
    """
    # More targeted + higher volume retrieval from assigned documents
    prb_context   = query_rag(f"program requirements baseline change impact of: {change_description}", top_k=5)
    specs_context = query_rag(f"key specifications change impact of: {change_description}", top_k=4)
    ims_context   = query_rag(f"integrated master schedule change impact of: {change_description}", top_k=5)
    risk_context  = query_rag(f"risk register change impact of: {change_description}", top_k=4)
    temp_context  = query_rag(f"test evaluation master plan change impact of: {change_description}", top_k=4)

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

Analyze the proposed change using the context below. You must draw from **all** the document sections provided and avoid over-relying on any single source (especially the Risk Register).

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