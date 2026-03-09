from __future__ import annotations

"""Action trace logger for Error Notebook."""

from datetime import datetime
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / "memory" / "action_log.md"


def append_action_log(task: str, error_type: str, notebook_path: str, verification: str) -> None:
    """Append a markdown action trace entry."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M')} - {task}\n")
        handle.write(f"- 类型：{error_type}\n")
        handle.write(f"- 读取错题：{notebook_path}\n")
        handle.write("- 触发方式：post-error\n")
        handle.write(f"- 验证证据：{verification or 'TBD'}\n")
