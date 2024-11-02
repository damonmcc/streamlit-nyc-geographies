import streamlit as st

from utils.dev import show_code

PAGE_HEADER = "Operate Page"
PAGE_ICON = "⚗️"


def _operation():
    print("starting an operation")
    # export nyc city borders
    # fetch_geometries(GEOEGRAPHIES.values())
    # all_ny_borders = GEOEGRAPHIES["city"].geometries
    # st.info(all_ny_borders.columns)
    # nyc_only = all_ny_borders[all_ny_borders["NAME"] == "New York"]
    # st.info(nyc_only)
    # # nyc_only.to_json("nyc_boundaries.json")
    # nyc_only.to_file("nyc_boundaries.geojson", driver="GeoJSON")


def run_page():
    st.markdown(f"# {PAGE_HEADER}")

    def form_callback():
        # st.write(st.session_state.my_slider)
        # st.write(st.session_state.my_checkbox)
        _operation()

    with st.form(key="my_form"):
        slider_input = st.slider("My slider", 0, 10, 5, key="my_slider")
        checkbox_input = st.checkbox("Yes or No", key="my_checkbox")
        submit_button = st.form_submit_button(
            label="Perform an operation", on_click=form_callback
        )
    # st.button("Resety")
    # if st.button('Say hello', type="primary"):
    #     st.write('Why hello there')
    # else:
    #     st.write('Goodbye')


if __name__ == "__main__":
    st.set_page_config(page_title=PAGE_HEADER, page_icon=PAGE_ICON)
    st.sidebar.header("Settings")

    show_code(run_page, "run_page")
    show_code(_operation, "_operation")

    run_page()
