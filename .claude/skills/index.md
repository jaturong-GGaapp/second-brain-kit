# Skill Library Index

_Last updated: 2026-05-05_

---

## Agents

| Agent | Description | Lenses |
|-------|-------------|--------|
| [secretary.md](../agents/secretary.md) | Master orchestrator — route งานตาม domain, โหลด context ที่ถูกต้อง | `skills/secretary/` (3 lenses) |
| [journal-agent.md](../agents/journal-agent.md) | Daily FWIM interview + patch current-state.md | `skills/journal-agent/` (3 lenses) |
| [wiki-agent.md](../agents/wiki-agent.md) | INGEST / QUERY / LINT บน wiki/ layer | — |
| [skill-optimizer.md](../agents/skill-optimizer.md) | Systems architect สำหรับ .claude/ — survey, diagnose, recommend | `skills/skill-optimizer/` (3 lenses) |
| [business-plan-analyst.md](../agents/business-plan-analyst.md) | วิเคราะห์แผนธุรกิจผ่าน multi-lens framework (Market, Model, Moat, Money, Milestones) | — |

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
| [daily-capture.md](journal-agent/daily-capture.md) | Neutral witness — รับข้อมูลโดยไม่นำ ไม่ judge | journal-agent, /journal |
| [reflect.md](journal-agent/reflect.md) | Compassionate pattern-finder — หา pattern ไม่ใช่ตัวผู้กระทำ | journal-agent, /weekly-review |
| [export-to-obsidian.md](journal-agent/export-to-obsidian.md) | Careful archivist — เขียนให้อ่านได้ใน 6 เดือน | journal-agent |

### secretary/
| Lens | Character | Used by |
|------|-----------|---------|
| [intent-analysis.md](secretary/intent-analysis.md) | Translator — เข้าใจ intent จริงก่อนตอบ | secretary |
| [worker-routing.md](secretary/worker-routing.md) | Dispatcher — route by capability ไม่ใช่ keyword | secretary |
| [delivery.md](secretary/delivery.md) | Editor — output เฉพาะที่ user ต้องการลงมือ | secretary |

### skill-optimizer/
| Lens | Character | Used by |
|------|-----------|---------|
| [survey.md](skill-optimizer/survey.md) | Cartographer — map ก่อน judge | skill-optimizer |
| [diagnose.md](skill-optimizer/diagnose.md) | Structural engineer — หา load-bearing problems | skill-optimizer |
| [recommend.md](skill-optimizer/recommend.md) | Pragmatic builder — minimum effective change | skill-optimizer |

---

## Shared Skills

| Skill | Used by |
|-------|---------|
| [shared/obsidian-markdown/](shared/obsidian-markdown/SKILL.md) | journal-agent, /session-to-wiki, /deep-wiki-ingest, /weekly-review |
| [shared/para-router.md](shared/para-router.md) | secretary (classify Project/Area/Todo/Resource + scaffold flow) |
| [shared/roi-analyzer.md](shared/roi-analyzer.md) | general purpose — ROI calculations |
| [shared/grill-with-docs/](shared/grill-with-docs/SKILL.md) | document analysis |
| [shared/webapp-testing/](shared/webapp-testing/SKILL.md) | webapp QA |
| [shared/creating-financial-models/](shared/creating-financial-models/SKILL.md) | finance calculations |