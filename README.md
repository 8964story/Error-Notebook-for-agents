# 错题本（Error Notebook）

An Agent Reliability Starter Kit for turning failures into reusable fixes.

## What it is
`错题本（Error Notebook）` is a lightweight error-governance layer for AI agents:
- Post-error retrieval of similar failures
- Explicit verification after suggested fixes
- Standardized error notebooks / playbooks
- Auditable action traces

## What changed in v0.1
This repository is no longer only a skill stub.

It now contains a runnable minimal pipeline:

```text
error input
  -> classify
  -> retrieve notebook(s)
  -> extract fix / verification
  -> append action log
```

## Repository structure
- `skill/` — original skill-oriented protocol materials
- `docs/` — architecture + protocol
- `error_memory/` — minimal runnable pipeline
- `errors/` — categorized notebooks
- `examples/` — demo inputs and runnable example
- `tests/` — basic tests
- `memory/` — action log output

## Quick start
Run the demo:

```bash
python examples/demo_pipeline.py
```

Expected output:
- error type
- retrieved notebook(s)
- suggested fix
- verification checklist

## Included notebooks
- `errors/api_call/api_key_missing.md`
- `errors/file_io/path_not_found.md`
- `errors/web_scraping/page_loaded_but_no_data.md`
- `errors/logic/wrong_branch.md`

## Trigger policy
- Default: **post-error first**
- Preflight only for high-risk tasks (config / cron / delivery / model-provider changes)

## Project boundary
This project is **not**:
- a self-healing framework
- a full agent platform
- a production-grade reliability OS

It is a practical starter kit for making failures reusable and verifiable.

## Next priorities
1. Add 10+ real failure cases
2. Improve notebook retrieval quality
3. Add metrics (repeat failure rate / verification coverage)
4. Add one real OpenClaw integration demo

## License
MIT
