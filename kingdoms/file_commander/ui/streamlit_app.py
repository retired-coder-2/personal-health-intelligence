"""
Because we want a visual way to explore our file catalog without writing
Python code each time, this Streamlit app lets us choose a directory,
build the catalog, and interactively filter and sort the results.
"""

from __future__ import annotations
from pathlib import Path
import streamlit as st
from src.scanner import build_file_catalog


def main() -> None:
    """Because we want a simple, interactive front-end for our file catalog,
    this function defines the layout and behavior of the Streamlit page.
    """

    #Basic page configuration title and layout
    st.set_page_config(
        page_title= "File Commander - Catalog Explorer",
        layout = "wide"
    )

    st.title("📁 File Commander — Catalog Explorer")
    st.write("This is the simplest possible version of our app.")

    # st.markdown(
    #     """ Use this tool to scan a directory, classify its files by type,
    #     and explore them in a table you can filter and sort."""
    # )

    # #Default directory is the user's Downloads folder, but the user can change it.

    # default_directory = Path.home() / "Downloads"

if __name__ == "__main__":
    main()
