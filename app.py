import streamlit as st

st.set_page_config(
    page_title="ARIA | Eurus Systems",
    page_icon="🚁",
    layout="wide"
)

# ===================== CUSTOM STYLING =====================
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 { color: #1E3A5F; font-weight: 700; }
    h2, h3 { color: #2E5A8C; border-bottom: 2px solid #E8F0F8; padding-bottom: 8px; }
    .stButton > button {
        background-color: #1E3A5F;
        color: white;
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.title("Welcome to ARIA")
st.subheader("Agentic Reasoning for Impact Analysis")

st.markdown("---")

st.markdown("""
### Eurus Systems – MAAP Program

**ARIA** is an AI-powered multi-agent system designed to analyze the cross-functional impact of engineering and program changes.

Use the **sidebar** to navigate:

- **Program Overview** — Summary of the MAAP program and timeline
- **ARIA Tool** — Interactive change impact analysis tool
- **How It Works** — Technical explanation of the system
- **Future Improvements** — Roadmap and ideas
""")

st.markdown("---")
st.caption("Eurus Systems • MAAP Program | ARIA – Agentic Reasoning for Impact Analysis")