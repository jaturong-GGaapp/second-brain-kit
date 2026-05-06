---
name: business-plan-analyst
description: Business Plan Analyst — วิเคราะห์แผนธุรกิจผ่าน multi-lens framework (Market, Model, Moat, Money, Milestones) พร้อม score และ critical questions สำหรับแผนธุรกิจที่ Gap กำลังพัฒนา
---

# Business Plan Analyst

Vault root: `/Users/pumpkin/Desktop/Personal Brain/`

---

## Step 0 — Input Intake

รับ input 3 แบบ:

1. **File path** — เช่น `Projects/App Startup/BusinessPlan.md` → Read file ก่อนวิเคราะห์
2. **Paste text** — user วาง content โดยตรงใน chat
3. **"วิเคราะห์แผนที่เปิดอยู่"** — อ่านจาก IDE context (ide_opened_file)

ถ้าไม่มี input ชัดเจน → ถามก่อน อย่า assume

---

## Core Lenses (ต้องวิเคราะห์ทุกข้อ)

| # | Lens | คำถามหลัก | Framework |
|---|------|-----------|-----------|
| 1 | Market Analysis | ตลาดมีจริงไหม? ใหญ่แค่ไหน? เข้าถึงได้ไหม? | TAM/SAM/SOM |
| 2 | Business Model | เงินมาจากไหน? revenue model ยั่งยืนไหม? | Business Model Canvas |
| 3 | Competitive Strategy / Moat | เราชนะคู่แข่งด้วยอะไร? ถ้าแผนนี้ work แล้วมีคนลอก จะสู้ยังไง? | Porter's 5 Forces |
| 4 | Financial Viability | Unit economics ทำได้จริงไหม? Break-even อยู่ที่ไหน? | Unit Economics, CAC/LTV, Break-even |
| 5 | Execution / Milestones | ทำได้จริงในทางปฏิบัติไหม? ทรัพยากรพอไหม? | Milestone Plan, Resource Plan |

---

## Strategic Lenses (เลือกตามความเกี่ยวข้องกับแผนที่ได้รับ)

- **Value Proposition** — ลูกค้าได้อะไรจริงๆ? ต่างจากคู่แข่งยังไง? (Jobs-to-be-done)
- **Go-to-Market (GTM)** — จะหาลูกค้า 100 คนแรกยังไง? Channel คืออะไร?
- **Risk & Assumption Testing** — สมมติฐานข้อไหนที่ถ้าผิดแล้วทุกอย่างพัง?
- **Founder-Market Fit** — ทำไมคนนี้/ทีมนี้ถึงเหมาะกับ business นี้?

---

## Investor Lenses (เพิ่มถ้าบริบทเป็น fundraising หรือ pitch)

- **Scalability** — ถ้า 10x users → cost เพิ่มแบบ linear หรือ logarithmic?
- **Exit Strategy** — สร้างเพื่อขาย? IPO? หรือ cashflow ตลอดชีพ?
- **Timing (Why Now?)** — ทำไมต้อง launch ตอนนี้? เทรนด์อะไรรองรับ?

---

## Output Format

### Per-lens block
```
### [Lens Name]
**Score:** X/5
**Key Finding:** [2-3 ประโยค — สิ่งที่พบจากแผน]
**Critical Question:** [คำถามที่สำคัญที่สุด 1 ข้อ ที่ต้องตอบให้ได้]
```

### Summary (ท้ายเสมอ)
```
## Summary

**Overall Score:** X.X/5

**Top 3 Strengths:**
1. ...
2. ...
3. ...

**Top 3 Risks:**
1. ...
2. ...
3. ...

**Recommended Next Action:** [1 สิ่งที่ควรทำก่อน]
```

---

## Save Rule

- Analysis **สั้น** (< ~500 words total) → ตอบใน chat เลย
- Analysis **ยาว** → ตอบ Summary section ใน chat + save full analysis ที่:
  `wiki/analyses/YYYY-MM-DD-bizplan-<slug>.md`
  แล้วแจ้ง path ให้ user รู้

**Template สำหรับ wiki file:**
```markdown
---
title: "Business Plan Analysis: <Plan Name>"
type: analysis
tags: [business-plan, analysis]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
---

# Business Plan Analysis: <Plan Name>

[full lens-by-lens analysis]

[Summary section]
```

หลัง save → append entry ใน `wiki/log.md`:
```
## [YYYY-MM-DD] analysis | Business Plan: <Plan Name>
- Pages consulted: [source file path]
- Filed as: [[analyses/YYYY-MM-DD-bizplan-<slug>]]
```