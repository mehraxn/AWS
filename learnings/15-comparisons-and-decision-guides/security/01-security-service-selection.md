# AWS Security Service Selection

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Quick Decision

- Suspicious activity and threats: **Amazon GuardDuty**.
- Software vulnerabilities and unintended exposure in supported compute workloads: **Amazon Inspector**.
- Sensitive-data discovery and S3 data-security posture: **Amazon Macie**.
- Aggregated findings and cloud security posture: **AWS Security Hub**.
- Investigation of related entities and activity: **Amazon Detective**.
- Resource configuration history and rule-based compliance: **AWS Config**.

These services complement one another. Detection is not prevention, and a finding is not automatically remediated unless you build or enable a response workflow.

## Decision Table

| Service | Primary question | Scope and evidence | Typical output | Common response |
|---|---|---|---|---|
| GuardDuty | Is suspicious or malicious activity occurring? | AWS activity and supported data sources analyzed with threat intelligence and detection techniques | Threat findings | Validate, contain identity/workload, preserve evidence |
| Inspector | Which supported workloads have vulnerabilities or exposure? | Supported EC2, container-image, and Lambda scanning capabilities | Vulnerability findings with severity/context | Patch, rebuild image, update dependency, reduce exposure |
| Macie | Where is sensitive data in S3, and is it exposed? | S3 inventory, security posture, and selected object classification | Policy and sensitive-data findings | Restrict access, classify, encrypt, investigate sharing |
| Security Hub | What is the consolidated security posture? | Findings from integrated services plus security-standard controls | Normalized findings, controls, scores/status | Prioritize and route remediation across accounts/Regions |
| Detective | How are entities and events related during investigation? | Security data organized into behavior and relationship views | Investigation profiles and visual context | Determine scope, timeline, and affected resources |
| AWS Config | Did configuration change, and does it meet a rule? | Recorded supported resource configuration and Config rules | History and compliance evaluations | Remediate configuration and verify policy |

## Amazon GuardDuty

GuardDuty is a managed threat-detection service. It analyzes supported AWS data sources and produces findings for behaviors such as compromised credentials, suspicious API activity, malicious network behavior, or workload threats. It does not function as a web firewall, vulnerability patcher, or SIEM replacement.

Use delegated administration and organization integration to manage coverage consistently. Enable the required protection plans and Regions deliberately; a finding in one account or Region does not prove every environment is covered.

## Amazon Inspector

Inspector continuously evaluates supported workloads for software vulnerabilities and unintended network exposure. Its exact coverage depends on resource type and enabled scanning mode. Treat a finding as prioritized remediation input: update packages or functions, rebuild container images, remove exposure, and verify the new artifact.

Inspector is different from GuardDuty: Inspector evaluates vulnerability and exposure conditions, while GuardDuty detects suspicious activity and threats.

## Amazon Macie

Macie is a data-security and privacy service focused on Amazon S3. It inventories buckets, evaluates security and access conditions, and uses managed and custom data identifiers to discover sensitive data in selected objects.

Macie does not scan every database, file system, or application payload. Classification jobs, sampling choices, object access, and multi-account/Regional enablement affect coverage and cost.

## AWS Security Hub

Security Hub centralizes and normalizes findings from AWS and supported partner products and provides cloud security posture management through standards and controls. Aggregation improves prioritization, but Security Hub does not make every source service unnecessary and does not automatically repair every finding.

A multi-account design normally chooses delegated administrators, enabled standards, aggregation strategy, severity workflow, ownership tags, and EventBridge-based ticketing or remediation. Avoid sending every finding directly to automation without validation and rollback controls.

## Amazon Detective

Detective helps security teams investigate by organizing related activity and resource relationships into behavior graphs and profiles. It is useful after a finding raises a question such as which identities, IP addresses, instances, or API calls are connected.

Detective supports investigation; GuardDuty and other services still produce the initial findings, and responders still decide containment and recovery actions.

## AWS Config

AWS Config records supported resource configurations and their changes and evaluates them against Config rules. It answers configuration and compliance questions such as whether encryption, logging, or public-access settings meet policy.

Config is not a threat-detection engine. A compliant configuration can still be attacked, and a threat finding can occur without a Config rule change.

## Finding-to-Response Pattern

1. Enable services consistently across required accounts and Regions.
2. Send findings to a central Security Hub administration and aggregation design where appropriate.
3. Route selected findings through EventBridge to case management or automation.
4. Validate severity, ownership, and possible false positives.
5. Contain the affected identity, workload, network path, or data access.
6. Remediate, recover, and verify with rescanning or compliance evaluation.
7. Preserve evidence and tune controls without suppressing real risk.

## Security and Governance

Use least-privilege delegated-administrator roles, separate security tooling accounts, organization policies, encrypted destinations, protected logs, and explicit cross-account trust. Monitor service coverage as well as findings: a silent dashboard can mean no threats or missing sensors.

## Cost Considerations

Costs vary by enabled service and analyzed volume: events or data sources, scanned resources and images, S3 objects classified, enabled controls, configuration items, and retained investigation data. Enable coverage based on risk, then use organization policies, scoping, and lifecycle controls to avoid blind spots and uncontrolled cost.

## CPP Exam Focus

- GuardDuty: threats.
- Inspector: workload vulnerabilities.
- Macie: sensitive data in S3.
- Security Hub: aggregated findings and posture.
- Detective: investigation.
- Config: configuration history and compliance.

## SAA Scenarios

1. Detect suspicious access-key behavior: GuardDuty, then investigate and contain the principal.
2. Find vulnerable packages in supported compute: Inspector and a patch/rebuild pipeline.
3. Discover personal data in S3: Macie with controlled classification jobs.
4. Give a central team cross-account posture: Security Hub delegated administration and aggregation.
5. Explain relationships around a GuardDuty finding: pivot to Detective.
6. Prove that buckets remain encrypted: AWS Config recording and rules, with remediation as a separate action.

## Common Mistakes

- Calling Inspector a threat-detection service or GuardDuty a vulnerability scanner.
- Treating Macie as a universal data-classification engine.
- Assuming Security Hub enables every source or fixes every finding.
- Treating Config compliance as proof that no compromise exists.
- Automating destructive containment without validation or rollback.

## Knowledge Check

1. Which service discovers sensitive data in S3? 2. Which service evaluates supported compute vulnerabilities? 3. Which service centralizes findings? 4. Which service records configuration history? 5. Which service helps investigate relationships after a finding?

<details><summary>Answers</summary>

1. Macie. 2. Inspector. 3. Security Hub. 4. AWS Config. 5. Amazon Detective.

</details>

## Canonical Lessons

- [Amazon GuardDuty](../../09-security-and-compliance/amazon-guardduty/01-overview.md)
- [Amazon Inspector](../../09-security-and-compliance/amazon-inspector/01-overview.md)
- [Amazon Macie](../../09-security-and-compliance/amazon-macie/01-overview.md)
- [AWS Security Hub](../../09-security-and-compliance/aws-security-hub/01-overview.md)
- [AWS Config](../../10-monitoring-management-and-deployment/aws-config/01-overview.md)

## References

Checked: 2026-07-24.

- [Amazon GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
- [What is Amazon Macie?](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [What is AWS Security Hub?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
- [What is Amazon Detective?](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)
- [What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
