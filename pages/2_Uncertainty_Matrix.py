import streamlit as st
from utils.data_loader import load_project_data
from utils.scoring import calculate_uncertainty_score
from utils.visualization import uncertainty_matrix
from utils.ui import inject_brand_css

st.set_page_config(page_title='Uncertainty Matrix', page_icon='🔬', layout='wide')
inject_brand_css()
st.title('2. Uncertainty & Scope Matrix')
projects = load_project_data()
projects['uncertainty_score'] = projects.apply(lambda r: calculate_uncertainty_score(r.goal_volatility, r.data_uncertainty, r.model_uncertainty, r.stakeholder_dependency, r.legal_complexity), axis=1)
st.plotly_chart(uncertainty_matrix(projects), use_container_width=True)
st.dataframe(projects[['project_id','project_name','uncertainty_score','goal_volatility','data_uncertainty','model_uncertainty','stakeholder_dependency','legal_complexity']], use_container_width=True)
st.info('High-uncertainty research projects need shorter review cycles, stronger decision logs, and explicit risk owners.')
