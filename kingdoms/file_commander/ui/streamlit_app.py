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
        with st.spinner(f"Scanning {target_directory}..."):
            file_catalog = build_file_catalog(target_directory)


        st.success(f"Scan complete. Found {len(file_catalog)} files.")
        #Sidebar filters.
        st.sidebar.header("Filters")

        unique_file_types = sorted(file_catalog["file_type"].unique())
        selected_file_types = st.sidebar.multiselect(
            label = "File types",
            options = unique_file_types,
            default= unique_file_types,
        )

        minimum_size_mb = st.sidebar.number_input(
            label= "Minimum size (MB)",
            min_value= 0.0,
            value= 0.0,
            step = 1.0,
            help = "Only show files at or above this size."
        )

        # Apply filters
        filtered_catalog = file_catalog.copy()

        if selected_file_types:
            filtered_catalog = filtered_catalog[
                filtered_catalog["file_type"].isin(selected_file_types)
            ]

        if minimum_size_mb > 0:
            minimum_size_mb = minimum_size_mb *1024 * 1024
            filtered_catalog = filtered_catalog.sort_values(
                "modified_at", ascending=False
            )

        st.subheader("File catalog (filtered)")
        st.caption("Sorted by modified_at (newest first).")
        st.dataframe(filtered_catalog, width="stretch")

        # if not target_directory:
        #     st.error("Please enter a directory path.")
        #     return
        # if not target_directory.exists():
        #     st.error(f"Path does not exist: {target_directory}")
        #     return
        # if not target_directory.is_dir():
        #     st.error(f"Path is not a directory: {target_directory}")

        # #3 Valid path -> build the catalog.
        # with st.spinner(f"Scanning {target_directory}..."):
        #     file_catalog = build_file_catalog(target_directory)

        # st.success(f"Scan complete. Found {len(file_catalog)} files.")

        # #4. Show a small preview of the table.
        # st.subheader("File catalog preview.")
        # st.dataframe(file_catalog.head(20), width='stretch')

if __name__ == "__main__":
    main()
