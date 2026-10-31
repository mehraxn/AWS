# ☁️ AWS Savings Plans — Complete Study Guide
### AWS Cloud Practitioner Exam Prep  Tutor Edition

---

## 📌 WHAT ARE AWS SAVINGS PLANS

AWS Savings Plans are a flexible pricing model that offers lower prices compared to On-Demand rates, in exchange for a commitment to a consistent amount of usage, measured in $hour, for a term of 1 or 3 years.

 Think of it like a gym membership you pay monthly (committed $hour) whether you use it or not — but because you committed, the rate per class (instance hour) is much cheaper.

### Key Characteristics
- Unit of commitment $hour (NOT GB, NOT number of instances)
- Term options 1 year or 3 years (longer = more savings)
- Payment options All Upfront, Partial Upfront, No Upfront
- Savings of up to 72% compared to On-Demand pricing (depending on plan type)
- Automatically applied to eligible usage — no need to manually assign

---

## 🧩 THE FOUR TYPES OF AWS SAVINGS PLANS

```
┌─────────────────────────────────────────────────────────────────────┐
│              AWS SAVINGS PLANS — 4 TYPES                            │
│                                                                     │
│  1. Compute Savings Plans      → Most flexible, EC2+Fargate+Lambda  │
│  2. EC2 Instance Savings Plans → Deepest discount, EC2 only         │
│  3. Database Savings Plans     → RDS & managed DB workloads         │
│  4. SageMaker AI Savings Plans → MLSageMaker workloads             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 1️⃣ COMPUTE SAVINGS PLANS

### 🔑 Keywords to Remember
Most flexible  Broadest coverage  EC2 + Fargate + Lambda

### What it covers
- Amazon EC2 (any instance family, size, region, OS, tenancy)
- AWS Fargate (serverless containers)
- AWS Lambda (serverless functions)

### How flexible is it
You can freely change
- ✅ Instance family (e.g., m5 → c5 → r6g)
- ✅ Instance size (e.g., large → xlarge → 2xlarge)
- ✅ AWS Region (e.g., us-east-1 → eu-west-1)
- ✅ Operating System (e.g., Linux → Windows)
- ✅ Tenancy (shared → dedicated)
- ✅ Switch between EC2, Fargate, and Lambda freely

### Typical savings Up to ~66% vs On-Demand

---

### 💡 REAL-WORLD EXAMPLES — Compute Savings Plans

Example 1 — Startup with mixed workloads
 A startup runs web servers on EC2 (m5.large), background jobs on Lambda, and a microservices API on Fargate.
 They commit to $10hour under a Compute Savings Plan.
 All three services count toward that $10hour commitment automatically.
 ✔ One plan covers everything. No need for separate plans per service.

Example 2 — Migration mid-year
 A company commits to a 1-year Compute Savings Plan while running m5 instances in us-east-1.
 Midway through the year, the team migrates to r6g (ARM) instances in eu-west-1.
 ✔ Savings Plan still applies — no changes needed, no penalties.

Example 3 — Lambda-heavy architecture
 A company runs a mostly serverless application (Lambda + API Gateway).
 They buy a Compute Savings Plan at $5hour.
 The discount automatically applies to Lambda invocation costs (within the committed amount).
 ✔ Fargate and EC2 can be added later and still benefit from the same plan.

Example 4 — Flexibility test
 Team A uses t3.micro in us-west-2. Team B uses c5.4xlarge in ap-southeast-1.
 Both are covered under a single Compute Savings Plan.
 ✔ Region, size, and family don't matter — it all counts.

---

## 2️⃣ EC2 INSTANCE SAVINGS PLANS

### 🔑 Keywords to Remember
Lowest price  EC2 only  Instance family + Region locked  Less flexible

### What it covers
- Amazon EC2 only (no Fargate, no Lambda)

### Commitment is to
- A specific instance family (e.g., m5)
- A specific AWS Region (e.g., us-east-1)

### Within that family + region, you CAN still change
- ✅ Instance size (e.g., m5.large → m5.4xlarge)
- ✅ Operating System (e.g., Linux → Windows)
- ✅ Tenancy (shared → dedicated)

### You CANNOT change
- ❌ Instance family (locked to e.g., m5)
- ❌ AWS Region (locked to e.g., us-east-1)

### Typical savings Up to ~72% vs On-Demand (deepest discount of all Savings Plans)

---

### 💡 REAL-WORLD EXAMPLES — EC2 Instance Savings Plans

Example 1 — Stable production workload
 A company has been running m5 instances in us-east-1 for 2 years and expects no migration.
 They commit to m5us-east-1 EC2 Instance Savings Plan for 3 years.
 ✔ They get the maximum possible discount because they don't need flexibility.

Example 2 — Resizing allowed
 A company buys an EC2 Instance Savings Plan for m5 family in eu-west-1.
 They start with m5.large (4 instances), then need to scale up to m5.2xlarge.
 ✔ Still covered — same family, same region, just different size.

Example 3 — OS switch mid-term
 A team runs m5 on Linux. They decide to move to Windows for licensing reasons.
 ✔ Still covered — OS is flexible within the locked familyregion.

Example 4 — What breaks the plan
 A company bought an EC2 Instance Savings Plan for m5us-east-1.
 They then migrate to c5 instances (different family) or move to us-west-2 (different region).
 ❌ The plan no longer applies. Those new instances run at On-Demand price.
 The committed $hour is still charged — you're paying for something you're not using efficiently.

---

## 3️⃣ DATABASE SAVINGS PLANS

### 🔑 Keywords to Remember
Database workloads  Managed databases  RDS and more

### What it covers
- Amazon RDS (Relational Database Service)
- Amazon Aurora
- Other AWS managed database services

### Use case
For workloads that run databases consistently and predictably — such as production RDS instances running MySQL, PostgreSQL, Oracle, SQL Server, etc.

### Key point
This plan is specifically carved out for database workloads — it does NOT cover EC2, Fargate, Lambda, or SageMaker.

---

### 💡 REAL-WORLD EXAMPLES — Database Savings Plans

Example 1 — Production RDS
 An e-commerce company runs a PostgreSQL RDS db.r5.large instance 247.
 They commit to a 1-year Database Savings Plan.
 ✔ They get a significant discount on that steady, predictable database usage.

Example 2 — Aurora cluster
 A SaaS company runs an Aurora MySQL cluster as their primary data store.
 ✔ Database Savings Plans apply to Aurora usage.

Example 3 — Not the right plan for this
 A company wants to save on their EC2 web servers AND their RDS database.
 They buy only a Database Savings Plan.
 ❌ The EC2 instances are NOT covered. They still pay On-Demand for those.
 ✔ Correct approach Buy a separate Compute Savings Plan for EC2 + Database Savings Plan for RDS.

Example 4 — Mixed DB engines
 A company runs MySQL RDS in us-east-1 and PostgreSQL RDS in eu-west-1.
 ✔ A Database Savings Plan covers both (check specific flexibility terms for engineregion per AWS docs).

---

## 4️⃣ SAGEMAKER AI SAVINGS PLANS

### 🔑 Keywords to Remember
Machine learning  SageMaker  ML instance usage  Any size, any region

### What it covers
Amazon SageMaker AI ML instance usage across
- 🧪 Notebooks (developmentexperimentation)
- ⚙️ Processing jobs
- 🏋️ Training jobs
- 🔮 Real-time inference endpoints
- 📦 Batch transform jobs

### Key flexibility
- ✅ Applies regardless of instance family, size, or Region
- ✅ Covers the broadest set of SageMaker ML workloads
- ✅ Very flexible within the SageMaker service

---

### 💡 REAL-WORLD EXAMPLES — SageMaker AI Savings Plans

Example 1 — ML team with steady training
 A data science team trains deep learning models daily on ml.p3.2xlarge instances.
 They commit to a SageMaker AI Savings Plan for 1 year.
 ✔ They get a discount on training costs without being locked to a region or instance size.

Example 2 — Inference endpoints
 A company serves a real-time fraud detection model via a SageMaker endpoint 247.
 ✔ SageMaker AI Savings Plans cover the inference endpoint hours.

Example 3 — End-to-end ML pipeline
 A team uses SageMaker for notebooks (exploring data), training (ml.m5.xlarge), and batch transform (ml.c5.2xlarge).
 ✔ All three stages are covered under one SageMaker AI Savings Plan.

Example 4 — Region change mid-term
 A company shifts their SageMaker training from us-east-1 to us-west-2 to be closer to their data lake.
 ✔ The SageMaker AI Savings Plan still applies — region doesn't matter.

---

## 📊 SIDE-BY-SIDE COMPARISON TABLE

```
┌──────────────────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│ Feature                  │ Compute SP   │ EC2 Instance │ Database SP  │ SageMaker SP │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Services Covered         │ EC2+Fargate  │ EC2 only     │ RDSAurora   │ SageMaker    │
│                          │ +Lambda      │              │ managed DBs  │ ML instances │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Flexibility              │ HIGHEST      │ LOWEST       │ MEDIUM       │ HIGH         │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Discount Level           │ Up to 66%    │ Up to 72%    │ Significant  │ Significant  │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Instance Family Lock     │ No           │ YES          │ No           │ No           │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Region Lock              │ No           │ YES          │ No           │ No           │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Size Flexible           │ Yes          │ Yes          │ Varies       │ Yes          │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ OS Flexible             │ Yes          │ Yes          │ NA          │ NA          │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Covers Lambda           │ YES          │ No           │ No           │ No           │
├──────────────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Covers Fargate          │ YES          │ No           │ No           │ No           │
└──────────────────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

---

## ⚔️ SAVINGS PLANS vs OTHER PRICING MODELS

It is critical to know how Savings Plans fit alongside the other AWS pricing options

```
┌──────────────────┬────────────────────────────────────────────────────────────┐
│ Pricing Model    │ Key Characteristics                                        │
├──────────────────┼────────────────────────────────────────────────────────────┤
│ On-Demand        │ Pay per use, no commitment, most expensive, most flexible  │
│ Reserved         │ 1 or 3 year commit to specific instance typeregion,       │
│ Instances (RI)   │ can be Standard (sell on marketplace) or Convertible       │
│ Savings Plans    │ $hour commitment, flexible usage, applies automatically   │
│ Spot Instances   │ Use spare AWS capacity, up to 90% off, can be interrupted  │
│ Dedicated Hosts  │ Physical server dedicated to you, for compliancelicensing │
└──────────────────┴────────────────────────────────────────────────────────────┘
```

### Important Distinctions
- Reserved Instances commit to a specific instance type + region + OS (rigid)
- Savings Plans commit to a $hour spend (flexible, auto-applied)
- Spot Instances are for interruption-tolerant workloads (batch, CICD, etc.)
- Savings Plans replace the need for most Reserved Instances (simpler + flexible)

---

## 🚨 EXAM TRAPS — WHAT THE AWS EXAM TRIES TO TRICK YOU ON

These are the most common trick questions and misconceptions tested on the AWS Cloud Practitioner exam

---

### 🪤 TRAP 1 — Most flexible does NOT mean EC2 only
 Q Which Savings Plan offers the most flexibility for compute workloads
 Wrong answer EC2 Instance Savings Plans (because EC2 is most commonly used)
 Correct answer ✅ Compute Savings Plans — covers EC2, Fargate, AND Lambda

The word flexible is the exam signal → Compute Savings Plans.

---

### 🪤 TRAP 2 — Deepest discount does NOT mean most flexible
 Q Which Savings Plan provides the highest savings percentage
 Wrong answer Compute Savings Plans (because it sounds most powerful)
 Correct answer ✅ EC2 Instance Savings Plans — up to 72% savings

More restrictions = deeper discount. More flexibility = slightly less discount.

---

### 🪤 TRAP 3 — Commitment is in $hour, NOT in hours or instances
 Q How do you commit to an AWS Savings Plan
 Wrong answer You commit to a number of instances
 Wrong answer You commit to a number of hours per month
 Correct answer ✅ You commit to a consistent dollar amount per hour ($hour)

This is a very common misconception. Savings Plans are always measured in $hour.

---

### 🪤 TRAP 4 — EC2 Instance Savings Plans do NOT cover Fargate or Lambda
 Q A company uses EC2 and Fargate. Which Savings Plan covers both
 Wrong answer EC2 Instance Savings Plans
 Correct answer ✅ Compute Savings Plans

If the question mentions Fargate or Lambda, the answer is always Compute Savings Plans.

---

### 🪤 TRAP 5 — Savings Plans are NOT the same as Reserved Instances
 Q A company wants to reduce costs and is comfortable committing for 1 year. 
 They want maximum flexibility to change instance types. What should they use
 Wrong answer Reserved Instances (Convertible)
 Correct answer ✅ Compute Savings Plans

Savings Plans auto-apply and don't require you to pre-specify instance type. Reserved Instances do.

---

### 🪤 TRAP 6 — SageMaker Savings Plans are NOT covered by Compute Savings Plans
 Q A company runs EC2 and SageMaker training. Will a Compute Savings Plan reduce SageMaker costs
 Wrong answer Yes — Compute Savings Plans cover all compute services
 Correct answer ❌ No — Compute Savings Plans cover EC2, Fargate, Lambda. SageMaker requires its own SageMaker AI Savings Plans.

---

### 🪤 TRAP 7 — Database Savings Plans ≠ Compute Savings Plans for databases
 Q A company wants to save money on their RDS database. They buy a Compute Savings Plan. Will this work
 Wrong answer Yes — RDS runs on compute infrastructure
 Correct answer ❌ No — RDS is NOT covered by Compute Savings Plans. Use Database Savings Plans for RDS.

---

### 🪤 TRAP 8 — You are charged for your committed $hour EVEN IF you don't use it
 If you commit to $5hour and only use $2hour of eligible compute, you are still charged $5hour.
 This is the commitment risk — unlike On-Demand where you only pay for what you use.

---

### 🪤 TRAP 9 — Term length Only 1 year OR 3 years (not monthly, not 2 years)
 Q What are the available term lengths for AWS Savings Plans
 Wrong answer 1 month, 6 months, 12 months, 24 months
 Correct answer ✅ 1 year or 3 years only

---

### 🪤 TRAP 10 — Savings Plans automatically apply; no manual instance assignment needed
 Unlike Reserved Instances (where you explicitly assign capacity), Savings Plans apply automatically to any eligible usage across your account (or AWS Organization).

---

## 🧠 MEMORY SHORTCUTS FOR THE EXAM

```
Compute SP   = I want to save on ANYTHING compute-related, be flexible
EC2 SP       = I want MAXIMUM savings on EC2 and I won't change familyregion
Database SP  = I want to save on my managed databases (RDS, Aurora)
SageMaker SP = I want to save on my MLAI workloads in SageMaker
```

```
FLEXIBILITY RANKING (most → least)
Compute SP  SageMaker SP  Database SP  EC2 Instance SP

SAVINGS RANKING (most → least)
EC2 Instance SP  Compute SP  (Database SP ≈ SageMaker SP)
```

---

## 📝 QUICK EXAM FLASHCARDS

 Question  Answer 
------
 Which SP covers Lambda  Compute Savings Plans 
 Which SP covers Fargate  Compute Savings Plans 
 Which SP is most flexible  Compute Savings Plans 
 Which SP gives deepest EC2 discount  EC2 Instance Savings Plans 
 Which SP is locked to family + region  EC2 Instance Savings Plans 
 Which SP covers RDS  Database Savings Plans 
 Which SP covers SageMaker training  SageMaker AI Savings Plans 
 How is commitment measured  $hour 
 What are the term lengths  1 year or 3 years 
 Does Compute SP cover RDS  NO 
 Does EC2 SP cover Fargate  NO 
 Does Compute SP cover SageMaker  NO 
 What happens if you don't use your commitment  You still pay the committed $hour 
 Do Savings Plans apply automatically  YES 

---

## 🧩 PRACTICE SCENARIO QUESTIONS

Scenario 1
 A company runs web servers on EC2 (m5 family, us-east-1) and serverless functions on AWS Lambda.
 They want maximum savings. What should they choose
 → Compute Savings Plans (covers both EC2 and Lambda)

Scenario 2
 A company has run m5 instances in us-east-1 for years and will not change the instance family or region.
 What Savings Plan gives them the best discount
 → EC2 Instance Savings Plans (locked but deepest discount)

Scenario 3
 A company needs to reduce costs on their Aurora MySQL cluster.
 → Database Savings Plans

Scenario 4
 A data science team runs continuous training jobs on SageMaker.
 → SageMaker AI Savings Plans

Scenario 5
 A company wants to save on EC2, RDS, AND SageMaker. What do they need
 → Three separate plans Compute SP + Database SP + SageMaker SP

Scenario 6
 A company is unsure about their future architecture — they might move from EC2 to Fargate containers.
 → Compute Savings Plans (flexibility to move between services)

Scenario 7
 The exam asks which purchasing option gives the lowest price for EC2 in a committed scenario.
 → EC2 Instance Savings Plans (up to 72% — but check if they also mention Spot Instances, 
    which can be even cheaper but with interruption risk)

---

## 📚 RELATED CONCEPTS TO KNOW

### AWS Cost Management Tools (often paired with Savings Plans in exam questions)
- AWS Cost Explorer — Visualize usage and costs; has a Savings Plans recommendation engine
- AWS Budgets — Set alerts when costs exceed thresholds
- AWS Pricing Calculator — Estimate costs before committing
- AWS Trusted Advisor — Recommends cost optimization opportunities including Savings Plans
- AWS Cost and Usage Report (CUR) — Detailed billing data

### How to Purchase Savings Plans
1. Go to AWS Cost Explorer → Savings Plans
2. AWS analyzes your historical usage
3. It recommends the right plan and commitment amount
4. You select the plan type, term (1 or 3 year), and payment option

### Payment Options (affects upfront cost vs total savings)
 Option  How it works  Savings 
---------
 All Upfront  Pay full term cost upfront  Maximum savings 
 Partial Upfront  Pay part upfront + monthly  Medium savings 
 No Upfront  Pay monthly only  Minimum savings (but still vs On-Demand) 

---

## ✅ FINAL SUMMARY CHEAT SHEET

```
╔══════════════════════════════════════════════════════════════╗
║           AWS SAVINGS PLANS — ONE-PAGE CHEAT SHEET           ║
╠══════════════════════════════════════════════════════════════╣
║ WHAT  Commit to $hour usage for 1 or 3 years → save $$     ║
╠══════════════════════════════════════════════════════════════╣
║ TYPE 1 Compute SP                                           ║
║   → EC2 + Fargate + Lambda  Most flexible  ~66% savings    ║
║   → Change anything family, size, region, OS, tenancy       ║
╠══════════════════════════════════════════════════════════════╣
║ TYPE 2 EC2 Instance SP                                      ║
║   → EC2 ONLY  Locked family + region  ~72% savings        ║
║   → Can change size, OS, tenancy (within locked family)     ║
╠══════════════════════════════════════════════════════════════╣
║ TYPE 3 Database SP                                          ║
║   → RDS + Aurora + managed DBs  NOT EC2LambdaFargate      ║
╠══════════════════════════════════════════════════════════════╣
║ TYPE 4 SageMaker AI SP                                      ║
║   → SageMaker ML instances  Any sizeregion  Notebooks,    ║
║     training, inference, batch transform                     ║
╠══════════════════════════════════════════════════════════════╣
║ KEY EXAM SIGNALS                                            ║
║   flexible or FargateLambda → Compute SP                ║
║   deepest discount + EC2 only  → EC2 Instance SP           ║
║   database or RDS            → Database SP               ║
║   SageMaker or ML training   → SageMaker AI SP           ║
╚══════════════════════════════════════════════════════════════╝
```

---

Last updated for AWS Cloud Practitioner (CLF-C02) exam domain coverage.
Always verify the latest AWS documentation at httpsaws.amazon.comsavingsplans