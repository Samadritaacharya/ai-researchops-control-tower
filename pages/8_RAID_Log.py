"""RAID Log module for AI ResearchOps Control Tower."""

from __future__ import annotations

import pandas as pd
import streamlit as st

st.set_page_config(page_title="RAID Log", page_icon="📌", layout="wide")

st.title("📌 RAID Log")
st.markdown(
    "Track **Risks, Assumptions, Issues, and Dependencies** for uncertain AI/ML research initiatives. "
    "This page demonstrates PMO-style governance for AI delivery and research operations."
)

raid_data = pd.DataFrame(
    [
        {
            "Type": "Risk",
            "Item": "Model quality may not reach target acceptance threshold before handover.",
            "Owner": "ML Lead",
            "Impact": "High",
            "Status": "Open",
            "Next Step": "Review experiment metrics and define fallback baseline.",
        },
        {
            "Type": "Assumption",
            "Item": "Synthetic evaluation data is representative enough for portfolio demonstration.",
            "Owner": "Research PMO",
            "Impact": "Medium",
            "Status": "Accepted",
            "Next Step": "Document limitations in the handover note.",
        },
        {
            "Type": "Issue",
            "Item": "Stakeholder feedback is needed before finalizing release-readiness criteria.",
            "Owner": "Product Owner",
            "Impact": "Medium",
            "Status": "In progress",
            "Next Step": "Schedule review and capture decision log.",
        },
        {
            "Type": "Dependency",
            "Item": "Privacy review must be completed before using real user data.",
            "Owner": "Governance Lead",
            "Impact": "High",
            "Status": "Open",
            "Next Step": "Keep demo on synthetic data and prepare privacy checklist.",
        },
        {
            "Type": "Risk",
            "Item": "Unclear ownership may delay product handover after successful research validation.",
            "Owner": "Technical PM",
            "Impact": "High",
            "Status": "Open",
            "Next Step": "Confirm RACI and operational handover owner.",
        },
    ]
)

filters = st.columns(3)
with filters[0]:
    selected_type = st.multiselect("RAID type", sorted(raid_data["Type"].unique()), default=sorted(raid_data["Type"].unique()))
with filters[1]:
    selected_status = st.multiselect("Status", sorted(raid_data["Status"].unique()), default=sorted(raid_data["Status"].unique()))
with filters[2]:
    selected_impact = st.multiselect("Impact", sorted(raid_data["Impact"].unique()), default=sorted(raid_data["Impact"].unique()))

filtered = raid_data[
    raid_data["Type"].isin(selected_type)
    & raid_data["Status"].isin(selected_status)
    & raid_data["Impact"].isin(selected_impact)
]

st.subheader("RAID register")
st.dataframe(filtered, use_container_width=True, hide_index=True)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total RAID items", len(filtered))
c2.metric("Open items", int((filtered["Status"] == "Open").sum()))
c3.metric("High impact", int((filtered["Impact"] == "High").sum()))
c4.metric("Dependencies", int((filtered["Type"] == "Dependency").sum()))

st.download_button(
    "Download RAID log as CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="ai_researchops_raid_log.csv",
    mime="text/csv",
    use_container_width=True,
)

st.info(
    "Portfolio relevance: this module demonstrates risk tracking, assumptions management, issue escalation, dependency visibility, and PMO governance for AI/ML projects."
)
