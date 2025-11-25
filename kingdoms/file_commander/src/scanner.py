# src/scanner.py

"""
This module walks through a folder tree and returns every file path,
forming the foundation for our file catalog pipeline.
"""

from pathlib import Path


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
