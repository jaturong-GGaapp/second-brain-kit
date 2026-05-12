# /update-wiki

Sync LLM wiki files หลังจาก implementation มี decision หรือ architecture change ใหม่

## When to Use

- หลัง reviewer approve feature ที่มี architecture impact
- หลัง `/new-decision` สร้าง ADR ใหม่
- เมื่อผู้ใช้ต้องการ update wiki โดยตรง

## Steps

### Step 1 — Load Current Wiki

อ่านทุก wiki file:
- `wiki/architecture.md`
- `wiki/coding_rules.md`
- `wiki/api_contracts.md`
- `wiki/design_system.md`

### Step 2 — Identify What Changed

ถามผู้ใช้ (หรือ infer จาก context ของ session):
- มี package boundary ใหม่ไหม?
- มี API endpoint ใหม่หรือเปลี่ยนไหม?
- มี coding rule ที่ควรเพิ่มจาก code review?
- มี design token ใหม่ไหม?

### Step 3 — Draft Updates

- Show diff ที่จะ update ให้ผู้ใช้เห็นก่อน
- **หยุดรอผู้ใช้ approve** ก่อน write

### Step 4 — Write Updates

- Update เฉพาะ wiki files ที่มี change
- อัปเดต `Updated: YYYY-MM-DD` ที่ด้านบนของ file

### Step 5 — Confirm

รายงาน:
- Files updated
- Summary ของ changes
