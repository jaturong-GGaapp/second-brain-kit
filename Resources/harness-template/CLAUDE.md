# CLAUDE.md — Agent Harness Config

> [!note] วิธีใช้
> ไฟล์นี้คือ primary harness config — Claude Code อ่านทุก session
> อย่า rename หรือ move `.claude/` files — paths ถูก hardcode ไว้
> อย่า rename `Agents.md` ผ่าน Obsidian — จะทำลาย symlink

---

## Identity

คุณคือ **coding agent** สำหรับ project นี้ — ทำตาม harness rules ด้านล่างทุกครั้ง
รับ task จากผู้ใช้ → route ไป planner → coder → reviewer ตาม pipeline

---

## Session Start Protocol

ทำตามลำดับนี้ทุก session:

1. Read `CLAUDE.md` (this file)
2. Check `.initialized` — ถ้าไม่มี: หยุดและแจ้งผู้ใช้ว่า "run `python setup.py` ก่อน"
3. Read `Agents.md` (symlink → `.claude/agents/index.md`) — โหลด agent catalog
4. Read `wiki/architecture.md` + `wiki/coding_rules.md` — โหลด source of truth
5. Greet ผู้ใช้ + บอก current context (project name + wiki freshness)

---

## Harness Rules

### Done Condition
Task เสร็จเมื่อ **reviewer approve เท่านั้น** — ห้าม declare done ก่อนผ่าน review

### Limits
- **Max turns per task:** 10 (hard limit) — ถ้าเกิน: stop + report ผู้ใช้
- **Max turns per coder subtask:** 5
- **Tool error:** retry 1 ครั้ง → ถ้ายังล้มเหลว → stop + report ผู้ใช้

### Write Permissions
| Layer | Read | Write |
|---|---|---|
| `wiki/` | ✅ ทุก agent | ✅ reviewer เท่านั้น (หลัง approve) |
| `decisions/` | ✅ ทุก agent | ✅ ผู้ใช้ + reviewer |
| `.claude/` | ✅ ทุก agent | ❌ ห้ามแก้ |
| code files | ✅ ทุก agent | ✅ coder เท่านั้น |

### Context Priority Order
เมื่อต้องตัดสินใจหรือเลือก context ให้ใช้ลำดับนี้:
1. `current_task` — งานที่กำลังทำ
2. `related_code` — code ที่เกี่ยวข้อง (grep ก่อน)
3. `architecture_rules` — `wiki/architecture.md`
4. `past_decisions` — `decisions/`

### Fallback
ถ้า uncertain → อ่าน `wiki/` ก่อน → ถ้ายังไม่ชัด → **ถามผู้ใช้** อย่า guess

---

## Agent Pipeline

```
User request
    ↓
[planner] — break into tasks
    ↓
[coder] — implement one task at a time
    ↓
[reviewer] — approve or request-changes
    ↓
Done ✅ (update wiki if new decision)
```

Agent definitions: `.claude/agents/index.md` (accessible via `Agents.md`)

---

## LLM Wiki (Source of Truth)

AI อ่าน wiki/ ก่อนทำงานเสมอ — ไม่ใช่ knowledge base แต่เป็น **context ที่ compile ไว้ให้ AI**

| File | Content |
|---|---|
| `wiki/architecture.md` | Project structure, package boundaries, data flow |
| `wiki/coding_rules.md` | Code style, naming, forbidden patterns |
| `wiki/api_contracts.md` | API endpoints, request/response schemas |
| `wiki/design_system.md` | Animation tokens, colors, spacing |

อัปเดต wiki ผ่าน `/update-wiki` เท่านั้น — ไม่แก้โดยตรง

---

## Directory Structure

```
<project-root>/
├── CLAUDE.md              ← This file (harness config)
├── Agents.md              ← symlink → .claude/agents/index.md
├── wiki/                  ← LLM context (source of truth)
│   ├── architecture.md
│   ├── coding_rules.md
│   ├── api_contracts.md
│   └── design_system.md
├── decisions/             ← Architecture Decision Records
└── .claude/
    ├── agents/            ← planner, coder, reviewer
    ├── commands/          ← /new-feature, /new-decision, /update-wiki
    ├── skills/
    └── settings.json
```

---

## Commands

| Command | Description |
|---|---|
| `/init-wiki` | กรอก wiki ครั้งแรกจาก project context (รันหลัง setup) |
| `/new-feature [name]` | Scaffold feature: planner → task list → coder → reviewer |
| `/new-decision [topic]` | Create ADR สำหรับ architecture decision |
| `/update-wiki` | Sync wiki หลัง implementation มี decision ใหม่ |
