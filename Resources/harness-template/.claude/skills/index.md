# Skills

## Agents

| Agent | File | Role |
|---|---|---|
| planner | `.claude/agents/planner.md` | Break request → task list |
| coder | `.claude/agents/coder.md` | Implement single task |
| reviewer | `.claude/agents/reviewer.md` | Review + validate |

## Commands

| Command | File | Trigger |
|---|---|---|
| init-wiki | `.claude/commands/init-wiki.md` | `/init-wiki` (ครั้งแรกหลัง setup) |
| new-feature | `.claude/commands/new-feature.md` | `/new-feature [name]` |
| new-decision | `.claude/commands/new-decision.md` | `/new-decision [topic]` |
| update-wiki | `.claude/commands/update-wiki.md` | `/update-wiki` |

## LLM Wiki Files

| File | Purpose |
|---|---|
| `wiki/architecture.md` | Project structure + boundaries |
| `wiki/coding_rules.md` | Style + forbidden patterns |
| `wiki/api_contracts.md` | API schemas |
| `wiki/design_system.md` | Tokens + animation system |
