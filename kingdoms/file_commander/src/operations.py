"""
Because we want to safely move individual files as part of our file
management actions, this module defines small, focused functions for
operations like moving files.
"""

from pathlib import Path
import shutil

def move_file(source:Path, destination_directory:Path) -> Path:
    """ Because we want to move a single file into a new directory in a clear
    and testable way, this function:

      1. Validates that the source exists and is a file.
      2. Validates that the destination directory exists.
      3. Constructs the new path (destination_directory / source.name).
      4. Uses shutil.move() to perform the move.
      5. Returns the new Path to the moved file.

    :param source: Path to the existing file to move.
    :param destination_directory: Path to the directory where the file
                                  should be moved.
    :return: Path to the file at its new location.
    """
    source_path = Path(source)
    destination_dir_path = Path(destination_directory)

    if not source_path.exists():
        raise FileNotFoundError(f"Source file does not exist: {source_path}")

    if not source_path.is_file():
        raise ValueError(f"Source path is not a file {source_path}")

    if not destination_dir_path.exists():
        raise FileNotFoundError(f"Destination directory does not exist {destination_dir_path}")

    if not destination_dir_path.is_dir():
        raise NotADirectoryError(f"Destination is not a directory: {destination_dir_path}")


    destination_path = destination_dir_path / source_path.name

    # Perform the move. shutil.move returns the destination as a string,
    # but we wrap it back into a Path for consistency.

    result_path_str = shutil.move(str(source_path), str(destination_path))
    return Path(result_path_str)

