# Phase 6 Batch 5 Fact Corrections

## Delivery guarantees are scoped, not universal

Affected path:

`15-comparisons-and-decision-guides/application-integration/01-sqs-vs-sns-vs-eventbridge.md`

Related backlog ID:

AWS-031

Previous claim:

Existing shorthand could imply FIFO removes every possible duplicate application side effect.

Corrected claim:

Standard SQS and EventBridge use at-least-once paths and consumers must be idempotent. FIFO exactly-once terminology applies only under documented service conditions; downstream side effects still require idempotency.

Reason:

Retries can repeat delivery or external work.

Official source:

Official SQS, SNS, and EventBridge delivery documentation.

Date checked:

2026-07-23

Severity:

High

## Scheduled EventBridge rules are legacy scheduling

Affected path:

`08-serverless-and-application-integration/amazon-eventbridge/01-overview.md`

Related backlog ID:

AWS-032

Previous claim:

Older study language treats scheduled rules as the default scheduling choice.

Corrected claim:

EventBridge Scheduler is the current recommended scheduling service; scheduled rules remain a legacy feature.

Reason:

Current AWS terminology and product guidance changed.

Official source:

Official EventBridge rules documentation.

Date checked:

2026-07-23

Severity:

Medium

## Step Functions workflow semantics differ

Affected path:

`08-serverless-and-application-integration/aws-step-functions/01-overview.md`

Related backlog ID:

AWS-033

Previous claim:

No canonical owner distinguished execution semantics.

Corrected claim:

AWS documents exactly-once workflow execution for Standard and at-least-once execution for Express; external integrations should remain idempotent.

Reason:

Workflow selection changes duplicate and audit behavior.

Official source:

Official Step Functions workflow-type documentation.

Date checked:

2026-07-23

Severity:

High

## API Gateway features differ by API type

Affected path:

`08-serverless-and-application-integration/amazon-api-gateway/01-overview.md`

Related backlog ID:

AWS-034

Previous claim:

A generic feature list could imply caching, endpoints, usage plans, and authorizers are identical across REST, HTTP, and WebSocket APIs.

Corrected claim:

Feature support differs by API type; REST API stage caching is not universal, API keys are not primary authentication, and throttling is best effort.

Reason:

API-type selection affects security, behavior, and cost.

Official source:

Official API Gateway API-type, authorization, caching, and throttling documentation.

Date checked:

2026-07-23

Severity:

High
