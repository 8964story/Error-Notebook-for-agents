from __future__ import annotations

import re
from pathlib import Path

ERRORS_DIR = Path(__file__).resolve().parents[1] / "errors"


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9_\-.]+", (text or "").lower()))


def retrieve_notebooks(error_type: str, error_text: str, top_k: int = 3) -> list[Path]:
    target_dir = ERRORS_DIR / error_type
    if not target_dir.exists():
        return []

    query_tokens = _tokens(error_text)
    scored: list[tuple[int, Path]] = []

    for path in target_dir.glob("*.md"):
        content = path.read_text(encoding="utf-8")
        score = len(query_tokens & _tokens(content))
        scored.append((score, path))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [path for score, path in scored[:top_k] if score > 0] or [path for _, path in scored[:1]]
