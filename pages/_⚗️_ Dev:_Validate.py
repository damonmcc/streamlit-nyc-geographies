import streamlit as st

from utils.dev import show_code
from utils.mapping import create_basic_map, show_map
from utils.geography import (
    GEOGRAPHY_DETAILS,
    construct_all_geographies,
    fetch_geometries,
)

PAGE_HEADER = "Validate Page"
PAGE_ICON = "⚗️"


def run_page():
    st.markdown(f"# {PAGE_HEADER}")
    st.markdown(
        """
        This page is for validating the attributes and relationships of NYC geographic boundaries.
        """
    )
    with st.expander("View GEOGRAPHY_DETAILS"):
        st.dataframe(GEOGRAPHY_DETAILS)

    with st.spinner(f"⏳ Loading each geography's geometries ..."):
        geographies = construct_all_geographies()
        fetch_geometries(geographies)
    st.success("Loaded each geography's geometries")

    basic_map = create_basic_map()
    for geography in geographies.values():
        st.markdown(f"##### {geography.name}")
        st.markdown(
            f"""
            - projection: {geography.geometries.crs}
            - total area (sq mi): {round((geography.geometries.area.sum() * 3.587006427e-8), 4):,}
            """
        )
        # TODO vary line weight/color by layer
        basic_map.add_gdf(geography.geometries, layer_name=geography.name)

    with st.expander(f"View map of all geographies"):
        with st.spinner(f"⏳ Building map of all geographies ..."):
            show_map(basic_map)

    # TODO compare some geographies
    st.warning("Write some code.")


if __name__ == "__main__":
    st.set_page_config(page_title=PAGE_HEADER, page_icon=PAGE_ICON)
    st.sidebar.header("Settings")

    show_code(run_page, "run_page")

    run_page()
