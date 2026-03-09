from __future__ import annotations

"""Notebook parser for extracting fix and verification sections."""

import re
from pathlib import Path
from typing import Any


def _extract_section(text: str, title: str) -> str:
    """Extract a markdown H2 section by title."""
    pattern = rf"## {re.escape(title)}\n(.*?)(?:\n## |\Z)"
    match = re.search(pattern, text, re.S)
    return match.group(1).strip() if match else ""


def parse_notebook(path: Path) -> dict[str, Any]:
    """Parse a notebook and return core machine-readable fields."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = lines[0].strip() if lines else path.name

    return {
        "path": str(path),
        "title": title,
        "fix": _extract_section(text, "Fix") or _extract_section(text, "解决方法"),
        "verification": _extract_section(text, "Verification") or _extract_section(text, "验证方法"),
    }
