# Journal

Personal journal — daily entries and weekly reviews. All content here is private and gitignored.

---

## Structure

```
Journal/
├── Daily/                  ← daily notes (one file per day)
├── Weekly-Review/          ← weekly synthesis files
└── current-state.md        ← P0-only snapshot across all areas & projects (agent-maintained)
```

---

## Daily notes — FWIM format

Each daily entry captures four things:

| Field | Meaning |
|---|---|
| **F** act | What happened — observable events, no interpretation |
| **W** in | Something that went well or felt good |
| **I** mprove | Something to do differently |
| **M** eaning | What this day meant — the "so what" |

Run `/journal` to start a guided daily interview. The agent asks questions, you answer naturally — it formats and saves the entry automatically.

---

## Weekly review

Run `/weekly-review` at the end of each week. The agent:
1. Reads the last 7 daily entries
2. Synthesizes patterns across all domains
3. Updates `current-state.md` with a fresh P0 snapshot
4. Updates relevant `Areas/*/state-*.md` and `Projects/*/state-*.md`

---

## current-state.md

This file is the **agent's working memory** — a compact, always-current snapshot of what's happening across every area and project. It is:
- Written by the Weekly Review agent, not by you
- Read by the Secretary at the start of every session
- Limited to P0 items only (this week's priorities) — full details stay in state files
- Overwritten each week, not appended

---

## Privacy

Everything in this folder is gitignored — `Daily/`, `Weekly-Review/`, and `current-state.md` never leave your machine.
