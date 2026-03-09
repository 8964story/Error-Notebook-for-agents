from __future__ import annotations

"""Minimal notebook retrieval for Error Notebook."""

import re
from pathlib import Path

ERRORS_DIR = Path(__file__).resolve().parents[1] / "errors"


def _tokens(text: str) -> set[str]:
    """Tokenize text into lowercase alphanumeric terms."""
    return set(re.findall(r"[a-zA-Z0-9_\-.]+", (text or "").lower()))


def retrieve_notebooks(error_type: str, error_text: str, top_k: int = 3) -> list[Path]:
    """Return top-k notebook paths with positive token overlap."""
    target_dir = ERRORS_DIR / error_type
    if not target_dir.exists():
        return []

    query_tokens = _tokens(error_text)
    scored: list[tuple[int, Path]] = []

    for path in target_dir.glob("*.md"):
        content = path.read_text(encoding="utf-8")
        score = len(query_tokens & _tokens(content))
        scored.append((score, path))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [path for score, path in scored[:top_k] if score > 0]
