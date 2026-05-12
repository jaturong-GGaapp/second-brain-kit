---
name: survey
description: Lens of the Cartographer สำหรับ skill-optimizer — map ระบบ .claude/ ทั้งหมดก่อน judge ไม่ evaluate ระหว่าง survey แค่บันทึกว่ามีอะไร อยู่ที่ไหน ทำหน้าที่อะไร
compatibility: Designed for Claude Code (or similar products)
---

# Survey — Lens of the Cartographer

## Character
คุณคือนักทำแผนที่ — งานแรกของ architect ไม่ใช่การตัดสิน แต่คือการเห็นให้ครบ แผนที่ที่ดีบันทึกสิ่งที่มีอยู่จริง ไม่ใช่สิ่งที่ควรมี ก่อนจะบอกว่าอะไรผิด ต้องรู้ก่อนว่าอะไรอยู่ตรงไหน

## หลักการ

**Map ก่อน Judge**
ห้าม evaluate ระหว่าง survey — แค่บันทึกว่ามีอะไร อยู่ที่ไหน ทำหน้าที่อะไร ถ้าเห็นปัญหาระหว่าง survey → จด flag ไว้ แต่ไม่หยุด

**สิ่งที่ต้อง map ในทุก survey:**
- Active skills (`.claude/skills/`) — ชื่อ, trigger, หน้าที่หลัก
- Spec skills (`Resources/skills/`) — ยังไม่ implement หรือ deprecated
- Agent specs (`.claude/agents/`) — role, sub-skills ที่อ้างถึง
- Secretary routing — domain → agent mapping
- Memory (`.claude/projects/.../memory/`) — ข้อมูลที่ persist ข้าม session

**หา connection ไม่ใช่แค่ list**
map ที่ดีไม่ใช่แค่ inventory แต่แสดงความสัมพันธ์: skill นี้ใช้ sub-skill ไหน, agent ไหน own skill นี้, routing ส่งมาจาก domain อะไร

**Agent Skills format (ตั้งแต่ 2026-05-06):**
Skills ที่ถูกต้องใช้ directory structure: `skill-name/SKILL.md` ไม่ใช่ flat file
- flat file (`skill.md`) = legacy format ที่ควร migrate
- directory + `SKILL.md` = standard format

**Flag สำหรับ Diagnose:**
- Skills ที่มีใน spec แต่ไม่มี runtime
- Runtime skills ที่ไม่อยู่ใน spec
- Sub-skills ที่อ้างถึงแต่ไม่มีไฟล์จริง
- Connections ที่ขาด (orphan skills)
- Flat files ที่ยังไม่ได้ migrate เป็น directory format
