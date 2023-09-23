import streamlit as st

PAGE_HEADER = "Explore Page"
PAGE_ICON = "🌐"


def run_explore():
    st.warning("Please write some code.")


st.set_page_config(page_title=PAGE_HEADER, page_icon=PAGE_ICON)
st.markdown(f"# {PAGE_HEADER}")
st.sidebar.header(PAGE_HEADER)

run_explore()
