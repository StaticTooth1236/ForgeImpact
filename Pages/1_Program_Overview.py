import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MAAP Program Overview | ARIA", page_icon="🚁", layout="wide")

st.title("Eurus Systems – MAAP Program Overview")
st.subheader("Modular Autonomous Aerial Platform (MAAP)")

st.markdown("---")

# ===================== PROGRAM VISION =====================
st.header("Program Vision & Purpose")

st.markdown("""
The **MAAP (Modular Autonomous Aerial Platform)** is a next-generation **tandem-rotor heavy-lift autonomous helicopter** developed by **Eurus Systems**.

It is designed as a **dual-use platform** capable of supporting both civilian wildfire response and military logistics/ISR missions through a common airframe and modular mission systems.
""")

# ===================== KEY CAPABILITIES =====================
st.header("Key Technical Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Core Platform**
    - Tandem rotor configuration (forward + aft)
    - Advanced turboshaft propulsion
    - Lightweight composite drone-style airframe
    - Autonomous swarm operations capability
    - Mobile 18-wheeler trailer-based launch & recovery
    """)

with col2:
    st.markdown("""
    **Performance Highlights**
    - Heavy-lift capability with modular payloads
    - Long-endurance autonomous operations
    - Multi-mission flexibility via rapid module swaps
    - Designed for both civil certification (FAA) and military airworthiness
    """)

st.markdown("---")

# ===================== VARIANTS =====================
st.header("MAAP Variants & Mission Use Cases")

st.markdown("The MAAP program features three primary variants built on a common **Green Aircraft** baseline:")

st.subheader("MAAP-1F – Firefighting Variant")
st.markdown("""
**Primary Mission:** Wildfire suppression  
**Key Features:** Large water/retardant tank, aerial scooping, modular delivery systems.  
**Use Case:** Rapid aerial firefighting in remote terrain.
""")

st.subheader("MAAP-1I – ISR Variant")
st.markdown("""
**Primary Mission:** Intelligence, Surveillance & Reconnaissance  
**Key Features:** EO/IR sensors, SAR, SIGINT, real-time data links.  
**Use Case:** Persistent surveillance and intelligence gathering.
""")

st.subheader("MAAP-1C – Cargo / Logistics Variant")
st.markdown("""
**Primary Mission:** Military logistics and heavy cargo transport  
**Key Features:** Reinforced cargo systems, internal/external load capability.  
**Use Case:** Rapid transport in contested or austere environments.
""")

st.markdown("---")

# ===================== PROGRAM STATUS =====================
st.header("High-Level Program Status")

st.markdown("The MAAP program is transitioning from development into low-rate production while continuing flight testing and qualification.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Current Phase Highlights**
    - Flight testing and envelope expansion ongoing
    - LRIP preparation underway
    - Manufacturing processes being validated
    - Supply chain qualification in progress
    """)

with col2:
    st.markdown("""
    **Key Activities Underway**
    - Production rate ramp planning
    - Facility and tooling development
    - Workforce training and certification
    - Airworthiness and certification work
    """)

st.markdown("---")

# ===================== GANTT CHART =====================
st.header("MAAP Program Timeline")

st.markdown("High-level view of the major phases from the Integrated Master Schedule (IMS).")

df = pd.DataFrame([
    dict(Task="Phase 1: Program Initiation & Requirements", Start="2025-01-01", End="2025-09-30", Phase="Development"),
    dict(Task="Phase 2: Preliminary Design", Start="2025-09-01", End="2026-11-30", Phase="Development"),
    dict(Task="Phase 3: Critical Design", Start="2026-11-01", End="2027-12-31", Phase="Development"),
    dict(Task="Phase 4: Manufacturing Development", Start="2027-12-01", End="2029-05-31", Phase="Manufacturing"),
    dict(Task="Phase 5: System Integration & Test", Start="2028-06-01", End="2029-06-30", Phase="Test"),
    dict(Task="Phase 6: Flight Test & Qualification", Start="2028-04-01", End="2031-01-31", Phase="Flight Test"),
    dict(Task="Phase 7: Low-Rate Initial Production (LRIP)", Start="2030-01-01", End="2033-07-31", Phase="Production"),
    dict(Task="Phase 8: Full-Rate Production (FRP)", Start="2030-07-01", End="2035-12-31", Phase="Production"),
    dict(Task="Phase 9: Operational Deployment & IOC", Start="2030-03-01", End="2035-12-31", Phase="Operations"),
])

fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Task",
    color="Phase",
    color_discrete_map={
        "Development": "#1E3A5F",
        "Manufacturing": "#2E7D32",
        "Test": "#F57C00",
        "Flight Test": "#C62828",
        "Production": "#6A1B9A",
        "Operations": "#00695C"
    },
    title="MAAP-1 High-Level Program Timeline (from IMS)"
)

fig.update_yaxes(autorange="reversed")
fig.update_layout(height=550, xaxis_title="Timeline", legend_title="Phase")

st.plotly_chart(fig, use_container_width=True)
st.caption("Source: MAAP-1 Integrated Master Schedule (IMS) – Eurus Systems")