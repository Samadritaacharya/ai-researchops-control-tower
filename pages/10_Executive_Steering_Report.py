"""Executive steering report module for AI ResearchOps Control Tower."""

from __future__ import annotations

from datetime import date
from io import StringIO

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Executive Steering Report", page_icon="📊", layout="wide")

st.title("📊 Executive Steering Report")
st.markdown(
    "Generate a leadership-ready project status report for uncertain AI/ML initiatives. "
    "The goal is to translate research complexity into clear PMO communication."
)

with st.sidebar:
    st.header("Report inputs")
    project_name = st.text_input("Project name", "Proactive AI Coding Assistant Research Program")
    reporting_date = st.date_input("Reporting date", value=date.today())
    rag_status = st.selectbox("Overall RAG status", ["Green", "Amber", "Red"], index=1)
    sponsor = st.text_input("Sponsor", "Product & Engineering Leadership")

summary = {
    "Project": project_name,
    "Reporting date": str(reporting_date),
    "Sponsor": sponsor,
    "RAG status": rag_status,
    "Overall health": "Delivery is progressing, but privacy review and product handover ownership require active follow-up.",
    "Decision needed": "Confirm handover owner and approve readiness checklist before product transition.",
    "Next review": "Weekly research operations sync and monthly steering update.",
}

metrics = pd.DataFrame(
    [
        {"Metric": "Experiment target achievement", "Value": "78%", "Status": "Amber"},
        {"Metric": "Task completeness", "Value": "84%", "Status": "Green"},
        {"Metric": "Open high-severity risks", "Value": "2", "Status": "Red"},
        {"Metric": "Handover readiness", "Value": "72%", "Status": "Amber"},
    ]
)

risks = pd.DataFrame(
    [
        {"Risk": "Privacy review not completed", "Impact": "High", "Owner": "Governance Lead", "Mitigation": "Use synthetic data and complete checklist before real-data use."},
        {"Risk": "Product handover owner unclear", "Impact": "High", "Owner": "Technical PM", "Mitigation": "Confirm RACI and operating owner in next steering review."},
        {"Risk": "Model quality below target", "Impact": "Medium", "Owner": "ML Lead", "Mitigation": "Maintain fallback baseline and compare experiment outcomes."},
    ]
)

st.subheader("Executive summary")
cols = st.columns(4)
cols[0].metric("RAG", summary["RAG status"])
cols[1].metric("Task completeness", "84%")
cols[2].metric("Open high risks", "2")
cols[3].metric("Handover readiness", "72%")

st.info(summary["Overall health"])
st.warning(f"Decision needed: {summary['Decision needed']}")

st.subheader("KPI status")
st.dataframe(metrics, use_container_width=True, hide_index=True)

st.subheader("Top risks and mitigations")
st.dataframe(risks, use_container_width=True, hide_index=True)

st.subheader("Leadership report export")
report = StringIO()
report.write(f"# Executive Steering Report: {project_name}\n\n")
for key, value in summary.items():
    report.write(f"- **{key}:** {value}\n")
report.write("\n## KPI status\n")
for _, row in metrics.iterrows():
    report.write(f"- **{row['Metric']}:** {row['Value']} ({row['Status']})\n")
report.write("\n## Top risks\n")
for _, row in risks.iterrows():
    report.write(f"- **{row['Risk']}** | Impact: {row['Impact']} | Owner: {row['Owner']} | Mitigation: {row['Mitigation']}\n")

st.download_button(
    "Download executive report as Markdown",
    data=report.getvalue().encode("utf-8"),
    file_name="executive_steering_report.md",
    mime="text/markdown",
    use_container_width=True,
)

st.download_button(
    "Download top risks as CSV",
    data=risks.to_csv(index=False).encode("utf-8"),
    file_name="executive_top_risks.csv",
    mime="text/csv",
    use_container_width=True,
)
