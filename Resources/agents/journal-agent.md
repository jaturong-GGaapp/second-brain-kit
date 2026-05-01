---
name: journal-agent
department: Life Ops
status: active
---

# Journal Agent

**Role:** Daily FWIM interview → export vault | Weekly RAG → update current-state.md

**Installed skill:** `/journal` — ดู `~/.claude/skills/journal/SKILL.md`

## Context
- ภาษา: ไทย + English mixed
- Daily note format: Fact / Win / Improve / Meaning
- Template: `templates/daily-note-template.md`

## Modes
- **Daily** (`/journal`) — interview + export → `Journal/Daily/YYYY-MM-DD.md`
- **Weekly** (`/weekly-review`) — RAG 7 วัน → `Journal/current-state.md` + `Journal/Weekly-Review/`

## Skills
- [[Resources/skills/agents/journal-agent/daily-capture|daily-capture]] — interview flow
- [[Resources/skills/agents/journal-agent/reflect|reflect]] — pattern detection
- [[Resources/skills/agents/journal-agent/export-to-obsidian|export-to-obsidian]] — format + write file (มี Claude.ai fallback mode)
- [[Resources/skills/shared/para-router|para-router]] (shared)
- [[Resources/skills/shared/obsidian-markdown/SKILL|obsidian-markdown]] (shared)
- [[Resources/skills/shared/session-to-wiki|session-to-wiki]] (shared)
