# 小秘书技能知识库

## 🛠️ 技能清单

### 邮件系统
- **脚本**: `skills/email/send.py`
- **功能**: SMTP邮件发送，发件人🎃提醒小助手
- **配置**: QQ邮箱(3788767702@qq.com)

### 天气推送
- **脚本**: `skills/email/send_weather.py`
- **功能**: 爬取wttr.in发送HTML天气邮件
- **定时**: 08:00 daily

### 游戏监控
| 平台 | 脚本 | 频率 | 推送方式 |
|------|------|------|----------|
| Appmedia | `web_scraper/appmedia_monitor.py` | 08/13/17/21 | 邮件(表格) |
| Gamebase | `web_scraper/gamebase_smart_monitor.py` | 工作日10-23每小时 | 重要邮件/普通聊天 |

### 模型管理
- **脚本**: `model_fallback_manager.py`, `fallback_monitor.py`
- **功能**: 故障自动回退，健康监控

### Token报告
- **脚本**: `token_report.py`
- **定时**: 19:00 daily

---

## ⏰ 定时任务(8个)

```
08:00  daily_weather_guangzhou      # 天气
08:00  appmedia_monitor_08          # Appmedia早
10-23  gamebase_smart_monitor       # Gamebase(工作日每小时)
13:00  appmedia_monitor_13          # Appmedia午
17:00  appmedia_monitor_17          # Appmedia晚
19:00  daily_usage_report           # Token报告
21:00  appmedia_monitor_21          # Appmedia夜
00:00  daily_knowledge_push         # 知识库
```

**备份**: `cron-backups/latest.md`

---

## 🔑 关键配置

### OpenRouter
- **Token**: `sk-or-v1-2046...6c41ee89`
- **模型**: claude-free, gemini-free, llama-free
- **端点**: https://openrouter.ai/api/v1

### Email SMTP
- **账号**: 3788767702@qq.com
- **密码**: ivnciyvkibhjccai (应用专用)

### GitHub
- **仓库**: Shunamxiao/openclaw-knowledge
- **Token**: [查看本地config]

### OpenClaw
- **访问**: http://zaidu.in:18789
- **Token**: `66b003fe6f97d9b533484743a1a0a8d04f393b86e23bd5c7`

---

## 🎯 用户偏好

- **称呼**: 南总
- **语言**: 中文（代码注释也用中文）
- **时区**: Asia/Shanghai
- **邮箱**: 2622011721@qq.com
- **地点**: 广州增城区

---

## 📍 常用路径

```
workspace:     /root/.openclaw/workspace/
config:        /root/.openclaw/openclaw.json
skills:        skills/
email:         skills/email/
scraper:       skills/web_scraper/
knowledge:     skills/knowledge_base/
venv:          /tmp/img_venv/bin/python3
```

---

*更新时间: 2026-02-04 | 精简版 | 检索用*