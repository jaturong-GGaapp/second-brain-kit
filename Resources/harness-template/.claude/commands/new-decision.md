# /new-decision [topic]

สร้าง Architecture Decision Record (ADR) สำหรับ technical decision ใหม่

## Usage

```
/new-decision [topic]
/new-decision database-choice
/new-decision state-management-library
/new-decision monorepo-vs-polyrepo
```

## Steps

### Step 1 — Gather Context

ถามผู้ใช้ (ถ้าไม่ได้ระบุ):
1. **Problem:** ปัญหาหรือ context ที่นำมาสู่ decision นี้คืออะไร?
2. **Options considered:** ตัวเลือกอะไรบ้างที่พิจารณา?
3. **Decision:** เลือกตัวเลือกไหน?
4. **Reasoning:** ทำไมถึงเลือกตัวนั้น?

### Step 2 — Find ADR Number

- List ไฟล์ใน `decisions/` — หา ADR ล่าสุด
- Increment: ถ้า `ADR-003` อยู่แล้ว → ไฟล์ใหม่คือ `ADR-004`

### Step 3 — Create ADR File

สร้าง `decisions/ADR-[NNN]-[topic-slug].md` จาก template `decisions/ADR-000-template.md`

### Step 4 — Update wiki/architecture.md

เพิ่ม reference ใน `## Key Decisions` section:
```markdown
- [Decision title] — see [[decisions/ADR-NNN-topic]]
```

### Step 5 — Confirm

รายงาน:
- ไฟล์ที่สร้าง
- Link ไปยัง ADR ใหม่
