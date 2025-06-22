"""Data initialization helpers."""
from __future__ import annotations

from pathlib import Path

from ..core.utils import ensure_directories


def setup_data_dirs() -> None:
    """Create directories used by the project if they are missing."""
    ensure_directories(Path("reportes"), Path("pictures"), Path("chroma_db"))
