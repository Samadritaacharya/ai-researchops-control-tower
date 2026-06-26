# 🔬 AI ResearchOps Control Tower

A Streamlit web application for managing **uncertain AI/ML software-engineering research projects** — end to end, from intake and uncertainty scoring through risk, tasks, stakeholders, experiments, and product handover.

> **Disclaimer:** This is an independent portfolio project inspired by public software-engineering research themes. It is **not affiliated with JetBrains or any other organization.**

---

## Overview

The Control Tower gives a Research Operations / Technical Project Manager a single place to track what matters in uncertain AI research: risk, task readiness, ownership, experiments, and product handover. It is built around a realistic case study — a **Proactive AI Coding Assistant** research program — with pre-populated sample data so it runs out of the box.

## Key features

1. **Dashboard Overview** — portfolio KPIs and overview charts.
2. **Project Intake Wizard** — register projects and generate a charter.
3. **Uncertainty & Scope Matrix** — score and plot project uncertainty.
4. **AI/ML Risk Register** — risk taxonomy, heatmap, and high-severity flags.
5. **Task Completeness Analyzer** — nine-point task-readiness scoring.
6. **Stakeholder Map & RACI** — responsibilities and communication cadence.
7. **Experiment Tracker** — baseline, target, and actual metrics.
8. **Status & Communication** — weekly reports, decision log, and product handover readiness scorecard.

## Case study

The sample data models a **Proactive AI Coding Assistant** research program with four tracks: intent detection, suggestion quality, privacy and data, and product handover.

## Tech stack

Python · Streamlit · Pandas · Plotly · NumPy · GitHub Actions · pytest

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

After cloning the repo, you can also run:

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

## Project structure

```text
ai-researchops-control-tower/
├── app.py
├── requirements.txt
├── README.md
├── WINDOWS_SETUP.md
├── run_local.ps1
├── data/
├── pages/
├── utils/
├── docs/
├── tests/
└── .github/workflows/ci.yml
```

## Scoring logic

| Score | Formula | Range |
|-------|---------|-------|
| Uncertainty | mean of 5 components | 1–10 |
| Task completeness | checked fields / 9 × 100 | 0–100 |
| Risk | impact × likelihood | 1–25 |
| Handover readiness | mean of 5 components × 10 | 0–100 |

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

## Disclaimer

Independent portfolio project. Not affiliated with, endorsed by, or connected to JetBrains or any other organization. All data is fictional sample data.

## Contact / portfolio

- **GitHub:** https://github.com/Samadritaacharya
- **LinkedIn:** https://www.linkedin.com/in/samadrita-acharya-a07266184/
