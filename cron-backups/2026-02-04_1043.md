# OpenClaw 定时任务备份
# 备份时间: 2026-02-04 10:16
# 说明: 服务重启后若定时任务丢失，可使用此配置快速恢复

## 任务列表

### 1. 每日天气推送
- **ID**: 671babb0-2259-40b2-94d5-dd6a7a0767b3
- **名称**: daily_weather_guangzhou
- **时间**: 0 8 * * * (每天08:00)
- **命令**:
```bash
/tmp/img_venv/bin/python3 skills/email/send_weather.py Zengcheng,Guangzhou,Guangdong 2622011721@qq.com
```

### 2. Appmedia 监控 - 早班
- **ID**: 82d3e0e4-1bc3-4c5f-8c77-b80e32e754c1
- **名称**: appmedia_monitor_08
- **时间**: 0 8 * * * (每天08:00)
- **命令**:
```bash
/tmp/img_venv/bin/python3 skills/web_scraper/appmedia_monitor.py
```

### 3. Appmedia 监控 - 午班
- **ID**: d228f8f2-6d33-41ad-83ac-a706f08330a6
- **名称**: appmedia_monitor_13
- **时间**: 0 13 * * * (每天13:00)
- **命令**:
```bash
/tmp/img_venv/bin/python3 skills/web_scraper/appmedia_monitor.py
```

### 4. Appmedia 监控 - 晚班
- **ID**: b9aa6566-809a-4ec8-bdf2-a0d301dffc92
- **名称**: appmedia_monitor_17
- **时间**: 0 17 * * * (每天17:00)
- **命令**:
```bash
/tmp/img_venv/bin/python3 skills/web_scraper/appmedia_monitor.py
```

### 5. Appmedia 监控 - 夜班
- **ID**: d107cde0-937f-4c20-82d2-3ab11ead7814
- **名称**: appmedia_monitor_21
- **时间**: 0 21 * * * (每天21:00)
- **命令**:
```bash
/tmp/img_venv/bin/python3 skills/web_scraper/appmedia_monitor.py
```

### 6. Gamebase 智能监控
- **ID**: c86ae651-9c7d-4b52-a0cd-a8637267401a
- **名称**: gamebase_smart_monitor
- **时间**: 0 10-23 * * 1-5 (工作日10:00-23:00每小时)
- **命令**:
```bash
/tmp/img_venv/bin/python3 skills/web_scraper/gamebase_smart_monitor.py
```

### 7. 每日 Token 使用报告
- **ID**: 8cb70698-783e-4aa9-a13b-cd8e1921c859
- **名称**: daily_usage_report
- **时间**: 0 19 * * * (每天19:00)
- **说明**: 自动检查 session 状态并发送 Token 使用报告

### 8. 每日知识库推送
- **ID**: 15a431c4-e4ac-4bcd-94b4-269f418fb725
- **名称**: daily_knowledge_push
- **时间**: 0 0 * * * (每天00:00)
- **说明**: 总结当日经验教训并推送到知识库

## 快速恢复命令

如果定时任务丢失，执行以下命令快速恢复:

```bash
# 天气推送
openclaw cron add --name "daily_weather_guangzhou" --schedule "0 8 * * *" --command "/tmp/img_venv/bin/python3 skills/email/send_weather.py Zengcheng,Guangzhou,Guangdong 2622011721@qq.com"

# Appmedia 监控 (08,13,17,21)
openclaw cron add --name "appmedia_monitor_08" --schedule "0 8 * * *" --command "/tmp/img_venv/bin/python3 skills/web_scraper/appmedia_monitor.py"
openclaw cron add --name "appmedia_monitor_13" --schedule "0 13 * * *" --command "/tmp/img_venv/bin/python3 skills/web_scraper/appmedia_monitor.py"
openclaw cron add --name "appmedia_monitor_17" --schedule "0 17 * * *" --command "/tmp/img_venv/bin/python3 skills/web_scraper/appmedia_monitor.py"
openclaw cron add --name "appmedia_monitor_21" --schedule "0 21 * * *" --command "/tmp/img_venv/bin/python3 skills/web_scraper/appmedia_monitor.py"

# Gamebase 智能监控
openclaw cron add --name "gamebase_smart_monitor" --schedule "0 10-23 * * 1-5" --command "/tmp/img_venv/bin/python3 skills/web_scraper/gamebase_smart_monitor.py"
```

## 任务汇总

| 时间 | 任务 | 类型 |
|------|------|------|
| 00:00 | daily_knowledge_push | 系统 |
| 08:00 | daily_weather_guangzhou | 天气 |
| 08:00 | appmedia_monitor_08 | 游戏监控 |
| 10:00-23:00(每小时) | gamebase_smart_monitor | 游戏监控 |
| 13:00 | appmedia_monitor_13 | 游戏监控 |
| 17:00 | appmedia_monitor_17 | 游戏监控 |
| 19:00 | daily_usage_report | 系统 |
| 21:00 | appmedia_monitor_21 | 游戏监控 |

---
**最后更新**: 2026-02-04 10:16
**更新者**: 小秘书 💼