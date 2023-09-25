import inspect
import textwrap

import streamlit as st


def show_code(code: object, code_name: str):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox(f"Show {code_name} code", False)
    if show_code:
        st.markdown(f"## {code_name}")
        sourcelines, _ = inspect.getsourcelines(code)
        st.code(textwrap.dedent("".join(sourcelines[1:])))
