---
description: Session Capture to Vault — แปลง conversation → wiki pages (lightweight)
---

# /session-to-wiki — Session Capture to Vault

แปลง conversation ปัจจุบัน → wiki pages ครบชุดแบบ lightweight: source + entity/concept stubs

**ต่างจาก deep-wiki-ingest:** skill นี้ทำเร็ว เหมาะกับ session สั้นหรือเนื้อหาไม่ซับซ้อน — สร้าง concept/entity pages แบบ stub (50–100 คำ) แทนที่จะเป็น full pages — ถ้าต้องการละเอียดกว่านี้ ใช้ `/deep-wiki-ingest` แทน

Trigger: เมื่อ user พูดว่า "เก็บ session นี้", "save to wiki", "ingest", "บันทึก session",
"เอา session นี้ใส่ vault", "สรุป session" หรือบริบทชัดว่าอยากเก็บ conversation

---

## Step 0 — Load Context + Pending Check (ทำก่อนเริ่ม ไม่ต้องบอก user)

อ่าน:
1. `wiki/index.md` — รู้ว่า pages ไหนมีอยู่แล้ว (ไม่สร้างซ้ำ)
2. `raw/index.md` — ingest registry ของ raw files
3. `.claude/skills/shared/obsidian-markdown/SKILL.md` — Obsidian syntax reference

**Pending check:**
- list files ใน `raw/` filesystem (ยกเว้น `assets/`, `index.md`)
- candidate slug = filename - extension
- ถ้า `[[candidate slug]]` ไม่อยู่ใน `raw/index.md` → pending
- ถ้ามี pending list ไม่ว่าง:
  - แจ้ง user: "⏳ Found N pending raw files (in raw/ but not in raw/index.md): [list]"
  - ถาม: "Would you like to ingest these now or skip?"
- ถ้าว่าง → ดำเนินการต่อ

---

## Step 0.5 — Save Raw Content + Register

ก่อนประมวลผลใดๆ:

1. **เขียน raw file** — `raw/YYYY-MM-DD-slug.md` (content immutable, slug เดียวกับ wiki/sources/):
   ```markdown
   ---
   title: "[Title]"
   type: raw
   date: YYYY-MM-DD
   ---

   [original content as-is — ไม่แปลง ไม่ตัด ไม่เพิ่ม]
   ```

2. **Register ใน raw/index.md** — เพิ่ม row ใต้ heading `## YYYY-MM`:
   ```markdown
   | [[YYYY-MM-DD-slug]] | Title | YYYY-MM-DD | Format | YYYY-MM-DD |
   ```
   - สร้าง heading + table header ใหม่ถ้าเดือนนั้นยังไม่มี
   - อัปเดต counter ใน header file: `_N raw files registered_`

raw file content คือต้นฉบับ immutable — wiki/sources/ คือ processed version
**ห้ามแก้ไข raw file หลังจากสร้าง** — update เฉพาะ raw/index.md เท่านั้น

---

## Step 1 — Classify Session

อ่าน conversation แล้ว classify:

| ประเภท | ลักษณะ | Output |
|--------|--------|--------|
| **Knowledge** | framework, analysis, research, how-to, decision | `wiki/sources/` หรือ `Resources/` |
| **Personal** | insight, reflection, ตัดสินใจส่วนตัว, feeling | เพิ่มใน daily note วันนี้ |

ถ้าไม่ชัด → Knowledge เป็น default
ถ้ามีทั้งคู่ → ทำทั้ง 2 block

---

## Step 2 — Extract

ดึงจาก conversation:
- หัวข้อหลัก
- Key decisions ที่ตัดสินใจไปใน session
- Key takeaways ที่ควรจำ
- Action items ที่ต้องทำต่อ
- Tags ที่เหมาะสม
- Concepts ใหม่ที่ยังไม่มี page (เช็คจาก index.md)
- Entities ใหม่ที่ยังไม่มี page (เช็คจาก index.md)
- Connections ไปยัง wiki pages ที่มีอยู่แล้ว

---

## Step 3 — เขียนไฟล์

### Knowledge → wiki/sources/

**Path:** `wiki/sources/YYYY-MM-DD-short-kebab-title.md`

เขียนไฟล์ด้วย template:

```markdown
---
title: "[ชื่อ topic]"
type: source
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [self]
session: true
---

# [ชื่อ topic]

| Field | Value |
|-------|-------|
| **Format** | note (session capture) |
| **Date** | YYYY-MM-DD |

## Summary
[สรุปใจความหลักของ session ใน 2-3 ประโยค]

## Key Takeaways
- [สิ่งที่ควรจำ]

## Decisions Made
- [การตัดสินใจที่เกิดขึ้นใน session]

## Action Items
- [ ] [สิ่งที่ต้องทำต่อ]

## Connections
- [[concepts/X]]
- [[sources/Y]]
```

ถ้าเนื้อหาเหมาะกับ `Resources/` มากกว่า (how-to, reference) → ใช้ path `Resources/[category]/[slug].md` แทน และข้าม wiki/index.md update

---

### Personal → daily note patch

เพิ่มใน `Journal/Daily/YYYY-MM-DD.md` (วันนี้):

```markdown
### 💡 Session Insight — [หัวข้อ]
[insight หรือ reflection จาก session]
```

ถ้าไม่มีไฟล์วันนี้ → สร้างใหม่ก่อน แล้วค่อย append

---

## Step 3b — Concept Stubs (ถ้ามี concepts ใหม่)

สำหรับทุก concept ใหม่ที่พบใน Step 2 (ยังไม่มี page ใน index.md):

**Path:** `wiki/concepts/[ConceptName].md`

เขียน stub 50–100 คำ:

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

[คำนิยาม 1–2 ประโยค]

## Mentioned In
- [[sources/slug]]

## See Also
- [[concepts/X]]
```

---

## Step 3c — Entity Stubs (ถ้ามี entities ใหม่)

สำหรับทุก entity ใหม่ที่พบใน Step 2 (ยังไม่มี page ใน index.md):

**Path:** `wiki/entities/[EntityName].md`

เขียน stub 50–100 คำ:

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

[คำอธิบาย 1 ประโยค — ประเภท, บทบาท]

## Relevance to user's Work
[เชื่อมกับอะไร]

## Mentioned In
- [[sources/slug]]
```

---

## Step 4 — Update wiki/index.md

อ่าน `wiki/index.md` แล้วเพิ่ม rows ใน sections ที่เกี่ยวข้อง:

**Sources table:**
```
| [[sources/SLUG]] | Title | YYYY-MM-DD | note (session capture) | tags |
```

**Entities table** (ถ้าสร้าง entity stubs):
```
| [[entities/Name]] | One-line summary |
```

**Concepts table** (ถ้าสร้าง concept stubs):
```
| [[concepts/Name]] | One-line summary |
```

อัปเดต header count: `_Last updated: YYYY-MM-DD — N sources · N entities · N concepts · N analyses_`

ข้าม step นี้ถ้า output ไปที่ `Resources/` หรือ daily note เท่านั้น

---

## Step 5 — Append wiki/log.md

Append ท้าย `wiki/log.md`:

```
## [YYYY-MM-DD] ingest | [Title]
- Added: [[sources/SLUG]], raw/SLUG.md
- Created concepts: [[concepts/X]], ... (ถ้ามี)
- Created entities: [[entities/A]], ... (ถ้ามี)
- Tags: [tags]
- session: true
```

ข้าม step นี้ถ้า output ไปที่ `Resources/` หรือ daily note

---

## Step 6 — Report

รายงานในรูปแบบ CLAUDE.md INGEST convention:

```
## [YYYY-MM-DD] ingest | [Title]

- Added:   [[sources/SLUG]], raw/SLUG.md
- Created: [[concepts/X]], [[entities/Y]] (stubs — ขยายได้ด้วย /deep-wiki-ingest)
- Updated: [[wiki/index.md]] (N sources · N entities · N concepts), [[wiki/log.md]]
- Connections: [[concepts/X]], [[entities/Y]]
```

---

## กฎ

- ตอบภาษาไทย เป็นกันเอง
- เขียนไฟล์จริงทันที ไม่ต้อง output markdown block ให้ copy-paste
- raw/ files ที่สร้างใหม่ → write-once ไม่แก้หลังจากสร้าง
- ถ้า slug ซ้ำกับที่มีอยู่แล้วใน index → เพิ่ม suffix `-2`
- Concept/entity page ที่มีอยู่แล้ว → อัปเดต `## Mentioned In` แทนสร้างใหม่
- ไม่ต้องรอ confirm จาก user — ทำเลยทันที