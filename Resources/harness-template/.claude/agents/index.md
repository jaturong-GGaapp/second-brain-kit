# Agents

> นี่คือ target ของ `Agents.md` symlink ที่ vault root

## Agent Pipeline

```
planner → coder → reviewer
```

| Agent | File | Role | Guardrail |
|---|---|---|---|
| planner | `.claude/agents/planner.md` | Break request → task list | ห้าม implement |
| coder | `.claude/agents/coder.md` | Implement single task | ห้ามแก้ wiki/, decisions/, .claude/ |
| reviewer | `.claude/agents/reviewer.md` | Review + validate | เขียน wiki ได้หลัง approve |

## Commands

| Command | File | Description |
|---|---|---|
| `/init-wiki` | `.claude/commands/init-wiki.md` | กรอก wiki ครั้งแรกจาก project context |
| `/new-feature [name]` | `.claude/commands/new-feature.md` | Scaffold feature ผ่าน full pipeline |
| `/new-decision [topic]` | `.claude/commands/new-decision.md` | สร้าง ADR |
| `/update-wiki` | `.claude/commands/update-wiki.md` | Sync wiki หลัง decision ใหม่ |

## LLM Wiki (Source of Truth)

| File | Purpose |
|---|---|
| `wiki/architecture.md` | Project structure + package boundaries |
| `wiki/coding_rules.md` | Code style + forbidden patterns |
| `wiki/api_contracts.md` | API schemas |
| `wiki/design_system.md` | Design tokens |

## Skills

See `.claude/skills/index.md`
