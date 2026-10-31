# Amazon SQS vs Amazon SNS vs Amazon EventBridge

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Quick Decision

- Choose **SQS** when workers should pull durable buffered work independently.
- Choose **SNS** when one publication should be pushed to several subscribers.
- Choose **EventBridge** when rules should inspect events and route them to targets.

## Core Mental Model

| Service | Model | Consumer interaction | Best clue |
|---|---|---|---|
| SQS | Queue | Consumers poll/pull | Buffer and isolate work |
| SNS | Topic | SNS pushes to subscribers | Simple fanout notification |
| EventBridge | Event bus | Rules match and route | Content-based event routing |

## Amazon SQS: Queue

Producers send messages to a queue; consumers poll, process, and delete them. Visibility timeout temporarily hides an in-flight message. If processing fails, it becomes visible again; consumers must be idempotent. A dead-letter queue isolates messages after repeated receive failures, and long polling reduces empty responses.

Standard queues provide at-least-once delivery and best-effort ordering, so duplicates and reordering are possible. FIFO queues preserve ordering within message groups and provide deduplication/exactly-once processing terminology only within documented FIFO conditions; application side effects still require idempotency.

## Amazon SNS: Topic and Push Fanout

Publishers send to a topic and SNS pushes to subscriptions such as SQS queues, Lambda, HTTP/S endpoints, and supported notification protocols. Subscription filter policies can limit delivery. Delivery retries depend on endpoint protocol; supported subscriptions can configure dead-letter queues. SNS standard topics do not act as durable worker queues. FIFO topics preserve ordered fanout to supported FIFO endpoints under documented conditions.

## Amazon EventBridge: Event Bus and Rule-Based Routing

AWS services, applications, and partner sources put structured events on buses. Rules use event patterns for content-based filtering and send matches to targets such as Lambda, SQS, SNS, Step Functions, or other supported services. EventBridge can transform target input and supports archives/replay. It does not guarantee event ordering and consumers should tolerate duplicate delivery.

## Delivery, Ordering, and Filtering

| Need | SQS | SNS | EventBridge |
|---|---|---|---|
| Durable worker buffer | Strong fit | Use an SQS subscription | Target an SQS queue |
| Push fanout | One queue normally feeds competing consumers | Core model | Multiple rules/targets |
| Complex content routing | Consumer/application logic | Subscription filters | Event patterns and rules |
| Ordering | FIFO queue option | FIFO topic option | No ordering guarantee |
| Replay | Retain until consumed/expired; redrive patterns | Not a replay store | Archive and replay |

## Retries, Dead-Letter Handling, and Failure Isolation

SQS isolates work naturally: one slow worker does not require the producer to wait. Size visibility timeout for processing and use DLQs/redrive deliberately. SNS retries push delivery according to protocol; separate SQS subscriptions isolate subscribers and preserve messages. EventBridge retries failed target delivery conceptually and can use SQS DLQs. Every target should be idempotent and monitored.

## Fanout Patterns

- **SNS → several SQS queues:** each consumer group gets an independent durable buffer and failure boundary.
- **EventBridge → SQS/SNS/Lambda:** content-based rules select consumers without changing producers.
- **SNS → Lambda/HTTP:** simple push notifications when durable buffering is unnecessary or supplied downstream.

## Security, Availability, and Cost

Use IAM plus queue/topic/event-bus resource policies, least privilege, encryption, endpoint policies where relevant, and correct DLQ permissions. Cross-account publishing/routing requires explicit resource and identity permissions. These managed Regional services scale across underlying infrastructure, but applications still design retries, idempotency, monitoring, and Regional recovery.

Cost depends on requests/events, payload chunks, polling, publications/deliveries and protocol, archive/replay storage, transfer, DLQ/redrive, and target-service charges. No choice is always cheapest.

## CPP Exam Focus

Queue/buffer/workers → SQS. Push one message to many subscribers → SNS. Route structured events by content → EventBridge.

## SAA Design Scenarios

1. Image jobs must survive a worker outage: SQS with idempotent workers and a DLQ.
2. An order event must reach billing and fulfillment independently: SNS to separate SQS queues.
3. Different event details need different targets: EventBridge rules.
4. Strict ordered work: verify FIFO SQS/SNS compatibility and keep consumers idempotent.
5. A failed downstream service needs later reprocessing: buffer in SQS or use an EventBridge archive/replay design as appropriate.

## Common Mistakes

- Calling SNS a durable work queue.
- Claiming universal exactly-once application processing.
- Expecting EventBridge ordering.
- Using fanout without isolating subscriber failures.
- Forgetting target-service and data-transfer costs.

## Knowledge Check

1. Which service gives workers a pull-based buffer?
2. Which service provides simple push fanout?
3. Which service routes by structured event patterns?
4. Why should consumers be idempotent?
5. How can fanout consumers fail independently?

<details><summary>Answers</summary>

1. SQS. 2. SNS. 3. EventBridge. 4. Retries and at-least-once paths can produce duplicates. 5. Give each subscriber its own SQS queue/DLQ boundary.

</details>

## Canonical Lessons

- [Amazon SQS](../../08-serverless-and-application-integration/amazon-sqs/01-overview.md)
- [Amazon EventBridge](../../08-serverless-and-application-integration/amazon-eventbridge/01-overview.md)
- [AWS Step Functions](../../08-serverless-and-application-integration/aws-step-functions/01-overview.md)
- [Amazon API Gateway](../../08-serverless-and-application-integration/amazon-api-gateway/01-overview.md)

## References

Checked 2026-07-23.

- [AWS decision guide: SNS, SQS, or EventBridge](https://docs.aws.amazon.com/decision-guides/latest/sns-or-sqs-or-eventbridge/sns-or-sqs-or-eventbridge.html)
- [Amazon SQS delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html)
- [Amazon SNS message delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html)
- [Amazon EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
