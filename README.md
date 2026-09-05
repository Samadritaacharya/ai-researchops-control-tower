# AI ResearchOps Control Tower

[![CI](https://github.com/Samadritaacharya/ai-researchops-control-tower/actions/workflows/ci.yml/badge.svg)](https://github.com/Samadritaacharya/ai-researchops-control-tower/actions/workflows/ci.yml)

**A decision-oriented control tower for governing uncertain AI/ML initiatives from intake and experimentation through risk, stakeholder alignment, roadmap, steering communication, and product handover.**

[**Open live app →**](https://ai-researchops-control-tower.streamlit.app/) · [Source](https://github.com/Samadritaacharya/ai-researchops-control-tower)

> All initiatives and data are fictional or synthetic. No confidential employer, client, university, or personal data is included.

## What it solves

AI initiatives often change while teams are still learning about the data, model behavior, scope, feasibility, governance requirements, and product expectations. This project makes those uncertainties visible and gives teams one place to manage ownership, evidence, decisions, and handover readiness.

## Working modules

| Module | Decision supported |
|---|---|
| Dashboard Overview | What is the overall health of the initiative? |
| Project Intake Wizard | Is the initiative clearly defined and chartered? |
| Uncertainty & Scope Matrix | Where is ambiguity highest? |
| AI/ML Risk Register | Which model, data, governance, or adoption risks need ownership? |
| Task Completeness Analyzer | Is the work ready to enter delivery? |
| Stakeholder Map & RACI | Who is accountable, consulted, and informed? |
| Experiment Tracker | Are experiments progressing against measurable targets? |
| Status & Communication | Which decisions and escalations need attention? |
| RAID Log | Which risks, assumptions, issues, and dependencies affect delivery? |
| Roadmap View | Which milestones, blockers, and owners determine timing? |
| Executive Steering Report | What should leadership understand and decide? |
| AI Governance Checklist | Are privacy, quality, explainability, security, and adoption controls ready? |

## Governance model

The application connects technical uncertainty with delivery governance through:

- initiative intake and chartering
- uncertainty and scope scoring
- model/data/adoption risk registers
- experiment baselines, targets, and actuals
- stakeholder maps and RACI
- RAID and decision logs
- milestone roadmaps and blockers
- governance and handover readiness checks

The included scenario is synthetic and keeps the workflow fully usable without external API credentials.

## Verification

GitHub Actions installs the declared dependencies, compiles the application and utility modules, and runs the pytest suite on pushes and pull requests to `main`.

## Technology

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

## Design principle

ResearchOps should not pretend uncertainty has disappeared. It should make uncertainty measurable, assignable, discussable, and easier to govern as an initiative moves toward product delivery.
