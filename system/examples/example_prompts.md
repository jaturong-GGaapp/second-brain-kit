# Example Prompts in Action

Real input/output examples for each prompt in the system.

---

## 1. Journal Interview

**User input:**
```
[paste prompt_journal_interview.md]

current_state: focused on debt payoff, 4 interviews done for app, energy low this week
```

**Conversation:**
```
Agent: วันนี้เกิดอะไรขึ้น? (แค่ข้อเท็จจริง ไม่ต้องตีความ)

User: ประชุมงาน 3 ชั่วโมง แล้วก็ทำ interview กับ user คนที่ 5

Agent: ทำอะไรได้ดีวันนี้?

User: interview นี้ได้ insight ดีมาก เขาบอกว่า pain point จริงๆ ไม่ใช่ที่เราคิด

Agent: มีอะไรพังหรือ friction ไหม?

User: เสียเวลาไปกับ meeting ที่ไม่จำเป็น ทำให้ไม่มีแรงทำงานช่วงบ่าย

Agent: เรื่องนี้บอกอะไรกับชีวิตเรา?

User: ต้องรักษา energy ให้งานที่ matter จริงๆ ก่อน
```

**Output:**
```markdown
---
date: 2026-04-01
type: daily
---

# 2026-04-01

## Fact
ประชุมงาน 3 ชั่วโมง แล้วทำ user interview คนที่ 5

## Win
ได้ insight สำคัญ — pain point จริงๆ ต่างจากที่สมมติไว้

## Improve
Meeting ที่ไม่จำเป็นดึง energy จนทำงานช่วงบ่ายไม่ได้

## Meaning
ต้องรักษา energy ให้งานที่ matter ก่อน ไม่ใช่ตอบทุก request
```

---

## 2. Weekly Review

**User input:**
```
[paste prompt_weekly_review.md]

daily_notes: [paste 7 daily notes]
current_state: [paste current-state.md]
```

**Output (excerpt):**
```markdown
# Weekly Review — 2026-W13

## Wins
- Completed 3 user interviews (total: 7/10)
- Paid extra $100 on Card A
- Slept before midnight 5/7 days

## Patterns (Improve)
- Energy crashes after long meeting blocks — happens 3x this week
- Skipping lunch = bad afternoon focus (appeared in 4 notes)

## State Updates
| Domain | Before | After |
|--------|--------|-------|
| App | 4 interviews done | 7 interviews done |
| Finance | Card A: $3,200 | Card A: $3,100 |

## Focus next week
1. Protect 2-hour deep work block before any meetings
2. Complete final 3 interviews
```

---

## 3. Knowledge Ingest

**User input:**
```
[paste prompt_knowledge_ingest.md]

wiki_index: [paste wiki/index.md]

source: Article — "Why Community Apps Fail"
Key points:
- Most fail because they optimize for growth before retention
- The "cold start problem" kills 80% of community apps in year 1
- Successful ones start with 50–100 highly engaged core members, not mass acquisition
```

**Output (excerpt):**
```markdown
# Why Community Apps Fail

| Field | Value |
|-------|-------|
| **Format** | article |
| **Date** | 2026-04-01 |

## Summary
Community apps fail when they chase growth before establishing retention. The cold start problem — having too few users for the network to be valuable — kills most apps in year 1. The antidote is starting with a small, highly engaged core group rather than mass acquisition.

## Key Takeaways
- Optimize retention before growth
- Target 50–100 core members first
- Cold start problem is the #1 killer

## Connections
- Supports: [[concepts/Product-Market-Fit]]
- See also: [[sources/community-flywheel]]
```

**New concept page created:** `wiki/concepts/Cold-Start-Problem.md`

---

## 4. Secretary Routing

**User input:**
```
[paste prompt_secretary_routing.md]

user_profile: [paste Me.md]
current_state: [paste current-state.md]
domain_state: [paste Areas/finance/state.md]

user_request: ควรโยกเงินไปจ่าย Card A เพิ่มไหม หรือเก็บ emergency fund ก่อน?
```

**Output:**
```
ดูตัวเลขของคุณ: Card A ดอกเบี้ย ~20%, emergency fund ตอนนี้ $1,200 จาก $3,000

ถ้า emergency fund ยังต่ำกว่า 1 เดือนค่าใช้จ่าย → เติม emergency ก่อน
ถ้าเกิน 1 เดือนแล้ว → โยกจ่าย Card A คุ้มกว่าเก็บเงินที่ดอกเบี้ยต่ำกว่า 20%

ค่าใช้จ่ายต่อเดือนของคุณประมาณเท่าไหร่?
```

---

## 5. Session to Wiki

**User input:**
```
[paste prompt_session_to_wiki.md]

session_topic: วิธีออกแบบ onboarding flow สำหรับ community app
session_summary:
- First action ต้องให้ value ทันที ไม่ใช่ให้กรอก profile
- Social proof ในหน้าแรกสำคัญมาก
- ถามแค่ 1 คำถาม: "คุณอยากเจอคนแบบไหน?"
your_name: Alex
```

**Output:**
```
Type detected: KNOWLEDGE

---
title: "Onboarding Flow Design for Community Apps"
type: source
tags: [product, onboarding, community]
created: 2026-04-01
sources: [self]
---

# Onboarding Flow Design for Community Apps

| Field | Value |
|-------|-------|
| Author | [[entities/Alex]] |
| Format | note (session capture) |

## Summary
Effective community app onboarding delivers value immediately rather than asking users to complete a profile first. Social proof on the first screen reduces drop-off. Reducing the ask to a single question — "who do you want to meet?" — increases completion rates.

## Key Takeaways
- First action = immediate value, not profile setup
- Social proof on screen 1 is critical
- One question max: "who do you want to meet?"

## Connections
- Supports: [[concepts/Cold-Start-Problem]]
- See also: [[sources/why-community-apps-fail]]
```
