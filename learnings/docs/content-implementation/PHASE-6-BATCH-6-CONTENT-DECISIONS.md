# Phase 6 Batch 6 Content Decisions

## AWS-035 — Data protection architecture

### Official requirement
Encryption and key design.
### Required CPP depth
Awareness/fundamental recognition of KMS, TLS, ACM, Secrets Manager, and Parameter Store.
### Required SAA depth
Scenario-ready key policy, envelope encryption, secret lifecycle, TLS, and cross-account design.
### Canonical target
`13-architecture-and-design-patterns/security/01-data-protection-patterns.md`
### Existing files reviewed
KMS, Secrets Manager, ACM, IAM, and TLS canonical lessons.
### Official sources used
AWS KMS, Secrets Manager, Parameter Store, and ACM documentation checked 2026-07-24.
### Gap being resolved
Service definitions existed, but no integrated data-protection architecture.
### CPP content added
Service recognition and at-rest/in-transit distinctions.
### SAA architecture content added
Key ownership, policies, envelope encryption, rotation, cross-account authorization, failure, monitoring, and cost.
### Security, monitoring, or governance scenarios added
Rotating credentials, client-side encryption, managed TLS, and cross-account encrypted data.
### Existing content preserved
Canonical service lessons remain owners and are linked.
### Content removed or corrected
No existing target; avoided implying encryption supplies replication or availability.
### Badge decision
Both badges justified by fundamental CPP and scenario-ready SAA content.
### Navigation and map updates
Architecture/security indexes, service index, inventory, task maps, matrices, and dashboards.
### Acceptance-criteria result
Passed on content; final repository gate pending.
### Remaining work
None for AWS-035.
### Validation result
Passed: naming, internal-link, duplicate-candidate, hash, lesson-structure, CSV, and diff checks.

## AWS-036 — Security service selection

### Official requirement
Threat-detection and security-service selection.
### Required CPP depth
Awareness/fundamental service recognition.
### Required SAA depth
Architecture-and-design selection, integration, response, multi-account scope, and cost.
### Canonical target
`15-comparisons-and-decision-guides/security/01-security-service-selection.md`
### Existing files reviewed
GuardDuty, Inspector, Macie, Security Hub, Config, and security-category lessons.
### Official sources used
Official service user guides checked 2026-07-24.
### Gap being resolved
No single guide consistently compared scope and response.
### CPP content added
Recognition table for threats, vulnerabilities, S3 sensitive data, posture, investigation, and configuration.
### SAA architecture content added
Delegated administration, finding aggregation, response workflow, coverage boundaries, and cost.
### Security, monitoring, or governance scenarios added
Credential threat, vulnerability, data discovery, central posture, investigation, and compliance cases.
### Existing content preserved
Service-specific canonical lessons remain unchanged and linked.
### Content removed or corrected
Corrected detection-versus-prevention and finding-versus-remediation implications.
### Badge decision
Both badges justified.
### Navigation and map updates
Security/comparison indexes, service index, inventory, maps, matrices, and dashboards.
### Acceptance-criteria result
Passed on content; final repository gate pending.
### Remaining work
None for AWS-036.
### Validation result
Passed: naming, internal-link, duplicate-candidate, hash, lesson-structure, CSV, and diff checks.

## AWS-037 — CloudWatch vs CloudTrail vs AWS Config

### Official requirement
Observability service selection.
### Required CPP depth
Fundamental signal and service recognition.
### Required SAA depth
Scenario-ready telemetry, audit, configuration, tracing, retention, and multi-account decisions.
### Canonical target
`15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md`
### Existing files reviewed
Config, X-Ray, Systems Manager, and operations navigation.
### Official sources used
CloudWatch, CloudTrail, Config, and X-Ray documentation checked 2026-07-24.
### Gap being resolved
No consistent comparison separated symptoms, request flow, API activity, and resource state.
### CPP content added
Metrics/logs/alarms, API activity, configuration/compliance, and tracing recognition.
### SAA architecture content added
Signal correlation, centralized evidence, coverage, retention, failure behavior, and cost.
### Security, monitoring, or governance scenarios added
API errors, actor attribution, public-bucket timeline, tracing, and cross-account audit.
### Existing content preserved
Existing Config and X-Ray lessons remain linked canonical owners.
### Content removed or corrected
Corrected the implication that Config prevents all changes or CloudWatch collects all logs automatically.
### Badge decision
Both badges justified.
### Navigation and map updates
Operations/comparison indexes, service index, inventory, maps, matrices, and dashboards.
### Acceptance-criteria result
Passed; combined quota/observability map remains partial only for quota design outside Batch 6.
### Remaining work
None for AWS-037; service quota depth remains later work and does not block Batch 7.
### Validation result
Passed: naming, internal-link, duplicate-candidate, hash, lesson-structure, CSV, and diff checks.

## AWS-038 — Multi-account governance

### Official requirement
Multi-account guardrails and governance.
### Required CPP depth
Awareness of Organizations, OUs, SCPs, Control Tower, and Identity Center.
### Required SAA depth
Scenario-ready account, identity, control, logging, failure, and trade-off design.
### Canonical target
`13-architecture-and-design-patterns/security/02-multi-account-governance.md`
### Existing files reviewed
Organizations, SCP, Control Tower, Identity Center, IAM, and existing comparison lessons.
### Official sources used
Organizations, Control Tower, and Identity Center documentation checked 2026-07-24.
### Gap being resolved
Existing definitions lacked an integrated landing-zone architecture.
### CPP content added
Organizations, OU, SCP, Control Tower, and Identity Center recognition.
### SAA architecture content added
Account boundaries, delegated administration, Account Factory, centralized logs, failure behavior, and cost.
### Security, monitoring, or governance scenarios added
Audit protection, standardized accounts, workforce access, delegated security, and environment isolation.
### Existing content preserved
Existing service lessons and comparison remain canonical and linked.
### Content removed or corrected
Used current “controls” terminology and explicitly stated that SCPs do not grant permissions.
### Badge decision
Both badges justified.
### Navigation and map updates
Identity/architecture indexes, service index, inventory, maps, matrices, and dashboards.
### Acceptance-criteria result
Passed on content; final repository gate pending.
### Remaining work
None for AWS-038.
### Validation result
Passed: naming, internal-link, duplicate-candidate, hash, lesson-structure, CSV, and diff checks.

## AWS-039 — AWS Systems Manager

### Official requirement
Operations-management selection and architecture.
### Required CPP depth
Awareness of Inventory, patching, automation, parameters, sessions, and hybrid nodes.
### Required SAA depth
Architecture-and-design security, rollout, failure, hybrid, monitoring, and cost trade-offs.
### Canonical target
`10-monitoring-management-and-deployment/aws-systems-manager/01-overview.md`
### Existing files reviewed
Existing Systems Manager overview and Session Manager lesson.
### Official sources used
Official Systems Manager tool, Inventory, Patch Manager, Automation, Parameter Store, and Session Manager documentation checked 2026-07-24.
### Gap being resolved
Existing lesson was accurate but definition-focused.
### CPP content added
Badges and explicit capability recognition.
### SAA architecture content added
Prerequisites, patch waves, runbook controls, SecureString permissions, hybrid nodes, partial failure, and cost.
### Security, monitoring, or governance scenarios added
Fleet patching, private administration, Config remediation, hybrid management, and parameter selection.
### Existing content preserved
Original overview retained verbatim; supplement appended.
### Content removed or corrected
No useful content removed; clarified that registration and managed access do not guarantee success or least privilege.
### Badge decision
Both badges justified.
### Navigation and map updates
Operations index, service index, inventory, matrices, and dashboards.
### Acceptance-criteria result
Passed on content; final repository gate pending.
### Remaining work
None for AWS-039.
### Validation result
Passed: naming, internal-link, duplicate-candidate, hash, lesson-structure, CSV, and diff checks.
