# Cloud Fundamentals Review

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Use this review after completing the Cloud Fundamentals lessons. It tests concept recognition, comparisons, and scenario reasoning rather than memorizing isolated definitions.

## Review Checklist

You should be able to explain:

- cloud computing and its value proposition;
- agility, elasticity, scalability, availability, and fault tolerance;
- the six common advantages of cloud computing;
- IaaS, PaaS, SaaS, and public, private, and hybrid deployment models;
- security of the cloud versus security in the cloud;
- the six Well-Architected pillars;
- the six AWS CAF perspectives and four transformation outcomes;
- assess, mobilize, and migrate and modernize;
- the 7 Rs of migration;
- discovery, database migration, online transfer, offline transfer, and migration tracking services;
- fixed and variable costs, rightsizing, automation, economies of scale, BYOL, and license included.

## Fast Comparison Tables

### Core cloud concepts

| Concept | Meaning | Example |
|---|---|---|
| Agility | Provision and change quickly | Create a development environment in minutes |
| Scalability | Increase capacity to handle growth | Add application servers or use a larger database |
| Elasticity | Add and remove capacity as demand changes | Scale out for a sale and scale in afterward |
| High availability | Minimize interruption | Run across multiple Availability Zones |
| Fault tolerance | Continue operating through failure | Redundant active components tolerate a failure without service loss |
| Global reach | Deploy closer to users worldwide | Select Regions and global delivery services based on requirements |

### Responsibility boundary

| Area | Typical owner |
|---|---|
| Data centers, physical hardware, and AWS global infrastructure | AWS |
| EC2 guest operating system and installed software | Customer |
| Customer data classification and access decisions | Customer |
| Managed-service platform operation | AWS, according to the service model |
| IAM permissions and resource configuration | Customer |

### Well-Architected pillars

| Pillar | Memory question |
|---|---|
| Operational Excellence | Can we run and improve it effectively? |
| Security | Is access and data protected? |
| Reliability | Can it recover and handle change? |
| Performance Efficiency | Are resources suitable and efficient? |
| Cost Optimization | Are we avoiding unnecessary spending? |
| Sustainability | Are we minimizing resource impact per useful outcome? |

### AWS CAF perspectives

| Perspective | Main concern |
|---|---|
| Business | Strategy and business outcomes |
| People | Skills, culture, leadership, and change |
| Governance | Policies, risk, finance, and decision rights |
| Platform | Technical cloud foundation and delivery environment |
| Security | Protection, detection, and compliance controls |
| Operations | Monitoring, support, service delivery, and recovery |

### Migration strategies

| Strategy | Fast definition |
|---|---|
| Rehost | Move with minimal change |
| Relocate | Move the platform or workload without changing the overall architecture |
| Replatform | Make limited platform optimizations |
| Refactor | Redesign for cloud-native benefits |
| Repurchase | Replace with another product, often SaaS |
| Retain | Keep where it is for now |
| Retire | Decommission it |

### Migration service recognition

| Need | Service or approach |
|---|---|
| Discover servers and dependencies | Application Discovery Service |
| Rehost supported servers | Application Migration Service |
| Migrate and replicate database data | AWS DMS |
| Convert database schemas for an engine change | Schema-conversion tooling |
| Transfer files online | DataSync |
| Transfer huge data sets offline | Snowball device |
| Track migration progress | Migration Hub |
| Run AWS infrastructure on premises | Outposts |

## Practice Questions

### Question 1

A company purchases enough servers for its annual sales peak. The servers are mostly idle during the rest of the year. Which cloud benefit most directly addresses the problem?

- A. Global reach
- B. Elastic capacity and reduced need to guess peak capacity
- C. Dedicated tenancy
- D. Fault tolerance

<details>
<summary>Answer</summary>

**B.** Elastic capacity allows the company to add and remove resources with demand rather than permanently purchasing peak capacity.

</details>

### Question 2

A team creates a complete test environment in minutes, runs an experiment, and deletes the environment. Which benefit is most directly demonstrated?

- A. Agility
- B. Fault tolerance
- C. Data sovereignty
- D. Reserved capacity

<details>
<summary>Answer</summary>

**A.** Rapid provisioning and experimentation demonstrate agility.

</details>

### Question 3

Who is responsible for patching the guest operating system of an Amazon EC2 instance?

- A. AWS
- B. The customer
- C. The hardware vendor
- D. The AWS Support team

<details>
<summary>Answer</summary>

**B.** AWS operates the physical infrastructure and hypervisor; the customer manages the EC2 guest operating system.

</details>

### Question 4

Which Well-Architected pillar most directly addresses automatic recovery from component failure?

- A. Cost Optimization
- B. Reliability
- C. Sustainability
- D. Performance Efficiency

<details>
<summary>Answer</summary>

**B.** Reliability focuses on performing the intended function, handling change, and recovering from failure.

</details>

### Question 5

Which AWS CAF perspective focuses most directly on employee skills, culture, and organizational change?

- A. Platform
- B. Governance
- C. People
- D. Operations

<details>
<summary>Answer</summary>

**C.** The People perspective addresses culture, skills, leadership, workforce, and change readiness.

</details>

### Question 6

A company wants to move a database to a managed AWS database service with limited application changes. Which migration strategy is the best match?

- A. Retire
- B. Replatform
- C. Retain
- D. Repurchase

<details>
<summary>Answer</summary>

**B.** Replatform introduces limited optimization, such as moving from a self-managed database to a managed service, without a full redesign.

</details>

### Question 7

A company has a very large file archive and insufficient network bandwidth to meet its migration deadline. Which option is the best starting point?

- A. AWS Migration Hub
- B. AWS Snowball device
- C. AWS CloudFormation
- D. AWS License Manager

<details>
<summary>Answer</summary>

**B.** Snowball supports offline transfer when sending the data over the network is impractical.

</details>

### Question 8

A database must remain active while its data is copied to a target database. The company wants ongoing change replication to reduce cutover downtime. Which service is most relevant?

- A. AWS DMS
- B. AWS Outposts
- C. AWS Artifact
- D. Amazon Route 53

<details>
<summary>Answer</summary>

**A.** AWS DMS can support initial data migration and ongoing replication for supported sources and targets.

</details>

### Question 9

A company wants to use existing eligible software licenses on AWS. Which licensing model describes this?

- A. License included
- B. Bring Your Own License
- C. On-Demand Instances
- D. Consolidated billing

<details>
<summary>Answer</summary>

**B.** BYOL means using eligible customer-owned licenses, subject to vendor terms.

</details>

### Question 10

Which statement about AWS License Manager is correct?

- A. It grants legal permission to move any license to AWS.
- B. It automatically rewrites vendor license agreements.
- C. It helps track and govern supported software-license usage.
- D. It is a database migration service.

<details>
<summary>Answer</summary>

**C.** License Manager helps track and manage license usage. Vendor agreements determine legal eligibility.

</details>

### Question 11

A team wants to reduce manual environment creation and make deployments repeatable and reversible. Which combination best fits?

- A. Infrastructure as code and automation
- B. One large manually configured server
- C. Offline data transfer
- D. Dedicated physical media

<details>
<summary>Answer</summary>

**A.** Automation and infrastructure as code improve repeatability, reviewability, and rollback.

</details>

### Question 12

Which statement correctly compares AWS CAF and the AWS Well-Architected Framework?

- A. Both are data-transfer services.
- B. AWS CAF focuses on organizational transformation; Well-Architected focuses on workload quality.
- C. AWS CAF performs audits; Well-Architected provides software licenses.
- D. They are two names for the same service.

<details>
<summary>Answer</summary>

**B.** AWS CAF addresses organizational readiness and transformation capabilities; Well-Architected evaluates architecture decisions and workload risks.

</details>

## Scenario Drill

Read the scenario and identify the most important concept before thinking about a service.

### Scenario A

A startup needs to release features quickly, has unpredictable traffic, and has a small operations team.

**Reasoning:**

- rapid release → agility and operational excellence;
- unpredictable traffic → elasticity;
- small operations team → managed services and automation;
- architecture still needs security, observability, and failure handling.

### Scenario B

An enterprise must leave a data center in six months. It has hundreds of applications, incomplete dependency records, and several licensed databases.

**Reasoning:**

- begin with assessment and discovery;
- classify applications with the 7 Rs;
- create migration waves from dependencies and criticality;
- evaluate database replication and schema compatibility;
- verify BYOL or license-included options;
- prepare platform, security, governance, and operations during mobilization.

### Scenario C

An application is available only in one Availability Zone. The business requires continued service during an AZ failure.

**Reasoning:**

- primary concern → Reliability pillar;
- architecture must use multiple AZs across the full request and data path;
- health detection, traffic routing, state, database behavior, and recovery must all be considered;
- merely “running on AWS” does not meet the requirement.

## Final Self-Test

You are ready to continue when you can answer these without notes:

1. What exact problem does elasticity solve?
2. Why is a managed service not responsibility-free?
3. Can you name and distinguish the six Well-Architected pillars?
4. Can you name the six AWS CAF perspectives?
5. Can you distinguish rehost, replatform, and refactor?
6. Can you choose between DMS, DataSync, Snowball, Discovery Service, and Migration Hub?
7. Can you explain BYOL versus license included?
8. Can you explain why cloud cost optimization is more than choosing the lowest price?

## Next Steps

Continue with:

1. [Global Infrastructure](../02-global-infrastructure/README.md)
2. [Identity, Governance, and Organizations](../03-identity-governance-and-organizations/README.md)
3. [Compute](../04-compute/README.md)
4. [Billing, Pricing, and Support](../12-billing-pricing-and-support/README.md)
5. [Architecture and Design Patterns](../13-architecture-and-design-patterns/README.md)
6. [Exam Preparation](../16-exam-preparation/README.md)

## References

- [CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
- [CLF-C02 Domain 1: Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html)
- [CLF-C02 Domain 2: Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html)
- [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html)

Sources checked: **2026-08-01**.
