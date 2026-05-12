# API Contracts

> [!note] LLM Context File
> Schema ที่ AI ใช้ verify ว่า implementation ตรงกับ contract
> Updated: YYYY-MM-DD

---

## Base URL

| Env | Base URL |
|---|---|
| Local | `http://localhost:3000/api` |
| Production | `https://[domain]/api` |

---

## Authentication

- Method: [Bearer token / Cookie / API Key]
- Header: `Authorization: Bearer <token>`
- Token lifetime: [e.g. 7 days]

---

## Response Format

ทุก endpoint return format นี้:

```typescript
// Success
{ data: T, error: null }

// Error
{ data: null, error: { code: string, message: string } }
```

---

## Endpoints

### Auth

```
POST /auth/register
Body: { email: string, password: string, name: string }
Response: { data: { userId: string, token: string } }

POST /auth/login
Body: { email: string, password: string }
Response: { data: { userId: string, token: string } }
```

### [Resource Name]

```
GET  /[resource]
GET  /[resource]/:id
POST /[resource]
PUT  /[resource]/:id
DELETE /[resource]/:id
```

---

## Error Codes

| Code | Meaning |
|---|---|
| `UNAUTHORIZED` | Token missing or invalid |
| `FORBIDDEN` | Token valid but insufficient permission |
| `NOT_FOUND` | Resource not found |
| `VALIDATION_ERROR` | Request body failed validation |
| `INTERNAL_ERROR` | Server error |
