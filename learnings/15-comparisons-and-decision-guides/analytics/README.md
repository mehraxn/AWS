# Analytics Decision Guides

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Choose analytics services from data volume, latency, processing model, query style, and audience.

## Guide Order

| Order | Topic | What it covers |
|---:|---|---|
| 1 | [Amazon EMR vs Amazon Redshift](01-emr-vs-redshift.md) | Study notes and decision points for Amazon EMR vs Amazon Redshift. |
| 2 | [AWS Analytics Service Selection](02-analytics-service-selection.md) | Study notes and decision points for AWS Analytics Service Selection. |

## Decision Questions

- Is the workload streaming, batch, interactive query, ETL, warehouse, or visualization?
- Does the solution need managed clusters, serverless queries, or a data warehouse?
- What latency and operational-control requirements matter?

## Recommended Method

1. Extract the requirement and constraints.
2. Identify two or three plausible services.
3. Compare them across functionality, availability, security, operations, performance, and cost.
4. State why the rejected options fail the requirement.

[Back to all comparisons](../README.md) · [Repository home](../../README.md)
