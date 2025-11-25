"""
Because we want a quick, visual way to understand what our file catalog
functions are doing, this module acts as a small playground script:
it takes a directory, builds a file catalog, and prints a preview.
"""

from __future__ import annotations

import sys
from pathlib import Path

from src.scanner import build_file_catalog


def main() -> None:
    """
    Because we want to run this module from the command line, this function
    reads an optional directory argument, builds the catalog, and prints
    a simple summary and preview.
    """
    # If the user passes a directory path as the first argument, use it.
    # Otherwise, default to the user's Downloads folder.
    if len(sys.argv) > 1:
        target_directory = Path(sys.argv[1])
    else:
        target_directory = Path.home() / "Downloads"

    print(f"\n[playground] Scanning directory: {target_directory}")

    file_catalog = build_file_catalog(target_directory)

    print(f"[playground] Number of files found: {len(file_catalog)}\n")

    # Show the first 10 rows so we do not flood the terminal.
    print("[playground] Preview of file catalog (up to 10 rows):")
    print(file_catalog.head(10))

    # Optionally show the data types to reinforce how pandas sees each column.
    print("\n[playground] Data types:")
    print(file_catalog.dtypes)


if __name__ == "__main__":
    main()
