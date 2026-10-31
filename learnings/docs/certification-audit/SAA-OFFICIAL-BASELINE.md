# SAA Official Baseline

- Certification: **AWS Certified Solutions Architect - Associate**
- Current exam code verified: **SAA-C03**
- Checked: **2026-07-21**
- [Official exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html)
- [Official in-scope services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html)

AWS states that its service and feature lists are non-exhaustive and subject to change. This baseline maps the published guide as checked; it does not guarantee future exam coverage.

## Candidate and Required Depth

The target learner needs at least one year of hands-on design experience. Coverage requires architecture decisions, integrations, security, resilience, performance, scalability, cost optimization, and explicit trade-offs; a definition alone is insufficient.

## Domains

| Domain | Name | Weight |
|---|---|---|
| 1 | Design Secure Architectures | 30% |
| 2 | Design Resilient Architectures | 26% |
| 3 | Design High-Performing Architectures | 24% |
| 4 | Design Cost-Optimized Architectures | 20% |

## Tasks, Knowledge, and Skills

### Task 1.1: Design secure access to AWS resources

Expected repository category: `03-identity-governance-and-organizations/`

Knowledge statements (paraphrased):

- multi-account access
- federation and IAM Identity Center
- least privilege
- resource and identity policies
- SCPs and Control Tower

Skill statements (paraphrased):

- Design root and MFA controls
- Design cross-account and federated access
- Apply least privilege

### Task 1.2: Design secure workloads and applications

Expected repository category: `09-security-and-compliance/`

Knowledge statements (paraphrased):

- credential management
- secure endpoints
- network segmentation
- edge protection
- threat detection

Skill statements (paraphrased):

- Design VPC security boundaries
- Select WAF, Shield, firewall, and detection controls
- Secure hybrid connectivity

### Task 1.3: Determine data security controls

Expected repository category: `09-security-and-compliance/`

Knowledge statements (paraphrased):

- data classification
- encryption at rest and in transit
- key and certificate management
- retention and recovery
- compliance controls

Skill statements (paraphrased):

- Design KMS and TLS usage
- Design backup, replication, lifecycle, and key rotation

### Task 2.1: Design scalable and loosely coupled architectures

Expected repository category: `13-architecture-and-design-patterns/`

Knowledge statements (paraphrased):

- stateless and microservice design
- event-driven architecture
- messaging and workflows
- caching
- horizontal scaling

Skill statements (paraphrased):

- Design multi-tier and serverless systems
- Select queues, topics, events, and workflows
- Select load balancing and containers

### Task 2.2: Design highly available and fault-tolerant architectures

Expected repository category: `13-architecture-and-design-patterns/`

Knowledge statements (paraphrased):

- failure domains
- Multi-AZ and Multi-Region
- disaster recovery strategies
- durability and failover
- service quotas and observability

Skill statements (paraphrased):

- Remove single points of failure
- Design recovery and failover
- Select resilient data and compute patterns

### Task 3.1: Determine high-performing storage solutions

Expected repository category: `05-storage/`

Knowledge statements (paraphrased):

- object, block, and file characteristics
- storage performance
- access patterns
- hybrid storage
- data lifecycle

Skill statements (paraphrased):

- Select S3, EBS, EFS, FSx, and instance storage
- Match throughput, IOPS, latency, and durability requirements

### Task 3.2: Design high-performing and elastic compute

Expected repository category: `04-compute/`

Knowledge statements (paraphrased):

- compute selection
- instance families and sizing
- Auto Scaling
- load balancing
- containers and serverless

Skill statements (paraphrased):

- Select compute for workload characteristics
- Design elastic capacity
- Choose scaling metrics and policies

### Task 3.3: Determine high-performing database solutions

Expected repository category: `06-databases/`

Knowledge statements (paraphrased):

- relational and nonrelational selection
- read scaling
- caching
- serverless databases
- database migration

Skill statements (paraphrased):

- Choose database engines
- Design replicas, caches, and partitions
- Match consistency and performance needs

### Task 3.4: Determine high-performing network architectures

Expected repository category: `07-networking-and-content-delivery/`

Knowledge statements (paraphrased):

- VPC design
- hybrid connectivity
- DNS and routing
- edge delivery
- network performance

Skill statements (paraphrased):

- Design subnets and routing
- Choose VPN, Direct Connect, Transit Gateway, and peering
- Select CloudFront or Global Accelerator

### Task 3.5: Determine high-performing data ingestion and transformation

Expected repository category: `14-ai-ml-analytics-and-other-services/`

Knowledge statements (paraphrased):

- streaming and batch ingestion
- data transformation
- data lakes and warehouses
- analytics stores
- transfer services

Skill statements (paraphrased):

- Select Kinesis, Firehose, Glue, EMR, and Redshift
- Design ingestion for volume, velocity, and format

### Task 4.1: Design cost-optimized storage

Expected repository category: `05-storage/`

Knowledge statements (paraphrased):

- storage classes
- lifecycle policies
- retention
- access patterns
- backup cost

Skill statements (paraphrased):

- Choose cost-effective storage
- Automate tiering and expiration
- Balance retrieval and durability needs

### Task 4.2: Design cost-optimized compute

Expected repository category: `04-compute/`

Knowledge statements (paraphrased):

- purchasing options
- rightsizing
- elasticity
- serverless and containers
- license considerations

Skill statements (paraphrased):

- Choose On-Demand, Spot, Reserved Instances, or Savings Plans
- Reduce idle capacity
- Match compute model to demand

### Task 4.3: Design cost-optimized databases

Expected repository category: `06-databases/`

Knowledge statements (paraphrased):

- engine and licensing costs
- capacity models
- read scaling
- retention and backup
- managed service trade-offs

Skill statements (paraphrased):

- Select cost-effective database
- Right-size and scale database capacity
- Balance operational and service cost

### Task 4.4: Design cost-optimized networks

Expected repository category: `07-networking-and-content-delivery/`

Knowledge statements (paraphrased):

- data transfer charges
- NAT and endpoint costs
- hybrid connectivity costs
- content delivery
- network topology

Skill statements (paraphrased):

- Reduce cross-AZ and internet transfer cost
- Choose endpoints and gateways
- Balance managed connectivity cost and operations

## Technologies and Concepts

Cloud value proposition, AWS Shared Responsibility Model, AWS global infrastructure, AWS Well-Architected Framework, AWS Cloud Adoption Framework, migration strategies, high availability, fault tolerance, elasticity and scalability, disaster recovery, least privilege, federation and cross-account access, encryption at rest and in transit, multi-account governance, infrastructure as code, stateless architecture, event-driven architecture, decoupling, caching, load balancing, Auto Scaling, Multi-AZ design, Multi-Region design, RTO and RPO, object block and file storage, relational versus NoSQL, VPC segmentation and routing, hybrid connectivity, monitoring logging and auditing, rightsizing, pricing models, data transfer costs, AWS Support resources, service quotas, streaming and batch ingestion, backup and lifecycle, AWS APIs, AWS SDKs, AWS Management Console and AWS CLI, AWS compliance, EC2 purchasing options, AWS Partner Network, AWS Pricing Calculator, AWS Professional Services, AWS re:Post, AWS Prescriptive Guidance, AWS Security Blog, AWS Support Center and plans, AWS Knowledge Center, AWS Solutions Architects, cloud migration and data transfer, management and governance

## Listed In-Scope Services

Amazon Athena, AWS Data Exchange, Amazon Data Firehose, Amazon EMR, AWS Glue, Amazon Kinesis, AWS Lake Formation, Amazon MSK, Amazon OpenSearch Service, Amazon Quick, Amazon Redshift, Amazon AppFlow, AWS AppSync, Amazon EventBridge, Amazon MQ, Amazon SNS, Amazon SQS, AWS Step Functions, AWS Budgets, AWS Cost and Usage Report, AWS Cost Explorer, Savings Plans, AWS Batch, Amazon EC2, Amazon EC2 Auto Scaling, AWS Elastic Beanstalk, AWS Outposts, AWS Serverless Application Repository, VMware Cloud on AWS, AWS Wavelength, Amazon ECR, Amazon ECS, Amazon ECS Anywhere, Amazon EKS, Amazon EKS Anywhere, Amazon EKS Distro, Amazon Aurora, Amazon Aurora Serverless, Amazon DocumentDB, Amazon DynamoDB, Amazon ElastiCache, Amazon Keyspaces, Amazon Neptune, Amazon RDS, Amazon Redshift, AWS X-Ray, AWS Amplify, Amazon API Gateway, AWS Device Farm, Amazon Comprehend, Amazon Kendra, Amazon Lex, Amazon Polly, Amazon Rekognition, Amazon SageMaker AI, Amazon Textract, Amazon Transcribe, Amazon Translate, AWS Auto Scaling, AWS CLI, AWS CloudFormation, AWS CloudTrail, Amazon CloudWatch, AWS Compute Optimizer, AWS Config, AWS Control Tower, AWS Health Dashboard, AWS License Manager, Amazon Managed Grafana, Amazon Managed Service for Prometheus, AWS Management Console, AWS Organizations, AWS Service Catalog, AWS Systems Manager, AWS Trusted Advisor, AWS Well-Architected Tool, Amazon Elastic Transcoder, Amazon Kinesis Video Streams, AWS Application Migration Service, AWS DataSync, AWS DMS, AWS Snow Family, AWS Transfer Family, AWS Client VPN, Amazon CloudFront, AWS Direct Connect, Elastic Load Balancing, AWS Global Accelerator, AWS PrivateLink, Amazon Route 53, AWS Site-to-Site VPN, AWS Transit Gateway, Amazon VPC, AWS Artifact, AWS Audit Manager, AWS Certificate Manager, AWS CloudHSM, Amazon Cognito, Amazon Detective, AWS Directory Service, AWS Firewall Manager, Amazon GuardDuty, AWS IAM Identity Center, Amazon Inspector, AWS KMS, Amazon Macie, AWS Network Firewall, AWS Resource Access Manager, AWS Secrets Manager, AWS Security Hub, AWS Shield, AWS WAF, AWS IAM, AWS Fargate, AWS Lambda, AWS Backup, Amazon EBS, Amazon EFS, Amazon FSx, Amazon S3, Amazon S3 Glacier, AWS Storage Gateway

## Listed Out-of-Scope Services

[Official out-of-scope list](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-out-of-scope-services.html): Amazon MWAA, Amazon Sumerian, Amazon Managed Blockchain, Amazon Lightsail, Amazon RDS on VMware, AWS CDK, AWS CloudShell, AWS CodeArtifact, AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, Amazon Corretto, AWS Fault Injection Simulator, AWS Tools and SDKs, Amazon Location Service, Amazon GameLift, All IoT services, Apache MXNet on AWS, Amazon Augmented AI, AWS DeepComposer, AWS Deep Learning AMIs, AWS Deep Learning Containers, Amazon DevOps Guru, Amazon Elastic Inference, Amazon HealthLake, AWS Inferentia, Amazon Personalize, PyTorch on AWS, Amazon SageMaker Canvas, Amazon SageMaker Ground Truth, TensorFlow on AWS, AWS Console Mobile Application, AWS Distro for OpenTelemetry, AWS Elemental Appliances and Software, AWS Elemental MediaConnect, AWS Elemental MediaConvert, AWS Elemental MediaLive, AWS Elemental MediaPackage, AWS Elemental MediaTailor, Amazon Interactive Video Service, Migration Evaluator, AWS Cloud Map, Amazon Braket, AWS Ground Station

Out-of-scope lists are also non-exhaustive. Existing notes on these services are retained as supplementary or historical material rather than deleted.

## Source and Copyright Note

Statements above are concise paraphrases for mapping; consult the linked AWS guide for authoritative wording. No completeness beyond the checked guide version is claimed.
