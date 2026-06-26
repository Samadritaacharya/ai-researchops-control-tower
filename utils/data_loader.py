"""Data loading helpers with small in-memory fallbacks."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def _load_csv(filename, fallback_rows):
    path = DATA_DIR / filename
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame(fallback_rows)


def load_project_data():
    return _load_csv(
        "sample_research_projects.csv",
        [
            {"project_id":"P001","project_name":"Proactive AI Coding Assistant","research_goal":"Evaluate proactive AI suggestions in IDE","primary_researcher":"Alice Chen","status":"Active","goal_volatility":7,"data_uncertainty":6,"model_uncertainty":8,"stakeholder_dependency":7,"legal_complexity":6},
            {"project_id":"P002","project_name":"Intent Detection Model","research_goal":"Build classifier for developer intent","primary_researcher":"Bob Smith","status":"Active","goal_volatility":5,"data_uncertainty":4,"model_uncertainty":6,"stakeholder_dependency":5,"legal_complexity":3},
            {"project_id":"P003","project_name":"Privacy Assessment","research_goal":"Evaluate data privacy risks","primary_researcher":"Carol White","status":"Completed","goal_volatility":8,"data_uncertainty":7,"model_uncertainty":5,"stakeholder_dependency":8,"legal_complexity":9},
        ],
    )


def load_risks():
    return _load_csv(
        "risk_register.csv",
        [
            {"risk_id":"R001","project_id":"P001","title":"Model drift over time","category":"Model Risks","description":"AI model performance may degrade with new IDE versions","impact":4,"likelihood":4,"mitigation":"Monitor model performance quarterly","owner":"Alice Chen","status":"Open"},
            {"risk_id":"R002","project_id":"P001","title":"Privacy violation","category":"Data Risks","description":"Potential exposure of developer code context","impact":5,"likelihood":3,"mitigation":"Implement data anonymization","owner":"Bob Smith","status":"Mitigated"},
            {"risk_id":"R003","project_id":"P002","title":"Training data bias","category":"Data Risks","description":"Training data may not represent diverse coding styles","impact":3,"likelihood":5,"mitigation":"Diversify training dataset","owner":"Bob Smith","status":"Open"},
        ],
    )


def load_tasks():
    return _load_csv(
        "task_backlog.csv",
        [
            {"task_id":"T001","project_id":"P001","task_name":"Define intent taxonomy","owner":"Bob Smith","status":"In Progress","clear_objective":"Yes","has_owner":"Yes","has_output":"Yes","acceptance_criteria":"Yes","dependencies":"None","ai_metric":"Accuracy metric","risk_level":"High","timeline":"2024-06-30","stakeholder_impact":"Critical"},
            {"task_id":"T002","project_id":"P001","task_name":"Collect IDE telemetry","owner":"Alice Chen","status":"Completed","clear_objective":"Yes","has_owner":"Yes","has_output":"Yes","acceptance_criteria":"Yes","dependencies":"T001","ai_metric":"Data quality","risk_level":"Medium","timeline":"2024-05-15","stakeholder_impact":"Critical"},
            {"task_id":"T003","project_id":"P002","task_name":"Train intent classifier","owner":"Bob Smith","status":"In Progress","clear_objective":"Yes","has_owner":"Yes","has_output":"No","acceptance_criteria":"No","dependencies":"T002","ai_metric":"F1 score","risk_level":"High","timeline":"2024-07-31","stakeholder_impact":"High"},
        ],
    )


def load_stakeholders():
    return _load_csv(
        "stakeholder_map.csv",
        [
            {"project_id":"P001","stakeholder_name":"Alice Chen","role":"Researcher","responsible":"Yes","accountable":"No","consulted":"No","informed":"No"},
            {"project_id":"P001","stakeholder_name":"Bob Smith","role":"Engineer","responsible":"No","accountable":"Yes","consulted":"Yes","informed":"No"},
            {"project_id":"P001","stakeholder_name":"Carol White","role":"Product Manager","responsible":"No","accountable":"No","consulted":"Yes","informed":"Yes"},
        ],
    )


def load_experiments():
    return _load_csv(
        "experiment_tracker.csv",
        [
            {"experiment_id":"EXP001","project_id":"P002","track":"Intent Detection","experiment_name":"Intent Classifier v1","hypothesis":"Debug intent > 70% accuracy","baseline_metric":"55%","target_metric":"70%","actual_metric":"68%","dataset_size":"5000 samples","status":"Completed","start_date":"2024-03-01","end_date":"2024-04-15"},
            {"experiment_id":"EXP002","project_id":"P002","track":"Intent Detection","experiment_name":"Intent Classifier v2","hypothesis":"Debug intent with context > 75%","baseline_metric":"68%","target_metric":"75%","actual_metric":"76%","dataset_size":"8000 samples","status":"Completed","start_date":"2024-04-20","end_date":"2024-05-30"},
            {"experiment_id":"EXP003","project_id":"P001","track":"Suggestion Quality","experiment_name":"Suggestion Ranking v1","hypothesis":"Useful suggestions > 50%","baseline_metric":"40%","target_metric":"50%","actual_metric":"48%","dataset_size":"2000 interactions","status":"Running","start_date":"2024-05-01","end_date":""},
        ],
    )
