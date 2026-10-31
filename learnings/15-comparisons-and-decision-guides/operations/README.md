# Operations Decision Guides

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Distinguish operational services by whether they observe performance, record API activity, or evaluate resource configuration.

## Guide Order

| Order | Topic | What it covers |
|---:|---|---|
| 1 | [Amazon CloudWatch vs AWS CloudTrail vs AWS Config](01-cloudwatch-vs-cloudtrail-vs-config.md) | Study notes and decision points for Amazon CloudWatch vs AWS CloudTrail vs AWS Config. |

## Decision Questions

- Do you need metrics and alarms, an audit trail, or configuration compliance?
- Is the question about application health, user actions, or resource state?
- Will the result trigger operations, investigation, or governance?

## Recommended Method

1. Extract the requirement and constraints.
2. Identify two or three plausible services.
3. Compare them across functionality, availability, security, operations, performance, and cost.
4. State why the rejected options fail the requirement.

[Back to all comparisons](../README.md) · [Repository home](../../README.md)
