# Phase 6 Batch Plan

Authority: `PHASE-6-CONTENT-BACKLOG.csv`. Only rows with the selected batch may be implemented. Dependencies must be satisfied first.

## Batch 1: Critical foundations and factual corrections

- Purpose: Critical foundations and factual corrections.
- Included backlog IDs: AWS-001, AWS-002, AWS-003, AWS-004, AWS-005, AWS-006
- Certification focus: CPP, both
- Official domains addressed: Cloud Concepts, Cloud Concepts / Resilience, Cloud Technology / Resilience, Cloud foundations, Multiple, Security
- Target categories: 01-cloud-fundamentals, 02-global-infrastructure, 03-identity-governance-and-organizations, 13-architecture-and-design-patterns, manual-review
- Exact target files:

  - `01-cloud-fundamentals/01-shared-responsibility-model.md` (AWS-001)
  - `01-cloud-fundamentals/02-cloud-concepts-and-benefits.md` (AWS-002)
  - `02-global-infrastructure/01-regions-availability-zones-and-edge.md` (AWS-003)
  - `03-identity-governance-and-organizations/aws-iam/01-overview.md` (AWS-004)
  - `13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md` (AWS-005)
  - `manual-review` (AWS-006)

- Dependencies: AWS-002, none
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 2.

## Batch 2: Core compute and storage

- Purpose: Core compute and storage.
- Included backlog IDs: AWS-007, AWS-008, AWS-009, AWS-010, AWS-011, AWS-012, AWS-013, AWS-014, AWS-015, AWS-016, AWS-017, AWS-018, AWS-019
- Certification focus: SAA, both
- Official domains addressed: Compute, Compute/Storage, Resilience/Performance, Storage, Storage/Resilience
- Target categories: 04-compute, 05-storage, 15-comparisons-and-decision-guides
- Exact target files:

  - `04-compute/amazon-ec2/01-overview.md` (AWS-007)
  - `04-compute/elastic-load-balancing/01-overview.md` (AWS-008)
  - `04-compute/ec2-auto-scaling/01-target-tracking-scaling.md` (AWS-009)
  - `04-compute/aws-lambda/01-overview.md` (AWS-010)
  - `04-compute/containers/01-ecs-eks-and-fargate.md` (AWS-011)
  - `05-storage/amazon-s3/01-overview.md` (AWS-012)
  - `05-storage/amazon-ebs/01-overview.md` (AWS-013)
  - `05-storage/ec2-instance-store/01-overview.md` (AWS-014)
  - `05-storage/amazon-efs/01-overview.md` (AWS-015)
  - `05-storage/amazon-fsx/01-family-and-selection.md` (AWS-016)
  - `05-storage/aws-storage-gateway/01-overview.md` (AWS-017)
  - `05-storage/aws-backup/01-overview.md` (AWS-018)
  - `15-comparisons-and-decision-guides/compute-and-storage/01-core-selection-guide.md` (AWS-019)

- Dependencies: AWS-003; AWS-004, AWS-007, AWS-007; AWS-009; AWS-010; AWS-012, AWS-008, none
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 3.

## Batch 3: Core networking and content delivery

- Purpose: Core networking and content delivery.
- Included backlog IDs: AWS-020, AWS-021, AWS-022, AWS-023, AWS-024, AWS-025
- Certification focus: SAA, both
- Official domains addressed: Networking
- Target categories: 07-networking-and-content-delivery, 15-comparisons-and-decision-guides
- Exact target files:

  - `07-networking-and-content-delivery/amazon-vpc/01-overview.md` (AWS-020)
  - `07-networking-and-content-delivery/amazon-vpc/09-subnets-route-tables-and-internet-gateways.md` (AWS-021)
  - `15-comparisons-and-decision-guides/networking/03-security-groups-vs-network-acls.md` (AWS-022)
  - `07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md` (AWS-023)
  - `15-comparisons-and-decision-guides/networking/02-vpc-connectivity-options.md` (AWS-024)
  - `15-comparisons-and-decision-guides/networking/04-dns-edge-and-global-routing.md` (AWS-025)

- Dependencies: AWS-003, AWS-020, none
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 4.

## Batch 4: Databases and caching

- Purpose: Databases and caching.
- Included backlog IDs: AWS-026, AWS-027, AWS-028, AWS-029, AWS-030
- Certification focus: SAA, both
- Official domains addressed: Databases
- Target categories: 06-databases, 15-comparisons-and-decision-guides
- Exact target files:

  - `06-databases/amazon-rds/01-overview.md` (AWS-026)
  - `06-databases/amazon-aurora/01-overview.md` (AWS-027)
  - `06-databases/amazon-dynamodb/01-overview.md` (AWS-028)
  - `06-databases/amazon-elasticache/01-overview.md` (AWS-029)
  - `15-comparisons-and-decision-guides/databases/01-database-selection-guide.md` (AWS-030)

- Dependencies: AWS-026, AWS-026; AWS-027; AWS-028; AWS-029, none
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 5.

## Batch 5: Serverless and application integration

- Purpose: Serverless and application integration.
- Included backlog IDs: AWS-031, AWS-032, AWS-033, AWS-034
- Certification focus: both
- Official domains addressed: Application Integration, Serverless
- Target categories: 08-serverless-and-application-integration, 15-comparisons-and-decision-guides
- Exact target files:

  - `15-comparisons-and-decision-guides/application-integration/01-sqs-vs-sns-vs-eventbridge.md` (AWS-031)
  - `08-serverless-and-application-integration/amazon-eventbridge/01-overview.md` (AWS-032)
  - `08-serverless-and-application-integration/aws-step-functions/01-overview.md` (AWS-033)
  - `08-serverless-and-application-integration/amazon-api-gateway/01-overview.md` (AWS-034)

- Dependencies: AWS-010, none
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 6.

## Batch 6: Security, monitoring, and governance

- Purpose: Security, monitoring, and governance.
- Included backlog IDs: AWS-035, AWS-036, AWS-037, AWS-038, AWS-039
- Certification focus: SAA, both
- Official domains addressed: Operations, Security
- Target categories: 10-monitoring-management-and-deployment, 13-architecture-and-design-patterns, 15-comparisons-and-decision-guides
- Exact target files:

  - `13-architecture-and-design-patterns/security/01-data-protection-patterns.md` (AWS-035)
  - `15-comparisons-and-decision-guides/security/01-security-service-selection.md` (AWS-036)
  - `15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md` (AWS-037)
  - `13-architecture-and-design-patterns/security/02-multi-account-governance.md` (AWS-038)
  - `10-monitoring-management-and-deployment/aws-systems-manager/01-overview.md` (AWS-039)

- Dependencies: AWS-004, none
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 7.

## Batch 7: Resilience and architecture patterns

- Purpose: Resilience and architecture patterns.
- Included backlog IDs: AWS-040, AWS-041, AWS-042, AWS-043
- Certification focus: SAA
- Official domains addressed: Resilience
- Target categories: 13-architecture-and-design-patterns
- Exact target files:

  - `13-architecture-and-design-patterns/01-highly-available-web-applications.md` (AWS-040)
  - `13-architecture-and-design-patterns/02-disaster-recovery-strategies.md` (AWS-041)
  - `13-architecture-and-design-patterns/03-event-driven-and-decoupled-systems.md` (AWS-042)
  - `13-architecture-and-design-patterns/04-serverless-application-patterns.md` (AWS-043)

- Dependencies: AWS-018, Batch 5, Batches 2-4
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 8.

## Batch 8: Billing, pricing, and support

- Purpose: Billing, pricing, and support.
- Included backlog IDs: AWS-044, AWS-045, AWS-046, AWS-047
- Certification focus: CPP, both
- Official domains addressed: Billing, Cost optimization, Pricing, Support
- Target categories: 12-billing-pricing-and-support, 15-comparisons-and-decision-guides
- Exact target files:

  - `12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md` (AWS-044)
  - `12-billing-pricing-and-support/aws-support/02-support-plans.md` (AWS-045)
  - `15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md` (AWS-046)
  - `12-billing-pricing-and-support/aws-billing-and-cost-management/03-data-transfer-costs.md` (AWS-047)

- Dependencies: AWS-006, none
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 9.

## Batch 9: Analytics, AI/ML, and awareness services

- Purpose: Analytics, AI/ML, and awareness services.
- Included backlog IDs: AWS-048, AWS-049, AWS-050
- Certification focus: CPP, both
- Official domains addressed: AI/ML, Analytics
- Target categories: 14-ai-ml-analytics-and-other-services, 15-comparisons-and-decision-guides
- Exact target files:

  - `14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md` (AWS-048)
  - `15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md` (AWS-049)
  - `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md` (AWS-050)

- Dependencies: AWS-006, AWS-047, none
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Batch 10.

## Batch 10: Comparisons and exam preparation

- Purpose: Comparisons and exam preparation.
- Included backlog IDs: AWS-051, AWS-052, AWS-053, AWS-054
- Certification focus: CPP, SAA, both
- Official domains addressed: All
- Target categories: 16-exam-preparation, manual-review
- Exact target files:

  - `16-exam-preparation/01-cpp-scenario-reasoning.md` (AWS-051)
  - `16-exam-preparation/02-saa-architecture-scenario-reasoning.md` (AWS-052)
  - `manual-review` (AWS-053)
  - `manual-review` (AWS-054)

- Dependencies: Batches 1-10, Batches 1-9
- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.
- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.
- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.
- Expected next batch: Phase 6 re-audit and closure review.
