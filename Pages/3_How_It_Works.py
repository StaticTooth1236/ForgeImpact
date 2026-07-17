import streamlit as st

st.set_page_config(page_title="How ARIA Works | Eurus Systems", page_icon="🚁", layout="wide")

st.markdown("""
<style>
    .main .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
    h1 { color: #1E3A5F; font-weight: 700; }
    h2, h3 { color: #2E5A8C; }
</style>
""", unsafe_allow_html=True)

st.title("How ARIA Works")
st.subheader("Eurus Systems • MAAP Program")

st.markdown("---")

st.header("Overview")

st.markdown("""
**ARIA (Agentic Reasoning for Impact Analysis)** is a multi-agent AI system designed to evaluate the cross-functional impact of engineering and program changes on complex aerospace programs.

Rather than using a single large model, ARIA leverages a team of specialized agents — each focused on a specific domain — to deliver more accurate, grounded, and actionable analysis.
""")

st.header("Core Architecture")

st.markdown("""
### 1. Specialized Domain Agents
- **Change Impact Analyst** — Evaluates overall technical and configuration impact
- **Risk & Schedule Impact Analyst** — Focuses on IMS, milestones, and risk elevation
- **Supply Chain & Procurement Agent** — Analyzes suppliers, lead times, and make-vs-buy decisions
- **Manufacturing & Production Planning Agent** — Assesses production rates, tooling, and workforce impact

### 2. Synthesis Agent
Aggregates outputs from the domain agents and produces a leadership-ready **Executive Summary** and **PMP-style Project Plan**.

### 3. Coordinator
Orchestrates agent execution based on user selection and ensures consistent, structured outputs.
""")

st.header("How Analysis Works")

st.markdown("""
When you submit a proposed change, ARIA supports two modes:

- **Single Agent Mode**: Runs one specialized agent for a focused analysis.
- **Full Multi-Agent Coordinator Mode**: Runs multiple agents in sequence and then generates a synthesized Executive Summary + Project Plan.

All analysis is grounded in the synthetic MAAP program data (requirements, drawing trees, IMS, manufacturing plans, and risk register).
""")

st.header("Technology Stack")

st.markdown("""
- **Large Language Model**: Claude (Anthropic)
- **RAG Framework**: LlamaIndex
- **Embeddings**: Local sentence-transformers models
- **Interface**: Streamlit (multi-page application)
- **Agent Framework**: Custom Python agents with structured prompting
""")

st.markdown("---")
st.caption("Eurus Systems • MAAP Program | ARIA – Agentic Reasoning for Impact Analysis")