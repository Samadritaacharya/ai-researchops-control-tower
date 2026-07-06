"""AI governance checklist module for AI ResearchOps Control Tower."""

from __future__ import annotations

import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Governance Checklist", page_icon="✅", layout="wide")

st.title("✅ AI Governance Checklist")
st.markdown(
    "A practical checklist for reviewing AI/ML research initiatives before product handover. "
    "This page demonstrates responsible AI, governance awareness, and operational readiness thinking."
)

checklist = pd.DataFrame(
    [
        {"Area": "Data privacy", "Control": "Only synthetic or approved data is used in the portfolio/demo environment.", "Status": "Done", "Owner": "Governance Lead"},
        {"Area": "Data privacy", "Control": "Real-data usage requires documented approval and minimization review.", "Status": "Open", "Owner": "Governance Lead"},
        {"Area": "Model quality", "Control": "Baseline, target, and actual metrics are documented.", "Status": "Done", "Owner": "ML Lead"},
        {"Area": "Explainability", "Control": "Model limitations and decision boundaries are documented for stakeholders.", "Status": "In progress", "Owner": "Research PMO"},
        {"Area": "Bias and fairness", "Control": "Potential bias sources are identified before production use.", "Status": "Open", "Owner": "ML Lead"},
        {"Area": "Security", "Control": "Secrets and credentials are not committed to GitHub.", "Status": "Done", "Owner": "Developer"},
        {"Area": "Operational readiness", "Control": "Runbook, owner, escalation path, and handover checklist are completed.", "Status": "In progress", "Owner": "Technical PM"},
        {"Area": "Stakeholder adoption", "Control": "Stakeholder feedback has been captured and translated into next actions.", "Status": "In progress", "Owner": "Product Owner"},
    ]
)

status_filter = st.multiselect("Filter by status", sorted(checklist["Status"].unique()), default=sorted(checklist["Status"].unique()))
area_filter = st.multiselect("Filter by area", sorted(checklist["Area"].unique()), default=sorted(checklist["Area"].unique()))
filtered = checklist[checklist["Status"].isin(status_filter) & checklist["Area"].isin(area_filter)]

st.subheader("Governance controls")
st.dataframe(filtered, use_container_width=True, hide_index=True)

total = len(checklist)
done = int((checklist["Status"] == "Done").sum())
completion = round(done / total * 100, 1)

c1, c2, c3 = st.columns(3)
c1.metric("Checklist completion", f"{completion}%")
c2.metric("Open controls", int((checklist["Status"] == "Open").sum()))
c3.metric("In progress", int((checklist["Status"] == "In progress").sum()))

if completion < 80:
    st.warning("Governance readiness is not yet green. Complete open privacy, bias, and handover controls before product transition.")
else:
    st.success("Governance readiness is close to handover-ready.")

st.download_button(
    "Download governance checklist as CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="ai_governance_checklist.csv",
    mime="text/csv",
    use_container_width=True,
)

st.info(
    "Portfolio relevance: this module shows awareness of responsible AI, security, data privacy, explainability, stakeholder adoption, and operational handover readiness."
)
