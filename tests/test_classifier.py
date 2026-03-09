from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.classifier import classify_error


def test_classifier_provider_auth() -> None:
    assert classify_error("OpenAI API key missing") == "provider_auth"


def test_classifier_file_io() -> None:
    assert classify_error("File not found: config/models.json") == "file_io"


def test_classifier_web_scraping() -> None:
    assert classify_error("Browser page loaded but extracted content is empty") == "web_scraping"


def test_classifier_cron_not_api_call() -> None:
    assert classify_error("cron delivery failed silently") == "workflow_or_logic"
