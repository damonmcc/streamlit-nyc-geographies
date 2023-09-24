import streamlit as st

from utils.dev import show_code
from utils.mapping import show_basic_map
from utils.geography import GEOEGRAPHIES

PAGE_HEADER = "Validate Page"
PAGE_ICON = "⚗️"


def run_page():
    st.markdown(f"# {PAGE_HEADER}")
    st.markdown(
        """
        This page is for exploring the validating the relationshi NYC geogrpahic boundaries using a map.
        """
    )
    for geography in GEOEGRAPHIES:
        # st.markdown(f"## {geography.name=}, ({geography.code=})")

        # st.dataframe(
        #     geography.geometries
        #     # geography.geometries.style.applymap(
        #     #     dataframe_style_source_report_results,
        #     #     subset=["same_columns", "same_row_count"],
        #     # )
        # )
        with st.expander(f"{geography.name}"):
            # with st.spinner(f"⏳ Loading {geography.name} ..."):
            #     status_messages = load_source_data_to_compare(
            #         dataset=dataset, source_data_versions=source_data_versions
            #     )
            # success_message = "\n\n".join(status_messages)
            # st.success(success_message)
            st.markdown(
                f"""
                {type(geography.geometries)}
                """
            )
            show_basic_map(geography.geometries, geography.name)
            # st.dataframe(geography.geometries)
            # st.table(geography.geometries)
            # st.json(source_report_results)

    # show_demo_map()
    # m = leafmap.Map()
    # m.to_streamlit()
    # st.warning("Please write some code.")


if __name__ == "__main__":
    st.set_page_config(page_title=PAGE_HEADER, page_icon=PAGE_ICON)
    st.sidebar.header("Settings")

    show_code(run_page)

    run_page()
