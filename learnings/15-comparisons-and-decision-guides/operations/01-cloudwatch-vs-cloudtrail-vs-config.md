# Amazon CloudWatch vs AWS CloudTrail vs AWS Config

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Quick Decision

- **CloudWatch:** What is happening to workload health and performance?
- **CloudTrail:** Who or what performed supported AWS API and account activity?
- **AWS Config:** What was a supported resource's configuration, how did it change, and is it compliant?
- **AWS X-Ray:** How did one distributed request travel through an application?

Production operations normally combine these signals rather than choosing only one.

## Decision Table

| Need | Primary service | Evidence | Typical action |
|---|---|---|---|
| CPU, latency, errors, queue depth, log patterns | CloudWatch | Metrics and logs | Alarm, dashboard, scale, notify, investigate |
| API actor, source, request, and time | CloudTrail | Events and trails/event data stores | Audit, detect activity, investigate identity |
| Configuration timeline and policy evaluation | AWS Config | Configuration items and Config rules | Assess compliance, remediate drift |
| End-to-end request latency and dependencies | AWS X-Ray | Traces, segments, subsegments, service graph | Find slow or failing application components |

## Amazon CloudWatch

CloudWatch collects and analyzes operational telemetry. Core capabilities include metrics, logs, alarms, dashboards, metric math, anomaly detection, and event-driven integrations. AWS services publish selected metrics; applications can publish custom metrics and logs.

An alarm evaluates a metric or composite condition and can notify or initiate supported actions. Design alarms around user impact and actionable symptoms, not every fluctuation. Missing data, dimensions, aggregation period, and statistic choice can change an alarm's meaning.

CloudWatch Logs can centralize application and service logs, query them, create metric filters, and route subscriptions. Logs are not automatically complete: applications and services must be configured to emit the evidence you need.

## AWS CloudTrail

CloudTrail records supported AWS API and account activity as events. Management events describe control-plane operations; data events and other event categories provide additional visibility when configured and can have separate cost considerations.

A trail delivers selected events to durable destinations for ongoing audit; CloudTrail Lake event data stores support collection, retention, querying, and analysis patterns. CloudTrail is the primary answer for questions such as who changed a security group or called a KMS API.

CloudTrail is not a performance-monitoring system. You can route or analyze events to create operational detection, but the source evidence remains API/account activity.

## AWS Config

AWS Config records supported resource configurations and relationships and maintains configuration history when recording is enabled. Config rules evaluate resources against desired conditions and report compliance; conformance packs group rules and remediation guidance.

Config does not prevent every change. A preventive policy such as an SCP or IAM denial acts before a request, while Config generally records/evaluates resource state and can trigger a separate remediation workflow. Coverage depends on enabled resource types, Regions, recorder settings, and rule scope.

## AWS X-Ray

X-Ray provides distributed tracing concepts such as traces, segments, subsegments, annotations, and service graphs. It helps explain which dependency made a request slow or failed. Instrumentation and sampling determine what is visible.

CloudWatch tells you that latency increased across a service; X-Ray can show where sampled requests spent time. Traces can complement logs and metrics but do not replace them.

## How the Signals Work Together

Example: a production API starts returning errors.

1. CloudWatch alarm detects an elevated error metric.
2. CloudWatch Logs provides application exceptions and correlation identifiers.
3. X-Ray traces show latency or faults in a downstream dependency.
4. CloudTrail shows whether an operator or automation changed the service configuration.
5. AWS Config shows the before/after resource state and whether the new state violates a rule.
6. EventBridge and Systems Manager Automation can coordinate a controlled response.

This pattern separates symptoms, request flow, API activity, and resource state instead of expecting one tool to answer every question.

## Security, Retention, and Multi-Account Design

Centralize telemetry in dedicated logging or security accounts where requirements justify it. Encrypt destinations, restrict deletion, protect cross-account roles, validate source identity, and monitor gaps in delivery. Select retention from audit and incident-response needs; do not assume every default lasts indefinitely.

CloudWatch, CloudTrail, Config, and X-Ray are Regional in important ways, while some aggregation features can present data centrally. Enable and aggregate the required Regions explicitly.

## Cost Considerations

Cost drivers include custom metrics, log ingestion/storage/querying, alarms, traces, CloudTrail event copies and data events, event data stores, Config configuration items, rule evaluations, aggregators, and destination services. Collect evidence intentionally, but do not remove security-critical telemetry merely to reduce cost.

## CPP Exam Focus

- CloudWatch = metrics, logs, alarms, dashboards.
- CloudTrail = AWS API and account activity.
- Config = resource configuration history and compliance.
- X-Ray = distributed traces.

## SAA Scenarios

1. Alarm when a queue grows faster than workers consume it: CloudWatch metric and alarm.
2. Determine who deleted a resource: CloudTrail.
3. Show when a bucket became public and evaluate policy: Config, correlated with CloudTrail for the actor.
4. Find which microservice adds latency: X-Ray plus application metrics/logs.
5. Build central audit evidence across accounts: organization-aware CloudTrail/Config designs and centralized protected destinations.

## Common Mistakes

- Using CloudTrail as the answer for CPU or application latency.
- Assuming Config prevents noncompliant changes by itself.
- Assuming CloudWatch collects every application log automatically.
- Treating an X-Ray sample as a complete audit record.
- Enabling services in one Region and claiming organization-wide coverage.

## Knowledge Check

1. Which service records supported API activity? 2. Which service evaluates resource configuration? 3. Which service creates metric alarms? 4. Which service follows a distributed request? 5. Which two services help show both who changed a resource and what its configuration became?

<details><summary>Answers</summary>

1. CloudTrail. 2. AWS Config. 3. CloudWatch. 4. X-Ray. 5. CloudTrail and AWS Config.

</details>

## Canonical Lessons

- [AWS Config](../../10-monitoring-management-and-deployment/aws-config/01-overview.md)
- [AWS X-Ray](../../10-monitoring-management-and-deployment/aws-x-ray/01-overview.md)
- [AWS Systems Manager](../../10-monitoring-management-and-deployment/aws-systems-manager/01-overview.md)

## References

Checked: 2026-07-24.

- [CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
- [What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- [AWS Config compliance history](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource-console.html)
- [AWS X-Ray concepts](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html)
