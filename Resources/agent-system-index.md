---
title: "Agents & Skills"
type: reference
updated: 2026-05-05
---

# Agents & Skills

## File Structure

```
Personal Brain/
├── Me.md                          ← Profile (source of truth)
├── CLAUDE.md                      ← Wiki agent instructions
├── Resources/
│   └── agent-system-index.md      ← ไฟล์นี้ (human-facing architecture doc)
└── .claude/                       ← Single source of truth (Anthropic official)
    ├── agents/                    ← agent prompt files
    │   ├── secretary.md
    │   ├── wiki-agent.md
    │   ├── journal-agent.md
    │   └── skill-optimizer.md
    ├── commands/                  ← slash commands
    │   ├── journal.md
    │   ├── session-to-wiki.md
    │   ├── deep-wiki-ingest.md
    │   ├── weekly-review.md
    │   ├── skill-optimizer.md
    │   ├── new-claude-project.md
    │   ├── sync-claude-project.md
    │   └── archive-project.md    (TODO)
    ├── hooks/                     ← pre-commit hook
    └── skills/                   ← skill library (index.md = operational catalog)
        ├── shared/                ← ใช้ได้หลาย agent
        │   ├── roi-analyzer.md
        │   ├── para-router.md
        │   ├── grill-with-docs/
        │   ├── obsidian-markdown/
        │   ├── webapp-testing/
        │   └── creating-financial-models/
        ├── journal-agent/         (daily-capture, reflect, export-to-obsidian)
        ├── secretary/             (intent-analysis, worker-routing, delivery)
        └── skill-optimizer/       (survey, diagnose, recommend)
```

**Operational index (Claude-facing):** `.claude/skills/index.md`

---

## Architecture

```
User
 ↓
Secretary Agent  ←──── Skill Optimizer (ปรับ routing policy)
                                ↑
                   (ปรับ skill library)
```

> Worker agents สร้างเมื่อต้องการจริงๆ — ไม่ pre-create เพื่อประหยัด context

---

## Agents

### Secretary
**File:** `.claude/agents/secretary.md`
**Role:** รับทุก request → อ่าน Me.md → route ไป worker ที่ถูก → aggregate ผลกลับ
**Lenses:** intent-analysis, worker-routing, delivery

### Wiki Agent
**File:** `CLAUDE.md` (โหลดอัตโนมัติทุก session)
**Role:** INGEST / QUERY / LINT บน `wiki/` layer — ไม่ต้อง invoke

### Journal Agent
**File:** `.claude/agents/journal-agent.md`
**Role:** Daily FWIM interview + patch `current-state.md`
**Lenses:** daily-capture, reflect, export-to-obsidian

### Skill Optimizer
**File:** `.claude/agents/skill-optimizer.md`
**Role:** ปรับปรุง Skill Library และ routing policy — ไม่ execute งาน แต่ทำให้ระบบดีขึ้น
**Trigger:** "optimize skills", "review system", "improve agent", "skill ซ้ำ", "ระบบช้า"

---

## Commands

| Command | Trigger | หน้าที่ |
|---------|---------|---------|
| `/journal` | `/journal` | Daily FWIM interview → export to Obsidian |
| `/session-to-wiki` | `/session-to-wiki`, "เก็บ session" | Ingest Claude.ai session → wiki |
| `/deep-wiki-ingest` | `/deep-wiki-ingest`, "deep ingest" | Ingest raw source → wiki (ละเอียด) |
| `/weekly-review` | `/weekly-review` | Weekly synthesis + update state files |
| `/skill-optimizer` | `/skill-optimizer` | Survey → diagnose → recommend skill changes |
| `/sync-claude-project` | `/sync-claude-project` | Sync knowledge files ใน Resources/claude-ai/ ให้ตรงกับ vault state |
| `/new-claude-project [name]` | `/new-claude-project [name]` | Scaffold Claude.ai workspace ใหม่สำหรับ project ใน Projects/ |
| `/archive-project [name]` | `/archive-project [name]` | ย้าย project เสร็จแล้ว → Archive/ (TODO) |

---

## Memory Architecture

| ไฟล์ | ขนาด | ใครอ่าน | หน้าที่ |
|---|---|---|---|
| `Journal/current-state.md` | เล็ก (<30 บรรทัด) | Secretary ทุก session | Agent context — ภาพรวมปัจจุบันของทุก dept |
| `Areas/*/state-*.md` | ละเอียด | Weekly Review | รายละเอียดต่อ area |
| `Projects/*/state-*.md` | ละเอียด | Weekly Review | รายละเอียดต่อ project |

**Update flow:**
```
Daily Notes (7 วัน)
      ↓ /weekly-review
current-state.md  ← เขียนทับ (ภาพรวม)
Areas/*/state-*.md  ← อัปเดต section ที่เกี่ยวข้อง
Projects/*/state-*.md ← อัปเดต section ที่เกี่ยวข้อง
```

---

## Shared Skills

| Skill | ใช้โดย |
|---|---|
| obsidian-markdown | journal-agent, session-to-wiki, deep-wiki-ingest, weekly-review |
| para-router | secretary (domain routing reference) |
| roi-analyzer | general purpose — ROI calculations |
| grill-with-docs | document analysis |
| webapp-testing | webapp QA |
| creating-financial-models | finance / sensitivity analysis |

---

_Source of truth สำหรับ Claude: `.claude/skills/index.md`_
