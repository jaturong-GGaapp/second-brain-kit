# /deep-wiki-ingest — Deep Wiki Ingest

แปลง conversation ปัจจุบัน → wiki pages ครบชุด: source + concepts + entities + analysis + state updates

Vault root: `/Users/pumpkin/Desktop/Personal Brain/`

**ต่างจาก session-to-wiki:** skill นี้สร้าง concept pages, entity pages, และ analysis แยกต่างหาก ไม่ใช่แค่ stubs — เหมาะกับ session ที่มี ideas/keywords สำคัญจำนวนมากและต้องการเก็บอย่างละเอียด (200–600 คำต่อ concept page)

Trigger: `/deep-wiki-ingest`, "deep ingest", "เก็บละเอียด", "ingest แบบเต็ม", "เก็บทั้งหมดลง wiki"

---

## Step 0 — Load Context (ทำก่อนเริ่ม ไม่ต้องบอก Gap)

อ่าน:
1. `wiki/index.md` — รู้ว่า pages ไหนมีอยู่แล้ว (ไม่สร้างซ้ำ)
2. `wiki/log.md` (30 บรรทัดสุดท้าย) — last activity
3. State file ที่เกี่ยวข้องกับ session domain ถ้ามี (ดูจาก Secretary.md domain routing)

---

## Step 0.5 — Save Raw Content

ก่อนสร้าง inventory หรือเขียน wiki page ใดๆ — บันทึก original content ลง `raw/YYYY-MM-DD-slug.md` เสมอ (slug เดียวกับที่จะใช้ใน wiki/sources/)

```markdown
---
title: "[Title]"
type: raw
date: YYYY-MM-DD
slug: YYYY-MM-DD-slug
---

[original content as-is — ไม่แปลง ไม่ตัด ไม่เพิ่ม]
```

raw file คือต้นฉบับที่อ่านได้โดยตรง — wiki/sources/ คือ processed version ที่มี links และ structure

---

## Step 1 — Scan & Inventory

อ่าน conversation ทั้งหมดแล้วสร้าง inventory ก่อนเขียนอะไร:

### 1a — Concepts
list ทุก framework, methodology, idea, mechanic, mental model ที่ปรากฏใน session

สำหรับแต่ละอัน ตัดสินใจ:
- มี wiki page อยู่แล้วไหม? (เช็คจาก index.md)
- สำคัญพอที่จะมี page เป็นของตัวเองไหม? (เกณฑ์: ถ้าใน session อื่นในอนาคต Gap น่าจะอยากอ้างอิงถึงมัน → ใช่)
- ถ้าใช่ → เพิ่มใน "concepts to create" list

### 1b — Entities
list ทุก บุคคล, บริษัท, product, app, platform ที่ปรากฏใน session

สำหรับแต่ละอัน ตัดสินใจ:
- มี wiki page อยู่แล้วไหม?
- มีบทบาทในเนื้อหาพอที่ควรมี page ไหม? (competitor, reference, inspiration, key person)
- ถ้าใช่ → เพิ่มใน "entities to create" list

### 1c — Analysis
session นี้มี deliverable ที่ชัดเจนไหม? เช่น:
- business plan, roadmap, decision framework
- comparison / recommendation
- synthesis ที่ Gap น่าจะ reference กลับมาในอนาคต

ถ้าใช่ → สร้าง analysis page

### 1d — State Files
session นี้ update state ของ Project หรือ Area ไหนไหม?
- ถ้าใช่ → ระบุไฟล์ที่ต้องอัปเดต

**รายงาน inventory แล้วเริ่มทำเลย — ไม่ต้องรอ confirm:**
```
📋 กำลังสร้าง:
- Source: 1 file
- Concepts: [N] — [ชื่อ]
- Entities: [N] — [ชื่อ]
- Analysis: [มี/ไม่มี]
- State updates: [ไฟล์ที่จะแก้]
```

---

## Step 2 — Source File

**Path:** `wiki/sources/YYYY-MM-DD-short-kebab-title.md`

ใช้ template จาก CLAUDE.md (source summary template):
- Title, author, date, format, link
- Summary (3–5 ประโยค)
- Key Takeaways
- Notable Quotes (ถ้ามี)
- Connections → link ไปทุก concept/entity page ที่สร้างใน step นี้
- Notes

---

## Step 3 — Concept Pages

สำหรับทุก concept ใน "concepts to create" list:

**Path:** `wiki/concepts/[ConceptName].md`

Template:
```markdown
---
title: "[Concept Name]"
type: concept
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug]
---

# [Concept Name]

[คำนิยามหรือภาพรวม 1–2 ประโยค]

[เนื้อหาหลัก — ใช้ tables, lists, examples ตามความเหมาะสม]

## Mentioned In
- [[sources/slug]]

## See Also
- [[concepts/X]]
- [[entities/Y]]
```

เป้าหมาย 200–600 คำต่อหน้า — ละเอียดพอให้ Gap อ้างอิงได้ในอนาคต ไม่ใช่แค่ stub

---

## Step 4 — Entity Pages

สำหรับทุก entity ใน "entities to create" list:

**Path:** `wiki/entities/[EntityName].md`

Template:
```markdown
---
title: "[Entity Name]"
type: entity
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug]
---

# [Entity Name]

[คำอธิบาย 1 ประโยค]

| Field | Value |
|-------|-------|
| **Type** | ... |
| **Model** | ... |
| ... | ... |

## [Strengths / Core / ส่วนที่เกี่ยวข้อง]
...

## Relevance to Gap's Work
[ทำไมถึงอยู่ใน vault นี้ — เชื่อมกับอะไร]

## Mentioned In
- [[sources/slug]]
```

เป้าหมาย 100–400 คำต่อหน้า

---

## Step 5 — Analysis (ถ้ามี)

**Path:** `wiki/analyses/YYYY-MM-DD-slug.md`

ใช้ template จาก CLAUDE.md (analysis template):
- Question, date, sources consulted
- Answer / deliverable หลัก
- Follow-up questions

---

## Step 6 — State File Updates (ถ้ามี)

อัปเดต state file ที่ระบุใน Step 1d:
- `## Status`, `## Current Focus`, `## Next Actions`, `## Done ✅`
- เพิ่ม link ไปที่ source/analysis ที่เพิ่งสร้าง

---

## Step 7 — Update wiki/index.md

เพิ่ม rows ใน sections ที่เกี่ยวข้อง:
- Sources table
- Entities table
- Concepts table
- Analyses table (ถ้ามี)

อัปเดต header count: `N sources · N entities · N concepts · N analyses`

---

## Step 8 — Append wiki/log.md

Format:
```
## [YYYY-MM-DD] ingest | [Title]
- Added: [[sources/slug]], raw/SLUG.md
- Created concepts: [[concepts/X]], [[concepts/Y]], ...
- Created entities: [[entities/A]], [[entities/B]], ...
- Created analysis: [[analyses/slug]] (ถ้ามี)
- Updated: wiki/index.md (N sources · N entities · N concepts), [state files ที่แก้]
- Notes: [สิ่งสำคัญที่ควรรู้เกี่ยวกับ session นี้]
```

---

## Step 9 — Update wiki/overview.md (ถ้าจำเป็น)

เพิ่ม theme ใหม่ถ้า session นี้เปลี่ยน direction หรือเพิ่ม dimension ที่ยังไม่มีใน overview — ถ้าแค่เพิ่ม knowledge ใน theme ที่มีอยู่แล้ว → ข้ามได้

อัปเดต Sources Count ด้วยทุกครั้ง

---

## Step 10 — Report

รายงานในรูปแบบ CLAUDE.md INGEST convention:

```
## [YYYY-MM-DD] ingest | [Title]

- Added:    [[sources/slug]], raw/SLUG.md
- Created:  [[concepts/X]], [[concepts/Y]], [[entities/A]], [[analyses/slug]]
- Updated:  [[wiki/index.md]] (N sources · N entities · N concepts · N analyses),
            [[wiki/log.md]], [state files ถ้ามี], [wiki/overview.md ถ้ามี]
- Connections: (cross-links หลักที่สร้าง)
```

---

## กฎ

- ตอบภาษาไทย เป็นกันเอง
- เขียนไฟล์จริงทันที ไม่ต้อง output markdown block
- raw/ files ที่สร้างใหม่ → write-once ไม่แก้หลังจากสร้าง
- Link generously — ทุก concept/entity ที่ mention กันควร wikilink ถึงกัน
- ถ้า slug ซ้ำ → เพิ่ม suffix `-2`
- Concept/entity page ที่มีอยู่แล้ว → อัปเดต `## Mentioned In` แทนสร้างใหม่
- ไม่ต้องรอ confirm จาก Gap — รายงาน inventory แล้วเริ่มทำเลย
