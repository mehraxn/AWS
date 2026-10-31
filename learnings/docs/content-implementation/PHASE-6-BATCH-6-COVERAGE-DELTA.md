# Phase 6 Batch 6 Coverage Delta

## Dependency Resolution

All mandatory Batch 5 records were present. AWS-031 through AWS-034 and direct dependency AWS-004 were completed with no Batch 6 blocker.

## Encryption and Key Management Improved

AWS-035 adds scenario-ready coverage of KMS key ownership, key policies, IAM interaction, data keys, envelope encryption, rotation choices, monitoring, failure behavior, and cost trade-offs.

## Secrets and Certificates Improved

AWS-035 distinguishes KMS, Secrets Manager, Parameter Store, and ACM by purpose and explains secret rotation and managed certificate renewal responsibilities.

## Application and Network Protection Improved

No application or network protection backlog row was selected for Batch 6.

## Threat Detection and Security Posture Improved

AWS-036 adds a decision guide for GuardDuty, Inspector, Macie, Security Hub, Detective, and AWS Config, including a multi-account response workflow.

## Monitoring and Observability Improved

AWS-037 distinguishes CloudWatch operational telemetry from X-Ray request tracing and shows how those signals complement audit and configuration evidence.

## Audit and Compliance Improved

AWS-037 distinguishes CloudTrail activity history from AWS Config configuration history and compliance evaluation.

## Systems Management Improved

AWS-039 expands Systems Manager coverage for managed nodes, Inventory, Patch Manager, Run Command, State Manager, Automation, Parameter Store, Session Manager, hybrid environments, audit, and partial failure.

## Infrastructure Deployment Improved

No CloudFormation or other infrastructure-deployment backlog row was selected for Batch 6.

## Governance and Multi-Account Management Improved

AWS-038 adds scenario-ready Organizations, OU, SCP, Control Tower, Account Factory, IAM Identity Center, delegated administration, and centralized logging guidance.

## CPP Requirements Fully Resolved

CPP-2.2-02, CPP-2.2-03, CPP-2.2-04, and CPP-2.4-01 now have direct canonical evidence.

## CPP Requirements Partially Improved

None among the directly affected CPP task statements.

## SAA Requirements Fully Resolved

Direct scenario-ready evidence was added for SAA-1.1-01, SAA-1.1-02, SAA-1.1-05, SAA-1.2-01, SAA-1.2-05, SAA-1.3-02, and SAA-1.3-03.

## SAA Requirements Partially Improved

AWS-037 improves observability evidence for SAA-2.2-05, but that combined task also requires service-quota architecture evidence outside this batch and therefore remains partial.

## New Scenario-Ready Topics

- Data protection architecture
- Security-service selection
- Operational evidence selection
- Multi-account governance
- Systems Manager fleet operations

## New Comparison Guides

- GuardDuty vs Inspector vs Macie vs Security Hub, with Detective and Config boundaries
- CloudWatch vs CloudTrail vs AWS Config, with X-Ray boundaries
- KMS vs Secrets Manager vs Parameter Store vs ACM
- AWS Organizations vs AWS Control Tower
- Session Manager vs bastion-host access

## Factual Corrections

Five substantive corrections are recorded in `PHASE-6-BATCH-6-FACT-CORRECTIONS.md`.

## Terminology Corrections

The new governance lesson uses current Control Tower `controls` terminology and states that SCPs limit but do not grant permissions.

## Badge Corrections

Both badges were added only where the targets now contain meaningful CPP recognition content and SAA architecture depth.

## Navigation Improvements

Direct category, comparison, repository-map, root, and service-index links were added for the five selected targets.

## Audit Map and Dashboard Updates

The canonical inventory, badge audit, CPP and SAA task maps, service and concept matrices, depth matrix, architecture-quality audit, and coverage dashboards were updated only for Batch 6 evidence.

## Remaining Security Gaps

Later-batch or unselected protection topics remain governed by the authoritative backlog; none were pulled into Batch 6.

## Remaining Monitoring Gaps

The service-quota portion of SAA-2.2-05 remains partial and non-blocking for Batch 7.

## Remaining Governance Gaps

No selected Batch 6 governance item remains incomplete.

## Deferred Batch 7 and Later Work

Batch 7 and all later work remain untouched.
