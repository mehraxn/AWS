# Phase 4 Misplacement Corrections

| Original canonical path | Corrected canonical path | Reason |
|---|---|---|
| `08-serverless-and-application-integration/amazon-ses/02-session-manager.md` | `10-monitoring-management-and-deployment/aws-systems-manager/02-session-manager.md` | Session Manager is a Systems Manager capability, not part of Amazon SES. |
| `08-serverless-and-application-integration/aws-lambda/01-overview.md` | `04-compute/aws-lambda/01-overview.md` | Lambda is canonically owned by compute. |
| `10-monitoring-management-and-deployment/aws-elastic-beanstalk/01-overview.md` | `04-compute/aws-elastic-beanstalk/01-overview.md` | Elastic Beanstalk is application compute and deployment. |
| `13-architecture-and-design-patterns/amazon-ec2-auto-scaling/03-target-tracking-scaling.md` | `04-compute/ec2-auto-scaling/01-target-tracking-scaling.md` | EC2 Auto Scaling is compute-owned. |
| `13-architecture-and-design-patterns/amazon-ec2/02-placement-groups.md` | `04-compute/amazon-ec2/07-placement-groups.md` | Placement groups are an EC2 feature. |
| `11-migration-and-hybrid-cloud/aws-storage-gateway/` | `05-storage/aws-storage-gateway/` | Storage Gateway is storage-owned; migration pages may link to it. |
| `14-ai-ml-analytics-and-other-services/amazon-redshift/` | `14-ai-ml-analytics-and-other-services/analytics/amazon-redshift/` | Redshift is primarily analytics. |
| `14-ai-ml-analytics-and-other-services/aws-schema-conversion-tool-aws-sct/` | `11-migration-and-hybrid-cloud/aws-schema-conversion-tool/` | Schema conversion supports database migration. |
| `10-monitoring-management-and-deployment/aws-managed-services/` | `12-billing-pricing-and-support/customer-enablement/aws-managed-services/` | AMS is customer operations enablement/support. |
| `14-ai-ml-analytics-and-other-services/aws-partner-network/` | `12-billing-pricing-and-support/customer-enablement/aws-partner-network/` | APN is customer and partner enablement. |
| `04-compute/amazon-ec2/03-instance-store.md` | `05-storage/ec2-instance-store/01-overview.md` | Instance store is storage-owned with EC2 cross-reference. |

## Required ownership confirmations

- Elastic Load Balancing: the legacy `g)ELB & ASG/` directory contained no remaining source file at consolidation time. No placeholder lesson was created; future ELB content is owned by `04-compute/elastic-load-balancing/`.
- EC2 Auto Scaling: the existing target-tracking lesson is now under `04-compute/ec2-auto-scaling/`.
- AWS Outposts remained correctly owned by `11-migration-and-hybrid-cloud/aws-outposts/`.
- AWS Trusted Advisor remained correctly owned by `12-billing-pricing-and-support/aws-trusted-advisor/`.
- Amazon Redshift moved into the analytics subgroup under category 14.
- EC2 numbering is unique: reserved instances is `03`, key pairs `04`, Instance Connect `05`, RDP `06`, and placement groups `07`; instance store moved to storage.
