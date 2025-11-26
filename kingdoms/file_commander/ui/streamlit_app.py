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
    """Level 2:
    Because we want to tell the app which folder to work with, this version
    adds a text box where we can type a directory path and then shows
    the path back to us.
    """

    st.set_page_config(
        page_title= "File Commander - Level 2",
        layout = "wide"
    )

    st.title("📁 File Commander — Level 2")
    st.write("Type a directory path below and we will echo it back.")

    #1 Take input from user.
    directory_text = st.text_input(
        label= "Directory to use",
        help="Enter a folder path, for example: /Users/yourname/Documents"
    )

    #2 Show what the user typed.
    st.write("You entered:", directory_text)

if __name__ == "__main__":
    main()
