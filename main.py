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

# Upload File PDF
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# Translate button
translate_button = st.button("Start translation", type="primary")

# Show results
result_container = st.container()

if translate_button and uploaded_file is not None:
    with st.spinner("Processing file PDF..."):
        # Reading content PDF
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        # Show summary of main content
        with result_container:
            st.subheader("Main contents PDF:")
            st.text_area("Original text", text, height=200, disabled=True)
            
            st.subheader(f"Translation into language {target_language}:")
            
            # Simulate translation with DeepSeek (in practice, the real API must be used)
            with st.spinner(f"Translating to {target_language}..."):
                # This section should be replaced with the actual DeepSeek API                
                # Example of a mock translation for demonstration
                translated_text = f"[This text will be translated into {target_language}]\n\n{text[:500]}..."
                
                st.text_area("Translated text", translated_text, height=400)
                
                # Download translation button
                st.download_button(
                    label="Download translation as TXT",
                    data=translated_text,
                    file_name=f"translated_{uploaded_file.name.split('.')[0]}_{target_language}.txt",
                    mime="text/plain"
                )
                
                st.success("Translation completed successfully.!")
elif translate_button and uploaded_file is None:
                st.warning("Please upload a PDF file first.")

# App Guide
with st.expander("User Guide"):
    st.markdown("""
**How ​​to use PDF Translator:**

1. Upload your PDF file using the upload button at the top.
2. Select the target language from the side menu.
3. Specify the translation quality level.
4. Click the "Start Translation" button.
5. After processing is complete, the translation will be displayed.
6. You can download the translation as a text file.

**Note:**
- This app uses DeepSeek AI for translation.
- The translation quality depends on the complexity of the text and the target language.
- For large files, translation may take several minutes.
""")

# Footnote
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
<p>Built with Streamlit and DeepSeek AI | Version 1.0</p>
</div>
""", unsafe_allow_html=True)