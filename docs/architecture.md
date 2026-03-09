# Error Notebook v0.1 Architecture / 错题本 v0.1 架构

## Positioning / 定位
Error Notebook is not a self-healing system, and it is not a large all-in-one agent framework.  
Error Notebook 不是自动自愈系统，也不是大而全的 agent 框架。

It is an **Agent Error Governance Starter Kit**:  
它是一个 **Agent Error Governance Starter Kit（错误治理入门工具包）**：
turning failures into retrievable, verifiable, and reusable recovery assets.  
把失败变成可检索、可验证、可复用的修复资产。

Core loop / 核心闭环：

```text
error input
  -> classify
  -> retrieve similar notebook(s)
  -> suggest fix path
  -> explicit verification checklist
  -> append action trace
```

```text
错误输入
  -> 分类
  -> 检索相似 notebook
  -> 给出修复路径
  -> 显式验证清单
  -> 记录 action trace
```

## v0.1 Scope / v0.1 范围
This version only does four things:  
本版本只做四件事：

1. Error classification (rule-based)  
   错误分类（基于规则）
2. Notebook retrieval (minimal keyword / BM25-style retrieval)  
   notebook 检索（最小关键词 / BM25 风格实现）
3. Extract Fix / Verification from a notebook  
   从 notebook 中提取 Fix / Verification
4. Record action trace  
   记录 action trace

## Non-goals / 明确不做的事
This version explicitly does **not** do:  
当前版本明确**不做**：
- knowledge graph  
  知识图谱
- clustering  
  聚类归纳
- vector DB  
  向量数据库
- adaptive policy learning  
  自适应策略学习
- automatic high-risk repair  
  自动高风险修复

## Directory Layout / 目录结构

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

## Design Principles / 设计原则
- **post-error first**: solve real failures before building bigger systems  
  **post-error first**：先解决真实失败，再谈更大的系统
- **verification mandatory**: every fix must include explicit verification  
  **verification mandatory**：每次修复都必须包含显式验证
- **starter kit, not framework**: stay light, stable, and runnable first  
  **starter kit, not framework**：先轻、先稳、先能跑
- **real cases over abstract architecture**: prioritize real cases over future blueprints  
  **real cases over abstract architecture**：真实案例优先于未来蓝图

## Success Criteria / 成功标准
The success criterion for v0.1 is simple:  
v0.1 的成功标准很简单：

```bash
python examples/demo_pipeline.py
```

It should produce:  
它应该能跑出：
- error type  
  错误类型
- retrieved notebook  
  命中的 notebook
- suggested fix  
  建议修复路径
- verification checklist  
  验证清单
- appended action log  
  已追加的 action log

If this loop is real, the project is no longer just a template collection — it is a runnable system.  
只要这条闭环是真的，这个项目就不再只是模板集合，而是一个可运行系统。
