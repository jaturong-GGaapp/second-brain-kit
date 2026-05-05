---
description: Weekly RAG Review — สรุปอาทิตย์ + อัปเดต current-state.md
---

# /weekly-review — Weekly RAG Review

ทำตามลำดับนี้เมื่อถูก invoke — **รันทั้งหมดโดยไม่หยุดรอ input ยกเว้นขั้นตอนที่ระบุ**

Vault root: `/Users/pumpkin/Desktop/Personal Brain/`

---

## Step 0 — Internalize Sub-skills (ทำก่อนเริ่ม ไม่ต้องบอก Gap)

อ่านไฟล์เหล่านี้เพื่อ internalize lens ก่อน execute — ไม่ต้อง output อะไร:

1. `.claude/skills/journal-agent/reflect.md` — lens ของ compassionate pattern-finder: หา pattern ข้ามสัปดาห์
2. `.claude/skills/shared/obsidian-markdown/SKILL.md` — Obsidian syntax reference

ใช้ lens เหล่านี้ตลอด session

---

## Step 1 — อ่าน Daily Notes (RAG)

อ่าน `Journal/Daily/*.md` ทั้งหมดที่มีใน 7 วันล่าสุด
ถ้าวันไหนไม่มีไฟล์ → ข้าม ไม่ต้อง error

---

## Step 2 — อ่าน State Files (Context)

อ่านทุกไฟล์ต่อไปนี้:
- `Journal/current-state.md`
- `Areas/การเงิน-แคนาดา/state-การเงิน-แคนาดา.md`
- `Areas/จัดการหนี้/state-จัดการหนี้.md`
- `Areas/การลงทุน/state-การลงทุน.md`
- `Areas/สุขภาพ/state-สุขภาพ.md`
- `Areas/พัฒนาตนเอง/state-พัฒนาตนเอง.md`
- `Areas/แผนอนาคต/state-แผนอนาคต.md`
- `Projects/App Startup/state-app-startup.md`
- `Projects/พัฒนาที่ดินไทย/state-พัฒนาที่ดินไทย.md`
- `Projects/Second Brain/state-second-brain.md`

---

## Step 3 — Synthesize (ทำภายใน ไม่แสดงผล raw)

จาก daily notes 7 วัน + state files สรุป:
1. **Wins** — สิ่งที่ทำได้ดีในสัปดาห์นี้
2. **Blockers** — อะไรที่ติดซ้ำหรือไม่คืบหน้า
3. **Patterns** — พฤติกรรมหรือ theme ที่สังเกตได้
4. **Domain status** — Areas / Projects มีความเปลี่ยนแปลงอะไร

---

## Step 4 — อัปเดต current-state.md

เขียนทับ `Journal/current-state.md` ด้วย state ล่าสุด ใช้ format เดิมของไฟล์ (อ่านก่อนเขียน)

ใช้ข้อมูลจริงจาก state files + daily notes — ถ้าไม่มีข้อมูลจริง ใช้ "—" ไม่ต้องเดา

---

## Step 5 — เขียน Weekly Summary

เขียน `Journal/Weekly-Review/YYYY-WXX.md`
(XX = เลขอาทิตย์ของปี เช่น W18)

```markdown
---
date: YYYY-MM-DD
week: YYYY-WXX
type: weekly-review
---

# Weekly Review — YYYY-WXX

## ✅ Wins
- [win 1]
- [win 2]

## 🔴 Blockers
- [blocker 1]

## 🔁 Patterns
- [pattern ที่สังเกตได้]

## 📊 Domain Status
| Domain | Status | Movement |
|--------|--------|----------|
| Life Ops | | |
| Startup | | |
| Thailand | | |
| Knowledge | | |

## 🎯 Focus Week หน้า
1. [priority 1]
2. [priority 2]
3. [priority 3]

## Notes
[อะไรก็ตามที่ไม่เข้า category ด้านบน]
```

---

## Step 6 — ถาม Focus Week หน้า

"สัปดาห์หน้าอยากโฟกัสอะไรเป็นพิเศษ? (หรือ skip ถ้าโอเคกับที่ recommend ไว้)"

ถ้า Gap ให้ input → อัปเดต section Focus Week หน้าในไฟล์

---

## Step 7 — สรุปให้ Gap

```
Weekly review เสร็จแล้ว

📁 อัปเดต: Journal/current-state.md
📁 สร้าง: Journal/Weekly-Review/YYYY-WXX.md

สัปดาห์นี้:
• Wins: [1-2 bullet]
• Blockers: [1-2 bullet]
• Pattern: [1 ประโยค]

Focus week หน้า: [top 3]
```

---

## กฎ

- ตอบเป็นภาษาไทย เป็นกันเอง
- ใช้ข้อมูลจริงจากไฟล์เท่านั้น ไม่เดา
- ถ้า daily notes ไม่มีเลย → บอก Gap แล้วสร้าง current-state.md จาก state files อย่างเดียว
- ไม่แสดง raw content ของไฟล์ที่อ่าน — แสดงแค่ synthesis