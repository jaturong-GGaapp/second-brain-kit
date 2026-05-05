# Projects

Active project workspaces — things you are working on right now with a clear end state.

---

## What belongs here

A **Project** has:
- A specific outcome (done-when condition)
- Active work happening this month
- An expected completion within ~6–12 months

If it has no end date → it's an **Area** (`Areas/`).
If it's a single action → it's a **Todo** inside a state file.
If it's blocked indefinitely → keep it as a note in an Area until it becomes active.

> Keep this folder lean. A long list of Projects usually means most of them should be Areas or Todos.

---

## Structure

Each project gets its own folder:

```
Projects/
└── My Project/
    └── state-my-project.md    ← single source of truth for this project
```

The state file tracks: status, current phase, next actions (P0–P3), blockers, and definition of done.

---

## State file fields

| Field | Purpose |
|---|---|
| `## Status` | One-liner: current phase + overall health |
| `## Current Phase` | Phase name + done-when condition |
| `## Current Focus` | What's actively being worked on right now |
| `## Next Actions` | P0 (this week) → P3 (parking lot) |
| `## Blockers` | What's stuck — or "-" if none |
| `## Done ✅` | Completed milestones |
| `## Definition of Done` | What "complete" looks like |

**Priority tags:** `P0` this week · `P1` this month · `P2` when capacity allows · `P3` parking lot

---

## Adding a new project

Tell the Secretary agent: *"อยากเริ่ม project ใหม่เรื่อง X"*

The agent will:
1. Classify it (Project / Area / Todo) using PARA rules
2. Show a draft for you to confirm
3. Scaffold the state file + Claude.ai workspace in `Resources/claude-ai/`
4. Add routing keywords to the Secretary automatically

Or run `/new-claude-project [name]` directly.

---

## Claude.ai mobile context

Each project can have a matching workspace in `Resources/claude-ai/[project-name]/` with knowledge files for use in Claude.ai on mobile. Run `/sync-claude-project` to keep them up to date.

---

## Example

See `_example-project/` for the folder structure. State file template is at `system/templates/project-state-template.md`.
