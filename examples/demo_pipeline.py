from __future__ import annotations

"""Runnable demo for the Error Notebook pipeline."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.pipeline import handle_error


def main() -> None:
    """Run the demo pipeline against sample errors."""
    sample_path = ROOT / "examples" / "sample_errors.json"
    samples = json.loads(sample_path.read_text(encoding="utf-8"))

    print("# Error Notebook Demo")
    print(f"Samples: {len(samples)}")
    print(f"Action log: {ROOT / 'memory' / 'action_log.md'}")

    for item in samples:
        result = handle_error(item["error"])
        print(f"\n=== {item['name']} ===")
        print(f"error_type: {result['error_type']}")
        print(f"retrieved_notebooks: {result['retrieved_notebooks']}")
        print(f"suggested_fix: {result['suggested_fix']}")
        print("verification:")
        if result["verification"]:
            for line in result["verification"]:
                print(f"- {line}")
        else:
            print("- <empty>")


if __name__ == "__main__":
    main()
