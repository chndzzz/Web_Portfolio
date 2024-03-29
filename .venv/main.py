import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("../images/photo.png",width = 600)

with col2:
    st.title("Chandrakant Panjal")
    content = """
    Hi I am Chandrakant! I am a python developer, data scientist and data analyst.
    I graduated from SNPIT in 2016 and worked for Yantram Medtech Pvt Ltd."""
    st.info(content)