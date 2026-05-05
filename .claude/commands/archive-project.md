# /archive-project [project-name]

ย้าย project ที่เสร็จแล้วจาก `Projects/` → `Archive/` พร้อม closing summary

---

## When to use

- Project ถึง Definition of Done แล้ว
- Project ถูก cancel หรือ deprioritized อย่างถาวร

---

## Protocol

TODO: implement เมื่อ project แรกเสร็จ

### Step 1 — Confirm closure
### Step 2 — Draft summary.md
### Step 3 — Move files
### Step 4 — Clean up
- ลบ routing ใน `secretary.md` Domain Routing
- ลบ workspace ใน `Resources/claude-ai/[name]/` (หรือ archive ไว้ด้วย?)
- อัปเดต `Journal/current-state.md`

---

## Output structure

```
Archive/[project-name]/
├── state-[project-name].md   ← moved from Projects/
└── summary.md                ← new closing summary
```
