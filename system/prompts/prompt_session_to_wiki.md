# Prompt: Session to Wiki

## Purpose
Convert a Claude.ai (or any AI chat) session into a structured wiki entry and route it to the right place — knowledge wiki or daily journal.

## Input Variables
- `{{session_summary}}` — paste key points or full summary of the session
- `{{session_topic}}` — one line describing what the session was about
- `{{your_name}}` — your name for the entities link (e.g. `[[entities/You]]`)

## Output
A markdown block ready to copy into your vault:
- **Knowledge sessions** → `wiki/sources/YYYY-MM-DD-slug.md`
- **Personal insight sessions** → add to `Journal/Daily/YYYY-MM-DD.md`

---

## Prompt

```
You are a vault assistant. Convert the session below into a structured note for my second brain.

Session topic: {{session_topic}}
Session summary / key points:
{{session_summary}}

Step 1 — Detect the type:

KNOWLEDGE if the session is about:
- a framework, concept, or methodology
- research, analysis, or external information
- how something works

PERSONAL if the session is about:
- a personal decision or realization
- self-reflection or insight
- a win, failure, or lesson from my own life

Step 2 — Format accordingly:

If KNOWLEDGE → produce a wiki source summary:

---
title: "{{session_topic}}"
type: source
tags: []
created: YYYY-MM-DD
sources: [self]
---

# {{session_topic}}

| Field | Value |
|-------|-------|
| **Author** | [[entities/{{your_name}}]] |
| **Date** | YYYY-MM-DD |
| **Format** | note (session capture) |

## Summary
3–5 sentences.

## Key Takeaways
- ...

## Connections
- Supports: [[concepts/X]]
- See also: [[sources/Y]]

## Notes

---

If PERSONAL → produce a journal addition:

**Where to add:** paste into today's daily note under the matching section.

**Insight / realization** → ## Meaning
**Decision made** → ## Win or ## Improve
**Next action** → end of note as a task

Format:
> [insight or decision in 1–2 sentences]
> — from session: {{session_topic}}

---

Tell me which type you detected and show the formatted output.
```
