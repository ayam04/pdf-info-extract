import streamlit as st
import PyPDF2
# Set the title and description of your app
st.title("PDf Data extractor")
extracted_text = ''
# File upload widget
uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

if uploaded_file is not None:
    pdf_file=open(uploaded_file,'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        extracted_text += page.extractText()
    pdf_file.close()
    st.write(extracted_text)

