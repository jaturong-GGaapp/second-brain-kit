# Claude Project Setup — [Project Name]

_Last updated: YYYY-MM-DD_

---

## 1. PROJECT IDENTITY

| Field | Value |
|-------|-------|
| **Project Name** | [ชื่อ] |
| **Purpose** | [จุดประสงค์หลักในหนึ่งประโยค] |
| **Primary Use** | daily chat / deep research / automation / PKM |
| **Linked State Files** | [[]] |

---

## 2. SYSTEM PROMPT (≤500 tokens)

```
Role: Claude คือ [อะไร] ใน project นี้
Context: [background ที่ต้องรู้ทุก session]
Output Format: [bullet / prose / table / code]
Language: [Thai / English / Mixed]

Always:
- [สิ่งที่ต้องทำเสมอ]

Never:
- [สิ่งที่ห้ามทำ]
```

---

## 3. PROJECT KNOWLEDGE FILES

Files จริงอยู่ที่ `files/` — upload เข้า Claude.ai ได้เลย
Export/sync ทำตอน maintenance review แต่ละครั้ง

| ไฟล์ใน files/ | Vault Source | ใช้บ่อยแค่ไหน |
|--------------|-------------|--------------|
| `[name].md` | `[vault path]` | ทุก session / เป็นครั้งคราว |

---

## 4. SKILLS (Optional)

| Skill Name | Trigger Phrase | What It Does |
|------------|---------------|--------------|
| [ชื่อ] | [คำที่พูดแล้ว skill ทำงาน] | [อธิบายสั้นๆ] |

---

## 5. TOKEN EFFICIENCY CHECKLIST

- [ ] System prompt ≤500 tokens?
- [ ] ข้อมูลหนักอยู่ใน files ไม่ใช่ system prompt?
- [ ] ไม่มี instruction ที่ Claude รู้อยู่แล้ว (default behavior)?
- [ ] แต่ละ project แยก context ชัดเจน ไม่ปนกัน?
- [ ] ใช้ bullet point แทน paragraph ใน instructions?

---

## 6. MAINTENANCE

- รีวิว system prompt ทุก [X สัปดาห์/เดือน]
- ลบ instruction ที่ไม่ได้ใช้จริง
- ย้าย context ที่โตขึ้นจาก system prompt → files
- **Sync `files/`** — copy vault sources ใหม่ → re-upload ใน Claude.ai

### Changelog

| Date | Change |
|------|--------|
| YYYY-MM-DD | Created |
