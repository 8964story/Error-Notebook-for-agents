# Agent 错题本 / Error Notebook

**A lightweight failure-governance starter kit for AI agents.**  
**一个面向 AI agents 的轻量级失败治理入门工具包。**

---

## Why this project exists / 为什么要做这个项目

AI agents tend to repeat the same failures.  
AI agent 往往会重复犯同类错误。

Traditional logs record what happened, but they do not prevent recurrence.  
传统日志只能记录发生了什么，却不能阻止错误再次发生。

Error Notebook is built to turn failures into reusable recovery knowledge.  
错题本的目标，是把失败转化为可复用的修复知识。

It focuses on a practical loop:  
它聚焦于一个务实的闭环：

- classify the failure  
  对失败进行分类
- retrieve similar historical cases  
  检索相似历史案例
- suggest a fix path  
  给出修复路径
- require explicit verification  
  要求显式验证
- write an auditable action trace  
  写入可审计的行动轨迹

---

## Core loop / 核心闭环

```text
error input
  -> classify
  -> retrieve similar notebook(s)
  -> suggest fix
  -> explicit verification
  -> append action trace
```

```text
错误输入
  -> 分类
  -> 检索相似 notebook
  -> 给出修复建议
  -> 显式验证
  -> 追加 action trace
```

---

## What it is / 它是什么

Error Notebook is a lightweight error-governance layer for AI agents.  
Error Notebook 是一个面向 AI agent 的轻量级错误治理层。

It provides:  
它提供：

- **Post-error retrieval**  
  **错误后检索**：从历史 notebook 中找相似失败案例
- **Explicit verification**  
  **显式验证**：修复后必须验证，而不是“看起来没报错就算成功”
- **Standardized playbooks**  
  **标准化 playbook**：把修复经验沉淀成可复用模板
- **Auditable traces**  
  **可审计轨迹**：记录每次动作、依据和验证证据

---

## What it is not / 它不是什么

This project is **not**:  
这个项目**不是**：

- a self-healing framework  
  自动自愈框架
- a full agent platform  
  完整 agent 平台
- a production-grade reliability OS  
  生产级可靠性操作系统

It is a practical starter kit.  
它是一个务实的 starter kit。

The goal is not to solve everything automatically, but to make repeated failures reusable, verifiable, and easier to govern.  
目标不是自动解决一切，而是让重复失败变得可复用、可验证、可治理。

---

## What changed in v0.1 / v0.1 当前状态

This repository is no longer only a skill stub.  
这个仓库不再只是一个 skill 雏形。

It now contains a runnable minimal pipeline.  
它现在已经具备一个可运行的最小闭环。

Current v0.1 scope includes:  
当前 v0.1 范围包括：

1. rule-based error classification  
   基于规则的错误分类
2. notebook retrieval  
   notebook 检索
3. extracting fix / verification from notebooks  
   从 notebook 中提取修复建议 / 验证项
4. action trace logging  
   action trace 记录

---

## Installation / 安装

Install dependencies:  
安装依赖：

```bash
pip install -r requirements.txt
```

## Quick start / 快速开始

Run the demo:  
运行 demo：

```bash
python examples/demo_pipeline.py
```

Run tests:  
运行测试：

```bash
pytest -q
```

Expected output:  
预期输出包括：

- error type / 错误类型
- retrieved notebook(s) / 命中的 notebook
- suggested fix / 建议修复路径
- verification checklist / 验证清单

---

## Repository structure / 仓库结构

- `skill/` — original skill-oriented protocol materials  
  `skill/` —— 原始 skill 协议材料
- `docs/` — architecture + protocol  
  `docs/` —— 架构与协议说明
- `error_memory/` — minimal runnable pipeline  
  `error_memory/` —— 最小可运行闭环
- `errors/` — categorized notebooks  
  `errors/` —— 分类后的错误 notebook
- `examples/` — runnable examples  
  `examples/` —— 可运行示例
- `tests/` — basic tests  
  `tests/` —— 基础测试
- `memory/` — action log output  
  `memory/` —— action log 输出位置

---

## Included notebooks / 当前已包含的 notebook

- `errors/api_call/api_key_missing.md`
- `errors/file_io/path_not_found.md`
- `errors/web_scraping/page_loaded_but_no_data.md`
- `errors/logic/wrong_branch.md`

---

## Trigger policy / 触发策略

- Default: **post-error first**  
  默认：**先处理已发生错误**
- Preflight only for high silent-failure-risk tasks  
  仅对高静默失败风险任务做 preflight

Examples include:  
这类任务包括：
- config changes / 配置修改
- cron or delivery routing / cron 或投递路由
- scraping and browser extraction / 抓取与浏览器抽取

---

## Next priorities / 下一步重点

1. Add 10+ real failure cases  
   增加 10+ 个真实失败案例
2. Improve notebook retrieval quality  
   提升 notebook 检索质量
3. Add metrics such as repeat failure rate and verification coverage  
   增加重复失败率、验证覆盖率等指标
4. Add one real OpenClaw integration demo  
   增加一个真实 OpenClaw 接入 demo

---

## License / 许可证

MIT
