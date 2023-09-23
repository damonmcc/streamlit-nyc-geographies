import streamlit as st

from utils.dev import show_code
from utils.mapping import show_demo_map

PAGE_HEADER = "Explore Page"
PAGE_ICON = "🌐"


def run_explore():
    st.markdown(f"# {PAGE_HEADER}")
    st.markdown(
        """
        This page is for exploring the various NYC geogrpahic boundaries using a map.
        """
    )
    show_demo_map()
    # demo_map.to_streamlit(width=700, height=500, add_layer_control=True)
    st.warning("Please write some code.")


if __name__ == "__main__":
    st.set_page_config(page_title=PAGE_HEADER, page_icon=PAGE_ICON)
    st.sidebar.header("Settings")

    show_code(run_explore)

    run_explore()
