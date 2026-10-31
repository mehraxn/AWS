# Limited Gap Summary

This is intentionally a coarse evidence-based gap scan, not a certification coverage audit. It describes the present corpus only and does not propose creating empty lessons.

## Major obvious CPP gaps or thin areas

- Cloud fundamentals are thin as a standalone area: there is no dedicated cloud concepts, shared-responsibility, elasticity, high availability, or economies-of-scale lesson set. Relevant ideas are scattered through service notes.
- Global infrastructure is very thin: only Local Zones and Wavelength map directly to category 02; there is no focused Regions/AZs/edge-locations overview.
- Databases are narrow: Aurora and ElastiCache are present, but no dedicated RDS overview, DynamoDB overview, or database-selection guide exists. The file under `h) RDS/` is about TLS, not RDS fundamentals.
- Serverless/application integration is limited to Lambda, API Gateway, AppSync, SQS, and SES; event buses, notification/pub-sub, and workflow orchestration are not represented as standalone notes.

## Major obvious SAA gaps or thin areas

- No dedicated load balancer or Auto Scaling Group overview exists; only SSL termination and a target-tracking policy are present.
- RDS is not covered as a general service despite Aurora mode notes and one TLS-related file.
- DynamoDB, SNS, EventBridge, Step Functions, Kinesis Data Streams, ECS, EKS, and container architecture are absent or represented only indirectly.
- Disaster recovery, backup strategy, multi-account landing-zone design, caching patterns, decoupling patterns, and multi-tier reference architectures are sparse as standalone design lessons.
- Network ACLs, subnets/route tables, internet gateways, VPN connections, and hybrid DNS lack focused atomic notes despite a broad networking guide.

## Existing content that appears out of place

- Four prompt/template files are mixed into the repository root and service-note/comparison directories; move them to `docs/templates/aws-study-prompts/` after review.
- `Amazon Elastic Transcoder .md` covers a service whose AWS support ended in 2025; archive it with migration context rather than deleting it.
- `SSL & TLS with Load Balancer and RDS.md` is a transport-security/design note, not an RDS service overview.
- `AWS Charging Patterns and Data Transfer Costs.md` currently sits with gateways but belongs with billing/pricing.
- IAM policies are split between service explanations and Tools & Policies; the proposed IAM directory reunifies them.

## Excessively duplicated topics

- KMS has three broad notes; S3 has three broad notes.
- Sixteen other service/version pairs need consolidation or explicit separation, detailed in `DUPLICATE-ANALYSIS.md`.
- Support Plans has both a broad note and a much larger complete guide; retain one canonical guide after review.

## Topics represented by one isolated note

There are **85** proposed service/concept directories with one source document. This is not automatically a defect. Particularly notable isolated topics include Amazon Athena, Amazon Redshift, AWS Glue, Amazon QuickSight, Amazon Kinesis Video Streams, AWS IoT, AWS IoT Greengrass, Amazon Connect, Amazon SES, AWS AppSync, AWS WAF, AWS Shield, Amazon Macie, AWS Certificate Manager, AWS Direct Connect, AWS Wavelength, and AWS Local Zones.

The complete isolated-source list is derivable from the one-row service/concept groups in `INVENTORY.md` and `MOVE-MAP.csv`; no missing lesson files should be created solely to make those directories look complete.

