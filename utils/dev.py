import inspect
import textwrap
from typing import Callable

import streamlit as st


def show_code(code: Callable, code_name: str):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox(f"Show {code_name} code", False)
    if show_code:
        st.markdown(f"## {code_name}")
        sourcelines, _ = inspect.getsourcelines(code)
        st.code(textwrap.dedent("".join(sourcelines[1:])))
