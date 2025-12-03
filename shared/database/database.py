# shared/database/database.py

"""
Tiny helper for getting a SQLite database engine.
Right now we only care about "give me something I can .to_sql() into".
"""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_sqlite_engine(db_path: str | Path) -> Engine:
    """
    Because we want a simple way to talk to a local SQLite file,
    this helper builds a SQLAlchemy Engine pointed at that file.

    Example:
        engine = get_sqlite_engine("file_commander.db")
    """
    db_path = Path(db_path)
    # sqlite:////absolute/path/to/file.db
    url = f"sqlite:///{db_path.resolve()}"
    return create_engine(url, future=True)
