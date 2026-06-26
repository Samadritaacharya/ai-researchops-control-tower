import streamlit as st
from utils.data_loader import load_tasks
from utils.scoring import calculate_task_completeness
from utils.visualization import task_completeness_chart
from utils.ui import inject_brand_css

st.set_page_config(page_title='Task Completeness', page_icon='🔬', layout='wide')
inject_brand_css()
st.title('4. Task Completeness Analyzer')
tasks = load_tasks()
tasks['completeness'] = tasks.apply(lambda r: calculate_task_completeness(r.to_dict()), axis=1)
st.metric('Average task completeness', f"{tasks.completeness.mean():.0f}%")
st.plotly_chart(task_completeness_chart(tasks), use_container_width=True)
st.dataframe(tasks, use_container_width=True)
st.info('A task is considered ready when objective, owner, output, acceptance criteria, dependencies, AI metric, risk level, timeline, and stakeholder impact are all defined.')
