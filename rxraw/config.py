"""Config: database URL and data directory. No dependency on etl."""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_database_url() -> str | None:
    """PostgreSQL connection string. Set EXTERNAL_DATABASE_URL in env or .env."""
    return os.environ.get("EXTERNAL_DATABASE_URL")


def get_data_dir() -> Path:
    """Directory containing MED-File v2 files. Default: project data/. Override with DATA_DIR."""
    raw = os.environ.get("DATA_DIR")
    if raw:
        return Path(raw)
    root = Path(__file__).resolve().parent.parent
    return root / "data"


def get_insert_batch_size() -> int:
    """Batch size for bulk inserts (execute_values page_size). Default 5000. Override with RXRAW_INSERT_BATCH_SIZE."""
    raw = os.environ.get("RXRAW_INSERT_BATCH_SIZE")
    if raw is None:
        return 5000
    try:
        n = int(raw)
        return max(500, min(n, 50000))
    except ValueError:
        return 5000
