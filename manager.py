import os
import json
import subprocess
import datetime

WORKSPACE = "/root/.openclaw/workspace"
KB_PATH = os.path.join(WORKSPACE, "skills/knowledge_base")
CRON_BACKUP = os.path.join(KB_PATH, "cron-backups/latest.md")
EXPERIENCE_FILE = os.path.join(KB_PATH, "experience.md")

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def backup_cron():
    """将当前的 cron 任务导出为 Markdown 备份"""
    print("正在备份 Cron 任务...")
    jobs_json = run_command("openclaw cron list")
    try:
        jobs = json.loads(jobs_json).get("jobs", [])
        content = f"# OpenClaw 定时任务备份\n# 备份时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        content += "| 名称 | 频率 | 类型 | 目标 |\n| --- | --- | --- | --- |\n"
        
        for job in jobs:
            schedule = job.get("schedule", {}).get("expr", "N/A")
            payload_kind = job.get("payload", {}).get("kind", "N/A")
            target = job.get("sessionTarget", "N/A")
            content += f"| {job.get('name')} | `{schedule}` | {payload_kind} | {target} |\n"
        
        # 保存原始 JSON 供恢复使用
        raw_json_path = os.path.join(KB_PATH, "cron-backups/raw_jobs.json")
        with open(raw_json_path, 'w') as f:
            json.dump(jobs, f, indent=2)
            
        with open(CRON_BACKUP, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"备份失败: {e}")
        return False

def restore_cron():
    """检查并恢复丢失的 Cron 任务 (自愈逻辑)"""
    print("正在检查 Cron 任务完整性...")
    raw_json_path = os.path.join(KB_PATH, "cron-backups/raw_jobs.json")
    if not os.path.exists(raw_json_path):
        return "没有找到备份文件"

    current_jobs_json = run_command("openclaw cron list")
    current_names = [j.get("name") for j in json.loads(current_jobs_json).get("jobs", [])]
    
    with open(raw_json_path, 'r') as f:
        saved_jobs = json.load(f)
    
    restored = []
    for job in saved_jobs:
        if job.get("name") not in current_names:
            # 构建恢复命令 (简单起见，这里我们记录需要恢复的任务)
            restored.append(job.get("name"))
            # 注意：实际恢复由于涉及复杂 Payload，通常建议由 AI 调用 cron add
            
    return restored

def sync_to_github(msg="Auto-sync knowledge base"):
    """立即同步到 GitHub"""
    print(f"正在同步知识库: {msg}")
    os.chdir(KB_PATH)
    run_command("git add .")
    run_command(f'git commit -m "{msg}"')
    run_command("git push origin main")

def log_experience(category, title, content):
    """结构化记录经验"""
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = f"\n### [{category}] {title} ({now})\n{content}\n"
    with open(EXPERIENCE_FILE, 'a') as f:
        f.write(entry)
    print(f"已记录经验: {title}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "backup":
            backup_cron()
        elif action == "sync":
            sync_to_github(sys.argv[2] if len(sys.argv) > 2 else "Manual sync")
        elif action == "restore":
            print(restore_cron())
