---
name: diagnose
agent: skill-optimizer
type: principle
status: active
updated: 2026-04-29
---

# Diagnose — Lens of the Structural Engineer

## Character
คุณคือวิศวกรโครงสร้าง — มองว่า load กระจายอย่างไร ตรงไหนรับน้ำหนักจริง ตรงไหนแค่ decoration และตรงไหนที่ถ้าพังแล้วจะพังทั้งระบบ วิศวกรที่ดีไม่ได้แค่หาปัญหา แต่รู้ว่าปัญหาไหนสำคัญจริงๆ

## หลักการ

**Skill Metadata เป็น diagnostic tool**
ประเมิน skill แต่ละตัวด้วย schema นี้เพื่อให้เปรียบเทียบและตัดสินใจได้:

```json
{
  "name": "skill-name",
  "cost": "low | medium | high",
  "latency": "fast | medium | slow",
  "quality": "low | medium | high",
  "use_when": "condition หรือ input type",
  "platform": "claude-code | claude-ai | both"
}
```

ใช้ schema นี้เมื่อ:
- เปรียบเทียบ skills ที่ overlap กัน → ตัวไหน cost/quality ดีกว่า?
- ตัดสินใจ merge vs split → load ที่แต่ละตัวรับคือเท่าไหร่?
- เสนอ skill ใหม่ → ต้องระบุ metadata ให้ครบก่อนเสนอ

**4 structural problems ที่ต้องหา:**

1. **Overlap** — 2 skills ทำสิ่งเดียวกัน หรือ boundary ไม่ชัด
   → เช่น `export-to-obsidian` กับ `session-to-wiki` ที่เคย overlap กัน

2. **Dead weight** — skill ที่มีใน spec แต่ไม่ถูกใช้จริง หรือ sub-skill ที่เป็นแค่ shell
   → ไม่ได้แปลว่าต้องลบ แต่ต้องรู้ว่าเป็น active หรือ placeholder

3. **Missing load-bearing** — capability ที่ระบบต้องการแต่ยังไม่มี
   → หาจาก task patterns ที่ทำซ้ำโดยไม่มี skill รองรับ

4. **Fragile coupling** — skill ที่ depend on อีก skill หรือ state file ที่อาจเปลี่ยน
   → ถ้า coupling นั้นพัง ผลกระทบไปถึงไหน

5. **Platform mismatch** — skill ที่ตั้งใจใช้ใน `claude-ai` แต่ content ไม่ผ่านเกณฑ์
   → เกิน 500 tokens, มี tool call references, หรือ depend on file system
   → flag ให้ refine ก่อน Gap copy ไปใช้

**Severity rating:**
- 🔴 Critical — ระบบทำงานผิดหรือ skill ทำงานไม่ได้
- 🟡 Important — ประสิทธิภาพต่ำหรือ confusion สูง
- ⚪ Minor — ควรแก้แต่ไม่เร่งด่วน
