# Second Brain Kit

A personal knowledge system with AI agents — ready to use in 5 minutes.

Built on [Obsidian](https://obsidian.md) + [Claude Code](https://claude.ai/code).

---

## What you get

- **Wiki agent** — ingest sources, query your knowledge, keep it linked
- **Secretary** — routes any request to the right agent automatically
- **Journal agent** — daily interview + weekly review that updates your context
- **Skill Optimizer** — improves the system over time as you use it
- **Your own brain** — all knowledge stays local, in plain Markdown files

---

## Requirements

- [Obsidian](https://obsidian.md) (free)
- [Claude Code](https://claude.ai/code) **or** Claude Desktop with filesystem access

---

## Install

```bash
git clone https://github.com/YOUR_USERNAME/second-brain-kit.git
cd second-brain-kit
python3 setup.py
```

Then:
1. Open the folder in Obsidian as a vault
2. Open Claude Code in the same folder
3. Fill in `Me.md` with your profile
4. Fill in `Secretary.md` with your life areas

Your agent is ready.

---

## How it works

```
CLAUDE.md           ← always loaded (wiki agent + smart router)
Secretary.md        ← your personal layer (routing, context)
Me.md               ← your profile
Journal/            ← daily notes, weekly reviews
wiki/               ← your knowledge base (grows as you ingest)
```

**Your data never leaves your machine.** Everything is plain Markdown.

---

## Customization

Copy `Secretary.template.md` → `Secretary.md` and fill in your own domains, projects, and routing preferences.

Copy `Me.template.md` → `Me.md` and fill in your profile. The agents use this to give context-aware responses.

---

## License

MIT — free to use, fork, and build on.
See [LICENSE](LICENSE).
