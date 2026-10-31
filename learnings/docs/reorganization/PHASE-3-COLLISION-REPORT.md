# Phase 3 Collision Report

Audit date: 2026-07-21

No destination file existed before migration. No case-only destination collision, source/destination normalized-identity case, Windows-incompatible proposed filename, or malformed Unicode representation was detected.

Exact multi-source destination collisions: **18**. Every source in these groups remains in place for Phase 4.

## 03-identity-governance-and-organizations/aws-iam/05-customer-managed-policies.md

Duplicate group: `DG-17-customer-managed-policies`

- `a) Service Explanations/AWS Customer Managed Policies.md` — action `merge-later`
- `d) Tools & Policies/AWS Customer Managed Policies (Claude version).txt` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 04-compute/aws-batch/01-overview.md

Duplicate group: `DG-04-batch`

- `a) Service Explanations/AWS Batch (Claude version).md` — action `rename-and-move`
- `a) Service Explanations/AWS Batch.md` — action `merge-later`

Decision: skip the entire group; do not overwrite or merge.

## 04-compute/aws-fargate/01-overview.md

Duplicate group: `DG-02-fargate`

- `a) Service Explanations/AWS Fargate v1.md` — action `rename-and-move`
- `a) Service Explanations/AWS Fargate V2.md` — action `merge-later`

Decision: skip the entire group; do not overwrite or merge.

## 05-storage/amazon-ebs/01-overview.md

Duplicate group: `DG-16-ebs`

- `a) Service Explanations/Amazon EBS Volume.md` — action `merge-later`
- `a) Service Explanations/Amazon Elastic Block Store.md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 05-storage/amazon-efs/01-overview.md

Duplicate group: `DG-15-efs`

- `a) Service Explanations/Amazon EFS .md` — action `merge-later`
- `a) Service Explanations/Amazon Elastic File System.md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 05-storage/amazon-fsx-for-lustre/01-overview.md

Duplicate group: `DG-06-fsx-lustre`

- `a) Service Explanations/Amazon FSx for Lustre (Claude version).md` — action `merge-later`
- `a) Service Explanations/Amazon FSx for Lustre.md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 05-storage/amazon-s3/01-overview.md

Duplicate group: `DG-01-s3-overviews`

- `a) Service Explanations/Amazon S3 (Claude version).md` — action `rename-and-move`
- `a) Service Explanations/Amazon S3 v1 .md` — action `merge-later`
- `a) Service Explanations/Amazon S3 v2 .md` — action `merge-later`

Decision: skip the entire group; do not overwrite or merge.

## 09-security-and-compliance/aws-audit-manager/01-overview.md

Duplicate group: `DG-03-audit-manager`

- `a) Service Explanations/AWS Audit Manager (Claude version) .md` — action `rename-and-move`
- `a) Service Explanations/AWS Audit Manager.md` — action `merge-later`

Decision: skip the entire group; do not overwrite or merge.

## 09-security-and-compliance/aws-kms/01-overview.md

Duplicate group: `DG-07-kms`

- `a) Service Explanations/AWS KMS (AWS Key Management Service).md` — action `merge-later`
- `a) Service Explanations/AWS KMS (Key Management Service) Claude version .md` — action `merge-later`
- `a) Service Explanations/AWS KMS (Key Management Service).md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 10-monitoring-management-and-deployment/aws-codebuild/01-overview.md

Duplicate group: `DG-12-codebuild`

- `a) Service Explanations/AWS CodeBuild .md` — action `rename-and-move`
- `a) Service Explanations/AWS CodeBuild.md` — action `merge-later`

Decision: skip the entire group; do not overwrite or merge.

## 10-monitoring-management-and-deployment/aws-elastic-beanstalk/01-overview.md

Duplicate group: `DG-14-elastic-beanstalk`

- `a) Service Explanations/AWS Elastic Beanstalk  (Claude version).md` — action `merge-later`
- `a) Service Explanations/AWS Elastic Beanstalk.md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 11-migration-and-hybrid-cloud/aws-storage-gateway/03-volume-gateway-cached.md

Duplicate group: `DG-10-volume-gateway-cached`

- `e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode) Claude version .md` — action `rename-and-move`
- `e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode).md` — action `merge-later`

Decision: skip the entire group; do not overwrite or merge.

## 11-migration-and-hybrid-cloud/aws-storage-gateway/05-tape-gateway.md

Duplicate group: `DG-09-tape-gateway`

- `e) AWS Claude Network & Gateways/AWS Tape Gateway.md` — action `merge-later`
- `e) AWS Claude Network & Gateways/AWS Tape Gateway(Claude version) .md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 12-billing-pricing-and-support/aws-service-quotas/01-overview.md

Duplicate group: `DG-08-service-quotas`

- `a) Service Explanations/AWS Service Quotas V2 .md` — action `rename-and-move`
- `a) Service Explanations/AWS Service Quotas.md` — action `merge-later`

Decision: skip the entire group; do not overwrite or merge.

## 12-billing-pricing-and-support/aws-support/02-study-guide.md

Duplicate group: `DG-18-support-plans`

- `a) Service Explanations/AWS Support Plans.md` — action `merge-later`
- `c) Keywords services/AWS Support Plans — Complete Study Guide.md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 14-ai-ml-analytics-and-other-services/amazon-comprehend/01-overview.md

Duplicate group: `DG-13-comprehend`

- `a) Service Explanations/Amazon Comprehend .md` — action `merge-later`
- `a) Service Explanations/Amazon Comprehend.md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 14-ai-ml-analytics-and-other-services/amazon-emr/01-overview.md

Duplicate group: `DG-05-emr`

- `a) Service Explanations/Amazon EMR (Claude version).md` — action `merge-later`
- `a) Service Explanations/Amazon EMR.md` — action `rename-and-move`

Decision: skip the entire group; do not overwrite or merge.

## 14-ai-ml-analytics-and-other-services/aws-amplify/01-overview.md

Duplicate group: `DG-11-amplify`

- `a) Service Explanations/AWS Amplify (Claude Code).md` — action `rename-and-move`
- `a) Service Explanations/AWS Amplify.md` — action `merge-later`

Decision: skip the entire group; do not overwrite or merge.

## Additional Audit Counts

- Case-only destination collision groups: **0**
- Existing destination files: **0**
- Source/destination normalized-identity paths: **0**
- Windows-incompatible proposed paths: **0**
- Source filenames with a space immediately before the extension or a trailing segment space: **44**
- Malformed Unicode filename representations: **0** (all paths round-trip through strict UTF-8).

### Source trailing-space risks

- `a) Service Explanations/Amazon Alexa .md`
- `a) Service Explanations/Amazon CodeGuru .md`
- `a) Service Explanations/Amazon Cognito .md`
- `a) Service Explanations/Amazon Comprehend .md`
- `a) Service Explanations/Amazon Connect .md`
- `a) Service Explanations/Amazon EC2 .md`
- `a) Service Explanations/Amazon EC2 Instance Connect .md`
- `a) Service Explanations/Amazon EC2 Key Pairs .md`
- `a) Service Explanations/Amazon EFS .md`
- `a) Service Explanations/Amazon Elastic Transcoder .md`
- `a) Service Explanations/Amazon Lightsail .md`
- `a) Service Explanations/Amazon S3 v1 .md`
- `a) Service Explanations/Amazon S3 v2 .md`
- `a) Service Explanations/Amazon Textract .md`
- `a) Service Explanations/AWS Account Root User .md`
- `a) Service Explanations/AWS Audit Manager (Claude version) .md`
- `a) Service Explanations/AWS Budgets .md`
- `a) Service Explanations/AWS CodeBuild .md`
- `a) Service Explanations/AWS CodePipeline .md`
- `a) Service Explanations/AWS Database Migration Service (AWS DMS) .md`
- `a) Service Explanations/AWS Direct Connect .md`
- `a) Service Explanations/AWS Glue .md`
- `a) Service Explanations/AWS IAM Access Analyzer .md`
- `a) Service Explanations/AWS IAM Group .md`
- `a) Service Explanations/AWS IAM Role .md`
- `a) Service Explanations/AWS IAM User .md`
- `a) Service Explanations/AWS KMS (Key Management Service) Claude version .md`
- `a) Service Explanations/AWS Organizations .md`
- `a) Service Explanations/AWS Pricing Calculator .md`
- `a) Service Explanations/AWS Service Quotas V2 .md`
- `a) Service Explanations/AWS Trusted Advisor .md`
- `a) Service Explanations/copy paste ptompt Explanations .txt`
- `a) Service Explanations/VPC Peering .md`
- `b) Service Comparisons/Amazon EMR vs Amazon Redshift .md`
- `b) Service Comparisons/AWS Account Root User vs AWS IAM .md`
- `b) Service Comparisons/VPC Endpoint vs VPC Peering vs AWS Transit Gateway .md`
- `COPY PASTE Prompt .txt`
- `e) AWS Claude Network & Gateways/Amazon VPC Security Groups .md`
- `e) AWS Claude Network & Gateways/AWS Storage Gateway .md`
- `e) AWS Claude Network & Gateways/AWS Tape Gateway(Claude version) .md`
- `e) AWS Claude Network & Gateways/AWS Transit Gateway .md`
- `e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode) Claude version .md`
- `e) AWS Claude Network & Gateways/VPC Flow Logs .md`
- `g)ELB & ASG/SSL Termination .md`
