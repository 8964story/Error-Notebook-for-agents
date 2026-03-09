from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.retrieval import retrieve_notebooks


def test_retrieve_notebooks():
    hits = retrieve_notebooks('api_call', 'OpenAI API key missing for request')
    assert hits
    assert hits[0].name == 'api_key_missing.md'
