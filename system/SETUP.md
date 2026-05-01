# Setup Guide — Claude + Obsidian

How to wire Claude Code into your Obsidian vault so agents have full context and can read/write notes directly.

---

## Prerequisites

- [Obsidian](https://obsidian.md) — vault already created
- [Claude Code](https://claude.ai/code) — CLI installed and authenticated
- Terminal access to your vault folder

---

## How It Works

```
Obsidian vault/
└── CLAUDE.md          ← Claude reads this automatically on every session
                          Contains: who you are, folder structure, agent routing rules
```

Claude Code runs **inside your vault folder**. It can read and write `.md` files directly — no plugins needed.

The `CLAUDE.md` file acts as a persistent system prompt. Every session, Claude reads it first and orients itself before responding.

---

## Step 1 — Run Claude Code from Your Vault

```bash
cd /path/to/your/vault
claude
```

That's it. Claude now has access to all your notes.

---

## Step 2 — Create CLAUDE.md

`CLAUDE.md` is the most important file. It tells Claude:
- Who you are and what your goals are
- What the folder structure means
- Which files to read when you ask about a specific domain
- How to behave (language, tone, when to push back)

**Minimal CLAUDE.md structure:**

```markdown
# CLAUDE.md

## Who I am
{{your name, role, goals, personality}}

## Folder Structure
{{explain what each folder contains}}

## Secretary Routing
When I mention X topic → read {{file}} before responding

| Keywords | Read first |
|----------|-----------|
| finance, money | Areas/finance/state.md |
| work, project | Projects/{{project}}/state.md |

## Behavior
- Respond in {{language}}
- Keep answers short and direct
```

---

## Step 3 — Session Start Protocol

Add this to CLAUDE.md so Claude always orients itself at the start:

```markdown
## Session Start
1. Read CLAUDE.md (this file)
2. Read Me.md — current goals and projects
3. Read Journal/current-state.md — live status across all areas
4. Greet me with a short status summary
```

Claude will follow this automatically every new session.

---

## Step 4 — Install Agent Skills (Optional)

Skills add slash commands (`/journal`, `/weekly-review`) that trigger agents directly.

```bash
# Install from skills.sh
npx skills install journal
npx skills install weekly-review
```

After install, type `/journal` in Claude Code to start a daily interview.

Browse available skills: [skills.sh](https://skills.sh)

---

## Step 5 — Set Obsidian Template Folder

If you use the templates from this repo:

```
Obsidian Settings → Templates → Template folder location
Set to: system/templates
```

---

## Recommended Vault Structure

```
vault/
├── CLAUDE.md                      ← agent config (required)
├── Me.md                          ← your profile, goals, active projects
│
├── Journal/
│   ├── current-state.md           ← live state across all domains (agent-maintained)
│   ├── Daily/                     ← one file per day: YYYY-MM-DD.md
│   └── Weekly-Review/             ← one file per week: YYYY-WNN.md
│
├── Projects/                      ← active projects only
│   └── my-project/
│       └── state.md               ← phase, done, next actions, blockers
│
├── Areas/                         ← ongoing life areas (no end date)
│   └── finance/
│       └── state.md               ← numbers, open loops, focus
│
├── Resources/                     ← reference material + agent system config
│   ├── agents/                    ← personal agent definitions (vault-specific)
│   │   └── agent-name.md
│   └── skills/
│       ├── inbox/                 ← drop skill ideas here for Skill Optimizer
│       ├── shared/                ← skills available to all agents
│       │   └── skill-name.md
│       └── agents/                ← skills scoped to specific agents
│           └── agent-name/
│               └── skill-name.md
│
├── wiki/                          ← LLM-maintained knowledge wiki
│   ├── index.md                   ← master catalog (agent-maintained)
│   ├── log.md                     ← append-only activity log
│   ├── overview.md                ← high-level synthesis
│   ├── sources/                   ← one page per ingested source
│   ├── entities/                  ← people, orgs, places, products
│   └── concepts/                  ← ideas, frameworks, methodologies
│
├── raw/                           ← source documents, immutable
│   └── assets/                    ← downloaded images and attachments
│
├── Archive/                       ← completed projects and outdated notes
│   └── completed-project/
│
└── system/                        ← this repo (agents, workflows, templates)
```

---

## Folder Lifecycle

### Projects → Archive
Move a project to `Archive/` when its Definition of Done is met.

```
Projects/my-project/ → Archive/my-project/
```

Keep the `state.md` as a record. Add a final note:
```markdown
## Completed
YYYY-MM-DD — [one sentence on outcome]
```

### Resources/skills/inbox
The Skill Optimizer monitors this folder. Drop a raw idea as a `.md` file:
```markdown
# Idea: habit-streak-calculator
use when: user asks about streak counts or habit consistency
```
Skill Optimizer processes it → creates proper skill file → deletes from inbox.

### Areas vs Projects
| | Projects | Areas |
|---|---|---|
| Has end date | ✅ | ❌ |
| Has Definition of Done | ✅ | ❌ |
| When finished | → Archive | stays active |
| Example | "Launch MVP" | "Finance", "Health" |

---

## The State File Pattern

Each Project and Area has a `state.md` — a living document that agents update over time.

```
Projects/my-project/state.md   ← current phase, done, next actions, blockers
Areas/finance/state.md         ← current numbers, open loops, focus
```

Claude reads the relevant state file before answering questions about that domain. This keeps context tight — no need to re-explain your situation every session.

Use the templates in `system/templates/` to create state files:
- `project-state-template.md`
- `area-state-template.md`

---

## Daily Usage Pattern

```
Morning:  /journal          → daily note interview
Evening:  ask Claude        → secretary routes to correct context automatically
Weekly:   /weekly-review    → synthesize week, update current-state.md
Ad hoc:   paste + "ingest"  → Knowledge Agent files it into wiki
```
