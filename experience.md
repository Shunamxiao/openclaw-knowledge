# 💼 小秘书技术笔记 (Technical Memory)
> 目标：拒绝失忆，积累经验，极致避坑。

## ⚙️ [Config] 核心配置
- **Claude (MMKG代理)**: 必须用 `anthropic-messages` 格式，baseUrl 为 `https://code.mmkg.cloud` (无/v1)。原版 ID 切换最稳定。
- **SMTP**: 使用 QQ 邮箱授权码 (16位)，发件人名：`🎃提醒小助手`。
- **环境**: Playwright 位于 `/tmp/img_venv/bin/python3`，执行所有爬虫必须指定此解释器。

## ⚠️ [Bugfix] 避坑指南
- **404 错误**: 发生在模型调用时，通常是 API 格式 (`api` 字段) 选错或 baseUrl 多了 `/v1`。
- **Cron 丢失**: 网关重启后任务会清空。对策：必须保留 `cron-backups/latest.md`，丢失后根据备份重加。
- **JSON 解析**: `edit` 工具对空格极其敏感，重写配置建议直接用 `write`。
- **权限问题**: 修改 `openclaw.json` 后必须重启网关 (`restart`) 才能生效。

## 🛠️ [Skill] 技能备忘
- **智能监控**: `gamebase_smart_monitor.py` 依赖 AI 提取关键词（上市/公测/周年），不要轻易修改判定逻辑。
- **自愈脚本**: `manager.py` 负责手动备份 Cron。
