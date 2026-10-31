# Cloud Migration Journey and the 7 Rs

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Cloud migration is the planned movement or transformation of applications, data, and infrastructure into the AWS Cloud. A successful migration begins with business outcomes, application dependencies, security requirements, downtime tolerance, data volume, and operating readiness—not with selecting a migration tool at random.

This lesson covers the migration journey and the seven common migration strategies. Continue with [Migration Service Selection](07-migration-service-selection.md) to choose between discovery, application, database, file, and offline-transfer services.

## Why Organizations Migrate

Common goals include:

- reducing data-center ownership and refresh work;
- improving agility and deployment speed;
- increasing elasticity and global reach;
- improving resilience and recovery capabilities;
- using managed and cloud-native services;
- improving security visibility and automation;
- modernizing applications and data platforms;
- changing the cost and licensing model;
- exiting a facility or responding to a hardware deadline.

A migration should have measurable outcomes. “Move to the cloud” is not specific enough to guide architecture or determine whether the migration succeeded.

## Three High-Level Migration Phases

AWS commonly organizes a large migration into three phases.

### 1. Assess

Build the business case and understand the current environment.

Typical activities include:

- inventory applications, servers, databases, and dependencies;
- assess cloud readiness;
- identify owners, business criticality, and compliance needs;
- estimate cost and migration value;
- identify initial migration strategies;
- prioritize applications and define success measures.

**Output:** an initial business case, portfolio view, readiness findings, and migration direction.

### 2. Mobilize

Prepare the organization and AWS environment for migration at scale.

Typical activities include:

- build foundational accounts, identity, networking, logging, and security controls;
- define governance and the operating model;
- create migration tooling and repeatable processes;
- train teams and assign responsibilities;
- resolve capability gaps;
- run pilot migrations and refine the plan.

**Output:** a prepared organization, landing-zone foundation, migration factory or repeatable process, and validated experience.

### 3. Migrate and Modernize

Move workloads in planned waves, validate them, cut over users, and improve them where justified.

Typical activities include:

- replicate and transfer applications and data;
- test functionality, security, performance, and recovery;
- perform cutover and rollback planning;
- monitor migrated workloads;
- decommission replaced resources after validation;
- modernize applications when business value justifies it.

**Output:** migrated workloads that meet agreed requirements and an improvement path for modernization and optimization.

The phases are not merely technical steps. Business, people, governance, platform, security, and operations readiness remain important throughout the journey.

## The 7 Rs of Migration

The 7 Rs classify the strategy for each application or workload.

| Strategy | Meaning | Typical use |
|---|---|---|
| Rehost | Move the application with minimal or no application change. Often called “lift and shift.” | Fast migration, data-center exit, or modernization planned later |
| Relocate | Move a workload or platform without changing its overall architecture or purchasing new hardware. | Moving compatible virtualized environments or AWS resources between locations/accounts |
| Replatform | Make limited changes to use a more suitable platform without redesigning the whole application. | Move a self-managed database to Amazon RDS or a runtime to a managed platform |
| Refactor or re-architect | Redesign the application to use cloud-native patterns and services. | Strong need for agility, scale, resilience, or modernization |
| Repurchase | Replace the existing application with another product, commonly SaaS. | Replace an owned application with a vendor-managed alternative |
| Retain | Keep the application in the current environment for now. | Compliance, unresolved dependencies, specialized hardware, low migration value, or timing constraints |
| Retire | Decommission the application because it is no longer needed. | Remove duplicate, unused, unsupported, or low-value systems |

## Strategy Details and Trade-Offs

### Rehost

**Change level:** low

**Advantages:**

- can move workloads quickly;
- reduces immediate redesign effort;
- useful for facility-exit deadlines;
- creates a starting point for later optimization.

**Trade-offs:**

- preserves many legacy limitations;
- might not use managed or elastic services;
- can reproduce inefficient capacity and licensing choices;
- does not automatically improve application availability.

### Relocate

**Change level:** low

**Advantages:**

- minimizes application and operating-model changes;
- can move compatible environments quickly;
- useful when the platform itself can be transferred.

**Trade-offs:**

- cloud-native benefits may remain limited;
- compatibility and target-platform constraints must be verified.

### Replatform

**Change level:** low to moderate

**Advantages:**

- reduces operational burden without a full rewrite;
- can improve availability, patching, scaling, or cost;
- often provides faster value than refactoring.

**Trade-offs:**

- requires testing application and platform compatibility;
- managed-service constraints may require configuration or code changes;
- migration is more involved than a direct rehost.

### Refactor or re-architect

**Change level:** high

**Advantages:**

- can maximize elasticity, resilience, agility, and managed-service use;
- removes architectural constraints that block business goals;
- can improve long-term delivery and scalability.

**Trade-offs:**

- highest complexity, cost, testing effort, and migration risk;
- takes more time;
- should be driven by a clear business requirement rather than modernization for its own sake.

### Repurchase

**Change level:** replaces the application

**Advantages:**

- removes infrastructure and application maintenance;
- can provide modern features quickly;
- changes spending toward a subscription or service model.

**Trade-offs:**

- requires data migration, integration, identity setup, and user training;
- introduces vendor constraints and subscription costs;
- existing workflows may need to change.

### Retain

**Change level:** none for now

Retain is a valid decision when migration risk or effort exceeds current value. It should be documented with an owner, reason, dependencies, and review date so that “temporary” does not become an unmanaged permanent state.

### Retire

**Change level:** remove the system

Retiring workloads can reduce cost, risk, attack surface, and migration scope. Confirm data-retention, legal, audit, and dependency requirements before shutdown.

## Choosing a Migration Strategy

Ask these questions for each workload:

1. Is the application still required?
2. Does it provide enough value to migrate?
3. Are there legal, residency, hardware, or dependency constraints?
4. Is there a fixed data-center exit deadline?
5. How much downtime is acceptable?
6. What are the current pain points: cost, scale, reliability, delivery speed, or operations?
7. Does a suitable SaaS replacement exist?
8. Can limited platform changes deliver most of the required benefit?
9. Is a full redesign justified by measurable business outcomes?
10. How will the team test, cut over, roll back, operate, and optimize the workload?

## Example Portfolio

| Workload | Requirement | Likely strategy |
|---|---|---|
| Old reporting tool with no active users | Remove maintenance and risk | Retire |
| Manufacturing control system tied to specialized local hardware | No cloud equivalent yet | Retain |
| Standard virtual machine with a facility-exit deadline | Move quickly with minimal change | Rehost |
| VMware-based environment supported by a compatible target platform | Move platform without application redesign | Relocate |
| Database on a VM where the team wants AWS to operate the database platform | Reduce administration with limited changes | Replatform |
| Legacy CRM with a suitable SaaS replacement | Avoid maintaining the application | Repurchase |
| Monolith cannot meet release-speed and scaling requirements | Redesign around measurable business needs | Refactor or re-architect |

## Migration Wave Planning

Large migrations are usually divided into waves rather than moving everything at once.

A wave plan should consider:

- application dependencies;
- business criticality;
- migration strategy;
- team and tool capacity;
- maintenance windows;
- data volume and replication time;
- security and compliance validation;
- rollback options;
- learning from earlier waves.

Begin with representative but manageable workloads. The purpose of a pilot is to validate assumptions and improve the migration process, not merely to claim that one server was moved.

## CPP Knowledge

For Cloud Practitioner:

- recognize the purpose of assess, mobilize, and migrate and modernize;
- distinguish the 7 Rs from migration services;
- identify that rehost means minimal change;
- recognize replatform as limited optimization;
- recognize refactor as significant redesign;
- understand that retain and retire can be correct strategies;
- connect AWS CAF to organizational readiness and migration planning.

## SAA Architecture and Design

For SAA, also evaluate:

- dependency discovery and network connectivity;
- data consistency and replication method;
- downtime and cutover requirements;
- target availability and recovery design;
- security controls before data transfer begins;
- service quotas, performance testing, and capacity behavior;
- rollback and validation plans;
- licensing and platform compatibility;
- post-migration observability and cost optimization.

A migration is not complete when data arrives. The target workload must meet functional, security, performance, reliability, operational, and recovery requirements.

## Common Exam Traps

- Rehost and replatform are not the same. Replatform includes purposeful platform optimization.
- Refactor is not always the best strategy; it is the most complex and must be justified.
- Retain is a deliberate strategy, not necessarily a failed migration.
- Retire requires dependency and retention checks before shutdown.
- AWS CAF guides readiness; it is not one of the 7 Rs.
- AWS Migration Hub tracks progress; it does not choose the business strategy automatically.
- Migration does not automatically modernize, secure, or rightsize the workload.

## Summary

AWS migration planning moves from assessment, through organizational and platform preparation, into controlled migration and modernization. The 7 Rs provide a strategy for each workload: rehost, relocate, replatform, refactor, repurchase, retain, or retire. The correct strategy depends on business value, constraints, required change, risk, time, and operational outcomes.

## Knowledge Check

1. What are the three high-level migration phases?
2. Which strategy is commonly called lift and shift?
3. What is the difference between rehost and replatform?
4. Which strategy replaces an existing application with another product such as SaaS?
5. Why can retain be a correct decision?
6. Which strategy normally has the greatest redesign effort?
7. Why should applications be grouped into migration waves?

<details>
<summary>Show answers</summary>

1. Assess, Mobilize, and Migrate and Modernize.
2. Rehost.
3. Rehost moves with minimal change; replatform makes limited changes to use a more suitable platform or managed service.
4. Repurchase.
5. Compliance, dependencies, hardware, timing, risk, or low migration value can justify keeping the workload in its current environment for now.
6. Refactor or re-architect.
7. To manage dependencies, risk, team capacity, testing, cutover, and learning in controlled groups.

</details>

## References

- [Phases of a large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/phases.html)
- [About the migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html)
- [AWS migration strategy overview](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/overview.html)
- [CLF-C02 Domain 1: Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html)

Sources checked: **2026-08-01**.
