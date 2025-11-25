# tests/test_scanner.py

"""
In this file we prove that `list_files` can discover every file inside
a tiny nested folder structure using a temporary directory as our playground.
"""

from pathlib import Path
from src.scanner import list_files


def test_list_files_returns_all_files(tmp_path: Path) -> None:
    """
    Because we want to see a list of all files in a directory tree,
    we create a fake folder with a subfolder and two files, then check that
    `list_files` finds both files and nothing else.
    """
    # tmp_path is a pytest-provided temporary directory on disk.
    base_directory = tmp_path

    # First file directly inside the base directory.
    first_file = base_directory / "file1.txt"
    first_file.write_text("hello")

    # A subdirectory under the base directory.
    subdirectory = base_directory / "subdir"
    subdirectory.mkdir()

    # Second file inside the subdirectory.
    second_file = subdirectory / "file2.log"
    second_file.write_text("world")

    # Act: call the function we are testing.
    discovered_paths = list_files(base_directory)

    # Convert all Paths to strings for easier comparison.
    discovered_path_strings = sorted(str(file_path) for file_path in discovered_paths)
    expected_path_strings = sorted([str(first_file), str(second_file)])

    # Assert: we found exactly the two files we created.
    assert discovered_path_strings == expected_path_strings
