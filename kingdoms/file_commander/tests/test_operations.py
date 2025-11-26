"""
In this file we prove that move_file can relocate a file from one
directory to another while preserving its contents.
"""


from pathlib import Path

from src.operations import move_file

def test_move_file_moves_file_and_preserves_contents(tmp_path:Path) -> None:
    """
    Because we want to be confident that move_file actually moves a file
    and does not lose its contents, this test:

      1. Creates a temporary source and destination directory.
      2. Writes a small text file in the source directory.
      3. Calls move_file to move it to the destination directory.
      4. Asserts that:
         - the original file no longer exists,
         - the new file exists in the destination,
         - and the contents are unchanged.
    """

    #1. Arrange: set up source and destination directories.
    source_directory = tmp_path /"source"
    destination_directory = tmp_path / "destination"
    source_directory.mkdir()
    destination_directory.mkdir()

    #Create a file in the source directory.
    original_file = source_directory / "example.txt"
    original_contents = "hello, world"
    original_file.write_text(original_contents)

    #2. Act : move the file
    new_path = move_file(original_file, destination_directory)

    #3. Assert: the original path no longer exists.
    assert not original_file.exists()

    #Assert the new path exist ans has the same contents
    assert new_path.exists()
    assert new_path.read_text() == original_contents

    #Assert: the new file lives inside the destination directory.
    assert new_path.parent == destination_directory
