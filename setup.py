#!/usr/bin/env python3
"""
Second Brain Kit — Setup Script
Creates vault folder structure and initializes personal config files.
Run once after cloning the repo.
"""

import os
import shutil
from datetime import date

VAULT = os.path.dirname(os.path.abspath(__file__))
TODAY = date.today().isoformat()


def create_dir(path):
    os.makedirs(path, exist_ok=True)


def copy_template(src, dst):
    if not os.path.exists(dst):
        shutil.copy2(src, dst)
        print(f"  ✓ Created {os.path.relpath(dst, VAULT)}")
    else:
        print(f"  · Skipped {os.path.relpath(dst, VAULT)} (already exists)")


def write_file(path, content):
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(content)
        print(f"  ✓ Created {os.path.relpath(path, VAULT)}")
    else:
        print(f"  · Skipped {os.path.relpath(path, VAULT)} (already exists)")


def main():
    print("\n=== Second Brain Kit — Setup ===\n")

    # ── 1. Personal config files ──────────────────────────────────────────
    print("📄 Personal config files:")
    copy_template(
        os.path.join(VAULT, "Secretary.template.md"),
        os.path.join(VAULT, "Secretary.md"),
    )
    copy_template(
        os.path.join(VAULT, "Me.template.md"),
        os.path.join(VAULT, "Me.md"),
    )

    # ── 2. Folder structure ───────────────────────────────────────────────
    print("\n📁 Folder structure:")
    dirs = [
        "Projects/_example-project",
        "Areas/_example-area",
        "Journal/Daily",
        "Journal/Weekly-Review",
        "wiki/sources",
        "wiki/entities",
        "wiki/concepts",
        "wiki/analyses",
        "raw/assets",
    ]
    for d in dirs:
        full = os.path.join(VAULT, d)
        create_dir(full)
        print(f"  ✓ {d}/")

    # ── 3. Wiki foundation files ──────────────────────────────────────────
    print("\n📚 Wiki foundation:")
    write_file(
        os.path.join(VAULT, "wiki/index.md"),
        f"""---
title: "Wiki Index"
type: index
updated: {TODAY}
---

# Wiki Index

_Last updated: {TODAY} — 0 sources · 0 entity pages · 0 concept pages · 0 analyses_

## Sources
| Slug | Title | Date | Format | Tags |
|------|-------|------|--------|------|

## Entities
| Page | One-line summary |
|------|-----------------|

## Concepts
| Page | One-line summary |
|------|-----------------|

## Analyses
| Page | Summary | Date |
|------|---------|------|
""",
    )
    write_file(
        os.path.join(VAULT, "wiki/log.md"),
        f"""---
title: "Activity Log"
type: log
---

# Activity Log

_Append-only. Parse with: `grep "^## \\[" wiki/log.md | tail -10`_

---

## [{TODAY}] init | Vault initialized
- Setup script ran — folder structure ready
- Status: ready for first ingest
""",
    )
    write_file(
        os.path.join(VAULT, "wiki/overview.md"),
        f"""---
title: "Wiki Overview"
type: overview
updated: {TODAY}
---

# Wiki Overview

_High-level synthesis of all wiki knowledge. Updated by wiki agent after significant ingests._

## Themes

_(none yet — start by ingesting your first source)_
""",
    )

    # ── 4. Example files ──────────────────────────────────────────────────
    print("\n💡 Example files (to show structure):")
    copy_template(
        os.path.join(VAULT, "system/examples/example_area_state.md"),
        os.path.join(VAULT, "Areas/_example-area/state-_example-area.md"),
    )
    copy_template(
        os.path.join(VAULT, "system/examples/example_project_state.md"),
        os.path.join(VAULT, "Projects/_example-project/state-_example-project.md"),
    )
    copy_template(
        os.path.join(VAULT, "system/templates/daily-note-template.md"),
        os.path.join(VAULT, "Journal/Daily/_template.md"),
    )

    # ── 5. current-state.md ───────────────────────────────────────────────
    write_file(
        os.path.join(VAULT, "Journal/current-state.md"),
        f"""---
title: "Current State"
updated: {TODAY}
note: updated by Journal Agent after weekly review — do not edit manually
---

# Current State

## 🏠 Life Ops
- Habits: —
- Finance: —

## 🚀 Projects
- —

## 📚 Knowledge
- —

## 🔧 Second Brain
- Phase: Setup — just initialized

## 🔴 Open Loops
1. Fill in Me.md with your profile
2. Fill in Secretary.md with your routing preferences
3. Run your first daily journal entry (/journal)
""",
    )

    # ── Done ──────────────────────────────────────────────────────────────
    print("""
=== Setup complete ✓ ===

Next steps:
  1. Open Me.md — fill in your profile
  2. Open Secretary.md — customize domain routing for your life areas
  3. Open this vault in Obsidian
  4. Open Claude Code (or Claude Desktop) — your agent is ready

Your vault is private. Only the framework files are tracked by git.
Personal files (Me.md, Secretary.md, Journal/, wiki/sources/, etc.) are gitignored.
""")


if __name__ == "__main__":
    main()
