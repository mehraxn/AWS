# Complete Proposed Repository Tree

This is a migration plan only; none of these paths has been applied. Every one of the 185 existing files is represented. When multiple current files map to one path, that path is a planned merge target and each source is listed.

```text
02-global-infrastructure/
  aws-local-zones/
    01-overview.md
      <- a) Service Explanations/AWS Local Zones.md
  aws-wavelength/
    01-overview.md
      <- a) Service Explanations/AWS Wavelength.md
03-identity-governance-and-organizations/
  aws-control-tower/
    01-overview.md
      <- a) Service Explanations/AWS Control Tower.md
  aws-directory-service/
    01-overview.md
      <- a) Service Explanations/AWS Directory Service.md
  aws-iam-identity-center/
    01-overview.md
      <- a) Service Explanations/AWS IAM Identity Center.md
  aws-iam/
    01-overview.md
      <- a) Service Explanations/AWS IAM (Identity and Access Management).md
    02-users.md
      <- a) Service Explanations/AWS IAM User .md
    03-groups.md
      <- a) Service Explanations/AWS IAM Group .md
    04-roles.md
      <- a) Service Explanations/AWS IAM Role .md
    05-customer-managed-policies.md
      <- a) Service Explanations/AWS Customer Managed Policies.md [merge-later]
      <- d) Tools & Policies/AWS Customer Managed Policies (Claude version).txt
    06-inline-policies.md
      <- d) Tools & Policies/IAM Inline Policy.md
    07-read-only-access-policy.md
      <- a) Service Explanations/AWS IAM (ReadOnlyAccess).md
    08-administrator-access-policy.md
      <- a) Service Explanations/Administrator Access.md
    09-access-analyzer.md
      <- a) Service Explanations/AWS IAM Access Analyzer .md
    10-root-user.md
      <- a) Service Explanations/AWS Account Root User .md
  aws-organizations/
    01-overview.md
      <- a) Service Explanations/AWS Organizations .md
    02-service-control-policies.md
      <- a) Service Explanations/Service Control Policy (SCP).md
  aws-resource-access-manager/
    01-overview.md
      <- a) Service Explanations/AWS Resource Access Manager (AWS RAM).md
  aws-service-catalog/
    01-overview.md
      <- a) Service Explanations/AWS Service Catalog.md
04-compute/
  amazon-ec2/
    01-overview.md
      <- a) Service Explanations/Amazon EC2 .md
    02-study-guide.md
      <- c) Keywords services/Amazon EC2 Purchasing & Billing Options.md
    03-instance-store.md
      <- a) Service Explanations/Amazon EC2 Instance Store.md
    03-reserved-instances.md
      <- d) Tools & Policies/EC2 Pricing Models (Reserved Instances).md
    04-key-pairs.md
      <- a) Service Explanations/Amazon EC2 Key Pairs .md
    05-instance-connect.md
      <- a) Service Explanations/Amazon EC2 Instance Connect .md
    06-rdp-connections.md
      <- e) AWS Claude Network & Gateways/Remote Desktop Protocol (RDP) Connection.md
  amazon-lightsail/
    01-overview.md
      <- a) Service Explanations/Amazon Lightsail .md
  aws-batch/
    01-overview.md
      <- a) Service Explanations/AWS Batch (Claude version).md
      <- a) Service Explanations/AWS Batch.md [merge-later]
  aws-fargate/
    01-overview.md
      <- a) Service Explanations/AWS Fargate v1.md
      <- a) Service Explanations/AWS Fargate V2.md [merge-later]
05-storage/
  amazon-ebs/
    01-overview.md
      <- a) Service Explanations/Amazon EBS Volume.md [merge-later]
      <- a) Service Explanations/Amazon Elastic Block Store.md
  amazon-efs/
    01-overview.md
      <- a) Service Explanations/Amazon EFS .md [merge-later]
      <- a) Service Explanations/Amazon Elastic File System.md
  amazon-fsx-for-lustre/
    01-overview.md
      <- a) Service Explanations/Amazon FSx for Lustre (Claude version).md [merge-later]
      <- a) Service Explanations/Amazon FSx for Lustre.md
  amazon-fsx-for-windows-file-server/
    01-overview.md
      <- a) Service Explanations/Amazon FSx for Windows File Server.md
  amazon-s3/
    01-overview.md
      <- a) Service Explanations/Amazon S3 (Claude version).md
      <- a) Service Explanations/Amazon S3 v1 .md [merge-later]
      <- a) Service Explanations/Amazon S3 v2 .md [merge-later]
    02-storage-classes.md
      <- a) Service Explanations/S3 Storage Classes.md
    03-lifecycle-policies.md
      <- c) Keywords services/Amazon S3 Lifecycle Policy.md
06-databases/
  amazon-aurora/
    01-overview.md
      <- a) Service Explanations/Amazon Aurora.md
    02-provisioned.md
      <- a) Service Explanations/Aurora Provisioned.md
    03-serverless.md
      <- a) Service Explanations/Aurora Serverless.md
  amazon-elasticache/
    01-overview.md
      <- a) Service Explanations/Amazon ElastiCache.md
07-networking-and-content-delivery/
  amazon-cloudfront/
    01-overview.md
      <- a) Service Explanations/Amazon CloudFront.md
  amazon-route-53/
    01-overview.md
      <- a) Service Explanations/Amazon Route 53.md
  amazon-vpc/
    02-security-groups.md
      <- e) AWS Claude Network & Gateways/Amazon VPC Security Groups .md
    03-flow-logs.md
      <- e) AWS Claude Network & Gateways/VPC Flow Logs .md
    04-endpoint-services.md
      <- a) Service Explanations/VPC Endpoint Services.md
    05-vpc-peering.md
      <- a) Service Explanations/VPC Peering .md
    06-customer-gateway.md
      <- e) AWS Claude Network & Gateways/Customer Gateway (CGW).md
    07-virtual-private-gateway.md
      <- e) AWS Claude Network & Gateways/Virtual Private Gateway (VGW).md
    08-nat-gateway.md
      <- e) AWS Claude Network & Gateways/NAT Gateway.md
  aws-direct-connect/
    01-overview.md
      <- a) Service Explanations/AWS Direct Connect .md
  aws-global-accelerator/
    01-overview.md
      <- a) Service Explanations/AWS Global Accelerator.md
    02-static-ip-addresses.md
      <- a) Service Explanations/AWS Global Accelerator Static IPs.md
  aws-transit-gateway/
    01-overview.md
      <- e) AWS Claude Network & Gateways/AWS Transit Gateway .md
  networking-guide/
    01-cloud-practitioner-study-guide.md
      <- c) Keywords services/AWS Networking – Complete Cloud Practitioner Study Guide.md
08-serverless-and-application-integration/
  amazon-api-gateway/
    01-overview.md
      <- a) Service Explanations/Amazon API Gateway.md
  amazon-ses/
    01-overview.md
      <- a) Service Explanations/Amazon Simple Email Service (Amazon SES).md
    02-session-manager.md
      <- a) Service Explanations/AWS Systems Manager Session Manager.md
  amazon-sqs/
    01-overview.md
      <- a) Service Explanations/Amazon Simple Queue Service (Amazon SQS).md
  aws-appsync/
    01-overview.md
      <- a) Service Explanations/AWS AppSync.md
  aws-lambda/
    01-overview.md
      <- a) Service Explanations/AWS Lambda.md
09-security-and-compliance/
  amazon-cognito/
    01-overview.md
      <- a) Service Explanations/Amazon Cognito .md
  amazon-guardduty/
    01-overview.md
      <- a) Service Explanations/Amazon GuardDuty.md
  amazon-inspector/
    01-overview.md
      <- a) Service Explanations/Amazon Inspector.md
  amazon-macie/
    01-overview.md
      <- a) Service Explanations/Amazon Macie.md
  amazon-verified-permissions/
    01-overview.md
      <- a) Service Explanations/Amazon Verified Permissions.md
  aws-artifact/
    01-overview.md
      <- a) Service Explanations/AWS Artifact.md
  aws-audit-manager/
    01-overview.md
      <- a) Service Explanations/AWS Audit Manager (Claude version) .md
      <- a) Service Explanations/AWS Audit Manager.md [merge-later]
  aws-certificate-manager/
    01-overview.md
      <- a) Service Explanations/AWS Certificate Manager (ACM).md
  aws-compliance-programs/
    01-overview.md
      <- a) Service Explanations/AWS Compliance Programs.md
  aws-kms/
    01-overview.md
      <- a) Service Explanations/AWS KMS (AWS Key Management Service).md [merge-later]
      <- a) Service Explanations/AWS KMS (Key Management Service) Claude version .md [merge-later]
      <- a) Service Explanations/AWS KMS (Key Management Service).md
  aws-network-firewall/
    01-overview.md
      <- e) AWS Claude Network & Gateways/AWS Network Firewall.md
  aws-secrets-manager/
    01-overview.md
      <- a) Service Explanations/AWS Secrets Manager.md
  aws-security-and-compliance-reference/
    01-overview.md
      <- a) Service Explanations/AWS Security and Compliance Center.md
  aws-security-hub/
    01-overview.md
      <- a) Service Explanations/AWS Security Hub.md
  aws-shield/
    01-overview.md
      <- a) Service Explanations/AWS Shield.md
  aws-trust-and-safety/
    01-overview.md
      <- a) Service Explanations/AWS Trust & Safety Team.md
  aws-waf/
    01-overview.md
      <- a) Service Explanations/AWS WAF.md
10-monitoring-management-and-deployment/
  amazon-codeguru/
    01-overview.md
      <- a) Service Explanations/Amazon CodeGuru .md
  aws-cloudformation/
    01-overview.md
      <- a) Service Explanations/AWS CloudFormation Templates.md
  aws-cloudshell/
    01-overview.md
      <- a) Service Explanations/AWS CloudShell.md
  aws-codebuild/
    01-overview.md
      <- a) Service Explanations/AWS CodeBuild .md
      <- a) Service Explanations/AWS CodeBuild.md [merge-later]
  aws-codecommit/
    01-overview.md
      <- a) Service Explanations/AWS CodeCommit.md
  aws-codedeploy/
    01-overview.md
      <- a) Service Explanations/AWS CodeDeploy.md
  aws-codepipeline/
    01-overview.md
      <- a) Service Explanations/AWS CodePipeline .md
  aws-codestar/
    01-overview.md
      <- a) Service Explanations/AWS CodeStar.md
  aws-config/
    01-overview.md
      <- a) Service Explanations/AWS Config.md
  aws-elastic-beanstalk/
    01-overview.md
      <- a) Service Explanations/AWS Elastic Beanstalk  (Claude version).md [merge-later]
      <- a) Service Explanations/AWS Elastic Beanstalk.md
  aws-managed-services/
    01-overview.md
      <- a) Service Explanations/AWS Managed Services (AMS).md
  aws-systems-manager/
    01-overview.md
      <- a) Service Explanations/AWS Systems Manager.md
  aws-x-ray/
    01-overview.md
      <- a) Service Explanations/AWS X-Ray.md
11-migration-and-hybrid-cloud/
  aws-application-discovery-service/
    01-overview.md
      <- a) Service Explanations/AWS Application Discovery Service.md
  aws-database-migration-service/
    01-overview.md
      <- a) Service Explanations/AWS Database Migration Service (AWS DMS) .md
  aws-datasync/
    01-overview.md
      <- a) Service Explanations/AWS DataSync.md
  aws-migration-hub/
    01-overview.md
      <- a) Service Explanations/AWS Migration Hub.md
  aws-outposts/
    01-overview.md
      <- a) Service Explanations/AWS Outposts.md
  aws-snowball-edge/
    01-overview.md
      <- a) Service Explanations/AWS Snowball Edge.md
  aws-storage-gateway/
    01-overview.md
      <- e) AWS Claude Network & Gateways/AWS Storage Gateway .md
    02-file-gateway.md
      <- e) AWS Claude Network & Gateways/AWS File Gateway.md
    03-volume-gateway-cached.md
      <- e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode) Claude version .md
      <- e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode).md [merge-later]
    04-volume-gateway-stored.md
      <- e) AWS Claude Network & Gateways/AWS Volume Gateway (Stored Mode).md
    05-tape-gateway.md
      <- e) AWS Claude Network & Gateways/AWS Tape Gateway.md [merge-later]
      <- e) AWS Claude Network & Gateways/AWS Tape Gateway(Claude version) .md
12-billing-pricing-and-support/
  aws-billing-and-cost-management/
    01-overview.md
      <- a) Service Explanations/AWS Billing and Cost Management.md
    02-study-guide.md
      <- c) Keywords services/AWS Cloud Practitioner — Fixed vs Variable Costs.md
    03-data-transfer-costs.md
      <- e) AWS Claude Network & Gateways/AWS Charging Patterns and Data Transfer Costs.md
    04-rightsizing.md
      <- d) Tools & Policies/Rightsizing on AWS.txt
  aws-billing-conductor/
    01-overview.md
      <- a) Service Explanations/AWS Billing Conductor.md
  aws-budgets/
    01-overview.md
      <- a) Service Explanations/AWS Budgets .md
  aws-cost-allocation-tags/
    01-overview.md
      <- a) Service Explanations/AWS Cost Allocation Tags.md
  aws-cost-and-usage-reports/
    01-overview.md
      <- a) Service Explanations/AWS Cost and Usage Reports (CUR).md
  aws-cost-explorer/
    01-overview.md
      <- a) Service Explanations/AWS Cost Explorer.md
  aws-pricing-calculator/
    01-overview.md
      <- a) Service Explanations/AWS Pricing Calculator .md
  aws-savings-plans/
    02-study-guide.md
      <- c) Keywords services/AWS Savings Plans — Complete Study Guide.md
  aws-service-quotas/
    01-overview.md
      <- a) Service Explanations/AWS Service Quotas V2 .md
      <- a) Service Explanations/AWS Service Quotas.md [merge-later]
  aws-support/
    01-overview.md
      <- a) Service Explanations/AWS Support Center.md
    02-study-guide.md
      <- a) Service Explanations/AWS Support Plans.md [merge-later]
      <- c) Keywords services/AWS Support Plans — Complete Study Guide.md
  aws-trusted-advisor/
    01-overview.md
      <- a) Service Explanations/AWS Trusted Advisor .md
13-architecture-and-design-patterns/
  amazon-ec2-auto-scaling/
    03-target-tracking-scaling.md
      <- d) Tools & Policies/Target Tracking Scaling Policy.md
  amazon-ec2/
    02-placement-groups.md
      <- f) EC2/PlacementGroups.md
  aws-cloud-adoption-framework/
    01-overview.md
      <- a) Service Explanations/AWS Cloud Adoption Framework (AWS CAF).md
  aws-well-architected-framework/
    01-overview.md
      <- a) Service Explanations/AWS Well-Architected Framework.md
  transport-layer-security/
    01-ssl-termination.md
      <- g)ELB & ASG/SSL Termination .md
    02-tls-with-load-balancers-and-rds.md
      <- h) RDS/SSL & TLS with Load Balancer and RDS.md
14-ai-ml-analytics-and-other-services/
  amazon-alexa/
    01-overview.md
      <- a) Service Explanations/Amazon Alexa .md
  amazon-athena/
    01-overview.md
      <- a) Service Explanations/Amazon Athena.md
  amazon-chime/
    01-overview.md
      <- a) Service Explanations/Amazon Chime Video Meetings.md
  amazon-comprehend/
    01-overview.md
      <- a) Service Explanations/Amazon Comprehend .md [merge-later]
      <- a) Service Explanations/Amazon Comprehend.md
  amazon-connect/
    01-overview.md
      <- a) Service Explanations/Amazon Connect .md
  amazon-elastic-transcoder/
    01-overview.md
      <- a) Service Explanations/Amazon Elastic Transcoder .md
  amazon-emr/
    01-overview.md
      <- a) Service Explanations/Amazon EMR (Claude version).md [merge-later]
      <- a) Service Explanations/Amazon EMR.md
  amazon-kendra/
    01-overview.md
      <- a) Service Explanations/Amazon Kendra.md
  amazon-kinesis-video-streams/
    01-overview.md
      <- a) Service Explanations/Amazon Kinesis Video Streams.md
  amazon-lex/
    01-overview.md
      <- a) Service Explanations/Amazon Lex.md
  amazon-polly/
    01-overview.md
      <- a) Service Explanations/Amazon Polly.md
  amazon-quicksight/
    01-overview.md
      <- a) Service Explanations/Amazon QuickSight.md
  amazon-redshift/
    01-overview.md
      <- a) Service Explanations/Amazon Redshift.md
  amazon-rekognition/
    01-overview.md
      <- a) Service Explanations/Amazon Rekognition.md
  amazon-textract/
    01-overview.md
      <- a) Service Explanations/Amazon Textract .md
  amazon-translate/
    01-overview.md
      <- a) Service Explanations/Amazon Translate.md
  aws-amplify/
    01-overview.md
      <- a) Service Explanations/AWS Amplify (Claude Code).md
      <- a) Service Explanations/AWS Amplify.md [merge-later]
  aws-glue/
    01-overview.md
      <- a) Service Explanations/AWS Glue .md
  aws-guidance/
    02-study-guide.md
      <- c) Keywords services/AWS Documentation & Guidance Services.md
  aws-health/
    01-overview.md
      <- a) Service Explanations/AWS Personal Health Dashboard (AWS Health).md
  aws-iot-greengrass/
    01-overview.md
      <- a) Service Explanations/AWS IoT Greengrass.md
  aws-iot/
    01-overview.md
      <- a) Service Explanations/AWS IoT.md
  aws-partner-network/
    01-overview.md
      <- a) Service Explanations/AWS Partner Network (APN).md
  aws-prescriptive-guidance/
    01-overview.md
      <- d) Tools & Policies/AWS Prescriptive Guidance.md
  aws-professional-services/
    01-overview.md
      <- a) Service Explanations/AWS Professional Services Consulting Engagement Team.md
  aws-recommendation-services-complete-study-guide/
    02-study-guide.md
      <- c) Keywords services/AWS Recommendation Services — Complete Study Guide.md
  aws-repost-knowledge-center/
    01-overview.md
      <- a) Service Explanations/AWS Knowledge Center.md
  aws-repost/
    01-overview.md
      <- a) Service Explanations/AWS rePost.md
  aws-schema-conversion-tool-aws-sct/
    01-overview.md
      <- a) Service Explanations/AWS Schema Conversion Tool (AWS SCT).md
15-comparisons-and-decision-guides/
  cross-service/
    01-amazon-cloudfront-vs-aws-global-accelerator.md
      <- b) Service Comparisons/Amazon CloudFront vs AWS Global Accelerator.md
    01-amazon-emr-vs-amazon-redshift.md
      <- b) Service Comparisons/Amazon EMR vs Amazon Redshift .md
    01-aws-account-root-user-vs-aws-iam.md
      <- b) Service Comparisons/AWS Account Root User vs AWS IAM .md
    01-aws-datasync-vs-aws-database-migration-service-aws-dms.md
      <- b) Service Comparisons/AWS DataSync vs AWS Database Migration Service (AWS DMS).md
    01-aws-file-gateway-vs-aws-volume-gateway-cached.md
      <- b) Service Comparisons/AWS File Gateway vs AWS Volume Gateway (Cached).md
    01-aws-organizations-vs-aws-control-tower.md
      <- b) Service Comparisons/AWS Organizations vs AWS Control Tower.md
    01-aws-snowball-edge-vs-aws-outposts.md
      <- b) Service Comparisons/AWS Snowball Edge vs AWS Outposts.md
    01-aws-storage-gateway-vs-aws-file-gateway.md
      <- e) AWS Claude Network & Gateways/AWS Storage Gateway vs AWS File Gateway.md
    01-iam-role-vs-iam-group-vs-iam-user.md
      <- b) Service Comparisons/IAM Role vs IAM Group vs IAM User.md
    01-vpc-endpoint-vs-vpc-peering-vs-aws-transit-gateway.md
      <- b) Service Comparisons/VPC Endpoint vs VPC Peering vs AWS Transit Gateway .md
docs/
  templates/
    02-service-comparison-prompt.md
      <- b) Service Comparisons/Comparison copy paste prompt.txt
    04-latex-study-document-prompt.md
      <- COPY PASTE PROMPT OF CLAUDE (BOTH CONTENT AND STYLE ).txt
    03-saa-study-note-prompt.md
      <- COPY PASTE Prompt .txt
    01-service-explanation-prompt.md
      <- a) Service Explanations/copy paste ptompt Explanations .txt
```

