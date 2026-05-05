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
│   └── agents.md                  ← ไฟล์นี้ (index)
└── .claude/                       ← Single source of truth (Anthropic official)
    ├── agents/                    ← agent prompt files
    │   ├── secretary.md
    │   ├── wiki-agent.md
    │   ├── journal-agent.md
    │   ├── skill-optimizer.md
    │   ├── health-habits.md
    │   ├── finance-debt.md
    │   ├── idea-validator.md
    │   ├── task-tracker.md
    │   ├── land-dev.md
    │   ├── note-organizer.md
    │   ├── learning-research.md
    │   └── weekly-review.md
    ├── commands/                  ← slash commands (/journal, /weekly-review, etc.)
    ├── hooks/                     ← pre-commit hook
    └── skills/                   ← skill library
        ├── shared/                ← ใช้ได้หลาย agent
        │   ├── roi-analyzer.md
        │   ├── para-router.md
        │   ├── find-skills.md         (conditional — ถาม user ก่อน / user สั่งเท่านั้น)
        │   ├── grill-with-docs/       (SKILL.md, ADR-FORMAT.md, CONTEXT-FORMAT.md)
        │   └── obsidian-markdown/     (SKILL.md, refs: CALLOUTS, EMBEDS, PROPERTIES)
        ├── journal-agent/         (daily-capture, reflect, export-to-obsidian)
        ├── secretary/             (intent-analysis, worker-routing, delivery)
        ├── skill-optimizer/       (survey, diagnose, recommend)
        ├── health-habits/         (habit-tracker, streak-calculator)
        ├── finance-debt/          (debt-payoff-calculator, spreadsheet-reader)
        ├── idea-validator/        (tam-estimator)
        ├── land-dev/              (roi-land-calculator)
        ├── note-organizer/        (link-suggester)
        ├── learning-research/     (web-researcher, analyzing-financial-statements)
        └── weekly-review/         (focus-setter)

vault/Journal/
└── current-state.md               ← อัปเดตโดย Journal Agent ทุกอาทิตย์
```

**Profile (source of truth):** `Personal Brain/Me.md`

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
**File:** [[.claude/agents/secretary]]
**Role:** รับทุก request → อ่าน Me.md → route ไป worker ที่ถูก → aggregate ผลกลับ

---

## Meta Layer

### Skill Optimizer
**File:** [[.claude/agents/skill-optimizer]]
**Role:** ปรับปรุง Skill Library และ routing policy — ไม่ execute งาน แต่ทำให้ระบบดีขึ้น
**Trigger:** "optimize skills", "review system", "improve agent", "skill ซ้ำ", "ระบบช้า"

---

## Workers

### 🏠 Life Ops

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[.claude/agents/health-habits\|health-habits]] | habit-tracker, streak-calculator | obsidian-markdown |
| [[.claude/agents/finance-debt\|finance-debt]] | debt-payoff-calculator, spreadsheet-reader | roi-analyzer |
| [[.claude/agents/journal-agent\|journal-agent]] | daily-capture, reflect, export-to-obsidian | para-router, obsidian-markdown |

### 🚀 Startup

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[.claude/agents/idea-validator\|idea-validator]] | tam-estimator | roi-analyzer, grill-with-docs |
| [[.claude/agents/task-tracker\|task-tracker]] | — | roi-analyzer, grill-with-docs |

### 🌏 Thailand

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[.claude/agents/land-dev\|land-dev]] | roi-land-calculator | roi-analyzer, obsidian-markdown |

### 📚 Knowledge

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[.claude/agents/note-organizer\|note-organizer]] | link-suggester | para-router, obsidian-markdown |
| [[.claude/agents/learning-research\|learning-research]] | web-researcher, analyzing-financial-statements *(pending-verify)* | para-router, obsidian-markdown |

### 📊 Review

| Worker | Own Skills | Shared Skills |
|---|---|---|
| [[.claude/agents/weekly-review\|weekly-review]] | focus-setter | obsidian-markdown, grill-with-docs |

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
| roi-analyzer | [[.claude/skills/shared/roi-analyzer]] | finance-debt, land-dev, idea-validator, task-tracker |
| para-router | [[.claude/skills/shared/para-router]] | note-organizer, journal-agent, learning-research, wiki-agent |
| grill-with-docs | [[.claude/skills/shared/grill-with-docs/SKILL\|grill-with-docs]] | idea-validator, task-tracker, weekly-review |
| obsidian-markdown | [[.claude/skills/shared/obsidian-markdown/SKILL\|obsidian-markdown]] | wiki-agent, note-organizer, journal-agent, weekly-review, learning-research, land-dev |
| find-skills | [[.claude/skills/shared/find-skills\|find-skills]] | skill-optimizer *(conditional)* |
| webapp-testing *(pending-verify)* | [[.claude/skills/shared/webapp-testing/SKILL\|webapp-testing]] | idea-validator — เมื่อ App Startup มี web app |
| creating-financial-models *(pending-verify)* | [[.claude/skills/shared/creating-financial-models/SKILL\|creating-financial-models]] | idea-validator, land-dev — เมื่อต้องการ sensitivity analysis |

---

## Status

| หมวด | มีแล้ว | TODO |
|---|---|---|
| Master | 1 ✅ | — |
| Meta layer | 1 ✅ (skill-optimizer) | — |
| Worker prompts | 9 ✅ (skeleton) | เติมรายละเอียด |
| Shared skills | 5 active + 2 pending-verify | webapp-testing, creating-financial-models |
| Agent-specific skills | 8 ✅ (skeleton) | เติมรายละเอียด |
| Memory | current-state.md ✅ | logs/ |
| References | agents.md ✅ | — |

---

_secretary.md อ่านไฟล์นี้ใน Phase 2 ก่อน delegate_
