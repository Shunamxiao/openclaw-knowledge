# 💼 小秘书技术笔记 (Technical Memory)
> 目标：拒绝失忆，积累经验，极致避坑。

## ⚙️ [Config] 核心配置

### 配置文件规范 (来自官方文档)
- **配置路径**: `~/.openclaw/openclaw.json` (JSON5 格式，支持注释和尾逗号)
- **严格验证**: OpenClaw 只接受完全匹配 schema 的配置，未知键/错误类型会导致网关拒绝启动
- **修改方式**:
  - `config.patch`: 部分更新 (推荐，只改需要的键)
  - `config.apply`: 全量替换 (危险，会覆盖整个配置)
  - 手动编辑后必须 `gateway restart`
- **诊断命令**: `openclaw doctor` 查看配置问题，`openclaw doctor --fix` 自动修复

### 模型配置结构
```json
{
  "auth": {
    "profiles": {
      "provider:profile-name": {
        "provider": "provider-name",
        "mode": "api_key",
        "apiKey": "sk-xxx"  // 可选，也可用环境变量
      }
    }
  },
  "models": {
    "providers": {
      "provider-name": {
        "baseUrl": "https://api.example.com",
        "apiKey": "provider:profile-name",  // 引用 auth profile
        "api": "openai-completions | anthropic-messages",
        "models": [...]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": { "primary": "provider/model-id" },
      "models": { "provider/model-id": { "alias": "shortname" } }
    }
  }
}
```

### 已验证的配置
- **Claude (MMKG代理)**: `api: "anthropic-messages"`, baseUrl: `https://code.mmkg.cloud` (无/v1)
- **Kimi**: `api: "openai-completions"`, baseUrl: `https://api.moonshot.cn/v1`
- **OpenRouter**: `api: "openai-completions"`, baseUrl: `https://openrouter.ai/api/v1`
- **SMTP**: QQ 邮箱授权码 (16位)，发件人：`🎃提醒小助手`
- **Python 环境**: `/tmp/img_venv/bin/python3`

## ⚠️ [Bugfix] 避坑指南

### 配置相关
- **网关卡死**: 配置格式错误会导致网关拒绝启动。修改前先备份，出问题用 `openclaw doctor` 诊断
- **404 错误**: API 格式 (`api` 字段) 选错或 baseUrl 路径错误
- **JSON 解析**: `edit` 工具对空格敏感，大改动用 `write` 重写整个文件更安全
- **权限问题**: 修改配置后必须 `gateway restart` 才生效

### 运维相关
- **Cron 丢失**: 网关重启后任务可能清空。对策：保留 `cron-backups/latest.md` 备份
- **环境丢失**: `/tmp` 目录重启后可能清空，虚拟环境需要重建

## 🛠️ [Skill] 技能备忘
- **智能监控**: `gamebase_smart_monitor.py` 依赖关键词（上市/公测/周年）
- **自愈脚本**: `manager.py` 负责备份 Cron
- **qmd 语义搜索**: 本地运行，索引在 `~/.cache/qmd/`

## 🤖 [Multi-Agent] 多 Agent 架构 (2026-02-05)

### 架构设计
- **职责分离**: 不同 Agent 处理不同类型任务
- **成本优化**: 简单任务用免费/低成本模型，复杂任务用高级模型
- **独立空间**: 各 Agent 有独立的工作空间和记忆

### Agent 配置结构
```json
// agents.list 中定义
{
  "id": "monitor",
  "name": "资讯监控员",
  "workspace": "/root/.openclaw/workspace-monitor",
  "model": {
    "primary": "kimi-coding/k2p5",
    "fallbacks": ["qwen-portal/coder-model"]
  },
  "identity": { "name": "资讯监控员", "emoji": "📡" }
}
```

### 群组绑定 (bindings)
```json
{
  "agentId": "monitor",
  "match": {
    "channel": "telegram",
    "peer": { "kind": "group", "id": "-1003312777824" }
  }
}
```

### 群组配置 (channels.telegram.groups)
```json
{
  "-1003312777824": {
    "enabled": true,
    "requireMention": false,
    "systemPrompt": "你是 资讯监控员 📡..."
  }
}
```

### CLI 命令
```bash
# 添加 Agent
openclaw agents add <id> --workspace <dir> --model <model> --bind "telegram:<group>" --non-interactive

# 设置身份
openclaw agents set-identity --agent <id> --name "名称" --emoji "🎯"

# 列出 Agent
openclaw agents list --json
```

### 当前 Agent 列表
| Agent | 身份 | 模型 | 绑定 |
|-------|------|------|------|
| main | 💼 小秘书 | Claude Opus | 默认 |
| monitor | 📡 资讯监控员 | Kimi K2.5 | 群组 -1003312777824 |

## 📡 [Monitor] 监控脚本优化 (2026-02-05)

### 脚本简化原则
- **移除邮件推送**: 所有结果通过 Telegram 群组推送
- **纯输出模式**: 脚本只 `print()` 输出，OpenClaw 捕获并推送
- **移除冗余依赖**: 不再需要 telegram_notify 模块的直接发送功能

### 翻译 API
- **MyMemory**: 免费但有日配额限制 (约1000次/天)
- **配额用完**: 返回 429 错误，17小时后恢复
- **降级处理**: 翻译失败时返回原文

### Telegram Bot Token
- **更新方式**: 通过 `config.patch` 更新 `channels.telegram.botToken`
- **验证**: `curl https://api.telegram.org/bot<token>/getMe`
- **401 错误**: Token 已失效，需要从 @BotFather 获取新 token
