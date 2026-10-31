# 🖥️ Amazon EC2 Purchasing & Billing Options
### Complete AWS Cloud Practitioner Study Guide

 How to use this guide Read each section top-to-bottom. Every option includes a plain-English definition, a real-world analogy, concrete examples, cost comparison, and a dedicated ⚠️ EXAM TRAP block. A master cheat-sheet and a decision flowchart are at the bottom.

---

## 📋 Table of Contents

1. [On-Demand Instances](#1-on-demand-instances)
2. [Savings Plans](#2-savings-plans)
3. [Reserved Instances (RI)](#3-reserved-instances-ri)
4. [Spot Instances](#4-spot-instances)
5. [Dedicated Hosts](#5-dedicated-hosts)
6. [Dedicated Instances](#6-dedicated-instances)
7. [Capacity Reservations](#7-capacity-reservations)
8. [Capacity Blocks (for MLGPU)](#8-capacity-blocks-for-mlgpu)
9. [Master Comparison Table](#-master-comparison-table)
10. [Decision Flowchart (Text Version)](#-decision-flowchart-text-version)
11. [Common Exam Scenarios & Answers](#-common-exam-scenarios--answers)
12. [What the Examiner Tests — Top Traps Summary](#-what-the-examiner-tests--top-traps-summary)

---

## 1. On-Demand Instances

### 📖 Definition
You pay for compute capacity by the second (Linux) or by the hour (Windows) with no upfront payment and no long-term commitment. You start and stop whenever you want.

### 🏠 Real-World Analogy
Like renting a hotel room — you show up, pay per night, and check out whenever you want. No lease, no deposit.

### ✅ When to Use
- Short-term, spiky, or unpredictable workloads
- Applications being developed or tested for the first time
- You cannot predict how much compute you need
- You need to run a workload for less than 1 year

### 💰 Pricing
- No upfront cost
- No commitment
- Highest per-hour price among all options
- Billed per second (minimum 60 seconds) for most Linux instances

### 📌 Concrete Examples

Example 1 — Startup Dev Environment
A startup is building a new web app. They spin up 3 On-Demand t3.medium instances for 2 weeks of development. When done, they terminate them. Total cost = only the hours actually used. No wasted spend.

Example 2 — Black Friday Traffic Spike
An e-commerce site expects a massive traffic spike on Black Friday (totally unpredictable scale). They launch extra On-Demand instances at midnight, handle the load, and terminate them 48 hours later.

Example 3 — Batch Job with Unknown Duration
A data science team needs to run a one-time data migration that might take 4 hours or 40 hours — they don't know. On-Demand is the right choice since they cannot commit to a duration.

### ⚠️ EXAM TRAPS

 Trap 1 The exam says a company has unpredictable workloads and wants the lowest cost. The answer is NOT On-Demand — it's Spot Instances if interruption is tolerable. On-Demand is lowest cost only when you cannot tolerate interruption AND cannot commit.

 Trap 2 On-Demand does NOT mean real-time or immediate provisioning is guaranteed in all cases. During extreme capacity constraints in a region, on-demand capacity can be limited (though this is rare).

 Trap 3 The question asks about no long-term commitment and no upfront payment — this describes On-Demand, NOT Savings Plans. Both have no commitment to instance type, but Savings Plans DO require a 1- or 3-year spend commitment.

---

## 2. Savings Plans

### 📖 Definition
You commit to a consistent amount of compute usage (measured in $hour) for 1 or 3 years. In return, AWS gives you discounts of up to 66% off On-Demand prices. You are NOT committing to a specific instance type, region, or OS — just a dollar spend level.

### 🏠 Real-World Analogy
Like a gym membership where you commit to paying $50month for a year. You can use any machine, any class, any time — you just have to keep paying $50month regardless.

### 🗂️ Types of Savings Plans

 Type  Flexibility  Max Discount 
---------
 Compute Savings Plans  Any instance family, size, region, OS, tenancy, and even AWS Lambda & Fargate  Up to 66% 
 EC2 Instance Savings Plans  Locked to one instance family in one region, but flexible on size, OS, tenancy  Up to 72% 
 SageMaker Savings Plans  For SageMaker ML workloads specifically  Up to 64% 

 Cloud Practitioner Focus You mainly need to know that Savings Plans exist for EC2 + Fargate + Lambda and that they give discounts in exchange for a usage commitment.

### ✅ When to Use
- You have steady-state usage but want flexibility to change instance types
- You use AWS Lambda or Fargate heavily (Reserved Instances don't cover these!)
- You want simplicity — one plan covers multiple services

### 💰 Pricing
- Commit to a $hour spend (e.g., $10hour of compute)
- Usage up to that amount is billed at the discounted rate
- Usage above your committed amount is billed at On-Demand rates
- Payment options All Upfront, Partial Upfront, No Upfront

### 📌 Concrete Examples

Example 1 — Flexible Growing Startup
A company currently runs m5.xlarge instances but plans to upgrade to m5.2xlarge in 6 months and possibly switch to a different family next year. A Compute Savings Plan lets them commit to $5hour of compute and get discounts regardless of which instance they're on.

Example 2 — Lambda-Heavy Architecture
A company runs most of its backend as AWS Lambda functions with consistent daily invocations. Reserved Instances don't cover Lambda — Savings Plans do.

Example 3 — EC2 Instance Savings Plan
A company is 100% sure they'll run m5 instances in us-east-1 for 3 years but will vary the size. An EC2 Instance Savings Plan for the m5 family in us-east-1 gives maximum discount.

### ⚠️ EXAM TRAPS

 Trap 1 Savings Plans sounds like it's about saving money flexibly — but it DOES require a 1- or 3-year commitment. It is NOT a pay-as-you-go option.

 Trap 2 Many students think Reserved Instances and Savings Plans are the same. Key difference Reserved Instances are for EC2 only. Savings Plans also cover Lambda and Fargate.

 Trap 3 Savings Plans are listed under EC2 billing options in the AWS console, which confuses people into thinking they ONLY apply to EC2. They don't — Compute Savings Plans apply broadly.

 Trap 4 If the question says a company wants to commit to a dollar amount per hour of compute — the answer is Savings Plans, not Reserved Instances.

---

## 3. Reserved Instances (RI)

### 📖 Definition
You commit to a specific EC2 instance configuration (instance type, region, tenancy, OS) for 1 or 3 years in exchange for significant discounts (up to 72% off On-Demand). This is a billing discount — NOT a physical reservation of hardware.

### 🏠 Real-World Analogy
Like signing a 1- or 2-year apartment lease. You commit to paying a fixed amount every month, and your monthly rate is much lower than a hotel (On-Demand). You're locked in, but you save a lot.

### 🗂️ Types of Reserved Instances

 Type  Flexibility  Discount 
---------
 Standard RI  Cannot change instance family or region. Can change size, OS, AZ within family  Highest (~72%) 
 Convertible RI  Can exchange for a different instance family, OS, or tenancy  Lower (~54%) 
 Scheduled RI  Reserve for a specific time window (e.g., every day 9am–5pm)  Deprecated — not tested heavily 

### 🗂️ Scope Options
- Regional RI Discount applies to any instance in any AZ in that region (more flexible)
- Zonal RI Discount applies to a specific AZ AND reserves capacity in that AZ

### ✅ When to Use
- Steady-state, predictable workloads (e.g., a database that runs 247365)
- You know exactly what instance type, OS, and region you'll use for 1–3 years
- You want the highest possible discount on EC2

### 💰 Pricing
- Payment options
  - All Upfront — highest discount
  - Partial Upfront — medium discount
  - No Upfront — lowest discount (but still beats On-Demand)
- Term 1-year or 3-year (3-year = bigger discount)
- You PAY for the RI whether or not you use it

### 📌 Concrete Examples

Example 1 — Production Database Server
A company runs a MySQL RDS instance on r5.2xlarge 247 in us-east-1. It will run for at least 3 years. They buy a Standard RI for 3 years, All Upfront → ~72% savings vs On-Demand.

Example 2 — Growing Company Using Convertible RI
A company is growing and knows they'll need more compute in 18 months but isn't sure which instance family. They buy a Convertible RI so they can exchange it later for a larger or different instance type without losing the discount entirely.

Example 3 — RI Marketplace
A company bought a 3-year Standard RI but closes its product after 1 year. They sell the remaining 2 years on the Reserved Instance Marketplace to recoup some cost.

Example 4 — Zonal RI for Capacity Guarantee
A company needs a guaranteed m5.xlarge in us-east-1a (specific AZ) during peak hours. They buy a Zonal RI — this both discounts AND reserves capacity.

### ⚠️ EXAM TRAPS

 Trap 1 (MOST COMMON) Reserved Instances give you a reserveddedicated physical server. FALSE. A Reserved Instance is purely a billing discount. The actual EC2 instance runs on shared hardware (unless you also choose Dedicated Tenancy).

 Trap 2 You bought a Reserved Instance but decided to use a larger instance — will the RI discount still apply For Standard RI Only if it's the same family (e.g., m5.large → m5.xlarge, instance size flexibility). For Convertible RI Yes, after an exchange.

 Trap 3 You still pay for unused RIs. If you buy an RI and never launch an instance, you still owe AWS for the committed term.

 Trap 4 Regional RIs provide no capacity reservation guarantee. Zonal RIs DO guarantee capacity in a specific AZ.

 Trap 5 The exam might describe a workload that runs 247 for 3 years — the answer is Reserved Instances (or Savings Plans), NOT On-Demand.

---

## 4. Spot Instances

### 📖 Definition
You use spare AWS EC2 capacity at discounts of up to 90% off On-Demand prices. The catch AWS can interrupt (terminatestophibernate) your instance with only a 2-minute warning if it needs that capacity back.

### 🏠 Real-World Analogy
Like standby airline seats — you get a huge discount, but the airline can bump you if a full-paying passenger shows up. You need flexibility about when exactly you travel.

### ✅ When to Use
- Fault-tolerant workloads that can handle interruptions
- Flexible startend times — the job can be paused and resumed
- Batch processing jobs (genomics, financial modeling, big data)
- CICD pipelines that can retry failed jobs
- Stateless web servers behind a load balancer (losing one instance is okay)
- Machine learning training jobs (can checkpoint and resume)

### ❌ When NOT to Use
- Databases (data loss risk)
- Critical stateful applications
- Anything requiring guaranteed availability
- Production workloads that cannot tolerate any interruption

### 💰 Pricing
- Up to 90% cheaper than On-Demand
- Price fluctuates based on supply and demand in each AZ
- You set a maximum price (Spot Price); if market price exceeds it, instance is reclaimed
- If AWS interrupts the instance, you are NOT charged for the partial hour

### 📌 Concrete Examples

Example 1 — Genomics Research Batch Job
A pharmaceutical company needs to process 10TB of genomic data. The job can take 10 hours, and it's fine if it takes 15 due to interruptions. They run 100 Spot Instances, save 80% on compute costs vs On-Demand.

Example 2 — Video Rendering Farm
A media company renders 3D video frames. Each frame is independent. If a Spot Instance is interrupted, the in-progress frame is requeued and another instance picks it up.

Example 3 — CICD Build Servers
A software company uses Spot Instances for their Jenkins build agents. If a build is interrupted, it simply reruns — the cost savings over a month are enormous.

Example 4 — Wrong Use Case
A company tries to run its production PostgreSQL database on a Spot Instance to save costs. Bad idea — the database is interrupted, causing data corruption and downtime. ❌

### 🔑 Key Concepts

Spot Fleet A collection of Spot Instances (and optionally On-Demand) that tries to meet a target capacity and cost. Automatically replaces interrupted instances.

Spot Instance Interruption AWS gives a 2-minute warning via instance metadata and CloudWatch Events before termination.

Spot Blocks (deprecated) Used to reserve Spot capacity for 1–6 hours without interruption. Now deprecated by AWS.

### ⚠️ EXAM TRAPS

 Trap 1 (MOST COMMON) The exam says lowest cost — the answer IS Spot Instances, but ONLY if the question also says the workload can tolerate interruption or is fault-tolerant.

 Trap 2 Spot Instances give 2-hour warning before termination. FALSE — it's 2 MINUTES.

 Trap 3 A company wants to run a production database at the lowest cost. The answer is NOT Spot Instances — databases cannot tolerate interruption. Reserved Instances would be correct here.

 Trap 4 If AWS interrupts a Spot Instance, you are not charged for the partial hour of use. If YOU terminate it, you ARE charged for the partial hour.

 Trap 5 Spot Instances cannot be stopped and started in the traditional sense — when AWS reclaims them, they are terminated (unless you configured hibernate behavior).

---

## 5. Dedicated Hosts

### 📖 Definition
A physical server fully dedicated to you. You get visibility into the underlying hardware (sockets, cores, host IDs) and control over instance placement. AWS does not place other customers' instances on that server.

### 🏠 Real-World Analogy
Like buying (or long-term renting) an entire apartment building. The whole building is yours — no other tenants. You manage which unit each person goes into.

### ✅ When to Use
- BYOL (Bring Your Own License) — software licenses tied to physical cores, sockets, or VMs (e.g., Windows Server, SQL Server, Oracle Database, RHEL, SUSE)
- Regulatory compliance requiring physical server isolation
- You need to know the Host ID for licensing audits
- Compliance needs that mandate no hardware sharing with other AWS accounts

### 💰 Pricing
- Billed per host, per hour (not per instance)
- More expensive than Dedicated Instances
- Available as On-Demand or Reserved (1- or 3-year commitment for discount)

### 📌 Concrete Examples

Example 1 — Oracle Database Licensing
Oracle licenses are often tied to the number of physical cores. A company running Oracle DB on AWS buys a Dedicated Host so they can count exact cores, satisfy Oracle's audit requirements, and avoid paying for cores used by other customers.

Example 2 — SQL Server Per-Core Licensing
A company has existing SQL Server per-core licenses. They use Dedicated Hosts to control exactly which physical cores their SQL Server VMs use, staying compliant with Microsoft's licensing terms.

Example 3 — Compliance Requirement
A government agency requires that no other organization shares any physical hardware with their workloads. Dedicated Hosts provide this guarantee with full audit visibility.

### ⚠️ EXAM TRAPS

 Trap 1 (MOST COMMON) A company needs dedicated hardware for licensing compliance — answer is Dedicated Hosts (NOT Dedicated Instances). Dedicated Hosts give you hardware visibility and control. Dedicated Instances just give you isolation.

 Trap 2 Dedicated Hosts are billed per host — not per instance. You can run many instances on one host and the host cost stays the same.

 Trap 3 The keyword BYOL or software license tied to physical coressockets → always Dedicated Hosts.

 Trap 4 Don't confuse Dedicated Host with Dedicated Instance. A Dedicated HOST gives you the full physical server. A Dedicated INSTANCE just means your VM doesn't share hardware with other AWS customers but you don't control or see the host.

---

## 6. Dedicated Instances

### 📖 Definition
EC2 instances that run on hardware dedicated to a single AWS account. Other instances from your account may share the host, but instances from other AWS accounts will never share it. You do NOT get visibility into the underlying physical host.

### 🏠 Real-World Analogy
Like renting a floor in an apartment building — only people from your company are on that floor. You don't control which room each person is in, and you don't own the building.

### ✅ When to Use
- Compliance requirements mandate no sharing of physical hardware with other organizations
- You do NOT need licensing tied to specific coressockets (that's Dedicated Hosts)
- You want hardware isolation without the complexitycost of a full Dedicated Host

### 💰 Pricing
- Per-instance billing (like On-DemandReserved but with an isolation fee)
- Dedicated Instance fee $2regionhour (flat fee per region, regardless of number of instances)
- Per-instance charge on top of that
- Cheaper than Dedicated Hosts

### 📌 Concrete Examples

Example 1 — Compliance Without BYOL
A healthcare company needs physical isolation from other AWS customers for HIPAA reasons, but they don't have any per-core software licenses. Dedicated Instances solve this without paying for an entire host.

Example 2 — Multi-account AWS Organization
A company wants to ensure their sensitive workloads never share hardware with any other AWS account. They use Dedicated Instances in a specific VPC.

### ⚠️ EXAM TRAPS

 Trap 1 Dedicated Instances ≠ Dedicated Hosts. Key differences
 - Dedicated Instances isolated per AWS ACCOUNT, no hardware visibility
 - Dedicated Hosts isolated per CUSTOMER, full hardware visibility, BYOL support

 Trap 2 Even within the same AWS account, your Dedicated Instances may share the underlying host with your own other Dedicated Instances. Non-dedicated instances from the same account do NOT share the host.

 Trap 3 Dedicated Instances do not help with per-core or per-socket software licensing. They do not provide socketcore visibility. Use Dedicated Hosts for that.

---

## 7. Capacity Reservations

### 📖 Definition
Reserve EC2 compute capacity in a specific Availability Zone for any duration. This guarantees that capacity is available when you need it — even during AWS regional events. This is about availability assurance, not discounting.

### 🏠 Real-World Analogy
Like reserving a table at a restaurant — you're guaranteed a table when you arrive, but you still pay full menu price. The reservation doesn't give you a discount.

### ✅ When to Use
- You need guaranteed capacity for a critical event (product launch, major event)
- Disaster recovery scenarios requiring guaranteed failover capacity
- Business-critical applications that cannot risk InsufficientCapacityError
- Compliance requiring guaranteed availability in a specific AZ

### 💰 Pricing
- Billed at On-Demand rates whether or not you use the reserved capacity
- No discount — you pay On-Demand pricing
- You can combine with Reserved Instances or Savings Plans to also get a discount
- No required term length (unlike RIs)

### 📌 Concrete Examples

Example 1 — Major Product Launch
A company is launching a new product on a specific date and expects a traffic surge. They create a Capacity Reservation for 50 c5.xlarge instances in us-east-1a so they're guaranteed to have capacity available on launch day, even if AWS is under regional stress.

Example 2 — Disaster Recovery
A bank has a DR plan that requires spinning up 100 EC2 instances in eu-west-1b within minutes of a disaster. They maintain a Capacity Reservation so capacity is always available, even if they never use it day-to-day.

Example 3 — Combining with RI for Discount + Guarantee
A company buys a Zonal Reserved Instance (which also reserves capacity) to get both the billing discount AND the capacity guarantee in a specific AZ.

### ⚠️ EXAM TRAPS

 Trap 1 (MOST COMMON) Capacity Reservations give you a discount. FALSE. They guarantee capacity at On-Demand prices. Zero discount.

 Trap 2 If the question asks about ensuring capacity is available or avoiding InsufficientCapacityError → Capacity Reservations (or Zonal RIs).

 Trap 3 Capacity Reservations do not expire (unlike Reserved Instances). You pay On-Demand rates indefinitely until you cancel them.

 Trap 4 The exam may describe a company wants a discount AND guaranteed capacity — the answer is a Zonal Reserved Instance (provides both), or Capacity Reservation + Savings Plan combo.

---

## 8. Capacity Blocks (for MLGPU)

### 📖 Definition
Reserve GPU instances (specifically for ML workloads) for a specific future time window (e.g., I need 8x p4d.24xlarge instances from March 15–22). You know exactly when you'll get your capacity and for how long.

### 🏠 Real-World Analogy
Like booking a block of hotel conference rooms for a specific week-long conference — you pay in advance, you know exactly when you have it, and it's released afterward.

### ✅ When to Use
- Large-scale ML model training that requires specific GPU instances
- You need a predictable, scheduled block of GPU capacity
- Training runs that cannot be interrupted and need guaranteed hardware
- Research teams running periodic large training jobs

### 💰 Pricing
- Billed at a fixed price for the reserved block
- Listed in the EC2 Billing and Purchasing Options section
- Higher than On-Demand in some cases — you're paying for guaranteed future GPU capacity

### 📌 Concrete Examples

Example 1 — LLM Training
An AI startup needs to train a large language model. They need 32 p4d.24xlarge GPU instances for 7 consecutive days. They book a Capacity Block 2 weeks in advance to guarantee those GPUs are available.

Example 2 — Research Experiment
A university ML lab runs quarterly large training experiments. They book Capacity Blocks for their scheduled experiment windows rather than hoping GPU capacity is available on demand.

### ⚠️ EXAM TRAPS

 Trap 1 Capacity Blocks are specific to ML GPU workloads — don't confuse them with general Capacity Reservations.

 Trap 2 For the Cloud Practitioner exam, Capacity Blocks are the newest and least heavily tested of the eight options. Know what they are and when they apply (MLGPU + future scheduling), but don't over-study this one.

 Trap 3 If the question mentions GPUs, large ML training, or needing to book future compute capacity for AI workloads → think Capacity Blocks.

---

## 📊 Master Comparison Table

 Option  Commitment  Discount vs On-Demand  Interruption Risk  Best For  Hardware Isolation 
------------------
 On-Demand  None  0% (baseline)  None  Short-term, unpredictable  Shared 
 Savings Plans  1 or 3 years ($hr)  Up to 66%  None  Flexible steady-state, Lambda  Shared 
 Reserved Instances  1 or 3 years (instance config)  Up to 72%  None  Predictable steady-state EC2  Shared (unless Dedicated tenancy) 
 Spot Instances  None  Up to 90%  YES (2-min warning)  Fault-tolerant, batch, flexible  Shared 
 Dedicated Hosts  Optional (On-Demand or Reserved)  Up to 70% (if Reserved)  None  BYOL, physical compliance  Full physical server 
 Dedicated Instances  None required  ~0% (isolation fee)  None  Account-level physical isolation  Per-account isolation 
 Capacity Reservations  None (but pay always)  0%  None  Guaranteed capacity in AZ  Shared 
 Capacity Blocks  Fixed future window  Varies  None (guaranteed block)  Scheduled GPUML training  Shared 

---

## 🔀 Decision Flowchart (Text Version)

```
START What kind of workload is it
│
├─ Is it a GPUML large training job with a scheduled window
│   └─ YES → CAPACITY BLOCKS
│
├─ Does it need guaranteed hardware for BYOL software licensing
│   └─ YES → DEDICATED HOSTS
│
├─ Does it need physical isolation (no other AWS accounts on same hardware)
│   ├─ Need coresocket visibility for licensing → DEDICATED HOSTS
│   └─ Just need isolation, no visibility needed → DEDICATED INSTANCES
│
├─ Must capacity be GUARANTEED in a specific AZ
│   └─ YES → CAPACITY RESERVATION (+ RI or Savings Plan for discount)
│
├─ Can the workload tolerate interruption (fault-tolerant, batch)
│   └─ YES → SPOT INSTANCES (cheapest option — up to 90% off)
│
├─ Is the workload steady-state and predictable for 1–3 years
│   ├─ Uses LambdaFargate OR wants flexibility across instance types
│   │   └─ → SAVINGS PLANS
│   └─ Stays on same EC2 instance typeregion long-term
│       └─ → RESERVED INSTANCES (highest EC2 discount)
│
└─ None of the above (short-term, unpredictable, or testing)
    └─ → ON-DEMAND INSTANCES
```

---

## 🎯 Common Exam Scenarios & Answers

 Scenario  Correct Answer  Why 
---------
 Lowest cost, fault-tolerant batch job  Spot Instances  90% discount, workload can handle interruption 
 247 production database for 3 years  Reserved Instances  Predictable, steady-state, maximum EC2 discount 
 Need flexibility to change instance types over 3 years  Convertible Reserved Instances or Savings Plans  Both allow changes; Savings Plans more flexible 
 Run Oracle with per-core licensing  Dedicated Hosts  Need physical coresocket visibility for Oracle audit 
 No hardware sharing with other companies, no licensing needs  Dedicated Instances  Account-level isolation without full host 
 Guarantee capacity available for product launch  Capacity Reservation  Ensures no InsufficientCapacityError on launch day 
 Lambda + EC2 mixed workload, want one discount plan  Compute Savings Plans  Only savings plan that covers Lambda + EC2 
 Short-term workload, no idea how long it will run  On-Demand  No commitment, pay only for what you use 
 Schedule GPU instances for ML training 2 weeks from now  Capacity Blocks  Future scheduled GPUML capacity 
 Discount AND guaranteed capacity in specific AZ  Zonal Reserved Instance  Provides both discount + capacity guarantee 

---

## 🪤 What the Examiner Tests — Top Traps Summary

### Trap Category 1 Reserved Instances ≠ Physical Reservation
 RI = billing discount only. Not a physical dedicated server. Hardware is still shared unless you specify Dedicated tenancy separately.

### Trap Category 2 Dedicated Hosts vs Dedicated Instances
   Dedicated Hosts  Dedicated Instances 
 ---------
  Physical server control  ✅ Full  ❌ No 
  See host ID  core count  ✅ Yes  ❌ No 
  BYOL licensing compliance  ✅ Yes  ❌ No 
  Billing  Per host  Per instance 
  Other accounts on hardware  ❌ Never  ❌ Never 
  Your own account's other instances  You control  May share the host 

### Trap Category 3 Savings Plans vs Reserved Instances
   Savings Plans  Reserved Instances 
 ---------
  Covers Lambda  ✅ Compute SP only  ❌ No 
  Covers Fargate  ✅ Compute SP only  ❌ No 
  Commitment type  $hour spend  Specific instance config 
  Maximum EC2 discount  72% (EC2 SP)  72% (Standard RI) 
  Flexibility  High  Low (Standard)  Medium (Convertible) 

### Trap Category 4 Capacity Reservations Have No Discount
 Capacity Reservations = guaranteed availability at On-Demand PRICES. Zero discount. You can combine them with an RI or Savings Plan for a discount, but the reservation itself doesn't discount.

### Trap Category 5 Spot Interruption Details
 - Warning 2 MINUTES (not 2 hours, not 5 minutes)
 - If AWS interrupts you are NOT charged for the partial hour
 - If YOU terminate you ARE charged for the partial hour
 - Keyword triggers fault-tolerant, batch processing, flexible startend times, can be interrupted

### Trap Category 6 Lowest Cost Is Context-Dependent
 - Lowest cost + cannot be interrupted → Reserved Instances (for long-term) or On-Demand (short-term)
 - Lowest cost + CAN be interrupted → Spot Instances (always)
 - Lowest cost + uses LambdaFargate → Compute Savings Plans

### Trap Category 7 Zonal vs Regional Reserved Instances
 - Zonal RI Discount in specific AZ + capacity is reserved in that AZ
 - Regional RI Discount anywhere in the region (more flexible) + NO capacity guarantee

---

## 📚 Quick-Review Mnemonics

OSRSDCC B — On-demand, Savings, Reserved, Spot, Dedicated-host, Dedicated-instance, Capacity-reservation, Capacity-Blocks

SPOT = Short-term + Pause-able + Optional-availability + Tolerates-interruption

Dedicated HOST = Hardware visiblity + BYOL + Own physical server + Licensing audits

Capacity Reservation = Capacity ONLY, no discount, no commitment term

Savings Plans = Spend commitment, Flexible, covers Serverless (LambdaFargate) too

---

## 🔗 Official AWS References

- EC2 Pricing Overview httpsaws.amazon.comec2pricing
- Savings Plans httpsaws.amazon.comsavingsplans
- Reserved Instances httpsaws.amazon.comec2pricingreserved-instances
- Spot Instances httpsaws.amazon.comec2spot
- Dedicated Hosts httpsaws.amazon.comec2dedicated-hosts
- Capacity Reservations httpsdocs.aws.amazon.comAWSEC2latestUserGuideec2-capacity-reservations.html
- Capacity Blocks for ML httpsdocs.aws.amazon.comAWSEC2latestUserGuideec2-capacity-blocks.html

---

Last reviewed against AWS Cloud Practitioner CLF-C02 exam domains. All 8 EC2 purchasing options from the official AWS EC2 Billing and Purchasing Options page are covered.