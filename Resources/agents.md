---
title: "Agents & Skills"
type: reference
updated: 2026-04-28
---

# Agents & Skills

## File Structure

```
Personal Brain (private)/          ← Obsidian vault (แก้ไขได้จากที่นี่)
├── Me.md                          ← Profile (source of truth)
├── CLAUDE.md                      ← Wiki agent instructions
└── Resources/
    ├── agents.md                  ← ไฟล์นี้ (index)
    ├── agents/                    ← agent prompt files
    │   ├── health-habits.md
    │   ├── finance-debt.md
    │   ├── journal-agent.md
    │   ├── idea-validator.md
    │   ├── task-tracker.md
    │   ├── land-dev.md
    │   ├── note-organizer.md
    │   ├── learning-research.md
    │   ├── weekly-review.md
    │   └── skill-optimizer.md     ← meta layer
    └── skills/
        ├── inbox/                 ← วาง skill ideas — Skill Optimizer process
        ├── shared/                ← ใช้ได้หลาย agent
        │   ├── roi-analyzer.md
        │   ├── para-router.md
        │   ├── find-skills.md         (conditional — ถาม user ก่อน / user สั่งเท่านั้น)
        │   ├── grill-with-docs/       (SKILL.md, ADR-FORMAT.md, CONTEXT-FORMAT.md)
        │   └── obsidian-markdown/     (SKILL.md, refs: CALLOUTS, EMBEDS, PROPERTIES)
        └── agents/                ← skill ย่อยของแต่ละ agent
            ├── health-habits/     (habit-tracker, streak-calculator)
            ├── finance-debt/      (debt-payoff-calculator, spreadsheet-reader)
            ├── journal-agent/     (pattern-detector)
            ├── idea-validator/    (tam-estimator)
            ├── task-tracker/
            ├── land-dev/          (roi-land-calculator)
            ├── note-organizer/    (link-suggester)
            ├── learning-research/ (web-researcher)
            └── weekly-review/     (focus-setter)

vault/Journal/
└── current-state.md               ← อัปเดตโดย Journal Agent ทุกอาทิตย์
```

**Profile (source of truth):** `Personal Brain (private)/Me.md`

---

## Architecture

```
User
 ↓
Secretary Agent  ←──── Skill Optimizer (ปรับ routing policy)
 ↓                              ↑
Worker Agents   ────────────────┘
                   (ปรับ skill library)
```

---

## Master

### Secretary
**File:** [[Resources/secretary|secretary.md]]
**Role:** รับทุก request → อ่าน Me.md → route ไป worker ที่ถูก → aggregate ผลกลับ

---

## Meta Layer

### Skill Optimizer
**File:** [[Resources/agents/skill-optimizer|skill-optimizer.md]]
**Role:** ปรับปรุง Skill Library และ routing policy — ไม่ execute งาน แต่ทำให้ระบบดีขึ้น
**Trigger:** "optimize skills", "review system", "improve agent", "skill ซ้ำ", "ระบบช้า"

---

## Workers

### 🏠 Life Ops

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[Resources/agents/health-habits\|health-habits]] | habit-tracker, streak-calculator | obsidian-markdown |
| [[Resources/agents/finance-debt\|finance-debt]] | debt-payoff-calculator, spreadsheet-reader | roi-analyzer |
| [[Resources/agents/journal-agent\|journal-agent]] | daily-capture, reflect, export-to-obsidian | para-router, obsidian-markdown |

### 🚀 Startup

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[Resources/agents/idea-validator\|idea-validator]] | tam-estimator | roi-analyzer, grill-with-docs |
| [[Resources/agents/task-tracker\|task-tracker]] | — | roi-analyzer, grill-with-docs |

### 🌏 Thailand

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[Resources/agents/land-dev\|land-dev]] | roi-land-calculator | roi-analyzer, obsidian-markdown |

### 📚 Knowledge

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[Resources/agents/note-organizer\|note-organizer]] | link-suggester | para-router, obsidian-markdown |
| [[Resources/agents/learning-research\|learning-research]] | web-researcher | para-router, obsidian-markdown |

### 📊 Review

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[Resources/agents/weekly-review\|weekly-review]] | focus-setter | obsidian-markdown, grill-with-docs |

### 📖 Wiki (parallel system)

| Worker | File | หมายเหตุ |
|---|---|---|
| wiki-agent | `CLAUDE.md` | โหลดอัตโนมัติทุก session — ไม่ต้อง invoke |

**Routing:** trigger คำว่า "ingest", "query", "wiki", "บันทึกความรู้", "lint" → wiki-agent รับ

---

## Memory Architecture

| ไฟล์ | ขนาด | ใครอ่าน | หน้าที่ |
|---|---|---|---|
| `Journal/current-state.md` | เล็ก (<30 บรรทัด) | Secretary ทุก session | Agent context — ภาพรวมปัจจุบันของทุก dept |
| `Areas/*/state-*.md` | ละเอียด | RAG (Weekly Review) | รายละเอียดต่อ area — target สำหรับ query |
| `Projects/*/state-*.md` | ละเอียด | RAG (Weekly Review) | รายละเอียดต่อ project — target สำหรับ query |

**Update flow:**
```
Daily Notes (7 วัน)
      ↓ Weekly Review Agent
current-state.md  ← เขียนทับ (ภาพรวม)
Areas/*/state-*.md  ← อัปเดต section ที่เกี่ยวข้อง
Projects/*/state-*.md ← อัปเดต section ที่เกี่ยวข้อง
```

---

## Shared Skills

| Skill | File | ใช้โดย |
|---|---|---|
| roi-analyzer | [[Resources/skills/shared/roi-analyzer]] | finance-debt, land-dev, idea-validator, task-tracker |
| para-router | [[Resources/skills/shared/para-router]] | note-organizer, journal-agent, learning-research, wiki-agent |
| grill-with-docs | [[Resources/skills/shared/grill-with-docs/SKILL\|grill-with-docs]] | idea-validator, task-tracker, weekly-review |
| obsidian-markdown | [[Resources/skills/shared/obsidian-markdown/SKILL\|obsidian-markdown]] | wiki-agent, note-organizer, journal-agent, weekly-review, learning-research, land-dev |
| session-to-wiki | [[Resources/skills/shared/session-to-wiki\|session-to-wiki]] | journal-agent, learning-research |
| find-skills | [[Resources/skills/shared/find-skills\|find-skills]] | skill-optimizer *(conditional)* |

---

## Status

| หมวด | มีแล้ว | TODO |
|---|---|---|
| Master | 1 ✅ | — |
| Meta layer | 1 ✅ (skill-optimizer) | — |
| Worker prompts | 9 ✅ (skeleton) | เติมรายละเอียด |
| Shared skills | 5 ✅ | — |
| Agent-specific skills | 8 ✅ (skeleton) | เติมรายละเอียด |
| Memory | current-state.md ✅ | logs/ |
| References | agents.md ✅ | secretary-techniques.md, communication-style.md |

---

_secretary.md อ่านไฟล์นี้ใน Phase 2 ก่อน delegate_
