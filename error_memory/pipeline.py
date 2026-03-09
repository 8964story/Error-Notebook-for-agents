from __future__ import annotations

from .classifier import classify_error
from .logger import append_action_log
from .parser import parse_notebook
from .retrieval import retrieve_notebooks


def handle_error(error_text: str) -> dict:
    error_type = classify_error(error_text)
    notebooks = retrieve_notebooks(error_type, error_text)
    if not notebooks:
        result = {
            "error_type": error_type,
            "retrieved_notebooks": [],
            "suggested_fix": "No notebook found. Create a new notebook from this failure.",
            "verification": [],
        }
        append_action_log(error_text, error_type, "NONE", "No notebook found")
        return result

    best = parse_notebook(notebooks[0])
    verification_lines = [line.strip("- ").strip() for line in best["verification"].splitlines() if line.strip()]
    result = {
        "error_type": error_type,
        "retrieved_notebooks": [str(p) for p in notebooks],
        "suggested_fix": best["fix"],
        "verification": verification_lines,
    }
    append_action_log(error_text, error_type, best["path"], best["verification"])
    return result
