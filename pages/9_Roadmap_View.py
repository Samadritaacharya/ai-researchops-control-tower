"""Roadmap view module for AI ResearchOps Control Tower."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Roadmap View", page_icon="🗺️", layout="wide")

st.title("🗺️ Roadmap View")
st.markdown(
    "Visualize AI/ML research milestones, delivery owners, blockers, and handover readiness. "
    "This module connects research uncertainty with project-management planning."
)

roadmap = pd.DataFrame(
    [
        {
            "Milestone": "Project intake and charter",
            "Track": "PMO Setup",
            "Owner": "Technical PM",
            "Start": "2026-07-01",
            "Finish": "2026-07-05",
            "Status": "Done",
            "Blocker": "None",
        },
        {
            "Milestone": "Baseline model evaluation",
            "Track": "Experimentation",
            "Owner": "ML Lead",
            "Start": "2026-07-06",
            "Finish": "2026-07-12",
            "Status": "Done",
            "Blocker": "None",
        },
        {
            "Milestone": "Risk and privacy review",
            "Track": "Governance",
            "Owner": "Governance Lead",
            "Start": "2026-07-10",
            "Finish": "2026-07-18",
            "Status": "In progress",
            "Blocker": "Privacy checklist sign-off",
        },
        {
            "Milestone": "Stakeholder demo and feedback",
            "Track": "Stakeholder Alignment",
            "Owner": "Product Owner",
            "Start": "2026-07-16",
            "Finish": "2026-07-22",
            "Status": "Planned",
            "Blocker": "Demo slot confirmation",
        },
        {
            "Milestone": "Product handover readiness review",
            "Track": "Handover",
            "Owner": "Technical PM",
            "Start": "2026-07-23",
            "Finish": "2026-07-30",
            "Status": "Planned",
            "Blocker": "RACI and runbook finalization",
        },
    ]
)
roadmap["Start"] = pd.to_datetime(roadmap["Start"])
roadmap["Finish"] = pd.to_datetime(roadmap["Finish"])

status_filter = st.multiselect("Filter by status", sorted(roadmap["Status"].unique()), default=sorted(roadmap["Status"].unique()))
filtered = roadmap[roadmap["Status"].isin(status_filter)]

fig = px.timeline(
    filtered,
    x_start="Start",
    x_end="Finish",
    y="Milestone",
    color="Status",
    hover_data=["Track", "Owner", "Blocker"],
    title="AI ResearchOps Roadmap",
)
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Milestone table")
st.dataframe(filtered, use_container_width=True, hide_index=True)

open_blockers = filtered[filtered["Blocker"].str.lower() != "none"]
st.metric("Milestones with blockers", len(open_blockers))
if not open_blockers.empty:
    st.warning("Open blockers need PMO follow-up before handover readiness can be marked green.")
    st.dataframe(open_blockers[["Milestone", "Owner", "Blocker"]], use_container_width=True, hide_index=True)

st.download_button(
    "Download roadmap as CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="ai_researchops_roadmap.csv",
    mime="text/csv",
    use_container_width=True,
)
