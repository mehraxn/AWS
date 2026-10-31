# Phase 6 Batch 7 Content Decisions

## AWS-040 — Highly Available Web Application

### Official requirement
Design a multi-tier highly available workload with explicit failure behavior.
### Required CPP depth
Recognize availability, Availability Zones, load balancing, Auto Scaling, and backup versus high availability.
### Required SAA depth
Select Multi-AZ tiers, stateless compute, database failover, zonal egress, health checks, monitoring, and cost trade-offs.
### Canonical target
`13-architecture-and-design-patterns/01-highly-available-web-applications.md`
### Existing files reviewed
Architecture index plus canonical ELB, Auto Scaling, RDS, Route 53, networking, monitoring, and data-protection lessons.
### Official sources used
AWS Reliability Pillar, multi-location guidance, RDS Multi-AZ documentation, and single-Region resilience guidance.
### Gap being resolved
Evidence was scattered across services and did not form a scenario-ready multi-tier pattern.
### CPP content added
Definitions, recognition cues, simple service roles, and availability-versus-backup distinctions.
### SAA architecture content added
Multi-AZ diagram and flow, statelessness, capacity, RDS and NAT decisions, security, monitoring, failure tables, and trade-offs.
### Failure scenarios added
Instance, AZ, database-primary, NAT, deployment, and Regional disruption.
### Trade-offs added
Redundant capacity, cross-AZ transfer, NAT topology, Multi-AZ database cost, and unnecessary Multi-Region complexity.
### Existing content preserved
All service lessons remain canonical owners and are linked rather than copied wholesale.
### Content removed or corrected
No existing lesson text removed; corrected the implied equivalence of Multi-AZ standby and read replica.
### Badge decision
Both badges: fundamental CPP context and scenario-ready SAA design are present.
### Navigation and map updates
Architecture/root navigation, inventory, badge audit, CPP/SAA maps, concept/depth matrices, dashboards, and architecture-quality audit.
### Acceptance-criteria result
Passed: the canonical lesson meets the backlog-specific acceptance criteria.
### Remaining work
None for AWS-040; does not block Batch 8.
### Validation result
Passed: naming, links, duplicate scan, hash, CSV, lesson structure, Mermaid review, and diff checks.

## AWS-041 — Disaster Recovery

### Official requirement
Select among backup/restore, pilot light, warm standby, and active-active using RTO/RPO and cost.
### Required CPP depth
Recognize RTO, RPO, backup, replication, high availability, and relative strategy cost.
### Required SAA depth
Evaluate recovery environment, data behavior, failover, failback, testing, security, monitoring, automation, and complexity.
### Canonical target
`13-architecture-and-design-patterns/02-disaster-recovery-strategies.md`
### Existing files reviewed
Architecture index, AWS Backup, Route 53, RDS, data protection, prior coverage deltas, and audit evidence.
### Official sources used
AWS DR objectives, DR options whitepaper, Reliability Pillar backup guidance, and resilience-testing guidance.
### Gap being resolved
No canonical strategy-selection lesson connected business objectives to recovery execution.
### CPP content added
Clear terminology, RTO/RPO examples, relative strategy table, and common misconceptions.
### SAA architecture content added
Four strategies, failover/failback runbook, backup/replication distinction, security, observability, testing, and trade-offs.
### Failure scenarios added
Regional disruption, data corruption, failed automated health decision, configuration drift, insufficient recovery capacity, and unsafe failback.
### Trade-offs added
Recovery interruption, data loss, steady-state cost, replication, control-plane dependency, and operational complexity.
### Existing content preserved
AWS Backup and service owners remain unchanged and are cross-linked.
### Content removed or corrected
No content removed; corrected treatment of RTO/RPO as guarantees and replication as a backup substitute.
### Badge decision
Both badges are justified by fundamental recognition and scenario-ready selection depth.
### Navigation and map updates
Architecture/root navigation and all directly affected evidence maps and dashboards.
### Acceptance-criteria result
Passed: the canonical lesson meets the backlog-specific acceptance criteria.
### Remaining work
None for AWS-041; does not block Batch 8.
### Validation result
Passed: naming, links, duplicate scan, hash, CSV, lesson structure, and diff checks.

## AWS-042 — Event-Driven Resilience

### Official requirement
Design decoupled failure handling with queues, retries, DLQs, idempotency, orchestration/choreography, and observability.
### Required CPP depth
Recognize SQS, SNS, EventBridge, and Step Functions by purpose.
### Required SAA depth
Select buffering, fanout, routing, workflow, retry, replay, compensation, and backpressure behavior under failure.
### Canonical target
`13-architecture-and-design-patterns/03-event-driven-and-decoupled-systems.md`
### Existing files reviewed
Batch 5 SQS, EventBridge, Step Functions, API Gateway, and service-selection lessons plus architecture and audit maps.
### Official sources used
AWS Reliability Pillar, SQS at-least-once delivery, Serverless Lens failure management, and the AWS messaging decision guide.
### Gap being resolved
Service selection existed, but end-to-end failure isolation and recovery patterns were not scenario-ready in one architecture lesson.
### CPP content added
Service-role recognition and simple decoupling benefits.
### SAA architecture content added
Fanout queues, load levelling, backpressure, bounded retries, jitter, idempotency, DLQs, replay, saga awareness, security, and metrics.
### Failure scenarios added
Consumer outage, poison message, duplicate delivery, burst overload, workflow timeout, and routing defect.
### Trade-offs added
Temporal decoupling versus eventual consistency, replay complexity, component count, requests, logging, and workflow transitions.
### Existing content preserved
Batch 5 canonical service and comparison lessons remain intact and linked.
### Content removed or corrected
No content removed; corrected assumptions that asynchronous delivery is failure-proof or exactly-once end to end.
### Badge decision
Both badges supported by CPP service recognition and SAA failure-handling depth.
### Navigation and map updates
Architecture/root navigation and direct inventory, badge, task, concept, depth, dashboard, and architecture-quality evidence.
### Acceptance-criteria result
Passed: the canonical lesson meets the backlog-specific acceptance criteria.
### Remaining work
None for AWS-042; does not block Batch 8.
### Validation result
Passed: naming, links, duplicate scan, hash, CSV, lesson structure, Mermaid review, and diff checks.

## AWS-043 — Serverless Architecture

### Official requirement
Design a serverless application across API, compute, data, events, security, failure, scaling, and cost.
### Required CPP depth
Recognize API Gateway, Lambda, DynamoDB, and EventBridge and understand customer responsibility.
### Required SAA depth
Select synchronous/asynchronous paths, stateless compute, data access, idempotency, concurrency, invocation-specific failure controls, observability, and deployment recovery.
### Canonical target
`13-architecture-and-design-patterns/04-serverless-application-patterns.md`
### Existing files reviewed
Canonical API Gateway, Lambda, DynamoDB, EventBridge, SQS, Step Functions, monitoring, and security lessons.
### Official sources used
AWS Serverless Applications Lens web-application, foundations, failure-management, and deployment guidance.
### Gap being resolved
Individual service owners existed but did not provide one scenario-ready serverless workload pattern.
### CPP content added
Managed-service roles, pay-for-use concepts, scaling benefits, and retained customer responsibilities.
### SAA architecture content added
Request/data flow, short synchronous paths, durable asynchronous intent, concurrency protection, invocation modes, security, monitoring, deployment, and cost.
### Failure scenarios added
Ambiguous API timeout, asynchronous error, duplicate queue delivery, blocked stream shard, workflow task error, and throttled database write.
### Trade-offs added
Managed operations versus quotas, downstream protection, chatty request cost, retry amplification, and observability volume.
### Existing content preserved
All service-specific lessons remain canonical and are linked.
### Content removed or corrected
No existing content removed; corrected the ideas that managed scaling is unlimited and every Lambda invocation retries identically.
### Badge decision
Both badges supported by explicit CPP and SAA sections.
### Navigation and map updates
Architecture/root navigation and direct certification evidence updates.
### Acceptance-criteria result
Passed: the canonical lesson meets the backlog-specific acceptance criteria.
### Remaining work
None for AWS-043; does not block Batch 8.
### Validation result
Passed: naming, links, duplicate scan, hash, CSV, lesson structure, Mermaid review, and diff checks.
