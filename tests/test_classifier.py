from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.classifier import classify_error


def test_classifier_api():
    assert classify_error('OpenAI API key missing') == 'api_call'


def test_classifier_file():
    assert classify_error('File not found: config/models.json') == 'file_io'
