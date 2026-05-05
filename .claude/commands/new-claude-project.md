# /new-claude-project [project-name]

Scaffold workspace ใหม่ใน `Resources/claude-ai/` สำหรับ project ที่มีอยู่ใน `Projects/`

---

## When to use

- มี project ใหม่ใน `Projects/` ที่ต้องการ Claude.ai mobile context
- ต้องการ draft system prompt สำหรับ project นั้น

---

## Protocol

### Step 1 — Check existing state

ก่อนทำอะไร เช็คก่อนว่า:
- มี `Projects/[project-name]/` อยู่แล้วไหม?
- มี `Resources/claude-ai/[project-name]/` อยู่แล้วไหม?

ถ้ามีแล้ว → แจ้ง user และถามว่าต้องการ update หรือ scaffold ใหม่

### Step 2 — Read context

1. อ่าน `Me.md` — personal context ที่เกี่ยวข้อง
2. อ่าน `system/templates/claude-ai-project-template.md` — template structure
3. อ่าน `Resources/claude-ai/` workspaces ที่มีอยู่แล้ว — ดู pattern system prompts + หา overlap กับ project ใหม่

### Step 3 — Draft & confirm

Draft ให้ user approve ก่อนเสมอ — แสดง:

```
Project: [name]
PARA: Project ✅ (เหตุผล: ...)

State file: Projects/[name]/state-[name].md
Claude.ai workspace: Resources/claude-ai/[name]/

System prompt draft:
---
[draft ≤500 tokens]
---

โอเคไหม? จะ scaffold ให้เลย
```

**System prompt guidelines:**
- Role ชัดเจนและเฉพาะ project นี้
- Context เฉพาะ project (phase, goal) — ไม่ใส่สิ่งที่ Claude รู้แล้ว
- Output format ที่เหมาะกับ use case
- Always/Never เฉพาะที่จำเป็น

### Step 4 — Scaffold (หลัง user approve)

**4a. สร้าง state file:**
```
Projects/[project-name]/
└── state-[project-name].md   ← จาก project-state-template, กรอก context จริงจาก conversation
```

**4b. สร้าง claude-ai workspace:**
```
Resources/claude-ai/[project-name]/
├── project.md          ← จาก claude-ai-project-template, ใส่ system prompt ที่ approve แล้ว
└── knowledge/
    ├── README.md        ← file mapping table
    ├── system-prompt.md ← copy จาก project.md section 2
    ├── project-state.md ← copy จาก Projects/[name]/state-[name].md
    └── profile.md       ← copy จาก Me.md
```

**4c. อัปเดต secretary routing:**
เพิ่ม domain keywords และ state file path ของ project ใหม่ใน `## Domain Routing` ของ `.claude/agents/secretary.md`

---

## Naming convention

Folder name ต้องตรงกับ folder name ใน `Projects/` — ใช้ชื่อเดียวกันทุกตัวอักษร

## Scope

- ไม่แตะ source files (`Projects/`, `Me.md`)
- Draft system prompt ให้ user approve ก่อนเสมอ
- สร้างได้ทีละ 1 project ต่อครั้ง
