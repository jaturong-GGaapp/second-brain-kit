#!/usr/bin/env python3
"""
Agent Harness Setup Script
รัน: python setup.py
จาก directory ที่ต้องการติดตั้ง harness

Idempotent — รันซ้ำได้ (skip ไฟล์ที่มีอยู่แล้ว)
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import date

# ========================================
# Config
# ========================================

TEMPLATE_DIR = Path(__file__).parent  # directory ของ setup.py นี้
TARGET_DIR = Path.cwd()               # directory ที่ user รัน setup.py

TODAY = date.today().isoformat()

DIRS_TO_CREATE = [
    ".claude/agents",
    ".claude/commands",
    ".claude/skills",
    "wiki",
    "decisions",
]

FILES_TO_COPY = [
    # (source relative to TEMPLATE_DIR, dest relative to TARGET_DIR)
    ("CLAUDE.md",                               "CLAUDE.md"),
    (".claude/agents/index.md",                 ".claude/agents/index.md"),
    (".claude/agents/planner.md",               ".claude/agents/planner.md"),
    (".claude/agents/coder.md",                 ".claude/agents/coder.md"),
    (".claude/agents/reviewer.md",              ".claude/agents/reviewer.md"),
    (".claude/commands/new-feature.md",         ".claude/commands/new-feature.md"),
    (".claude/commands/new-decision.md",        ".claude/commands/new-decision.md"),
    (".claude/commands/update-wiki.md",         ".claude/commands/update-wiki.md"),
    (".claude/skills/index.md",                 ".claude/skills/index.md"),
    (".claude/settings.json",                   ".claude/settings.json"),
    ("wiki/architecture.md",                    "wiki/architecture.md"),
    ("wiki/coding_rules.md",                    "wiki/coding_rules.md"),
    ("wiki/api_contracts.md",                   "wiki/api_contracts.md"),
    ("wiki/design_system.md",                   "wiki/design_system.md"),
    ("decisions/ADR-000-template.md",           "decisions/ADR-000-template.md"),
    (".claude/commands/init-wiki.md",           ".claude/commands/init-wiki.md"),
]

# ========================================
# Helpers
# ========================================

def log(msg: str):
    print(msg)

def skip(msg: str):
    print(f"  [skip] {msg}")

def created(msg: str):
    print(f"  [+]    {msg}")

def error(msg: str):
    print(f"  [!]    {msg}", file=sys.stderr)

# ========================================
# Steps
# ========================================

def create_dirs():
    log("\n1. Creating directories...")
    for d in DIRS_TO_CREATE:
        target = TARGET_DIR / d
        if target.exists():
            skip(d)
        else:
            target.mkdir(parents=True, exist_ok=True)
            created(d)

def copy_files():
    log("\n2. Copying harness files...")
    for src_rel, dst_rel in FILES_TO_COPY:
        src = TEMPLATE_DIR / src_rel
        dst = TARGET_DIR / dst_rel

        if not src.exists():
            error(f"Template not found: {src_rel}")
            continue

        if dst.exists():
            skip(dst_rel)
        else:
            shutil.copy2(src, dst)
            created(dst_rel)

def create_symlink():
    log("\n3. Creating Agents.md symlink...")
    symlink_path = TARGET_DIR / "Agents.md"
    symlink_target = ".claude/agents/index.md"

    if symlink_path.exists() or symlink_path.is_symlink():
        skip("Agents.md (already exists)")
    else:
        symlink_path.symlink_to(symlink_target)
        created(f"Agents.md -> {symlink_target}")

def create_sentinel():
    log("\n4. Creating .initialized sentinel...")
    sentinel = TARGET_DIR / ".initialized"
    if sentinel.exists():
        skip(".initialized")
    else:
        sentinel.write_text(f"initialized: {TODAY}\n")
        created(".initialized")

def print_summary():
    log("\n" + "=" * 50)
    log("Setup complete!")
    log("=" * 50)
    log(f"\nHarness installed at: {TARGET_DIR}")
    log("\nNext steps:")
    log("  1. Open Claude Code at this directory")
    log("  2. Run /init-wiki — paste your project context, AI fills wiki for you")
    log("  3. Done — start building with /new-feature [name]")
    log("\nVerify symlink:")
    log("  ls -la Agents.md")
    log("  # should show: Agents.md -> .claude/agents/index.md")

# ========================================
# Main
# ========================================

def main():
    log(f"Agent Harness Setup")
    log(f"Template: {TEMPLATE_DIR}")
    log(f"Target:   {TARGET_DIR}")

    if TARGET_DIR == TEMPLATE_DIR:
        error("Running setup.py inside the template directory.")
        error("Copy this setup.py to your project root and run it there.")
        error("Or run: python /path/to/setup.py from your project root.")
        sys.exit(1)

    create_dirs()
    copy_files()
    create_symlink()
    create_sentinel()
    print_summary()

if __name__ == "__main__":
    main()
