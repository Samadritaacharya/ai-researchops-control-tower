"""AI ResearchOps Control Tower - main dashboard.

Run with:
    streamlit run app.py

This is the landing page. The module pages live in the ``pages/`` folder
and appear automatically in the sidebar (Streamlit multipage convention).
"""

import streamlit as st

from utils.data_loader import (
    load_project_data,
    load_risks,
    load_tasks,
)
from utils.scoring import (
    calculate_risk_score,
    calculate_task_completeness,
    is_high_risk,
)
from utils.visualization import (
    PRIMARY,
    SECONDARY,
    project_status_pie,
    risk_heatmap,
    uncertainty_distribution,
)

st.set_page_config(
    page_title="AI ResearchOps Control Tower",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


def inject_brand_css():
    """Apply the teal/navy brand styling shared across pages."""
    st.markdown(
        f"""
        <style>
        .hero {{
            background: linear-gradient(135deg, #06252b 0%, #0f5661 55%, {PRIMARY} 100%);
            color: white;
            padding: 2rem 2.2rem;
            border-radius: 22px;
            margin-bottom: 1.4rem;
            box-shadow: 0 18px 55px rgba(6, 37, 43, 0.22);
        }}
        .hero h1 {{font-size: 2.35rem; margin: 0 0 .55rem 0; letter-spacing: -.04em; color: white;}}
        .hero p {{font-size: 1.02rem; max-width: 980px; color: #e4fbff; margin: 0;}}
        h1, h2, h3 {{ color: {SECONDARY}; }}
        div[data-testid="stMetric"] {{
            background: #F4F8F9;
            border-left: 5px solid {PRIMARY};
            border-radius: 10px;
            padding: 12px 16px;
        }}
        .disclaimer {{
            background: #FFF6E6;
            border: 1px solid #F39C12;
            border-radius: 10px;
            padding: 12px 16px;
            margin-bottom: 16px;
            color: #7a5b13;
        }}
        .input-card {{
            background: #F7FBFC;
            border: 1px solid #D8E7EA;
            border-left: 5px solid {PRIMARY};
            border-radius: 14px;
            padding: 1rem 1.1rem;
            margin: 10px 0 18px;
        }}
        .module-card {{
            background: #F7FBFC;
            border: 1px solid #D8E7EA;
            border-left: 5px solid {PRIMARY};
            border-radius: 10px;
            padding: 14px 16px;
            margin: 8px 0;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 12px;
            border-top: 1px solid #ddd;
            color: #888;
            font-size: 0.85rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def pmo_recommendation(stage: str, risk_level: str, governance: str) -> str:
    """Simple demo recommendation for the live landing-page input workflow."""
    if risk_level == "High" or governance == "Low":
        return "Focus first on RAID visibility, governance checklist, RACI ownership and executive steering decisions."
    if stage in ("Experiment validation", "Product handover"):
        return "Prioritize experiment evidence, acceptance criteria, handover readiness and decision-log clarity."
    return "Start with project intake, uncertainty scoring, stakeholder RACI and a lightweight weekly status cadence."


def main():
    inject_brand_css()

    st.markdown(
        """
        <div class="hero">
          <h1>🔬 AI ResearchOps Control Tower</h1>
          <p>Interactive PMO-style control tower for uncertain AI/ML initiatives — from intake and uncertainty scoring to RAID, RACI, experiments, roadmap, governance, steering reports and handover readiness.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="disclaimer"><strong>Disclaimer:</strong> Independent portfolio project with fictional/synthetic portfolio data. No employer or client data is used.</div>',
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.header("🎛️ Live demo input")
        initiative = st.text_input("AI initiative", "Proactive AI Coding Assistant")
        stage = st.selectbox("Project stage", ["Intake", "Experiment validation", "Stakeholder alignment", "Product handover"])
        risk_level = st.selectbox("Current risk level", ["Low", "Medium", "High"], index=1)
        governance = st.selectbox("Governance maturity", ["Low", "Medium", "High"], index=1)
        run_demo = st.button("🚀 Generate PMO focus", width="stretch", type="primary")
        st.caption("Use this input during interviews to explain how AI uncertainty becomes structured PMO governance.")

    if run_demo:
        st.success("Live PMO recommendation generated from your input scenario.")

    st.markdown(
        f"""
        <div class="input-card">
          <b>Demo scenario:</b> {initiative} · stage: {stage} · risk: {risk_level} · governance maturity: {governance}<br>
          <b>Recommended PMO focus:</b> {pmo_recommendation(stage, risk_level, governance)}
        </div>
        """,
        unsafe_allow_html=True,
    )

    try:
        projects = load_project_data()
        risks = load_risks()
        tasks = load_tasks()
    except Exception as exc:  # noqa: BLE001
        st.error(f"Could not load sample data: {exc}")
        return

    total_projects = len(projects)
    active_research = int((projects["status"] == "Active").sum())

    risks = risks.copy()
    risks["risk_score"] = risks.apply(
        lambda r: calculate_risk_score(r["impact"], r["likelihood"]), axis=1
    )
    open_risks = int((risks["status"].str.lower() == "open").sum())

    completeness = tasks.apply(
        lambda r: calculate_task_completeness(r.to_dict()), axis=1
    )
    avg_completion = completeness.mean() if len(completeness) else 0

    st.subheader("Portfolio at a glance")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Projects", total_projects)
    c2.metric("Active Research", active_research)
    c3.metric("Open Risks", open_risks)
    c4.metric("Task Completion Rate", f"{avg_completion:.0f}%")

    high_risks = int(risks["risk_score"].apply(is_high_risk).sum())
    if high_risks:
        st.warning(
            f"⚠️ {high_risks} high-severity risk(s) need attention. "
            "See the Risk Register and RAID Log pages."
        )

    st.subheader("Overview charts")
    col_a, col_b = st.columns(2)
    with col_a:
        st.plotly_chart(project_status_pie(projects), width="stretch")
    with col_b:
        st.plotly_chart(uncertainty_distribution(projects), width="stretch")
    st.plotly_chart(risk_heatmap(risks), width="stretch")

    st.subheader("Modules")
    modules = [
        ("Project Intake", "Register new research projects and generate a charter."),
        ("Uncertainty Matrix", "Score and plot project uncertainty."),
        ("Risk Register", "Manage AI/ML risk taxonomy and heatmap."),
        ("Task Completeness", "Score task readiness across nine dimensions."),
        ("Stakeholder RACI", "Map stakeholders and responsibilities."),
        ("Experiment Tracker", "Track ML experiments and success rates."),
        ("Status & Communication", "Generate weekly status reports and handover readiness."),
        ("RAID Log", "Track risks, assumptions, issues, and dependencies."),
        ("Roadmap View", "Visualize milestones, owners, blockers, and handover timeline."),
        ("Executive Steering Report", "Create leadership-ready RAG, KPI, and risk summaries."),
        ("AI Governance Checklist", "Review privacy, model quality, explainability, security, adoption, and handover controls."),
    ]
    for title, description in modules:
        st.markdown(
            f'<div class="module-card"><strong>{title}</strong><br>{description}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="footer">AI ResearchOps Control Tower &middot; '
        '<a href="https://github.com/Samadritaacharya/ai-researchops-control-tower" target="_blank">View on GitHub</a> &middot; '
        "Independent portfolio project.</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
