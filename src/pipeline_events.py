"""
ForgeImpact — Pipeline Event Generator
--------------------------------------
Same analysis pipeline as synthesis_agent.py, refactored as a Python generator
that yields structured events as work happens. The FastAPI server (api.py)
forwards these events to the browser, which renders them live.

Event types yielded (all dicts with a "type" key):
  phase                — a pipeline stage is starting
  agent_started        — a specialized agent began work
  agent_completed      — a specialized agent finished (includes a short preview)
  documents_identified — the list of documents selected for impact analysis
  document_completed   — one document's impact analysis finished
  synthesis_token      — a chunk of PMP text, streamed live as it's written
  done                 — everything finished (includes the full PMP)
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import concurrent.futures

from src.rag_system import get_index
from src.synthesis_agent import (
    MODEL,
    SYNTHESIS_MAX_TOKENS,
    claude,
    get_relevant_documents,
    analyze_document_impact,
)

from src.change_impact_agent import analyze_change_impact
from src.cost_margin_impact_agent import analyze_cost_margin_impact
from src.manufacturing_production_agent import analyze_manufacturing_impact
from src.supply_chain_procurement_agent import analyze_supply_chain_impact
from src.risk_schedule_impact_agent import analyze_risk_schedule_impact

AGENT_LABELS = {
    "change_impact": "Change Impact Analyst",
    "cost_margin": "Cost & Margin Analyst",
    "manufacturing": "Manufacturing & Production Analyst",
    "supply_chain": "Supply Chain Analyst",
    "risk_schedule": "Risk & Schedule Analyst",
}


def _preview(text: str, limit: int = 300) -> str:
    """Short plain-text preview of an analysis for live status cards."""
    text = " ".join(text.split())
    return text[:limit] + ("…" if len(text) > limit else "")


def run_analysis_events(change_description: str):
    """Generator: runs the full pipeline, yielding events as they happen."""

    # --- Phase 0: warm up the index before any parallel work -----------------
    yield {"type": "phase", "phase": "warmup", "label": "Loading program knowledge base"}
    get_index()

    # --- Phase 1: specialized agents in parallel -----------------------------
    yield {"type": "phase", "phase": "agents", "label": "Running specialized analysis agents"}
    agent_funcs = {
        "change_impact": analyze_change_impact,
        "cost_margin": analyze_cost_margin_impact,
        "manufacturing": analyze_manufacturing_impact,
        "supply_chain": analyze_supply_chain_impact,
        "risk_schedule": analyze_risk_schedule_impact,
    }

    specialized_outputs = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(func, change_description): name
            for name, func in agent_funcs.items()
        }
        for name in agent_funcs:
            yield {"type": "agent_started", "agent": name, "label": AGENT_LABELS[name]}
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            output = future.result()
            specialized_outputs[name] = output
            yield {
                "type": "agent_completed",
                "agent": name,
                "label": AGENT_LABELS[name],
                "preview": _preview(output),
            }

    # --- Phase 2: document impact analysis (manifest + discovered) -----------
    yield {"type": "phase", "phase": "documents", "label": "Analyzing document-level impacts"}
    relevant_docs = get_relevant_documents(change_description)
    yield {"type": "documents_identified", "documents": relevant_docs}

    impact_by_doc = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(analyze_document_impact, doc, change_description): doc
            for doc in relevant_docs
        }
        for future in concurrent.futures.as_completed(futures):
            doc = futures[future]
            impact_by_doc[doc] = future.result()
            yield {
                "type": "document_completed",
                "document": doc,
                "preview": _preview(impact_by_doc[doc]),
            }
    # Preserve manifest ordering for the synthesis prompt
    document_impacts = [impact_by_doc[doc] for doc in relevant_docs]

    # --- Phase 3: streamed synthesis -----------------------------------------
    yield {"type": "phase", "phase": "synthesis", "label": "Synthesizing Project Management Plan"}

    impacts_text = "\n\n".join(document_impacts)
    specialized_text = "\n\n".join(
        f"**{k}:**\n{v}" for k, v in specialized_outputs.items()
    )
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

    chunks = []
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
            yield {"type": "synthesis_token", "text": text}

    pmp = "".join(chunks)
    yield {"type": "done", "pmp": pmp}