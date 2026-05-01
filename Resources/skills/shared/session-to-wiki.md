---
name: session-to-wiki
description: use when user อยากเก็บ session หรือ conversation → vault, "เก็บ session นี้", "save to wiki", "ingest conversation"
cost: low
latency: fast
quality: medium
use_when: user อยากเก็บ session หรือ conversation → vault, "เก็บ session นี้", "save to wiki", "ingest conversation"
placement: shared
platform: claude-ai
agents: [journal-agent, learning-research]
updated: 2026-04-28
---

# Session to Wiki

แปลง Claude.ai session เป็น wiki source summary พร้อม ingest

## Auto-detect: ใช้ agent ไหน

```
session เกี่ยวกับ personal insight / ตัดสินใจ / self-reflection
  → journal-agent (เก็บใน Meaning/Win หรือ daily note)

session เกี่ยวกับ knowledge / framework / analysis / research
  → learning-research → wiki ingest
```

## Workflow

1. User paste summary หรือ key points จาก session
2. บอก context: "session นี้เกี่ยวกับ [อะไร]"
3. Detect ประเภท → format ตาม template ที่เหมาะ
4. Output markdown block ให้ copy → ส่งต่อให้ Claude Code เพื่อ ingest ลง `raw/`

## Output Format (wiki path)

```markdown
---
title: "[Session Topic]"
type: source
tags: []
created: YYYY-MM-DD
---

## Summary
...

## Key Takeaways
- ...

## Connections
- Author: [[entities/Gap]]
- Supports: [[concepts/X]]
- See also: [[sources/Y]]
```

## Output Format (journal path)

เพิ่มใน daily note section ที่เหมาะ:
- **Insight สำคัญ** → Meaning
- **ตัดสินใจ** → Win หรือ Improve
- **Next action** → ท้าย note
