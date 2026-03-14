"""Config: database URL. Same env as rxraw (EXTERNAL_DATABASE_URL)."""

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_database_url() -> str | None:
    """PostgreSQL connection string. Set EXTERNAL_DATABASE_URL in env or .env."""
    return os.environ.get("EXTERNAL_DATABASE_URL")
