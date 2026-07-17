import streamlit as st

st.set_page_config(page_title="Future Improvements | Eurus Systems", page_icon="🚁", layout="wide")

st.markdown("""
<style>
    .main .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
    h1 { color: #1E3A5F; font-weight: 700; }
    h2, h3 { color: #2E5A8C; }
</style>
""", unsafe_allow_html=True)

st.title("Future Improvements & Roadmap")
st.subheader("Eurus Systems • MAAP Program")

st.markdown("---")

st.header("Current Limitations")

st.markdown("""
While ARIA already delivers strong cross-functional analysis, there are several areas we plan to enhance:

- **Speed**: Running multiple agents can take several minutes. We aim to improve this through parallel execution and smarter routing.
- **Visual Outputs**: Currently generates text-based recommendations. Future versions will include actual visuals (Gantt charts, updated schedules, etc.).
- **Synthesis Quality**: The Executive Summary and Project Plan can be made more detailed and actionable.
- **User Experience**: The interface is functional but can be further refined for professional users.
""")

st.header("Planned Enhancements")

st.markdown("""
#### Near-Term (1–3 Months)
- Generate simple Gantt charts and updated schedule visuals
- Improve PDF export quality and formatting
- Add more specialized agents (Finance, Safety, Compliance)
- Enhance loading states and user feedback

#### Medium-Term (3–6 Months)
- Intelligent **Coordinator Agent** that automatically selects relevant agents
- Support for uploading real (anonymized) program documents
- Conversation memory for follow-up questions
- Comparison mode between multiple change scenarios

#### Long-Term Vision
- Integration with PLM / ERP systems for real program data
- Full multi-agent orchestration with tool use and planning
- “What-If” simulation capabilities
- Secure internal deployment for program management teams
""")

st.header("Ideas Under Exploration")

st.markdown("""
- Using code execution to dynamically generate updated schedules or cost models
- Adding a dedicated **What-If Simulator** mode
- Creating a polished portfolio version with realistic but anonymized data
- Exploring fine-tuning or advanced RAG techniques for improved consistency
""")

st.markdown("---")
st.caption("Eurus Systems • MAAP Program | ARIA – Agentic Reasoning for Impact Analysis")