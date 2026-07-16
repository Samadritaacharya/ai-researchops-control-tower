# AI ResearchOps Control Tower

A PMO-style control tower for managing uncertain AI/ML initiatives from intake and scope definition through risk, experiments, stakeholder governance, roadmap, steering communication, and product-handover readiness.

[![CI](https://github.com/Samadritaacharya/ai-researchops-control-tower/actions/workflows/ci.yml/badge.svg)](https://github.com/Samadritaacharya/ai-researchops-control-tower/actions/workflows/ci.yml)

**Live application:** [ai-researchops-control-tower.streamlit.app](https://ai-researchops-control-tower.streamlit.app/)  
**Portfolio owner:** [Samadrita Acharya](https://www.linkedin.com/in/samadrita-acharya-a07266184/)

## Recruiter quick view

| Area | Evidence in this project |
|---|---|
| Business problem | AI/ML initiatives combine technical uncertainty, evolving scope, data dependencies, governance risk, and difficult handovers. |
| Product solution | A multi-page Streamlit control tower for Research Operations and Technical PM/PMO workflows. |
| Project governance | Intake, chartering, uncertainty scoring, task readiness, RAID, RACI, roadmap, decision logs, and steering reports. |
| AI delivery | Experiment tracking, metric targets, model-risk categories, privacy, explainability, bias/fairness, security, and adoption readiness. |
| Product handover | Readiness checks connect research outputs to operational ownership and product delivery. |
| Engineering | Python, modular Streamlit pages, Pandas/NumPy/Plotly, pytest, compile checks, and GitHub Actions. |
| Data/privacy | Uses fictional initiatives and synthetic portfolio data only. |

## Business problem

AI initiatives are harder to govern than standard delivery projects because scope, data, model quality, acceptance criteria, privacy, and product feasibility can change during experimentation. Without a structured operating model, teams can lose visibility into blockers, decisions, risk ownership, and handover readiness.

## Solution

The Control Tower provides one decision-oriented workspace for:

- project intake and chartering
- uncertainty and scope scoring
- AI/ML risk registers
- task-completeness and readiness analysis
- stakeholder maps and RACI
- experiment baselines, targets, and actuals
- status reporting and decision logs
- RAID management
- milestone roadmaps and blockers
- executive steering reports
- AI governance checklists
- product-handover readiness

The application uses a fictional **Proactive AI Coding Assistant** program with workstreams for intent detection, suggestion quality, privacy/data, and product handover.

## Two-minute recruiter demo

1. Open the [live app](https://ai-researchops-control-tower.streamlit.app/).
2. Enter an AI initiative, project stage, risk level, and governance maturity.
3. Click **Generate PMO focus**.
4. Review the uncertainty, risk, and stakeholder views.
5. Open the experiment tracker, RAID log, and roadmap.
6. Finish with the steering report, governance checklist, and handover readiness.

## Core modules

| Module | Delivery question answered |
|---|---|
| Dashboard Overview | What is the overall health of the initiative? |
| Project Intake Wizard | Is the initiative clearly defined and chartered? |
| Uncertainty & Scope Matrix | Where is ambiguity highest? |
| AI/ML Risk Register | Which model, data, governance, or adoption risks need ownership? |
| Task Completeness Analyzer | Is the work ready to enter delivery? |
| Stakeholder Map & RACI | Who is accountable, consulted, and informed? |
| Experiment Tracker | Are model experiments progressing against measurable targets? |
| Status & Communication | Which decisions and escalations need stakeholder attention? |
| RAID Log | What risks, assumptions, issues, and dependencies affect delivery? |
| Roadmap View | Which milestones, blockers, and owners determine handover timing? |
| Executive Steering Report | What should leadership understand and decide? |
| AI Governance Checklist | Are privacy, quality, explainability, security, and adoption controls ready? |

## Quality and automation

The repository includes a GitHub Actions workflow that:

- installs the declared Python dependencies
- compiles the application, page, utility, and test modules
- runs the pytest suite on pushes and pull requests to `main`

The live demo uses included fictional data and does not require an external API key.

## Technology stack

`Python 3.11` · `Streamlit` · `Pandas` · `NumPy` · `Plotly` · `pytest` · `GitHub Actions`

## Run locally

```bash
git clone https://github.com/Samadritaacharya/ai-researchops-control-tower.git
cd ai-researchops-control-tower
python -m venv .venv
```

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
python -m streamlit run app.py
```

## Skills demonstrated

Technical project management · AI transformation · Research Operations · AI/ML delivery governance · PMO · RAID · RACI · uncertainty management · stakeholder communication · experiment tracking · AI governance · product handover · executive reporting · Python engineering

## Why this project is relevant to my profile

This project connects my SAP Cloud Delivery Architecture/AIOps and PMO experience, RWTH Management & Engineering background, IBM/Kyndryl service operations, and applied AI/ML research exposure. It demonstrates how I bring delivery structure, stakeholder governance, and decision visibility to technically uncertain initiatives.

## CV / LinkedIn project description

> Built an AI ResearchOps Control Tower using Python, Streamlit, Pandas, Plotly, pytest, and GitHub Actions to manage AI/ML project intake, uncertainty, task readiness, risk, RAID, stakeholder RACI, experiment metrics, governance controls, roadmaps, steering communication, and product-handover readiness.

## Responsible portfolio use

This is an independent portfolio project. It is not affiliated with JetBrains or any other organization. All initiatives and data are fictional or synthetic, and no confidential SAP, IBM, Kyndryl, university, employer, or client data is used.
