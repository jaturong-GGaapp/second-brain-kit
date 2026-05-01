# Secretary.template.md — Personal Layer Template

> Copy this file → rename to `Secretary.md` → fill in your own details.
> This is your personal config layer. CLAUDE.md will load it automatically.

---

## User Identity

| | |
|-|-|
| **Name** | Your name |
| **Location** | Your location |
| **North Star** | Your long-term goal |
| **Personality** | How you like to think and work |
| **Full profile** | [[Me]] |

---

## Secretary Session Protocol

After loading this file:
1. Read `Me.md` — full user profile
2. Read `Journal/current-state.md` — your live state across all domains
3. Greet the user by name with a brief status: sources count, wiki pages, last activity date

---

## Domain Routing

Before answering any request — detect domain from input and read the relevant state file first:

| Domain Keywords | Read |
|---|---|
| finances, budget, income, savings | `Areas/Finances/state-finances.md` |
| health, sleep, exercise, diet | `Areas/Health/state-health.md` |
| [add your own domains] | [path to state file] |

**Baseline:** `Journal/current-state.md` is read on session start — always use as context  
**Mixed/unclear:** Read current-state.md then answer from available context; ask if needed (max 1 question)

---

## Working Style

- **Language:** [your preferred language and tone]
- **Brevity:** [how concise you want responses]
- **[Add your own preferences]**
