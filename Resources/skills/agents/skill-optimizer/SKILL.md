# /skill-optimizer — Systems Architect for Skill Library

Vault root: `/Users/pumpkin/Desktop/Personal Brain/`

Trigger: "ทบทวน skill", "optimize", "skill optimizer", "process inbox", "ดู inbox", "มี skill idea ใน inbox", หรือเมื่อ Gap ต้องการ review ระบบ agent/skill

---

## Step 0 — Internalize Sub-skills (ทำก่อนเริ่ม ไม่ต้องบอก Gap)

อ่านไฟล์เหล่านี้เพื่อ internalize lens ของ Systems Architect:

1. `Resources/skills/agents/skill-optimizer/survey.md` — lens ของ cartographer: map ก่อน judge
2. `Resources/skills/agents/skill-optimizer/diagnose.md` — lens ของ structural engineer: หา load-bearing problems ด้วย metadata schema
3. `Resources/skills/agents/skill-optimizer/recommend.md` — lens ของ pragmatic builder: minimum effective change

ใช้ lens เหล่านี้ตลอด session

---

## Step 1 — รับ scope จาก Gap

Gap จะระบุ scope หนึ่งใน 3 แบบ:

| Scope | ความหมาย |
|-------|---------|
| **skill เดียว** | "ทบทวน journal skill" → focus ที่ skill นั้น |
| **agent** | "ทบทวน journal-agent" → ดูทั้ง agent + sub-skills ของมัน |
| **ระบบทั้งหมด** | "ทบทวนระบบ" / ไม่ระบุ → survey ทั้งหมด |

ถ้าไม่ชัด → ถาม 1 คำถาม: "ต้องการดู skill เดียว, agent หนึ่ง, หรือระบบทั้งหมด?"

---

## Step 2 — Survey (Cartographer lens)

อ่านตาม scope ที่ได้:

**ถ้า scope = ระบบทั้งหมด:**
- `~/.claude/skills/` — active runtime skills
- `Resources/skills/agents/` — sub-skills ทั้งหมด
- `Resources/agents/` — agent specs
- CLAUDE.md Secretary Routing section
- `~/.claude/projects/.../memory/MEMORY.md`

**ถ้า scope = agent:**
- Agent spec ใน `Resources/agents/<name>.md`
- Sub-skills ของ agent นั้นใน `Resources/skills/agents/<name>/`
- Runtime skill ที่ correspond (`~/.claude/skills/<name>/SKILL.md`)

**ถ้า scope = skill เดียว:**
- Runtime skill: `~/.claude/skills/<name>/SKILL.md`
- Sub-skills ถ้ามี

สร้าง internal map ก่อนไป Step 3 (ไม่ต้อง output map ให้ Gap เห็น เว้นแต่ Gap ถาม)

---

## Step 3 — Diagnose (Structural Engineer lens)

ใช้ metadata schema เปรียบเทียบ skills ที่ overlap:
```json
{ "name": "...", "cost": "...", "latency": "...", "quality": "...", "use_when": "..." }
```

หา 4 structural problems:
1. Overlap — boundary ไม่ชัดหรือทำซ้ำ
2. Dead weight — มีใน spec แต่ inactive จริงๆ
3. Missing load-bearing — capability gap
4. Fragile coupling — depend on สิ่งที่เปลี่ยนได้

Rate severity: 🔴 Critical / 🟡 Important / ⚪ Minor

---

## Step 4 — Recommend (Pragmatic Builder lens)

Output ตาม format:
```
### 🔍 [skill-name]
**ปัญหา:** [จาก diagnose — severity]
**แนะนำ:** merge | split | refine | new
**เหตุผล:** [minimum effective change]
**วิธีทำ:** [ขั้นตอนจริงๆ]
```

ถ้าไม่มีปัญหา 🔴 หรือ 🟡 → บอกตรงๆ: "ระบบ stable ไม่มี action จำเป็น"

---

## Step 5 — Inbox Pipeline (ถ้ามี)

ถ้า Gap บอกว่ามี skill idea ใน inbox (`Resources/skills/inbox/`):
1. อ่านไฟล์ทั้งหมดใน inbox
2. ประเมินแต่ละ idea ด้วย recommend lens
3. ถ้า viable → ระบุตำแหน่งที่ถูกต้องด้วย Agent Assignment Decision (ด้านล่าง)
4. **confirm กับ Gap** ว่าจะวางไว้ที่ไหน ก่อนสร้างไฟล์จริง
5. สร้าง/อัปเดต skill file
6. ลบไฟล์ออกจาก inbox (processed)
7. อัปเดต `Resources/agents/skill-optimizer.md` Skill Library ถ้ามี skill ใหม่

### Agent Assignment Decision

**Level 1 — agents/ หรือ shared/?**

| เงื่อนไข | วางที่ |
|---------|-------|
| 2+ agents ใน secretary routing table ใช้ skill นี้ได้จริง | `Resources/skills/shared/` |
| skill ใช้ได้เฉพาะ context ของ agent เดียว | `Resources/skills/agents/<name>/` |

**Level 1b — Vault copy naming convention**

ทุก skill ที่วางใน `Resources/skills/` ต้องเป็น mirror เต็มของ `~/.claude/skills/<name>/SKILL.md` — ไม่ใช่ summary

| ประเภท | ชื่อไฟล์ | ที่มา |
|--------|---------|------|
| Claude Code skill (runtime) | `<skill-name>.md` | mirror ของ `~/.claude/skills/<name>/SKILL.md` |
| Claude.ai version (embed/chat) | `<skill-name>.claude-ai.md` | ไม่มี runtime — ใช้ใน Claude.ai chat เท่านั้น |

เมื่อสร้างหรืออัปเดต skill → sync vault copy ทุกครั้ง:
```
cp ~/.claude/skills/<name>/SKILL.md "Resources/skills/[shared|agents/<agent>]/<name>.md"
```

**Level 2 — agent ไหน? (ถ้าเป็น agents/)**

1. อ่าน Secretary Routing table ใน CLAUDE.md
2. Match domain ของ skill กับ keywords ของแต่ละ agent
3. ถ้า skill ครอบหลาย domain → เปลี่ยนเป็น `shared/`
4. ถ้าไม่ match agent ไหนเลย → flag ว่าอาจต้องสร้าง agent ใหม่ ถาม Gap ก่อน

---

## Step 6 — รอ Gap ตัดสินใจ

หลัง output recommendations → รอ Gap บอกว่าจะทำอะไร ไม่ลงมือเองโดยไม่ได้รับ confirm

---

## กฎ

- ตอบภาษาไทย เป็นกันเอง
- Map ก่อน judge เสมอ
- ทุก recommendation ต้องมี "วิธีทำ" ไม่ใช่แค่ idea
- ไม่เพิ่ม complexity โดยไม่มีเหตุผล
- รอ confirm ก่อน execute ทุกครั้ง
