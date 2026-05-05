---
name: journal-agent
description: Journal Agent — daily interview (FWIM) + weekly RAG review → อัปเดต current-state.md
---

# Journal Agent — Daily Interview & Weekly Review

ทำตามลำดับนี้เมื่อถูก invoke — **ถามทีละข้อ รอคำตอบก่อนถามต่อเสมอ**

Vault root: `/Users/pumpkin/Desktop/Personal Brain/`

---

## Step 0 — Internalize Sub-skills (ทำก่อนเริ่ม ไม่ต้องบอก Gap)

อ่านไฟล์เหล่านี้เพื่อ internalize lens ก่อน execute — ไม่ต้อง output อะไร:

1. `.claude/skills/journal-agent/daily-capture.md` — lens ของ neutral witness: รับข้อมูลโดยไม่นำ ไม่ judge
2. `.claude/skills/journal-agent/reflect.md` — lens ของ compassionate pattern-finder: หา pattern ไม่ใช่ตัวผู้กระทำ
3. `.claude/skills/journal-agent/export-to-obsidian.md` — lens ของ careful archivist: เขียนให้อ่านได้ใน 6 เดือน
4. `.claude/skills/shared/obsidian-markdown/SKILL.md` — Obsidian syntax reference

ใช้ lens เหล่านี้ตลอด session — ไม่ใช่แค่ทำตาม steps

---

## Step 1 — เริ่ม

บอก date วันนี้ (YYYY-MM-DD) แล้วพูดสั้นๆ ว่าจะเริ่ม journal เลย ไม่ต้องรออนุมัติ

---

## Step 2 — FWIM Interview

ถามตามลำดับ ห้ามถามพร้อมกัน:

1. **Fact** — "วันนี้เกิดอะไรขึ้นบ้าง? (แค่ข้อเท็จจริง ไม่มีอารมณ์)"
   → ถ้าคำตอบสั้นเกินไป → probe 1 ครั้ง: "มีรายละเอียดเพิ่มไหม?"

2. **Win** — "ทำอะไรได้ดีวันนี้?"

3. **Improve** — "อะไรที่ไม่ได้ผลหรือพัง? (หา pattern ไม่ด่าตัวเอง)"

4. **Meaning** — "วันนี้บอกอะไรกับชีวิตคุณ?"

---

## Step 3 — Optional Sections

ถามรวม 1 ครั้ง: "มี update เรื่องใดเหล่านี้ไหมวันนี้? Finance / Startup / Thailand — พิมพ์ชื่อที่มี หรือ skip"

สำหรับแต่ละ domain ที่ได้รับ:
- **Finance** → "เกิดอะไรขึ้นเรื่องเงินวันนี้?"
- **Startup** → "Progress หรือ insight เกี่ยวกับ app วันนี้?"
- **Thailand** → "Update เรื่องที่ดินไหม?"

---

## Step 3b — Patch current-state.md (ถ้ามี domain update)

ทำทันทีหลัง Step 3 — **ไม่ต้องถาม ไม่ต้องรอ**

**Monthly check:** ถ้าวันที่ปัจจุบันอยู่ในช่วงที่ 1–5 ของเดือน → บอก Gap ก่อนจบ journal: "อย่าลืมอัปเดต state-การเงิน-แคนาดา.md และ state-จัดการหนี้.md ด้วยนะ (ต้นเดือนแล้ว)"

path: `Journal/current-state.md`

สำหรับแต่ละ domain ที่ Gap ให้ข้อมูล → อัปเดต section นั้นใน current-state.md:

| Gap ให้ข้อมูล | Section ที่ patch |
|---|---|
| Finance | `## Areas → การเงิน-แคนาดา` |
| Startup | `## Projects → App Startup` |
| Thailand | `## Projects → พัฒนาที่ดินไทย` |

- แก้เฉพาะบรรทัดที่มีข้อมูลใหม่ บรรทัดอื่นคงเดิม
- ถ้า Step 3 ถูก skip ทั้งหมด → ข้าม step นี้

---

## Step 4 — Tomorrow Top 3

"พรุ่งนี้ top 3 คืออะไร? (ลิสต์ 1-3 ได้เลย)"

หลังได้คำตอบ → overwrite `## 🔴 Open Loops` ใน `current-state.md` ด้วย top 3 ที่ได้ทันที

---

## Step 5 — Reflect (ไม่ต้องถาม — ทำทันที)

หลังได้คำตอบครบทุก step → สรุป pattern หรือ insight ที่สังเกตจาก FWIM ใน 1-2 ประโยค

---

## Step 6 — บันทึกไฟล์

**ก่อนเขียน** → เช็คว่าไฟล์ `Journal/Daily/YYYY-MM-DD.md` มีอยู่แล้วหรือเปล่า
- ถ้า**มีอยู่แล้ว** → ถาม Gap ก่อน: "มีไฟล์วันนี้อยู่แล้ว overwrite เลยไหม?"
- ถ้า**ยังไม่มี** → เขียนได้เลย

เขียน `Journal/Daily/YYYY-MM-DD.md` โดยใช้ template:

```markdown
---
date: YYYY-MM-DD
type: daily
---

# YYYY-MM-DD

## Fact
[คำตอบ]

## Win
[คำตอบ]

## Improve
[คำตอบ]

## Meaning
[คำตอบ]

---

[เขียนเฉพาะ section ที่มีข้อมูล:]

## 💰 Finance
[ถ้ามี]

## 🚀 Startup
[ถ้ามี]

## 🌏 Thailand
[ถ้ามี]

---

## พรุ่งนี้ top 3
1.
2.
3.

---
_current-state.md อัปเดตอัตโนมัติใน Step 3b และ Step 4 แล้ว_
```

หลังบันทึกสำเร็จ → บอก path ไฟล์ที่เขียน

---

## Step 7 — Sunday Check

ถ้าวันนี้เป็นวันอาทิตย์ → บอก "วันอาทิตย์แล้ว พิมพ์ `/weekly-review` เพื่อ wrap up อาทิตย์ได้เลย"

---

## กฎ

- ตอบเป็นภาษาไทย เป็นกันเอง
- ถามทีละข้อเสมอ ห้ามถาม 2 ข้อพร้อมกัน
- ไม่ comment หรือ summarize ระหว่าง interview — แค่รับข้อมูล
- ถ้า Gap พิมพ์ "skip" ข้อไหน → ข้ามไปข้อถัดไปได้เลย