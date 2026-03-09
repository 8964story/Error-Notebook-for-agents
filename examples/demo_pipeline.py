from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.pipeline import handle_error


def main() -> None:
    sample_path = ROOT / "examples" / "sample_errors.json"
    samples = json.loads(sample_path.read_text(encoding="utf-8"))
    for item in samples:
        result = handle_error(item["error"])
        print(f"\n=== {item['name']} ===")
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
