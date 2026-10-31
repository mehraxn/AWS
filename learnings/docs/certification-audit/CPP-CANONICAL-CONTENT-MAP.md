# CPP Canonical Content Map

This map assigns one primary owner to every major CLF-C02 concept and every service on the official in-scope list checked **2026-07-27**. A path marked **planned** is the authorized destination for a current gap; it is not a claim that the file exists.

Canonical owners teach the subject. Related files should link to them, add local context, and avoid repeating the full definition. Comparison guides own cross-service decisions, not the underlying service definition.

## Major Concepts and Decisions

| Topic | Canonical file | Related evidence | Duplication risk | Recommended action |
|---|---|---|---|---|
| Cloud benefits and economics | `01-cloud-fundamentals/02-cloud-concepts-and-benefits.md` | Billing study guide; global infrastructure | Medium | Link cost lessons back; keep purchasing detail in billing. |
| Shared Responsibility | `01-cloud-fundamentals/01-shared-responsibility-model.md` | IAM, RDS, Lambda, S3 lessons | Medium | Service lessons add only service-specific responsibilities. |
| Global infrastructure | `02-global-infrastructure/01-regions-availability-zones-and-edge.md` | CloudFront, Route 53, HA patterns | Medium | Keep Local Zones/Wavelength as optional context. |
| Well-Architected | `13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md` | Trusted Advisor; Support | Low | Preserve framework/tool distinction. |
| Cloud adoption and migration strategies | `11-migration-and-hybrid-cloud/01-cpp-migration-strategies.md` **planned** | CAF, Migration Hub, DMS, Snowball | High | Create journey/strategy owner; link tool lessons to it. |
| AWS access and operating methods | `10-monitoring-management-and-deployment/01-access-deployment-and-operations.md` **planned** | CloudFormation; deployment models | High | Create Console/CLI/SDK/API/IaC owner. |
| IAM and least privilege | `03-identity-governance-and-organizations/aws-iam/01-overview.md` | IAM child lessons; comparison guides | High | Child lessons teach narrower detail; comparison owns selection. |
| Root user | `03-identity-governance-and-organizations/aws-iam/10-root-user.md` | Root vs IAM comparison | Medium | Keep root-only task facts sourced and dated. |
| Compliance and governance | `09-security-and-compliance/security-and-compliance-overview/01-overview.md` | Artifact, Audit Manager, Organizations | High | Refocus on concepts and link service owners. |
| Encryption and data protection | `13-architecture-and-design-patterns/security/01-data-protection-patterns.md` | KMS, ACM, Secrets Manager | Medium | Service owners define products; pattern owns at-rest/in-transit choice. |
| Security-service selection | `15-comparisons-and-decision-guides/security/01-security-service-selection.md` | Security service lessons | Medium | Apply consistent decision criteria. |
| Monitoring, auditing, and configuration | `15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md` | Config; X-Ray; Flow Logs | Medium | Add canonical service pages only where Level 2 depth requires them. |
| Core compute and storage selection | `15-comparisons-and-decision-guides/compute-and-storage/01-core-selection-guide.md` | Compute and storage service owners | Medium | Keep service definitions in their category lessons. |
| Database selection | `15-comparisons-and-decision-guides/databases/01-database-selection-guide.md` | RDS, Aurora, DynamoDB, ElastiCache | Medium | Add recognition rows for DocumentDB and Neptune. |
| VPC and connectivity | `07-networking-and-content-delivery/networking-guide/01-cloud-practitioner-study-guide.md` | VPC lessons; networking comparisons | High | Add a short start section; retain deep details as optional. |
| Messaging and events | `15-comparisons-and-decision-guides/application-integration/01-sqs-vs-sns-vs-eventbridge.md` | SQS and EventBridge lessons | Medium | Create/link SNS service owner. |
| Pricing models | `12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md` | Reserved Instances; Savings Plans | High | Deprecate duplicated full definitions through links, not deletion. |
| Cost-management tools | `15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md` | Budgets, Cost Explorer, CUR, Calculator | Medium | Service lessons add product detail only. |
| Support and technical resources | `12-billing-pricing-and-support/aws-support/02-support-plans.md` | Customer-enablement lessons | High | Add resource selector; date volatile plan details. |
| AI/ML recognition | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md` | Individual AI service lessons | High | Awareness lessons should link instead of copying the full catalog. |
| Analytics selection | `15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md` | Analytics service lessons | Medium | Preserve workload-to-service criteria. |
| Additional in-scope categories | `14-ai-ml-analytics-and-other-services/01-cpp-additional-service-recognition.md` **planned** | Integration, business, developer, EUC, frontend, IoT | High | Create one Level 1 category guide and link owners. |

## Official In-Scope Services

### Analytics

| Service | Canonical owner | Ownership status |
|---|---|---|
| Amazon Athena | `14-ai-ml-analytics-and-other-services/analytics/amazon-athena/01-overview.md` | Existing |
| Amazon EMR | `14-ai-ml-analytics-and-other-services/analytics/amazon-emr/01-overview.md` | Existing |
| AWS Glue | `14-ai-ml-analytics-and-other-services/analytics/aws-glue/01-overview.md` | Existing |
| Amazon Kinesis | `14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md` | Existing |
| Amazon OpenSearch Service | `14-ai-ml-analytics-and-other-services/analytics/amazon-opensearch-service/01-overview.md` | Planned Level 1 |
| Amazon QuickSight | `14-ai-ml-analytics-and-other-services/analytics/amazon-quicksight/01-overview.md` | Existing; normalize product spelling in visible title |
| Amazon Redshift | `14-ai-ml-analytics-and-other-services/analytics/amazon-redshift/01-overview.md` | Existing |

### Application Integration

| Service | Canonical owner | Ownership status |
|---|---|---|
| Amazon EventBridge | `08-serverless-and-application-integration/amazon-eventbridge/01-overview.md` | Existing |
| Amazon SNS | `08-serverless-and-application-integration/amazon-sns/01-overview.md` | Planned Level 2 |
| Amazon SQS | `08-serverless-and-application-integration/amazon-sqs/01-overview.md` | Existing |
| AWS Step Functions | `08-serverless-and-application-integration/aws-step-functions/01-overview.md` | Existing |

### Business Applications

| Service | Canonical owner | Ownership status |
|---|---|---|
| Amazon Connect | `14-ai-ml-analytics-and-other-services/business-applications/amazon-connect/01-overview.md` | Existing |
| Amazon SES | `08-serverless-and-application-integration/amazon-ses/01-overview.md` | Existing |

### Cloud Financial Management

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS Budgets | `12-billing-pricing-and-support/aws-budgets/01-overview.md` | Existing |
| AWS Cost and Usage Reports | `12-billing-pricing-and-support/aws-cost-and-usage-reports/01-overview.md` | Existing |
| AWS Cost Explorer | `12-billing-pricing-and-support/aws-cost-explorer/01-overview.md` | Existing |
| AWS Marketplace | `12-billing-pricing-and-support/aws-marketplace/01-overview.md` | Planned Level 2 |

### Compute and Containers

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS Batch | `04-compute/aws-batch/01-overview.md` | Existing |
| Amazon EC2 | `04-compute/amazon-ec2/01-overview.md` | Existing |
| AWS Elastic Beanstalk | `04-compute/aws-elastic-beanstalk/01-overview.md` | Existing |
| Amazon Lightsail | `04-compute/amazon-lightsail/01-overview.md` | Existing |
| AWS Outposts | `11-migration-and-hybrid-cloud/aws-outposts/01-overview.md` | Existing |
| Amazon ECR | `04-compute/containers/02-amazon-ecr.md` | Planned Level 1 |
| Amazon ECS | `04-compute/containers/01-ecs-eks-and-fargate.md` | Existing shared owner |
| Amazon EKS | `04-compute/containers/01-ecs-eks-and-fargate.md` | Existing shared owner |

### Customer Enablement

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS Support | `12-billing-pricing-and-support/aws-support/02-support-plans.md` | Existing |

### Database

| Service | Canonical owner | Ownership status |
|---|---|---|
| Amazon Aurora | `06-databases/amazon-aurora/01-overview.md` | Existing |
| Amazon DocumentDB | `06-databases/amazon-documentdb/01-overview.md` | Planned Level 1 |
| Amazon DynamoDB | `06-databases/amazon-dynamodb/01-overview.md` | Existing |
| Amazon ElastiCache | `06-databases/amazon-elasticache/01-overview.md` | Existing |
| Amazon Neptune | `06-databases/amazon-neptune/01-overview.md` | Planned Level 1 |
| Amazon RDS | `06-databases/amazon-rds/01-overview.md` | Existing |

### Developer Tools

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS CLI | `10-monitoring-management-and-deployment/01-access-deployment-and-operations.md` | Planned shared owner |
| AWS CodeBuild | `10-monitoring-management-and-deployment/aws-codebuild/01-overview.md` | Existing |
| AWS CodePipeline | `10-monitoring-management-and-deployment/aws-codepipeline/01-overview.md` | Existing |
| AWS X-Ray | `10-monitoring-management-and-deployment/aws-x-ray/01-overview.md` | Existing |

### End User Computing

| Service | Canonical owner | Ownership status |
|---|---|---|
| Amazon AppStream 2.0 | `14-ai-ml-analytics-and-other-services/end-user-computing/01-service-recognition.md` | Planned shared owner |
| Amazon WorkSpaces | `14-ai-ml-analytics-and-other-services/end-user-computing/01-service-recognition.md` | Planned shared owner |
| Amazon WorkSpaces Secure Browser | `14-ai-ml-analytics-and-other-services/end-user-computing/01-service-recognition.md` | Planned shared owner |

### Frontend Web, Mobile, and IoT

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS Amplify | `14-ai-ml-analytics-and-other-services/business-applications/aws-amplify/01-overview.md` | Existing; directory placement is imperfect but no move authorized |
| AWS AppSync | `08-serverless-and-application-integration/aws-appsync/01-overview.md` | Existing |
| AWS IoT Core | `14-ai-ml-analytics-and-other-services/internet-of-things/aws-iot/01-overview.md` | Existing; normalize visible product name |

### Machine Learning

| Service | Canonical owner | Ownership status |
|---|---|---|
| Amazon Comprehend | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-comprehend/01-overview.md` | Existing |
| Amazon Kendra | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-kendra/01-overview.md` | Existing |
| Amazon Lex | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-lex/01-overview.md` | Existing |
| Amazon Polly | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-polly/01-overview.md` | Existing |
| Amazon Q | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md` | Existing shared recognition owner |
| Amazon Rekognition | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-rekognition/01-overview.md` | Existing |
| Amazon SageMaker AI | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md` | Existing shared recognition owner |
| Amazon Textract | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-textract/01-overview.md` | Existing |
| Amazon Transcribe | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md` | Existing shared recognition owner |
| Amazon Translate | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-translate/01-overview.md` | Existing |

### Management and Governance

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS Auto Scaling | `04-compute/ec2-auto-scaling/01-target-tracking-scaling.md` | Existing evidence; visible scope is EC2-centric |
| AWS CloudFormation | `10-monitoring-management-and-deployment/aws-cloudformation/01-overview.md` | Existing |
| AWS CloudTrail | `15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md` | Existing shared owner; dedicated page optional |
| Amazon CloudWatch | `15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md` | Existing shared owner; dedicated page optional |
| AWS Compute Optimizer | `12-billing-pricing-and-support/customer-enablement/aws-recommendation-resources/01-study-guide.md` | Existing shared owner |
| AWS Config | `10-monitoring-management-and-deployment/aws-config/01-overview.md` | Existing |
| AWS Control Tower | `03-identity-governance-and-organizations/aws-control-tower/01-overview.md` | Existing |
| AWS Health Dashboard | `12-billing-pricing-and-support/aws-health-dashboard/01-overview.md` | Existing |
| AWS License Manager | `12-billing-pricing-and-support/aws-license-manager/01-overview.md` | Planned Level 1 |
| AWS Management Console | `10-monitoring-management-and-deployment/01-access-deployment-and-operations.md` | Planned shared owner |
| AWS Organizations | `03-identity-governance-and-organizations/aws-organizations/01-overview.md` | Existing |
| AWS Service Catalog | `03-identity-governance-and-organizations/aws-service-catalog/01-overview.md` | Existing |
| Service Quotas | `10-monitoring-management-and-deployment/service-quotas/01-overview.md` | Existing |
| AWS Systems Manager | `10-monitoring-management-and-deployment/aws-systems-manager/01-overview.md` | Existing |
| AWS Trusted Advisor | `12-billing-pricing-and-support/aws-trusted-advisor/01-overview.md` | Existing |
| AWS Well-Architected Tool | `13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md` | Existing shared owner |

### Migration and Transfer

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS Application Discovery Service | `11-migration-and-hybrid-cloud/aws-application-discovery-service/01-overview.md` | Existing |
| AWS Application Migration Service | `11-migration-and-hybrid-cloud/aws-application-migration-service/01-overview.md` | Planned Level 1 |
| AWS Database Migration Service | `11-migration-and-hybrid-cloud/aws-database-migration-service/01-overview.md` | Existing |
| Migration Evaluator | `11-migration-and-hybrid-cloud/migration-evaluator/01-overview.md` | Planned Level 1 |
| AWS Migration Hub | `11-migration-and-hybrid-cloud/aws-migration-hub/01-overview.md` | Existing |
| AWS Schema Conversion Tool | `11-migration-and-hybrid-cloud/aws-schema-conversion-tool/01-overview.md` | Existing |
| AWS Snow Family | `11-migration-and-hybrid-cloud/aws-snowball-edge/01-overview.md` | Existing family evidence; rename not authorized |

### Networking and Content Delivery

| Service | Canonical owner | Ownership status |
|---|---|---|
| Amazon API Gateway | `08-serverless-and-application-integration/amazon-api-gateway/01-overview.md` | Existing |
| Amazon CloudFront | `07-networking-and-content-delivery/amazon-cloudfront/01-overview.md` | Existing |
| AWS Direct Connect | `07-networking-and-content-delivery/aws-direct-connect/01-overview.md` | Existing |
| AWS Global Accelerator | `07-networking-and-content-delivery/aws-global-accelerator/01-overview.md` | Existing |
| AWS PrivateLink | `07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md` | Existing evidence; title should clarify PrivateLink |
| Amazon Route 53 | `07-networking-and-content-delivery/amazon-route-53/01-overview.md` | Existing |
| AWS Transit Gateway | `07-networking-and-content-delivery/aws-transit-gateway/01-overview.md` | Existing |
| Amazon VPC | `07-networking-and-content-delivery/amazon-vpc/01-overview.md` | Existing |
| AWS VPN | `07-networking-and-content-delivery/networking-guide/01-cloud-practitioner-study-guide.md` | Existing shared owner |
| AWS Site-to-Site VPN | `07-networking-and-content-delivery/networking-guide/01-cloud-practitioner-study-guide.md` | Existing shared owner |
| AWS Client VPN | `07-networking-and-content-delivery/networking-guide/01-cloud-practitioner-study-guide.md` | Existing shared owner |

### Security, Identity, and Compliance

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS Artifact | `09-security-and-compliance/aws-artifact/01-overview.md` | Existing |
| AWS Audit Manager | `09-security-and-compliance/aws-audit-manager/01-overview.md` | Existing |
| AWS Certificate Manager | `09-security-and-compliance/aws-certificate-manager/01-overview.md` | Existing |
| AWS CloudHSM | `09-security-and-compliance/aws-cloudhsm/01-overview.md` | Planned Level 1 |
| Amazon Cognito | `09-security-and-compliance/amazon-cognito/01-overview.md` | Existing |
| Amazon Detective | `09-security-and-compliance/amazon-detective/01-overview.md` | Planned Level 1 |
| AWS Directory Service | `03-identity-governance-and-organizations/aws-directory-service/01-overview.md` | Existing |
| AWS Firewall Manager | `15-comparisons-and-decision-guides/security/01-security-service-selection.md` | Existing shared owner |
| Amazon GuardDuty | `09-security-and-compliance/amazon-guardduty/01-overview.md` | Existing |
| AWS IAM | `03-identity-governance-and-organizations/aws-iam/01-overview.md` | Existing |
| AWS IAM Identity Center | `03-identity-governance-and-organizations/aws-iam-identity-center/01-overview.md` | Existing |
| Amazon Inspector | `09-security-and-compliance/amazon-inspector/01-overview.md` | Existing |
| AWS KMS | `09-security-and-compliance/aws-kms/01-overview.md` | Existing |
| Amazon Macie | `09-security-and-compliance/amazon-macie/01-overview.md` | Existing |
| AWS Resource Access Manager | `03-identity-governance-and-organizations/aws-resource-access-manager/01-overview.md` | Existing |
| AWS Secrets Manager | `09-security-and-compliance/aws-secrets-manager/01-overview.md` | Existing |
| AWS Security Hub | `09-security-and-compliance/aws-security-hub/01-overview.md` | Existing |
| AWS Shield | `09-security-and-compliance/aws-shield/01-overview.md` | Existing |
| AWS WAF | `09-security-and-compliance/aws-waf/01-overview.md` | Existing |

### Serverless and Storage

| Service | Canonical owner | Ownership status |
|---|---|---|
| AWS Fargate | `04-compute/aws-fargate/01-overview.md` | Existing |
| AWS Lambda | `04-compute/aws-lambda/01-overview.md` | Existing |
| AWS Backup | `05-storage/aws-backup/01-overview.md` | Existing |
| Amazon EBS | `05-storage/amazon-ebs/01-overview.md` | Existing |
| Amazon EFS | `05-storage/amazon-efs/01-overview.md` | Existing |
| AWS Elastic Disaster Recovery | `11-migration-and-hybrid-cloud/aws-elastic-disaster-recovery/01-overview.md` | Planned Level 1 |
| Amazon FSx | `05-storage/amazon-fsx/01-family-and-selection.md` | Existing |
| Amazon S3 | `05-storage/amazon-s3/01-overview.md` | Existing |
| Amazon S3 Glacier | `05-storage/amazon-s3/02-storage-classes.md` | Existing shared owner |
| AWS Storage Gateway | `05-storage/aws-storage-gateway/01-overview.md` | Existing |

## Ownership Findings

- **115/115** official in-scope services now have an existing or explicitly planned canonical destination.
- **98** have meaningful existing canonical evidence; **17** require a new owner or planned shared owner before service-level recognition can be considered structurally complete.
- The highest repetition risk is in IAM, pricing, support resources, networking, migration, and awareness-service catalogs.
- No major learning files are merged or deleted in this phase. Link-first consolidation is safer until each planned owner exists and internal links are verified.
