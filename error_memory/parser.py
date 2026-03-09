from __future__ import annotations

import re
from pathlib import Path


def _extract_section(text: str, title: str) -> str:
    pattern = rf"## {re.escape(title)}\n(.*?)(?:\n## |\Z)"
    match = re.search(pattern, text, re.S)
    return match.group(1).strip() if match else ""


def parse_notebook(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return {
        "path": str(path),
        "title": text.splitlines()[0].strip() if text else path.name,
        "fix": _extract_section(text, "Fix") or _extract_section(text, "解决方法"),
        "verification": _extract_section(text, "Verification") or _extract_section(text, "验证方法"),
    }
