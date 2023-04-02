import time

import streamlit as st

from medium_processor import get_medium_text
from models.summarize import TextSummarizer

st.set_page_config(page_title='Medium Post Summarizer', layout='wide', initial_sidebar_state='auto')

# Setting Title
st.title("Medium Post Summarizer")
url = st.text_input("Enter the URL: ")
if url:
    st.markdown("\nPost URL: {}".format(url))

    # Fetching Text
    fetch_state = st.text(f"Fetching Medium Post...")
    start = time.time()
    text = get_medium_text(url)
    fetch_state.text("Fetched Medium Post in {:.2f}s...".format(time.time() - start))

    # Summarizing
    summarizer_state = st.text("Summarizing Post...")
    start = time.time()
    summarizer = TextSummarizer()
    summarized_text = summarizer.summarize(text)
    summarizer_state.text("Post Summarization Done in {:.2f}s...".format(time.time() - start))
    st.write(summarized_text)
