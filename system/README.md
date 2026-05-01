# Personal Agent System

A modular agent framework for personal knowledge management and daily workflows.

Designed to work inside [Obsidian](https://obsidian.md) with [Claude Code](https://claude.ai/code), but built to be vault-agnostic — agents use abstract inputs, not hardcoded paths.

**→ [Setup Guide](SETUP.md)** — how to wire Claude Code into your Obsidian vault

---

## Structure

```
system/
├── agents/       — Agent definitions (purpose, input/output, routing logic)
├── prompts/      — Reusable prompt templates (copy-paste into any AI)
├── templates/    — Note templates (Obsidian-compatible)
├── examples/     — Filled-in examples for areas, projects, and prompts in action
├── README.md
├── SETUP.md      — Full setup guide: Claude + Obsidian integration
└── .gitignore
```

---

## Agents

| Agent | Role |
|-------|------|
| [Secretary](agents/agent_secretary.md) | Master orchestrator — reads context, routes requests to workers |
| [Journal Agent](agents/agent_journal.md) | Daily interview (Fact/Win/Improve/Meaning) + weekly review |
| [Knowledge Agent](agents/agent_knowledge.md) | Ingest sources into wiki, answer queries, run health checks |
| [Skill Optimizer](agents/agent_skill_optimizer.md) | Meta-agent — improves skill library and routing policy over time |

---

## Design Principles

- **Vault-agnostic** — abstract inputs (`{{input_context}}`, `{{note_topic}}`), no hardcoded paths
- **Self-contained files** — each agent/workflow documents its own Purpose, Input, Output, and Logic
- **Separation of concerns** — system (this repo) is independent from personal data and local config
- **Functional naming** — `agent_task_dispatcher.md`, not `note1.md`

---

## Usage

All files are plain-text specs — paste into any AI assistant (Claude, ChatGPT, etc.) as a system prompt or context block.

- **agents/** — full agent personas with routing logic and workflows embedded
- **prompts/** — standalone building blocks, ready to copy-paste
- **templates/** — note templates for your vault
- **examples/** — see prompts in action with real input/output samples

1. Open the agent or prompt file
2. Copy into your Claude/GPT session
3. Replace `{{placeholders}}` with actual context
4. Run

---

## Roadmap

- [x] Core agents: Secretary, Journal, Knowledge, Skill Optimizer
- [x] Prompts: journal interview, weekly review, knowledge ingest, secretary routing, session-to-wiki
- [x] Templates: daily note, area state, project state
- [x] Examples: area state, project state, all prompts in action
- [x] Setup guide: Claude + Obsidian integration
- [ ] Worker agents: Life Ops, Startup, Thailand, Review
- [ ] Automation layer (Phase 2)
