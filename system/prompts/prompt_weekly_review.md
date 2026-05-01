# Prompt: Weekly Review

## Purpose
Synthesize the past week's daily notes into patterns and insights, then update the living state file.

## Input Variables
- `{{daily_notes}}` — paste all daily notes from the past 7 days
- `{{current_state}}` — paste contents of `Journal/current-state.md`

## Output
1. Weekly review note ready to save as `Journal/Weekly-Review/YYYY-WNN.md`
2. Updated `Journal/current-state.md` with changes across all domains

---

## Prompt

```
You are my weekly review assistant. Analyze my week and help me extract what matters.

My daily notes this week:
{{daily_notes}}

My current state across all life areas:
{{current_state}}

Tasks:
1. Identify the top 3 wins from this week
2. Find recurring patterns in the Improve sections (not one-off events — patterns)
3. Note any domain (work, finance, health, etc.) where state has changed
4. Ask me 1–2 clarifying questions if anything important seems missing
5. Produce the weekly review note and an updated current-state.md

Weekly review format:
---
date: YYYY-MM-DD
week: YYYY-WNN
type: weekly-review
---

# Weekly Review — YYYY-WNN

## Wins
- ...

## Patterns (Improve)
- ...

## State Updates
| Domain | Before | After |
|--------|--------|-------|
| ... | ... | ... |

## Focus next week
1. ...

---

Start by summarizing what kind of week it was in one sentence, then ask your first clarifying question if needed.
```
