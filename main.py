import streamlit as st

# Set the title and description of your app
st.title("PDf Data extractor")

# File upload widget
uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

