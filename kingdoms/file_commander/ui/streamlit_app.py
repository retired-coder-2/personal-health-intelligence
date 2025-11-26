"""
Because we want a visual way to explore our file catalog without writing
Python code each time, this Streamlit app lets us choose a directory,
build the catalog, and interactively filter and sort the results.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd
import streamlit as st

from src.scanner import build_file_catalog




def main() -> None:
    """
    Level 4:
    Because we want to see a real table of files and plan future file actions,
    this version lets us:
      - Choose a directory to scan
      - Choose a destination directory for future actions
      - Scan and build a file catalog (stored in session state)
      - Filter the catalog by file_type, size, and "stale days"
    """

    # -------------------------------------------------------------------------
    # 0. Page setup
    # -------------------------------------------------------------------------
    st.set_page_config(
        page_title="File Commander - Level 5",
        layout="wide",
    )

    st.title("📁 File Commander — Level 4")
    st.write(
        "Type a directory path, click 'Scan directory', "
        "and we will show a table of files."
    )

    # -------------------------------------------------------------------------
    # 1a. Directory to scan
    # -------------------------------------------------------------------------
    directory_text = st.text_input(
        label="Directory to scan",
        help="Enter a folder path, for example: /Users/yourname/Documents",
    )

    target_directory: Optional[Path] = None
    if directory_text:
        target_directory = Path(directory_text).expanduser()

    # -------------------------------------------------------------------------
    # 1b. Destination directory for future actions
    # -------------------------------------------------------------------------
    destination_text = st.text_input(
        label="Destination directory for actions (future)",
        help=(
            "Enter a folder path where files could be moved, e.g."
            " /Users/yourname/Desktop/archive"
        ),
    )

    destination_directory: Optional[Path] = None
    if destination_text:
        destination_directory = Path(destination_text).expanduser()

    if destination_directory is not None:
        st.info(f"Planned destination directory: {destination_directory}")

    # -------------------------------------------------------------------------
    # 2. Scan button: on click, build catalog and store it in session_state
    # -------------------------------------------------------------------------
    if st.button("🔍 Scan directory"):
        if target_directory is None:
            st.error("Please enter a directory path.")
            return

        if not target_directory.exists():
            st.error(f"Path does not exist {target_directory}")
            return

        if not target_directory.is_dir():
            st.error(f"Path is not a directory: {target_directory}")
            return

        with st.spinner(f"Scanning {target_directory}..."):
            file_catalog = build_file_catalog(target_directory)

        # Store in session so we can reuse it across reruns
        st.session_state["file_catalog"] = file_catalog

        st.success(f"Scan complete. Found {len(file_catalog)} files.")

    # -------------------------------------------------------------------------
    # 3. If we have a catalog in session_state, show filters + table
    #    This block runs on every rerun, so sidebar changes update the table.
    # -------------------------------------------------------------------------
    file_catalog = st.session_state.get("file_catalog")

    if file_catalog is not None and not file_catalog.empty:
        st.sidebar.header("Filters")

        # File type filter
        unique_file_types = sorted(file_catalog["file_type"].unique())
        selected_file_types = st.sidebar.multiselect(
            label="File types",
            options=unique_file_types,
            default=unique_file_types,
        )

        # Size filter
        minimum_size_mb = st.sidebar.number_input(
            label="Minimum size (MB)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            help="Only show files at or above this size.",
        )

        # Stale filter
        stale_days = st.sidebar.number_input(
            label="Stale if not accessed in (days)",
            min_value=0,
            value=0,
            step=30,
            help=(
                "Set this to a positive number to show only files that have "
                "not been accessed for at least this many days."
            ),
        )

        # ---------------------------------------------------------------------
        # Apply filters
        # ---------------------------------------------------------------------
        filtered_catalog = file_catalog.copy()

        # 1️⃣ Filter by file_type
        if selected_file_types:
            filtered_catalog = filtered_catalog[
                filtered_catalog["file_type"].isin(selected_file_types)
            ]

        # 2️⃣ Filter by minimum size
        if minimum_size_mb > 0:
            minimum_size_bytes = minimum_size_mb * 1024 * 1024
            filtered_catalog = filtered_catalog[
                filtered_catalog["size_bytes"] >= minimum_size_bytes
            ]

        # 3️⃣ Filter by "stale" last accessed
        if stale_days > 0:
            cutoff_timestamp = pd.Timestamp.now() - pd.Timedelta(days=stale_days)
            filtered_catalog = filtered_catalog[
                filtered_catalog["last_accessed_at"] < cutoff_timestamp
            ]

        # 4️⃣ Sort by modified_at (newest first)
        if not filtered_catalog.empty:
            filtered_catalog = filtered_catalog.sort_values(
                "modified_at", ascending=False
            )

        # ---------------------------------------------------------------------
        # 4. Display table
        # ---------------------------------------------------------------------
        st.subheader("File catalog (filtered)")
        st.caption("Sorted by modified_at (newest first).")
        st.dataframe(filtered_catalog, width="stretch")
    else:
        st.info("Scan a directory to see the file catalog.")

if __name__ == "__main__":
    main()
