# AWS Cloud Adoption Framework

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

The AWS Cloud Adoption Framework (AWS CAF) helps organizations assess cloud readiness, identify capability gaps, align stakeholders, and build an evolving cloud-transformation roadmap.

Cloud adoption is not only a technical migration. It also requires business alignment, trained people, governance, security, an appropriate platform, and operating processes.

A deeper supporting lesson is available in [AWS Cloud Adoption Framework](../13-architecture-and-design-patterns/aws-cloud-adoption-framework/01-overview.md).

## What AWS CAF Is and Is Not

AWS CAF is:

- a best-practice framework;
- a readiness and transformation model;
- a way to identify organizational capabilities and gaps;
- guidance for prioritizing transformation work;
- useful before, during, and after migration.

AWS CAF is not:

- a compute or storage service;
- an automated migration tool;
- a compliance certification;
- a replacement for detailed architecture design;
- the same thing as AWS Migration Hub or the Well-Architected Framework.

## The Six Perspectives

AWS CAF groups capabilities into six perspectives.

### Business

**Focus:** make cloud investment support business strategy and outcomes.

Common topics include:

- business goals and value realization;
- transformation strategy;
- product and portfolio direction;
- financial planning;
- risk and business-case alignment.

**Typical stakeholders:** executives, finance leaders, business owners, CIO, CTO.

**Exam clue:** “How will cloud adoption increase business value or support a new market?”

### People

**Focus:** develop culture, skills, leadership, organizational structure, and change readiness.

Common topics include:

- cloud skills and training;
- workforce planning;
- leadership sponsorship;
- organizational design;
- culture and change management.

**Typical stakeholders:** human resources, leadership, training teams, technology managers.

**Exam clue:** “Employees need new cloud skills and the organization must manage cultural change.”

### Governance

**Focus:** coordinate initiatives, manage risk, control investment, and guide decision-making.

Common topics include:

- policies and decision rights;
- portfolio and program management;
- cloud financial management;
- risk and compliance oversight;
- measurement and accountability.

**Typical stakeholders:** finance, risk, compliance, program management, enterprise architecture.

**Exam clue:** “The organization needs policies, accountability, cost control, and risk oversight.”

### Platform

**Focus:** build and evolve the technical cloud environment used to deliver workloads.

Common topics include:

- cloud architecture and engineering;
- landing-zone foundations;
- networks and accounts;
- application and data platforms;
- infrastructure automation and delivery pipelines.

**Typical stakeholders:** architects, engineers, application teams, data teams.

**Exam clue:** “The organization needs a scalable technical foundation for workloads.”

### Security

**Focus:** protect data and workloads while managing security and compliance risk.

Common topics include:

- identity and access management;
- security governance;
- detection and response;
- infrastructure and data protection;
- compliance assurance.

**Typical stakeholders:** security leadership, compliance teams, auditors, security engineers.

**Exam clue:** “The company must define cloud controls for confidentiality, integrity, availability, and compliance.”

### Operations

**Focus:** operate cloud services at levels that meet business requirements.

Common topics include:

- monitoring and observability;
- incident, problem, and change management;
- service management;
- availability and continuity;
- operational automation and support models.

**Typical stakeholders:** operations leaders, service managers, platform teams, site reliability engineers.

**Exam clue:** “The organization needs processes to monitor, support, and recover cloud services.”

## Business and Technical Grouping

A useful high-level grouping is:

- **Business capabilities:** Business, People, Governance
- **Technical capabilities:** Platform, Security, Operations

This grouping is helpful for memory, but the perspectives interact. Security, for example, needs executive policy, trained people, governance, technical controls, and operational response.

## Transformation Outcomes

CLF-C02 specifically expects awareness of outcomes associated with AWS CAF:

- **Reduced business risk:** improve reliability, security, performance, and decision quality.
- **Improved environmental, social, and governance performance:** use measurement, efficient technology, and transparency to support ESG goals.
- **Increased revenue:** create products, reach customers, and enter markets more quickly.
- **Increased operational efficiency:** automate processes, improve productivity, and reduce avoidable operational effort.

These are outcomes, not guarantees. Achieving them depends on effective transformation and execution.

## Transformation Journey

AWS CAF describes cloud transformation as iterative. A practical simplified flow is:

1. **Envision:** identify business outcomes and transformation opportunities.
2. **Align:** identify capability gaps and dependencies across perspectives.
3. **Launch:** deliver initial initiatives and demonstrate value.
4. **Scale:** expand successful approaches and continuously improve capabilities.

An organization does not need to complete every capability before beginning. It prioritizes the capabilities that are necessary for its current transformation stage and risk profile.

## AWS CAF versus Related Concepts

| Concept | Primary purpose |
|---|---|
| AWS CAF | Organizational cloud readiness and transformation capabilities |
| AWS Well-Architected Framework | Review and improve individual workload architecture |
| AWS Migration Hub | Track migration progress across applications and tools |
| AWS Application Discovery Service | Discover on-premises servers and dependencies |
| AWS Organizations | Centrally manage multiple AWS accounts and organizational policies |
| AWS Prescriptive Guidance | Detailed patterns and recommendations for specific migration and modernization problems |

### Easy memory rule

- **CAF:** is the organization ready and aligned?
- **Well-Architected:** is the workload designed and operated well?
- **Migration Hub:** how is the migration progressing?

## Example: Retail Company Migration

A retail company wants to migrate its online platform to AWS.

- **Business:** defines expected customer and revenue outcomes.
- **People:** trains teams and updates responsibilities.
- **Governance:** establishes budget, risk, and decision policies.
- **Platform:** creates accounts, networking, and delivery foundations.
- **Security:** defines identity, logging, encryption, and incident controls.
- **Operations:** establishes monitoring, support, backup, and recovery procedures.

Migrating servers without addressing these capabilities could create technical progress without organizational readiness.

## CPP Scenario Reasoning

| Scenario | Perspective most directly emphasized |
|---|---|
| Train employees and change team structure | People |
| Align cloud investment with business outcomes | Business |
| Define policies, budgets, and risk ownership | Governance |
| Build accounts, networking, and workload foundations | Platform |
| Establish identity, encryption, and incident controls | Security |
| Define monitoring, support, and recovery processes | Operations |

A scenario can involve more than one perspective. Select the one most directly tied to the stated requirement.

## Common Exam Traps

- AWS CAF is a framework, not a deployable AWS service.
- CAF contains six perspectives, not the six Well-Architected pillars.
- Business, People, and Governance are not “non-cloud” concerns; they are central to successful adoption.
- AWS CAF does not migrate a workload automatically.
- AWS Migration Hub tracks migrations; it does not replace organizational readiness planning.
- The transformation outcomes are goals that cloud-enabled change can support, not automatic results of opening an AWS account.

## Summary

AWS CAF helps organizations approach cloud adoption as a coordinated transformation. Its six perspectives—Business, People, Governance, Platform, Security, and Operations—help stakeholders identify gaps, prioritize capabilities, and pursue reduced risk, increased revenue, operational efficiency, and improved ESG performance.

## Knowledge Check

1. What is the main purpose of AWS CAF?
2. Name the six perspectives.
3. Which perspective focuses most directly on skills and organizational culture?
4. Which perspective focuses most directly on policies, risk, and financial oversight?
5. What is the difference between AWS CAF and the Well-Architected Framework?
6. Name the four transformation outcomes emphasized in CLF-C02.

<details>
<summary>Show answers</summary>

1. To assess cloud readiness, identify capability gaps, align stakeholders, and guide an iterative cloud-transformation roadmap.
2. Business, People, Governance, Platform, Security, and Operations.
3. People.
4. Governance.
5. AWS CAF focuses on organization-wide readiness and transformation; Well-Architected focuses on the quality and trade-offs of workloads.
6. Reduced business risk, improved ESG performance, increased revenue, and increased operational efficiency.

</details>

## References

- [AWS Cloud Adoption Framework](https://aws.amazon.com/cloud-adoption-framework/)
- [Overview of the AWS Cloud Adoption Framework](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/introduction.html)
- [Cloud transformation journey](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/your-cloud-transformation-journey.html)
- [Cloud-powered business outcomes](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/accelerating-business-outcomes.html)
- [CLF-C02 Domain 1: Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html)

Sources checked: **2026-08-01**.
