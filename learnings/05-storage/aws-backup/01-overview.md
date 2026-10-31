# AWS Backup

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

AWS Backup centrally manages backup and restore policies across supported AWS services and accounts. It coordinates service-native backup capabilities through plans, vaults, assignments, monitoring, and governance.

## Core Concepts

- A **backup plan** contains rules for schedule, backup window, retention/lifecycle, destination vault, and optional copy actions.
- A **resource assignment** selects protected resources directly or with tags and supported AWS Organizations policies.
- A **backup vault** logically stores and controls recovery points. Vault access policies and encryption help protect them.
- **Cross-Region copies** support regional recovery designs; **cross-account copies** support isolation where the service and resource type allow them.
- **Vault Lock** applies governance or compliance controls against early deletion. Compliance mode requires careful planning because its controls become immutable after the grace period.
- **Restore testing** can schedule tests and report results so a stored recovery point is not mistaken for proven recoverability.

## Backup Versus Snapshot or Replication

A service-native snapshot is a recovery mechanism for one service. AWS Backup adds centralized policy, monitoring, retention, and supported copy/governance workflows. Replication improves availability and recovery time but can copy unwanted changes; it is not a substitute for independent, retained backups.

## Security and Shared Responsibility

AWS operates the backup service. Customers select resources and schedules, grant service roles, control vault and KMS permissions, protect destination accounts, monitor failed jobs, test restores, and set retention that satisfies business and compliance requirements. A successful backup job is not proof that the application can be restored correctly.

## Resilience and Cost

Align frequency and retention with recovery point objectives; align restore procedures with recovery time objectives. Use cross-account or cross-Region copies only when isolation and disaster requirements justify them. Costs depend on backup storage, retention, restore activity, copy operations, and data transfer. Lifecycle rules can move eligible recovery points to lower-cost storage.

## CPP Knowledge

Recognition clues are **centralized backup policy**, **multiple supported AWS services**, **backup vaults**, and **compliance reporting**.

## SAA Architecture and Design

- Apply organization-wide plans to tagged resources for consistent coverage.
- Place copies in a dedicated backup account to reduce the blast radius of a compromised workload account.
- Add another Region where regional recovery objectives require it.
- Restrict vault deletion, monitor job failures, and perform restore testing.
- Keep application-consistent procedures where a crash-consistent infrastructure backup is insufficient.

## Common Exam Traps

- Backup, replication, and high availability solve different objectives.
- AWS Backup supports specific services and features; verify current resource support.
- Vault Lock is a governance control, not a replacement for least privilege.
- Creating recovery points without testing restores leaves recovery risk unknown.

## Practice Questions

1. What defines schedules and retention in AWS Backup?
2. Why copy backups to another account?
3. Why perform restore testing?

<details><summary>Answers</summary>

1. Backup-plan rules. 2. To isolate recovery points from the workload account's failure or compromise. 3. To validate that recovery points and restore procedures actually work.

</details>

## References

- [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html)
- [Cross-account backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html)
- [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html)
- [Restore testing](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html)

Official references checked: 2026-07-22.
