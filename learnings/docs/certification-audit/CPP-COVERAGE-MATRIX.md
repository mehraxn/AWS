# CLF-C02 Coverage Matrix

This is the authoritative Cloud Practitioner coverage baseline for the repository as inspected on **2026-07-27**. It supersedes earlier CPP totals for current planning but preserves the older audit files as history.

The denominator is **134 atomic criteria**: every knowledge and skill bullet in the 19 task statements in the current official CLF-C02 exam guide. AWS describes the guide and service lists as non-exhaustive and subject to change. Status measures repository evidence, not likelihood of an exam question or a guarantee of readiness.

## Method

- **Sources:** current official [CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html), its four domain pages, [technologies and concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-technologies-concepts.html), and [in-scope service list](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html), checked 2026-07-27.
- **Evidence:** lesson bodies, not filenames, badges, indexes, or old audit claims alone.
- **Depth:** Level 2 foundational understanding unless a row explicitly says Level 1 recognition or Level 3 CPP scenario reasoning. The levels are defined in the [CPP content and style standard](../content-standards/CPP-CONTENT-AND-STYLE-STANDARD.md).
- **Statuses:** only `complete`, `partial`, `mention-only`, `missing`, `wrong-depth`, `duplicate-evidence`, and `potentially-outdated` are used. A status is exclusive.
- **Evidence paths:** the first path is the canonical owner; paths after a semicolon are supporting evidence.

## Domain 1: Cloud Concepts

### Task 1.1: Define the benefits of the AWS Cloud

Canonical evidence: `01-cloud-fundamentals/02-cloud-concepts-and-benefits.md`  
Supporting evidence: `02-global-infrastructure/01-regions-availability-zones-and-edge.md`, `13-architecture-and-design-patterns/01-highly-available-web-applications.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-1.1-K1 | Knowledge | Value proposition of the AWS Cloud | L2 | complete | Defines on-demand delivery, managed services, agility, elasticity, global reach, and usage-based economics. | Maintain and refresh references. | P2 |
| CPP-1.1-S1 | Skill | Benefits of global infrastructure, including deployment speed and global reach | L3 | complete | Explains business benefit and Region selection constraints with scenarios. | Maintain. | P2 |
| CPP-1.1-S2 | Skill | Advantages of high availability, elasticity, and agility | L3 | complete | Separates the concepts and maps scenario wording to each. | Maintain. | P2 |

### Task 1.2: Identify design principles of the AWS Cloud

Canonical evidence: `13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-1.2-K1 | Knowledge | AWS Well-Architected Framework | L2 | complete | Defines the framework, review process, tool distinction, and improvement purpose. | Maintain. | P2 |
| CPP-1.2-S1 | Skill | Understand all six Well-Architected pillars | L2 | complete | Names and explains the six current pillars. | Maintain against official framework changes. | P2 |
| CPP-1.2-S2 | Skill | Distinguish the Well-Architected pillars | L3 | complete | Decision table and traps distinguish pillar outcomes. | Maintain. | P2 |

### Task 1.3: Understand migration benefits and strategies

Canonical planned owner: `11-migration-and-hybrid-cloud/01-cpp-migration-strategies.md` (not yet created)  
Supporting evidence: `13-architecture-and-design-patterns/aws-cloud-adoption-framework/01-overview.md`, `11-migration-and-hybrid-cloud/aws-migration-hub/01-overview.md`, `11-migration-and-hybrid-cloud/aws-snowball-edge/01-overview.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-1.3-K1 | Knowledge | Cloud adoption strategies | L2 | partial | CAF readiness is explained, but no canonical beginner lesson connects adoption goals to migration approaches. | Create the planned migration-strategy lesson. | P0 |
| CPP-1.3-K2 | Knowledge | Resources supporting the cloud migration journey | L2 | partial | Discovery, Migration Hub, DMS, SCT, Snowball, and guidance exist in separate files; there is no staged journey or selection overview. | Add a journey and resource-selection map. | P0 |
| CPP-1.3-S1 | Skill | Understand AWS CAF components and transformation outcomes | L2 | partial | Six perspectives are present; the official outcome examples—reduced risk, ESG improvement, revenue, and operational efficiency—are not taught clearly. | Expand the CAF lesson at CPP depth. | P1 |
| CPP-1.3-S2 | Skill | Select an appropriate migration strategy, including replication or Snowball | L3 | partial | Individual tools are described, and rehost/replatform/refactor are mentioned, but strategy reasoning is not canonical or complete. | Add strategy-to-tool scenarios and explained checks. | P0 |

### Task 1.4: Understand cloud economics

Canonical evidence: `01-cloud-fundamentals/02-cloud-concepts-and-benefits.md`  
Supporting evidence: `12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md`, `12-billing-pricing-and-support/aws-billing-and-cost-management/04-rightsizing.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-1.4-K1 | Knowledge | Aspects of cloud economics | L2 | complete | Covers variable consumption, managed services, scale, and cost alignment. | Maintain. | P2 |
| CPP-1.4-K2 | Knowledge | Cost savings from moving to the cloud | L2 | complete | Explains why savings can occur without claiming migration is automatically cheaper. | Maintain. | P2 |
| CPP-1.4-S1 | Skill | Fixed costs compared with variable costs | L3 | complete | Definitions and purchasing scenarios are clear. | Maintain. | P2 |
| CPP-1.4-S2 | Skill | Costs associated with on-premises environments | L2 | complete | Hardware, facilities, procurement, and operating effort are addressed. | Maintain. | P2 |
| CPP-1.4-S3 | Skill | BYOL compared with included licensing | L2 | mention-only | Licensing appears mainly as a Dedicated Host use case; no learner can reliably compare the models. | Add a stable licensing subsection and AWS License Manager distinction. | P1 |
| CPP-1.4-S4 | Skill | Rightsizing | L3 | complete | Dedicated lesson defines measurement-driven fit and distinguishes discounts and scaling. | Add official references during style batch. | P2 |
| CPP-1.4-S5 | Skill | Benefits of automation | L2 | complete | Connects repeatability, scheduling, scaling, and reduced waste. | Maintain. | P2 |
| CPP-1.4-S6 | Skill | Economies of scale | L2 | complete | Clear definition and business relevance are present. | Maintain. | P2 |

## Domain 2: Security and Compliance

### Task 2.1: Understand the AWS shared responsibility model

Canonical evidence: `01-cloud-fundamentals/01-shared-responsibility-model.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-2.1-K1 | Knowledge | AWS shared responsibility model | L2 | complete | Defines security of and in the cloud and the shifting boundary. | Maintain. | P2 |
| CPP-2.1-S1 | Skill | Recognize model components | L3 | complete | Layer table and scenarios support recognition. | Maintain. | P2 |
| CPP-2.1-S2 | Skill | Describe customer responsibilities | L2 | complete | Data, identity, configuration, guest OS, logging, and recovery are explicit. | Maintain. | P2 |
| CPP-2.1-S3 | Skill | Describe AWS responsibilities | L2 | complete | Facilities, hardware, network, hypervisor, and managed layers are explicit. | Maintain. | P2 |
| CPP-2.1-S4 | Skill | Describe shared responsibilities | L2 | complete | Patch, configuration, training, and identity context is explained. | Maintain. | P2 |
| CPP-2.1-S5 | Skill | Explain shifts for EC2, RDS, and Lambda | L3 | complete | Side-by-side table and service scenarios meet CPP reasoning depth. | Maintain. | P2 |

### Task 2.2: Understand security, governance, and compliance concepts

Canonical evidence: `09-security-and-compliance/security-and-compliance-overview/01-overview.md`  
Supporting evidence: `13-architecture-and-design-patterns/security/01-data-protection-patterns.md`, `15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md`, `15-comparisons-and-decision-guides/security/01-security-service-selection.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-2.2-K1 | Knowledge | AWS compliance and governance concepts | L2 | partial | The overview identifies resources but does not clearly teach governance versus compliance and customer evidence obligations. | Rewrite the canonical overview around the concepts. | P0 |
| CPP-2.2-K2 | Knowledge | Benefits of cloud security, including encryption | L2 | complete | Encryption, managed controls, and customer choices are explained. | Maintain. | P2 |
| CPP-2.2-K3 | Knowledge | Capture and locate security-related logs | L3 | complete | CloudWatch, CloudTrail, Config, and VPC Flow Logs are distinguished. | Add links from the security overview. | P2 |
| CPP-2.2-S1 | Skill | Find AWS compliance information with Artifact | L2 | complete | Artifact reports and agreements are distinguished from Audit Manager. | Maintain. | P2 |
| CPP-2.2-S2 | Skill | Understand geographic and industry compliance needs | L3 | partial | Region/residency and general programs appear separately; industry and location scenario reasoning is thin. | Add two compliance-context scenarios. | P1 |
| CPP-2.2-S3 | Skill | Describe customer use of Inspector, Security Hub, GuardDuty, and Shield | L3 | complete | Security selection guide explains purpose and distractors. | Maintain. | P2 |
| CPP-2.2-S4 | Skill | Identify encryption in transit and at rest | L3 | complete | Data-protection lesson compares both and related services. | Maintain. | P2 |
| CPP-2.2-S5 | Skill | Recognize CloudWatch, CloudTrail, Audit Manager, Config, and access reports | L3 | complete | Primary operational distinctions are clear; Audit Manager and access reports have supporting lessons. | Improve canonical cross-links. | P2 |
| CPP-2.2-S6 | Skill | Recognize that compliance requirements vary by service | L3 | partial | Shared responsibility implies the shift, but no focused compliance scenario compares service models. | Add EC2/RDS/S3 compliance examples. | P1 |

### Task 2.3: Identify AWS access management capabilities

Canonical evidence: `03-identity-governance-and-organizations/aws-iam/01-overview.md`  
Supporting evidence: `03-identity-governance-and-organizations/aws-iam/10-root-user.md`, `03-identity-governance-and-organizations/aws-iam-identity-center/01-overview.md`, `15-comparisons-and-decision-guides/identity-and-governance/03-users-groups-and-roles.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-2.3-K1 | Knowledge | Identity and access management with IAM | L2 | complete | Canonical IAM lesson covers authentication, authorization, identities, policies, and evaluation. | Maintain. | P2 |
| CPP-2.3-K2 | Knowledge | Importance of protecting the root user | L3 | complete | Root lesson explains uniqueness, MFA, access keys, and daily-use traps. | Maintain. | P2 |
| CPP-2.3-K3 | Knowledge | Least privilege | L3 | complete | Principle, policy behavior, and scenario use are present. | Maintain. | P2 |
| CPP-2.3-K4 | Knowledge | IAM Identity Center | L2 | complete | Workforce, multi-account, identity-source, permission-set, and temporary-access use are clear. | Maintain. | P2 |
| CPP-2.3-S1 | Skill | Access keys, password policies, and credential storage | L3 | partial | Roles and Secrets Manager are covered; password policy and safe human-versus-workload credential choices are fragmented. | Add one credential-selection section and check. | P1 |
| CPP-2.3-S2 | Skill | Authentication with MFA, Identity Center, and cross-account roles | L3 | complete | All three are explained with temporary credential context. | Maintain. | P2 |
| CPP-2.3-S3 | Skill | Users, groups, custom and managed policies under least privilege | L3 | complete | Dedicated lessons and a comparison guide provide distinctions. | Clarify canonical linking to reduce repetition. | P2 |
| CPP-2.3-S4 | Skill | Tasks only the root user can perform | L2 | partial | Root uniqueness is strong, but the lesson avoids a current, sourced set of root-only task examples. | Add a short official-reference-backed list with checked date. | P1 |
| CPP-2.3-S5 | Skill | Methods that protect the root user | L3 | complete | MFA, no root access keys, restricted use, monitoring, and emergency access are present. | Maintain. | P2 |
| CPP-2.3-S6 | Skill | Federated identity management | L2 | complete | Federation and Identity Center are defined and distinguished. | Maintain. | P2 |

### Task 2.4: Identify components and resources for security

Canonical evidence: `15-comparisons-and-decision-guides/security/01-security-service-selection.md`  
Supporting evidence: `09-security-and-compliance/README.md`, `12-billing-pricing-and-support/aws-trusted-advisor/01-overview.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-2.4-K1 | Knowledge | Security capabilities provided by AWS | L2 | complete | Selection guide groups preventive, detective, data, and network services. | Maintain. | P2 |
| CPP-2.4-K2 | Knowledge | Security documentation provided by AWS | L2 | partial | Security Center is described, but Knowledge Center, Security Blog, and service documentation are not presented as one selection set. | Add a security-resource subsection. | P1 |
| CPP-2.4-S1 | Skill | Describe WAF, Firewall Manager, Shield, and GuardDuty | L3 | complete | Guide explains scope, fit, and common confusion. | Maintain. | P2 |
| CPP-2.4-S2 | Skill | Third-party security products in AWS Marketplace | L1 | missing | Marketplace is mentioned in support material but security-product discovery is not meaningfully taught. | Add to a canonical Marketplace lesson. | P0 |
| CPP-2.4-S3 | Skill | Locate Knowledge Center, Security Center, and Security Blog | L2 | partial | Security Center has a lesson; the other resources are fragmented or absent. | Add direct official links and selection guidance. | P1 |
| CPP-2.4-S4 | Skill | Use Trusted Advisor to identify security issues | L2 | complete | Trusted Advisor lesson identifies security checks and its advisory role. | Add checked date for volatile access details. | P2 |

## Domain 3: Cloud Technology and Services

### Task 3.1: Define methods of deploying and operating in the AWS Cloud

Canonical planned owner: `10-monitoring-management-and-deployment/01-access-deployment-and-operations.md` (not yet created)  
Supporting evidence: `10-monitoring-management-and-deployment/aws-cloudformation/01-overview.md`, `01-cloud-fundamentals/02-cloud-concepts-and-benefits.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-3.1-K1 | Knowledge | Ways to provision and operate in AWS | L2 | partial | CloudFormation and several deployment tools exist, but no beginner-wide operating-method overview exists. | Create the planned canonical lesson. | P0 |
| CPP-3.1-K2 | Knowledge | Ways to access AWS services | L2 | mention-only | Console, CLI, SDK, and APIs appear incidentally; they are not defined or compared. | Add access-method definitions and decision table. | P0 |
| CPP-3.1-K3 | Knowledge | Cloud deployment models | L2 | complete | Public, private, and hybrid models are defined in cloud fundamentals. | Link from the planned owner. | P2 |
| CPP-3.1-S1 | Skill | Choose API, SDK, CLI, Console, or IaC | L3 | partial | IaC is explained, but a complete method-selection scenario is absent. | Add scenarios and distractor explanations. | P0 |
| CPP-3.1-S2 | Skill | Choose one-time operations or repeatable processes | L3 | partial | Automation value is present; the explicit decision is not practiced. | Add one-time versus repeatable examples. | P1 |
| CPP-3.1-S3 | Skill | Identify cloud, hybrid, and on-premises deployment | L3 | complete | Definitions and a hybrid scenario exist. | Maintain. | P2 |

### Task 3.2: Define the AWS global infrastructure

Canonical evidence: `02-global-infrastructure/01-regions-availability-zones-and-edge.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-3.2-K1 | Knowledge | Regions, Availability Zones, and edge locations | L2 | complete | Definitions, scope, and purposes are compared. | Maintain. | P2 |
| CPP-3.2-K2 | Knowledge | High availability | L3 | complete | Multi-AZ purpose and customer design responsibility are clear. | Maintain. | P2 |
| CPP-3.2-K3 | Knowledge | Use of multiple Regions | L3 | complete | DR, continuity, latency, and sovereignty uses are taught. | Maintain. | P2 |
| CPP-3.2-K4 | Knowledge | Benefits of edge locations | L2 | complete | Latency, delivery, DNS, and caching are distinguished. | Maintain. | P2 |
| CPP-3.2-S1 | Skill | Relationships among Regions, AZs, and edge locations | L3 | complete | Side-by-side comparison and scenarios provide recognition. | Maintain. | P2 |
| CPP-3.2-S2 | Skill | Achieve high availability with multiple AZs | L3 | complete | Explicit scenario reasoning is present. | Maintain. | P2 |
| CPP-3.2-S3 | Skill | Recognize separate AZ failure boundaries | L2 | complete | Isolation is stated without claiming absolute independence. | Maintain. | P2 |
| CPP-3.2-S4 | Skill | Choose multiple Regions for DR, continuity, latency, or sovereignty | L3 | complete | All official examples are addressed. | Maintain. | P2 |

### Task 3.3: Identify AWS compute services

Canonical evidence: `15-comparisons-and-decision-guides/compute-and-storage/01-core-selection-guide.md`  
Supporting evidence: `04-compute/amazon-ec2/01-overview.md`, `04-compute/containers/01-ecs-eks-and-fargate.md`, `04-compute/aws-lambda/01-overview.md`, `04-compute/ec2-auto-scaling/01-target-tracking-scaling.md`, `04-compute/elastic-load-balancing/01-overview.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-3.3-K1 | Knowledge | AWS compute services | L2 | complete | Core selection guide distinguishes virtual machines, containers, functions, and managed platforms. | Maintain. | P2 |
| CPP-3.3-S1 | Skill | Select EC2 instance families, such as compute or storage optimized | L3 | complete | EC2 material and selection guide connect workload shape to families. | Consolidate links during comparison batch. | P2 |
| CPP-3.3-S2 | Skill | Select ECS or EKS container options | L3 | complete | Container guide distinguishes orchestrators and Fargate. | Maintain. | P2 |
| CPP-3.3-S3 | Skill | Select Fargate or Lambda serverless compute | L3 | complete | Serverless patterns and compute comparison explain fit and limits. | Maintain. | P2 |
| CPP-3.3-S4 | Skill | Recognize Auto Scaling elasticity | L3 | complete | Target-tracking lesson links demand to elastic capacity. | Maintain. | P2 |
| CPP-3.3-S5 | Skill | Identify load balancer purposes | L3 | complete | Distribution, health checks, and availability purpose are clear. | Maintain. | P2 |

### Task 3.4: Identify AWS database services

Canonical evidence: `15-comparisons-and-decision-guides/databases/01-database-selection-guide.md`  
Supporting evidence: `06-databases/`, `11-migration-and-hybrid-cloud/aws-database-migration-service/01-overview.md`, `11-migration-and-hybrid-cloud/aws-schema-conversion-tool/01-overview.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-3.4-K1 | Knowledge | AWS database services | L2 | complete | Selection guide covers relational, key-value/NoSQL, cache, and self-managed options. | Maintain. | P2 |
| CPP-3.4-K2 | Knowledge | Database migration | L2 | complete | DMS and SCT purposes and combination are explained. | Improve journey cross-link. | P2 |
| CPP-3.4-S1 | Skill | Choose EC2-hosted or AWS-managed databases | L3 | complete | Responsibility and operational trade-offs are compared. | Maintain. | P2 |
| CPP-3.4-S2 | Skill | Identify RDS and Aurora as relational options | L3 | complete | Both have canonical lessons and comparison evidence. | Maintain. | P2 |
| CPP-3.4-S3 | Skill | Identify DynamoDB as NoSQL | L3 | complete | Service purpose and database-category choice are clear. | Maintain. | P2 |
| CPP-3.4-S4 | Skill | Identify ElastiCache as an in-memory option and DMS/SCT as migration tools | L3 | complete | Selection and migration distinctions are present. | Maintain. | P2 |

### Task 3.5: Identify AWS network services

Canonical evidence: `07-networking-and-content-delivery/networking-guide/01-cloud-practitioner-study-guide.md`  
Supporting evidence: `07-networking-and-content-delivery/amazon-vpc/`, `15-comparisons-and-decision-guides/networking/`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-3.5-K1 | Knowledge | AWS network services | L2 | complete | Long-form study guide covers the main connectivity situations. | Add a shorter entry path. | P2 |
| CPP-3.5-S1 | Skill | Identify VPC components such as subnets and gateways | L3 | complete | VPC overview and component lesson explain purpose and traffic path. | Maintain. | P2 |
| CPP-3.5-S2 | Skill | Understand VPC security with network ACLs, security groups, and Inspector | L3 | complete | Network controls are compared; Inspector is correctly treated as workload vulnerability management. | Maintain. | P2 |
| CPP-3.5-S3 | Skill | Understand the purpose of Route 53 | L2 | partial | Service lesson is detailed but lacks a compact beginner decision and explained knowledge check. | Refocus the canonical overview at CPP depth. | P1 |
| CPP-3.5-S4 | Skill | Choose AWS VPN or Direct Connect | L3 | complete | Connectivity comparison distinguishes encrypted internet connectivity and dedicated connectivity. | Maintain. | P2 |

### Task 3.6: Identify AWS storage services

Canonical evidence: `15-comparisons-and-decision-guides/compute-and-storage/01-core-selection-guide.md`  
Supporting evidence: `05-storage/`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-3.6-K1 | Knowledge | AWS storage services | L2 | complete | Object, block, file, backup, archive, and hybrid storage are distinguished. | Maintain. | P2 |
| CPP-3.6-S1 | Skill | Identify object-storage uses | L3 | complete | S3 use cases and selection criteria are clear. | Maintain. | P2 |
| CPP-3.6-S2 | Skill | Distinguish S3 storage classes | L3 | complete | Access frequency, retrieval, resilience, and cost drivers are compared without relying on exact prices. | Add checked date to volatile details. | P2 |
| CPP-3.6-S3 | Skill | Identify EBS and instance store block storage | L3 | complete | Persistence and attachment distinctions are scenario-ready. | Maintain. | P2 |
| CPP-3.6-S4 | Skill | Identify EFS and FSx file services | L3 | complete | File-family selection guide provides fit and distractors. | Maintain. | P2 |
| CPP-3.6-S5 | Skill | Identify cached file systems with Storage Gateway | L2 | complete | File Gateway and cached volumes are distinguished. | Clarify terminology during comparison batch. | P2 |
| CPP-3.6-S6 | Skill | Understand lifecycle-policy use cases | L3 | complete | S3 lifecycle lesson explains transitions and expiration. | Add official references/check date. | P2 |
| CPP-3.6-S7 | Skill | Understand AWS Backup use cases | L3 | complete | Central policy, supported resources, and distinction from availability are clear. | Maintain. | P2 |

### Task 3.7: Identify AI/ML and analytics services

Canonical evidence: `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md`  
Supporting evidence: `15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md`, `14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-3.7-K1 | Knowledge | AWS AI/ML services | L1 | complete | Recognition guide covers SageMaker AI and prebuilt AI services by task. | Maintain official names. | P2 |
| CPP-3.7-K2 | Knowledge | AWS analytics services | L1 | complete | Selection guide covers query, ETL, streaming, warehouses, clusters, and visualization. | Maintain. | P2 |
| CPP-3.7-S1 | Skill | Recognize tasks for SageMaker AI, Lex, and Kendra | L2 | complete | Service-to-task and distractor mapping is explicit. | Maintain. | P2 |
| CPP-3.7-S2 | Skill | Select Athena, Kinesis, Glue, and QuickSight for analytics tasks | L3 | complete | Comparison guide provides decision criteria and scenarios. | Maintain. | P2 |

### Task 3.8: Identify services from other in-scope categories

Canonical planned owner: `14-ai-ml-analytics-and-other-services/01-cpp-additional-service-recognition.md` (not yet created)  
Supporting evidence: `08-serverless-and-application-integration/`, `10-monitoring-management-and-deployment/`, `12-billing-pricing-and-support/aws-support/02-support-plans.md`, `14-ai-ml-analytics-and-other-services/`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-3.8-K1 | Knowledge | EventBridge, SNS, and SQS integration services | L2 | complete | Comparison guide teaches event routing, pub/sub notifications, and queues. | Create/link an SNS owner. | P2 |
| CPP-3.8-K2 | Knowledge | Connect and SES business applications | L1 | partial | Both services have lessons, but the category-level business need distinction is weak. | Add a compact recognition comparison. | P1 |
| CPP-3.8-K3 | Knowledge | Customer enablement, including AWS Support | L2 | complete | Support plans and resources are explained. | Maintain. | P2 |
| CPP-3.8-K4 | Knowledge | CodeBuild, CodePipeline, and X-Ray developer tools | L1 | partial | Separate lessons exist; category recognition and current product context are inconsistent. | Add one recognition table and links. | P1 |
| CPP-3.8-K5 | Knowledge | AppStream 2.0, WorkSpaces, and WorkSpaces Secure Browser | L1 | missing | No meaningful learner evidence exists. | Add recognition content for all three. | P0 |
| CPP-3.8-K6 | Knowledge | Amplify and AppSync frontend/mobile services | L1 | complete | Both are defined and their purposes are distinguishable. | Link through planned owner. | P2 |
| CPP-3.8-K7 | Knowledge | AWS IoT Core | L1 | partial | An IoT lesson exists, but current naming and the managed-device purpose need a checked canonical summary. | Refocus and source the lesson. | P1 |
| CPP-3.8-S1 | Skill | Choose messaging, alerts, and notifications | L3 | complete | SQS/SNS/EventBridge selection is scenario-ready. | Maintain. | P2 |
| CPP-3.8-S2 | Skill | Choose a service for a business-application need | L2 | partial | Connect versus SES is not explicitly practiced. | Add two recognition scenarios. | P1 |
| CPP-3.8-S3 | Skill | Choose business support assistance | L3 | complete | Support plan and assistance selection is strong. | Maintain against plan changes. | P2 |
| CPP-3.8-S4 | Skill | Identify tools to develop, deploy, and troubleshoot applications | L2 | partial | Code services and X-Ray exist without one clear lifecycle comparison. | Add build/pipeline/tracing selection. | P1 |
| CPP-3.8-S5 | Skill | Identify services presenting VM output to end-user devices | L2 | missing | End-user computing services are absent. | Add AppStream and WorkSpaces scenarios. | P0 |
| CPP-3.8-S6 | Skill | Identify services for frontend and mobile creation/deployment | L2 | complete | Amplify and AppSync roles are present. | Add comparison link. | P2 |
| CPP-3.8-S7 | Skill | Identify services that manage IoT devices | L2 | partial | IoT Core purpose is present but not sufficiently contrasted with out-of-scope Greengrass. | Add distinction and explained answer. | P1 |

## Domain 4: Billing, Pricing, and Support

### Task 4.1: Compare AWS pricing models

Canonical evidence: `12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md`  
Supporting evidence: `12-billing-pricing-and-support/aws-billing-and-cost-management/03-data-transfer-costs.md`, `05-storage/amazon-s3/02-storage-classes.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-4.1-K1 | Knowledge | Compute purchasing options | L2 | complete | On-Demand, Reserved, Spot, Savings Plans, Dedicated, and Capacity Reservations are compared. | Refresh volatile attributes. | P2 |
| CPP-4.1-K2 | Knowledge | Storage options and tiers | L2 | complete | Storage classes and pricing dimensions are explained. | Maintain. | P2 |
| CPP-4.1-S1 | Skill | Choose compute purchasing options | L3 | complete | Decision table and scenarios cover commitment, interruption, tenancy, and capacity. | Maintain. | P2 |
| CPP-4.1-S2 | Skill | Describe Reserved Instance flexibility | L2 | complete | Standard/Convertible and scope/flexibility concepts are described. | Verify periodically. | P2 |
| CPP-4.1-S3 | Skill | Describe Reserved Instance behavior in Organizations | L2 | partial | Discount sharing is referenced but not explained with a stable, sourced organization scenario. | Add a concise checked explanation. | P1 |
| CPP-4.1-S4 | Skill | Understand incoming and outgoing data-transfer costs | L3 | complete | Same-AZ, cross-AZ, cross-Region, ingress, and egress patterns are explained without fixed rates. | Maintain. | P2 |
| CPP-4.1-S5 | Skill | Understand storage pricing options and tiers | L3 | complete | Capacity, request, retrieval, minimum-duration, and transfer drivers are covered. | Add checked date to the storage-class lesson. | P2 |

### Task 4.2: Understand billing, budget, and cost-management resources

Canonical evidence: `15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md`  
Supporting evidence: `12-billing-pricing-and-support/`, `03-identity-governance-and-organizations/aws-organizations/01-overview.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-4.2-K1 | Knowledge | Billing support and information | L2 | complete | Billing console, reports, and support routes are explained. | Maintain. | P2 |
| CPP-4.2-K2 | Knowledge | Pricing information for AWS services | L2 | complete | Pricing pages and Calculator are distinguished. | Maintain. | P2 |
| CPP-4.2-K3 | Knowledge | AWS Organizations | L2 | complete | Multi-account organization and consolidated billing are covered. | Maintain. | P2 |
| CPP-4.2-K4 | Knowledge | Cost allocation tags | L2 | complete | Activation, grouping, and report relationship are explained. | Maintain. | P2 |
| CPP-4.2-S1 | Skill | Choose Budgets or Cost Explorer | L3 | complete | Alerts/limits versus historical analysis/forecasting are clear. | Maintain. | P2 |
| CPP-4.2-S2 | Skill | Use AWS Pricing Calculator appropriately | L3 | complete | Pre-deployment estimate purpose and limitations are explicit. | Maintain. | P2 |
| CPP-4.2-S3 | Skill | Understand consolidated billing and cost allocation | L3 | complete | Organization billing and allocation use are present. | Maintain. | P2 |
| CPP-4.2-S4 | Skill | Relate cost allocation tags to Cost and Usage Reports | L3 | complete | Tag/report relationship is taught in canonical cost materials. | Maintain. | P2 |

### Task 4.3: Identify technical resources and Support options

Canonical evidence: `12-billing-pricing-and-support/aws-support/02-support-plans.md`  
Supporting evidence: `12-billing-pricing-and-support/customer-enablement/`, `12-billing-pricing-and-support/aws-health-dashboard/01-overview.md`, `12-billing-pricing-and-support/aws-trusted-advisor/01-overview.md`

| ID | Type | Official requirement (concise paraphrase) | Depth | Status | Evidence and exact weakness | Action | Priority |
|---|---|---|---|---|---|---|---|
| CPP-4.3-K1 | Knowledge | Official AWS website resources and documentation | L2 | complete | Guidance, documentation, whitepapers, Knowledge Center, and re:Post purposes are described. | Improve one learner-facing resource index. | P2 |
| CPP-4.3-K2 | Knowledge | AWS Support plans | L3 | complete | Current plan names, fit, channels, and response-context cautions are sourced and dated. | Reverify on a schedule. | P1 |
| CPP-4.3-K3 | Knowledge | AWS Partner Network roles, including ISVs and system integrators | L2 | complete | Partner lesson defines roles and customer value. | Maintain. | P2 |
| CPP-4.3-K4 | Knowledge | AWS Support Center | L2 | partial | Support Center is mentioned but lacks a focused definition and access/use distinction. | Add to support-resource comparison. | P1 |
| CPP-4.3-S1 | Skill | Locate official AWS whitepapers, blogs, and documentation | L2 | complete | Resource purposes and official-source policy are clear. | Add learner path links. | P2 |
| CPP-4.3-S2 | Skill | Identify Prescriptive Guidance, Knowledge Center, and re:Post | L3 | complete | Separate lessons and support comparison distinguish them. | Consolidate cross-links. | P2 |
| CPP-4.3-S3 | Skill | Select customer service, community, Developer, Business, Enterprise On-Ramp, or Enterprise Support | L3 | complete | Support-plan selection is scenario-ready and dated. | Maintain. | P1 |
| CPP-4.3-S4 | Skill | Use Trusted Advisor, Health Dashboard, and Health API for environment management | L3 | partial | Trusted Advisor and dashboard are covered; Health API purpose and access context are thin. | Add one three-way comparison. | P1 |
| CPP-4.3-S5 | Skill | Use Trust and Safety to report abuse | L1 | complete | Dedicated lesson defines the reporting purpose. | Add official references during style batch. | P2 |
| CPP-4.3-S6 | Skill | Understand AWS Partners, Marketplace, ISVs, and system integrators | L2 | complete | Partner roles and Marketplace relationship are described. | Maintain. | P2 |
| CPP-4.3-S7 | Skill | Identify benefits of being an AWS Partner | L1 | complete | Training, certification, events, and business benefits are covered. | Avoid volatile benefit guarantees. | P2 |
| CPP-4.3-S8 | Skill | Identify Marketplace cost, governance, and entitlement capabilities | L2 | missing | No canonical Marketplace lesson teaches these capabilities. | Create a Marketplace recognition lesson. | P0 |
| CPP-4.3-S9 | Skill | Identify Professional Services and Solutions Architects as assistance options | L2 | complete | Professional Services and guidance resources are distinguished. | Add explicit Solutions Architect wording. | P2 |

## Totals

| Domain | Criteria | Complete | Partial | Mention-only | Missing | Wrong-depth | Duplicate-evidence | Potentially outdated |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1. Cloud Concepts | 18 | 13 | 4 | 1 | 0 | 0 | 0 | 0 |
| 2. Security and Compliance | 31 | 23 | 7 | 0 | 1 | 0 | 0 | 0 |
| 3. Cloud Technology and Services | 57 | 44 | 10 | 1 | 2 | 0 | 0 | 0 |
| 4. Billing, Pricing, and Support | 28 | 24 | 3 | 0 | 1 | 0 | 0 | 0 |
| **Repository** | **134** | **104** | **24** | **2** | **4** | **0** | **0** | **0** |

The zero counts for `wrong-depth`, `duplicate-evidence`, and `potentially-outdated` do not mean the repository has no such file-level risks. They mean no atomic official requirement received one of those statuses after its best current canonical evidence was assessed. File-level duplication, excessive depth, and freshness candidates are recorded in the canonical map, backlog, and phase report.

## Classification Boundary

The official service list is broader than the 134 task-statement criteria. A service can be represented at Level 1 without changing a task criterion from partial to complete. Conversely, a polished service lesson does not complete a skill unless the learner can make the required distinction. See the [canonical content map](CPP-CANONICAL-CONTENT-MAP.md) for service ownership and planned destinations.
