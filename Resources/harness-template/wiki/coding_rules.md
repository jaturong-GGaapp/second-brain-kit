# Coding Rules

> [!note] LLM Context File
> ทุก agent ต้อง enforce rules เหล่านี้ — reviewer reject ถ้า violate
> Updated: YYYY-MM-DD

---

## Language & Type Safety

- ใช้ **TypeScript strict mode** — ห้าม `any` type ทุกกรณี
- ห้าม `// @ts-ignore` หรือ `// eslint-disable` โดยไม่มี comment อธิบาย
- ทุก function ที่ return type ไม่ obvious ต้องมี explicit return type annotation

---

## Naming Conventions

| Thing | Convention | Example |
|---|---|---|
| Component | PascalCase | `UserCard`, `AuthModal` |
| Function | camelCase | `getUserById`, `formatDate` |
| Constant | SCREAMING_SNAKE | `MAX_RETRY_COUNT` |
| File (component) | PascalCase | `UserCard.tsx` |
| File (util/hook) | camelCase | `useAuth.ts`, `formatDate.ts` |
| CSS class | kebab-case | `user-card__avatar` |

---

## Forbidden Patterns

- ❌ ห้าม `console.log` ใน production code — ใช้ logger utility แทน
- ❌ ห้าม hardcode secrets หรือ API keys
- ❌ ห้าม mutate props โดยตรง (React)
- ❌ ห้าม `useEffect` without dependency array (เว้นแต่ตั้งใจ + comment)
- ❌ ห้าม import circular dependencies

---

## File Organization

- 1 component per file
- ไฟล์ที่ยาวกว่า 300 lines ควรแตกออก
- Test file อยู่ข้างๆ implementation: `Component.test.tsx`

---

## Error Handling

- ทุก async function ต้อง handle error — ห้าม silent catch
- User-facing errors ต้องมี message ที่ readable (ไม่ใช่ raw error message จาก server)
- Log error ด้วย context: `logger.error('context message', { error, userId })`

---

## Comments

- เขียน comment เฉพาะเมื่อ **"ทำไม"** ไม่ชัดเจน
- ห้ามเขียน comment อธิบาย "ทำอะไร" — code ควรอ่านได้เอง
- ห้าม commented-out code ใน PR

---

## Git

- Commit message format: `type(scope): description`  
  e.g. `feat(auth): add email verification flow`
- Types: `feat`, `fix`, `refactor`, `docs`, `chore`, `test`
- ห้าม commit โดยตรงที่ `main` — ใช้ feature branch เสมอ
