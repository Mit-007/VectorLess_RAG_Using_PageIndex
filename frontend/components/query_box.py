import streamlit as st

def render_query_box():
    query = st.text_input("Enter Your Question",placeholder="Ask Somethings From Your Uploaded Documents")
    return query
