---
name: weekly-review
department: Review
status: active
---

# Weekly Review Agent

**Role:** RAG 7 daily notes + all state files → อัป current-state.md + เขียน weekly summary

## Skills
- [[Resources/skills/agents/weekly-review/focus-setter|focus-setter]]
- [[Resources/skills/shared/obsidian-markdown/SKILL|obsidian-markdown]] (shared)
- [[Resources/skills/shared/grill-with-docs/SKILL|grill-with-docs]] (shared)

## Trigger
- Gap พูดว่า "weekly review" / "สรุปสัปดาห์" / "review week"
- ทุกวันอาทิตย์ (แนะนำโดย `/journal` อัตโนมัติ)

## Outputs
- `Journal/current-state.md` — อัปเดต live state
- `Journal/Weekly-Review/YYYY-WXX.md` — weekly summary

## Embedded Skills

### dept-aggregator
อ่าน state files แต่ละ domain แล้ว diff กับ daily notes:
- ตัวเลขหรือ phase เปลี่ยนไปไหม?
- มี blocker ใหม่ที่ยังไม่อยู่ใน state file?
- มี decision ที่ทำแล้วแต่ยังไม่ได้บันทึก?

### win-loss-analyzer
จาก daily notes 7 วัน:
- Win ที่ซ้ำหรือ build กัน → เป็น strength ที่กำลัง develop
- Improve ที่ซ้ำ → เป็น pattern ที่ต้องแก้
- วัน Meaning ว่าง / สั้นมาก → วันที่ disconnected

## Output Format

```
Weekly review เสร็จแล้ว

📁 อัปเดต: Journal/current-state.md
📁 สร้าง: Journal/Weekly-Review/YYYY-WXX.md

สัปดาห์นี้:
• Wins: [1-2 bullet]
• Blockers: [1-2 bullet]
• Pattern: [1 ประโยค]

Focus week หน้า: [top 3]
```

**Installed skill:** `/weekly-review` — ดู `~/.claude/skills/weekly-review/SKILL.md`
