import streamlit as st

from utils.dev import show_code

PAGE_HEADER = "Explore Page"
PAGE_ICON = "🌐"


def run_explore():
    st.markdown(f"# {PAGE_HEADER}")
    st.markdown(
        """
        This page is for exploring the various NYC Geogrpahies.
    """
    )
    st.warning("Please write some code.")


if __name__ == "__main__":
    st.set_page_config(page_title=PAGE_HEADER, page_icon=PAGE_ICON)
    st.sidebar.header("Settings")
    
    # # DEBUG
    # st.sidebar.warning(f"{_repo_root=}")
    show_code(run_explore)

    run_explore()

