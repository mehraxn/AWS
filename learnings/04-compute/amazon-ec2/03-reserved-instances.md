# 💡 EC2 Reserved Instances (RI) — Standard vs Convertible

> A structured study guide for AWS practitioners and exam candidates.  
> Covers all RI dimensions: offering class, scope, term, and payment options.

---

## 📚 Table of Contents

1. [What is an EC2 Reserved Instance?](#1-what-is-an-ec2-reserved-instance)
2. [The Two Main RI Types](#2-the-two-main-ri-types)
3. [Standard Reserved Instance](#3-standard-reserved-instance)
4. [Convertible Reserved Instance](#4-convertible-reserved-instance)
5. [What Can Be Changed?](#5-what-can-be-changed)
6. [General RI Settings](#6-general-ri-settings)
7. [RI Term: 1 Year vs 3 Years](#7-ri-term-1-year-vs-3-years)
8. [RI Payment Options](#8-ri-payment-options)
9. [RI Scope: Regional vs Zonal](#9-ri-scope-regional-vs-zonal)
10. [Regional RI](#10-regional-ri)
11. [Zonal RI](#11-zonal-ri)
12. [Capacity Reservation Confusion](#12-capacity-reservation-confusion)
13. [RI Marketplace](#13-ri-marketplace)
14. [Common Mistakes](#14-common-mistakes)
15. [Quick Memory Rules](#15-quick-memory-rules)
16. [Final Summary & Comparison Table](#16-final-summary--comparison-table)

---

## 1. What is an EC2 Reserved Instance?

An **EC2 Reserved Instance (RI)** is a **pricing commitment**, not a separate type of EC2 machine.

> You commit to using a certain type of EC2 capacity for **1 year or 3 years**, and AWS gives you a **discount** compared to On-Demand pricing.

When you purchase an RI, AWS automatically applies the discount to **matching EC2 usage** in your account — you still need to launch and run the instances yourself.

**Example:**

```
You buy an RI for: Linux | m5.large | us-east-1
You run a matching: Linux | m5.large | us-east-1 instance
→ AWS applies the RI discount automatically to that usage.
```

> ⚠️ **Tutor Note:** This is one of the most misunderstood concepts for beginners. Many students think purchasing an RI automatically provisions an EC2 instance — it does not. Think of an RI as a *discount coupon* that applies when your running instances match the committed attributes. If no matching instance is running, the RI cost still applies but you get no compute in return — wasted money.

---

## 2. The Two Main RI Types

EC2 Reserved Instances have two **offering classes**:

```
EC2 Reserved Instance
├── Standard Reserved Instance    → Bigger discount, less flexibility
└── Convertible Reserved Instance → Smaller discount, more flexibility
```

> 📌 **One-liner to remember:**
> `Standard RI = savings first` | `Convertible RI = flexibility first`

---

## 3. Standard Reserved Instance

A **Standard RI** delivers the **highest discount** available among RI types — but in exchange, it locks you into specific instance attributes.

**Best for:** Stable, predictable workloads where you're confident about the instance family, OS, Region, and tenancy for 1–3 years.

### Key Properties

| Property | Details |
|---|---|
| 💰 Discount | Highest among RI offering classes (up to ~72% vs On-Demand) |
| 🔒 Flexibility | Lower — attributes are mostly fixed |
| ♻️ Exchangeable? | ❌ No — cannot be exchanged into a different offering class |
| 🔧 Modifiable? | ✅ Yes — within limits (AZ, scope, size in same family) |
| 🏪 RI Marketplace? | ✅ Yes — eligible Standard RIs can be listed for sale |
| 🎯 Best for | Very stable, unchanged workloads |

### Exam Rule

```
Standard RI → maximum savings, minimum flexibility
```

> 📌 **Exam tip:** If a question describes a company with a steady-state workload (e.g., always-on database server, consistent web tier) and asks for the *largest discount*, **Standard RI** is your answer.

---

## 4. Convertible Reserved Instance

A **Convertible RI** offers a **lower discount** than Standard RI, but provides the ability to **exchange** your RI for a different one if your needs change.

**Best for:** Predictable long-term usage where the instance family, OS, or tenancy *might* evolve over the commitment period.

**Example scenario:**

```
Today:  running m5 instances (memory-balanced workload)
Future: may migrate to c6i instances (compute-optimized)
→ Convertible RI lets you exchange without losing the discount entirely.
```

### Key Properties

| Property | Details |
|---|---|
| 💰 Discount | Lower than Standard RI (up to ~66% vs On-Demand) |
| 🔓 Flexibility | Higher — can exchange to a different Convertible RI |
| ♻️ Exchangeable? | ✅ Yes — exchange for another Convertible RI of equal or greater value |
| 🔧 Modifiable? | ✅ Yes — within limits |
| 🏪 RI Marketplace? | ❌ No — Convertible RIs cannot be sold in the Marketplace |
| 🎯 Best for | Predictable workloads that may change attributes over time |

### Exam Rule

```
Convertible RI → flexibility + discount, but NOT the maximum discount
```

> 📌 **Exam tip:** If a question says the company wants a long-term commitment but *might need to change* instance family, OS, or tenancy — go with **Convertible RI**. The keyword to watch for is "may change" or "expects to evolve."

---

## 5. What Can Be Changed?

This is a common source of confusion. There are two distinct mechanisms: **modification** and **exchange**.

### Standard RI — Modification Only

Standard RIs **cannot be exchanged** but can be **modified** within limits:

| Attribute | Modifiable? |
|---|---|
| Availability Zone | ✅ Yes |
| Scope (Regional ↔ Zonal) | ✅ Yes |
| Instance size (same family) | ✅ In some cases |
| Instance family | ❌ No |
| Operating System | ❌ No |
| Tenancy | ❌ No |

```
Allowed:  m5.large → m5.xlarge  (same family, different size)
Not allowed: m5.large → c6i.large  (different family)
```

### Convertible RI — Exchange Mechanism

Convertible RIs support a formal **exchange** to a new Convertible RI, allowing changes to:

- Instance family (e.g., m5 → c6i)
- Instance type
- Operating system
- Tenancy
- Scope (Regional ↔ Zonal)

> ⚠️ **Important condition:** The new Convertible RI must be of **equal or greater value**. You cannot exchange "down" — AWS won't return money if the new RI is cheaper.

> 📌 **Tutor Note:** Think of the Convertible RI exchange like upgrading an airline ticket — you can always move to a more expensive seat, but you can't get a refund for the difference if you move to a cheaper one. Plan your exchange accordingly.

---

## 6. General RI Settings

These settings apply to **both** Standard and Convertible RIs:

```
Reserved Instance
├── Offering class   → Standard | Convertible
├── Term             → 1 year | 3 years
├── Payment option   → No Upfront | Partial Upfront | All Upfront
├── Scope            → Regional | Zonal
├── Platform/OS      → Linux | Windows | etc.
├── Tenancy          → Default | Dedicated
└── Instance attrs   → Family, type, size, Region
```

---

## 7. RI Term: 1 Year vs 3 Years

| Term | Discount | Best for |
|---|---|---|
| 1 Year | Smaller | Shorter commitments, moderate savings |
| 3 Years | Larger | Long-term workloads, maximum savings |

```
Rule: Longer commitment = bigger discount
```

> 📌 **Tutor Note:** The 3-year term gives significantly more savings, but only makes sense if you're highly confident the workload will remain stable. Committing to 3 years on an instance type that gets replaced by a newer generation could leave you with an RI that's technically still discounting but on outdated hardware. For rapidly evolving applications, 1-year terms or Savings Plans may be smarter.

---

## 8. RI Payment Options

| Option | Upfront Cost | Discount Level | When to Choose |
|---|---|---|---|
| No Upfront | $0 at purchase | Lowest among RI options | Minimal cash commitment |
| Partial Upfront | Partial at purchase | Middle | Balanced approach |
| All Upfront | Full amount at purchase | Highest | Maximum savings, cash available |

```
Rule: More upfront payment = more discount
```

> 📌 **Tutor Note:** From a pure financial standpoint, **All Upfront** is almost always the best deal if you have the cash — the effective hourly rate is the lowest. However, for organizations with cash flow constraints or those following OpEx vs CapEx policies, **No Upfront** may be preferred even at a slight discount cost. Always align the payment option with your organization's financial strategy, not just the raw discount percentage.

---

## 9. RI Scope: Regional vs Zonal

> ⚠️ **Critical distinction:** Standard/Convertible is the **offering class**. Regional/Zonal is the **scope**. These are **two separate, independent dimensions**. Do not conflate them.

```
Reserved Instance
├── Offering Class
│   ├── Standard
│   └── Convertible
│
└── Scope
    ├── Regional
    └── Zonal
```

Any combination is valid:

```
✅ Standard RI   + Regional scope
✅ Standard RI   + Zonal scope
✅ Convertible RI + Regional scope
✅ Convertible RI + Zonal scope
```

---

## 10. Regional RI

A **Regional RI** applies at the **AWS Region level** (e.g., `us-east-1`).

- The discount applies to matching usage **anywhere in that Region**
- Flexible across all Availability Zones within the Region
- **Does NOT reserve capacity** in any specific AZ

```
Rule: Regional RI = flexible discount across AZs, but NO capacity guarantee
```

> 📌 **Exam tip:** Regional RIs are great for autoscaling workloads where instances may launch in different AZs. But if the question involves *guaranteed capacity*, Regional RI is not your answer.

---

## 11. Zonal RI

A **Zonal RI** is tied to a **specific Availability Zone** (e.g., `us-east-1a`).

- The discount applies only in that specific AZ
- **Reserves capacity** in that AZ — AWS guarantees EC2 capacity will be available

```
Rule: Zonal RI = discount + capacity reservation in one specific AZ
```

> 📌 **Exam tip:** The unique value of Zonal RIs is **capacity reservation**. If the exam question asks about ensuring EC2 is available during high-demand periods or in a specific AZ, Zonal RI (or On-Demand Capacity Reservations) is the answer.

---

## 12. Capacity Reservation Confusion

This is one of the most frequently missed concepts on AWS exams:

| Scope | Discount | Capacity Reserved? |
|---|---|---|
| Regional RI | ✅ Yes | ❌ No |
| Zonal RI | ✅ Yes | ✅ Yes (in that specific AZ) |

**When the question says:**
> *"The company needs to guarantee EC2 capacity is available in a specific Availability Zone."*

**The answer is:**
```
→ Zonal Reserved Instance
OR
→ On-Demand Capacity Reservation (if no long-term commitment desired)
```

> 📌 **Tutor Note:** On-Demand Capacity Reservations are worth knowing alongside Zonal RIs. They reserve capacity in a specific AZ without requiring a 1 or 3-year commitment — but you pay On-Demand rates with no discount unless you pair them with a Regional RI or Savings Plan. Zonal RI = commitment + discount + capacity. On-Demand Capacity Reservation = flexibility + capacity, no discount on its own.

---

## 13. RI Marketplace

The **RI Marketplace** lets AWS customers sell unused EC2 Reserved Instances they no longer need.

| RI Type | Can Be Sold? |
|---|---|
| Standard RI (eligible) | ✅ Yes |
| Convertible RI | ❌ No |

> ⚠️ **Common mistake to avoid:**
> ```
> ❌ Wrong:   "All RIs can be sold in the RI Marketplace."
> ✅ Correct: "Only eligible EC2 Standard RIs can be listed. Convertible RIs cannot."
> ```

> 📌 **Tutor Note:** The Marketplace exists specifically because Standard RIs are inflexible — if your workload changes and you're stuck with a Standard RI you can't exchange, selling it is your exit ramp. Convertible RIs don't need a Marketplace because you can exchange them directly with AWS. This is why the Marketplace applies only to Standard RIs.

---

## 14. Common Mistakes

### ❌ Mistake 1 — "Buying an RI launches an EC2 instance"

```
Wrong:   Purchasing an RI provisions an EC2 instance automatically.
Correct: An RI is a billing discount. You still launch instances yourself.
         AWS applies the discount to matching running instances.
```

### ❌ Mistake 2 — "All RIs reserve capacity"

```
Wrong:   All Reserved Instances guarantee EC2 capacity.
Correct: Only Zonal RIs reserve capacity in a specific AZ.
         Regional RIs provide discount only, with no capacity guarantee.
```

### ❌ Mistake 3 — "Standard = Regional, Convertible = Zonal"

```
Wrong:   Standard means Regional. Convertible means Zonal.
Correct: Offering class (Standard/Convertible) and scope (Regional/Zonal)
         are two independent dimensions. Any combination is valid.
```

### ❌ Mistake 4 — "Convertible RI has the biggest discount"

```
Wrong:   Convertible RI is better because it's flexible AND has the largest discount.
Correct: Standard RI has the higher discount (~72%).
         Convertible RI has a lower discount (~66%) in exchange for flexibility.
```

### ❌ Mistake 5 — "Standard RI can be exchanged"

```
Wrong:   Standard RI can be exchanged to a different instance family.
Correct: Standard RI can only be modified within limits.
         Only Convertible RI can be formally exchanged.
```

### ❌ Mistake 6 — "Convertible RI can be sold in the Marketplace"

```
Wrong:   Convertible RIs can be listed on the RI Marketplace.
Correct: Only eligible EC2 Standard RIs can be sold there.
         Convertible RIs cannot be sold in the Marketplace.
```

### ⚖️ Mistake 7 — "RI is always better than Savings Plans"

Not always. Here's a simple comparison:

| Feature | Reserved Instance | Savings Plan |
|---|---|---|
| Commitment basis | Specific EC2 attributes | Hourly spend amount |
| Flexibility | Lower | Higher (especially Compute SP) |
| Service coverage | EC2 only | EC2, Fargate, Lambda (Compute SP) |
| Capacity reservation | Zonal RI only | Not available |

> 📌 **Tutor Note:** For most modern AWS cost optimization scenarios, **Compute Savings Plans** offer more flexibility — they apply across instance families, Regions, and even non-EC2 services. Use RIs when you specifically need **AZ-level capacity reservation** (Zonal RI) or when you need to leverage the **RI Marketplace** for resale. Otherwise, Savings Plans are often the cleaner choice.

---

## 15. Quick Memory Rules

### Standard RI
```
✅ Highest discount
✅ Can be sold in RI Marketplace
✅ Modifiable within limits
❌ Cannot be exchanged
❌ Less flexible
→ Best for: Very stable, predictable, unchanging workloads
```

### Convertible RI
```
✅ Can be exchanged for equal/greater-value Convertible RI
✅ Modifiable within limits
✅ More flexible
❌ Lower discount than Standard RI
❌ Cannot be sold in RI Marketplace
→ Best for: Predictable workloads that may evolve over time
```

### Regional RI
```
✅ Discount applies across all AZs in a Region
❌ No capacity reservation
→ Best for: Flexible scaling across AZs
```

### Zonal RI
```
✅ Discount in a specific AZ
✅ Capacity reservation in that AZ
→ Best for: Guaranteed EC2 capacity in a specific AZ
```

### Term
```
1 year → Less discount, shorter commitment
3 years → More discount, longer commitment
```

### Payment
```
No Upfront     → Least upfront, least discount
Partial Upfront → Middle ground
All Upfront    → Most upfront, most discount
```

---

## 16. Final Summary & Comparison Table

### The Clean Mental Model

```
RI = discount model for predictable EC2 usage

Dimensions:
├── Offering Class → Standard | Convertible
├── Scope          → Regional | Zonal
├── Term           → 1 year   | 3 years
└── Payment        → No Upfront | Partial Upfront | All Upfront
```

### Standard vs Convertible — Full Comparison

| Feature | Standard RI | Convertible RI |
|---|---|---|
| 💰 Discount | Higher (~72%) | Lower (~66%) |
| 🔓 Flexibility | Lower | Higher |
| ♻️ Exchangeable | ❌ No | ✅ Yes (equal/greater value) |
| 🔧 Modifiable | ✅ Within limits | ✅ Within limits |
| 🏪 Marketplace Resale | ✅ Yes (if eligible) | ❌ No |
| 🎯 Best for | Very stable workloads | Predictable but changeable workloads |

### Final Memory Sentence

> **Standard RI is for maximum savings when you know exactly what you need.**  
> **Convertible RI is for long-term savings when you still need flexibility.**

---

*Study guide maintained for AWS exam preparation and cloud cost optimization reference.*