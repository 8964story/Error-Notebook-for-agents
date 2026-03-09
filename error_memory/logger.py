from __future__ import annotations

from datetime import datetime
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / "memory" / "action_log.md"


def append_action_log(task: str, error_type: str, notebook_path: str, verification: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M')} - {task}\n")
        f.write(f"- 类型：{error_type}\n")
        f.write(f"- 读取错题：{notebook_path}\n")
        f.write(f"- 触发方式：post-error\n")
        f.write(f"- 验证证据：{verification or 'TBD'}\n")
