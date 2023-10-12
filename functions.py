import streamlit as st
import PyPDF2
from io import BytesIO
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pyperclip

def extractinfo(uploaded_file):
    file = BytesIO(uploaded_file.read())
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words]
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    final_text = " ".join(words)
    return final_text