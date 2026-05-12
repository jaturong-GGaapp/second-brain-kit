# Design System

> [!note] LLM Context File
> Design tokens + animation system สำหรับ AI ใช้ implement UI ให้ consistent
> Updated: YYYY-MM-DD

---

## Colors

```typescript
// Primary
primary: {
  50: '#[hex]',
  100: '#[hex]',
  500: '#[hex]',   // main
  900: '#[hex]',
}

// Semantic
background: '#[hex]'
surface: '#[hex]'
textPrimary: '#[hex]'
textSecondary: '#[hex]'
error: '#[hex]'
success: '#[hex]'
```

---

## Typography

| Token | Size | Weight | Usage |
|---|---|---|---|
| `heading-xl` | 32px | 700 | Page titles |
| `heading-lg` | 24px | 700 | Section titles |
| `heading-md` | 20px | 600 | Card titles |
| `body-lg` | 16px | 400 | Body text |
| `body-sm` | 14px | 400 | Secondary text |
| `caption` | 12px | 400 | Labels, hints |

---

## Spacing

Base unit: **4px**

| Token | Value |
|---|---|
| `xs` | 4px |
| `sm` | 8px |
| `md` | 16px |
| `lg` | 24px |
| `xl` | 32px |
| `2xl` | 48px |

---

## Animation System

> Animation เป็น system — implement ตาม tokens นี้เสมอ ห้าม hardcode duration/easing

| Token | Type | Duration | Easing | Usage |
|---|---|---|---|---|
| `anim-instant` | immediate | 0ms | - | State updates ที่ไม่ต้องการ feedback |
| `anim-micro` | micro | 100ms | `ease-out` | Button press, hover |
| `anim-fast` | transition | 200ms | `ease-in-out` | Modal open/close, expand |
| `anim-medium` | transition | 300ms | `ease-in-out` | Page transitions, slide |
| `anim-slow` | transition | 500ms | `ease-in-out` | Onboarding, celebration |

```typescript
// Usage example
transition: `all ${tokens.anim.fast.duration} ${tokens.anim.fast.easing}`
```

---

## Breakpoints

| Token | Value | Target |
|---|---|---|
| `sm` | 640px | Mobile landscape |
| `md` | 768px | Tablet |
| `lg` | 1024px | Desktop |
| `xl` | 1280px | Wide desktop |

---

## Border Radius

| Token | Value | Usage |
|---|---|---|
| `radius-sm` | 4px | Inputs, chips |
| `radius-md` | 8px | Cards, buttons |
| `radius-lg` | 12px | Modals, sheets |
| `radius-full` | 9999px | Pills, avatars |
