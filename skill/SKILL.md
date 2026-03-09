---
name: agent-error-spine
description: Error governance and recovery loop for agent tasks. Use when a task fails, partially fails, or has high risk of silent failure (config changes, scheduled jobs, delivery routing, model/provider switching). Applies post-error retrieval of similar past errors, and preflight checks for non-immediate-verification tasks.
---

# Agent Error Spine

Default policy:
- **Post-error first**: when execution returns an error, immediately retrieve similar error records and reuse fixes.
- **Preflight only for silent-failure risk**: config, cron, delivery, model/provider, permission changes.

## Trigger routing
Map task → error file:
- model/config/provider/auth → `docs/errors/errors_by_type/file_io.md` + `api_call.md`
- cron/delivery/channel routing → `docs/errors/errors_by_type/api_call.md`
- scraping/download/page-read → `docs/errors/errors_by_type/web_scraping.md`
- decision/planning mistakes → `docs/errors/errors_by_type/logic.md`

## Execution protocol
1. Classify task/error type.
2. Read mapped error file(s) and extract one reusable fix path.
3. Execute fix.
4. Verify outcome with explicit check command.
5. Append action trace to `memory/action_log.md`.
6. If new failure pattern: append full record to `docs/errors/...` and update index.

## Hard checks before closing task
- For model/config changes: verify via `/model status` or equivalent status command.
- For cron/delivery: verify with list/status + one manual run.
- For browser/read tasks: verify content actually extracted, not only page opened.

## Record format
Use template in `references/error_template.md`.
Use action trace format in `references/action_log_template.md`.

## Non-goals
- Do not read all error files every time.
- Do not skip verification after "config written".
- Do not mark success without evidence output.
