from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.parser import parse_notebook


def test_parser_reads_frontmatter() -> None:
    path = ROOT / "errors" / "provider_auth" / "api_key_missing.md"
    parsed = parse_notebook(path)
    assert parsed["has_frontmatter"] is True
    assert parsed["category"] == "provider_auth"
    assert "api_key" in parsed["tags"]
    assert parsed["fix"]
    assert parsed["verification"]
