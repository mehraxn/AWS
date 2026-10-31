# AWS Recommendation Services — Complete Study Guide
> **AWS Cloud Practitioner** | Tutor-Grade Reference

---

## 📌 Table of Contents

1. [What Is a Recommendation Service?](#-what-is-a-recommendation-service)
2. [Quick Verification Pass](#-quick-verification-pass)
3. [Core Recommendation Services](#-part-1--core-recommendation-services)
   - [AWS Trusted Advisor](#1️⃣-aws-trusted-advisor)
   - [AWS Compute Optimizer](#2️⃣-aws-compute-optimizer)
   - [AWS Well-Architected Tool](#3️⃣-aws-well-architected-tool)
   - [AWS Cost Optimization Hub](#4️⃣-aws-cost-optimization-hub)
   - [AWS Cost Explorer](#5️⃣-aws-cost-explorer)
4. [Specialized Recommendation Services](#-part-2--specialized-recommendation-services)
   - [AWS Security Hub (CSPM)](#6️⃣-aws-security-hub--cspm)
   - [IAM Access Analyzer](#7️⃣-iam-access-analyzer)
   - [Amazon DevOps Guru](#8️⃣-amazon-devops-guru)
   - [AWS Resilience Hub](#9️⃣-aws-resilience-hub)
5. [Services That Are NOT Recommendation Services](#-part-3--services-that-are-not-recommendation-services)
6. [Exam Traps](#-part-4--exam-traps)
7. [Master Cheat Sheet](#-part-5--master-cheat-sheet)
8. [Additional Facts](#-part-6--additional-facts)

---

## ⚠️ What Is a Recommendation Service?

A true AWS Recommendation Service must satisfy **all three** of the following:

| # | Requirement |
|---|-------------|
| ✅ | **Scans** your account/resources automatically (no manual rules needed) |
| ✅ | **Analyzes** something — cost, performance, security, resilience, etc. |
| ✅ | **Returns actionable recommendations** — "you should do X" |

> ❌ If a service only monitors, alerts, or requires you to write your own rules → it is **NOT** a recommendation service.

---

## 🔍 Quick Verification Pass

| Service | Scans Automatically | Gives Recommendations | Verdict |
|---------|--------------------|-----------------------|---------|
| AWS Trusted Advisor | ✅ Yes | ✅ Yes | ✅ **CONFIRMED** |
| AWS Compute Optimizer | ✅ Yes | ✅ Yes | ✅ **CONFIRMED** |
| AWS Well-Architected Tool | ⚠️ You answer questions | ✅ Yes (based on answers) | ✅ **CONFIRMED** (semi-automated) |
| AWS Cost Optimization Hub | ✅ Yes (aggregates) | ✅ Yes | ✅ **CONFIRMED** |
| AWS Cost Explorer | ✅ Yes (for RI/Savings Plans) | ✅ Partially | ✅ **CONFIRMED** (partial) |
| AWS Security Hub CSPM | ✅ Yes | ✅ Yes (remediation findings) | ✅ **CONFIRMED** |
| IAM Access Analyzer | ✅ Yes | ✅ Yes (policy suggestions) | ✅ **CONFIRMED** |
| Amazon DevOps Guru | ✅ Yes (ML-based) | ✅ Yes | ✅ **CONFIRMED** |
| AWS Resilience Hub | ✅ Yes | ✅ Yes | ✅ **CONFIRMED** |

---

## 📚 Part 1 — Core Recommendation Services

---

### 1️⃣ AWS Trusted Advisor

> **Memory Trick:** Think of Trusted Advisor as your **AWS doctor** who does a full-body checkup across 5 health areas.  
> *"AWS checks my account and gives general advice."*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **5 Pillars** | Cost Optimization, Performance, Security, Fault Tolerance, Service Limits |
| **Account-level** | Always scans the whole account, not individual resources |
| **No setup required** | Scans automatically — just open it |
| **Free tier exists** | Core checks are free for all AWS accounts |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **Number of checks** | Free tier ≈ 6 basic checks · Business/Enterprise = 400+ checks |
| **Which checks apply** | Only shows relevant findings based on deployed resources |
| **Severity** | 🔴 Action needed · 🟡 Investigation · 🟢 OK |
| **Notifications** | Weekly email summaries — configurable |
| **Multi-account** | Aggregatable via AWS Organizations |

#### Real-World Examples

<details>
<summary>Example 1 — Security Check (Free)</summary>

> You have an S3 bucket with public read access.  
> 🔴 **S3 Bucket Permissions** — Bucket `my-data` has open access permissions.
</details>

<details>
<summary>Example 2 — Cost Optimization Check (Paid)</summary>

> 3 EC2 instances have had ≤5% CPU utilization for 14 days.  
> 🟡 **Low Utilization EC2 Instances** — 3 instances may be candidates for stopping or downsizing.
</details>

<details>
<summary>Example 3 — Service Limits Check</summary>

> You are at 80% of your EC2 On-Demand instance limit in `us-east-1`.  
> 🟡 **EC2 On-Demand Instances** — 80% of limit used. Request a limit increase.
</details>

<details>
<summary>Example 4 — Fault Tolerance Check</summary>

> Your RDS instance does not have Multi-AZ enabled.  
> 🔴 **Amazon RDS Backups** — Multi-AZ is not enabled on production DB instance.
</details>

---

### 2️⃣ AWS Compute Optimizer

> **Memory Trick:** Think of Compute Optimizer as a **personal trainer** who watches how hard your resources work and tells you if you're over-provisioning.  
> *"Am I using the right-size resource?"*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **ML-based analysis** | Uses CloudWatch metrics + ML models — not just rules |
| **Supported resources** | EC2, Auto Scaling Groups, EBS Volumes, Lambda, ECS on Fargate, RDS |
| **Requires CloudWatch data** | Minimum 14 days of metrics to generate recommendations |
| **Scope** | Single account or AWS Organizations level |
| **Cost** | Free for standard recommendations |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **Recommendation quality** | Improves with more data (30+ days ideal) |
| **Savings estimate** | Varies by actual instance types and sizes |
| **Enhanced Infrastructure Metrics** | Optional paid feature — extends lookback to 3 months |
| **External metrics** | Optional — Datadog, Dynatrace integration for better accuracy |

#### Real-World Examples

<details>
<summary>Example 1 — EC2 Right-Sizing</summary>

> `m5.2xlarge` instance: CPU avg 8%, memory 12%.  
> ✅ **Downsize to `m5.large`** — estimated monthly savings **$120**
</details>

<details>
<summary>Example 2 — Lambda Optimization</summary>

> Lambda configured at 1024 MB but uses only 128 MB.  
> ✅ **Reduce memory to 256 MB** — 75% cost reduction per invocation.
</details>

<details>
<summary>Example 3 — EBS Volume</summary>

> `gp2` volume at 500 GB with only 30 GB used and very low IOPS.  
> ✅ **Migrate to `gp3`** and reduce provisioned size — estimated savings **$40/month**.
</details>

<details>
<summary>Example 4 — Auto Scaling Group</summary>

> ASG always runs 10 instances, but 70% of the time only 3 are needed.  
> ✅ **Reduce min capacity**, enable predictive scaling with a smaller baseline instance type.
</details>

---

### 3️⃣ AWS Well-Architected Tool

> **Memory Trick:** Think of it as an **architect's blueprint review** — you submit your design (by answering questions), and an expert checks it against building codes (AWS best practices).  
> *"How do I improve my architecture overall?"*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **6 Pillars** | Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability |
| **Question-based** | You (or your solutions architect) answer the questions — **not fully automatic** |
| **Output** | High Risk Issues (HRI) and Medium Risk Issues (MRI) |
| **Workload-centric** | You define a workload and review it — not the whole account |
| **Cost** | Free to use |
| **Lenses available** | SaaS, Serverless, Machine Learning, and more |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **Lenses applied** | You choose which lens fits (e.g., Serverless Lens for Lambda-based apps) |
| **Question count** | Varies by pillar and lens selected |
| **Milestone tracking** | Save snapshots over time — improvement tracked per workload |
| **Sharing** | Reviews can be shared with AWS Partners |

#### Real-World Examples

<details>
<summary>Example 1 — Security Pillar</summary>

> Q: *How do you manage identities?* → A: We use long-term IAM user access keys.  
> 🔴 **HRI** — Use temporary credentials. Replace long-term keys with IAM Roles.
</details>

<details>
<summary>Example 2 — Reliability Pillar</summary>

> Q: *How do you back up data?* → A: We take manual snapshots occasionally.  
> 🟡 **MRI** — Automate backups using AWS Backup. Define RPO and RTO targets.
</details>

<details>
<summary>Example 3 — Sustainability Pillar</summary>

> Q: *How do you select deployment regions?* → A: Where our team is located.  
> 🟡 **MRI** — Consider regions powered by renewable energy where latency permits.
</details>

---

### 4️⃣ AWS Cost Optimization Hub

> **Memory Trick:** Think of it as a **shopping mall directory** — it doesn't run any stores, but it shows you every deal across the whole mall.  
> *"Show me ALL my cost-saving opportunities in one place."*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **Location** | Lives inside AWS Billing and Cost Management console |
| **Data sources** | Aggregates from Compute Optimizer, Trusted Advisor, and others |
| **Recommendation types** | Rightsizing, idle resources, Savings Plans, Reserved Instances |
| **Requires opt-in** | Must be enabled — not on by default |
| **Cost** | Free to use |
| **Organizations support** | Aggregates across all member accounts |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **Recommendations shown** | Only relevant to your deployed resources |
| **Filtering** | By account, region, resource type, action type |
| **After-discount savings** | Can factor in your specific discount rates (EDP, etc.) |

#### Real-World Examples

<details>
<summary>Example 1 — Aggregated Multi-Account View</summary>

> 5 AWS accounts in an organization.  
> ✅ Total estimated monthly savings: **$4,320** — 12 rightsizing, 4 idle resources, 2 Savings Plan opportunities.
</details>

<details>
<summary>Example 2 — Savings Plan Recommendation</summary>

> Consistently running 20 EC2 instances every hour.  
> ✅ Purchase a **$500/month Compute Savings Plan** — estimated net savings **$1,200/month**.
</details>

<details>
<summary>Example 3 — Idle Resource</summary>

> RDS instance with no connections in 45 days.  
> ✅ Delete/stop idle RDS instance `db-legacy-01` — estimated savings **$240/month**.
</details>

---

### 5️⃣ AWS Cost Explorer

> **Memory Trick:** Think of Cost Explorer as a **financial analyst** — its main job is reporting, but it also gives you a few investment tips (RI/SP).  
> *"Understand my spend AND get some cost recommendations."*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **Primary function** | Cost analysis and visualization |
| **Recommendations** | Reserved Instances (RI) and Savings Plans based on usage history |
| **Rightsizing** | EC2 rightsizing recommendations (via Compute Optimizer integration) |
| **History** | Up to 12 months of historical cost data |
| **Forecasting** | Predicts future costs based on current trends |
| **Cost** | Console is free; API calls have a small cost |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **RI recommendation type** | Standard RI, Convertible RI, zonal vs regional |
| **Lookback period** | Configurable: 7, 30, or 60 days |
| **RI term length** | 1-year or 3-year recommendations |
| **Payment option** | All upfront, partial upfront, no upfront — affects recommendation |

#### Real-World Examples

<details>
<summary>Example 1 — RI Recommendation</summary>

> Running `t3.medium` EC2 in `us-east-1` for 6 months, 24/7.  
> ✅ Purchase **1-year Standard RI** — estimated savings ~38% (~$180/year).
</details>

<details>
<summary>Example 2 — Savings Plan Recommendation</summary>

> Lambda + EC2 compute costs $2,000/month On-Demand.  
> ✅ A **$600/month Compute Savings Plan** → estimated savings **$480/month**.
</details>

<details>
<summary>⚠️ Example 3 — Cost Analysis (NOT a Recommendation)</summary>

> S3 costs increased 220% in March due to data transfer from `us-east-1` to internet.  
> ⚠️ This is **analysis only** — not a recommendation. Important exam distinction.
</details>

---

## 📚 Part 2 — Specialized Recommendation Services

---

### 6️⃣ AWS Security Hub — CSPM

> **Memory Trick:** Think of Security Hub as a **security auditor** who checks your account against known security standards and tells you what to fix.  
> *"Security best-practice findings and remediation guidance."*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **Standards-based** | AWS FSBP, CIS AWS Benchmarks, PCI DSS, NIST |
| **Aggregates findings** | GuardDuty, Inspector, Macie, IAM Access Analyzer, Firewall Manager, 3rd parties |
| **Security Score** | Overall posture score per standard (0–100%) |
| **Remediation guidance** | Each finding links to how to fix it |
| **Setup** | Requires opt-in per region |
| **Cross-account** | Works with AWS Organizations |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **Standards enabled** | You choose: FSBP, CIS, PCI, etc. |
| **Finding severity** | CRITICAL · HIGH · MEDIUM · LOW · INFORMATIONAL |
| **Automated remediation** | Optional — trigger Lambda/SSM via EventBridge |
| **3rd party integrations** | Palo Alto, Splunk, etc. |

#### Real-World Examples

<details>
<summary>Example 1 — S3 Finding</summary>

> 🔴 **CRITICAL** S3.1 — S3 buckets should have block public access enabled.  
> **Fix:** Enable S3 Block Public Access at account level.
</details>

<details>
<summary>Example 2 — IAM Finding</summary>

> 🟠 **HIGH** IAM.4 — IAM root user access key should not exist.  
> **Fix:** Delete root user access keys. Use least-privilege IAM roles instead.
</details>

<details>
<summary>Example 3 — MFA Finding</summary>

> 🔴 **CRITICAL** IAM.6 — Hardware MFA should be enabled for the root user.  
> **Fix:** Enable MFA on root account immediately.
</details>

---

### 7️⃣ IAM Access Analyzer

> **Memory Trick:** Think of it as a **security guard + HR auditor** — it checks who has keys to your building AND whether those keys should be downgraded.  
> *"Who has access, and can AWS recommend tighter permissions?"*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **Two main functions** | (1) External access analysis · (2) Unused access analysis |
| **Supported resources** | S3, IAM Roles, KMS Keys, Lambda, SQS, Secrets Manager, SNS |
| **Uses Zelkova** | Mathematical reasoning — not heuristics |
| **Policy generation** | Generates least-privilege policy from CloudTrail logs |
| **Setup** | Must create an Analyzer (account or org scope) |
| **Cost** | Free |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **Scope** | Account-level or Organization-level |
| **Archive rules** | Auto-archive expected findings (e.g., known cross-account access) |
| **CloudTrail lookback** | Up to 90 days for policy generation |
| **Inactivity threshold** | Configurable: 1–180 days |

#### Real-World Examples

<details>
<summary>Example 1 — External Access Finding</summary>

> S3 bucket policy allows `s3:GetObject` to `*` (everyone).  
> 🔴 Bucket `company-data` is publicly accessible.
</details>

<details>
<summary>Example 2 — Policy Generation (Recommendation)</summary>

> IAM role has `AdministratorAccess`. After 90 days of CloudTrail analysis:  
> ✅ **Generated least-privilege policy** — role only used `s3:GetObject`, `s3:PutObject`, `cloudwatch:PutMetricData`.
</details>

<details>
<summary>Example 3 — Unused Access Finding</summary>

> IAM user has `EC2FullAccess` but no EC2 API usage in 120 days.  
> 🟡 Consider removing or replacing with a scoped-down policy.
</details>

---

### 8️⃣ Amazon DevOps Guru

> **Memory Trick:** Think of DevOps Guru as a **NOC AI analyst** — it watches all your operational data and calls you when something looks wrong, with a suggested fix.  
> *"Operational problem detected — here's what to check."*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **ML-based** | Trained on millions of operational events — no rules to write |
| **Proactive insights** | Warns you BEFORE an issue causes an outage |
| **Data sources** | CloudWatch metrics, logs, X-Ray, CloudTrail |
| **Insight types** | Reactive (problem detected) · Proactive (incoming issue) |
| **OpsCenter integration** | Creates OpsItems automatically |
| **Supported resources** | ECS, EKS, Lambda, RDS, DynamoDB, EC2, ELB, and more |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **Coverage scope** | CloudFormation stacks, all account, or tag-based |
| **Notifications** | SNS — configurable |
| **Cost** | Charged per resource analyzed per hour |
| **CodeGuru integration** | Optional — deeper code-level recommendations |

#### Real-World Examples

<details>
<summary>Example 1 — RDS Anomaly (Reactive)</summary>

> RDS read replica shows 10× normal read latency.  
> 🔴 **Reactive Insight** — Check long-running queries with Performance Insights. Consider adding a read replica.
</details>

<details>
<summary>Example 2 — Lambda Anomaly (Proactive)</summary>

> Error rate patterns suggest approaching concurrency limits.  
> 🟡 **Proactive Insight** — Request concurrency limit increase or implement exponential backoff.
</details>

<details>
<summary>Example 3 — DynamoDB Throttling</summary>

> `ProvisionedThroughputExceededException` burst on `sessions` table.  
> 🔴 **Hot partition detected** — Implement write sharding or migrate to on-demand capacity mode.
</details>

---

### 9️⃣ AWS Resilience Hub

> **Memory Trick:** Think of Resilience Hub as a **disaster recovery consultant** — you tell it how fast you need to recover, it tests your setup and tells you what to add.  
> *"How can I make the application more resilient?"*

#### Fixed Characteristics

| Property | Detail |
|----------|--------|
| **Resiliency Score** | Always generates a score per application (0–100) |
| **RTO/RPO checks** | You define recovery goals; Hub tells you if you meet them |
| **Application-based** | Defined via CloudFormation, Terraform, AppRegistry, or Resource Group |
| **Disruption categories** | Software · Hardware · AZ · Region |
| **FIS integration** | Suggests chaos engineering tests via AWS Fault Injection Simulator |

#### Variable Characteristics

| Property | Detail |
|----------|--------|
| **RTO/RPO targets** | You set your own — Hub judges against YOUR targets |
| **Recommendation types** | Backups, Multi-AZ, cross-region replication |
| **Cost** | Charged per application assessment |
| **Drift detection** | Continuously monitors for changes that reduce resiliency |

#### Real-World Examples

<details>
<summary>Example 1 — Missing Multi-AZ</summary>

> Single-AZ RDS with RTO target of 1 hour.  
> 🔴 Enable RDS Multi-AZ. **Current recovery time: 4 hrs · Target: 1 hr · Gap: 3 hrs.**
</details>

<details>
<summary>Example 2 — Missing Backup</summary>

> DynamoDB table with no PITR enabled and RPO target of 15 minutes.  
> 🔴 Enable DynamoDB Point-In-Time Recovery. **Current RPO: ∞ · Target: 15 min.**
</details>

<details>
<summary>Example 3 — Resiliency Score</summary>

> Application `ecommerce-prod` assessed.  
> **Score: 62/100** · 2 high-severity gaps (No Multi-AZ, No DynamoDB backup) · 1 medium gap.
</details>

---

## ❌ Part 3 — Services That Are NOT Recommendation Services

| Service | What It Does | Why It's NOT a Recommendation Service |
|---------|-------------|---------------------------------------|
| **Amazon CloudWatch** | Monitors metrics, logs, and alarms | Watches and alerts — **you** write the rules and interpret the data |
| **Amazon GuardDuty** | Detects active threats (malware, brute force, crypto mining) | Detects threats — does **not** recommend architecture or config improvements |
| **AWS Prescriptive Guidance / Docs** | Provides written best-practice guidance | Static content — does **not** scan your account or generate personalized findings |

> **⚠️ Exam Trap:** GuardDuty feeds its findings **into** Security Hub, but GuardDuty itself does not give architecture recommendations.

---

## 🚨 Part 4 — Exam Traps

### Trap 1 — Trusted Advisor vs. Compute Optimizer

| Aspect | Trusted Advisor | Compute Optimizer |
|--------|----------------|-------------------|
| EC2 check | "This instance has low utilization" (threshold rule) | "Switch from `m5.2xlarge` to `t3.medium`" (ML analysis) |
| Data source | CloudWatch CPU/network thresholds | ML models on 14+ days of metrics |
| Specificity | General alert | Specific target instance type |
| Other resource types | Account-wide (security, limits, etc.) | Compute ONLY |

> ✅ **Rule:** Right-size / specific instance type → **Compute Optimizer**. Best-practice check / account health → **Trusted Advisor**.

---

### Trap 2 — Cost Explorer vs. Cost Optimization Hub

| Aspect | Cost Explorer | Cost Optimization Hub |
|--------|--------------|----------------------|
| Primary purpose | Cost analysis & visualization | Aggregated cost recommendations |
| Recommendations | RI + Savings Plans (+ rightsizing) | ALL types from multiple sources |
| Data source | Itself | Aggregates from Compute Optimizer, Trusted Advisor, etc. |

> ✅ **Rule:** Understand spend + RI recommendations → **Cost Explorer**. All savings in one view → **Cost Optimization Hub**.

---

### Trap 3 — Security Hub vs. GuardDuty vs. IAM Access Analyzer

| Aspect | GuardDuty | Security Hub | IAM Access Analyzer |
|--------|-----------|--------------|---------------------|
| Focus | Active threats | Config best-practice compliance | Access control analysis |
| Example finding | "Instance communicating with malware C2 server" | "MFA not enabled on root" | "S3 bucket is publicly readable" |
| Gives recommendations? | ❌ Detect only | ✅ Includes remediation steps | ✅ Generates least-privilege policies |
| Feeds into Security Hub? | ✅ Yes (as a source) | — (is the aggregator) | ✅ Yes (as a source) |

---

### Trap 4 — Well-Architected Tool Is NOT Automatic

> ❌ **WRONG:** Well-Architected Tool scans my AWS account automatically.  
> ✅ **RIGHT:** You answer questions about your workload; it gives recommendations based on your answers.

---

### Trap 5 — Cost Optimization Hub Requires Opt-In

> Trusted Advisor and Compute Optimizer are visible by default.  
> ✅ **Cost Optimization Hub must be explicitly enabled** before it shows any data.

---

### Trap 6 — Trusted Advisor access depends on the Support plan

| Plan | Checks Available |
|------|-----------------|
| Basic Support | Service Limits checks plus selected Security and Fault Tolerance checks |
| Business Support+, Enterprise Support, or Unified Operations | All Trusted Advisor checks plus documented Trusted Advisor API access |

> ❌ **FALSE:** "Every AWS account receives every Trusted Advisor check." Access depends on the Support plan. This distinction was verified on **2026-07-25**; transition-plan entitlements and check availability can change.

[AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html)

---

### Trap 7 — DevOps Guru vs. CloudWatch Alarms

| Aspect | CloudWatch Alarms | DevOps Guru |
|--------|------------------|-------------|
| Setup | You define thresholds | No setup — ML figures it out |
| Trigger | Exact threshold breach | Anomalous patterns detected by ML |
| Recommendations | ❌ Alerts only | ✅ Tells you what to investigate and how to fix it |

> ✅ **Rule:** Detect operational anomalies WITHOUT defining thresholds → **DevOps Guru**.

---

### Trap 8 — IAM Access Analyzer Policy Generation Requires CloudTrail

Policy generation needs **all three**:
1. ✅ CloudTrail must be enabled
2. ✅ API activity in the last 90 days
3. ✅ You must **manually trigger** policy generation — it does not run on a schedule

> ❌ **FALSE:** "IAM Access Analyzer automatically generates new policies on a schedule."

---

### Trap 9 — Resilience Hub RTO/RPO Are YOUR Numbers

> Resilience Hub judges you against your **own** defined targets — not a universal standard.
>
> - RTO target = 24 hrs, recovery time = 10 hrs → ✅ PASSING  
> - RTO target = 1 hr, recovery time = 10 hrs → ❌ FAILING

---

### Trap 10 — CloudWatch Contributes to Recommendations But Isn't One

> Compute Optimizer and DevOps Guru both **use** CloudWatch metrics as a data source.  
> ❌ **FALSE:** "Use CloudWatch to get rightsizing recommendations." → That's **Compute Optimizer**.

---

## 📋 Part 5 — Master Cheat Sheet

### Keyword → Service Mapping

| If the question mentions... | The answer is... |
|-----------------------------|-----------------|
| Best practices · no custom rules · quick account check | AWS Trusted Advisor |
| Right-size · resize EC2/Lambda/EBS · ML-based compute | AWS Compute Optimizer |
| Review architecture · 6 pillars · improve workload | AWS Well-Architected Tool |
| All cost savings in one place · multi-account cost aggregation | AWS Cost Optimization Hub |
| Reserved Instances · Savings Plan · visualize/understand spend | AWS Cost Explorer |
| Security posture · compliance standard · remediation · CIS benchmark | AWS Security Hub |
| Overly permissive policies · least-privilege · who has access to S3 | IAM Access Analyzer |
| Operational anomaly · no threshold setup · ML ops intelligence | Amazon DevOps Guru |
| Resiliency score · RTO/RPO gap · application resilience | AWS Resilience Hub |
| Detect malicious activity · compromised credentials · crypto mining | Amazon GuardDuty ❌ *(NOT a recommendation service)* |
| Monitor metrics · set alarms · dashboards | Amazon CloudWatch ❌ *(NOT a recommendation service)* |

---

### 🔢 Top 5 Services — Most Exam Questions Come From Here

```
1. Trusted Advisor     → Account-level best-practice recommendations (5 pillars)
2. Compute Optimizer   → Right-size compute resources (EC2, Lambda, EBS, ASG, ECS, RDS)
3. Well-Architected    → Architecture improvement recommendations (6 pillars, self-assessment)
4. Cost Explorer       → Understand spend + RI/Savings Plan recommendations
5. Cost Opt Hub        → All cost savings aggregated in one place
```

---

### 🎯 Memory Phrases

```
Trusted Advisor        → General AWS health checkup
Compute Optimizer      → Right-size your compute
Well-Architected Tool  → Architecture blueprint review
Cost Optimization Hub  → All savings deals in one mall
Cost Explorer          → Finance analyst + RI investment tips
Security Hub           → Security auditor + remediation guide
IAM Access Analyzer    → Who has your keys? Shrink those permissions.
DevOps Guru            → AI ops analyst watching for anomalies
Resilience Hub         → Disaster recovery consultant — do you meet your RTO/RPO?
```

---

### 📐 Decision Tree

```
COST questions
├── Understand/analyze spend            → Cost Explorer
├── Right-size a specific resource      → Compute Optimizer
├── All cost savings in one view        → Cost Optimization Hub
└── Best practices (including cost)     → Trusted Advisor

SECURITY questions
├── Active threats / malicious activity → GuardDuty ❌ (not a rec. service)
├── Security posture / compliance       → Security Hub
├── IAM permissions / who has access    → IAM Access Analyzer
└── Security best practices (broad)     → Trusted Advisor

PERFORMANCE / COMPUTE questions
├── Right-size EC2/Lambda/EBS           → Compute Optimizer
├── Operational anomaly / ML detection  → DevOps Guru
└── Architecture performance pillar     → Well-Architected Tool

RELIABILITY / RESILIENCE questions
├── RTO/RPO gap                         → Resilience Hub
├── Fault tolerance best practices      → Trusted Advisor
└── Architecture reliability pillar     → Well-Architected Tool

ARCHITECTURE OVERALL
└── Always                              → AWS Well-Architected Tool
```

---

## 📌 Part 6 — Additional Facts

### Compute Optimizer — Supported Resources

| # | Resource |
|---|----------|
| 1 | EC2 Instances |
| 2 | EC2 Auto Scaling Groups |
| 3 | EBS Volumes |
| 4 | Lambda Functions |
| 5 | ECS Services on AWS Fargate |
| 6 | RDS DB Instances |

---

### Well-Architected Tool — 6 Pillars

| # | Pillar |
|---|--------|
| 1 | Operational Excellence |
| 2 | Security |
| 3 | Reliability |
| 4 | Performance Efficiency |
| 5 | Cost Optimization |
| 6 | Sustainability |

> **Mnemonic:** **O**h **S**omebody **R**eally **P**aid for **C**loud **S**ustainability → **OSRPCS**

---

### Trusted Advisor — 5 Pillars

| # | Pillar |
|---|--------|
| 1 | Cost Optimization |
| 2 | Performance |
| 3 | Security |
| 4 | Fault Tolerance |
| 5 | Service Limits |

> **Mnemonic:** **C**ats **P**urr **S**o **F**earlessly **L**oudly → **CPSFL**

---

### Trusted Advisor — Free vs. Paid

| Check Type | Free (Basic/Developer) | Business/Enterprise Support |
|------------|----------------------|-----------------------------|
| Cost Optimization | Very limited | Full (50+ checks) |
| Performance | Very limited | Full |
| Security | 6 core checks | Full |
| Fault Tolerance | Very limited | Full |
| Service Limits | Very limited | Full |
| API Access | ❌ No | ✅ Yes |
| CloudWatch Integration | ❌ No | ✅ Yes |

---

## 🏁 Final Summary Table

| Service | Focus | Auto-Scans | Self-Assessment | Free | Best Trigger Words |
|---------|-------|-----------|----------------|------|-------------------|
| Trusted Advisor | All 5 pillars, account health | ✅ | ❌ | Partial | best practices, no setup, account health |
| Compute Optimizer | Right-size compute | ✅ ML | ❌ | ✅ | right-size, instance type, Lambda memory |
| Well-Architected Tool | Architecture review | ❌ | ✅ | ✅ | review architecture, 6 pillars, workload |
| Cost Optimization Hub | Aggregate cost savings | ✅ | ❌ | ✅ | all savings in one place, multi-account |
| Cost Explorer | Cost analysis + RI/SP | ✅ for RI/SP | ❌ | ✅ | visualize cost, RI recommendation |
| Security Hub | Security posture | ✅ | ❌ | Partial | security score, remediation, compliance |
| IAM Access Analyzer | Access + permissions | ✅ | ❌ | ✅ | public access, least-privilege, unused |
| DevOps Guru | Ops anomalies | ✅ ML | ❌ | Paid | anomaly, no threshold, ML ops |
| Resilience Hub | App resilience | ✅ | ❌ | Paid | resiliency score, RTO/RPO, app resilience |

---

*Guide prepared for AWS Cloud Practitioner Exam — covers all recommendation and advisory services with fixed/variable analysis, real-world examples, and exam trap awareness.*
