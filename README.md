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
CLAUDE.md                    ← always loaded (wiki agent + smart router)
Secretary.md                 ← your personal layer (routing, context)
Me.md                        ← your profile
Projects/                    ← active projects (end state + deadline)
Areas/                       ← ongoing responsibilities (no end date)
Journal/                     ← daily notes, weekly reviews
wiki/                        ← your knowledge base (grows as you ingest)
Resources/claude-ai/         ← Claude.ai mobile workspaces (one per project)
```

**Your data never leaves your machine.** Everything is plain Markdown.

---

## Getting content in

Knowledge comes from many places. Pick the method that fits the source:

**From the web — Obsidian Web Clipper**

Install the [Obsidian Web Clipper](https://obsidian.md/clipper) Chrome extension. Set the default save location to `raw/`. Clip any article, post, or page — then ingest it.

```
"ingest raw/my-clipped-article.md"
```

**From a file — manual drop**

Paste or save any content (notes, PDFs, exported chats, transcripts) directly into `raw/`, then ingest.

```
"ingest raw/expert-call-notes.md"
```

**From a conversation — session-to-wiki**

After any session — with Claude, an expert, a friend, or a mentor — where useful ideas or decisions came up, run:

```
/session-to-wiki
```

The skill summarizes the session and writes a source page to `wiki/sources/` automatically. Use it after sessions with important decisions, new frameworks, or insights — not for routine tasks.

---

## Commands

| Command | When to use |
|---|---|
| `/journal` | Daily FWIM interview → saves entry to `Journal/Daily/` |
| `/weekly-review` | End of week — synthesizes journal, updates all state files |
| `/session-to-wiki` | After a useful conversation — saves insights to wiki |
| `/deep-wiki-ingest` | Ingest a raw source file with full detail |
| `/new-claude-project [name]` | Scaffold a new project (state file + Claude.ai workspace) |
| `/sync-claude-project` | Sync `Resources/claude-ai/` knowledge files with current vault state |
| `/skill-optimizer` | Review and improve the agent skill library |

---

## Claude.ai on mobile

Each project can have a matching workspace in `Resources/claude-ai/[project-name]/` — a folder of knowledge files you upload to a Claude.ai project for mobile use.

Run `/sync-claude-project` to keep all workspaces up to date after state changes. Run `/new-claude-project [name]` to scaffold a workspace for a new project.

---

## Customization

Copy `Secretary.template.md` → `Secretary.md` and fill in your own domains, projects, and routing preferences.

Copy `Me.template.md` → `Me.md` and fill in your profile. The agents use this to give context-aware responses.

---

## Tips & tricks

**Obsidian Web Clipper** — a browser extension that converts web articles to Markdown. Very useful for quickly getting sources into your `raw/` collection.

**Download images locally** — In Obsidian Settings → Files and links, set "Attachment folder path" to `raw/assets/`. Then in Settings → Hotkeys, search for "Download" and bind "Download attachments for current file" to a hotkey (e.g. `Ctrl+Shift+D`). After clipping an article, hit the hotkey and all images are saved locally. Note: LLMs can't read inline images in one pass — the workaround is to have the agent read the text first, then view referenced images separately for additional context.

**Graph view** — Obsidian's graph view is the best way to see the shape of your wiki: what's connected, which pages are hubs, which are orphans.

**Marp** — a Markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.

**Dataview** — an Obsidian plugin that runs queries over page frontmatter. If your agent adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.

**Version control** — the wiki is just a git repo of Markdown files. You get version history, branching, and collaboration for free.

---

## License

MIT — free to use, fork, and build on.
See [LICENSE](LICENSE).
