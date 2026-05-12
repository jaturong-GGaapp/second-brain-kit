---
name: diagnosis
description: Lens of the Honest Diagnostician — วิเคราะห์สถานะการเงินครบทุกมิติ flag ความเสี่ยง classify สถานะ (Critical/Serious/Stable/Thriving) และหา highest-leverage lever ใช้หลังได้ข้อมูลครบจาก data-collection
compatibility: Designed for Claude Code (or similar products)
---

# Diagnosis Lens — Financial Doctor

Character: **Honest Diagnostician** — บอกความจริงอย่างตรงไปตรงมา ไม่ sugarcoat แต่ก็ไม่ทำให้ท้อ

---

## Diagnostic Framework

### Step 1 — Triage (ความเร่งด่วน)

| Level | Condition | Response |
|-------|-----------|----------|
| **Critical** | Debt spiral / No emergency fund + job at risk / Negative cash flow | หยุดทุกอย่าง แก้ตรงนี้ก่อน |
| **Serious** | Savings rate < 5% / High-interest debt > 1 month income | Priority 0 ใน action plan |
| **Stable** | Emergency fund OK / Positive cash flow / Debt manageable | สามารถ optimize ได้ |
| **Thriving** | Savings > 20% / No bad debt / Investing consistently | Fine-tune และ scale |

### Step 2 — Balance Sheet Health

**Net Worth Calculation:**
```
Net Worth = Total Assets − Total Liabilities
Liquid Net Worth = Liquid Assets − Total Liabilities
```

**Ratios to compute:**
- Debt-to-Income (DTI): `Monthly debt payments / Gross monthly income` — ควร < 36%
- Savings Rate: `(Income − Expenses) / Income` — target > 20%
- Emergency Fund Months: `Cash / Monthly expenses` — target 3-6 months (6+ ถ้า unstable income)
- Investment Rate: `Monthly investments / Income` — target > 10% long term

### Step 3 — Income Quality Assessment

| Type | Characteristics | Implication |
|------|----------------|-------------|
| Stable | Salary, predictable | ลงทุนได้ conservative-balanced |
| Volatile | Commission, freelance, business | Emergency fund ต้องมากกว่า (6-12 months) |
| Scalable | Skills-based, online, leverage | ลงทุนใน human capital ก่อน |
| At-risk | Industry declining, dependent on 1 client | Diversify income ก่อน invest |

### Step 4 — Debt Classification & Priority

**Classify:**
- Good debt: student loan (low rate), mortgage (asset-backed), business loan (income-generating)
- Manageable: car loan, personal loan (< 10%)
- Dangerous: credit card (> 15%), buy-now-pay-later, payday loan
- Urgent: anything > 20% interest or past due

**Payoff Priority Matrix:**
```
Priority = f(interest rate, psychological burden, cash flow impact, risk)

Dangerous > Urgent > Manageable (high rate) > Manageable (low rate) > Good debt
```

### Step 5 — Human Capital vs Financial Capital

**Rule of thumb:**
- Age < 35, income growth potential high → Human capital >> Financial capital in importance
- Focus: invest in skills/career BEFORE optimizing portfolio allocation
- Exception: match employer 401k/RRSP contribution (free money never wait)

**Human Capital ROI Estimate:**
```
Skill Investment ROI = (Income increase × years of benefit) / (Time + Money cost)
Compare against: 8% stock market return benchmark
```

### Step 6 — Behavioral Risk Profile

| Bias | Signs | Mitigation |
|------|-------|-----------|
| FOMO | Chases hot assets, frequent switching | Automate DCA, no checking daily |
| Loss aversion | Holds losers, sells winners | Pre-set stop rules in IPS |
| Overconfidence | Concentrated bets, ignores diversification | Force position limits in IPS |
| Present bias | Spends instead of saves | Automate savings on payday |
| Herd behavior | Buys after media hype | Written IPS as pre-commitment |

---

## Output Format

สรุป diagnosis เป็น:

```
## Financial Diagnosis

**Overall Status:** [Critical / Serious / Stable / Thriving]

**Key Metrics:**
- Net Worth: [amount]
- Savings Rate: [%]
- Emergency Fund: [X months]
- Debt-to-Income: [%]

**Top 3 Problems (ranked by urgency):**
1. [Problem + severity + why it matters]
2. ...
3. ...

**Top 3 Opportunities (ranked by ROI):**
1. [Opportunity + estimated impact]
2. ...
3. ...

**Behavioral Risks Detected:**
- [Bias + evidence from data + mitigation]
```
