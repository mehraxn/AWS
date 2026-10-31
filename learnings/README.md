# AWS CPP and SAA Study Notes

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

A structured AWS learning repository for:

- **AWS Certified Cloud Practitioner — CLF-C02**
- **AWS Certified Solutions Architect – Associate — SAA-C03**

The material starts with beginner-friendly cloud concepts and progresses to service comparisons, architecture patterns, resilience, security, cost optimization, and scenario reasoning.

## Who This Repository Is For

- Beginners learning AWS for the first time
- Learners preparing for the AWS Cloud Practitioner exam
- Learners preparing for the AWS Solutions Architect – Associate exam
- Developers, DevOps engineers, and cloud practitioners reviewing AWS services

## Certification Labels

- **CPP** marks meaningful Cloud Practitioner relevance and foundational or service-recognition depth.
- **SAA** marks meaningful Solutions Architect relevance with architecture decisions or scenario depth.
- A badge indicates relevance; it is not a completeness or exam-outcome guarantee.

Read the full [certification-label policy](docs/certification-labels.md).

## Start Here

### Cloud Practitioner Path

Start with the dedicated [CLF-C02 start-here and study-path guide](16-exam-preparation/cloud-practitioner/). It separates essential CPP lessons, useful supporting material, optional SAA-depth reading, comparisons, practice, and final review.

The essential sequence is:

1. Cloud fundamentals
2. Global infrastructure
3. Security and Shared Responsibility
4. Core AWS services
5. Billing, pricing, and support
6. Service comparisons
7. Domain quizzes
8. Full mock exams
9. Final review

Domain quizzes and full mock exams are planned but not yet present. The guide points to current lesson-level checks and scenario practice in the meantime.

### Solutions Architect – Associate Path

1. Review the core service categories: identity, compute, storage, databases, networking, and security.
2. Study [Serverless and Application Integration](08-serverless-and-application-integration/).
3. Study [Monitoring, Management, and Deployment](10-monitoring-management-and-deployment/).
4. Review [Migration and Hybrid Cloud](11-migration-and-hybrid-cloud/).
5. Work through [Architecture and Design Patterns](13-architecture-and-design-patterns/).
6. Practice with [Comparisons and Decision Guides](15-comparisons-and-decision-guides/).
7. Finish with [SAA Architecture Scenario Reasoning](16-exam-preparation/02-saa-architecture-scenario-reasoning.md).

## Learning Map

| Section | Main focus |
|---|---|
| [Cloud Fundamentals](01-cloud-fundamentals/) | Cloud concepts and shared responsibility |
| [Global Infrastructure](02-global-infrastructure/) | Regions, Availability Zones, and edge infrastructure |
| [Identity, Governance, and Organizations](03-identity-governance-and-organizations/) | IAM and multi-account governance |
| [Compute](04-compute/) | EC2, containers, serverless, scaling, and load balancing |
| [Storage](05-storage/) | Object, block, file, backup, and hybrid storage |
| [Databases](06-databases/) | Relational, NoSQL, and caching services |
| [Networking and Content Delivery](07-networking-and-content-delivery/) | VPC, DNS, connectivity, and edge delivery |
| [Serverless and Application Integration](08-serverless-and-application-integration/) | APIs, queues, events, and workflows |
| [Security and Compliance](09-security-and-compliance/) | Encryption, detection, protection, and compliance |
| [Monitoring, Management, and Deployment](10-monitoring-management-and-deployment/) | Observability, automation, configuration, and deployment |
| [Migration and Hybrid Cloud](11-migration-and-hybrid-cloud/) | Migration, transfer, discovery, and hybrid infrastructure |
| [Billing, Pricing, and Support](12-billing-pricing-and-support/) | Pricing, cost tools, support, and health |
| [Architecture and Design Patterns](13-architecture-and-design-patterns/) | Availability, resilience, security, and disaster recovery |
| [AI, ML, Analytics, and Other Services](14-ai-ml-analytics-and-other-services/) | Analytics, managed AI, IoT, and business services |
| [Comparisons and Decision Guides](15-comparisons-and-decision-guides/) | Requirement-driven service selection |
| [Exam Preparation](16-exam-preparation/) | Original CPP and SAA scenario reasoning |
| [Archive](90-archive/) | Historical and retired content; not part of the study path |

## How to Use the Notes

For each service or concept, answer these questions:

1. What problem does it solve?
2. Is it managed, serverless, regional, or global?
3. When should it be selected?
4. When should it not be selected?
5. Which services are commonly compared with it?
6. What remains the customer’s responsibility?
7. How does it affect availability, performance, security, operations, and cost?

Use the [service index](docs/service-index.md) to locate a topic and the [comparison guides](15-comparisons-and-decision-guides/) to practice requirement-driven selection.

## Repository Quality

The repository includes validation and review records for:

- Internal Markdown links and anchors
- File naming and duplicate detection
- Empty files and canonical ownership
- Certification badge consistency
- AWS terminology and volatile product-status checks
- Sensitive files, temporary artifacts, and exam-integrity concerns

Technical audit and release history are kept under [`docs/`](docs/) so the learner-facing pages remain focused on study.

## Known Limitations

- Some certification task statements still have partial learning depth.
- Some older knowledge checks do not yet include detailed explanations.
- Pricing, quotas, Support plans, Free Tier rules, product availability, and certification scope can change.
- These notes support study and architecture practice; they do not guarantee exam success.

Review the [known limitations](docs/release/KNOWN-LIMITATIONS.md) and [maintenance guide](docs/release/MAINTENANCE-AND-FRESHNESS-GUIDE.md).

## Exam Integrity

This repository contains original learning material. It does not intentionally include real exam questions, recalled confidential questions, or exam dumps.

## Documentation

- [Repository documentation](docs/)
- [Repository map](docs/repository-map.md)
- [Certification audit](docs/certification-audit/)
- [Validation and release records](docs/release/)
- [Contributing guide](CONTRIBUTING.md)
- [Validation scripts](scripts/)

## Disclaimer

AWS services, prices, quotas, availability, product names, and certification objectives can change. Verify time-sensitive information against current official AWS documentation.
