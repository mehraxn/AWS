# AWS Certified Cloud Practitioner (CLF-C02) Start Here

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

Use this page as the main route through the repository for AWS Certified Cloud Practitioner (CLF-C02). The notes are a study and revision resource. They do not guarantee an exam result, and AWS can change the exam guide, services, pricing, and Support features.

## Before You Begin

- Start with the essential path even if you already use one AWS service at work. CLF-C02 tests breadth across four domains.
- Learn the problem a service solves before memorizing features.
- Follow comparison links when two services appear similar.
- Treat architecture-heavy sections labeled SAA as optional deeper reading.
- Verify time-sensitive details against the official references in each lesson.

## The CPP Study Path

### 1. Cloud fundamentals — Essential for CPP

Read:

1. [Cloud concepts and benefits](../../01-cloud-fundamentals/02-cloud-concepts-and-benefits.md)
2. [AWS Shared Responsibility Model](../../01-cloud-fundamentals/01-shared-responsibility-model.md)
3. [AWS Well-Architected Framework](../../13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md)
4. [AWS Cloud Adoption Framework](../../13-architecture-and-design-patterns/aws-cloud-adoption-framework/01-overview.md)

Focus on agility, elasticity, high availability, global reach, variable cost, rightsizing, automation, the six Well-Architected pillars, migration benefits, and who is responsible for each security layer.

### 2. Global infrastructure — Essential for CPP

Read [Regions, Availability Zones, and edge infrastructure](../../02-global-infrastructure/01-regions-availability-zones-and-edge.md).

Be able to choose multiple Availability Zones for high availability and recognize when multiple Regions support disaster recovery, business continuity, latency, or data-sovereignty needs.

### 3. Security, identity, and compliance — Essential for CPP

Study in this order:

1. [IAM overview](../../03-identity-governance-and-organizations/aws-iam/01-overview.md)
2. [Root-user protection](../../03-identity-governance-and-organizations/aws-iam/10-root-user.md)
3. [IAM Identity Center](../../03-identity-governance-and-organizations/aws-iam-identity-center/01-overview.md)
4. [Security and compliance](../../09-security-and-compliance/)
5. [Security-service selection](../../15-comparisons-and-decision-guides/security/01-security-service-selection.md)
6. [CloudWatch, CloudTrail, and Config](../../15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md)

Focus on least privilege, multi-factor authentication (MFA), temporary credentials, federation, encryption at rest and in transit, AWS Artifact, logging/auditing, and the purpose of common security services.

### 4. Core AWS services — Essential for CPP

Use the category introductions, then the decision guides:

- [Compute](../../04-compute/)
- [Storage](../../05-storage/)
- [Databases](../../06-databases/)
- [Networking and content delivery](../../07-networking-and-content-delivery/)
- [Core compute and storage selection](../../15-comparisons-and-decision-guides/compute-and-storage/01-core-selection-guide.md)
- [Database selection](../../15-comparisons-and-decision-guides/databases/01-database-selection-guide.md)
- [Cloud Practitioner networking guide](../../07-networking-and-content-delivery/networking-guide/01-cloud-practitioner-study-guide.md)

At CPP depth, choose the correct service category and explain the basic reason. Detailed implementation commands, complex routing, and architecture patterns are optional SAA-depth material.

### 5. Billing, pricing, and support — Essential for CPP

Study:

1. [Pricing fundamentals and purchasing models](../../12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md)
2. [Cost-management tool selection](../../15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md)
3. [Data-transfer cost patterns](../../12-billing-pricing-and-support/aws-billing-and-cost-management/03-data-transfer-costs.md)
4. [AWS Support plans](../../12-billing-pricing-and-support/aws-support/02-support-plans.md)
5. [Billing, pricing, and support index](../../12-billing-pricing-and-support/)

Prefer stable decision rules over memorized prices. Support-plan features, Free Tier terms, and exact rates can change.

### 6. Service comparisons — Essential for CPP review

Open the [comparisons and decision guides](../../15-comparisons-and-decision-guides/) after learning the individual concepts. Prioritize:

- SQS versus SNS versus EventBridge
- CloudWatch versus CloudTrail versus Config
- core compute and storage selection
- database selection
- security-service selection
- cost-management tool selection
- CloudFront versus Global Accelerator

A comparison is useful only after you understand what each option does.

### 7. Secondary service recognition — Useful supporting material

Review:

- [Serverless and application integration](../../08-serverless-and-application-integration/)
- [Monitoring, management, and deployment](../../10-monitoring-management-and-deployment/)
- [Migration and hybrid cloud](../../11-migration-and-hybrid-cloud/)
- [AI, ML, analytics, and other services](../../14-ai-ml-analytics-and-other-services/)

Several lower-priority services need recognition rather than implementation depth. The current [coverage dashboard](../../docs/certification-audit/CPP-COVERAGE-DASHBOARD.md) identifies remaining gaps, including end-user computing and Marketplace coverage.

### 8. Domain quizzes and mock exams — Planned

Domain quizzes and full mock exams will live in this directory. They are not present yet. Until they are added, use the knowledge checks in canonical lessons and the [CPP scenario-reasoning guide](../01-cpp-scenario-reasoning.md).

Do not treat the absence of a mock exam as evidence that content coverage is complete.

### 9. Final review — Essential for CPP

1. Revisit every question you answered incorrectly.
2. Group mistakes by the four official domains, not only by service.
3. Read the canonical lesson and comparison for each weak area.
4. Explain why the correct option fits and why the closest distractor does not.
5. Recheck volatile pricing, Support, service-status, and scope facts in official AWS documentation.

## Essential, Supporting, and Optional Material

| Label | Meaning |
|---|---|
| **Essential for CPP** | Directly supports a core task statement or heavily used CPP decision. Study it before practice. |
| **Useful supporting material** | Improves recognition or fills context but should not displace the essential path. |
| **Optional SAA-depth material** | Explores architecture, implementation, resilience, or trade-offs beyond the CPP requirement. Read only when useful to you. |

Badges mark meaningful certification relevance, not completeness. Read the [certification-label policy](../../docs/certification-labels.md).

## Track Weak Domains

| Domain | Questions attempted | Correct | Main weak concepts | Lessons to revisit |
|---|---:|---:|---|---|
| 1. Cloud Concepts |  |  |  |  |
| 2. Security and Compliance |  |  |  |  |
| 3. Cloud Technology and Services |  |  |  |  |
| 4. Billing, Pricing, and Support |  |  |  |  |

The official domain weights are 24%, 30%, 34%, and 12%, respectively. Use the table to diagnose gaps; do not infer an exam score from repository quiz results.

## Maintainer Evidence

- [Current CPP coverage dashboard](../../docs/certification-audit/CPP-COVERAGE-DASHBOARD.md)
- [Requirement-level coverage matrix](../../docs/certification-audit/CPP-COVERAGE-MATRIX.md)
- [Canonical content map](../../docs/certification-audit/CPP-CANONICAL-CONTENT-MAP.md)
- [Implementation backlog](../../docs/certification-audit/CPP-IMPLEMENTATION-BACKLOG.md)
- [CPP content and style standard](../../docs/content-standards/CPP-CONTENT-AND-STYLE-STANDARD.md)

Official scope checked: **2026-07-27**. See the [official CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html).

[Back to exam preparation](../README.md) · [Repository home](../../README.md)
