"""Utility helpers for file and configuration handling."""
from __future__ import annotations

import yaml
from pathlib import Path
from typing import Any


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YAML configuration file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_directories(*paths: str | Path) -> None:
    """Ensure all given directories exist."""
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)
