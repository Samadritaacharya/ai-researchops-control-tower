import plotly.express as px
import plotly.graph_objects as go

PRIMARY = '#0B5B73'
SECONDARY = '#1F3347'
SUCCESS = '#2ECC71'
WARNING = '#F39C12'
DANGER = '#E74C3C'


def project_status_pie(projects):
    return px.pie(projects, names='status', title='Project Status Distribution', hole=0.35)


def uncertainty_distribution(projects):
    df = projects.copy()
    if 'uncertainty_score' not in df.columns:
        df['uncertainty_score'] = df[['goal_volatility', 'data_uncertainty', 'model_uncertainty', 'stakeholder_dependency', 'legal_complexity']].mean(axis=1)
    return px.bar(df, x='project_name', y='uncertainty_score', color='status', title='Uncertainty Score by Project')


def uncertainty_matrix(projects):
    return px.scatter(projects, x='goal_volatility', y='data_uncertainty', size='stakeholder_dependency', color='status', hover_name='project_name', title='Goal Volatility vs Data Uncertainty')


def risk_heatmap(risks):
    df = risks.copy()
    if 'risk_score' not in df.columns:
        df['risk_score'] = df['impact'] * df['likelihood']
    fig = px.scatter(df, x='likelihood', y='impact', size='risk_score', color='risk_score', hover_name='title', title='Risk Heatmap: Impact x Likelihood', range_x=[0.5, 5.5], range_y=[0.5, 5.5])
    fig.update_layout(xaxis_title='Likelihood', yaxis_title='Impact')
    return fig


def task_completeness_chart(tasks):
    return px.bar(tasks, x='task_name', y='completeness', color='status', title='Task Completeness')


def experiment_results_chart(experiments):
    df = experiments.copy()
    for col in ['baseline_metric', 'target_metric', 'actual_metric']:
        df[col + '_value'] = df[col].astype(str).str.rstrip('%').astype(float)
    fig = go.Figure()
    fig.add_bar(x=df['experiment_name'], y=df['baseline_metric_value'], name='Baseline')
    fig.add_bar(x=df['experiment_name'], y=df['target_metric_value'], name='Target')
    fig.add_bar(x=df['experiment_name'], y=df['actual_metric_value'], name='Actual')
    fig.update_layout(title='Experiment Metrics', barmode='group', yaxis_title='Metric (%)')
    return fig
