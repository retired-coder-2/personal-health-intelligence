# tests/test_scanner.py

"""
In this file we prove that `list_files` can discover every file inside
a tiny nested folder structure using a temporary directory as our playground.
"""

from pathlib import Path
import pandas as pd

from src.scanner import list_files, build_file_catalog


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


def test_build_file_catalog_basic_metadata(tmp_path: Path) -> None:
    """
    Because we want a table-like view of our files (not just a list of paths),
    this test builds a tiny fake directory, calls `build_file_catalog`, and
    checks that the resulting DataFrame has the expected rows and key columns.
    """
    base_directory = tmp_path

    #Create two files just like in the previous test(test_list_files_returns_all_files)
    first_file = base_directory / "file1.txt"
    first_file_content = "hello"
    first_file.write_text(first_file_content)

    subdirectory = base_directory / "subdir"
    subdirectory.mkdir()

    second_file = subdirectory / "file2.log"
    second_file_content = "world"
    second_file.write_text(second_file_content)

     # Act: build the file catalog as a pandas DataFrame.
    file_catalog = build_file_catalog(base_directory)

    # The catalog should have exactly one row per file.
    assert len(file_catalog) == 2


    expected_columns = {
        "path",
        "directory",
        "name",
        "extension",
        "size_bytes",
        "created_at",
        "modified_at"
    }

    assert expected_columns.issubset(set(file_catalog.columns))

    # Find the row for the first file by matching the path string.
    first_file_path_string = str(first_file)
    first_file_row = file_catalog.loc[file_catalog["path"] == first_file_path_string].squeeze()

    # Check a few important fields for that row.
    assert first_file_row["name"] == "file1.txt"
    assert first_file_row["extension"] == ".txt"
    assert first_file_row["size_bytes"] == len(first_file_content)

      # We do not assert exact timestamps (they are system-dependent),
    # but we at least confirm they are not null.
    assert pd.notnull(first_file_row["created_at"])
    assert pd.notnull(first_file_row["modified_at"])

