# AWS Step Functions

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

AWS Step Functions is a serverless workflow-orchestration service. A state machine coordinates distributed steps visually and is defined with the JSON-based Amazon States Language. Data flows through state inputs/outputs and transitions rather than custom coordination code.

## Important States

| State | Purpose |
|---|---|
| Task | Perform work through Lambda or another integration |
| Choice | Branch on data |
| Wait | Delay until a time/duration |
| Parallel | Run branches concurrently and join |
| Map | Process collection items, optionally with distributed processing options |
| Pass | Transform/pass data without external work |
| Succeed / Fail | End explicitly with success/failure |

## Standard and Express Workflows

Standard Workflows suit long-running, durable, auditable orchestration and official documentation describes exactly-once workflow execution. Express Workflows suit high-event-rate, short-duration workloads and use at-least-once execution; steps can run more than once. Synchronous Express can return a workflow result to a caller. Exact behavior applies to Step Functions execution semantics, not arbitrary external side effects—integrated tasks should still be idempotent.

Standard pricing centers on state transitions. Express pricing considers executions, duration, and memory; logging and integrated services add cost. Choose from duration, rate, audit history, integration pattern, and delivery semantics rather than price alone.

## Integrations and Patterns

Step Functions integrates with Lambda, ECS/Fargate, DynamoDB, SQS, SNS, EventBridge, API Gateway, and AWS SDK operations. Supported patterns include request/response, wait for a job, and callback with task token depending on integration/workflow type.

Use sequential, Choice branching, Parallel, Map, human-approval callback, and saga/compensation patterns. Step Functions is orchestration: a central workflow controls steps. EventBridge is choreography/routing: producers emit events and consumers react. SQS buffers work; Lambda executes code.

## Retries, Errors, and Availability

`Retry` handles selected transient errors with interval/backoff controls; `Catch` sends failures to fallback states. Configure timeouts/heartbeats where supported, distinguish retriable from permanent errors, and make tasks idempotent. Compensation reverses completed business actions when a later step fails; it is not a database rollback.

Step Functions is managed and Regional. Workflow durability does not guarantee that every downstream service is available; model timeouts, fallbacks, quotas, and Regional recovery.

## Security

Use a least-privilege state-machine execution role for every integration. Control who can start/inspect executions, protect logged input/output and sensitive payloads, use encryption/logging options appropriately, and avoid passing secrets through workflow history.

## CPP Exam Focus

Think Step Functions when AWS services or Lambda functions must be coordinated as a visible managed workflow with branching and error handling.

## SAA Scenarios

1. Coordinate payment, inventory, and shipping with compensation: Standard workflow with Retry/Catch and compensating states.
2. High-rate short event transformations: evaluate Express and idempotent tasks.
3. Wait for external approval: callback/task-token pattern where supported.
4. Process many independent items: Map; use Parallel for a fixed set of branches.
5. Route unrelated domain events: EventBridge may fit better than central orchestration.

## Common Mistakes

- Treating Lambda as the workflow engine.
- Assuming Express executes each step only once.
- Retrying permanent business errors indefinitely.
- Logging secrets in state input/output.
- Confusing orchestration with event choreography.

## Knowledge Check

1. Which state branches by data? 2. Standard or Express for durable auditable work? 3. What do Retry and Catch do? 4. Map versus Parallel? 5. Why keep tasks idempotent?

<details><summary>Answers</summary>

1. Choice. 2. Standard. 3. Retry repeats selected failures; Catch routes failures. 4. Map processes collections; Parallel runs defined branches. 5. Retries/at-least-once execution can repeat calls.

</details>

## References

Checked 2026-07-23.

- [What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Workflow types](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html)
- [State types](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-states.html)
- [Service integrations](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-service-integrations.html)
- [Error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
