"""
ForgeImpact — Synthesis Agent
-----------------------------
Orchestrates: 5 specialized agents (parallel) -> document impact analysis
(parallel, manifest-driven) -> synthesis into a Project Management Plan update.

Run: python3 src/synthesis_agent.py
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import concurrent.futures

from dotenv import load_dotenv
import anthropic

from src.rag_system import query_rag, format_context, get_index

from src.change_impact_agent import analyze_change_impact
from src.cost_margin_impact_agent import analyze_cost_margin_impact
from src.manufacturing_production_agent import analyze_manufacturing_impact
from src.supply_chain_procurement_agent import analyze_supply_chain_impact
from src.risk_schedule_impact_agent import analyze_risk_schedule_impact

load_dotenv()

# One model constant for this file. Sonnet 4.6 supports up to 64K output
# tokens, which a full PMP genuinely needs. (If your account can't access it,
# fall back to "claude-3-5-sonnet-20241022" and cap SYNTHESIS_MAX_TOKENS at 8192.)
MODEL = "claude-sonnet-4-6"
SYNTHESIS_MAX_TOKENS = 32000  # full PMPs run long; Sonnet 4.6 supports up to 64K out
DOC_IMPACT_MAX_TOKENS = 3000

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ---------------------------------------------------------------------------
# Document coverage: manifest-first, retrieval second.
#
# These documents are ALWAYS analyzed for every change. This is the structural
# fix for Risk Register bias: coverage is no longer decided by semantic
# similarity rankings (which the Risk Register always wins) — it's guaranteed.
# Retrieval is only used to DISCOVER additional documents beyond the manifest.
# ---------------------------------------------------------------------------
DOCUMENT_MANIFEST = [
    "maap1_integrated_master_schedule.md",
    "maap1_risk_register.md",
    "maap1_program_requirements_baseline.md",
    "maap1_financial_and_contract_management.md",
    "maap1_manufacturing_ramp_plan.md",
    "maap1_supply_chain_procurement_plan.md",
    "maap1_bill_of_materials.md",
]


def get_relevant_documents(change_description: str, extra_docs: int = 3) -> list:
    """Manifest docs always included; semantic retrieval adds up to `extra_docs` more."""
    results = query_rag(change_description, top_k=15)
    discovered = []
    for r in results:
        name = r["file_name"]
        if name not in DOCUMENT_MANIFEST and name not in discovered:
            discovered.append(name)
    return DOCUMENT_MANIFEST + discovered[:extra_docs]


def analyze_document_impact(document_name: str, change_description: str) -> str:
    """Assess how the proposed change affects one specific program document."""
    chunks = query_rag(change_description, top_k=5, file_filter=document_name)
    context = format_context(chunks)

    prompt = f"""Proposed Change:
{change_description}

Relevant content from {document_name}:
{context}

Analyze the impact of the proposed change on the document "{document_name}".
Provide a structured assessment with:
- Impact Level (High / Medium / Low / None)
- Key Sections Affected
- Specific Impacts
- New or Modified Risks
- Recommended Updates

Be specific. If the retrieved content shows this document is unaffected, say so
briefly rather than inventing impacts."""

    try:
        message = claude.messages.create(
            model=MODEL,
            max_tokens=DOC_IMPACT_MAX_TOKENS,
            system="You are a precise aerospace program analyst.",
            messages=[{"role": "user", "content": prompt}],
        )
        body = message.content[0].text
    except Exception as e:
        # Loud, labeled failure — never silently blend errors into the analysis.
        body = f"[ANALYSIS FAILED for {document_name}: {e}]"
        print(f"  ⚠️  Document impact failed for {document_name}: {e}")

    return f"=== Impact on {document_name} ===\n{body}"


def synthesize_pmp(change_description: str, specialized_outputs: dict, document_impacts: list) -> str:
    """Combine all agent and document analyses into a PMP update."""
    impacts_text = "\n\n".join(document_impacts)
    specialized_text = "\n\n".join(f"**{k}:**\n{v}" for k, v in specialized_outputs.items())

    # Prompt architecture: context FIRST, instructions LAST, explicit skeleton.
    prompt = f"""**Proposed Change:**
{change_description}

**Specialized Agent Analysis:**
{specialized_text}

**Document-Level Impact Assessments:**
{impacts_text}

---

Using ALL of the analysis above, produce a Project Management Plan UPDATE for
the MAAP-1 program reflecting this proposed change.

Formatting requirements (mandatory):
- Begin with the heading: # Project Management Plan Update — MAAP-1
- Include ALL 10 sections below, each as a numbered "##" heading, in order.
- Every section must contain substantive content synthesized from the analysis
  above. Only if a section truly has no supporting data, write exactly:
  "Data not yet available – placeholder section"
- Draw on the document-level assessments across ALL analyzed documents, not
  just the risk register.

Required sections:
1. Introduction
2. Project Scope
3. Milestone List & Schedule Baseline
4. Change Management Plan
5. Cost Management Plan & Cost Baseline
6. Risk Management Plan & Risk Register
7. Procurement / Supply Chain Management Plan
8. Quality Management Plan
9. Staffing & Resource Management
10. Overall Assessment & Recommended Path Forward"""

    # Streaming is REQUIRED by the SDK for potentially long generations
    # (32K tokens can exceed 10 minutes). It's also exactly the mechanism the
    # website will use to render PMP sections live as they're written.
    chunks = []
    chars_since_tick = 0
    print("      Streaming synthesis: ", end="", flush=True)
    with claude.messages.stream(
        model=MODEL,
        max_tokens=SYNTHESIS_MAX_TOKENS,
        system=(
            "You are a senior aerospace Program Manager. You write complete, "
            "structured Project Management Plan documents. You always follow the "
            "exact section structure requested."
        ),
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            chunks.append(text)
            chars_since_tick += len(text)
            if chars_since_tick >= 2000:  # one dot per ~2000 characters written
                print(".", end="", flush=True)
                chars_since_tick = 0
    print(" done.")
    return "".join(chunks)


def synthesize_change_analysis(change_description: str) -> str:
    print(">>> RUNNING synthesis_agent.py (v3 — thread-safe index warm-up) <<<")

    print("[0/3] Warming up RAG index (loads once, before any parallel work)...")
    get_index()

    print("[1/3] Running 5 specialized agents in parallel...")
    specialized_agents = {
        "change_impact": analyze_change_impact,
        "cost_margin": analyze_cost_margin_impact,
        "manufacturing": analyze_manufacturing_impact,
        "supply_chain": analyze_supply_chain_impact,
        "risk_schedule": analyze_risk_schedule_impact,
    }
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(func, change_description): name
            for name, func in specialized_agents.items()
        }
        specialized_outputs = {name: future.result() for future, name in futures.items()}

    print("[2/3] Analyzing document impacts (manifest + discovered)...")
    relevant_docs = get_relevant_documents(change_description)
    for d in relevant_docs:
        print(f"      - {d}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(analyze_document_impact, doc, change_description)
            for doc in relevant_docs
        ]
        document_impacts = [f.result() for f in futures]  # preserves manifest order

    print("[3/3] Synthesizing Project Management Plan update...")
    return synthesize_pmp(change_description, specialized_outputs, document_impacts)


if __name__ == "__main__":
    test_change = (
        "Change the primary battery supplier from Samsung SDI to LG Energy Solution. "
        "Assess the impact on certification timeline, unit cost, and supply chain risk."
    )
    result = synthesize_change_analysis(test_change)
    print("\n" + "=" * 80)
    print("PROJECT MANAGEMENT PLAN OUTPUT")
    print("=" * 80 + "\n")
    print(result)

    # Also save to a file so long outputs aren't lost to terminal scrollback.
    os.makedirs("outputs", exist_ok=True)
    out_path = "outputs/latest_pmp_update.md"
    with open(out_path, "w") as f:
        f.write(result)
    print(f"\n✅ Saved to {out_path}")