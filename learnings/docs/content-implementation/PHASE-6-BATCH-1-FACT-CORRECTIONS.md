# Phase 6 Batch 1 Fact Corrections

## Correction: AWS Health product name

Affected path: `12-billing-pricing-and-support/aws-health-dashboard/01-overview.md` and direct active support-plan references

Related backlog ID: AWS-006

Previous claim: The active product was called AWS Personal Health Dashboard.

Corrected claim: Current AWS documentation calls the console AWS Health Dashboard.

Reason: Current official branding replaced the older name.

Official source: [AWS Health User Guide](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)

Date checked: 2026-07-22

Severity: high

## Correction: Amazon Quick terminology

Affected path: `14-ai-ml-analytics-and-other-services/analytics/amazon-quicksight/01-overview.md` and direct active references

Related backlog ID: AWS-006

Previous claim: Amazon QuickSight was the current standalone service name.

Corrected claim: Amazon QuickSight was rebranded to Amazon Quick; the BI capability continues as Amazon Quick Sight within the broader platform. The lesson explains the transition because current exam surfaces may differ.

Reason: Official product documentation records the October 2025 rebrand.

Official source: [Amazon Quick document history](https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html)

Date checked: 2026-07-22

Severity: medium

## Correction: Amazon SageMaker AI name

Affected path: active references in the Savings Plans, Amazon Rekognition, and AWS IoT Greengrass lessons

Related backlog ID: AWS-006

Previous claim: The managed ML service was named Amazon SageMaker.

Corrected claim: The managed ML service is Amazon SageMaker AI; legacy API namespaces remain unchanged.

Reason: AWS renamed the service on 2024-12-03.

Official source: [What is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

Date checked: 2026-07-22

Severity: medium

## Correction: IAM permission guardrails

Affected path: `03-identity-governance-and-organizations/aws-iam/01-overview.md`

Related backlog ID: AWS-004

Previous claim: The overview did not explain whether permissions boundaries and SCPs grant permissions or how explicit deny affects an allow.

Corrected claim: Permissions boundaries and SCPs limit maximum effective permissions but do not grant them; an explicit deny overrides an allow.

Reason: These distinctions are required for accurate CPP recognition and SAA policy evaluation.

Official source: [IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

Date checked: 2026-07-22

Severity: high
