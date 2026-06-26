import streamlit as st
from utils.data_loader import load_stakeholders
from utils.ui import inject_brand_css

st.set_page_config(page_title='Stakeholder RACI', page_icon='🔬', layout='wide')
inject_brand_css()
st.title('5. Stakeholder Map & RACI')
stakeholders = load_stakeholders()
st.dataframe(stakeholders, use_container_width=True)
st.subheader('Communication recommendations')
st.markdown('- Researchers and engineers: weekly sync\n- Product and legal: milestone reviews\n- Academic partners: structured consultation points\n- Executive sponsors: monthly summary updates')
