# Duplicate and Overlap Analysis

## Method and result

All 185 files were hashed with SHA-256 and inspected by content and heading structure. **No exact duplicate group was found.** The groups below are near-duplicates or multiple versions of the same service. Broad-service-plus-feature relationships and section overlap are documented separately afterward; those are not automatically merge candidates.

## DG-01-s3-overviews

- Files:
  - `a) Service Explanations/Amazon S3 (Claude version).md` — recommended canonical
  - `a) Service Explanations/Amazon S3 v1 .md`
  - `a) Service Explanations/Amazon S3 v2 .md`
- Similarity/overlap: Three broad Amazon S3 introductions repeat object storage, buckets, durability, security, storage classes, lifecycle, and exam traps.
- Unique useful content:
  - `a) Service Explanations/Amazon S3 (Claude version).md`: Strong exam metadata, storage-class treatment, related-service distinctions, and explicit traps.
  - `a) Service Explanations/Amazon S3 v1 .md`: Clear coverage of versioning, lifecycle rules, encryption, and access control.
  - `a) Service Explanations/Amazon S3 v2 .md`: Concise object-storage framing and a compact security/lifecycle explanation.
- Recommended canonical document: `a) Service Explanations/Amazon S3 (Claude version).md`
- Merge strategy: Use the Claude-version document as the structural base because content inspection shows the broadest exam-oriented outline; diff both numbered versions section by section and import only distinct facts or clearer examples. Keep the separate lifecycle and storage-class feature notes.
- Confidence: **high**
- Human review required: **yes**

## DG-02-fargate

- Files:
  - `a) Service Explanations/AWS Fargate v1.md` — recommended canonical
  - `a) Service Explanations/AWS Fargate V2.md`
- Similarity/overlap: Both explain serverless container compute for ECS/EKS, scaling, and usage pricing.
- Unique useful content:
  - `a) Service Explanations/AWS Fargate v1.md`: Longer treatment of ECS/EKS, capacity planning, scaling, and operation.
  - `a) Service Explanations/AWS Fargate V2.md`: More compact revision useful for concise memory cues.
- Recommended canonical document: `a) Service Explanations/AWS Fargate v1.md`
- Merge strategy: Retain v1 content as the base after content review, then fold in any clearer V2 memory cues; remove version labels only during Phase 2.
- Confidence: **high**
- Human review required: **no**

## DG-03-audit-manager

- Files:
  - `a) Service Explanations/AWS Audit Manager.md`
  - `a) Service Explanations/AWS Audit Manager (Claude version) .md` — recommended canonical
- Similarity/overlap: Both cover automated evidence collection, frameworks, controls, and audit preparation.
- Unique useful content:
  - `a) Service Explanations/AWS Audit Manager.md`: Compact list of use cases and product capabilities.
  - `a) Service Explanations/AWS Audit Manager (Claude version) .md`: Adds definitions of audits and audit evidence, workflow detail, and exam framing.
- Recommended canonical document: `a) Service Explanations/AWS Audit Manager (Claude version) .md`
- Merge strategy: Use the more explanatory Claude-version outline as base and preserve concise capability statements from the shorter note.
- Confidence: **high**
- Human review required: **no**

## DG-04-batch

- Files:
  - `a) Service Explanations/AWS Batch.md`
  - `a) Service Explanations/AWS Batch (Claude version).md` — recommended canonical
- Similarity/overlap: Both describe managed batch scheduling, queues, compute environments, containers, scaling, and pricing.
- Unique useful content:
  - `a) Service Explanations/AWS Batch.md`: Concise feature inventory and compute-option summary.
  - `a) Service Explanations/AWS Batch (Claude version).md`: Adds a four-building-block explanation, workflow, real-world example, and exam traps.
- Recommended canonical document: `a) Service Explanations/AWS Batch (Claude version).md`
- Merge strategy: Use the Claude-version document as base; cross-check the compact note for missing compute options and wording.
- Confidence: **high**
- Human review required: **no**

## DG-05-emr

- Files:
  - `a) Service Explanations/Amazon EMR.md` — recommended canonical
  - `a) Service Explanations/Amazon EMR (Claude version).md`
- Similarity/overlap: Both cover managed Hadoop/Spark big-data processing, clusters, ETL, analytics, and exam comparisons.
- Unique useful content:
  - `a) Service Explanations/Amazon EMR.md`: Broader enumerated use cases and fuller feature detail.
  - `a) Service Explanations/Amazon EMR (Claude version).md`: Clear cluster-node explanation, compact comparison, and exam traps.
- Recommended canonical document: `a) Service Explanations/Amazon EMR.md`
- Merge strategy: Use the unlabelled, fuller document as base for substantive reasons; import the alternate's node-type and trap sections after factual review.
- Confidence: **high**
- Human review required: **no**

## DG-06-fsx-lustre

- Files:
  - `a) Service Explanations/Amazon FSx for Lustre.md` — recommended canonical
  - `a) Service Explanations/Amazon FSx for Lustre (Claude version).md`
- Similarity/overlap: Both explain high-performance managed Lustre storage for HPC, ML, analytics, and S3-linked workflows.
- Unique useful content:
  - `a) Service Explanations/Amazon FSx for Lustre.md`: More extensive use cases and feature coverage.
  - `a) Service Explanations/Amazon FSx for Lustre (Claude version).md`: Stepwise workflow, memory guide, and explicit EFS/Linux traps.
- Recommended canonical document: `a) Service Explanations/Amazon FSx for Lustre.md`
- Merge strategy: Use the larger service note as base; add only distinct workflow and trap material from the alternate.
- Confidence: **high**
- Human review required: **no**

## DG-07-kms

- Files:
  - `a) Service Explanations/AWS KMS (AWS Key Management Service).md`
  - `a) Service Explanations/AWS KMS (Key Management Service) Claude version .md`
  - `a) Service Explanations/AWS KMS (Key Management Service).md` — recommended canonical
- Similarity/overlap: All three cover managed encryption keys, permissions, rotation, auditing, and AWS integrations.
- Unique useful content:
  - `a) Service Explanations/AWS KMS (AWS Key Management Service).md`: Concise use-case and capability outline.
  - `a) Service Explanations/AWS KMS (Key Management Service) Claude version .md`: Key-type section and explicit KMS-versus-CloudHSM comparison.
  - `a) Service Explanations/AWS KMS (Key Management Service).md`: Broadest feature treatment including audit trail, rotation, hardware backing, and multiple key types.
- Recommended canonical document: `a) Service Explanations/AWS KMS (Key Management Service).md`
- Merge strategy: Use the broadest document as base, incorporate any distinct CloudHSM comparison and key-type explanations, and reconcile terminology with current KMS documentation.
- Confidence: **high**
- Human review required: **yes**

## DG-08-service-quotas

- Files:
  - `a) Service Explanations/AWS Service Quotas.md`
  - `a) Service Explanations/AWS Service Quotas V2 .md` — recommended canonical
- Similarity/overlap: Both explain viewing limits, requesting increases, avoiding deployment failures, and planning growth.
- Unique useful content:
  - `a) Service Explanations/AWS Service Quotas.md`: Short exam-focused overview.
  - `a) Service Explanations/AWS Service Quotas V2 .md`: Adds Organizations and monitoring coverage plus a fuller workflow.
- Recommended canonical document: `a) Service Explanations/AWS Service Quotas V2 .md`
- Merge strategy: Use V2 content as base because inspection shows substantive additional sections, then remove the version label in Phase 2.
- Confidence: **high**
- Human review required: **no**

## DG-09-tape-gateway

- Files:
  - `e) AWS Claude Network & Gateways/AWS Tape Gateway.md`
  - `e) AWS Claude Network & Gateways/AWS Tape Gateway(Claude version) .md` — recommended canonical
- Similarity/overlap: Both explain the VTL model, existing backup software, S3/Glacier-backed archival, and retrieval.
- Unique useful content:
  - `e) AWS Claude Network & Gateways/AWS Tape Gateway.md`: Straightforward deployment and retrieval steps.
  - `e) AWS Claude Network & Gateways/AWS Tape Gateway(Claude version) .md`: Adds exam traps and richer related-service distinctions.
- Recommended canonical document: `e) AWS Claude Network & Gateways/AWS Tape Gateway(Claude version) .md`
- Merge strategy: Use the more complete exam-oriented note as base while retaining the shorter note's clean operational sequence.
- Confidence: **high**
- Human review required: **no**

## DG-10-volume-gateway-cached

- Files:
  - `e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode).md`
  - `e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode) Claude version .md` — recommended canonical
- Similarity/overlap: Both explain iSCSI block storage with primary data in AWS and a local cache.
- Unique useful content:
  - `e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode).md`: Explicit feature list and simple operational flow.
  - `e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode) Claude version .md`: Adds gateway-family context and comparisons with Direct Connect and EFS.
- Recommended canonical document: `e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode) Claude version .md`
- Merge strategy: Use the Claude-version note as base and preserve the alternate's concise feature and workflow sections.
- Confidence: **high**
- Human review required: **no**

## DG-11-amplify

- Files:
  - `a) Service Explanations/AWS Amplify.md`
  - `a) Service Explanations/AWS Amplify (Claude Code).md` — recommended canonical
- Similarity/overlap: Both explain frontend/mobile tooling, hosting, authentication, APIs, storage, and managed deployment.
- Unique useful content:
  - `a) Service Explanations/AWS Amplify.md`: More granular use-case enumeration.
  - `a) Service Explanations/AWS Amplify (Claude Code).md`: Adds workflow and explicit comparisons/traps involving Elastic Beanstalk and backend services.
- Recommended canonical document: `a) Service Explanations/AWS Amplify (Claude Code).md`
- Merge strategy: Use the slightly fuller alternate as base for its unique trap material, then merge the granular use cases; the filename label is not a quality signal.
- Confidence: **medium**
- Human review required: **yes**

## DG-12-codebuild

- Files:
  - `a) Service Explanations/AWS CodeBuild.md`
  - `a) Service Explanations/AWS CodeBuild .md` — recommended canonical
- Similarity/overlap: Both explain managed build servers, compilation, testing, artifacts, scaling, and CI/CD integration.
- Unique useful content:
  - `a) Service Explanations/AWS CodeBuild.md`: Compact sources, build instructions, security, and integration summary.
  - `a) Service Explanations/AWS CodeBuild .md`: Broader use cases and fuller feature explanation.
- Recommended canonical document: `a) Service Explanations/AWS CodeBuild .md`
- Merge strategy: Use the larger content-rich note as base; import distinct security/source details from the compact note.
- Confidence: **high**
- Human review required: **no**

## DG-13-comprehend

- Files:
  - `a) Service Explanations/Amazon Comprehend.md` — recommended canonical
  - `a) Service Explanations/Amazon Comprehend .md`
- Similarity/overlap: Both explain NLP analysis including sentiment, entities, phrases, language, topics, and related AI services.
- Unique useful content:
  - `a) Service Explanations/Amazon Comprehend.md`: Explicit treatment of syntax, custom classification, and custom entities.
  - `a) Service Explanations/Amazon Comprehend .md`: More extensive comparisons with Rekognition, Lex, Transcribe, and Translate.
- Recommended canonical document: `a) Service Explanations/Amazon Comprehend.md`
- Merge strategy: Use the feature-richer note as base and import the alternate's distinct comparison material.
- Confidence: **high**
- Human review required: **no**

## DG-14-elastic-beanstalk

- Files:
  - `a) Service Explanations/AWS Elastic Beanstalk.md` — recommended canonical
  - `a) Service Explanations/AWS Elastic Beanstalk  (Claude version).md`
- Similarity/overlap: Both explain managed application deployment, provisioning, scaling, monitoring, and platform support.
- Unique useful content:
  - `a) Service Explanations/AWS Elastic Beanstalk.md`: Much broader use-case and provisioning coverage.
  - `a) Service Explanations/AWS Elastic Beanstalk  (Claude version).md`: Concise exam traps, including pricing and serverless misconceptions.
- Recommended canonical document: `a) Service Explanations/AWS Elastic Beanstalk.md`
- Merge strategy: Use the fuller service note as base and import only distinct, verified trap material.
- Confidence: **high**
- Human review required: **no**

## DG-15-efs

- Files:
  - `a) Service Explanations/Amazon EFS .md`
  - `a) Service Explanations/Amazon Elastic File System.md` — recommended canonical
- Similarity/overlap: Both explain managed, elastic, shared Linux/NFS file storage.
- Unique useful content:
  - `a) Service Explanations/Amazon EFS .md`: Compact list of elasticity, availability, and pay-for-use features.
  - `a) Service Explanations/Amazon Elastic File System.md`: Adds comparisons with EBS, S3, and FSx plus exam traps.
- Recommended canonical document: `a) Service Explanations/Amazon Elastic File System.md`
- Merge strategy: Use the comparison-rich note as base and verify that every concise feature from the shorter note remains represented.
- Confidence: **high**
- Human review required: **no**

## DG-16-ebs

- Files:
  - `a) Service Explanations/Amazon EBS Volume.md`
  - `a) Service Explanations/Amazon Elastic Block Store.md` — recommended canonical
- Similarity/overlap: Both explain persistent block storage for EC2, volumes, durability, and EBS comparisons.
- Unique useful content:
  - `a) Service Explanations/Amazon EBS Volume.md`: Concise comparisons with S3, EFS, Instance Store, and FSx.
  - `a) Service Explanations/Amazon Elastic Block Store.md`: Substantially broader explanation of persistence, boot volumes, databases, and operating model.
- Recommended canonical document: `a) Service Explanations/Amazon Elastic Block Store.md`
- Merge strategy: Use the broader EBS note as base and preserve any distinct comparison wording from the shorter volume note.
- Confidence: **high**
- Human review required: **no**

## DG-17-customer-managed-policies

- Files:
  - `a) Service Explanations/AWS Customer Managed Policies.md`
  - `d) Tools & Policies/AWS Customer Managed Policies (Claude version).txt` — recommended canonical
- Similarity/overlap: Both explain reusable customer-managed IAM policies, least privilege, attachment, and comparison with other policy types.
- Unique useful content:
  - `a) Service Explanations/AWS Customer Managed Policies.md`: Concise use cases and account-standardization discussion.
  - `d) Tools & Policies/AWS Customer Managed Policies (Claude version).txt`: Adds example JSON and a side-by-side policy-type comparison.
- Recommended canonical document: `d) Tools & Policies/AWS Customer Managed Policies (Claude version).txt`
- Merge strategy: Use the richer text document as content base, convert it to Markdown only in Phase 2, and import any missing governance wording from the Markdown note.
- Confidence: **high**
- Human review required: **yes**

## DG-18-support-plans

- Files:
  - `a) Service Explanations/AWS Support Plans.md`
  - `c) Keywords services/AWS Support Plans — Complete Study Guide.md` — recommended canonical
- Similarity/overlap: Both cover support tiers, intended users, features, response characteristics, and exam distinctions.
- Unique useful content:
  - `a) Service Explanations/AWS Support Plans.md`: Compact, readable per-tier memory lines.
  - `c) Keywords services/AWS Support Plans — Complete Study Guide.md`: Much deeper tier-by-tier examples, pricing context, and exam traps.
- Recommended canonical document: `c) Keywords services/AWS Support Plans — Complete Study Guide.md`
- Merge strategy: Use the complete guide as base; retain the shorter note's strongest memory lines. Re-verify plan names and benefits immediately before Phase 2 because support offerings change.
- Confidence: **medium**
- Human review required: **yes**

## Broad note plus narrower feature notes (retain separately)

- Amazon S3 overview family ↔ `S3 Storage Classes.md` and `Amazon S3 Lifecycle Policy.md`: broad notes overlap with these features, but the feature notes contain focused detail; link them instead of absorbing them automatically.
- Amazon EC2 overview ↔ EBS, Instance Store, Key Pairs, Instance Connect, Placement Groups, pricing, and target-tracking notes: these form a service family, not duplicates.
- AWS Systems Manager ↔ Session Manager: Session Manager is a focused feature lesson; retain and cross-link.
- AWS Global Accelerator ↔ Static IPs: retain the static-IP note as a feature lesson after removing repeated overview text.
- Amazon Aurora ↔ Provisioned and Serverless: retain both deployment-mode lessons and keep the overview concise.
- AWS Storage Gateway ↔ File, Tape, cached Volume, and stored Volume Gateway notes: preserve gateway-type lessons; consolidate only the two same-mode version pairs identified above.
- IAM overview ↔ users, groups, roles, access analyzer, managed/inline policies, and root-user notes: organize as one directory with separate lessons.

## Overlapping sections with unique information

- Every comparison document repeats short service definitions found in service notes. Keep comparisons in category 15 because their decision tables and exam contrasts are unique.
- `AWS Networking – Complete Cloud Practitioner Study Guide.md` overlaps many individual VPC/network notes but supplies a cross-service mental model and should remain a guide, not replace the atomic lessons.
- `AWS Recommendation Services — Complete Study Guide.md` overlaps Trusted Advisor, Cost Explorer, and rightsizing material but uniquely synthesizes recommendation sources.
- `AWS Documentation & Guidance Services.md` overlaps Well-Architected and Prescriptive Guidance notes but provides a useful navigation/selection guide.

## Obsolete or transitional terminology/content

- `Amazon Elastic Transcoder .md`: the document itself describes a retired service. [AWS ended support on 2025-11-13](https://aws.amazon.com/blogs/media/support-for-amazon-elastic-transcoder-ending-soon/); recommend `archive-later` with a replacement pointer to AWS Elemental MediaConvert.
- `AWS Personal Health Dashboard (AWS Health).md`: “Personal Health Dashboard” remains in some AWS documentation but current user-facing material commonly says AWS Health Dashboard. Treat as an obsolete-name candidate and verify terminology during Phase 2.
- `AWS Knowledge Center.md`: [AWS migrated Knowledge Center articles and videos into AWS re:Post in 2023](https://aws.amazon.com/about-aws/whats-new/2023/03/aws-re-post-includes-knowledge-center-articles/). Preserve the content but review whether it should become a re:Post Knowledge Center feature note.
- `AWS Security and Compliance Center.md`: content/path terminology does not clearly identify a current standalone AWS service; manual service-name verification is required.

## Prompts stored with study notes

The four prompt/template files are not lesson content and should move non-destructively to `docs/templates/aws-study-prompts/`. They are not duplicates of one another: they target explanation notes, comparisons, SAA/SAP prose, and LaTeX generation respectively.
