# Security Decision Guides

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Map the protected resource and threat type to the most appropriate AWS security service.

## Guide Order

| Order | Topic | What it covers |
|---:|---|---|
| 1 | [AWS Security Service Selection](01-security-service-selection.md) | Study notes and decision points for AWS Security Service Selection. |

## Decision Questions

- Are you protecting identities, secrets, data, workloads, networks, or web applications?
- Is the control preventive, detective, responsive, or compliance-oriented?
- Does the service inspect code, traffic, configuration, behavior, or stored data?

## Recommended Method

1. Extract the requirement and constraints.
2. Identify two or three plausible services.
3. Compare them across functionality, availability, security, operations, performance, and cost.
4. State why the rejected options fail the requirement.

[Back to all comparisons](../README.md) · [Repository home](../../README.md)
