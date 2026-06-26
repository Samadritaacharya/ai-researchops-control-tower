import streamlit as st
from utils.data_loader import load_risks
from utils.scoring import calculate_risk_score, classify_risk
from utils.visualization import risk_heatmap
from utils.ui import inject_brand_css

st.set_page_config(page_title='AI/ML Risk Register', page_icon='🔬', layout='wide')
inject_brand_css()
st.title('3. AI/ML Risk Register')
risks = load_risks()
risks['risk_score'] = risks.apply(lambda r: calculate_risk_score(r.impact, r.likelihood), axis=1)
risks['risk_level'] = risks['risk_score'].apply(classify_risk)
st.plotly_chart(risk_heatmap(risks), use_container_width=True)
st.dataframe(risks, use_container_width=True)
with st.form('risk_form'):
    st.text_input('Risk title')
    st.selectbox('Category', ['Data Risks', 'Model Risks', 'Deployment Risks', 'Organizational Risks'])
    st.slider('Impact', 1, 5, 3)
    st.slider('Likelihood', 1, 5, 3)
    st.text_area('Mitigation plan')
    st.form_submit_button('Save draft risk')
