import streamlit as st
import epitran
import re

epi = epitran.Epitran('eng-Latn')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def text_to_ipa(text):
    if not text.strip():
        return None, False, "Empty input text"
    try:
        cleaned = clean_text(text)
        words = cleaned.split()
        ipa_words = []
        for w in words:
            ipa_word = epi.transliterate(w)
            ipa_words.append(ipa_word)
        ipa = ' '.join(ipa_words)
        return f"/{ipa}/", True, None
    except Exception as e:
        st.error(f"IPA conversion error: {e} (repr: {repr(e)})")
        return None, False, f"IPA conversion error: {str(e)}"

st.title("IPA Conversion Test App")

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
