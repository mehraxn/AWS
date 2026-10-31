# Multi-Account Governance on AWS

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

A multi-account environment separates workloads, security boundaries, billing, quotas, and operational ownership. AWS Organizations supplies the account hierarchy and organization policies. AWS Control Tower builds and governs a landing zone using Organizations and other services. IAM Identity Center provides workforce access across accounts.

The objective is not the largest number of accounts. It is a repeatable boundary model that limits blast radius, assigns ownership, centralizes evidence, and lets teams deploy without bypassing security requirements.

## Core Account Structure

A common starting design includes:

- A management account used sparingly for organization administration.
- A security tooling account for delegated security administration.
- A log archive account with tightly controlled, durable audit destinations.
- Infrastructure or shared-services accounts for networking and common platforms.
- Separate workload accounts by environment, data sensitivity, team, or business boundary.

Organizational units (OUs) group accounts so policies and AWS Control Tower controls can be applied consistently. Design OUs around governance requirements rather than copying an org chart that changes frequently.

## AWS Organizations

Organizations provides consolidated account management, OUs, policy types, delegated administration, and consolidated billing capabilities. Service control policies (SCPs) define the maximum available permissions for principals in affected member accounts.

An SCP does **not** grant permission. An action succeeds only when identity/resource policies allow it and no applicable SCP, permissions boundary, session policy, or explicit denial blocks it. SCPs do not restrict principals in the organization management account, so protect that account through minimal use, strong authentication, monitoring, and carefully limited roles.

Useful SCP patterns include denying unapproved Regions, preventing security-service disablement, protecting audit destinations, or limiting high-risk services. Test policies in a sandbox OU before broad rollout and retain a recovery path for accidental lockout.

## AWS Control Tower

Control Tower orchestrates a governed landing zone using Organizations, AWS Service Catalog, IAM Identity Center, AWS Config, CloudTrail, and other services. It provides:

- Landing-zone setup and governance.
- Account Factory for repeatable member-account provisioning.
- Preventive, detective, and proactive **controls** applied to OUs.
- Dashboards for enrolled accounts, enabled controls, and noncompliant resources.
- Baselines and managed resources that must not be casually changed outside Control Tower.

Older material may call controls “guardrails”; current AWS documentation uses controls while acknowledging the terms may both appear. Control Tower accelerates governance but does not remove the need to design networks, identities, data protection, incident response, and workload architecture.

## Account Factory and Lifecycle

Account Factory standardizes account creation and enrollment. An account request should include owner, environment, OU, identity groups, network pattern, data classification, budget, and lifecycle metadata. Accounts inherit enabled baselines and controls from their OU.

Plan update, OU move, enrollment, exception, suspension, and closure processes. Moving an account can change applicable policies and controls; treat the move as a governed change and validate workloads afterward.

## IAM Identity Center and Workload Access

Use IAM Identity Center permission sets and groups for workforce access rather than creating long-lived IAM users in every account. Federate an external identity source when appropriate, require MFA, map job functions to permission sets, and keep emergency access controlled and audited.

Workloads use IAM roles and short-lived credentials. Cross-account roles should have both a least-privilege permissions policy and a trust policy restricted to intended principals and conditions. Human access and workload access are separate designs.

## Centralized Logging and Security

Central governance needs evidence that workload administrators cannot silently remove:

- Organization-aware CloudTrail design and protected log destinations.
- AWS Config recording/aggregation for required accounts and Regions.
- Delegated administrators for services such as GuardDuty and Security Hub.
- Central findings, alerts, and incident-response roles.
- KMS key policies and bucket policies that allow delivery while limiting deletion or mutation.

Centralization does not happen merely because accounts belong to an organization. Each service's organization integration, delegated administrator, Regions, destinations, and retention must be configured.

## Failure and Operational Behavior

- A bad SCP can block deployments across an OU; stage and test changes.
- A compromised management account has organization-wide impact; minimize its daily use.
- Missing Regions create monitoring blind spots.
- Central dependencies can become operational bottlenecks; design support and break-glass procedures.
- Control drift or changes to Control Tower-managed resources can leave controls in an unknown state.
- New accounts must enter patching, backup, logging, security, budget, and ownership workflows automatically.

## Cost and Trade-Offs

More accounts improve isolation but add logging, security-service, networking, support, automation, and operational cost. Central networking can simplify inspection but can increase data-processing charges and blast radius. Strict preventive controls reduce risk but can slow experimentation; detective controls provide flexibility but require reliable response.

Choose controls from risk and business requirements. Do not apply every possible control to every OU without considering workload function and recovery procedures.

## CPP Exam Focus

- Organizations: centrally manage multiple accounts and policies.
- OUs: group accounts for governance.
- SCPs: permission boundaries; they do not grant permissions.
- Control Tower: set up and govern a landing zone.
- IAM Identity Center: centralized workforce access to accounts and applications.

## SAA Design Scenarios

1. Prevent member accounts from disabling audit services: tested SCP/control strategy plus protected central logging.
2. Provision standardized project accounts: Control Tower Account Factory and approved blueprints.
3. Give employees role-based account access: Identity Center groups and permission sets.
4. Centralize threat findings: delegated security administrators in a security tooling account.
5. Separate production from development blast radius: different accounts and OUs with appropriate controls.

## Common Mistakes

- Claiming SCPs grant permissions.
- Using the management account for ordinary workloads.
- Treating consolidated billing as merged IAM or network boundaries.
- Assuming Control Tower controls every resource without enrollment and configuration.
- Centralizing logs without protecting destination policies and deletion permissions.

## Knowledge Check

1. Do SCPs grant access? 2. What is Account Factory for? 3. Where should immutable audit evidence commonly be centralized? 4. What provides workforce permission sets across accounts? 5. Why test an SCP in a sandbox OU?

<details><summary>Answers</summary>

1. No; they constrain maximum available permissions. 2. Repeatable account provisioning. 3. A protected log archive account. 4. IAM Identity Center. 5. A mistaken denial can disrupt every account beneath the OU.

</details>

## Related Lessons

- [AWS Organizations](../../03-identity-governance-and-organizations/aws-organizations/01-overview.md)
- [Service control policies](../../03-identity-governance-and-organizations/aws-organizations/02-service-control-policies.md)
- [AWS Control Tower](../../03-identity-governance-and-organizations/aws-control-tower/01-overview.md)
- [IAM Identity Center](../../03-identity-governance-and-organizations/aws-iam-identity-center/01-overview.md)
- [IAM](../../03-identity-governance-and-organizations/aws-iam/01-overview.md)

## References

Checked: 2026-07-24.

- [AWS Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [What is AWS Control Tower?](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [AWS Control Tower controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)
- [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)
- [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
