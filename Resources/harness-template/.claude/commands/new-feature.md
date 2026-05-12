# /new-feature [name]

Scaffold และ execute feature ผ่าน full planner → coder → reviewer pipeline

## Usage

```
/new-feature [feature-name]
/new-feature user-authentication
/new-feature payment-integration
```

## Steps

### Step 1 — Load Context

อ่านก่อนทุกครั้ง:
- `wiki/architecture.md`
- `wiki/coding_rules.md`

### Step 2 — Planner Phase

เรียก planner agent:
- รับ feature name + description จากผู้ใช้ (ถ้ายังไม่ได้ระบุ ถามก่อน)
- Output: structured task list ตาม planner output schema
- **หยุดรอผู้ใช้ approve task list** ก่อนไป Step 3

### Step 3 — Coder Phase (per task)

สำหรับแต่ละ task ใน task list (ตาม depends-on order):
- เรียก coder agent พร้อม task spec
- Coder output code diff
- **หยุด** รอ reviewer approve ก่อนไป task ถัดไป

### Step 4 — Reviewer Phase (per task)

- เรียก reviewer agent พร้อม coder output
- ถ้า ✅ approve → ไป task ถัดไป (หรือ done ถ้าเป็น task สุดท้าย)
- ถ้า ❌ request-changes → ส่ง feedback กลับ coder → loop ไม่เกิน 2 รอบ
  - ถ้า loop เกิน 2 รอบ: escalate ถามผู้ใช้

### Step 5 — Done

- รายงาน summary: tasks completed, files changed
- ถ้า reviewer อัปเดต wiki → แจ้งผู้ใช้ว่า wiki ถูก update แล้ว
