import streamlit as st
from utils.data_loader import load_project_data
from utils.ui import inject_brand_css, disclaimer

st.set_page_config(page_title='Project Intake', page_icon='🔬', layout='wide')
inject_brand_css()
st.title('1. Research Project Intake')
disclaimer()
projects = load_project_data()
with st.form('project_intake'):
    name = st.text_input('Project name')
    goal = st.text_area('Research goal')
    owner = st.text_input('Primary researcher')
    stakeholders = st.text_area('Key stakeholders')
    submitted = st.form_submit_button('Generate draft charter')
if submitted:
    st.subheader('Draft Research Charter')
    st.markdown(f'**Project:** {name}\n\n**Research goal:** {goal}\n\n**Primary researcher:** {owner}\n\n**Stakeholders:** {stakeholders}')
st.subheader('Existing sample projects')
st.dataframe(projects, use_container_width=True)
