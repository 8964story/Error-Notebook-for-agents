from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.pipeline import handle_error


def test_pipeline_basic():
    result = handle_error('OpenAI API key missing for request')
    assert result['error_type'] == 'api_call'
    assert result['retrieved_notebooks']
    assert result['suggested_fix']
    assert result['verification']
