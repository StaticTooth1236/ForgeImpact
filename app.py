import streamlit as st
from datetime import datetime
import concurrent.futures

st.set_page_config(
    page_title="ARIA | Agentic Reasoning for Impact Analysis",
    page_icon="🚁",
    layout="wide"
)

# ===================== PREMIUM STYLING =====================
st.markdown("""
<style>
    .main {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    h1, h2, h3 {
        color: #f1f5f9;
        font-weight: 600;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    .stButton > button {
        background-color: #1e40af;
        color: white;
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ===================== 1. HERO =====================
st.title("ARIA")
st.subheader("Agentic Reasoning for Impact Analysis")
st.markdown("**Eurus Systems • Synthetic MAAP Program Case Study**")

st.markdown("---")

# ===================== 2. HOW ARIA WORKS =====================
st.header("How ARIA Works", divider="blue")
st.markdown("""
ARIA uses specialized agents and smart model routing to balance **cost, speed, and accuracy**. 
Simple questions are handled by faster, lower-cost models, while complex questions use more powerful models.
""")

st.markdown("---")

# ===================== 3. PROGRAM OVERVIEW =====================
st.header("The Case Study: MAAP Program", divider="blue")
st.markdown("""
**Note:** All company and program data used in ARIA is **synthetic**. It was created as a realistic case study to demonstrate the tool’s capabilities.

The MAAP program involves a heavy-lift tandem-rotor autonomous helicopter designed for both wildfire response and military logistics/ISR missions.
""")

st.markdown("---")

# ===================== 4. TRY ARIA =====================
st.header("Try ARIA", divider="blue")

col1, col2 = st.columns(2)

# ===================== LEFT: PROGRAM Q&A CHAT (4-TIER ROUTING) =====================
with col1:
    st.subheader("Program Q&A Chat")
    st.caption("Ask questions about the synthetic MAAP program")

    if "qa_messages" not in st.session_state:
        st.session_state.qa_messages = []

    with st.expander("Recommended Questions"):
        st.markdown("""
        - What is the range and payload capacity of the MAAP-1?
        - How many variants does the MAAP program have?
        - What does the Integrated Master Schedule say about LRIP timing?
        - What are the key risks in the current risk register?
        - How does the manufacturing ramp plan align with customer demand?
        """)

    for message in st.session_state.qa_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question about the MAAP program..."):
        st.session_state.qa_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analyzing question complexity..."):
                try:
                    from src.claude_client import ClaudeClient

                    # === 4-TIER CLASSIFIER ===
                    router = ClaudeClient(model="claude-haiku-4-5-20251001")

                    classification_prompt = f"""Classify the following question into one of these categories:

- very_simple: Basic factual lookup, very short and direct
- simple: Straightforward question, easy to answer
- medium: Requires some explanation or connecting ideas
- complex: Requires reasoning, trade-offs, multi-step thinking, or deeper analysis

Respond with ONLY one of these words: very_simple, simple, medium, or complex

Question: {prompt}"""

                    classification = router.chat(classification_prompt).strip().lower()

                    # === Choose model based on classification ===
                    if classification == "very_simple":
                        model_to_use = "llama-3.1-8b-instant"
                        model_label = "Llama 3.1 8B (Groq - Very Fast)"
                    elif classification in ["simple", "medium"]:
                        model_to_use = "claude-haiku-4-5-20251001"
                        model_label = "Claude Haiku (Fast & Efficient)"
                    else:
                        model_to_use = "claude-sonnet-4-5-20250929"
                        model_label = "Claude Sonnet (High Accuracy)"

                    # Show routing decision
                    st.caption(f"**Complexity:** {classification.replace('_', ' ').title()} | **Model:** {model_label}")

                    # === Get response using RAG ===
                    from src.rag_system import query_rag
                    response = query_rag(prompt)

                    st.markdown(response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": response})

                except Exception as e:
                    error_msg = f"Sorry, I ran into an error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.qa_messages.append({"role": "assistant", "content": error_msg})

# ===================== RIGHT: ARIA TOOL =====================
with col2:
    st.subheader("ARIA Tool")
    st.caption("Analyze the impact of engineering or program changes")

    mode = st.radio(
        "Select Mode",
        ["Single Agent Analysis", "Full Multi-Agent Coordinator"],
        horizontal=True
    )

    change_description = st.text_area(
        "Describe the proposed engineering or program change:",
        height=100,
        placeholder="Example: Increase the firefighting variant water tank capacity by 10%"
    )

    if mode == "Single Agent Analysis":
        agent_choice = st.selectbox(
            "Choose Analysis Focus",
            [
                "Change Impact Analyst",
                "Risk & Schedule Impact Analyst",
                "Supply Chain & Procurement Agent",
                "Manufacturing & Production Agent"
            ]
        )

        if st.button("Run Analysis", key="single_agent"):
            if change_description.strip():
                with st.spinner(f"Running {agent_choice} (fast mode)..."):
                    try:
                        from src.llm_client import LLMClient
                        fast_client = LLMClient(model="claude-haiku-4-5-20251001")

                        system_prompt = f"You are a senior Aerospace {agent_choice}."
                        prompt = f"{system_prompt}\n\nProposed Change: {change_description}\n\nProvide a clear analysis."

                        result = fast_client.chat(prompt, system_prompt=system_prompt)
                        st.success(f"Analysis complete using **{agent_choice}**")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter a change description.")

    else:  # Full Multi-Agent Coordinator
        st.markdown("**Agents to Run:**")
        run_change = st.checkbox("Change Impact Analyst", value=True)
        run_risk = st.checkbox("Risk & Schedule Impact Analyst", value=True)
        run_supply = st.checkbox("Supply Chain & Procurement Agent", value=True)
        run_manufacturing = st.checkbox("Manufacturing & Production Agent", value=True)

        if st.button("Run Full Analysis + Generate Synthesis", key="multi_agent"):
            if change_description.strip():
                selected = []
                if run_change: selected.append(("Change Impact", "change_impact_agent"))
                if run_risk: selected.append(("Risk & Schedule", "risk_schedule_impact_agent"))
                if run_supply: selected.append(("Supply Chain & Procurement", "supply_chain_procurement_agent"))
                if run_manufacturing: selected.append(("Manufacturing & Production", "manufacturing_production_agent"))

                if selected:
                    with st.spinner("Running agents in parallel..."):
                        try:
                            import importlib
                            agent_results = {}

                            with concurrent.futures.ThreadPoolExecutor() as executor:
                                future_to_name = {}
                                for name, module_name in selected:
                                    module = importlib.import_module(f"src.{module_name}")
                                    func = getattr(module, f"analyze_{module_name.replace('_agent', '_impact')}")
                                    future_to_name[executor.submit(func, change_description)] = name

                                for future in concurrent.futures.as_completed(future_to_name):
                                    name = future_to_name[future]
                                    try:
                                        agent_results[name] = future.result()
                                    except Exception as exc:
                                        agent_results[name] = f"Error: {exc}"

                            from src.synthesis_agent import synthesize_change_analysis
                            synthesis = synthesize_change_analysis(change_description, agent_results)

                            st.success("Analysis complete!")
                            st.markdown("## Executive Summary")
                            st.markdown(synthesis)

                            with st.expander("View Detailed Agent Outputs"):
                                for name, output in agent_results.items():
                                    st.markdown(f"### {name}")
                                    st.markdown(output)

                        except Exception as e:
                            st.error(f"Error during analysis: {str(e)}")
                else:
                    st.warning("Please select at least one agent.")
            else:
                st.warning("Please enter a change description.")

st.markdown("---")

# ===================== FOOTER =====================
st.caption("Eurus Systems • Synthetic MAAP Program Case Study | ARIA v1.0")