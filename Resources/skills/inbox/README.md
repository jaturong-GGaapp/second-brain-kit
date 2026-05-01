---
title: "Skill Inbox"
type: reference
---

# Skill Inbox

วาง skill ideas ที่นี่ — [[Resources/agents/skill-optimizer|Skill Optimizer]] จะ process และ embed เข้า skill library

## วิธีใช้

1. สร้างไฟล์หรือ folder ใน inbox นี้ ชื่อใดก็ได้
2. เขียน idea คร่าวๆ หรือวาง prompt/concept ที่มี
3. บอก Skill Optimizer ว่า "มี skill idea ใน inbox"
4. Optimizer จะ analyze → confirm placement กับ Gap ก่อนสร้างไฟล์จริง
5. ลบไฟล์ออกจาก inbox หลัง process แล้ว

## Placement Options (Optimizer จะตัดสินใจ)

| ที่วาง | เมื่อไหร่ |
|--------|---------|
| `~/.claude/skills/<name>/` | skill ทั่วไป ไม่ผูกกับ domain ใด หรือไม่ match agent ไหน |
| `Resources/skills/shared/` | 2+ agents ใช้ได้จริง |
| `Resources/skills/agents/<agent>/` | ใช้ได้เฉพาะ context ของ agent เดียว |

## Skill Idea Template (ไม่บังคับ)

```
# ชื่อ skill idea

## ทำอะไร
...

## Input
...

## Output ที่อยากได้
...

## Platform
claude-code | claude-ai | both

## Placement hint (ถ้ามี idea)
standalone | shared | agent: <ชื่อ>
```

## Complex Skills (หลาย component)

ถ้า skill มี sub-skills หรือ scripts ให้สร้างเป็น folder แทนไฟล์เดียว:

```
inbox/
└── my-skill/
    ├── SKILL.md          ← main skill
    ├── sub-skill.md      ← sub-skill หรือ reference guide
    └── scripts/          ← supporting scripts (ถ้ามี)
```
