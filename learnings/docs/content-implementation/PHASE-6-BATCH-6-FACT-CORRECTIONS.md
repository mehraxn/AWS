# Phase 6 Batch 6 Fact Corrections

## Correction

Affected path: `13-architecture-and-design-patterns/security/01-data-protection-patterns.md`

Related backlog ID: AWS-035

Previous claim: The repository did not have a canonical architecture lesson that explained how KMS key policies, IAM permissions, data keys, and envelope encryption work together.

Corrected claim: AWS KMS controls use of KMS keys through key policies and, where the key policy permits it, IAM policies. Envelope encryption protects data with a data key and protects that data key with a KMS key. Secrets Manager, Parameter Store, and ACM solve different storage and certificate-management needs.

Reason: Replaced an incomplete treatment with current AWS terminology and explicit service boundaries.

Official source: [AWS KMS key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), [AWS KMS cryptography](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html), [Secrets Manager introduction](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), and [ACM managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html).

Date checked: 2026-07-24

Severity: high

## Correction

Affected path: `15-comparisons-and-decision-guides/security/01-security-service-selection.md`

Related backlog ID: AWS-036

Previous claim: No canonical decision guide clearly separated threat detection, vulnerability assessment, sensitive-data discovery, finding aggregation, investigation, and configuration compliance.

Corrected claim: GuardDuty detects threats, Inspector assesses supported workloads for vulnerabilities and exposure, Macie discovers sensitive data in Amazon S3, Security Hub aggregates findings and evaluates security posture, Detective supports investigation, and AWS Config records supported resource configurations and evaluates rules.

Reason: Prevents exam answers from treating distinct detective and posture-management services as interchangeable.

Official source: [AWS detective controls](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/detective-controls.html) and the service documentation linked by the lesson.

Date checked: 2026-07-24

Severity: high

## Correction

Affected path: `15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md`

Related backlog ID: AWS-037

Previous claim: Monitoring, API auditing, configuration history, compliance evaluation, and distributed tracing lacked one canonical comparison.

Corrected claim: CloudWatch handles operational metrics, logs, alarms, and dashboards; CloudTrail records supported AWS API and account activity; AWS Config records supported resource configuration history and evaluates compliance; X-Ray traces distributed application requests.

Reason: Clarifies which signal answers each operational or audit question and how the signals can be correlated.

Official source: [AWS Config resource history](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource-console.html), [AWS X-Ray concepts](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html), and the CloudWatch and CloudTrail documentation linked by the lesson.

Date checked: 2026-07-24

Severity: high

## Correction

Affected path: `13-architecture-and-design-patterns/security/02-multi-account-governance.md`

Related backlog ID: AWS-038

Previous claim: The repository lacked scenario-ready guidance distinguishing Organizations from Control Tower and did not clearly state the permission effect of SCPs.

Corrected claim: SCPs set permission guardrails but do not grant permissions. AWS Control Tower builds and governs a landing zone with controls and Account Factory on top of AWS Organizations; it does not replace Organizations.

Reason: Corrects a common permissions misconception and uses the current Control Tower term `controls`.

Official source: [Organizations SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [What is AWS Control Tower?](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), [Control Tower controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html), and [Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html).

Date checked: 2026-07-24

Severity: high

## Correction

Affected path: `10-monitoring-management-and-deployment/aws-systems-manager/01-overview.md`

Related backlog ID: AWS-039

Previous claim: The existing overview listed Systems Manager capabilities but lacked architecture depth for prerequisites, partial failure, audit, hybrid nodes, and Session Manager access.

Corrected claim: Systems Manager features operate on managed nodes with feature-specific prerequisites; fleet operations can partially succeed and must be reviewed per target. Session Manager can provide administrative access without opening inbound SSH or RDP ports, while CloudTrail and service logs provide audit evidence when configured.

Reason: Adds operational boundaries and failure behavior without removing the useful existing overview.

Official source: [AWS Systems Manager tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-tools.html) and the focused Systems Manager documentation linked by the lesson.

Date checked: 2026-07-24

Severity: medium
