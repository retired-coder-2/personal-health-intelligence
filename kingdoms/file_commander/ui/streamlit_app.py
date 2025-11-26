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
    """
    Level 3:
    Because we want to see a real table of files, this version lets us type
    a directory path, click a button to scan it, and then shows a preview
    of the file catalog built by `build_file_catalog`.
    """

    st.set_page_config(
        page_title= "File Commander - Level 3",
        layout = "wide"
    )

    st.title("📁 File Commander — Level 3")
    st.write(
        "Type a directory path click 'Scan directory' ,"
        "and we will show a table of files"
    )

    #1 Take input from user.
    directory_text = st.text_input(
        label= "Directory to scan",
        help="Enter a folder path, for example: /Users/yourname/Documents"
    )

    # Convert the string to a Path (now we can use .exists(), .is_dir(), etc.).
    target_directory = Path(directory_text).expanduser() if directory_text else None

    #2 Only do the scan when the button is pressed.
    if st.button("🔍 Scan directory"):
        if not target_directory:
            st.error("Please enter a directory path.")
            return
        if not target_directory.exists():
            st.error(f"Path does not exist: {target_directory}")
            return
        if not target_directory.is_dir():
            st.error(f"Path is not a directory: {target_directory}")

        #3 Valid path -> build the catalog.
        with st.spinner(f"Scanning {target_directory}..."):
            file_catalog = build_file_catalog(target_directory)

        st.success(f"Scan complete. Found {len(file_catalog)} files.")

        #4. Show a small preview of the table.
        st.subheader("File catalog preview.")
        st.dataframe(file_catalog.head(20), width='stretch')

if __name__ == "__main__":
    main()
