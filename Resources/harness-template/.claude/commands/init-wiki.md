# /init-wiki

กรอก LLM wiki files ทั้ง 4 ไฟล์จาก context ที่ผู้ใช้ให้มา

## When to Use

รัน **ครั้งเดียวหลัง setup** — เพื่อกรอก wiki/ ที่ยังเป็น template ว่างๆ ให้มีข้อมูลจริง

## Step 1 — Request Context Dump

บอกผู้ใช้:

> "Paste หรืออธิบาย project ของคุณ — ใส่ได้ทุกอย่าง:
> - README หรือ project description
> - Tech stack ที่ใช้ (framework, database, libraries)
> - Directory structure หรือ monorepo layout
> - Package boundaries (อะไร import อะไรได้บ้าง)
> - API endpoints ที่มีหรือวางแผนไว้
> - Design decisions ที่ทำไปแล้ว (เลือก library ไหน ทำไม)
> - Coding rules ของ team (ถ้ามี)
>
> ไม่ต้องครบ — ใส่เท่าที่มี AI จะ infer ส่วนที่เหลือและ mark ว่า TODO"

รอ context จากผู้ใช้ก่อน — **อย่า generate wiki โดยไม่มี input**

## Step 2 — Parse Context

จาก context ที่ได้ ดึงข้อมูลสำหรับแต่ละ wiki file:

**architecture.md ต้องการ:**
- Project name + type (web/mobile/API/monorepo)
- Tech stack
- Directory structure (ถ้ามีบอก หรือ infer จาก stack)
- Package boundaries
- Data flow
- Environment URLs (ถ้ามี)

**coding_rules.md ต้องการ:**
- Language (TypeScript/JavaScript/Python/etc.)
- Framework-specific rules
- Naming conventions ที่ระบุ หรือ infer จาก stack (e.g. Next.js → PascalCase components)
- Forbidden patterns ที่ระบุ
- Rules ทั่วไปที่ infer ได้จาก best practices ของ stack นั้น

**api_contracts.md ต้องการ:**
- Auth method
- Base URL pattern
- Endpoints ที่รู้ (ถ้ายังไม่มี → ใส่ placeholder ที่สมเหตุสมผล)
- Response format

**design_system.md ต้องการ:**
- Color palette (ถ้ามี หรือ mark TODO)
- Typography scale (infer จาก framework ถ้าไม่ระบุ)
- Spacing system
- Animation tokens

## Step 3 — Show Draft + Confirm

แสดง draft ของทุก wiki file ให้ผู้ใช้เห็นก่อน:

```
## Draft: wiki/architecture.md
[content...]

## Draft: wiki/coding_rules.md
[content...]

## Draft: wiki/api_contracts.md
[content...]

## Draft: wiki/design_system.md
[content...]

---
มีอะไรต้องแก้ก่อน write ไหม? (y แก้ / n write เลย)
```

**หยุดรอ confirm** — อย่า write ก่อนได้รับ approval

## Step 4 — Write Wiki Files

เขียนทับ wiki files ทั้ง 4:
- `wiki/architecture.md`
- `wiki/coding_rules.md`
- `wiki/api_contracts.md`
- `wiki/design_system.md`

ใส่ `Updated: [today's date]` ที่ header ของทุกไฟล์

## Step 5 — Report

```
✅ wiki initialized

Files written:
- wiki/architecture.md
- wiki/coding_rules.md
- wiki/api_contracts.md
- wiki/design_system.md

TODOs (กรอกเพิ่มเติมเอง):
- [list สิ่งที่ mark TODO เพราะ context ไม่พอ]
```

## Rules

- ข้อมูลที่ไม่รู้ → mark `[TODO: ...]` อย่า guess แล้ว present เป็นข้อเท็จจริง
- ถ้า context ขัดแย้งกัน → ถามผู้ใช้ก่อน write
- อย่าลบ section structure ของ template — กรอกข้อมูลเข้าไป ไม่ใช่ rewrite format
