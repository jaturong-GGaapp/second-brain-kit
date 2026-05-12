# Architecture

> [!note] LLM Context File
> ไฟล์นี้คือ source of truth สำหรับ AI — อัปเดตผ่าน `/update-wiki` เท่านั้น
> Updated: YYYY-MM-DD

---

## Project Overview

**Project:** [Project name]
**Type:** [Web app / Mobile app / API / Monorepo / etc.]
**Stack:** [e.g. Next.js 14, TypeScript, Prisma, PostgreSQL]

---

## Directory Structure

```
<project-root>/
├── [list your directories here]
```

---

## Package Boundaries

> กฎสำคัญ: package X ห้าม import จาก package Y ยกเว้นระบุไว้

| Package / Layer | Can import from | Cannot import from |
|---|---|---|
| `apps/web` | `packages/core`, `packages/ui-tokens` | `apps/mobile` |
| `packages/core` | - (standalone) | `apps/`, `packages/api` |
| `packages/api` | `packages/core` | `apps/` |

---

## Data Flow

```
[describe your data flow here]
e.g. User → UI → API Route → Service → Database
```

---

## Key Decisions

- [Decision 1 — see decisions/ADR-XXX.md]
- [Decision 2 — see decisions/ADR-XXX.md]

---

## Environment

| Env | URL / Config |
|---|---|
| Local | `http://localhost:3000` |
| Staging | [URL] |
| Production | [URL] |
