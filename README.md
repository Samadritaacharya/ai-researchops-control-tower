# 🔬 AI ResearchOps Control Tower

A Streamlit web application for managing **uncertain AI/ML software-engineering
research projects** — end to end, from intake and uncertainty scoring through
risk, tasks, stakeholders, experiments, and product handover.

> **Disclaimer:** This is an independent portfolio project inspired by public
> software-engineering research themes. It is **not affiliated with JetBrains or
> any other organization.**

---

## Overview
The Control Tower gives a Research Operations / Technical Project Manager a
single place to track what matters in messy, uncertain AI research: how risky a
project is, whether its tasks are actually ready, who owns what, which
experiments are working, and when a prototype is mature enough to hand over to
engineering. It is built around a realistic case study — a *Proactive AI Coding
Assistant* research program — with pre-populated sample data so it runs out of
the box.

**Who it's for:** ResearchOps / Technical PM candidates and teams who want a
lightweight, opinionated operating model for AI/ML research delivery.

## Why I built this
AI research rarely fails on the modeling — it fails on coordination, unclear
scope, unmanaged risk, and fuzzy handover. I built this to demonstrate a
concrete, working methodology for running AI/ML research like a managed program:
quantified uncertainty, an explicit risk taxonomy, task-readiness scoring, RACI,
experiment tracking, and a handover gate — all in one tool.

## Key features (8 modules)
1. **Dashboard Overview** — portfolio KPIs and overview charts.
2. **Project Intake Wizard** — register projects and auto-generate a charter.
3. **Uncertainty & Scope Matrix** — score and plot project uncertainty.
4. **AI/ML Risk Register** — risk taxonomy, heatmap, high-severity flags.
5. **Task Completeness Analyzer** — nine-point task-readiness scoring.
6. **Stakeholder Map & RACI** — responsibilities and communication cadence.
7. **Experiment Tracker** — baseline vs actual metrics and success rates.
8. **Status & Communication** — weekly reports, decision log, and the
   **Product Handover Readiness** scorecard.

## Case study
The sample data models a **Proactive AI Coding Assistant** research program with
four tracks: intent detection, suggestion quality, privacy & data, and product
handover. See [`docs/final_case_study.md`](docs/final_case_study.md) for the
full narrative.

## Tech stack
Python · Streamlit · Pandas · Plotly · NumPy · GitHub Actions (CI) · pytest

## Installation
```bash
git clone <your-repo-url>
cd ai-researchops-control-tower
pip install -r requirements.txt
```

## Running the app
```bash
streamlit run app.py
```
Then open the local URL Streamlit prints (usually http://localhost:8501).

## Project structure
```
ai-researchops-control-tower/
├── app.py                       # Main dashboard
├── requirements.txt
├── README.md
├── LICENSE                      # MIT
├── conftest.py                  # pytest path setup
├── data/                        # 5 sample CSVs
├── pages/                       # 7 Streamlit module pages
├── utils/                       # scoring, data_loader, visualization, ui
├── docs/                        # 7 documentation artifacts + screenshots
├── .github/
│   ├── workflows/ci.yml         # CI: tests + lint
│   └── ISSUE_TEMPLATE/          # 4 issue templates
└── tests/test_scoring.py        # unit tests
```

## How to use
1. **Dashboard** — start here for portfolio KPIs and overview charts.
2. **Project Intake** — fill the form, create a project, download its charter.
3. **Uncertainty Matrix** — read the bubble matrix and use the what-if sliders.
4. **Risk Register** — review the heatmap, add/remove risks, watch for >15 flags.
5. **Task Completeness** — see traffic-light task health and inspect any task.
6. **Stakeholder RACI** — filter by project, read the RACI and cadence table.
7. **Experiment Tracker** — filter by track/project, check success rates.
8. **Status & Communication** — generate a weekly report, log decisions, and
   score handover readiness.

## Artifacts included (docs/)
- `project_charter.md` — charter template
- `researchops_process_map.md` — end-to-end process flow
- `stakeholder_communication_plan.md` — cadence and escalation
- `ai_ml_risk_framework.md` — full risk taxonomy
- `legal_admin_checklist.md` — pre-handover legal checklist
- `decision_log.md` — decision record template + examples
- `final_case_study.md` — the full case-study narrative

## Scoring logic (at a glance)
| Score | Formula | Range |
|-------|---------|-------|
| Uncertainty | mean of 5 components | 1–10 |
| Task completeness | checked fields / 9 × 100 | 0–100 |
| Risk | impact × likelihood | 1–25 |
| Handover readiness | mean of 5 components × 10 | 0–100 |

High-risk flag: score > 15. Handover-ready flag: score > 80.

## Testing
```bash
pytest tests/
```
CI runs the same tests on Python 3.9 and 3.11 on every push to `main`.

## Disclaimer
Independent portfolio project. Not affiliated with, endorsed by, or connected to
JetBrains or any other organization. All data is fictional sample data.

## Future enhancements
- Persist user-created records to disk or a database.
- Authentication and multi-user workspaces.
- Live experiment-tracking integrations (e.g. MLflow, Weights & Biases).
- Automated weekly report delivery via email/Slack.

## Contact / portfolio
- **GitHub:** <your-github-url>
- **LinkedIn:** <your-linkedin-url>
