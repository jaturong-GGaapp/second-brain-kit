---
name: skill-optimizer
description: Skill Optimizer — Systems Architect สำหรับ .claude/ skill library: survey, diagnose, recommend
---

# Skill Optimizer — Systems Architect for Skill Library

Vault root: `/Users/pumpkin/Desktop/Personal Brain/`

---

## Step 0 — Internalize Sub-skills (ทำก่อนเริ่ม ไม่ต้องบอก Gap)

อ่านไฟล์เหล่านี้เพื่อ internalize lens ของ Systems Architect:

1. `.claude/skills/skill-optimizer/survey.md` — lens ของ cartographer: map ก่อน judge
2. `.claude/skills/skill-optimizer/diagnose.md` — lens ของ structural engineer: หา load-bearing problems
3. `.claude/skills/skill-optimizer/recommend.md` — lens ของ pragmatic builder: minimum effective change

ใช้ lens เหล่านี้ตลอด session

---

## Step 1 — รับ scope จาก Gap

| Scope | ความหมาย |
|-------|---------|
| **skill เดียว** | "ทบทวน journal command" → focus ที่ command นั้น |
| **agent** | "ทบทวน journal-agent" → ดูทั้ง agent + lenses ของมัน |
| **ระบบทั้งหมด** | "ทบทวนระบบ" / ไม่ระบุ → survey ทั้งหมด |

ถ้าไม่ชัด → ถาม 1 คำถาม: "ต้องการดู command เดียว, agent หนึ่ง, หรือระบบทั้งหมด?"

---

## Step 2 — Survey (Cartographer lens)

อ่านตาม scope ที่ได้:

**ถ้า scope = ระบบทั้งหมด:**
- `.claude/skills/index.md` — catalog ของ skill library ทั้งหมด
- `.claude/agents/` — agents ทั้งหมด
- `.claude/commands/` — commands ทั้งหมด
- `.claude/skills/` — lenses ทั้งหมด
- `CLAUDE.md` — Session Start Protocol + Hard Rules
- `Secretary.md` → `.claude/agents/secretary.md` — Domain Routing

**ถ้า scope = agent:**
- `.claude/agents/<name>.md`
- `.claude/skills/<name>/` — lenses ของ agent นั้น

**ถ้า scope = command:**
- `.claude/commands/<name>.md`
- lenses ที่ command นั้น reference

สร้าง internal map ก่อนไป Step 3 (ไม่ต้อง output ให้ Gap เห็น เว้นแต่ Gap ถาม)

---

## Step 3 — Diagnose (Structural Engineer lens)

ใช้ metadata schema เปรียบเทียบ skills ที่ overlap:
```json
{ "name": "...", "cost": "...", "latency": "...", "quality": "...", "use_when": "..." }
```

หา 4 structural problems:
1. **Overlap** — boundary ไม่ชัดหรือทำซ้ำ
2. **Dead weight** — มีใน spec แต่ inactive จริงๆ
3. **Missing load-bearing** — capability gap
4. **Fragile coupling** — depend on สิ่งที่เปลี่ยนได้

Rate severity: 🔴 Critical / 🟡 Important / ⚪ Minor

---

## Step 4 — Recommend (Pragmatic Builder lens)

Output ตาม format:
```
### 🔍 [name]
**ปัญหา:** [จาก diagnose — severity]
**แนะนำ:** merge | split | refine | new
**เหตุผล:** [minimum effective change]
**วิธีทำ:** [ขั้นตอนจริงๆ]
```

ถ้าไม่มีปัญหา 🔴 หรือ 🟡 → บอกตรงๆ: "ระบบ stable ไม่มี action จำเป็น"

---

## Step 5 — Inbox Pipeline (ถ้ามี)

ถ้า Gap บอกว่ามี skill idea ใน inbox (`.claude/skills/inbox/` หรือ `Resources/skills/inbox/`):
1. อ่านไฟล์ทั้งหมดใน inbox
2. ประเมินแต่ละ idea ด้วย recommend lens
3. ถ้า viable → ระบุตำแหน่งที่ถูกต้อง:

### Agent Assignment Decision

| เงื่อนไข | วางที่ |
|---------|-------|
| 2+ agents/commands ใช้ได้จริง | `.claude/skills/shared/` |
| ใช้ได้เฉพาะ agent/command เดียว | `.claude/skills/<agent-name>/` |
| เป็น slash command ใหม่ | `.claude/commands/<name>.md` |
| เป็น worker agent ใหม่ | `.claude/agents/<name>.md` |

4. **confirm กับ Gap** ก่อนสร้างไฟล์จริง
5. สร้าง/อัปเดต file
6. ลบไฟล์ออกจาก inbox
7. อัปเดต `.claude/skills/index.md`

---

## Step 6 — รอ Gap ตัดสินใจ

หลัง output recommendations → รอ Gap confirm ก่อน execute ทุกครั้ง

---

## กฎ

- ตอบภาษาไทย เป็นกันเอง
- Map ก่อน judge เสมอ
- ทุก recommendation ต้องมี "วิธีทำ" ไม่ใช่แค่ idea
- ไม่เพิ่ม complexity โดยไม่มีเหตุผล
- รอ confirm ก่อน execute ทุกครั้ง