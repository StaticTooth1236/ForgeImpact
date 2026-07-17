import streamlit as st
import sys
import os
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from change_impact_agent import analyze_change_impact
from risk_schedule_impact_agent import analyze_risk_schedule_impact
from supply_chain_procurement_agent import analyze_supply_chain_impact
from manufacturing_production_agent import analyze_manufacturing_impact
from synthesis_agent import synthesize_change_analysis
from claude_client import ClaudeClient

from fpdf import FPDF

st.set_page_config(page_title="ARIA Tool | Eurus Systems", page_icon="🚁", layout="wide")

# ===================== STYLING =====================
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    h1 { color: #1E3A5F; font-weight: 700; }
    h2, h3 { color: #2E5A8C; }
    .stButton > button {
        background-color: #1E3A5F;
        color: white;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
    }
    .stButton > button:hover {
        background-color: #2E5A8C;
    }
</style>
""", unsafe_allow_html=True)

st.title("ARIA Tool")
st.subheader("Agentic Reasoning for Impact Analysis • Eurus Systems")

st.markdown("---")

# ===================== FAST MODEL FOR SINGLE AGENT =====================
fast_client = ClaudeClient(model="claude-haiku-4-5-20251001")

def run_single_agent_fast(agent_name: str, change_description: str) -> str:
    """Run a single agent using the fast model (Haiku) with richer output"""

    system_prompt = f"""You are a senior Aerospace {agent_name} for the Eurus Systems MAAP program.

Analyze the proposed change thoroughly and provide a detailed but concise professional response using this structure:

## {agent_name} Analysis

**Proposed Change:**  
[Clear restatement]

**Overall Impact Level:** High / Medium / Low + one-sentence justification

**Key Impact Areas:**  
- List the main technical and programmatic areas affected

**Detailed Impact Summary:**  
[5-8 sentence overview covering the most important effects]

**Specific Impacts:**
- **Technical / Design Impact:** ...
- **Schedule & Program Impact:** ...
- **Supply Chain / Manufacturing Impact:** ...
- **Risk & Certification Impact:** ...
- **Operational / Performance Impact:** ...

**Dependencies & Interfaces:**  
[Any other systems, documents, or stakeholders that would be affected]

**Risk Level:** High / Medium / Low + brief explanation

**Recommendations & Mitigations:**  
[Clear, prioritized recommendations. Include whether this change should be approved, rejected, or studied further]

**Next Steps:**  
[Specific recommended actions to properly assess or implement this change]

**Confidence Level:** X/10 (with brief explanation)
"""

    prompt = f"""{system_prompt}

**Proposed Change:**  
{change_description}

Provide a detailed but concise analysis following the structure above. Focus on the most important impacts."""

    return fast_client.chat(prompt, system_prompt=system_prompt, max_tokens=3500)


# ===================== ROBUST SMART AGENT SELECTION =====================
def get_relevant_agents(change_description: str) -> list:
    prompt = f"""You are an expert at analyzing engineering changes in aerospace programs.

Given the change below, determine which of the following analysis areas are relevant:

Available agents:
- Change Impact
- Risk & Schedule
- Supply Chain & Procurement
- Manufacturing & Production

Change description:
{change_description}

Instructions:
- Only return the names of the relevant agents.
- Return them as a comma-separated list with no extra text.
- Example: Change Impact, Risk & Schedule, Manufacturing & Production

Relevant agents:"""

    try:
        response = fast_client.chat(prompt)  # Use fast model for classification
        agents = [a.strip() for a in response.strip().split(",") if a.strip()]
        
        valid = ["Change Impact", "Risk & Schedule", "Supply Chain & Procurement", "Manufacturing & Production"]
        filtered = [a for a in agents if a in valid]
        
        return filtered if filtered else valid
    except:
        return ["Change Impact", "Risk & Schedule", "Supply Chain & Procurement", "Manufacturing & Production"]


# ===================== MODE SELECTION =====================
st.markdown("### Select Analysis Mode")

mode = st.radio(
    "",
    ["Single Agent Analysis", "Full Multi-Agent Coordinator"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")

change_description = st.text_area(
    "**Describe the proposed engineering or program change:**",
    height=130,
    placeholder="Example: Increase the firefighting variant water tank capacity by 10%"
)

# ===================== SINGLE AGENT MODE (FAST) =====================
if mode == "Single Agent Analysis":
    st.markdown("### Choose Analysis Focus")

    agent_choice = st.selectbox(
        "",
        [
            "Change Impact Analyst",
            "Risk & Schedule Impact Analyst",
            "Supply Chain & Procurement Agent",
            "Manufacturing & Production Agent"
        ],
        label_visibility="collapsed"
    )

    if st.button("Run Analysis", type="primary"):
        if not change_description.strip():
            st.warning("Please enter a change description.")
        else:
            with st.spinner(f"Running {agent_choice} (fast mode)..."):
                try:
                    result = run_single_agent_fast(agent_choice, change_description)

                    st.success(f"Analysis complete using **{agent_choice}** (Fast Model)")
                    st.markdown("---")
                    st.markdown(result)

                    st.download_button(
                        label="📥 Download Report as Markdown",
                        data=result,
                        file_name=f"{agent_choice.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

# ===================== FULL COORDINATOR MODE (HIGH QUALITY) =====================
else:
    st.markdown("### Analysis Mode")

    use_smart = st.checkbox("Use Smart Agent Selection (Recommended)", value=True)

    relevant_agents = []
    if use_smart and change_description.strip():
        with st.spinner("Identifying relevant agents..."):
            try:
                relevant_agents = get_relevant_agents(change_description)
                st.info(f"**Recommended agents:** {', '.join(relevant_agents)}")
            except:
                relevant_agents = ["Change Impact", "Risk & Schedule", "Supply Chain & Procurement", "Manufacturing & Production"]

    st.markdown("**Agents to Run:**")

    col1, col2 = st.columns(2)

    with col1:
        default_change = "Change Impact" in relevant_agents if relevant_agents else True
        run_change = st.checkbox("Change Impact Analyst", value=default_change)

        default_risk = "Risk & Schedule" in relevant_agents if relevant_agents else True
        run_risk = st.checkbox("Risk & Schedule Impact Analyst", value=default_risk)

    with col2:
        default_supply = "Supply Chain & Procurement" in relevant_agents if relevant_agents else True
        run_supply = st.checkbox("Supply Chain & Procurement Agent", value=default_supply)

        default_mfg = "Manufacturing & Production" in relevant_agents if relevant_agents else True
        run_manufacturing = st.checkbox("Manufacturing & Production Agent", value=default_mfg)

    if st.button("Run Full Analysis + Generate Synthesis", type="primary"):
        if not change_description.strip():
            st.warning("Please enter a change description.")
        else:
            selected = []
            if run_change: selected.append(("Change Impact", analyze_change_impact))
            if run_risk: selected.append(("Risk & Schedule", analyze_risk_schedule_impact))
            if run_supply: selected.append(("Supply Chain & Procurement", analyze_supply_chain_impact))
            if run_manufacturing: selected.append(("Manufacturing & Production", analyze_manufacturing_impact))

            if not selected:
                st.warning("Please select at least one agent.")
            else:
                with st.spinner("Running agents in parallel..."):
                    try:
                        import concurrent.futures

                        agent_results = {}

                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            future_to_name = {
                                executor.submit(func, change_description): name 
                                for name, func in selected
                            }

                            for future in concurrent.futures.as_completed(future_to_name):
                                name = future_to_name[future]
                                try:
                                    agent_results[name] = future.result()
                                except Exception as exc:
                                    agent_results[name] = f"Error: {exc}"

                        # Synthesis uses high-quality model
                        synthesis = synthesize_change_analysis(change_description, agent_results)
                        st.session_state.synthesis = synthesis

                        st.success("Analysis complete!")

                        st.markdown("## Executive Summary & Project Plan")
                        st.markdown(synthesis)

                        if st.button("📄 Export Synthesis as PDF"):
                            pdf = FPDF()
                            pdf.add_page()
                            pdf.set_font("Arial", size=11)
                            pdf.multi_cell(0, 8, st.session_state.synthesis)
                            pdf_path = f"outputs/ARIA_Synthesis_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
                            pdf.output(pdf_path)

                            with open(pdf_path, "rb") as f:
                                st.download_button(
                                    label="⬇️ Download PDF Now",
                                    data=f,
                                    file_name=os.path.basename(pdf_path),
                                    mime="application/pdf"
                                )

                        with st.expander("View Detailed Agent Outputs"):
                            for name, output in agent_results.items():
                                st.markdown(f"### {name}")
                                st.markdown(output)
                                st.markdown("---")

                    except Exception as e:
                        st.error(f"Error during analysis: {str(e)}")

st.markdown("---")
st.caption("Eurus Systems • MAAP Program | ARIA – Agentic Reasoning for Impact Analysis")