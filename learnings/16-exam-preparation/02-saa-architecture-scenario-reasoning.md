# AWS Solutions Architect Associate Scenario Reasoning

![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

The SAA-C03 exam emphasizes architecture decisions under security, resilience, performance, and cost constraints. Strong reasoning separates mandatory requirements from preferences, compares viable designs, and rejects options that violate a constraint even when they use valid AWS services.

Every scenario in this guide is original study material. It does not reproduce or reconstruct real exam questions. The official exam guide and in-scope service list were checked on **2026-07-25**; AWS describes the service list as non-exhaustive and subject to change.

## Official Domain Map

| SAA-C03 domain | Weight | Architecture focus | Canonical review |
|---|---:|---|---|
| Design Secure Architectures | 30% | Identity, data protection, network boundaries, and workload security | [Security service selection](../15-comparisons-and-decision-guides/security/01-security-service-selection.md), [multi-account governance](../13-architecture-and-design-patterns/security/02-multi-account-governance.md) |
| Design Resilient Architectures | 26% | Fault isolation, high availability, decoupling, recovery, and disaster recovery | [Highly available web applications](../13-architecture-and-design-patterns/01-highly-available-web-applications.md), [DR strategies](../13-architecture-and-design-patterns/02-disaster-recovery-strategies.md) |
| Design High-Performing Architectures | 24% | Storage, compute, databases, networks, ingestion, and transformation | [Core selection guide](../15-comparisons-and-decision-guides/compute-and-storage/01-core-selection-guide.md), [database selection](../15-comparisons-and-decision-guides/databases/01-database-selection-guide.md), [analytics selection](../15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md) |
| Design Cost-Optimized Architectures | 20% | Right-sized resources, purchasing models, managed services, storage tiers, and transfer paths | [Pricing fundamentals](../12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md), [cost tool selection](../15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md) |

Domain weights describe the official content outline, not a guarantee about a particular exam form.

## Scenario-Decomposition Method

### 1. Extract functional requirements

Write down what the system must do: accept uploads, process orders, survive an Availability Zone failure, serve global users, or retain data.

### 2. Rank nonfunctional constraints

Mark constraints such as:

- recovery point and recovery time objectives;
- latency, throughput, and ordering;
- data residency and encryption;
- operational effort and team skills;
- budget and utilization pattern;
- service quotas and Regional availability.

Words such as **must**, **without**, **least operational overhead**, and **most cost-effective** usually control the decision.

### 3. Draw the smallest useful data flow

Identify source, processing, state, destination, trust boundaries, and failure boundaries. A small data flow exposes missing permissions, single points of failure, and synchronous dependencies.

### 4. Eliminate constraint violations

Reject an option as soon as it violates a mandatory requirement. Do not rescue it by silently adding components that the option did not include.

### 5. Compare the survivors

Evaluate security, resilience, performance, cost, and operational complexity. Select the option that satisfies all mandatory constraints with the best requested optimization.

## Domain 1: Secure Architecture Scenario

### Cross-account access without long-lived keys

A central security account must inspect resources in multiple workload accounts. The organization prohibits copied IAM user credentials and requires centrally auditable access.

**Requirements and constraints**

- Cross-account access is mandatory.
- Long-lived access keys are prohibited.
- Permissions must be least privilege and auditable.

**Decision**

Use an IAM role in each workload account with a trust policy that permits the approved central principal to assume it. Restrict role permissions, log AWS STS and service API activity with CloudTrail, and use organization-level governance where appropriate.

**Eliminate**

- Creating an IAM user in every account introduces long-lived credentials and duplicated identity administration.
- Sharing the root user violates least privilege and removes meaningful separation.
- A security group controls network traffic, not AWS API authorization.

**Trade-offs**

Role assumption requires trust-policy and permission-policy design. Central federation through IAM Identity Center can improve workforce administration, while service roles remain appropriate for workloads.

## Domain 2: Resilient Architecture Scenario

### Order intake during downstream failure

An order API must continue accepting requests when the fulfillment worker is unavailable. Each accepted order must remain available for later processing, and duplicate effects must be controlled.

**Requirements and constraints**

- Remove the synchronous dependency.
- Buffer work durably.
- Recover after worker failure.
- Avoid duplicate business effects.

**Decision**

Place orders in Amazon SQS, scale independent consumers, use a dead-letter queue for repeatedly failing messages, and make fulfillment idempotent. Monitor queue age, depth, failures, and dead-letter traffic.

**Eliminate**

- Calling the worker synchronously makes intake availability depend on the worker.
- Amazon SNS alone provides fan-out but does not replace the consumer-controlled work queue in this requirement.
- Increasing an EC2 instance size does not decouple failure domains.

**Trade-offs**

Asynchronous processing changes the user experience and introduces eventual completion, retry, duplicate, and poison-message handling. That complexity buys failure isolation and independent scaling.

## Domain 3: High-Performing Architecture Scenario

### Multiple consumers with replayable telemetry

Devices continuously produce telemetry. Fraud detection and aggregation consumers must process the same events independently, and a consumer must replay retained records after a deployment failure.

**Requirements and constraints**

- Continuous ingestion and low-latency processing.
- Multiple independent consumers.
- Replay within a configured recovery window.
- Ordering for related device events.

**Decision**

Use Amazon Kinesis Data Streams with a partition key that groups related device events, an appropriate capacity mode, monitored consumer lag, checkpoints, and idempotent processing. Deliver a durable analytical copy to Amazon S3 when long-term retention is required.

**Eliminate**

- Amazon Data Firehose is optimized for buffered managed delivery, not arbitrary independent replayable consumers.
- Amazon SQS is a work queue and does not provide the same multi-consumer stream model.
- A scheduled S3 batch job does not satisfy the continuous low-latency requirement.

**Trade-offs**

Partition-key design affects ordering and hot-shard risk. Longer retention improves recovery options but increases cost. Consumer control adds operational responsibility.

## Domain 4: Cost-Optimized Architecture Scenario

### Fault-tolerant interruptible batch processing

A nightly transformation processes objects from Amazon S3. Tasks are stateless, checkpointed, restartable, and can finish within a broad overnight window.

**Requirements and constraints**

- Minimize compute cost.
- Interruptions are acceptable.
- Failed work must resume safely.
- Data remains durable independently of compute.

**Decision**

Use interruptible discounted capacity such as EC2 Spot Instances through a managed scaling or batch-processing design, while keeping input and checkpoints in durable storage. Diversify allowed capacity where appropriate and monitor job completion.

**Eliminate**

- Dedicated Hosts address tenancy or licensing requirements, not the stated lowest-cost interruptible workload.
- A continuously running On-Demand fleet pays for idle time outside the batch window.
- Reserved capacity can help predictable steady usage, but the scenario explicitly tolerates interruption and requires the lowest suitable compute cost.

**Trade-offs**

Spot capacity can be interrupted or unavailable. The application must checkpoint, retry, and avoid local-only state. On-Demand capacity may be mixed in when completion certainty outweighs additional cost.

## Cross-Domain Scenario: Global Stateful Application

A customer-facing application needs low-latency global reads, controlled writes, encryption, Regional failure planning, and bounded cost.

Break the problem into decisions rather than searching for one service:

1. **Entry and routing:** choose DNS or global networking based on protocol, health checks, and failover behavior.
2. **Compute:** use Regional multi-AZ capacity and stateless application tiers where possible.
3. **State:** select a database replication model that matches write topology, consistency, failover, and recovery requirements.
4. **Security:** protect identities, secrets, network paths, edge traffic, and encryption keys.
5. **Recovery:** define detection, promotion, data-loss tolerance, and rollback; multi-Region deployment alone is not a tested recovery plan.
6. **Cost:** account for duplicated capacity, cross-Region transfer, storage, observability, and recovery testing.

The correct architecture depends on explicit constraints. “Use multiple Regions” is not sufficient without data, routing, security, and operational decisions.

## Common Option-Elimination Traps

- **Valid service, wrong requirement:** a service may be real but solve a different storage, messaging, or analytics problem.
- **Managed means responsibility-free:** customers still configure identity, data, recovery, monitoring, and application behavior.
- **Multi-AZ versus read scaling:** a standby can improve availability without serving application reads.
- **Backup versus high availability:** backups recover data; they do not keep an application serving during failure.
- **Encryption without authorization:** encryption does not replace least-privilege access.
- **Serverless means always cheapest:** usage shape, data transfer, storage, and supporting services determine cost.
- **One optimization overrides a must-have:** “lowest cost” never permits violating a mandatory security or recovery constraint.

## Review Checklist

Before selecting an answer, confirm:

- every mandatory requirement is satisfied;
- identity, encryption, and network boundaries are addressed;
- failure behavior and recovery are explicit;
- scaling matches state and traffic patterns;
- monitoring detects the important failure mode;
- cost includes storage and data transfer, not only compute;
- rejected options have a concrete constraint violation;
- no unstated guarantee or feature was assumed.

## Exam-Preparation Integrity

- Use official guides and original scenarios.
- Do not collect, share, or reconstruct live exam questions.
- Memorized answer letters do not teach architecture reasoning.
- Treat service features, quotas, and availability as changeable; verify current documentation for real designs.

## Knowledge Check

1. **Why should mandatory constraints be separated from preferences?**  
   **Answer:** An option that violates a mandatory requirement is invalid even if it optimizes a preferred quality such as cost.
2. **What is the first failure question for a synchronous dependency?**  
   **Answer:** Ask what happens to the caller when the downstream component is slow or unavailable; then consider decoupling, timeouts, retries, and idempotency.
3. **Why is a backup not equivalent to high availability?**  
   **Answer:** A backup supports restoration after loss, while high availability keeps service operating or fails over during component failure.
4. **When is a serverless option not automatically the answer?**  
   **Answer:** When its service behavior, latency, quotas, cost profile, networking, or operational constraints do not meet the workload requirements.
5. **What makes an option-elimination explanation useful?**  
   **Answer:** It identifies the exact requirement or constraint the rejected design fails instead of relying on vague preference.

## References

Checked **2026-07-25**.

- [AWS Certified Solutions Architect – Associate SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html)
- [SAA-C03 in-scope AWS services and features](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html)
- [AWS Certification exam preparation](https://aws.amazon.com/certification/certification-prep/)
