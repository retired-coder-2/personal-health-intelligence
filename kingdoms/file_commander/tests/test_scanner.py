"""
In this file we prove that `list_files` can discover every file inside
a tiny nested folder structure using a temporary directory as our playground,
and that `build_file_catalog` can describe those files as a table of metadata.
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
    base_directory = tmp_path

    first_file = base_directory / "file1.txt"
    first_file.write_text("hello")

    subdirectory = base_directory / "subdir"
    subdirectory.mkdir()

    second_file = subdirectory / "file2.log"
    second_file.write_text("world")

    discovered_paths = list_files(base_directory)

    discovered_path_strings = sorted(str(file_path) for file_path in discovered_paths)
    expected_path_strings = sorted([str(first_file), str(second_file)])

    assert discovered_path_strings == expected_path_strings


def test_build_file_catalog_basic_metadata(tmp_path: Path) -> None:
    """
    Because we want a table-like view of our files (not just a list of paths),
    this test builds a tiny fake directory, calls `build_file_catalog`, and
    checks that the resulting DataFrame has the expected rows and key columns.
    """
    base_directory = tmp_path

    first_file = base_directory / "file1.txt"
    first_file_content = "hello"
    first_file.write_text(first_file_content)

    subdirectory = base_directory / "subdir"
    subdirectory.mkdir()

    second_file = subdirectory / "file2.log"
    second_file_content = "world"
    second_file.write_text(second_file_content)

    file_catalog = build_file_catalog(base_directory)

    assert len(file_catalog) == 2

    expected_columns = {
        "path",
        "directory",
        "name",
        "extension",
        "size_bytes",
        "created_at",
        "modified_at",
    }
    assert expected_columns.issubset(set(file_catalog.columns))

    # first_file_path_string = str(first_file)
    # first_file_row = file_catalog.loc[file_catalog["path"] == first_file_path_string].squeeze()

    first_file_path_string = str(first_file)

    matching_rows = file_catalog.loc[file_catalog["path"] == first_file_path_string]

    # Make sure there is exactly one matching row.
    assert len(matching_rows) == 1

    # Take the first (and only) row as a Series.
    first_file_row = matching_rows.iloc[0]


    assert first_file_row["name"] == "file1.txt"
    assert first_file_row["extension"] == ".txt"
    assert first_file_row["size_bytes"] == len(first_file_content)

    assert pd.notnull(first_file_row["created_at"])
    assert pd.notnull(first_file_row["modified_at"])
