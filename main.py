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

# Sidebar for settings
with st.sidebar:
    st.header("Translation settings")
    target_language = st.selectbox(
        "Select target language:",
        ["English", "Persian", "Arabic", "French", "German", "Spanish", "Chinese", "Japanese", "Korean", "Russian"],
        index=1
    )
    
    quality_setting = st.radio(
        "Quality of translation:",
        ["Fast (general translation)", "Medium (more precise translation)", "Advanced (translation with structure preservation)"],
        index=1
    )
    
    st.markdown("---")
    st.markdown("**Note:** Translating large files may take time.")