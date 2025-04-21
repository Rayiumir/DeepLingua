import streamlit as st
import PyPDF2
from huggingface_hub import InferenceClient
import time

# Add Huggingface API Key
Huggingface_API_KEY = "API_KEY"

# Models
MODEL = "meta-llama/Llama-4-Scout-17B-16E-Instruct" #Changing Huggingface models

client = InferenceClient(
    model=MODEL,
    api_key=Huggingface_API_KEY,
)

# User interface
st.set_page_config(page_title="PDF Translator with Huggingface", layout="centered")
st.image("img/huggingface_logo-noborder.svg")
st.title("PDF Translator using Huggingface")

languages = {
    "Persian": "Persian",
    "French": "French",
    "Spanish": "Spanish",
    "German": "German",
    "Arabic": "Arabic",
    "Turkish": "Turkish"
}

pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
target_lang = st.selectbox("Translate to", list(languages.keys()))

# Text splitting function
def split_text(text, max_chars=1000):
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]

# Translate Chunk
def translate_chunk(chunk, target_language):
    system_prompt = f"You are a professional translator. Translate the following English text to {target_language}."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": chunk},
    ]

    try:
        response = client.chat_completion(messages, max_tokens=1000)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error translating chunk: {e}]"

# Processing PDF
if pdf_file and st.button("Translate PDF"):
    with st.spinner("Reading PDF..."):
        reader = PyPDF2.PdfReader(pdf_file)
        full_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    chunks = split_text(full_text, max_chars=1000)
    translated_chunks = []

    progress = st.progress(0)
    for i, chunk in enumerate(chunks):
        translated = translate_chunk(chunk, languages[target_lang])
        translated_chunks.append(translated)
        time.sleep(1)
        progress.progress((i + 1) / len(chunks))

    final_translation = "\n\n".join(translated_chunks)
    st.success("Translation complete!")
    st.text_area("Translated Text", final_translation, height=400)
    st.download_button("Download Translation", final_translation, file_name="translated.txt")
