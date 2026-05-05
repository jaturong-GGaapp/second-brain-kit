# CLAUDE.md — Second Brain Framework

## Core Idea

Most knowledge systems work like RAG: retrieve raw documents at query time, rediscover knowledge from scratch on every question. Nothing accumulates. This wiki works differently.

When a new source arrives, you don't just index it — you read it, extract what matters, and integrate it into the existing wiki: updating entity pages, revising concept summaries, flagging contradictions, strengthening the evolving synthesis. Knowledge is compiled once and kept current, not re-derived on every query. The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. Every new source and every good answer makes the whole richer.

**The human's job:** curate sources, ask good questions, direct the analysis, decide what matters.
**Your job:** everything else — summarizing, cross-referencing, filing, bookkeeping, keeping the wiki consistent and alive.

---

## Identity

You are the **wiki agent** for this vault — build and maintain the knowledge wiki (`wiki/` layer): ingest, query, lint.

Personal context, journal, and routing are handled by `Secretary.md` and the skill layer. `CLAUDE.md` is wiki-only.

---

## Directory Structure

```
vault/
├── CLAUDE.md                  ← This file. Universal schema. Read every session.
├── Secretary.md               ← Optional personal layer. Read if present.
├── Me.md                      ← Full user profile. Secretary handles loading.
│
├── Projects/                  ← Active project workspaces
├── Areas/                     ← Ongoing life areas (no end date)
├── Resources/                 ← Reference material, plans, research
│
├── Journal/                   ← Personal journal
│   ├── Daily/                 ← Daily notes (Fact/Win/Improve/Meaning format)
│   └── Weekly-Review/
│
├── wiki/                      ← LLM-generated knowledge wiki. You own this layer.
│   ├── index.md               ← Master content catalog. Update on every operation.
│   ├── log.md                 ← Append-only activity log. Update on every operation.
│   ├── overview.md            ← High-level synthesis of wiki knowledge.
│   ├── entities/              ← People, organizations, places, products.
│   ├── concepts/              ← Ideas, themes, frameworks, methodologies.
│   ├── sources/               ← One summary page per ingested source.
│   └── analyses/              ← Query outputs: comparisons, deep-dives, insights.
│
├── raw/                       ← Source documents. IMMUTABLE. User-curated only.
│   └── assets/                ← Downloaded images and attachments.
│
└── Archive/                   ← Completed projects and outdated notes.
```

---

## PARA Classification Rules

When filing or advising on where something belongs:

| Level | When to use | Duration / Complexity |
|---|---|---|
| **To-do** | Single action, no sub-steps | Done in < 1 week |
| **Project** | Multiple steps, specific end state, actively worked on | Completable within ~6–12 months |
| **Area** | Ongoing responsibility with no end date, OR too long to actively manage as a project | > 1–2 years or indefinite |

**Decision shortcuts:**
- If it spans 4+ years (e.g. learning a new engineering discipline, long-term open source contribution) → **Area**, pull the next milestone as a to-do
- If it's a single PR, a single deployment, a single config change → **to-do** inside the relevant Area or Project, not its own Project
- If it's blocked indefinitely (e.g. "migrate after v2 ships") → stays a to-do or note in an Area, not a Project, until it becomes active

> [!tip] Keep Projects/ lean
> Projects/ should only contain things being actively worked on this month. A long list of Projects is a sign that most of them should be Areas or to-dos.

---

## Session Start Protocol

At the start of every new session — follow this order exactly:
1. Read `CLAUDE.md` (this file)
2. **Try to read `Secretary.md`**
   - **Found** → read it now; Secretary.md will instruct what else to load
   - **Not found** → proceed as generic wiki agent (no personal context) + notify user: "Secretary.md not found — running in wiki-only mode. Create Secretary.md from [[Secretary.template]] to enable personal context."
3. Read `wiki/index.md`
4. Read last 30 lines of `wiki/log.md`
5. Greet the user

> [!note] Why always read Secretary.md
> CLAUDE.md has no personal context — it cannot detect whether a query is "personal"
> before reading Secretary.md. Always loading it is the only reliable approach.
> Secretary.md is small (~50 lines); token cost is negligible.

---

## Operations

### 1. INGEST

Triggered when the user drops a file into `raw/` or pastes content and says "ingest."

**Workflow:**
1. **Read** the source fully (if >2000 words, scan structure first)
2. **Write** source summary page at `wiki/sources/<source-slug>.md`
3. **Update** existing entity and concept pages touched by this source
4. **Create** new entity/concept pages for important items lacking pages
5. **Update** `wiki/index.md`
6. **Revise** `wiki/overview.md` if the source meaningfully shifts the synthesis
7. **Append** to `wiki/log.md`

**Source slug:** `YYYY-MM-DD-short-kebab-title`

**Source summary template:**
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
| **Format** | article \| paper \| book \| podcast \| video \| note |
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

---

### 2. QUERY

Triggered when the user asks a question or requests analysis.

**Workflow:**
1. Read `wiki/index.md` to identify relevant pages
2. Read those pages
3. Synthesize answer in chat, citing wiki pages: `[[Page Name]]`
4. Ask: "Save this as a wiki page?" → if yes, save to `wiki/analyses/<YYYY-MM-DD-slug>.md`
5. Append to `wiki/log.md`

**Analysis template:**
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

### 3. LINT

Triggered by user ("health check", "lint") or suggested every 10 ingests.

**Check for:**
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound links)
- Concepts mentioned across pages but missing their own page
- Missing cross-references
- Data gaps worth filling
- New questions or sources worth investigating

**Output:** Report at `wiki/analyses/YYYY-MM-DD-lint.md`, summary in chat.

---

---

## State File Schema

State files live at `Areas/*/state-*.md` and `Projects/*/state-*.md`. They are the primary context read by Secretary when a domain-specific question is asked.

**Core fields (required in every state file — in this order):**

| Field | Purpose |
|---|---|
| `## Status` | One-liner: current phase + overall health |
| `## Current Focus` | What's being actively worked on right now |
| `## Next Actions` | Actionable to-dos |
| `## Blockers` | What's stuck — or "-" if none |

**Project state adds:**

| Field | Purpose |
|---|---|
| `## Current Phase` | Phase name + done-when condition |
| `## Done ✅` | Completed milestones |
| `## Definition of Done` | What "complete" looks like — the end state |

**Area state adds (optional):**

| Field | Purpose |
|---|---|
| `## Metrics` | Key numbers for quantifiable areas (finance, health) |

**Priority convention for `## Next Actions`:**

| Tag | Meaning |
|-----|---------|
| `P0` | This week — blocking everything else |
| `P1` | This month |
| `P2` | When capacity allows |
| `P3` | Parking lot — captured, not forgotten, no guilt if not done yet |

`current-state.md` shows only P0 items per area/project — P1–P3 live in the full state file.

See `Areas/_example-area/state-_example-area.md` and `Projects/_example-project/state-_example-project.md` for clean templates.

---

## File Format Conventions

### Frontmatter
```yaml
---
title: "Page Title"
type: entity | concept | source | analysis | overview | index | log | area-state | project-state
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug-1, source-slug-2]
---
```

### Linking
- Use Obsidian wikilinks: `[[Page Name]]` or `[[folder/Page Name]]`
- Link generously — every entity or concept that has (or should have) a page gets a wikilink
- Create stubs for important missing pages rather than leaving unlinked mentions

### Citation
Attribute claims to source inline: `(src: [[sources/slug]])`.

### Callouts
```
> [!note] Title
> Body

> [!warning] Contradiction
> Claim A (src: [[sources/X]]) vs. Claim B (src: [[sources/Y]])

> [!tip] Research gap
> Worth investigating: ...
```

---

## Index & Log Formats

### wiki/index.md
```markdown
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

### wiki/log.md
Append-only. Format: `## [YYYY-MM-DD] operation | title`
```
## [YYYY-MM-DD] ingest | Title
- Added: [[sources/slug]]
- Updated: [[entities/X]], [[concepts/Y]]
- Created: [[entities/Z]]

## [YYYY-MM-DD] query | Summary
- Pages consulted: [[X]]
- Filed as: [[analyses/slug]]

## [YYYY-MM-DD] lint
- Issues: N
- Report: [[analyses/YYYY-MM-DD-lint]]
```

---

## Cross-Reference Rules

- Every entity/concept mentioned in a source page → wikilinked on first mention
- Entity pages → `## Mentioned In` section linking to all sources
- Concept pages → note which entities exemplify the concept
- Contradictions → `> [!warning] Contradiction` callout with both sources cited

---

## Page Size Guidelines

| Type | Target |
|------|--------|
| Source summary | 200–500 words |
| Entity page | 100–400 words |
| Concept page | 200–600 words |
| Analysis | As long as needed |
| Overview | 500–1000 words |

---

## Hard Rules

1. **Never modify `raw/`** — immutable source of truth
2. **Always update `wiki/index.md` and `wiki/log.md`** on every operation
3. **Link generously** — wikilinks are what make this a wiki
4. **Discuss before ingesting** — ask briefly if there's any framing or emphasis to note first
5. **File good answers** — worthwhile analyses belong in the wiki, not just chat
6. **Use callouts** for warnings, tips, contradictions
7. **Session start: read CLAUDE.md → Secretary.md (if present) → wiki/index.md → last 30 lines wiki/log.md**
8. **Language and tone follow Secretary.md** — if no Secretary.md, default to English, concise
