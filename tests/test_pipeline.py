from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from error_memory.pipeline import handle_error


def test_pipeline_no_notebook_match() -> None:
    result = handle_error("mysterious provider banana vacuum failure")
    assert result["error_type"] == "workflow_or_logic"
    assert result["retrieved_notebooks"] == []
    assert result["suggested_fix"] == "No notebook found. Create a new notebook from this failure."
    assert result["verification"] == []


def test_pipeline_file_hit() -> None:
    result = handle_error("File not found: config/models.json")
    assert result["error_type"] == "file_io"
    assert result["retrieved_notebooks"]
    assert result["suggested_fix"]


def test_pipeline_timeout_hit() -> None:
    result = handle_error("Request timed out once, retry later succeeded")
    assert result["error_type"] == "transient_network"
    assert result["retrieved_notebooks"]
    assert result["verification"]
