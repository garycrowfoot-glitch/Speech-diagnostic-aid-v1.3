import streamlit as st
import epitran

# Initialize epitran once
epi = epitran.Epitran('eng-Latn')

def text_to_ipa(text):
    if not text.strip():
        return None, False, "Empty input text"
    try:
        ipa = epi.transliterate(text)
        return f"/{ipa}/", True, None
    except Exception as e:
        st.error(f"IPA conversion error: {e} (repr: {repr(e)})")
        return None, False, f"IPA conversion error: {str(e)}"

st.title("IPA Conversion Test App")

st.write("This app converts English text to IPA using epitran.")

# Test inputs to demonstrate functionality
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
