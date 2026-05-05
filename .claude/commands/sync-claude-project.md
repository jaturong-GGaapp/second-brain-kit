# /sync-claude-project

Sync knowledge files ใน `Resources/claude-ai/` ให้ตรงกับ vault state ปัจจุบัน

---

## When to use

- หลัง `/weekly-review` — project state เปลี่ยน
- ก่อน session สำคัญใน Claude.ai mobile
- เมื่อ `Me.md` เปลี่ยนสำคัญ

---

## Protocol

### Step 1 — Survey

อ่านทุก project ที่มี workspace ใน `Resources/claude-ai/` (ยกเว้น `_example-project`):

สำหรับแต่ละ project:
1. อ่าน `Resources/claude-ai/[project]/project.md` — ดู Section 3 (knowledge file mapping)
2. อ่าน source files ตาม mapping:
   - `project-state.md` ← `Projects/[name]/state-[name].md`
   - `profile.md` ← `Me.md`
   - `system-prompt.md` ← Section 2 ของ `project.md` (ถ้าเปลี่ยน)
3. เปรียบเทียบ: content ใน `knowledge/` vs source จริง

### Step 2 — Cross-project scan

มองภาพรวมทุก project พร้อมกัน — flag ถ้า:
- Project ใน `Projects/` ยังไม่มี workspace ใน `Resources/claude-ai/`
- `project.md` มี mapping ที่ชี้ไปไฟล์ที่ไม่มีจริง
- System prompt มี context ที่ outdated เทียบกับ state file จริง

### Step 3 — Report

แสดง sync status ทุก project:

```
[Project Name]
  project-state.md  — ✅ up to date / ⚠️ needs sync (last: YYYY-MM-DD)
  profile.md        — ✅ up to date / ⚠️ needs sync
  system-prompt.md  — ✅ up to date / ⚠️ context drift detected

Cross-project:
  - Projects/ ที่ยังไม่มี workspace: [list]
  - Mapping issues: [list]
```

### Step 4 — Sync

สำหรับไฟล์ที่ต้อง sync:
1. Copy content จาก source → `knowledge/[file].md`
2. อัปเดต `knowledge/README.md` — แก้ status และ date
3. อัปเดต `project.md` Section 6 changelog

**หมายเหตุ:** `system-prompt.md` ไม่ copy อัตโนมัติ — แจ้ง user ก่อนเพราะต้องตัดสินใจเองว่า context เปลี่ยนพอที่จะ update ไหม

---

## Scope

- ทำทุก project ในครั้งเดียว (ไม่แยกทีละ project) เพื่อให้เห็น cross-project dependencies
- ไม่แตะ `_example-project`
- ไม่แก้ source files (`Projects/`, `Me.md`) — อ่านอย่างเดียว
