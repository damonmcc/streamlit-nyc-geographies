import streamlit as st

PAGE_HEADER = "Explore Page"


def run_explore():
    st.warning("Please write some code.")


st.set_page_config(page_title=PAGE_HEADER, page_icon="🌐")
st.markdown(f"# {PAGE_HEADER}")
st.sidebar.header(PAGE_HEADER)

run_explore()
