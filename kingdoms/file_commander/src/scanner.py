# src/scanner.py

"""
This module walks through a folder tree and returns every file path,
then turns those paths into a DataFrame that describes each file with
size and timestamps for our file catalog pipeline.
"""

from pathlib import Path
from datetime import datetime
from typing import Iterable

import pandas as pd


def list_files(root: Path) -> list[Path]:
    """
    Because we want a simple way to see every file inside a directory
    and its subdirectories, this function walks the folder tree and
    returns a list of file paths (no directories).

    :param root: The directory to scan (can be a Path or a string).
    :return: A list of Path objects, one for each file found.
    """
    # Normalize the input to a Path object even if a string was passed in.
    root_path = Path(root)

    # Guardrail: the starting path must exist.
    if not root_path.exists():
        raise FileNotFoundError(f"Root path does not exist: {root_path}")

    # Guardrail: the starting path must actually be a directory.
    if not root_path.is_dir():
        raise NotADirectoryError(f"Root path is not a directory: {root_path}")

    # We'll collect all file paths in this list.
    file_paths: list[Path] = []

    # root_path.rglob("*") walks the directory recursively and yields
    # both files and directories. We only keep the files.
    for candidate_path in root_path.rglob("*"):
        if candidate_path.is_file():
            file_paths.append(candidate_path)

    return file_paths

def build_file_catalog(root: Path) -> pd.DataFrame:
    """
    Because we want a table-like catalog of our files that is easy to query,
    this function walks the directory tree starting at `root`, collects
    metadata for each file, and returns a pandas DataFrame.

    Each row in the DataFrame describes one file with columns:
      - path: full path to the file (string)
      - directory: parent directory of the file (string)
      - name: file name with extension
      - extension: file extension (e.g. ".txt", ".pdf")
      - size_bytes: size of the file in bytes (integer)
      - created_at: file creation time as a datetime
      - modified_at: last modified time as a datetime
    """
    root_path =Path(root)

    file_paths: list[Path] = list_files(root_path)

    file_records: list[dict] = []

    for file_path in file_paths:
        file_stat = file_path.stat()

        file_record = {
            "path": str(file_path),
            "directory": str(file_path.parent),
            "name": file_path.name,
            "extension": file_path.suffix.lower(),
            "size_bytes": file_stat.st_size,
            "created_at": datetime.fromtimestamp(file_stat.st_ctime),
            "modified_at": datetime.fromtimestamp(file_stat.st_mtime)
        }

        file_records.append(file_record)


    expected_column_order = [
        "path",
        "directory",
        "name",
        "extension",
        "size_bytes",
        "created_at",
        "modified_at",
    ]

    file_catalog = pd.DataFrame.from_records(file_records) [expected_column_order]

    return file_catalog

