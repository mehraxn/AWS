# Migration Decision Guides

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Choose migration and hybrid services from data type, transfer path, downtime, bandwidth, and target environment.

## Guide Order

| Order | Topic | What it covers |
|---:|---|---|
| 1 | [AWS DataSync vs AWS Database Migration Service (AWS DMS)](01-datasync-vs-dms.md) | Study notes and decision points for AWS DataSync vs AWS Database Migration Service (AWS DMS). |
| 2 | [AWS Snowball Edge vs AWS Outposts](02-snowball-edge-vs-outposts.md) | Study notes and decision points for AWS Snowball Edge vs AWS Outposts. |

## Decision Questions

- Are you moving files, objects, databases, or whole workloads?
- Is the transfer online, offline, continuous, or one-time?
- Does the target remain hybrid after migration?

## Recommended Method

1. Extract the requirement and constraints.
2. Identify two or three plausible services.
3. Compare them across functionality, availability, security, operations, performance, and cost.
4. State why the rejected options fail the requirement.

[Back to all comparisons](../README.md) · [Repository home](../../README.md)
