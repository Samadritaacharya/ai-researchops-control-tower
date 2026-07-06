# 🔬 AI ResearchOps Control Tower

> PMO-style control tower for managing uncertain AI/ML research initiatives — from project intake, uncertainty scoring, risk tracking, RAID, RACI, experiments and roadmap through governance, executive reporting, and product handover readiness.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![PMO](https://img.shields.io/badge/PMO-Governance-purple)
![ResearchOps](https://img.shields.io/badge/AI-ResearchOps-teal)
![CI](https://img.shields.io/badge/GitHub%20Actions-CI-green)

> **Disclaimer:** This is an independent portfolio project inspired by public software-engineering research and AI project-management themes. It is **not affiliated with JetBrains or any other organization**. All data is fictional/synthetic portfolio data.

---

## Demo

- **Live app:** [Open the AI ResearchOps Control Tower](https://ai-researchops-control-tower.streamlit.app/)
- **Screenshots:** See `assets/screenshots/` after adding exported screenshots.
- **Demo data:** Included in the repository so the app runs out of the box.

---

## Live demo workflow

1. Open the live app.
2. Use the sidebar input panel to enter an AI initiative, project stage, risk level and governance maturity.
3. Click **Generate PMO focus**.
4. Review the generated PMO focus recommendation.
5. Use the multipage sidebar to explore intake, uncertainty, risk, RACI, experiments, RAID, roadmap, steering report and governance checklist.

---

## Business problem

AI/ML research projects are often uncertain. Scope changes, unclear acceptance criteria, data dependencies, privacy constraints, experiment risk, stakeholder misalignment and weak product handover can make execution difficult.

This project demonstrates how a technical PM / PMO analyst can create structure around uncertain AI initiatives through governance, risk tracking, task readiness, stakeholder alignment, experiment visibility, roadmap planning, and executive communication.

---

## Solution

The Control Tower gives a Research Operations / Technical Project Manager a single place to track what matters:

- project intake and chartering
- uncertainty scoring
- risk register and RAID log
- task readiness
- stakeholder RACI
- experiment tracking
- roadmap and blockers
- executive steering report
- AI governance checklist
- product handover readiness

It is built around a realistic fictional case study: a **Proactive AI Coding Assistant** research program with tracks for intent detection, suggestion quality, privacy/data, and product handover.

---

## Key features

1. **Dashboard Overview** — portfolio KPIs and overview charts.
2. **Project Intake Wizard** — register projects and generate a charter.
3. **Uncertainty & Scope Matrix** — score and plot project uncertainty.
4. **AI/ML Risk Register** — risk taxonomy, heatmap, and high-severity flags.
5. **Task Completeness Analyzer** — nine-point task-readiness scoring.
6. **Stakeholder Map & RACI** — responsibilities and communication cadence.
7. **Experiment Tracker** — baseline, target, and actual metrics.
8. **Status & Communication** — weekly reports, decision log, and handover readiness.
9. **RAID Log** — risks, assumptions, issues, and dependencies.
10. **Roadmap View** — milestones, owners, blockers, and handover timeline.
11. **Executive Steering Report** — leadership-ready RAG status, KPIs, decisions needed, and top risks.
12. **AI Governance Checklist** — privacy, model quality, explainability, bias/fairness, security, adoption, and operational readiness.

---

## Tech stack

| Layer | Technology |
|---|---|
| App | Streamlit |
| Language | Python |
| Data | Pandas, NumPy |
| Visualization | Plotly |
| Testing | pytest |
| CI | GitHub Actions |
| Local setup | Windows PowerShell and macOS/Linux commands included |

---

## Windows PowerShell quick start

```powershell
cd $HOME
git clone https://github.com/Samadritaacharya/ai-researchops-control-tower.git
cd ai-researchops-control-tower
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m pytest tests
py -m streamlit run app.py
```

## Why this project is relevant to my target roles

This project directly connects to my profile across SAP Cloud Delivery Architecture / AIOps PMO, RWTH Management & Engineering, IBM/Kyndryl IT operations, and AI/ML research exposure.

It demonstrates practical skills for Technical Project Management, PMO, AI Transformation, Research Operations, Product Handover, Stakeholder Governance, cloud/AIOps-adjacent delivery environments and Digital Transformation.

## CV bullet

> Built an AI ResearchOps Control Tower using Python, Streamlit, Pandas, Plotly and GitHub Actions to manage AI/ML project intake, uncertainty scoring, risk tracking, RAID, stakeholder RACI, experiment metrics, governance controls and product handover readiness.

## Disclaimer

Independent portfolio project. Not affiliated with, endorsed by, or connected to JetBrains or any other organization. All data is fictional/synthetic sample data. No confidential SAP, IBM, Kyndryl, university, employer, or client data is used.
