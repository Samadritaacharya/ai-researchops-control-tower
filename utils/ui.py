import streamlit as st
from utils.visualization import PRIMARY, SECONDARY


def inject_brand_css():
    st.markdown(
        f"""
        <style>
        h1, h2, h3 {{ color: {SECONDARY}; }}
        .stMetric {{ background: #F4F8F9; border-left: 5px solid {PRIMARY}; border-radius: 8px; padding: 12px 16px; }}
        .disclaimer {{ background: #FFF6E6; border: 1px solid #F39C12; border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def disclaimer():
    st.markdown(
        '<div class="disclaimer"><strong>Disclaimer:</strong> This is an independent portfolio project inspired by public software-engineering research themes. It is not affiliated with JetBrains or any other organization.</div>',
        unsafe_allow_html=True,
    )
