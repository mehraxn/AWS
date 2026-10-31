# Phase 6 Batch 7 Fact Corrections

## Correction

Affected path: `13-architecture-and-design-patterns/01-highly-available-web-applications.md`

Related backlog ID: AWS-040

Previous claim: The repository lacked a canonical explanation of complete Multi-AZ failure domains and could leave an RDS Multi-AZ standby confused with read scaling.

Corrected claim: Multi-AZ resilience requires viable paths for each critical tier. An RDS Multi-AZ DB instance standby supports high availability and does not serve read traffic; read replicas or an appropriate cluster design serve read-scaling requirements.

Reason: Availability and scaling use different database mechanisms, and a nominal two-AZ compute tier can retain a zonal database or egress dependency.

Official source: AWS Reliability Pillar multi-location guidance and RDS Multi-AZ DB instance documentation.

Date checked: 2026-07-24

Severity: high

## Correction

Affected path: `13-architecture-and-design-patterns/02-disaster-recovery-strategies.md`

Related backlog ID: AWS-041

Previous claim: RTO, RPO, high availability, replication, backup, and DR lacked one authoritative distinction.

Corrected claim: RTO and RPO are organization-defined objectives, not AWS guarantees. Multi-AZ high availability is not a complete Regional DR strategy, and replication does not replace point-in-time backup and tested restoration.

Reason: Each control addresses different interruption and data-loss failure modes.

Official source: AWS Reliability Pillar DR objectives and Disaster Recovery Options in the Cloud.

Date checked: 2026-07-24

Severity: high

## Correction

Affected path: `13-architecture-and-design-patterns/03-event-driven-and-decoupled-systems.md`

Related backlog ID: AWS-042

Previous claim: Existing service lessons did not clearly connect at-least-once delivery, idempotency, bounded retry, and DLQ recovery.

Corrected claim: Standard SQS delivery can produce duplicates, so consumers must be idempotent. A DLQ isolates repeatedly failing work but does not repair or safely replay it automatically.

Reason: Prevents duplicate business effects and abandoned poison messages.

Official source: Amazon SQS at-least-once delivery and AWS Serverless Applications Lens failure management.

Date checked: 2026-07-24

Severity: high

## Correction

Affected path: `13-architecture-and-design-patterns/04-serverless-application-patterns.md`

Related backlog ID: AWS-043

Previous claim: Cross-service serverless failure behavior and quota responsibility were incomplete.

Corrected claim: Synchronous, asynchronous, queue, stream, and workflow integrations have distinct failure behavior. Managed scaling remains subject to quotas and downstream capacity, and API keys are not a substitute for user authorization.

Reason: Architecture must apply the controls for the actual invocation path and protect downstream systems.

Official source: AWS Serverless Applications Lens foundations and failure-management guidance.

Date checked: 2026-07-24

Severity: high
