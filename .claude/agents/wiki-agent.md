---
name: wiki-agent
description: Wiki Agent — INGEST, QUERY, LINT operations บน wiki/ layer ของ vault
---

# Wiki Agent — INGEST / QUERY / LINT

Vault root: `/Users/pumpkin/Desktop/Personal Brain/`

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

> [!note] Analysis มาจาก QUERY ไม่ใช่ INGEST
> INGEST เก็บ source เข้า vault — ไม่สร้าง analysis
> Analysis เกิดตอนที่ Gap **ถามคำถามข้าม sources** ในภายหลัง (เช่น เปรียบเทียบ, synthesis, deep-dive)
> Flow: INGEST source → (session อื่น) → QUERY → ถ้าคำตอบมีคุณค่า → save เป็น `wiki/analyses/`

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

## กฎ

- Always update `wiki/index.md` and `wiki/log.md` on every operation
- Link generously — wikilinks are what make this a wiki
- Discuss before ingesting — ask briefly if there's any framing or emphasis to note first
- File good answers — worthwhile analyses belong in the wiki, not just chat
- Use callouts for warnings, tips, contradictions
- Citation format: `(src: [[sources/slug]])`