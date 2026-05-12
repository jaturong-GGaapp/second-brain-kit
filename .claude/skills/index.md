# Skill Library Index

_Last updated: 2026-05-06_

> **Format standard (ตั้งแต่ 2026-05-06):** skills ทุกตัวใช้ directory + `SKILL.md` ตาม Agent Skills spec
> Flat files (`.md` เดี่ยว) คือ legacy — ถ้าพบให้ migrate

---

## Agents

| Agent | Description | Lenses |
|-------|-------------|--------|
| [secretary.md](../agents/secretary.md) | Master orchestrator — route งานตาม domain, โหลด context ที่ถูกต้อง | `skills/secretary/` (3 lenses) |
| [journal-agent.md](../agents/journal-agent.md) | Daily FWIM interview + patch current-state.md | `skills/journal-agent/` (3 lenses) |
| [wiki-agent.md](../agents/wiki-agent.md) | INGEST / QUERY / LINT บน wiki/ layer | — |
| [skill-optimizer.md](../agents/skill-optimizer.md) | Systems architect สำหรับ .claude/ — survey, diagnose, recommend | `skills/skill-optimizer/` (3 lenses) |
| [business-plan-analyst.md](../agents/business-plan-analyst.md) | วิเคราะห์แผนธุรกิจผ่าน multi-lens framework (Market, Model, Moat, Money, Milestones) | — |
| [financial-advisor.md](../agents/financial-advisor.md) | ที่ปรึกษาการเงินส่วนตัวครบวงจร (Wealth Planner + Fund Manager + Career Coach + Risk Manager + Personal CFO) | `skills/financial-advisor/` (3 lenses) |

---

## Commands

| Command | Trigger | Delegates to |
|---------|---------|--------------|
| [/journal](../commands/journal.md) | `/journal` | `agents/journal-agent.md` |
| [/session-to-wiki](../commands/session-to-wiki.md) | `/session-to-wiki`, "เก็บ session", "ingest" | — (standalone) |
| [/deep-wiki-ingest](../commands/deep-wiki-ingest.md) | `/deep-wiki-ingest`, "deep ingest", "เก็บละเอียด" | — (standalone) |
| [/weekly-review](../commands/weekly-review.md) | `/weekly-review` | — (standalone) |
| [/skill-optimizer](../commands/skill-optimizer.md) | `/skill-optimizer` | `agents/skill-optimizer.md` |
| [/sync-claude-project](../commands/sync-claude-project.md) | `/sync-claude-project`, "sync knowledge", "sync claude project" | — (standalone) |
| [/new-claude-project](../commands/new-claude-project.md) | `/new-claude-project [name]`, "new claude project", "scaffold project" | — (standalone) |
| [/archive-project](../commands/archive-project.md) | `/archive-project [name]`, "project เสร็จแล้ว", "archive project" | — (TODO: implement) |

---

## Lenses (Sub-skills)

### journal-agent/
| Lens | Character | Used by |
|------|-----------|---------|
| [daily-capture/SKILL.md](journal-agent/daily-capture/SKILL.md) | Neutral witness — รับข้อมูลโดยไม่นำ ไม่ judge | journal-agent, /journal |
| [reflect/SKILL.md](journal-agent/reflect/SKILL.md) | Compassionate pattern-finder — หา pattern ไม่ใช่ตัวผู้กระทำ | journal-agent, /weekly-review |
| [export-to-obsidian/SKILL.md](journal-agent/export-to-obsidian/SKILL.md) | Careful archivist — เขียนให้อ่านได้ใน 6 เดือน | journal-agent |

### secretary/
| Lens | Character | Used by |
|------|-----------|---------|
| [intent-analysis/SKILL.md](secretary/intent-analysis/SKILL.md) | Translator — เข้าใจ intent จริงก่อนตอบ | secretary |
| [worker-routing/SKILL.md](secretary/worker-routing/SKILL.md) | Dispatcher — route by capability ไม่ใช่ keyword | secretary |
| [delivery/SKILL.md](secretary/delivery/SKILL.md) | Editor — output เฉพาะที่ user ต้องการลงมือ | secretary |
| [app-context/SKILL.md](secretary/app-context/SKILL.md) | Interviewer — เก็บ project context ก่อน init-wiki | secretary (on demand) |

### financial-advisor/
| Lens | Character | Used by |
|------|-----------|---------|
| [data-collection/SKILL.md](financial-advisor/data-collection/SKILL.md) | Empathetic Detective — ถาม 11 หมวดอย่างถูกจังหวะ | financial-advisor |
| [diagnosis/SKILL.md](financial-advisor/diagnosis/SKILL.md) | Honest Diagnostician — วิเคราะห์และ flag ความเสี่ยง | financial-advisor |
| [action-planner/SKILL.md](financial-advisor/action-planner/SKILL.md) | Pragmatic Engineer — แปลงวิเคราะห์ → steps ที่ทำได้จริง | financial-advisor |

### skill-optimizer/
| Lens | Character | Used by |
|------|-----------|---------|
| [survey/SKILL.md](skill-optimizer/survey/SKILL.md) | Cartographer — map ก่อน judge | skill-optimizer |
| [diagnose/SKILL.md](skill-optimizer/diagnose/SKILL.md) | Structural engineer — หา load-bearing problems | skill-optimizer |
| [recommend/SKILL.md](skill-optimizer/recommend/SKILL.md) | Pragmatic builder — minimum effective change | skill-optimizer |

---

## Shared Skills

| Skill | Used by |
|-------|---------|
| [shared/obsidian-markdown/SKILL.md](shared/obsidian-markdown/SKILL.md) | journal-agent, /session-to-wiki, /deep-wiki-ingest, /weekly-review |
| [shared/para-router/SKILL.md](shared/para-router/SKILL.md) | secretary (classify Project/Area/Todo/Resource + scaffold flow) |
| [shared/roi-analyzer/SKILL.md](shared/roi-analyzer/SKILL.md) | secretary — ROI calculations |
| [shared/grill-with-docs/SKILL.md](shared/grill-with-docs/SKILL.md) | stress-test code/architecture decisions (CONTEXT.md, ADRs) |
| [shared/grill-plan/SKILL.md](shared/grill-plan/SKILL.md) | stress-test แผนชีวิต/การเงิน/ธุรกิจ ด้วย Socratic questioning |
| [shared/find-skills/SKILL.md](shared/find-skills/SKILL.md) | ค้นหา skill จาก skills.sh ecosystem |
| [shared/webapp-testing/SKILL.md](shared/webapp-testing/SKILL.md) | webapp QA |
| [shared/creating-financial-models/SKILL.md](shared/creating-financial-models/SKILL.md) | finance calculations |