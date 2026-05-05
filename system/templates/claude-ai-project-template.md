# Claude Project — [Project Name]

_Last updated: YYYY-MM-DD_

---

## 1. PROJECT IDENTITY

| Field | Value |
|-------|-------|
| **Project Name** | [ชื่อ] |
| **Purpose** | [จุดประสงค์หลักในหนึ่งประโยค] |
| **Primary Use** | daily chat / deep research / automation / PKM |
| **Linked State Files** | [[Projects/[name]/state-[name]]] · [[Me]] |

---

## 2. SYSTEM PROMPT (≤500 tokens)

_Copy section นี้ → ใส่เป็น Instructions ใน Claude.ai project_

```
You are [role] for Gap — [one-line context].

Context:
- [background ที่ต้องรู้ทุก session — เฉพาะ project นี้]
- [current phase หรือ status]

Your role: [สิ่งที่ Claude ช่วย]

Output: [bullet / prose / table], [Thai / English], concise.

Always: [สิ่งที่ต้องทำเสมอ]
Never: [สิ่งที่ห้ามทำ]
```

---

## 3. PROJECT KNOWLEDGE FILES

Files จริงอยู่ที่ `knowledge/` — upload เข้า Claude.ai ได้เลย
Sync ทำเมื่อ state เปลี่ยน หรือถึง maintenance review

| ไฟล์ | Source | ใช้บ่อยแค่ไหน |
|------|--------|--------------|
| `system-prompt.md` | section 2 ด้านบน | ทุก session (ใส่เป็น instruction) |
| `project-state.md` | `Projects/[name]/state-[name].md` | ทุก session |
| `profile.md` | `Me.md` | เป็นครั้งคราว |

---

## 4. VAULT BRIDGE

**Workflow:** คุยไอเดียใน Claude.ai → copy session → run `/session-to-wiki` ใน Claude Code → vault รับและ link ต่อได้เลย

ใช้ `/session-to-wiki` เมื่อ session มี:
- ไอเดียใหม่ที่ควรเก็บไว้ใน wiki
- Decision หรือ design ที่ตกลงแล้ว
- Context ที่ควร link กับ state files อื่น

---

## 5. TOKEN EFFICIENCY CHECKLIST

- [ ] System prompt ≤500 tokens?
- [ ] ข้อมูลหนักอยู่ใน knowledge files ไม่ใช่ system prompt?
- [ ] ไม่มี instruction ที่ Claude รู้อยู่แล้ว (default behavior)?
- [ ] context เฉพาะ project นี้ ไม่ปนกับ project อื่น?
- [ ] ใช้ bullet point แทน paragraph?

---

## 6. MAINTENANCE

- รีวิว system prompt ทุก [phase transition / X เดือน]
- ลบ instruction ที่ไม่ได้ใช้จริง
- **Sync `knowledge/`** — copy vault sources ใหม่ → re-upload ใน Claude.ai
  - `project-state.md` ← `Projects/[name]/state-[name].md`
  - `profile.md` ← `Me.md`
  - `system-prompt.md` ← section 2 ด้านบน (ถ้าเปลี่ยน)

### Changelog

| Date | Change |
|------|--------|
| YYYY-MM-DD | Created |
