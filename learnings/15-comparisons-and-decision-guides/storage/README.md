# Storage Decision Guides

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Choose storage and gateway modes from protocol, sharing, local access, performance, durability, and cost.

## Guide Order

| Order | Topic | What it covers |
|---:|---|---|
| 1 | [AWS File Gateway vs AWS Volume Gateway (Cached)](01-file-gateway-vs-volume-gateway.md) | Study notes and decision points for AWS File Gateway vs AWS Volume Gateway (Cached). |
| 2 | [AWS Storage Gateway vs AWS File Gateway](02-storage-gateway-family.md) | Study notes and decision points for AWS Storage Gateway vs AWS File Gateway. |

## Decision Questions

- Does the application need object, block, or file access?
- Must on-premises applications keep low-latency local data?
- Is the use case active data, backup, archive, or migration?

## Recommended Method

1. Extract the requirement and constraints.
2. Identify two or three plausible services.
3. Compare them across functionality, availability, security, operations, performance, and cost.
4. State why the rejected options fail the requirement.

[Back to all comparisons](../README.md) · [Repository home](../../README.md)
