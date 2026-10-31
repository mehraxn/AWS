# Phase 6 Batch 1 Content Decisions

Sources were checked on **2026-07-22**. Existing canonical content was read before expansion and retained unless a verified current term replaced an outdated active term.

## AWS-001

### Official requirement

Teach responsibility allocation and how it changes across service models.

### Canonical target

`01-cloud-fundamentals/01-shared-responsibility-model.md`

### Existing files reviewed

Cloud-fundamentals index, Phase 5 concept matrix, and existing EC2, RDS, Lambda, and S3 references identified by the audit.

### Official sources used

AWS Shared Responsibility Model, Well-Architected Security Pillar, CLF-C02 guide, and SAA-C03 guide.

### Gap being resolved

No canonical foundation lesson distinguished security of and in the cloud with service-model comparisons.

### CPP content added

Definitions, responsibility recognition, common scenarios, traps, and a knowledge check.

### SAA content added

EC2, RDS, Lambda, and S3 responsibility boundaries; operational-burden and control implications.

### Existing content preserved

Existing service lessons remain canonical for service-specific detail and are not duplicated or rewritten.

### Content removed or corrected

None.

### Badge decision

CPP and SAA: both required depths are present.

### Remaining work

Later service batches may deepen service-specific implementation without replacing this owner.

### Validation result

Acceptance criterion satisfied.

## AWS-002

### Official requirement

Teach the AWS Cloud value proposition and Cloud Concepts Task 1.1.

### Canonical target

`01-cloud-fundamentals/02-cloud-concepts-and-benefits.md`

### Existing files reviewed

Cloud-fundamentals index, Phase 5 CPP baseline, task map, and concept/depth matrices.

### Official sources used

CLF-C02 Domain 1, AWS cloud-value guidance, and Well-Architected definitions.

### Gap being resolved

Cloud benefits and economics were dispersed or mention-only rather than beginner-ready.

### CPP content added

Agility, elasticity, scalability, availability, fault tolerance, global reach, economies of scale, CapEx/OpEx, fixed/variable cost, service models, deployment models, scenarios, and a knowledge check.

### SAA content added

Foundation-level distinctions and cross-reference to responsibility ownership; no later-batch architecture was introduced.

### Existing content preserved

Billing and architecture lessons retain their specialized ownership.

### Content removed or corrected

None.

### Badge decision

CPP only, matching the backlog's certification assignment and implemented depth.

### Remaining work

Service-specific cost and architecture treatment remains in later batches.

### Validation result

Acceptance criterion satisfied.

## AWS-003

### Official requirement

Teach Regions, Availability Zones, edge infrastructure, service scope, availability, and Region-selection trade-offs.

### Canonical target

`02-global-infrastructure/01-regions-availability-zones-and-edge.md`

### Existing files reviewed

Global-infrastructure index, Local Zones and Wavelength lessons, and Phase 5 maps.

### Official sources used

AWS Regions and Availability Zones guide, AWS fault-isolation guidance, CloudFront documentation, and both exam guides.

### Gap being resolved

The category lacked a canonical Regions/AZs/edge foundation and Multi-AZ/Multi-Region decision treatment.

### CPP content added

Definitions, Region factors, scope recognition, scenarios, traps, and a knowledge check.

### SAA content added

Failure boundaries, Multi-AZ versus Multi-Region, edge delivery, zonal dependencies, RTO/RPO context, and trade-offs.

### Existing content preserved

Local Zones and Wavelength lessons remain intact and are summarized only for awareness.

### Content removed or corrected

None.

### Badge decision

CPP and SAA: both required depths are present.

### Remaining work

Detailed networking and recovery designs remain in Batches 3 and 7.

### Validation result

Acceptance criterion satisfied.

## AWS-004

### Official requirement

Raise the IAM overview from awareness to CPP fundamentals and SAA identity-design depth.

### Canonical target

`03-identity-governance-and-organizations/aws-iam/01-overview.md`

### Existing files reviewed

The complete overview, IAM lesson sequence, IAM Identity Center, Organizations, SCP, and root-user notes.

### Official sources used

IAM User Guide, IAM best practices, root-user guidance, policy evaluation, permissions boundaries, temporary credentials, Organizations SCPs, and both exam guides.

### Gap being resolved

The overview lacked managed/inline and identity/resource policy distinctions, boundaries, complete evaluation logic, STS, federation, cross-account decision guidance, and SCP behavior.

### CPP content added

Root/MFA reinforcement, policy distinctions, explicit deny, temporary credentials, Identity Center, SCP recognition, traps, and a knowledge check.

### SAA content added

Policy-intersection reasoning, cross-account roles, delegated permissions, workforce/workload identity choices, and governance scenarios.

### Existing content preserved

SHA-256 before change: `bdec17759a6fe0039a3ae50ed924aa993d2c324ad375c83953d59c5c9c1ad8f9`. The original beginner explanation, examples, comparisons, summary, and memory aids remain.

### Content removed or corrected

None; missing current guidance was added in place.

### Badge decision

CPP and SAA, justified by the expanded body and official scope.

### Remaining work

Focused IAM sublessons can be re-audited later; no repository-wide badge pass was performed.

### Validation result

Acceptance criterion satisfied.

## AWS-005

### Official requirement

Teach all six pillars, trade-offs, review process, and architecture scenarios.

### Canonical target

`13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md`

### Existing files reviewed

The complete overview, architecture category index, Phase 5 depth matrix, and Well-Architected quality findings.

### Official sources used

AWS Well-Architected Framework definitions, review process, Tool guide, CLF-C02 Domain 1, and SAA-C03 guide.

### Gap being resolved

The lesson named pillars but lacked SAA-level design implications and trade-off reasoning.

### CPP content added

Pillar decision table, Framework/Tool distinction, traps, and a knowledge check.

### SAA content added

Failure design, automation, managed services, horizontal scaling, decoupling, observability, review milestones, and explicit trade-offs.

### Existing content preserved

SHA-256 before change: `67a13f455b1b6a63ba2a367a1a9e9be6f07bd05eb169d9ceae2d3a733f99d2b1`. Original pillar descriptions, review steps, comparisons, examples, and memory aids remain.

### Content removed or corrected

None.

### Badge decision

CPP and SAA, justified by the expanded body and official scope.

### Remaining work

Later resilience patterns remain in Batch 7.

### Validation result

Acceptance criterion satisfied.

## AWS-006

### Official requirement

Apply the terminology audit only after current official verification.

### Canonical target

Manual-review row bounded to active files containing Amazon QuickSight, Amazon SageMaker, or Personal Health Dashboard wording.

### Existing files reviewed

Terminology and freshness audits, Amazon Quick Sight lesson and direct references, AWS Health lesson and support-plan references, and three active SageMaker references. Historical audit, archive, and migration provenance was also checked but not rewritten.

### Official sources used

Amazon Quick User Guide and rebrand history, Amazon SageMaker AI Developer Guide, and AWS Health User Guide.

### Gap being resolved

Active notes used obsolete product branding.

### CPP content added

A transition note distinguishes the older Amazon QuickSight name from Amazon Quick and its Quick Sight BI component.

### SAA content added

No architecture content; this item is a terminology correction only.

### Existing content preserved

Pre-change checksums captured during preflight include AWS Health `60b0eee4fcd8c6f494d77aee1891652c39d508ca312866c9cde5f7495089f997`, QuickSight `05991f51ac46ed29d3a249b6f0d2abd9ec17633c27408fbc2bc39e6cb647b3d4`, Greengrass `e21853dc09fb4de529ae0b563bb8ffe7801cffebee4edf0e575fb17137b25821`, Rekognition `1f45a6af286ba9864a7a968dc695d53f52982965872a0b02d87d1cfe6f795c9c`, and Savings Plans `550bcf284ec53f781c097e96fd3661c67b2dd92a23ff0b9a9fd52708f744e23a`.

### Content removed or corrected

Active terminology changed to Amazon Quick Sight, Amazon SageMaker AI, and AWS Health Dashboard. Explicitly historical AWS Single Sign-On wording remains labeled as historical. Audit and migration provenance remains unchanged.

### Badge decision

No badge changes; repository-wide badge work belongs to Batch 10.

### Remaining work

None for the audited active terminology. Future guides may continue transitional naming and should be checked during re-audit.

### Validation result

Acceptance criterion satisfied.
