import streamlit as st
import pandas as pd
from utils.data_loader import load_project_data
from utils.scoring import calculate_handover_readiness
from utils.ui import inject_brand_css

st.set_page_config(page_title='Status and Communication', page_icon='🔬', layout='wide')
inject_brand_css()
st.title('7. Status and Communication Generator')
projects = load_project_data()
choice = st.selectbox('Project', projects.project_name)
readiness = calculate_handover_readiness(8, 7, 8, 6, 7)
st.metric('Product handover readiness', f'{readiness:.0f}%')
st.subheader('Weekly status draft')
message = f'Project: {choice}\nSummary: Research work is progressing across tasks, risks, and experiments.\nNext steps: Confirm owners, acceptance criteria, and handover readiness actions.'
st.text_area('Generated update', message, height=180)
st.subheader('Decision log')
st.dataframe(pd.DataFrame([{'Decision ID':'D001','Decision':'Use F1 score for intent classifier','Rationale':'Balances precision and recall','Status':'Open'}]), use_container_width=True)
