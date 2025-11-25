from pathlib import Path

def list_files(root:Path) -> list[Path]:
    """
    Docstring for list_files

    :param root: The directory to scan
    :type root: Path
    :return: A list paths pointing to files (not directories)
    :rtype: list[Path]
    """

    #Endire we have a Path object even if someone passes a string
    root_path = Path(root)

    if not root_path.exists():
        raise FileNotFoundError(f"Root path does not exist: {root_path}")

    if not root_path.is_dir():
        raise NotADirectoryError(f"Root path is not a directory: {root_path}")

    files: list[Path] = []

    for path in root_path.rglob("*"):
        if path.is_file():
            files.append(path)

    return files
