#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from datetime import datetime
import shutil
import filecmp

SITE_DIR = "/Volumes/01_hard/els-blog/blog_github"
PUBLIC_DIR = os.path.join(SITE_DIR, "public")
MAIN_BRANCH = "main"
DEPLOY_BRANCH = "gh-pages"
REPO = "git@github.com:wjz5788/blog_github.git"

def run(cmd, cwd=None, check=True):
    print(f"👉 {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"❌ 命令失败: {cmd}\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

# -----------------------------
# 步骤 1：同步 main
# -----------------------------
os.chdir(SITE_DIR)
run(f"git checkout {MAIN_BRANCH}")
run(f"git pull origin {MAIN_BRANCH} --rebase")

# -----------------------------
# 步骤 2：生成 Hugo 静态文件
# -----------------------------
run("hugo -D", cwd=SITE_DIR)

# -----------------------------
# 步骤 3：切换 gh-pages
# -----------------------------
branches = run("git branch", cwd=SITE_DIR)
if DEPLOY_BRANCH not in branches:
    run(f"git checkout --orphan {DEPLOY_BRANCH}", cwd=SITE_DIR)
else:
    run(f"git checkout {DEPLOY_BRANCH}", cwd=SITE_DIR)

# -----------------------------
# 步骤 4：逐文件增量更新
# -----------------------------
def copy_if_different(src_dir, dst_dir):
    modified = False
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(src_file, src_dir)
            dst_file = os.path.join(dst_dir, rel_path)

            os.makedirs(os.path.dirname(dst_file), exist_ok=True)

            if not os.path.exists(dst_file) or not filecmp.cmp(src_file, dst_file, shallow=False):
                shutil.copy2(src_file, dst_file)
                modified = True
    return modified

modified = copy_if_different(PUBLIC_DIR, SITE_DIR)

# -----------------------------
# 步骤 5：提交并推送
# -----------------------------
if modified:
    run("git add .", cwd=SITE_DIR)
    COMMIT_MESSAGE = f"自动部署: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run(f'git commit -m "{COMMIT_MESSAGE}"', cwd=SITE_DIR)
    run(f"git push origin {DEPLOY_BRANCH}", cwd=SITE_DIR)
    print("✅ 有修改，已推送 gh-pages")
else:
    print("ℹ️ 没有检测到修改，跳过推送")

# -----------------------------
# 步骤 6：回到 main
# -----------------------------
run(f"git checkout {MAIN_BRANCH}", cwd=SITE_DIR)
