import streamlit as st

def render_file_upload():
    uploaded_file = st.file_uploader("upload your file !",type=["pdf"])
    return uploaded_file