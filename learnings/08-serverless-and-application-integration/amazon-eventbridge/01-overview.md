# Amazon EventBridge

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Amazon EventBridge is a managed event-routing service for event-driven applications. AWS services, custom applications, and supported SaaS partners produce structured events; rules match event content and route it to targets without producers knowing each consumer.

## Event Buses, Events, Rules, and Targets

- The **default bus** receives events from many AWS services.
- **Custom buses** receive application or explicitly routed events.
- **Partner buses/sources** support integrated SaaS events where available.

An event contains metadata such as source and detail type plus a detail payload. An event pattern selects fields/values; a rule evaluates events on its associated bus. Matching rules invoke one or more configured targets. Input transformers can reshape target input. Use EventBridge Scheduler for new centralized one-time or recurring schedules; scheduled rules are a legacy scheduling option.

## Delivery and Failure Behavior

Target delivery is asynchronous and at-least-once paths can produce duplicates. EventBridge does not guarantee ordering. Configure supported retries and an SQS dead-letter queue for undelivered target events, monitor failed invocations, and make consumers idempotent. Target permissions differ: EventBridge may use an execution role or a target resource policy.

## Archive, Replay, and Schemas

An archive captures events matching a pattern from one bus. Replay sends selected archived events back to that source bus for recovery, reprocessing, or testing; replay is not guaranteed in original arrival order. Archives, storage, replay, and downstream targets add cost.

EventBridge Schemas can discover/catalog event structures and help generate code bindings. Treat schemas as contracts and version consumers defensively rather than coupling to unvalidated payloads.

## Security

Use least-privilege IAM for PutEvents/rule/target management, event-bus resource policies for cross-account routing, precise target roles/policies, and AWS KMS options where supported. Protect sensitive event contents, log control-plane activity with CloudTrail, and monitor rules/targets with CloudWatch. Cross-account and cross-Region routes require explicit permissions and cost/failure design.

## Availability, Scalability, and Cost

EventBridge is a managed Regional service. Decoupling lets consumers scale independently, but a rule is not a durable work queue. Use SQS when worker buffering/backpressure is primary. Cost factors include custom/partner/cross-account events, archive storage, replay, transfer, and targets.

## CPP Exam Focus

Think EventBridge when structured events from AWS, applications, or partners must be filtered and routed by rules.

## SAA Scenarios

1. Route only failed deployment events to remediation and audit targets: use event patterns and rules.
2. Add a consumer without changing producers: add a rule/target.
3. Reprocess events after a consumer defect: archive and replay to the source bus after fixing idempotency.
4. Buffer slow workers: target SQS rather than relying on the event bus as a queue.
5. Simple push fanout with little routing: SNS may be simpler.

## Common Mistakes

- Expecting ordered delivery or universal exactly once.
- Treating archive as automatic backup of every event without a matching archive policy.
- Giving a broad target role or cross-account bus policy.
- Using legacy scheduled rules when EventBridge Scheduler is the current recommended scheduler.

## Knowledge Check

1. What does an event pattern do? 2. Which bus receives many AWS service events? 3. What does replay target? 4. Why use a DLQ? 5. When is SQS a better core service?

<details><summary>Answers</summary>

1. Selects events by content. 2. Default bus. 3. The archive's source bus. 4. To retain failed target deliveries for investigation/redrive. 5. When durable worker buffering and backpressure are primary.

</details>

## References

Checked 2026-07-23.

- [Event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
- [Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)
- [Retrying delivery and DLQs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-retry-policy.html)
- [Archives and replay](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-archive.html)
- [EventBridge security](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-security.html)
