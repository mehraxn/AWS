# CPP Official Baseline

- Certification: **AWS Certified Cloud Practitioner**
- Current exam code verified: **CLF-C02**
- Checked: **2026-07-21**
- [Official exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
- [Official in-scope services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)

AWS states that its service and feature lists are non-exhaustive and subject to change. This baseline maps the published guide as checked; it does not guarantee future exam coverage.

## Candidate and Required Depth

The target learner needs broad cloud literacy, service recognition, basic security, pricing, and support reasoning.

## Domains

| Domain | Name | Weight |
|---|---|---|
| 1 | Cloud Concepts | 24% |
| 2 | Security and Compliance | 30% |
| 3 | Cloud Technology and Services | 34% |
| 4 | Billing, Pricing, and Support | 12% |

## Tasks, Knowledge, and Skills

### Task 1.1: Define the AWS Cloud and its value proposition

Expected repository category: `01-cloud-fundamentals/`

Knowledge statements (paraphrased):

- AWS Cloud value proposition
- cloud economics
- global reach and agility

Skill statements (paraphrased):

- Explain cloud benefits
- Match cloud benefits to business needs

### Task 1.2: Identify AWS Cloud design principles

Expected repository category: `13-architecture-and-design-patterns/`

Knowledge statements (paraphrased):

- Well-Architected pillars
- design for failure
- elasticity and automation

Skill statements (paraphrased):

- Recognize appropriate cloud design principles

### Task 1.3: Understand migration benefits and strategies

Expected repository category: `11-migration-and-hybrid-cloud/`

Knowledge statements (paraphrased):

- AWS Cloud migration benefits
- migration strategies
- AWS Cloud Adoption Framework

Skill statements (paraphrased):

- Identify migration approaches
- Recognize migration assistance resources

### Task 1.4: Understand cloud economics

Expected repository category: `12-billing-pricing-and-support/`

Knowledge statements (paraphrased):

- fixed versus variable cost
- rightsizing
- economies of scale
- licensing strategy

Skill statements (paraphrased):

- Compare on-premises and cloud costs
- Identify cost optimization practices

### Task 2.1: Understand the Shared Responsibility Model

Expected repository category: `01-cloud-fundamentals/`

Knowledge statements (paraphrased):

- AWS responsibilities
- customer responsibilities
- responsibility changes by service model

Skill statements (paraphrased):

- Assign security tasks for EC2, RDS, and Lambda

### Task 2.2: Understand security, governance, and compliance

Expected repository category: `09-security-and-compliance/`

Knowledge statements (paraphrased):

- compliance concepts
- encryption
- logging and auditing
- governance services

Skill statements (paraphrased):

- Identify AWS Artifact and compliance resources
- Choose monitoring and auditing services

### Task 2.3: Understand access management

Expected repository category: `03-identity-governance-and-organizations/`

Knowledge statements (paraphrased):

- least privilege
- root user protection
- IAM identities and policies
- federation and cross-account access

Skill statements (paraphrased):

- Apply MFA and access-key practices
- Select users, groups, roles, policies, and Identity Center

### Task 2.4: Identify security resources and capabilities

Expected repository category: `09-security-and-compliance/`

Knowledge statements (paraphrased):

- AWS security services
- security guidance
- Trusted Advisor security checks

Skill statements (paraphrased):

- Recognize threat detection and protection services
- Locate AWS security assistance

### Task 3.1: Define deployment and operation methods

Expected repository category: `10-monitoring-management-and-deployment/`

Knowledge statements (paraphrased):

- Management Console, CLI, SDK, and API access
- cloud, hybrid, and on-premises deployment
- infrastructure as code

Skill statements (paraphrased):

- Select an AWS interaction method
- Recognize deployment models

### Task 3.2: Understand AWS global infrastructure

Expected repository category: `02-global-infrastructure/`

Knowledge statements (paraphrased):

- Regions
- Availability Zones
- edge locations
- high availability and multi-Region use

Skill statements (paraphrased):

- Select Regions and Availability Zones
- Recognize edge-service benefits

### Task 3.3: Identify AWS compute services

Expected repository category: `04-compute/`

Knowledge statements (paraphrased):

- EC2 instance families
- containers
- serverless compute
- Auto Scaling and load balancing

Skill statements (paraphrased):

- Select a compute option
- Recognize scaling and load-balancing use cases

### Task 3.4: Identify AWS database services

Expected repository category: `06-databases/`

Knowledge statements (paraphrased):

- relational databases
- NoSQL databases
- caching
- database migration

Skill statements (paraphrased):

- Select a database category
- Recognize managed database benefits

### Task 3.5: Identify AWS network services

Expected repository category: `07-networking-and-content-delivery/`

Knowledge statements (paraphrased):

- VPC components
- security groups and network ACLs
- Route 53
- VPN and Direct Connect

Skill statements (paraphrased):

- Recognize public, private, and hybrid connectivity
- Select basic network controls

### Task 3.6: Identify AWS storage services

Expected repository category: `05-storage/`

Knowledge statements (paraphrased):

- object, block, and file storage
- S3 storage classes
- EBS and instance store
- EFS and FSx
- Storage Gateway and Backup

Skill statements (paraphrased):

- Select a storage type
- Recognize lifecycle and backup options

### Task 3.7: Identify AI, ML, and analytics services

Expected repository category: `14-ai-ml-analytics-and-other-services/`

Knowledge statements (paraphrased):

- AI and ML service purposes
- analytics service purposes
- data ingestion and visualization

Skill statements (paraphrased):

- Recognize common AI/ML and analytics use cases

### Task 3.8: Identify other in-scope service categories

Expected repository category: `14-ai-ml-analytics-and-other-services/`

Knowledge statements (paraphrased):

- application integration
- business applications
- developer tools
- end-user computing
- frontend and IoT services

Skill statements (paraphrased):

- Recognize services by category and business use

### Task 4.1: Compare AWS pricing models

Expected repository category: `12-billing-pricing-and-support/`

Knowledge statements (paraphrased):

- On-Demand, Reserved, Spot, and Savings Plans
- storage pricing drivers
- data transfer pricing

Skill statements (paraphrased):

- Choose a purchasing model
- Identify major cost drivers

### Task 4.2: Understand billing and cost-management resources

Expected repository category: `12-billing-pricing-and-support/`

Knowledge statements (paraphrased):

- Budgets
- Cost Explorer
- Cost and Usage Reports
- Organizations and cost allocation tags

Skill statements (paraphrased):

- Select cost tools
- Recognize consolidated billing and tagging

### Task 4.3: Identify AWS support resources

Expected repository category: `12-billing-pricing-and-support/`

Knowledge statements (paraphrased):

- AWS Support plans
- AWS re:Post and documentation
- Trusted Advisor and AWS Health
- Partners, Marketplace, and Professional Services

Skill statements (paraphrased):

- Select a support resource
- Recognize support-plan differences

## Technologies and Concepts

Cloud value proposition, AWS Shared Responsibility Model, AWS global infrastructure, AWS Well-Architected Framework, AWS Cloud Adoption Framework, migration strategies, high availability, fault tolerance, elasticity and scalability, disaster recovery, least privilege, federation and cross-account access, encryption at rest and in transit, multi-account governance, infrastructure as code, stateless architecture, event-driven architecture, decoupling, caching, load balancing, Auto Scaling, Multi-AZ design, Multi-Region design, RTO and RPO, object block and file storage, relational versus NoSQL, VPC segmentation and routing, hybrid connectivity, monitoring logging and auditing, rightsizing, pricing models, data transfer costs, AWS Support resources, service quotas, streaming and batch ingestion, backup and lifecycle, AWS APIs, AWS SDKs, AWS Management Console and AWS CLI, AWS compliance, EC2 purchasing options, AWS Partner Network, AWS Pricing Calculator, AWS Professional Services, AWS re:Post, AWS Prescriptive Guidance, AWS Security Blog, AWS Support Center and plans, AWS Knowledge Center, AWS Solutions Architects, cloud migration and data transfer, management and governance

## Listed In-Scope Services

Amazon Athena, Amazon EMR, AWS Glue, Amazon Kinesis, Amazon OpenSearch Service, Amazon QuickSight, Amazon Redshift, Amazon EventBridge, Amazon SNS, Amazon SQS, AWS Step Functions, Amazon Connect, Amazon SES, AWS Budgets, AWS Cost and Usage Reports, AWS Cost Explorer, AWS Marketplace, AWS Batch, Amazon EC2, AWS Elastic Beanstalk, Amazon Lightsail, AWS Outposts, Amazon ECR, Amazon ECS, Amazon EKS, AWS Support, Amazon Aurora, Amazon DocumentDB, Amazon DynamoDB, Amazon ElastiCache, Amazon Neptune, Amazon RDS, AWS CLI, AWS CodeBuild, AWS CodePipeline, AWS X-Ray, Amazon AppStream 2.0, Amazon WorkSpaces, Amazon WorkSpaces Secure Browser, AWS Amplify, AWS AppSync, AWS IoT Core, Amazon Comprehend, Amazon Kendra, Amazon Lex, Amazon Polly, Amazon Q, Amazon Rekognition, Amazon SageMaker AI, Amazon Textract, Amazon Transcribe, Amazon Translate, AWS Auto Scaling, AWS CloudFormation, AWS CloudTrail, Amazon CloudWatch, AWS Compute Optimizer, AWS Config, AWS Control Tower, AWS Health Dashboard, AWS License Manager, AWS Management Console, AWS Organizations, AWS Service Catalog, Service Quotas, AWS Systems Manager, AWS Trusted Advisor, AWS Well-Architected Tool, AWS Application Discovery Service, AWS Application Migration Service, AWS Database Migration Service, Migration Evaluator, AWS Migration Hub, AWS Schema Conversion Tool, AWS Snow Family, Amazon API Gateway, Amazon CloudFront, AWS Direct Connect, AWS Global Accelerator, AWS PrivateLink, Amazon Route 53, AWS Transit Gateway, Amazon VPC, AWS VPN, AWS Site-to-Site VPN, AWS Client VPN, AWS Artifact, AWS Audit Manager, AWS Certificate Manager, AWS CloudHSM, Amazon Cognito, Amazon Detective, AWS Directory Service, AWS Firewall Manager, Amazon GuardDuty, AWS IAM, AWS IAM Identity Center, Amazon Inspector, AWS KMS, Amazon Macie, AWS Resource Access Manager, AWS Secrets Manager, AWS Security Hub, AWS Shield, AWS WAF, AWS Fargate, AWS Lambda, AWS Backup, Amazon EBS, Amazon EFS, AWS Elastic Disaster Recovery, Amazon FSx, Amazon S3, Amazon S3 Glacier, AWS Storage Gateway

## Listed Out-of-Scope Services

[Official out-of-scope list](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html): Amazon AppFlow, AWS Clean Rooms, AWS Data Exchange, Amazon DataZone, Amazon MSK, Amazon Timestream for LiveAnalytics, AWS AppFabric, Amazon Simple Workflow Service, Amazon WorkDocs, Amazon WorkMail, AWS App Runner, AWS Copilot, AWS Wavelength, AWS Application Cost Profiler, Amazon DevPay, AWS Activate, AWS IQ, AWS Managed Services, AWS Billing Conductor, Amazon Keyspaces, Amazon MemoryDB for Redis OSS, AWS AppConfig, AWS Application Composer, AWS CodeArtifact, AWS CodeDeploy, Amazon CodeGuru, AWS CloudShell, AWS Device Farm, Amazon GameLift, Amazon Lumberyard, AWS IoT Device Defender, AWS IoT Greengrass, Amazon Monitron, Amazon Fraud Detector, Amazon Lookout for Metrics, Amazon Mechanical Turk, AWS Panorama, Amazon Personalize, AWS Chatbot, Amazon Data Lifecycle Manager, Amazon Elastic Transcoder, AWS Launch Wizard, AWS Elemental Appliances and Software, AWS Elemental MediaConnect, AWS Elemental MediaConvert, AWS Elemental MediaLive, AWS Elemental MediaPackage, AWS Elemental MediaStore, AWS Elemental MediaTailor, Amazon Interactive Video Service, AWS Migration Hub Refactor Spaces, AWS Transfer Family, AWS Cloud Map, AWS Network Access Analyzer, AWS Ground Station, Amazon VPC Lattice, Amazon Cloud Directory, AWS Network Firewall, AWS RoboMaker, Amazon FSx for Lustre

Out-of-scope lists are also non-exhaustive. Existing notes on these services are retained as supplementary or historical material rather than deleted.

## Source and Copyright Note

Statements above are concise paraphrases for mapping; consult the linked AWS guide for authoritative wording. No completeness beyond the checked guide version is claimed.
