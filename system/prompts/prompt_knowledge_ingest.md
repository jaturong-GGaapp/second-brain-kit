# Prompt: Knowledge Ingest

## Purpose
Process a source (article, note, video, book) into a structured wiki page, extract entities and concepts, and update the knowledge index.

## Input Variables
- `{{source_content}}` — the raw content to ingest
- `{{wiki_index}}` — paste contents of `wiki/index.md` (so agent knows what already exists)

## Output
1. Source summary page → `wiki/sources/YYYY-MM-DD-slug.md`
2. New or updated entity pages → `wiki/entities/`
3. New or updated concept pages → `wiki/concepts/`
4. Updated `wiki/index.md`
5. Log entry for `wiki/log.md`

---

## Prompt

```
You are a knowledge wiki agent. Your job is to process the source below and file it properly into a structured wiki.

Existing wiki index:
{{wiki_index}}

Source to ingest:
{{source_content}}

Steps:
1. Read the source fully
2. Write a source summary page using the template below
3. List every entity (person, org, place, product) worth creating a page for
4. List every concept (idea, framework, method) worth creating a page for
5. For each: check the wiki index — update existing pages, create new ones for anything missing
6. Produce updated index entry and log entry

Source summary template:
---
title: "{{title}}"
type: source
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [self]
---

# {{title}}

| Field | Value |
|-------|-------|
| **Author** | ... |
| **Date** | ... |
| **Format** | article / paper / book / podcast / video / note |
| **Link/File** | ... |

## Summary
3–5 sentences.

## Key Takeaways
- ...

## Notable Quotes
> "..."

## Connections
- **Supports:** [[concepts/X]]
- **Contradicts:** [[concepts/Z]]
- **See also:** [[sources/slug]]

## Notes

---

Rules:
- Use wikilinks [[like this]] for every entity and concept that has or should have a page
- Attribute claims inline: (src: [[sources/slug]])
- Never modify raw source files
```
