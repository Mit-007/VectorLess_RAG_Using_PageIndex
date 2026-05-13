import streamlit as st
from api_client import send_query, upload_file
from components.query_box import render_query_box
from components.file_upload import render_file_upload

st.set_page_config(page_title="RAG App", layout="wide")

st.title("📚 RAG Q&A System")

with st.sidebar.header("Upload Document"):
    uploaded_file = render_file_upload()

    if uploaded_file:
        if st.sidebar.button("Upload File"):
            with st.spinner("Uploading and processing..."):
                response = upload_file(uploaded_file)
                st.sidebar.success(response.get("doc_id","doc_id"))

st.header("Ask a Question")

query = render_query_box()

if st.button("Get Answer"):
    if query.strip() == "":
        st.warning("Please enter a query")
    else:
        with st.spinner("Thinking..."):
            response = send_query(query)
            answer = response.get("answer",response["message"])
            st.subheader("Answer:")
            st.write(answer)


# response["message"]["content"])
# response["message"]["content"][0]["text"](gemini 3 flash lite)