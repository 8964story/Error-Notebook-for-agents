# Error Notebook v0.1 Architecture

## 定位
Error Notebook 不是自动自愈系统，也不是大而全 agent 框架。

它是一个 **Agent Error Governance Starter Kit**：
把失败变成可检索、可验证、可复用的修复资产。

核心闭环：

```text
error input
  -> classify
  -> retrieve similar notebook(s)
  -> suggest fix path
  -> explicit verification checklist
  -> append action trace
```

## v0.1 范围
本版本只做四件事：

1. 错误分类（rule-based）
2. notebook 检索（关键词/BM25 风格的最小实现）
3. 从 notebook 中抽取 Fix / Verification
4. 记录 action trace

## 不做的事
当前版本明确不做：
- knowledge graph
- clustering
- vector DB
- adaptive policy learning
- 自动高风险修复

## 目录结构

```text
错题本-error-notebook/
├─ README.md
├─ docs/
│  ├─ architecture.md
│  └─ protocol.md
├─ error_memory/
│  ├─ __init__.py
│  ├─ classifier.py
│  ├─ retrieval.py
│  ├─ parser.py
│  ├─ logger.py
│  └─ pipeline.py
├─ errors/
│  ├─ api_call/
│  ├─ file_io/
│  ├─ web_scraping/
│  └─ logic/
├─ memory/
│  └─ action_log.md
├─ examples/
│  ├─ sample_errors.json
│  └─ demo_pipeline.py
└─ tests/
   ├─ test_classifier.py
   ├─ test_retrieval.py
   └─ test_pipeline.py
```

## 设计原则
- **post-error first**：先解决真实失败，再谈更大系统
- **verification mandatory**：修复后必须给显式验证
- **starter kit, not framework**：先轻、先稳、先能跑
- **real cases over abstract architecture**：真实案例优先于未来蓝图

## 成功标准
v0.1 的成功标准只有一个：

```bash
python examples/demo_pipeline.py
```

能跑出：
- error type
- retrieved notebook
- suggested fix
- verification checklist
- appended action log

只要这一条链是真的，项目就不是“模板集合”，而是可运行系统。
