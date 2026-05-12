---
name: app-context
description: Interview protocol สำหรับเก็บ project context ก่อน init-wiki — secretary โหลดเมื่อ Gap ต้องการตั้ง harness หรือ coding project ใหม่
agent: secretary
---

# App Context Skill

เก็บ project context ให้ครบก่อนส่งต่อให้ `/init-wiki`

## ข้อมูลขั้นต่ำ (required)

| หมวด | ต้องการ |
|---|---|
| **Project** | ชื่อ, เป้าหมายหลัก, target user |
| **Tech Stack** | ภาษา, framework, database, hosting |
| **Structure** | monorepo หรือ single app, package/folder หลัก |
| **Phase** | เริ่มใหม่ / มี code แล้ว / refactor |

## ข้อมูลเพิ่มเติม (ยิ่งครบยิ่งดี)

| หมวด | รายละเอียด |
|---|---|
| **Architecture** | package boundaries (X ห้าม import จาก Y), data flow |
| **API** | auth method, base URL, endpoints หลัก |
| **Coding rules** | naming convention, forbidden patterns |
| **Design system** | color palette, spacing base, animation philosophy |
| **Decisions made** | technical decisions ที่ทำไปแล้ว เช่น เลือก library X เพราะ Y |
| **Constraints** | deadline, team size, performance requirements |

## วิธี Interview

1. ถามเป็น batch — ไม่ถามทีละข้อ
2. ถ้า Gap ให้ข้อมูลพอสมควรแล้ว → ถามเฉพาะส่วนที่ขาด
3. ถ้า Gap paste README / PRD / design doc → extract เลย ไม่ถามซ้ำ
4. หลัง required ครบ → สรุป context block พร้อมบอกว่า "ใช้กับ `/init-wiki` ได้เลย"

## Output: Context Block

```
## Project Context: [ชื่อ project]

**Project:** [ชื่อ] — [เป้าหมายสั้นๆ]
**Target user:** [ใคร]
**Phase:** [เริ่มใหม่ / มี code แล้ว / refactor]

**Tech Stack:** [ภาษา, framework, database, hosting]

**Structure:**
[monorepo/single app + folder/package หลัก]

**Package Boundaries:**
[X ห้าม import จาก Y / ยังไม่ได้กำหนด]

**API:**
- Auth: [method]
- Endpoints หลัก: [list หรือ "ยังไม่ได้กำหนด"]

**Coding Rules:**
[naming convention, forbidden patterns ที่รู้]

**Design System:**
[color, spacing, animation / "ยังไม่ได้กำหนด"]

**Decisions Made:**
- [decision 1 — เพราะ reason]

**TODO (ยังไม่รู้/ยังไม่ได้กำหนด):**
- [list]
```
