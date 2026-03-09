# 错题本（Error Notebook）

An Agent Reliability Starter Kit for turning failures into reusable fixes.  
一个面向 AI agent 的可靠性入门工具包，把失败转化为可复用的修复资产。

## What it is / 它是什么
`错题本（Error Notebook）` is a lightweight error-governance layer for AI agents.  
`错题本（Error Notebook）` 是一个面向 AI agent 的轻量级错误治理层。

- Post-error retrieval of similar failures  
  在错误发生后检索相似失败案例
- Explicit verification after suggested fixes  
  在给出修复建议后要求显式验证
- Standardized error notebooks / playbooks  
  提供标准化的错误 notebook / 修复 playbook
- Auditable action traces  
  保留可审计的行动轨迹

## What changed in v0.1 / v0.1 有什么变化
This repository is no longer only a skill stub.  
这个仓库不再只是一个 skill 雏形。

It now contains a runnable minimal pipeline:  
它现在已经包含一个可以运行的最小闭环：

```text
error input
  -> classify
  -> retrieve notebook(s)
  -> extract fix / verification
  -> append action log
```

```text
错误输入
  -> 分类
  -> 检索 notebook
  -> 提取修复建议 / 验证项
  -> 追加 action log
```

## Repository structure / 仓库结构
- `skill/` — original skill-oriented protocol materials  
  `skill/` —— 原始的 skill 协议材料
- `docs/` — architecture + protocol  
  `docs/` —— 架构与协议说明
- `error_memory/` — minimal runnable pipeline  
  `error_memory/` —— 最小可运行闭环
- `errors/` — categorized notebooks  
  `errors/` —— 分类后的错误 notebook
- `examples/` — demo inputs and runnable example  
  `examples/` —— 演示输入与可运行示例
- `tests/` — basic tests  
  `tests/` —— 基础测试
- `memory/` — action log output  
  `memory/` —— action log 输出位置

## Quick start / 快速开始
Run the demo:  
运行演示：

```bash
python examples/demo_pipeline.py
```

Expected output:  
预期输出包括：
- error type  
  错误类型
- retrieved notebook(s)  
  命中的 notebook
- suggested fix  
  建议修复路径
- verification checklist  
  验证检查清单

## Included notebooks / 已包含的 notebook
- `errors/api_call/api_key_missing.md`
- `errors/file_io/path_not_found.md`
- `errors/web_scraping/page_loaded_but_no_data.md`
- `errors/logic/wrong_branch.md`

## Trigger policy / 触发策略
- Default: **post-error first**  
  默认：**先处理已发生错误（post-error first）**
- Preflight only for high-risk tasks (config / cron / delivery / model-provider changes)  
  仅在高静默失败风险任务中做 preflight（如 config / cron / delivery / model-provider 变更）

## Project boundary / 项目边界
This project is **not**:  
这个项目**不是**：
- a self-healing framework  
  自动自愈框架
- a full agent platform  
  完整 agent 平台
- a production-grade reliability OS  
  生产级可靠性操作系统

It is a practical starter kit for making failures reusable and verifiable.  
它是一个务实的 starter kit，目标是让失败变得可复用、可验证、可审计。

## Next priorities / 下一步重点
1. Add 10+ real failure cases  
   增加 10+ 个真实失败案例
2. Improve notebook retrieval quality  
   提升 notebook 检索质量
3. Add metrics (repeat failure rate / verification coverage)  
   增加指标（重复失败率 / 验证覆盖率）
4. Add one real OpenClaw integration demo  
   增加一个真实的 OpenClaw 接入 demo

## License / 许可证
MIT
