# Error Notebook Protocol / 错题本协议

## Core Protocol / 核心协议

### 1. When to Trigger / 何时触发
- Default: **post-error first**  
  默认：**先处理已发生错误（post-error first）**
- Use preflight only for high silent-failure-risk tasks:  
  仅在高静默失败风险任务中做 preflight：
  - config / provider / model changes  
    config / provider / model 变更
  - cron / delivery / routing  
    cron / delivery / routing 相关任务
  - scraping / browser extraction  
    scraping / browser extraction 相关任务

### 2. Execution Steps / 执行步骤
1. Take raw error text as input  
   输入原始错误文本
2. Classify it into an error domain  
   将其分类到错误域
3. Retrieve top-k historical notebooks  
   检索 top-k 历史 notebook
4. Extract Fix / Verification from the best notebook  
   从最佳 notebook 中提取 Fix / Verification
5. Output a suggested recovery path  
   输出建议修复路径
6. Append the action to `memory/action_log.md`  
   将本次动作写入 `memory/action_log.md`

### 3. Verification Rules / 验证规则
A fix is not complete just because a command stopped erroring.  
修复不能因为“命令不报错了”就算完成。

At least one explicit verification item is required:  
至少需要一个显式验证项：
- state check  
  状态检查
- output existence check  
  输出存在性检查
- content relevance check  
  内容相关性检查
- manual confirmation (when automatic verification is not possible)  
  手工确认（在无法自动验证时）

### 4. v0.1 Output Object / v0.1 输出对象
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

对应中文理解：
- `error_type`：错误类型
- `retrieved_notebooks`：命中的历史 notebook
- `suggested_fix`：建议修复路径
- `verification`：必须执行的验证项

## Non-goals / 非目标
- Not a promise to auto-fix everything  
  不承诺自动修复一切错误
- Not a promise of exact root-cause diagnosis  
  不承诺给出精确根因分析
- Not a complex agent orchestration system in v0.1  
  不在 v0.1 中扩展成复杂 agent orchestration 系统
