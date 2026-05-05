# Areas

Ongoing life responsibilities with no end date — things you maintain rather than complete.

---

## What belongs here

An **Area** has:
- No specific end state — it's maintained, not finished
- A standard you want to uphold over time
- A horizon of 1–2+ years (or indefinite)

If it has a clear end state and you're actively working on it → it's a **Project** (`Projects/`).
If it spans 4+ years (e.g. learning a new discipline) → keep it as an Area, pull the next milestone as a Todo.

---

## Structure

Each area gets its own folder:

```
Areas/
└── My Area/
    └── state-my-area.md    ← current status, focus, next actions
```

---

## State file fields

| Field | Purpose |
|---|---|
| `## Status` | One-liner: current phase + overall health |
| `## Current Focus` | What's being actively maintained right now |
| `## Next Actions` | P0 (this week) → P3 (parking lot) |
| `## Blockers` | What's stuck — or "-" if none |
| `## Metrics` | Key numbers for quantifiable areas (finance, health) — optional |

**Priority tags:** `P0` this week · `P1` this month · `P2` when capacity allows · `P3` parking lot

---

## How agents use Areas

- **Secretary** reads the relevant state file before answering any question in that domain
- **Weekly Review** (`/weekly-review`) updates all state files based on the week's journal entries
- **`Journal/current-state.md`** holds a P0-only snapshot across all areas — updated weekly

---

## Adding a new area

Tell the Secretary agent: *"อยากเพิ่ม area ใหม่เรื่อง X"*

The agent will classify it (Area vs Project vs Todo) and scaffold the state file after you confirm.

---

## Example

See `_example-area/` for the folder structure. State file template is at `system/templates/area-state-template.md`.
