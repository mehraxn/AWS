# Application Integration Comparisons

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Choose messaging and event services from delivery, routing, buffering, and orchestration requirements.

## Guide Order

| Order | Topic | What it covers |
|---:|---|---|
| 1 | [Amazon SQS vs Amazon SNS vs Amazon EventBridge](01-sqs-vs-sns-vs-eventbridge.md) | Study notes and decision points for Amazon SQS vs Amazon SNS vs Amazon EventBridge. |

## Decision Questions

- Does the producer need a queue, pub/sub fan-out, event routing, or a workflow?
- Must messages be retained until a consumer processes them?
- Are ordering, retries, filtering, or orchestration required?

## Recommended Method

1. Extract the requirement and constraints.
2. Identify two or three plausible services.
3. Compare them across functionality, availability, security, operations, performance, and cost.
4. State why the rejected options fail the requirement.

[Back to all comparisons](../README.md) · [Repository home](../../README.md)
