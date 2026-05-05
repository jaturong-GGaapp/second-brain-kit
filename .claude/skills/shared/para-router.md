---
name: para-router
type: shared-skill
used-by: [secretary, note-organizer, journal-agent]
status: active
updated: 2026-05-05
---

# PARA Router

**Role:** classify สิ่งใหม่ที่ user พูดถึง → แนะนำว่าควรเป็น Project / Area / Todo / Resource แล้วให้ user ตัดสินใจ ก่อน scaffold จริง

---

## PARA Definition

| Category | เมื่อไหร่ | Duration |
|---|---|---|
| **Project** | มี end state ชัดเจน + กำลัง active ทำอยู่ตอนนี้ | เสร็จได้ใน ~6–12 เดือน |
| **Area** | ongoing responsibility ไม่มี end date, หรือ horizon > 1–2 ปี | indefinite |
| **Todo** | action เดียว ไม่มี sub-steps | < 1 สัปดาห์ |
| **Resource** | reference material — ไม่ใช่งานที่ต้องทำ | — |

---

## Decision Tree

```
มีสิ่งใหม่ที่ user พูดถึง
│
├─ เป็น action เดียวจบได้ใน < 1 สัปดาห์?
│   └─ YES → Todo (ใส่ใน Next Actions ของ Area/Project ที่เกี่ยวข้อง)
│
├─ เป็น reference / ข้อมูลที่จะดูทีหลัง ไม่ใช่งาน?
│   └─ YES → Resource
│
├─ มี end state ชัดเจน + กำลังจะทำ/ทำอยู่ตอนนี้?
│   ├─ YES + เสร็จได้ใน ~12 เดือน → Project
│   └─ YES + horizon > 2 ปี หรือ blocked indefinitely → Area (pull milestone ออกมาเป็น Todo)
│
└─ ไม่มี end date / เป็น ongoing responsibility?
    └─ YES → Area
```

**Shortcuts:**
- span 4+ ปี (เช่น เรียนรู้ discipline ใหม่) → Area
- PR เดียว, deploy เดียว, config เดียว → Todo ใน Area/Project ที่เกี่ยวข้อง
- blocked indefinitely ("ทำหลัง v2") → Todo หรือ note ใน Area จนกว่าจะ active

> Keep Projects/ lean — มีเฉพาะสิ่งที่ทำอยู่เดือนนี้

---

## Output Format

เมื่อ classify แล้ว — แสดงให้ user confirm ก่อนเสมอ:

```
แนะนำ: [Project / Area / Todo / Resource]
เหตุผล: [1 ประโยค]
Path: [Projects/ชื่อ/ หรือ Areas/ชื่อ/ หรือ next action ใน state file ไหน]

ถูกต้องไหม? ถ้าโอเคจะ scaffold ให้เลย
```

---

## หลังจาก user confirm

| classify เป็น | ขั้นตอนต่อไป |
|---|---|
| **Project** | invoke `/new-claude-project [name]` — scaffold state file + claude-ai workspace |
| **Area** | สร้าง `Areas/[name]/state-[name].md` จาก area-state-template |
| **Todo** | เพิ่มใน `## Next Actions` ของ state file ที่เกี่ยวข้อง |
| **Resource** | บันทึกใน `Resources/` หรือ ingest เข้า wiki ถ้าเป็น knowledge |
