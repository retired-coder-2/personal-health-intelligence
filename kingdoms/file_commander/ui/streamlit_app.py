"""
Because we want a visual way to explore our file catalog without writing
Python code each time, this Streamlit app lets us choose a directory,
build the catalog, and interactively filter and sort the results.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional
import sys

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------
# Make sure the file_commander folder is on sys.path so we can import
# src.scanner no matter where Streamlit launches from.
#
# __file__ = .../kingdoms/file_commander/ui/streamlit_app.py
# parents[0] = ui
# parents[1] = file_commander   <-- we want this on sys.path
# ---------------------------------------------------------------------
FILE_COMMANDER_ROOT = Path(__file__).resolve().parents[1]
if str(FILE_COMMANDER_ROOT) not in sys.path:
    sys.path.insert(0, str(FILE_COMMANDER_ROOT))

from src.scanner import build_file_catalog  # noqa: E402  (import after sys.path setup on purpose)






def main() -> None:
    """
    Level 4:
    Because we want to see a real table of files and plan future file actions,
    this version lets us:

      1. Choose a directory to scan (text input).
      2. Choose a destination directory for future actions (text input).
      3. Click a button to scan and build a file catalog (stored in session).
      4. Use sidebar controls to filter the catalog by:
         - file_type
         - minimum size
         - "stale" (not accessed in N days)
      5. Interactively select files in the table with checkboxes.
      6. See a *dry-run* preview of which files would be moved to the
         destination directory (no actual file operations yet).
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
    #
    # UI: top text box "Directory to scan"
    # Code: we keep the raw string as `directory_text` and, if present,
    #       convert it to a Path for filesystem checks and scanning.
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
    #
    # UI: second text box "Destination directory for actions (future)"
    # Code: same pattern as above, but we only *display* it for now.
    #       The dry-run preview uses this Path to calculate target locations.
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
    #
    # UI: "🔍 Scan directory" button.
    # Code: when clicked, validate the path, run the scanner, and stash
    #       the resulting DataFrame in st.session_state["file_catalog"].
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

        # Store in session so we can reuse it across reruns.
        # This is always the full, original scan result (never filtered).
        st.session_state["file_catalog"] = file_catalog

        st.success(f"Scan complete. Found {len(file_catalog)} files.")

    # -------------------------------------------------------------------------
    # 3. If we have a catalog in session_state, show filters + table.
    #
    # UI:
    #   - Sidebar "Filters"
    #   - file_type multiselect
    #   - minimum size number input
    #   - stale_days number input
    #
    # Code:
    #   - Start from full `file_catalog` from session.
    #   - Apply filters to a copy (`filtered_catalog`).
    #   - Never overwrite the original in session.
    # -------------------------------------------------------------------------
    file_catalog = st.session_state.get("file_catalog")

    if file_catalog is not None and not file_catalog.empty:
        st.sidebar.header("Filters")

        # File type filter (multiselect)
        unique_file_types = sorted(file_catalog["file_type"].unique())
        selected_file_types = st.sidebar.multiselect(
            label="File types",
            options=unique_file_types,
            default=unique_file_types,
        )

        # Minimum size filter
        minimum_size_mb = st.sidebar.number_input(
            label="Minimum size (MB)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            help="Only show files at or above this size.",
        )

        # Stale filter (last accessed more than N days ago)
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
        # Apply filters starting from the full catalog every time.
        # This makes the filters reversible (e.g., increasing then decreasing
        # stale_days) because we never lose the original.
        # ---------------------------------------------------------------------
        filtered_catalog = file_catalog.copy()

        # 1️⃣ Filter by file_type
        if selected_file_types:
            filtered_catalog = filtered_catalog[
                filtered_catalog["file_type"].isin(selected_file_types)
            ]

        # 2️⃣ Filter by minimum size (MB -> bytes)
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

        # Make sure a 'selected' column exists.
        # This prepares us for future features where we mark rows as chosen.
        # For now, it simply shows up as a True/False column in the table.
        if "selected" not in filtered_catalog.columns:
            filtered_catalog = filtered_catalog.copy()
            filtered_catalog["selected"] = False


        # ---------------------------------------------------------------------
        # 4. Display table with a selectable column (checkboxes)
        #
        # We add a `selected` column, default False, and render with
        # st.data_editor so the user can check/uncheck rows.
        # The edited DataFrame comes back as `edited_catalog`.
        # ---------------------------------------------------------------------
        st.subheader("File catalog (filtered)")
        st.caption("Sorted by modified_at (newest first)")
        # st.caption(
        #   "Use the 'selected' column to mark files for a dry-run move preview. "
        #   "This does not change your filesystem."
        # )
        st.dataframe(filtered_catalog, width="stretch")


        # ---------------------------------------------------------
        # New: allow the user to download the current filtered view
        # as a CSV file.
        #
        # 1. Convert filtered_catalog (a DataFrame) into CSV text.
        # 2. Encode the text as UTF-8 bytes, which Streamlit expects.
        # 3. Feed those bytes into st.download_button so the browser
        #    offers a .csv file to save.
        # ---------------------------------------------------------
        csv_bytes = filtered_catalog.to_csv(index= False).encode("utf-8")

        st.download_button(
            label="⬇️ Download filtered catalog as CSV",
            data=csv_bytes,
            file_name= "file_commander_filtered.csv",
            mime="text/csv",
        )

        if filtered_catalog.empty:
            st.warning("No files match the current filters.")
            return

        st.write(
            f"Showing {len(filtered_catalog)} of {len(file_catalog)} files "
            f"(stale_days = {stale_days}, min_size_mb = {minimum_size_mb})"
        )


        # Add a checkbox column for selection (default False).
        catalog_for_edit = filtered_catalog.copy()
        if "selected" not in catalog_for_edit.columns:
            catalog_for_edit.insert(0, "selected", False)

        # Interactive table with checkboxes.
        edited_catalog = st.data_editor(
            catalog_for_edit,
            key="file_catalog_editor",
            hide_index=True,
            use_container_width=True,
        )

        # ---------------------------------------------------------------------
        # 5. Dry-run move preview: show which files WOULD be moved
        #
        # We never call any move/delete functions here. We only calculate:
        #   - how many files are selected
        #   - what their new paths WOULD be if moved to destination_directory
        # ---------------------------------------------------------------------
        selected_rows = edited_catalog[edited_catalog["selected"] == True]

        #### Use for debugging
        # st.write(
        #     f"Showing {len(filtered_catalog)} of {len(file_catalog)} files "
        #     f"(stale_days = {stale_days}, min_size_mb = {minimum_size_mb})"
        # )
        st.write(f"Selected files: {len(selected_rows)}")

        st.subheader("Move preview (dry run)")

        if destination_directory is None:
            st.info(
                "Set a destination directory above to see where selected files "
                "would be moved."
            )
        elif selected_rows.empty:
            st.info(
                "Select one or more files in the table to see the move preview."
            )
        else:
            # Build a small preview table with original path and proposed destination.
            preview_df = selected_rows[["path", "name"]].copy()
            preview_df["destination_path"] = preview_df["name"].apply(
                lambda name: str(destination_directory / name)
            )

            st.caption(
                "These files would be moved (in a future version) from their "
                "current locations to the destination directory:"
            )
            st.dataframe(preview_df, use_container_width=True)
            # st.dataframe(filtered_catalog, width="stretch")

    else:
        st.info("Scan a directory to see the file catalog.")



if __name__ == "__main__":
    main()
