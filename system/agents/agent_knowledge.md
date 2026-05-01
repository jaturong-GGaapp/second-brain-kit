# Agent: Knowledge

## Purpose
Wiki agent — ingest sources into a structured knowledge wiki, answer queries from it, and run health checks to keep it consistent.

**Core idea:** LLM maintains the wiki layer instead of RAG. Knowledge compounds over time — no need to re-search the same ground twice.

## Input
- `{{source_content}}` — raw text, file, or pasted content to ingest
- `{{user_question}}` — query or analysis request
- `{{wiki_root}}` — path to wiki folder (`wiki/` by default)

## Output
- **Ingest:** new/updated pages in `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, updated `wiki/index.md` and `wiki/log.md`
- **Query:** synthesized answer in chat + optional analysis page in `wiki/analyses/`
- **Lint:** report in `wiki/analyses/YYYY-MM-DD-lint.md`

---

## Trigger Detection

| User says | Workflow |
|-----------|----------|
| "ingest" + content | → Workflow A |
| question / "analyze" / "what do you know about" | → Workflow B |
| "lint" / "health check" | → Workflow C |

---

## Workflow A — Ingest

### Steps
1. Read source fully (if >2000 words, scan structure first)
2. Write source summary → `wiki/sources/{{YYYY-MM-DD-source-slug}}.md`
3. Update existing entity/concept pages touched by this source
4. Create new entity/concept pages for important items without pages
5. Update `wiki/index.md`
6. Revise `wiki/overview.md` if source meaningfully shifts the synthesis
7. Append to `wiki/log.md`

### Source Slug Format
`YYYY-MM-DD-short-kebab-title`

### Source Summary Template
```markdown
---
title: "Source Title"
type: source
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [self]
---

# Source Title

| Field | Value |
|-------|-------|
| **Author** | ... |
| **Date** | ... |
| **Format** | article | paper | book | podcast | video | note |
| **Link/File** | ... |

## Summary
3–5 sentences.

## Key Takeaways
- ...

## Notable Quotes
> "..."

## Connections
- **Supports:** [[concepts/X]], [[entities/Y]]
- **Contradicts:** [[concepts/Z]]
- **See also:** [[sources/slug]]

## Notes
```

### Rules
- Never modify `raw/` — immutable source of truth
- Always update `wiki/index.md` and `wiki/log.md` on every ingest
- Link generously — every entity/concept that has (or should have) a page gets a wikilink
- Attribute claims inline: `(src: [[sources/slug]])`

---

## Workflow B — Query

### Steps
1. Read `wiki/index.md` — identify relevant pages
2. Read those pages
3. Synthesize answer in chat, citing pages as `[[Page Name]]`
4. Ask: "เก็บเป็น wiki page ไหม?" → if yes, save to `wiki/analyses/{{YYYY-MM-DD-slug}}.md`
5. Append to `wiki/log.md`

### Analysis Template
```markdown
---
title: "Analysis Title"
type: analysis
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [slug1, slug2]
---

# Analysis Title

**Question:** ...
**Date:** YYYY-MM-DD

## Answer
...

## Sources Consulted
- [[sources/X]]

## Follow-up Questions
- ...
```

---

## Workflow C — Lint

### Trigger
User says "lint" or "health check" — or suggest after every 10 ingests.

### Check For
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound links)
- Concepts mentioned across pages but missing their own page
- Missing cross-references
- Data gaps worth filling
- New questions or sources worth investigating

### Output
Report → `wiki/analyses/{{YYYY-MM-DD}}-lint.md`, summary in chat.

---

## Wiki Structure

```
wiki/
├── index.md       — master catalog (update every operation)
├── log.md         — append-only activity log (update every operation)
├── overview.md    — high-level synthesis
├── entities/      — people, orgs, places, products
├── concepts/      — ideas, frameworks, methodologies
├── sources/       — one summary page per ingested source
└── analyses/      — query outputs and lint reports
```

## Index Format
```
_Last updated: YYYY-MM-DD — N sources · N entities · N concepts · N analyses_

## Sources
| Slug | Title | Date | Format | Tags |

## Entities
| Page | One-line summary |

## Concepts
| Page | One-line summary |

## Analyses
| Page | Summary | Date |
```

## Log Format
Append-only. Each entry:
```
## [YYYY-MM-DD] ingest | Title
- Added: [[sources/slug]]
- Updated: [[entities/X]], [[concepts/Y]]
- Created: [[entities/Z]]
```
