# Error Notebook Protocol

## 核心协议

### 1. 何时触发
- 默认：**post-error first**
- 仅在高静默失败风险任务中做 preflight：
  - config / provider / model 改动
  - cron / delivery / routing
  - scraping / browser extraction

### 2. 执行步骤
1. 输入原始错误文本
2. 分类到错误域
3. 检索 top-k 历史 notebook
4. 提取最佳 notebook 的 Fix / Verification
5. 输出建议修复路径
6. 将本次动作写入 `memory/action_log.md`

### 3. 验证规则
修复不能只看“命令没报错”，至少要有一个显式验证项：
- 状态检查
- 输出存在性检查
- 内容相关性检查
- 手工确认（在无法自动验证时）

### 4. v0.1 输出对象
```json
{
  "error_type": "api_call",
  "retrieved_notebooks": ["errors/api_call/api_key_missing.md"],
  "suggested_fix": "Set OPENAI_API_KEY or switch to a provider with valid auth.",
  "verification": [
    "Check OPENAI_API_KEY is present",
    "Run a minimal request and confirm real response"
  ]
}
```

## 非目标
- 不承诺自动修复一切错误
- 不承诺精确根因分析
- 不在 v0.1 里做复杂 agent orchestration
