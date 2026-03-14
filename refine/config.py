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


def get_refine_page_size() -> int:
    """Batch size for refine INSERT/UPDATE (execute_values, chunked processing). Tune via REFINE_INSERT_PAGE_SIZE (default 5000)."""
    raw = os.environ.get("REFINE_INSERT_PAGE_SIZE", "5000").strip()
    try:
        n = int(raw)
        return max(500, min(50_000, n))
    except ValueError:
        return 5000
