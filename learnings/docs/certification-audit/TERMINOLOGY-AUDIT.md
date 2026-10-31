# Terminology Audit

Checked: **2026-07-21**. No lesson was edited.

| Repository wording | Current official wording | Affected paths | Severity | Recommended correction | Official source |
|---|---|---|---|---|---|
| Amazon QuickSight | Amazon Quick (official SAA list wording) | `14-ai-ml-analytics-and-other-services/analytics/amazon-quicksight/01-overview.md` and references | medium; official materials are in transition | Confirm product-page branding before changing canonical title | [SAA scope](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html) |
| Amazon SageMaker / older Studio wording | Amazon SageMaker AI in current exam scope | Files found through service matrix/manual review | medium | Use current service name while explaining older source terminology | [SAA scope](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html) |
| AWS Personal Health Dashboard | AWS Health Dashboard | `12-billing-pricing-and-support/aws-health-dashboard/01-overview.md` and archived provenance | high | Correct active prose after verifying current AWS Health docs | [CPP guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) |
| AWS Single Sign-On | AWS IAM Identity Center | IAM/Organizations lessons if phrase appears | high | Replace active branding, preserving historical context where needed | [SAA guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html) |
| Amazon Elastic Transcoder | Retired service; official SAA guide still lists it in one guide surface | `90-archive/obsolete-services/amazon-elastic-transcoder.md` | low/archive | Retain as historical archive and flag official-list inconsistency | [SAA scope](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html) |
| AWS CodeCommit | No longer available to new customers; scope relevance requires review | `10-monitoring-management-and-deployment/aws-codecommit/01-overview.md` | medium | Keep supplementary until official scope and service status are reconciled | [CPP scope](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html) |

Capitalization and acronym variants are listed per file in the canonical inventory. These findings require source-by-source confirmation before mechanical replacement.

## Phase 6 Batch 9 update — 2026-07-25

- New Batch 9 content uses **Amazon Data Firehose**, the current name for the former Amazon Kinesis Data Firehose.
- New analytics guidance uses **Amazon Quick** for the broader service and **Amazon Quick Sight** for its business-intelligence capability. The older `amazon-quicksight` path remains unchanged pending a separately authorized rewrite.
- New AI/ML guidance distinguishes the broader next-generation **Amazon SageMaker** platform from **Amazon SageMaker AI**, the renamed build/train/deploy ML service.
