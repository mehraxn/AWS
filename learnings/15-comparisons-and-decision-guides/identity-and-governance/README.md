# Identity and Governance Decision Guides

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Choose identity and governance constructs from who needs access, where access is granted, and how accounts are controlled.

## Guide Order

| Order | Topic | What it covers |
|---:|---|---|
| 1 | [AWS Account Root User vs AWS IAM](01-root-user-vs-iam.md) | Study notes and decision points for AWS Account Root User vs AWS IAM. |
| 2 | [AWS Organizations vs AWS Control Tower](02-organizations-vs-control-tower.md) | Study notes and decision points for AWS Organizations vs AWS Control Tower. |
| 3 | [IAM Role vs IAM Group vs IAM User](03-users-groups-and-roles.md) | Study notes and decision points for IAM Role vs IAM Group vs IAM User. |

## Decision Questions

- Is the identity a person, application, AWS service, or external provider?
- Is access temporary, cross-account, or centrally governed?
- Do you need permission assignment or an organization-wide guardrail?

## Recommended Method

1. Extract the requirement and constraints.
2. Identify two or three plausible services.
3. Compare them across functionality, availability, security, operations, performance, and cost.
4. State why the rejected options fail the requirement.

[Back to all comparisons](../README.md) · [Repository home](../../README.md)
