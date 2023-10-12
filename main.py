import streamlit as st
from functions import *
import pyperclip

st.title("PDF Data Extractor")

# File upload widget
uploaded_file = st.file_uploader("Choose a file", type=["pdf"])
submitted = st.button("Submit")

if submitted:
    if uploaded_file is not None:
        a = extractinfo(uploaded_file)
        b =final(a)
        st.write(b)
        if st.button("Copy to Clipboard"):
            pyperclip.copy()
            st.write("Text copied to clipboard!")