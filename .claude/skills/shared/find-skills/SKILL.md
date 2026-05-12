---
name: find-skills
description: Discover and install agent skills from the skills.sh open ecosystem. Use only for generic capability gaps, and only when user confirms or explicitly requests. Use when user says "หา skill สำหรับ X" or confirms after optimizer identifies a generic gap.
compatibility: Requires internet access and npx
---

# find-skills

ค้นหา skill จาก [[concepts/Agent-Skills-Ecosystem]] (skills.sh) — ดู [[wiki/sources/2026-04-28-find-skills-vercel-labs]] สำหรับรายละเอียดเต็ม

## Commands

```bash
npx skills find [query]          # ค้นหา
npx skills add <owner/repo> -g -y  # ติดตั้ง
```

## Quality Check ก่อนแนะนำ

1. Install count ≥ 1K
2. Source น่าเชื่อถือ (vercel-labs, anthropics, microsoft)
3. GitHub stars ≥ 100

## ถ้าไม่เจอ

บอก user ตรงๆ แล้วเสนอสร้างเองผ่าน inbox pipeline
