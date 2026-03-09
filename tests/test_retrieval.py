from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.retrieval import retrieve_notebooks


def test_retrieve_notebooks_returns_hit() -> None:
    hits = retrieve_notebooks("file_io", "File not found: config/models.json")
    assert hits
    assert hits[0].name == "path_not_found.md"


def test_retrieve_notebooks_returns_empty_on_no_match() -> None:
    hits = retrieve_notebooks("file_io", "galaxy brain unicorn potato")
    assert hits == []
