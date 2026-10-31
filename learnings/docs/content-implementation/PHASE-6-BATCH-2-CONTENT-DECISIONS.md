# Phase 6 Batch 2 Content Decisions

Recovery review date: **2026-07-23**. Official lesson references were checked during the original implementation on **2026-07-22**. The Phase 5 backlog and batch plan remain authoritative.

## Reconciliation Method

Each Batch 2 row was compared with its canonical target, depth requirements, acceptance criteria, pre-implementation checksum, dated official references, navigation, and Git evidence from commit `6f9540d`. Existing implementation was recorded without lesson rewrites.

## AWS-007 — Amazon EC2

### Official requirement
EC2 families, sizing, lifecycle, storage/networking, high availability, security, cost, and selection at fundamental CPP and scenario-ready SAA depth.

### Canonical target
`04-compute/amazon-ec2/01-overview.md`

### Existing files reviewed
The canonical overview, compute index, pre-implementation manifest, Phase 5 backlog, and commit `6f9540d`.

### Evidence of earlier implementation
`SAA Design Supplement`, instance-family table, lifecycle and AMI guidance, security/shared-responsibility decisions, purchasing trade-offs, knowledge check, and official references.

### Official sources used
Amazon EC2 User Guide pages for concepts, instance types, AMIs, and purchasing options.

### Gap originally identified
The existing CPP-oriented overview lacked scenario-ready EC2 architecture and selection depth.

### Recovery assessment
Completed before recovery; records-only reconciliation.

### CPP content status
Fundamental recognition and shared-responsibility coverage complete.

### SAA content status
Architecture, availability, sizing, security, and cost trade-offs complete for this backlog criterion.

### Existing content preserved
All earlier beginner-focused explanations and comparisons remain.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Linked from the core selection guide; design signals and knowledge checks are present.

### Badge decision
CPP and SAA badges are supported by the implemented depths.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-007.

### Validation result
Passed in the final recovery validation run.

## AWS-008 — Elastic Load Balancing

### Official requirement
ALB, NLB, and GWLB selection; health, cross-zone behavior, TLS, high availability, and cost at scenario-ready SAA depth.

### Canonical target
`04-compute/elastic-load-balancing/01-overview.md`

### Existing files reviewed
The canonical ELB lesson, compute index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
Type-selection table, listener and target-group concepts, health checks, multi-AZ design, TLS, cost factors, SAA decisions, traps, questions, and references.

### Official sources used
Elastic Load Balancing, Network Load Balancer, and Gateway Load Balancer documentation.

### Gap originally identified
No canonical scenario-ready ELB lesson.

### Recovery assessment
Created before recovery; records-only reconciliation.

### CPP content status
Awareness and recognition coverage complete.

### SAA content status
Scenario-ready selection and resilience coverage complete.

### Existing content preserved
No prior target existed; related compute content was not duplicated or removed.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Decision table, design bullets, traps, and explained questions are present.

### Badge decision
CPP awareness and SAA architecture support both badges.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-008.

### Validation result
Passed in the final recovery validation run.

## AWS-009 — EC2 Auto Scaling

### Official requirement
Target tracking, step and scheduled scaling, health, capacity, and trade-offs.

### Canonical target
`04-compute/ec2-auto-scaling/01-target-tracking-scaling.md`

### Existing files reviewed
The canonical lesson, compute index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
The `Auto Scaling Group Design Supplement` covers launch templates, capacity bounds, health, warmup, Multi-AZ design, policy selection, failure behavior, cost, and knowledge checks.

### Official sources used
EC2 Auto Scaling launch-template, policy, health-check, and warmup documentation.

### Gap originally identified
Target-tracking prose lacked complete Auto Scaling group architecture depth.

### Recovery assessment
Completed before recovery; records-only reconciliation.

### CPP content status
Fundamental scaling-policy recognition complete.

### SAA content status
Scenario-ready capacity, resilience, metric, and policy decisions complete.

### Existing content preserved
The original target-tracking study note remains intact.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Policy comparisons, scenarios, traps, and knowledge checks are present.

### Badge decision
Both badges remain justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-009.

### Validation result
Passed in the final recovery validation run.

## AWS-010 — AWS Lambda

### Official requirement
Invocation, scaling and limits concepts, integrations, security, failure, and cost.

### Canonical target
`04-compute/aws-lambda/01-overview.md`

### Existing files reviewed
The Lambda overview, compute index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
The `Invocation and Architecture Supplement` addresses synchronous, asynchronous, and poll-based invocation; concurrency; retries and dead-letter/failure destinations; IAM; VPC implications; cost; and knowledge checks.

### Official sources used
AWS Lambda Developer Guide pages for invocation, scaling, retries, networking, and pricing concepts.

### Gap originally identified
The existing lesson was not deep enough for SAA design decisions.

### Recovery assessment
Completed before recovery; records-only reconciliation.

### CPP content status
Fundamental serverless and event-driven recognition complete.

### SAA content status
Invocation, failure, scaling, security, and cost decisions complete.

### Existing content preserved
The beginner-focused Lambda lesson remains intact.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Service comparisons, architecture patterns, traps, and questions are present.

### Badge decision
Both badges remain justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-010.

### Validation result
Passed in the final recovery validation run.

## AWS-011 — Containers

### Official requirement
ECS, EKS, Fargate, ECR, EC2 capacity, selection, scaling, operations, and cost.

### Canonical target
`04-compute/containers/01-ecs-eks-and-fargate.md`

### Existing files reviewed
The canonical containers lesson, compute index, related Fargate note, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
Service table, task/pod/image concepts, EC2-versus-Fargate comparison, scaling and availability, security, CPP recognition, SAA selection, traps, questions, and references.

### Official sources used
AWS container decision guide and ECS, EKS, Fargate, and ECR documentation.

### Gap originally identified
No unified canonical container-service selection lesson.

### Recovery assessment
Created before recovery; records-only reconciliation.

### CPP content status
Awareness and service recognition complete.

### SAA content status
Architecture-and-design selection and operations trade-offs complete.

### Existing content preserved
Related service-specific notes remain as supporting content.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Capacity decision table, SAA choices, traps, and explained questions are present.

### Badge decision
Both badges are justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-011.

### Validation result
Passed in the final recovery validation run.

## AWS-012 — Amazon S3

### Official requirement
Durability, availability, security, versioning, replication, events, performance, and cost.

### Canonical target
`05-storage/amazon-s3/01-overview.md`

### Existing files reviewed
The S3 overview and supporting S3 lessons, storage index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
The `SAA Security and Resilience Supplement` covers object design, security controls, versioning, replication, events, performance, cost, scenarios, knowledge checks, and references.

### Official sources used
Amazon S3 User Guide pages for durability, consistency, security, versioning, replication, events, and performance.

### Gap originally identified
The canonical overview lacked scenario-ready S3 architecture depth.

### Recovery assessment
Completed before recovery; records-only reconciliation.

### CPP content status
Fundamental object-storage and storage-class recognition complete.

### SAA content status
Security, resilience, performance, event, and cost trade-offs complete.

### Existing content preserved
All earlier S3 explanations and distinct source material remain.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Service comparisons, scenarios, traps, and checks are present.

### Badge decision
Both badges remain justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-012.

### Validation result
Passed in the final recovery validation run.

## AWS-013 — Amazon EBS

### Official requirement
Volume types, IOPS and throughput, snapshots, encryption, AZ scope, and cost.

### Canonical target
`05-storage/amazon-ebs/01-overview.md`

### Existing files reviewed
The EBS overview, storage index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
Volume-family selection and the `SAA Performance and Recovery Supplement` address performance, snapshots, encryption, AZ scope, availability, cost, scenarios, and checks.

### Official sources used
Amazon EBS User Guide pages for volume types, snapshots, encryption, and availability.

### Gap originally identified
Incomplete architecture-and-design treatment of block-storage performance and recovery.

### Recovery assessment
Completed before recovery; records-only reconciliation.

### CPP content status
Fundamental persistent block-storage recognition complete.

### SAA content status
Architecture, performance, recovery, encryption, and cost decisions complete.

### Existing content preserved
The detailed beginner-friendly EBS material remains.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
EBS comparisons, design scenarios, traps, and questions are present.

### Badge decision
Both badges remain justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-013.

### Validation result
Passed in the final recovery validation run.

## AWS-014 — EC2 Instance Store

### Official requirement
Ephemeral behavior, performance, failure, suitable data, and EBS comparison.

### Canonical target
`05-storage/ec2-instance-store/01-overview.md`

### Existing files reviewed
The instance-store overview, storage index, EBS comparison material, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
The `Failure and Design Supplement` explains stop, hibernate, terminate, and host-failure behavior, suitable recoverable data, replication responsibility, EBS decisions, and checks.

### Official sources used
Amazon EC2 instance-store documentation.

### Gap originally identified
Failure and architecture implications were incomplete.

### Recovery assessment
Completed before recovery; records-only reconciliation.

### CPP content status
Fundamental ephemeral-storage recognition complete.

### SAA content status
Failure, performance, recovery, and alternative-selection coverage complete.

### Existing content preserved
The original study note remains intact.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Direct EBS comparison, traps, and knowledge checks are present.

### Badge decision
Both badges remain justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-014.

### Validation result
Passed in the final recovery validation run.

## AWS-015 — Amazon EFS

### Official requirement
Regional design, mount targets, performance, lifecycle, security, and cost.

### Canonical target
`05-storage/amazon-efs/01-overview.md`

### Existing files reviewed
The EFS overview, storage index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
The `SAA File-System Design Supplement` covers Regional and One Zone choices, mount targets, NFS, throughput and performance, lifecycle, security, cost, scenarios, and checks.

### Official sources used
Amazon EFS User Guide pages for availability, mount targets, performance, lifecycle, and security.

### Gap originally identified
Shared-file-system architecture depth was insufficient.

### Recovery assessment
Completed before recovery; records-only reconciliation.

### CPP content status
Fundamental shared-file-storage recognition complete.

### SAA content status
Architecture, availability, performance, security, and cost decisions complete.

### Existing content preserved
The earlier EFS explanation remains intact.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
EBS, S3, and FSx comparisons plus design checks are present.

### Badge decision
Both badges remain justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-015.

### Validation result
Passed in the final recovery validation run.

## AWS-016 — Amazon FSx

### Official requirement
FSx families, protocols, performance, high availability, integration, and selection.

### Canonical target
`05-storage/amazon-fsx/01-family-and-selection.md`

### Existing files reviewed
The FSx family lesson, existing Lustre and Windows lessons, storage index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
Family-selection table, availability/performance/integration discussion, security, cost optimization, CPP recognition, SAA decisions, traps, questions, and references.

### Official sources used
Amazon FSx family and file-system documentation.

### Gap originally identified
No single decision-focused FSx family owner.

### Recovery assessment
Created before recovery; records-only reconciliation.

### CPP content status
Family awareness and recognition complete.

### SAA content status
Architecture-and-design selection coverage complete.

### Existing content preserved
Service-specific FSx lessons remain as supporting notes.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Family decision table, scenario guidance, traps, and questions are present.

### Badge decision
Both badges are justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-016.

### Validation result
Passed in the final recovery validation run.

## AWS-017 — AWS Storage Gateway

### Official requirement
File, Volume, and Tape Gateway; cache, recovery, connectivity, selection, and cost.

### Canonical target
`05-storage/aws-storage-gateway/01-overview.md`

### Existing files reviewed
The overview and gateway-specific lessons, storage index, storage comparisons, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
Gateway-type explanation and `Current Gateway Selection Supplement` cover S3/FSx File Gateway, cached/stored Volume modes, Tape Gateway, connectivity, recovery, shared responsibility, cost, and checks.

### Official sources used
AWS Storage Gateway User Guide pages for S3 File, Volume, and Tape Gateway.

### Gap originally identified
Gateway-mode selection and hybrid-design depth were incomplete.

### Recovery assessment
Completed before recovery; records-only reconciliation.

### CPP content status
Fundamental hybrid-storage recognition complete.

### SAA content status
Architecture, connectivity, recovery, and cost selection complete.

### Existing content preserved
All earlier overview and gateway-specific notes remain.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Service comparisons, hybrid scenarios, traps, and checks are present.

### Badge decision
Both badges remain justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-017.

### Validation result
Passed in the final recovery validation run.

## AWS-018 — AWS Backup

### Official requirement
Plans, vaults, policies, cross-account and cross-Region copies, restore, and cost.

### Canonical target
`05-storage/aws-backup/01-overview.md`

### Existing files reviewed
The AWS Backup lesson, storage index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
Plans, assignments, vaults, copy actions, Vault Lock, restore testing, backup-versus-replication decisions, security, resilience, cost, scenarios, and references.

### Official sources used
AWS Backup Developer Guide pages for plans, cross-account copies, Vault Lock, and restore testing.

### Gap originally identified
No canonical centralized backup-and-restore lesson.

### Recovery assessment
Created before recovery; records-only reconciliation.

### CPP content status
Fundamental centralized-backup recognition complete.

### SAA content status
Architecture, isolation, recovery, governance, and cost decisions complete.

### Existing content preserved
Related service-native snapshot lessons were not changed.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Backup, snapshot, replication, and recovery distinctions plus questions are present.

### Badge decision
Both badges are justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-018.

### Validation result
Passed in the final recovery validation run.

## AWS-019 — Core Compute and Storage Selection

### Official requirement
Decision tables for EC2, Lambda, containers, S3, EBS, EFS, and instance store at fundamental CPP and scenario-ready SAA depth.

### Canonical target
`15-comparisons-and-decision-guides/compute-and-storage/01-core-selection-guide.md`

### Existing files reviewed
The selection guide, all linked canonical lessons, comparison index, pre-manifest, backlog, and commit `6f9540d`.

### Evidence of earlier implementation
Compute and storage decision tables, selection sequence, CPP recognition, SAA scenario patterns, traps, canonical links, checks, and official decision-guide references.

### Official sources used
AWS compute, storage, and containers decision guides.

### Gap originally identified
No unified core compute-and-storage decision guide.

### Recovery assessment
Created before recovery; records-only reconciliation.

### CPP content status
Fundamental recognition comparisons complete.

### SAA content status
Scenario-ready selection and trade-off coverage complete.

### Existing content preserved
Canonical service lessons remain the detailed owners; the guide avoids duplicating them.

### Content added during recovery
None.

### Content corrected during recovery
None.

### Comparison or scenarios status
Both required decision tables and scenario patterns are present and linked.

### Badge decision
Both badges are justified.

### Final acceptance-criteria result
Passed.

### Remaining work
None for AWS-019.

### Validation result
Passed in the final recovery validation run.
