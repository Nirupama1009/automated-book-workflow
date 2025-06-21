import streamlit as st
from transformers import pipeline
import pdfplumber

# Load QA model
qa_pipeline = pipeline("question-answering")

st.title("📚 Chapter QA Chatbot")
st.write("Upload a chapter (PDF or text), ask questions, and get answers!")

# File uploader
uploaded_file = st.file_uploader("Upload your chapter (PDF)", type=["pdf"])
chapter_text = ""

# Extract text from PDF
if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            chapter_text += page.extract_text()

# Input question
question = st.text_input("Ask a question about the chapter:")

# Get and display answer
if st.button("Get Answer"):
    if chapter_text and question:
        result = qa_pipeline(question=question, context=chapter_text)
        st.success(result['answer'])
    else:
        st.error("Please upload a chapter and ask a question.")

