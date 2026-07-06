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

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
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
        h1, h2, h3 {{ color: {SECONDARY}; }}
        .stMetric {{
            background: #F4F8F9;
            border-left: 5px solid {PRIMARY};
            border-radius: 8px;
            padding: 12px 16px;
        }}
        .disclaimer {{
            background: #FFF6E6;
            border: 1px solid #F39C12;
            border-radius: 8px;
            padding: 12px 16px;
            margin-bottom: 16px;
            color: #7a5b13;
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


def main():
    inject_brand_css()

    st.title("🔬 AI ResearchOps Control Tower")
    st.markdown(
        "A PMO-style control tower for managing **uncertain AI/ML software-engineering "
        "research projects** — from intake and uncertainty scoring through risk, "
        "tasks, stakeholders, experiments, RAID, roadmap, governance, executive reporting, "
        "and product handover."
    )

    # Disclaimer - clearly visible, not hidden.
    st.markdown(
        '<div class="disclaimer"><strong>Disclaimer:</strong> This is an '
        "independent portfolio project inspired by public software-engineering "
        "research themes. It is not affiliated with JetBrains or any other "
        "organization. All data is fictional or synthetic portfolio data.</div>",
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------------------------
    # Load data (degrades gracefully thanks to fallbacks in data_loader)
    # -----------------------------------------------------------------------
    try:
        projects = load_project_data()
        risks = load_risks()
        tasks = load_tasks()
    except Exception as exc:  # noqa: BLE001
        st.error(f"Could not load sample data: {exc}")
        return

    # -----------------------------------------------------------------------
    # KPI cards
    # -----------------------------------------------------------------------
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
            f"⚠️ {high_risks} high-severity risk(s) (score > 15) need attention. "
            "See the **Risk Register** and **RAID Log** pages."
        )

    # -----------------------------------------------------------------------
    # Charts
    # -----------------------------------------------------------------------
    st.subheader("Overview charts")
    col_a, col_b = st.columns(2)
    with col_a:
        st.plotly_chart(project_status_pie(projects), use_container_width=True)
    with col_b:
        st.plotly_chart(uncertainty_distribution(projects), use_container_width=True)

    st.plotly_chart(risk_heatmap(risks), use_container_width=True)

    # -----------------------------------------------------------------------
    # Navigation
    # -----------------------------------------------------------------------
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
        ("AI Governance Checklist", "Review data privacy, model quality, explainability, security, adoption, and handover controls."),
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
