---
description: Weekly Review — สรุปอาทิตย์ + อัปเดต current-state.md
---

# /weekly-review — Weekly Review

ทำตามลำดับนี้เมื่อถูก invoke — **รันทั้งหมดโดยไม่หยุดรอ input ยกเว้นขั้นตอนที่ระบุ**

---

## Step 0 — Internalize Sub-skills (ทำก่อนเริ่ม ไม่ต้องบอก user)

อ่านไฟล์เหล่านี้เพื่อ internalize lens ก่อน execute — ไม่ต้อง output อะไร:

1. `.claude/skills/journal-agent/reflect/SKILL.md` — lens ของ compassionate pattern-finder: หา pattern ข้ามสัปดาห์
2. `.claude/skills/shared/obsidian-markdown/SKILL.md` — Obsidian syntax reference

ใช้ lens เหล่านี้ตลอด session

---

## Step 1 — อ่าน Daily Notes (RAG)

อ่าน `Journal/Daily/*.md` ทั้งหมดที่มีใน 7 วันล่าสุด
ถ้าวันไหนไม่มีไฟล์ → ข้าม ไม่ต้อง error

---

## Step 2 — อ่าน State Files (Context)

อ่าน `Journal/current-state.md` ก่อน — แล้ว find state files ที่เหลือทั้งหมดด้วย:
```
find Areas/ Projects/ -name "state-*.md"
```
อ่านทุกไฟล์ที่พบ

---

## Step 3 — Synthesize (ทำภายใน ไม่แสดงผล raw)

จาก daily notes 7 วัน + state files สรุป:
1. **Wins** — สิ่งที่ทำได้ดีในสัปดาห์นี้
2. **Blockers** — อะไรที่ติดซ้ำหรือไม่คืบหน้า
3. **Patterns** — พฤติกรรมหรือ theme ที่สังเกตได้
4. **Domain status** — Areas / Projects มีความเปลี่ยนแปลงอะไร

---

## Step 4 — อัปเดต State Files

สำหรับแต่ละ state file ที่อ่านใน Step 2:

1. เช็ค `updated:` ใน frontmatter เทียบกับวันนี้
2. ถ้าเก่าเกิน 7 วัน → patch ไฟล์นั้น:
   - อัปเดต `updated:` เป็นวันนี้
   - อัปเดต `## Blockers` จาก pattern ที่เจอใน daily notes (ถ้าไม่มีข้อมูลใหม่ → คงเดิม)
3. **ไม่แตะ** checklist items, phase, หรือ Next Actions — นั่นเป็นหน้าที่ Gap

---

## Step 5 — อัปเดต current-state.md

เขียนทับ `Journal/current-state.md` ด้วย state ล่าสุด ใช้ format เดิมของไฟล์ (อ่านก่อนเขียน)

ใช้ข้อมูลจริงจาก state files + daily notes — ถ้าไม่มีข้อมูลจริง ใช้ "—" ไม่ต้องเดา

---

## Step 6 — เขียน Weekly Summary

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

## Step 7 — ถาม Focus Week หน้า

"สัปดาห์หน้าอยากโฟกัสอะไรเป็นพิเศษ? (หรือ skip ถ้าโอเคกับที่ recommend ไว้)"

ถ้า user ให้ input → อัปเดต section Focus Week หน้าในไฟล์

---

## Step 8 — สรุปให้ user

```
Weekly review เสร็จแล้ว

📁 อัปเดต: Journal/current-state.md
📁 อัปเดต: state files ที่เก่าเกิน 7 วัน (N ไฟล์)
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
- ถ้า daily notes ไม่มีเลย → บอก user แล้วสร้าง current-state.md จาก state files อย่างเดียว
- ไม่แสดง raw content ของไฟล์ที่อ่าน — แสดงแค่ synthesis