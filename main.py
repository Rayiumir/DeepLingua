import streamlit as st

# Page Setting
st.set_page_config(
    page_title="PDF Translator with DeepSeek",
    page_icon="🌐",
    layout="wide"
)

# Program title

st.title("🌐 PDF Translator with DeepSeek AI")
st.markdown(
    """
        This program allows you to translate PDF files into different languages. 
        Upload your PDF file, select the target language, and get the translation.
    """
)