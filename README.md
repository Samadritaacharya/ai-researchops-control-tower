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

- **Live app:** Deployment-ready; add Streamlit Cloud URL after deployment.
- **Screenshots:** See `assets/screenshots/` after adding exported screenshots.
- **Demo data:** Included in the repository so the app runs out of the box.

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

## Architecture

```text
ai-researchops-control-tower/
├── app.py
├── requirements.txt
├── README.md
├── WINDOWS_SETUP.md
├── run_local.ps1
├── data/
├── pages/
│   ├── 8_RAID_Log.py
│   ├── 9_Roadmap_View.py
│   ├── 10_Executive_Steering_Report.py
│   └── 11_AI_Governance_Checklist.py
├── utils/
├── docs/
├── assets/
│   └── screenshots/
├── tests/
└── .github/workflows/ci.yml
```

---

## Windows PowerShell quick start

Open PowerShell and run:

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

Then open the local URL Streamlit prints, usually `http://localhost:8501`.

## Already cloned?

```powershell
cd $HOME\ai-researchops-control-tower
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m pytest tests
py -m streamlit run app.py
```

## One-command Windows launcher

```powershell
cd $HOME\ai-researchops-control-tower
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\run_local.ps1
```

## macOS/Linux quick start

```bash
git clone https://github.com/Samadritaacharya/ai-researchops-control-tower.git
cd ai-researchops-control-tower
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest tests
python -m streamlit run app.py
```

---

## Scoring logic

| Score | Formula | Range |
|-------|---------|-------|
| Uncertainty | mean of 5 components | 1–10 |
| Task completeness | checked fields / 9 × 100 | 0–100 |
| Risk | impact × likelihood | 1–25 |
| Handover readiness | mean of 5 components × 10 | 0–100 |

---

## Example use case

A technical PM or PMO analyst is supporting an AI research initiative. The team needs visibility into what is known, what is uncertain, what risks need escalation, which experiments are progressing, what stakeholders need updates, and whether the project is ready for product handover.

This dashboard translates that uncertainty into structured PMO views: RAG status, risk heatmaps, RAID logs, roadmap blockers, governance readiness, executive updates, and product handover signals.

---

## Skills demonstrated

- Technical project management
- PMO governance
- AI/ML research operations
- Risk and RAID management
- Stakeholder RACI mapping
- Experiment tracking
- Product handover readiness
- Executive status reporting
- Governance and responsible AI awareness
- Python dashboard development
- Data visualization with Plotly
- GitHub Actions CI and tests
- Documentation and recruiter-facing product packaging

---

## Why this project is relevant to my target roles

This project directly connects to my profile across SAP Cloud Delivery Architecture / AIOps PMO, RWTH Management & Engineering, IBM/Kyndryl IT operations, and AI/ML research exposure.

It demonstrates practical skills for:

- Technical Project Management
- PMO / Project Coordination
- AI Transformation
- Research Operations
- Product Handover
- Stakeholder Governance
- Cloud / AIOps-adjacent delivery environments
- Digital Transformation

The project shows how I can turn complex and uncertain technical initiatives into structured governance, reporting, risk tracking, and delivery-readiness workflows.

---

## CV bullet

> Built an AI ResearchOps Control Tower using Python, Streamlit, Pandas, Plotly and GitHub Actions to manage AI/ML project intake, uncertainty scoring, risk tracking, RAID, stakeholder RACI, experiment metrics, governance controls and product handover readiness.

---

## LinkedIn post idea

> AI/ML projects are often uncertain by nature. Scope changes, unclear ownership, data dependencies, experiment risk and product handover gaps can make execution difficult. I built an AI ResearchOps Control Tower to show how PMO thinking can support AI research projects through intake, uncertainty scoring, RAID, RACI, experiments, governance and executive reporting.

---

## Roadmap

- [x] Project intake and charter
- [x] Uncertainty matrix
- [x] Risk register
- [x] Task completeness scoring
- [x] Stakeholder RACI
- [x] Experiment tracker
- [x] Weekly status and communication
- [x] RAID log
- [x] Roadmap view
- [x] Executive steering report
- [x] AI governance checklist
- [ ] Add deployed Streamlit demo URL
- [ ] Add screenshots and short demo GIF
- [ ] Add PDF export for executive steering report
- [ ] Add editable persistent storage

---

## Common Windows error

If you see this:

```text
Could not open requirements file: No such file or directory: requirements.txt
```

You are not inside the project folder. Run:

```powershell
cd $HOME\ai-researchops-control-tower
```

Then install again.

If `pytest` or `streamlit` is not recognized, use:

```powershell
py -m pytest tests
py -m streamlit run app.py
```

---

## Disclaimer

Independent portfolio project. Not affiliated with, endorsed by, or connected to JetBrains or any other organization. All data is fictional/synthetic sample data. No confidential SAP, IBM, Kyndryl, university, employer, or client data is used.

---

## Contact / portfolio

- **GitHub:** https://github.com/Samadritaacharya
- **LinkedIn:** https://www.linkedin.com/in/samadrita-acharya-a07266184/
- **Portfolio website:** Coming soon
