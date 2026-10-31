# AWS Documentation & Guidance Services
 For AWS Cloud Practitioner Exam

---

## Key Rule to Remember
- Best practices, patterns, frameworks, blogs, reference architectures, guides, whitepapers → DocumentationGuidance Resource
- Findings, alerts, evidence, metrics, checks, remediation → OperationalSecurity Tool (NOT documentation)

---

## ✅ Services That Provide Documentation Guidance

### 1. AWS Well-Architected Framework
A best-practices framework for designing and operating workloads in AWS. Helps you understand the pros and cons of design decisions and learn architectural best practices across 6 pillars (Security, Reliability, Performance, Cost, Sustainability, Operational Excellence).

---

### 2. AWS Prescriptive Guidance
Provides planning and implementation guidance, best practices, patterns, and step-by-step instructions from AWS experts. Focuses on helping teams adopt and migrate to AWS faster.

---

### 3. AWS Architecture Center
A central hub for reference architectures, architecture diagrams, patterns, and best practices. Great for finding proven solution designs for common use cases.

---

### 4. AWS Security Blog
An AWS-authored learning resource covering security best practices, announcements, and architecturesecurity guidance. Written by AWS security experts.

---

### 5. AWS Documentation
The main official documentation hub containing user guides, tutorials, API references, code samples, and more for every AWS service.

---

### 6. AWS Whitepapers
In-depth documents published by AWS covering overview, security, compliance, and architectural topics. Some older whitepapers are archived, but most are available on the docs site.

---

### 7. AWS Security Reference Architecture (AWS SRA)
An AWS reference architecture that shows recommended security architecture, services, and features laid out in a structured design. Useful for understanding how security services fit together.

---

### 8. AWS Artifact
A self-service portal that provides official compliance reports and agreements on demand (e.g., SOC, PCI, ISO reports). It is a compliance documentation portal — not a findings or detection tool.

---

### 9. AWS Trust Center  AWS Compliance Pages
Resource hubs covering security, compliance programs, certifications, regulatory information, and learning material. Useful for understanding AWS's compliance posture.

---

## ❌ Services That Are NOT Documentation Guidance

 Service  What it actually does 
------
 Amazon GuardDuty  Threat detection → gives findings 
 AWS Security Hub  Centralizes and prioritizes security issues 
 AWS Config  Evaluates resource configurations and compliance 
 AWS Audit Manager  Collects audit evidence and maps controls 
 Amazon CloudWatch  Metrics, logs, alarms 
 AWS Budgets  Cost trackingforecasting 
 AWS Compute Optimizer  Performancecost recommendations 

---

## ⚠️ Exam Traps — Common Tricks AWS Uses

These are the most common ways AWS exam questions try to mislead you on this topic

---

### 🪤 Trap 1 — Amazon GuardDuty sounds educational
The word security guidance in a question might make you think of GuardDuty because it deals with security.
Reality GuardDuty is a threat detection service — it gives you findings (e.g., suspicious API call from a known malicious IP), not learning material or architectural advice.
 ❓ Which service provides security guidance and best practices → NOT GuardDuty

---

### 🪤 Trap 2 — AWS Artifact sounds like a tool, not a document portal
The name Artifact sounds like something you build or run.
Reality AWS Artifact is purely a self-service compliance document portal — you log in and download audit reports (SOC 2, ISO 27001, PCI DSS). No detection, no monitoring.
 ❓ Which service provides compliance reports on demand → AWS Artifact ✅

---

### 🪤 Trap 3 — AWS Config sounds like it gives configuration guidance
Config implies it helps you configure things correctly — like advice.
Reality AWS Config monitors and records resource configurations and checks them against rules. It tells you if something is non-compliant, it does not teach you how to configure things.
 ❓ Which service provides guidance on how to set up your AWS resources → NOT AWS Config

---

### 🪤 Trap 4 — AWS Audit Manager sounds like a studyaudit guide
Audit + Manager sounds like it manages audit learning or documentation.
Reality Audit Manager collects evidence automatically and maps it to compliance frameworks (like HIPAA, GDPR). It is an operational evidence-collection tool, not a guidance resource.
 ❓ Which service helps you prepare for audits by providing guidance → NOT Audit Manager (it collects evidence, not guidance)

---

### 🪤 Trap 5 — AWS Security Hub sounds like a hub of security knowledge
A hub suggests a central place to learn about security.
Reality Security Hub aggregates and prioritizes security findings from GuardDuty, Inspector, Macie, etc. It is a findings dashboard, not a documentation center.
 ❓ Which service is a central hub for security best practices and guidance → AWS Architecture Center or Security Blog, NOT Security Hub

---

### 🪤 Trap 6 — AWS Trusted Advisor the tricky middle ground
Trusted Advisor is often confused with documentation guidance because it gives recommendations.
Reality Trusted Advisor gives automated real-time recommendations on cost, performance, security, and fault tolerance based on your actual account. It is closer to an operational tool than a documentation resource — but questions may try to use recommendations to trick you into picking a documentation service instead.
 ❓ Which service gives best-practice recommendations based on your AWS environment → AWS Trusted Advisor (operational recommendations, not static documentation)

---

### 🪤 Trap 7 — Whitepapers vs. AWS Documentation they are NOT the same thing
Exam questions sometimes use these interchangeably to confuse you.
- AWS Whitepapers → Deep-dive documents on specific topics (security, architecture, compliance). They are standalone PDFs.
- AWS Documentation → The full official reference hub for every service (user guides, API docs, tutorials).
 Both are guidance, but they serve different purposes. Know the distinction.

---

### 🪤 Trap 8 — Compliance does not always mean documentation
- AWS Artifact → compliance documentation ✅ (reports and agreements)
- AWS Config → compliance checking ❌ (evaluates rules against your resources)
- AWS Audit Manager → compliance evidence ❌ (collects proof for auditors)
 The word compliance appears in all three — read carefully what the question is really asking.

---

## 📝 Quick Memory List

Guidance  Documentation
- Well-Architected Framework
- Prescriptive Guidance
- Architecture Center
- Security Blog
- AWS Documentation
- Whitepapers
- Security Reference Architecture (SRA)
- Artifact (compliance reports)
- Trust Center  Compliance Pages

Not Guidance (Operational Tools)
- GuardDuty, Security Hub, Config, Audit Manager, CloudWatch, Budgets, Compute Optimizer