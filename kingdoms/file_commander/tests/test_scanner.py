#test_scanner.py
import pytest
from src.scanner import list_files


def test_list_files_return_all_files(tmp_path):
    """Given a directory with nested folders and files, list_files should
    return all file paths (no directories)."""
    #tmp_path is a pytest fixture that gives us a temporary folder on disk
    #It's isolated per test and automatically cleaned up after the test.

    file1 = tmp_path /"file1.txt"
    file1.write_text("hello")

    subdir = tmp_path /"subdir"
    subdir.mkdir()


    file2 = subdir /"file2.log"
    file2.write_text("hello")

    result = list_files(tmp_path)

    result_strs = sorted(str(p) for p in result)

    expected = sorted([str(file1), str(file2)])

    assert result_strs == expected
