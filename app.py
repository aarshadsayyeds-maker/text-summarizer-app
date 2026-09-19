import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarizer", page_icon="📝")
st.title("📝 AI Text Summarizer")
st.write("Paste any article or text below to get a summary.")

text_input = st.text_area("Paste your text here", height=250)

col1, col2 = st.columns(2)
with col1:
    length = st.selectbox("Summary length", ["short", "medium", "long"])
with col2:
    style = st.selectbox("Style", ["simple", "formal", "bullet points"])

if st.button("Summarize", type="primary"):
    if not text_input.strip():
        st.warning("Please paste some text first.")
    elif len(text_input) < 50:
        st.warning("Text seems too short to summarize meaningfully.")
    else:
        with st.spinner("Summarizing..."):
            result = summarize_text(text_input, length, style)
        if result.startswith("Error:"):
            st.error(result)
        else:
            st.subheader("Summary")
            st.write(result)