---
name: roi-analyzer
description: Decision support tool — ช่วยตัดสินใจว่า "คุ้มไหม?" โดยเทียบ options อย่างมีโครงสร้าง ใช้เมื่อ user ถามว่าเลือก A หรือ B, worth it ไหม, หรือต้องการประเมิน ROI ของเวลา/เงิน/แรง
compatibility: Designed for Claude Code (or similar products)
---

# ROI Analyzer — Decision Support Tool

**Role:** ช่วยตัดสินใจว่า "คุ้มไหม?" โดยเทียบ options อย่างมีโครงสร้าง — ไม่ใช่แค่ความเห็น

---

## When to Use

- เลือกระหว่าง 2+ ทางเลือก ("ทำ A หรือ B ดีกว่า?")
- ประเมินว่าสิ่งที่จะทำ "worth it" ไหม ("เรียน course นี้คุ้มไหม?")
- ตัดสินใจลงทุนเวลา, เงิน, หรือแรง

---

## Framework

### Step 1 — ระบุ options
ถามให้ชัดว่าเทียบอะไรกับอะไร — ถ้ามีแค่ option เดียว ให้ถามว่า "ถ้าไม่ทำ จะทำอะไรแทน?" เพื่อสร้าง baseline

### Step 2 — ถามตัวแปรสำคัญ (per option)

| ตัวแปร | คำถาม |
|--------|-------|
| **Cost** | ต้องลงทุนเท่าไหร่? (เงิน + เวลา + แรง) |
| **Benefit** | ได้อะไรกลับมา? เป็น concrete ที่สุดเท่าที่ทำได้ |
| **Timeline** | เมื่อไหร่จะเห็นผล? |
| **Risk** | ถ้าไม่ work out — เสียอะไร? กลับมาได้ไหม? |
| **Opportunity cost** | ถ้าเลือก option นี้ → ต้องละทิ้งอะไร? |

### Step 3 — เปรียบเทียบ

ไม่ต้อง calculate จริงทุกครั้ง — ใช้ judgement ที่มีโครงสร้าง:

- **Upside vs Downside** — best case vs worst case ต่างกันมากไหม?
- **Reversibility** — ตัดสินใจผิดแล้วกลับได้ไหม? ถ้าได้ → รับความเสี่ยงได้มากขึ้น
- **Time to signal** — รู้เร็วไหมว่าได้ผลหรือเปล่า? ถ้ารู้เร็ว → risk ต่ำกว่า
- **Asymmetry** — มี option ที่ upside สูงมาก downside จำกัดไหม? → favor นั้น

### Step 4 — แนะนำ

ระบุชัดเจนว่าแนะนำ option ไหน และ **เหตุผลหลัก 1-2 ข้อ** — ไม่ใช่ "ขึ้นอยู่กับหลายปัจจัย"

ถ้า genuinely 50/50 → บอกตรงว่าอะไรคือ deciding factor ที่ user ต้องรู้เพิ่ม

---

## Output Format

```
## Decision: [ชื่อการตัดสินใจ]

| | Option A | Option B |
|--|----------|----------|
| Cost | | |
| Benefit | | |
| Timeline | | |
| Risk | | |
| Opportunity cost | | |

**Recommendation:** [Option X]
**เหตุผลหลัก:** [1-2 ข้อที่ชี้ขาด]
**Caveat:** [สิ่งที่อาจเปลี่ยน recommendation ถ้าข้อมูลต่างออกไป]
```

สำหรับ quick question ที่ไม่ต้องการ full table — ตอบสั้นได้: recommendation + เหตุผล + caveat
