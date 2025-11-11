import streamlit as st
import epitran
import re

# Initialize epitran once
epi = epitran.Epitran('eng-Latn')

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove anything except letters and spaces
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def text_to_ipa(text):
    if not text.strip():
        return None, False, "Empty input text"
    try:
        cleaned = clean_text(text)
        ipa = epi.transliterate(cleaned)
        return f"/{ipa}/", True, None
    except Exception as e:
        st.error(f"IPA conversion error: {e} (repr: {repr(e)})")
        return None, False, f"IPA conversion error: {str(e)}"

st.title("IPA Conversion Test App")

st.write("This app converts English text to IPA using epitran.")

test_inputs = [
    "hello",
    "this is a test",
    "",
    "1234",
    "How are you?"
]

st.header("Test Results")

for text in test_inputs:
    ipa, success, error = text_to_ipa(text)
    if success:
        st.write(f"Input: '{text}' → IPA: {ipa}")
    else:
        st.write(f"Input: '{text}' → Error: {error}")
