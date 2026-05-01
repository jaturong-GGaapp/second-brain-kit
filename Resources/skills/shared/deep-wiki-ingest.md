---
name: deep-wiki-ingest
description: use when Gap อยากเก็บ session แบบละเอียดครบชุด — สร้าง concepts, entities, analysis pages ทั้งหมด ไม่ใช่แค่ source file
cost: high
latency: slow
quality: high
use_when: session มี keywords/concepts/entities สำคัญจำนวนมากที่ต้องการ wiki pages แยก, "เก็บละเอียด", "deep ingest", "ingest แบบเต็ม", "เก็บทั้งหมดลง wiki"
placement: shared
platform: claude-code
agents: [wiki-agent]
updated: 2026-05-01
---

# Deep Wiki Ingest

Full INGEST workflow สำหรับ conversation session — สร้าง wiki pages ครบชุดจาก session เดียว

## ต่างจาก session-to-wiki

| | session-to-wiki | deep-wiki-ingest |
|--|--|--|
| Output | Source file เท่านั้น | Source + Concepts + Entities + Analysis |
| Speed | Fast | Slow (deliberate) |
| ใช้เมื่อ | ทุก session ทั่วไป | Session ที่มี ideas สำคัญเยอะ |

## Workflow (สั้น)

1. **Scan** — list concepts, entities, deliverables ทั้งหมดใน session
2. **Report** — แสดง inventory ให้ Gap confirm ก่อน
3. **Create** — source + concept pages + entity pages + analysis (ถ้ามี)
4. **Update** — state files ที่เกี่ยวข้อง, index.md, log.md, overview.md

## Trigger

```
/deep-wiki-ingest
"deep ingest"
"เก็บละเอียด"
"ingest แบบเต็ม"
"เก็บทั้งหมดลง wiki"
```
