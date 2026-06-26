import streamlit as st
from utils.data_loader import load_experiments
from utils.visualization import experiment_results_chart
from utils.ui import inject_brand_css

st.set_page_config(page_title='Experiment Tracker', page_icon='🔬', layout='wide')
inject_brand_css()
st.title('6. Experiment Tracker')
experiments = load_experiments()
st.plotly_chart(experiment_results_chart(experiments), use_container_width=True)
st.dataframe(experiments, use_container_width=True)
st.metric('Completed experiments', int((experiments.status == 'Completed').sum()))
