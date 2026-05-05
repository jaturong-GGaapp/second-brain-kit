---
name: session-to-wiki
platform: claude-ai
updated: 2026-04-28
description: >
  แปลง Claude.ai conversation หรือ session ให้เป็น structured note พร้อม ingest ลง Obsidian vault ของ Gap
  ใช้ skill นี้ทันทีเมื่อ Gap พูดว่า "เก็บ session นี้", "save to wiki", "ingest", "บันทึก conversation นี้",
  "เอา session นี้ใส่ vault", "สรุป session", หรือเมื่อจบ conversation แล้วมีความรู้/การตัดสินใจที่ควรเก็บไว้
  แม้ Gap จะไม่ได้พูดคำเหล่านี้ตรงๆ แต่ถ้าบริบทชัดว่าอยากเก็บ conversation → ใช้ skill นี้เลย
---

# Session to Wiki (Claude.ai version)

> **Note:** นี่คือ Claude.ai version — output เป็น markdown block สำหรับ copy-paste ลง Obsidian
> Claude Code version (auto-write): `~/.claude/skills/session-to-wiki/SKILL.md`

แปลง session → structured markdown พร้อม paste ลง Obsidian

---

## Step 1 — Detect ประเภท Session

อ่าน conversation แล้ว classify เป็น 1 ใน 2 ประเภท:

| ประเภท | ลักษณะ | Output path |
|--------|--------|-------------|
| **Knowledge** | มี framework, analysis, research, how-to, decision | `wiki/` หรือ `Resources/` |
| **Personal** | มี insight, reflection, ตัดสินใจส่วนตัว, feeling | เพิ่มใน daily note |

ถ้าไม่ชัด → เลือก Knowledge เป็น default

---

## Step 2 — Extract จาก Session

ดึงออกมาให้ครบ:
- **หัวข้อหลัก** คืออะไร
- **Key decisions** ที่ตัดสินใจไปใน session
- **Key takeaways** ที่ควรจำ
- **Action items** ที่ต้องทำต่อ
- **Vault ที่เหมาะ:** PersonalBrain / StartupBrain

---

## Step 3 — Output

### ถ้าเป็น Knowledge → Wiki Note

บอก path แล้ว output markdown block:

```
**Vault:** [PersonalBrain / StartupBrain]
**Path:** `wiki/[topic-slug].md`
หรือ   `Resources/[category]/[topic-slug].md`
```

```markdown
---
title: "[ชื่อ topic]"
type: source
tags: [tag1, tag2]
created: YYYY-MM-DD
session: true
---

## Summary
[สรุปใจความหลักของ session ใน 2-3 ประโยค]

## Key Takeaways
- [สิ่งที่ควรจำ]
- [สิ่งที่ควรจำ]

## Decisions Made
- [การตัดสินใจที่เกิดขึ้นใน session]

## Action Items
- [ ] [สิ่งที่ต้องทำต่อ]

## Connections
- [[concepts/X]]
- [[sources/Y]]
```

---

### ถ้าเป็น Personal → Journal Patch

บอกว่าเพิ่มใน section ไหนของ daily note วันนี้:

```
**Path:** `Journal/Daily/YYYY-MM-DD.md`
**เพิ่มใน section:** [Meaning / Win / Improve]
```

```markdown
### 💡 Session Insight — [หัวข้อ]
[insight หรือ reflection จาก session]
```

---

## Edge Cases

- **Session มีทั้ง knowledge และ personal** → output 2 block แยกกัน บอก path ของแต่ละก้อน
- **Session ยาวมาก** → สรุปเฉพาะ insight ที่ยังใช้ได้ในอนาคต ไม่ต้อง copy ทุกอย่าง
- **Gap บอก context เพิ่ม** → ใช้ context นั้นปรับ tags และ Connections

---

## ตัวอย่าง

**Input:** "เก็บ session นี้ — คุยเรื่อง export CSV จาก Google Sheet"

**Output:**
```
Vault: PersonalBrain
Path: Resources/Finance/google-sheet-csv-export.md
```
```markdown
---
title: "Google Sheet → CSV Export สำหรับ RAG"
type: source
tags: [finance, google-sheets, csv, RAG, claude-code]
created: 2026-04-28
session: true
---

## Summary
วิธี export Google Sheet ที่จด income/expense ออกมาเป็น CSV
สำหรับใช้กับ Claude Code และ RAG pipeline

## Key Takeaways
- Export เฉพาะ summary by category ไม่ต้องเอา raw transactions
- ทำ export tab แยกใน Sheet เพื่อ normalize format ก่อน export
- ต้องการ 2 ไฟล์: finance_summary.csv และ finance_debt.csv

## Decisions Made
- ไม่เอา transaction จริง — วิเคราะห์เองบางส่วนดีกว่า
- date format ต้องเป็น ISO YYYY-MM-DD

## Action Items
- [ ] สร้าง export tab ใน Google Sheet
- [ ] Export finance_summary.csv และ finance_debt.csv

## Connections
- [[Areas/Finance]]
- [[Projects/second-brain-setup]]
```
