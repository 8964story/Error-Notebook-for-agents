from __future__ import annotations

"""Notebook parser for extracting frontmatter, fix, and verification sections."""

import re
from pathlib import Path
from typing import Any

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def _extract_section(text: str, title: str) -> str:
    """Extract a markdown H2 section by title."""
    pattern = rf"## {re.escape(title)}\n(.*?)(?:\n## |\Z)"
    match = re.search(pattern, text, re.S)
    return match.group(1).strip() if match else ""


def _parse_simple_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse simple YAML-like frontmatter without external dependencies."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    raw = match.group(1)
    body = text[match.end():]
    data: dict[str, Any] = {}

    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
            data[key] = items
        else:
            data[key] = value.strip("'\"")

    return data, body


def parse_notebook(path: Path) -> dict[str, Any]:
    """Parse a notebook and return machine-readable fields."""
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _parse_simple_frontmatter(text)
    lines = body.splitlines()
    title = frontmatter.get("title") or (lines[0].strip() if lines else path.name)

    return {
        "path": str(path),
        "title": title,
        "category": frontmatter.get("category", ""),
        "tags": frontmatter.get("tags", []),
        "risk": frontmatter.get("risk", ""),
        "version": frontmatter.get("version", ""),
        "status": frontmatter.get("status", ""),
        "fix": _extract_section(body, "Fix") or _extract_section(body, "解决方法"),
        "verification": _extract_section(body, "Verification") or _extract_section(body, "验证方法"),
        "has_frontmatter": bool(frontmatter),
    }
