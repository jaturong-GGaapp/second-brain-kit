# Agent Harness Template

> infrastructure ที่ wrap Claude Code — กำหนดว่า agent ทำอะไรได้บ้าง, context อะไรเข้าถึงได้, "เสร็จ" คือเมื่อไหร่

## Quick Start

```bash
cd /path/to/your-project
python /path/to/harness-template/setup.py
```

แล้วกรอก `wiki/` files → เปิด Claude Code → พร้อมใช้งาน

---

## โครงสร้างที่ได้หลัง setup

```
your-project/
├── CLAUDE.md              ← harness config (Claude อ่านทุก session)
├── Agents.md              ← symlink → .claude/agents/index.md
│
├── wiki/                  ← LLM context: AI อ่านก่อนทำงานเสมอ
│   ├── architecture.md    ← project structure + package boundaries
│   ├── coding_rules.md    ← code style + forbidden patterns
│   ├── api_contracts.md   ← API schemas
│   └── design_system.md   ← tokens + animation system
│
├── decisions/             ← Architecture Decision Records
│   └── ADR-000-template.md
│
└── .claude/
    ├── agents/            ← planner, coder, reviewer
    ├── commands/          ← /new-feature, /new-decision, /update-wiki
    ├── skills/
    └── settings.json
```

---

## Agent Pipeline

```
User request
    ↓
[planner]  break request → numbered task list
    ↓
[coder]    implement one task at a time
    ↓
[reviewer] approve ✅ or request-changes ❌
    ↓
Done — reviewer updates wiki if new decision
```

### Guardrails

| Agent | Write permission |
|---|---|
| planner | ห้าม implement ใดๆ — output plan เท่านั้น |
| coder | code files เท่านั้น — ห้ามแก้ `wiki/`, `decisions/`, `.claude/` |
| reviewer | approve → อัปเดต `wiki/` ได้ |

---

## Commands

| Command | Description |
|---|---|
| `/init-wiki` | กรอก wiki ครั้งแรก — paste project context แล้ว AI กรอกให้ |
| `/new-feature [name]` | scaffold feature ผ่าน full pipeline |
| `/new-decision [topic]` | สร้าง ADR ใหม่ |
| `/update-wiki` | sync wiki หลัง implementation มี decision ใหม่ |

---

## หลัง setup: 3 ขั้นตอน

### 1. ตรวจสอบ symlink

```bash
ls -la Agents.md
# ควรแสดง: Agents.md -> .claude/agents/index.md
```

### 2. เปิด Claude Code แล้วรัน `/init-wiki`

```bash
claude  # จาก project root
```

แล้วพิมพ์ `/init-wiki` — AI จะขอให้ paste project context (README, tech stack, structure ฯลฯ) แล้วกรอก wiki files ทั้ง 4 ให้อัตโนมัติ

### 3. เริ่ม build

```
/new-feature [feature-name]
```

---

## Harness Rules สรุป

- **Done condition:** reviewer approve เท่านั้น
- **Max turns:** 10 turns/task (hard limit)
- **Tool error:** retry 1 → stop + report
- **Context priority:** `current_task` → `related_code` → `architecture_rules` → `past_decisions`
- **Fallback:** uncertain → อ่าน wiki → ถ้ายังไม่ชัด → ถามผู้ใช้

---

## คำเตือน

> อย่า rename `Agents.md` ผ่าน Obsidian — จะทำลาย symlink  
> อย่าแก้ไฟล์ใน `.claude/` โดยตรงระหว่าง session — แก้ที่ template แล้วรัน setup.py ใหม่
