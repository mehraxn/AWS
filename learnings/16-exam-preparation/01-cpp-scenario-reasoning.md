# AWS Certified Cloud Practitioner Scenario Reasoning

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

The CLF-C02 exam tests whether you can recognize cloud concepts, security responsibilities, AWS services, pricing tools, and support choices in short business scenarios. The safest method is to identify the requirement first and choose the service or concept that satisfies it most directly.

This guide contains original study scenarios. It does not reproduce or reconstruct real certification questions. The official exam guide and in-scope service list were checked on **2026-07-25**; AWS states that its service list is non-exhaustive and can change.

## Official Domain Map

| CLF-C02 domain | Weight | Question focus | Canonical review |
|---|---:|---|---|
| Cloud Concepts | 24% | Cloud value, economics, elasticity, design principles, and migration benefits | [Cloud concepts and benefits](../01-cloud-fundamentals/02-cloud-concepts-and-benefits.md) |
| Security and Compliance | 30% | Shared responsibility, IAM, governance, encryption, detection, and compliance resources | [Shared responsibility](../01-cloud-fundamentals/01-shared-responsibility-model.md), [security selection](../15-comparisons-and-decision-guides/security/01-security-service-selection.md) |
| Cloud Technology and Services | 34% | Service recognition, deployment, global infrastructure, compute, networking, storage, databases, analytics, and AI/ML | [Service and concept index](../docs/service-index.md) |
| Billing, Pricing, and Support | 12% | Pricing models, cost tools, data transfer, Support plans, Trusted Advisor, and AWS Health | [Pricing fundamentals](../12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md), [cost tool selection](../15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md) |

Weights describe the official content outline, not a guarantee about a particular exam form.

## A Four-Step Reasoning Method

1. **Name the business outcome.** Examples: reduce capital expense, protect credentials, query S3, forecast cost, or receive technical support.
2. **Underline the constraint.** Look for words such as managed, serverless, shared file storage, object storage, lowest operational effort, or historical spend.
3. **Classify the answer type.** Is the question asking for a cloud benefit, responsibility, service, pricing model, tool, or support resource?
4. **Eliminate near matches.** Explain why each distractor solves a different problem before choosing the direct match.

Do not select an answer only because it is a familiar AWS service. The service must satisfy the stated outcome and constraint.

## Domain 1: Cloud Concepts Scenarios

### Scenario: variable demand

A retailer experiences unpredictable traffic and wants resources to grow and shrink with demand rather than buying servers for the annual peak.

- **Requirement:** match capacity to demand.
- **Best concept:** elasticity.
- **Why:** elastic resources can scale out and in as demand changes.
- **Distractor reasoning:** high availability reduces interruption risk, while economies of scale can reduce cost; neither directly describes matching capacity to current demand.

### Scenario: replace upfront infrastructure spending

A startup wants to avoid purchasing data-center hardware before it knows whether a product will succeed.

- **Requirement:** exchange large upfront investment for usage-based spending.
- **Best concept:** trade capital expense for variable expense.
- **Distractor reasoning:** global reach and agility are cloud benefits, but the scenario is specifically about the spending model.

## Domain 2: Security and Compliance Scenarios

### Scenario: patch responsibility

A company runs an application on Amazon EC2 and asks who patches the guest operating system.

- **Requirement:** identify responsibility for the guest OS on an infrastructure service.
- **Best answer:** the customer.
- **Why:** AWS secures the underlying cloud infrastructure; the customer manages the EC2 guest OS, applications, data, and configured access.
- **Distractor reasoning:** AWS manages more of the stack for managed and serverless services, but that does not transfer the EC2 guest-OS responsibility.

### Scenario: investigate an exposed S3 bucket

A security team wants a history of API actions that changed an S3 bucket policy.

- **Requirement:** audit AWS API activity.
- **Best service:** AWS CloudTrail.
- **Distractor reasoning:** Amazon CloudWatch monitors metrics, logs, events, and alarms; AWS Config records configuration state and evaluates rules. CloudTrail answers who called which API and when.

### Scenario: compliance documents

An auditor needs AWS compliance reports and agreements.

- **Requirement:** access AWS compliance documentation.
- **Best service:** AWS Artifact.
- **Distractor reasoning:** Amazon Inspector assesses supported workloads for vulnerabilities, while AWS Audit Manager helps collect audit evidence. Neither is the portal for downloading AWS compliance reports.

## Domain 3: Technology and Services Scenarios

### Scenario: serverless SQL over S3

An analyst wants to run occasional SQL queries directly against log files in Amazon S3 without maintaining a database cluster.

- **Requirement:** serverless interactive SQL over S3.
- **Best service:** Amazon Athena.
- **Distractor reasoning:** Amazon Redshift is a managed data warehouse; AWS Glue catalogs and transforms data; Amazon Quick Sight visualizes data.

### Scenario: shared Linux file storage

Several Linux EC2 instances need concurrent access to the same elastic file system.

- **Requirement:** managed shared file storage.
- **Best service:** Amazon EFS.
- **Distractor reasoning:** Amazon EBS is block storage normally attached within an Availability Zone, while Amazon S3 is object storage rather than a mounted shared POSIX-style file system.

### Scenario: decouple work items

An application must place orders in a durable queue so worker components can process them independently.

- **Requirement:** queue and decouple work.
- **Best service:** Amazon SQS.
- **Distractor reasoning:** Amazon SNS fans messages out to subscribers; Amazon EventBridge routes events by rules. SQS directly provides a work queue with consumer-controlled processing.

### Scenario: foundation-model application

A team wants managed access to foundation models for a generative-AI assistant without operating model-serving infrastructure.

- **Requirement:** build a managed generative-AI application using foundation models.
- **Best service:** Amazon Bedrock.
- **Distractor reasoning:** Amazon SageMaker AI supports broader custom ML building, training, deployment, and operations; purpose-built AI services handle narrower tasks such as transcription or document extraction.

## Domain 4: Billing, Pricing, and Support Scenarios

### Scenario: cost forecast

A finance team wants to estimate the future cost of a planned architecture before deploying it.

- **Requirement:** pre-deployment estimate.
- **Best tool:** AWS Pricing Calculator.
- **Distractor reasoning:** AWS Cost Explorer analyzes and forecasts existing usage and spend; AWS Budgets tracks thresholds and can alert or initiate configured actions.

### Scenario: urgent production case

A company needs to open a technical support case for a production workload.

- **Requirement:** AWS technical support case access.
- **Best answer:** choose a current AWS Support plan that includes the required technical support capability and response target.
- **Distractor reasoning:** AWS re:Post is a community knowledge resource, AWS Health reports account and service events, and Trusted Advisor provides recommendations; they are not substitutes for plan-based technical support.

## Common Distractor Patterns

- **Monitoring versus auditing:** CloudWatch observes workloads; CloudTrail records API activity; Config tracks resource configuration and compliance.
- **Storage type:** S3 is object, EBS is block, and EFS is shared file storage.
- **Cost timing:** Pricing Calculator estimates planned resources; Cost Explorer analyzes existing spend; Budgets tracks thresholds.
- **Messaging:** SQS queues, SNS publishes to subscribers, and EventBridge routes events.
- **Analytics layers:** Glue catalogs/transforms, Athena queries, Redshift warehouses, and Quick Sight visualizes.
- **AI selection:** use a purpose-built AI service for a matched task, Bedrock for foundation-model applications, and SageMaker AI for custom ML lifecycles.

## Exam-Preparation Integrity

- Use official exam guides to define scope; do not rely on remembered question banks.
- Treat service lists as non-exhaustive and subject to change.
- Practice explaining why alternatives fail instead of memorizing answer letters.
- Never share or request content recalled from a live certification exam.

## Knowledge Check

1. **A company wants an alert when monthly spend crosses a threshold. Which tool fits?**  
   **Answer:** AWS Budgets, because it tracks configured budget thresholds. Cost Explorer is better for analyzing historical cost and usage.
2. **Which service records a call that changed a security group?**  
   **Answer:** AWS CloudTrail, because the requirement is API activity history.
3. **Why is Amazon Redshift not the direct answer for occasional SQL over S3 with no cluster management?**  
   **Answer:** Redshift is a managed analytical warehouse; Athena directly provides serverless query-on-demand over S3 data.
4. **Who patches an EC2 guest operating system?**  
   **Answer:** The customer under the shared responsibility model.
5. **What should you do when two services appear plausible?**  
   **Answer:** Return to the exact outcome and constraints, then state what problem each service actually solves.

## References

Checked **2026-07-25**.

- [AWS Certified Cloud Practitioner CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
- [CLF-C02 in-scope AWS services and features](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)
- [AWS Certification exam preparation](https://aws.amazon.com/certification/certification-prep/)
