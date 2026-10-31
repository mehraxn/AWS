# AWS Shared Responsibility Model

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Cloud security is shared between AWS and the customer. AWS secures the infrastructure that runs AWS services—**security of the cloud**. Customers secure their data, identities, configurations, and workloads—**security in the cloud**.

The dividing line changes with the service. A customer manages more layers on Amazon EC2 than on Amazon RDS, AWS Lambda, or Amazon S3, but using a managed service never removes the customer's security responsibilities.

## Security of the Cloud

AWS is responsible for the facilities and infrastructure that provide AWS services, including:

- Physical data centers and environmental controls
- Physical hosts, storage devices, and networking equipment
- The AWS global network
- The virtualization layer and hypervisor where applicable
- The infrastructure, operating system, and platform layers of abstracted managed services

Customers do not enter AWS data centers, replace failed disks, or patch the EC2 hypervisor.

## Security in the Cloud

Customer responsibilities commonly include:

- Classifying, protecting, backing up, and deleting data appropriately
- Configuring identities, permissions, MFA, and credential rotation
- Choosing Regions and configuring resources to meet residency requirements
- Configuring network controls such as security groups and resource policies
- Enabling and configuring encryption where required
- Securing application code, dependencies, and settings
- Configuring logging, monitoring, retention, and alerting
- Patching guest operating systems on self-managed compute such as EC2

AWS provides secure capabilities; the customer must configure and use them correctly.

## Shared Responsibilities

Some responsibilities depend on context. AWS supplies controls, documentation, and service capabilities, while customers choose and configure them. Examples include patch management, configuration management, awareness and training, and identity management.

For example, AWS patches the managed database engine and underlying host for Amazon RDS according to the service model. The customer still schedules maintenance appropriately, controls database access, protects credentials, and decides whether to encrypt data.

## How Responsibility Changes by Service

| Layer or decision | Amazon EC2 | Amazon RDS | AWS Lambda | Amazon S3 |
|---|---|---|---|---|
| Facilities, hardware, physical network | AWS | AWS | AWS | AWS |
| Hypervisor and managed infrastructure | AWS | AWS | AWS | AWS |
| Guest operating system | Customer | AWS | AWS | AWS |
| Runtime or database engine patching | Customer | AWS manages service layer | AWS | AWS |
| Application code | Customer | Customer | Customer | Customer application code |
| Identity and permissions | Customer | Customer | Customer | Customer |
| Network and public-access configuration | Customer | Customer | Customer | Customer |
| Data classification and protection choices | Customer | Customer | Customer | Customer |
| Availability and backup configuration | Customer designs and configures | Customer selects and configures | Customer designs concurrency, dependencies, and recovery | Customer configures versioning, replication, and lifecycle as needed |

The more control a service gives the customer, the more operational and security work remains with the customer.

## Amazon EC2 Example

AWS secures the facilities, servers, network, and hypervisor. The customer selects and patches the guest operating system, configures security groups, protects access keys, installs and patches application software, encrypts data when required, and designs backup and recovery.

**Exam signal:** a vulnerable package installed inside an EC2 instance is normally the customer's responsibility.

## Amazon RDS Example

AWS operates the host, guest operating system, and managed database software. The customer chooses the database configuration, controls users and network access, protects data, configures encryption and backups, and selects options such as Multi-AZ when the workload requires them.

**Exam signal:** AWS patches the managed platform; the customer does not surrender responsibility for database permissions or data protection.

## AWS Lambda Example

AWS operates the servers, operating system, and language runtime. The customer secures function code and dependencies, grants a least-privilege execution role, protects environment variables and secrets, configures network access, and handles failures and retries in the application design.

**Exam signal:** serverless removes server management, not application-security responsibility.

## Amazon S3 Example

AWS operates the storage infrastructure and service software. The customer controls object data, bucket and access-point policies, public-access settings, encryption choices, lifecycle rules, versioning, and replication.

**Exam signal:** an unintended public bucket policy is a customer configuration issue even though AWS operates Amazon S3.

## CPP Knowledge

For Cloud Practitioner questions, first identify the layer:

- Physical infrastructure, managed hardware, or the hypervisor → AWS
- Customer data, IAM permissions, application settings, or guest OS on EC2 → customer
- Managed service platform → AWS operates more layers, while the customer still controls data and access

The phrase “AWS handles security” is incomplete. The correct answer should distinguish security **of** the cloud from security **in** the cloud.

## SAA Architecture and Design

Service selection changes the operational burden. EC2 offers extensive control but requires OS hardening, patching, capacity management, and recovery design. RDS and Lambda transfer more platform operation to AWS, which can reduce undifferentiated work, but architects must still design identity, network boundaries, data protection, observability, and failure handling.

When evaluating an architecture:

1. Inventory every layer and data flow.
2. Identify which layers AWS operates for the selected services.
3. Assign customer-owned controls to teams and automation.
4. Use preventive controls, such as least-privilege policies and public-access blocks.
5. Use detective controls, such as logs, configuration monitoring, and alerts.
6. Test recovery rather than assuming a managed service automatically meets the workload's recovery objectives.

## Common Exam Scenarios

- A company wants AWS to patch the database operating system: choose a managed database such as Amazon RDS, while recognizing that the company still controls data and access.
- An EC2 instance requires an OS security update: the customer patches it or automates patching.
- A Lambda function reads secrets it does not need: narrow the execution role; AWS does not design the customer's permissions.
- An S3 bucket exposes confidential objects: correct the customer's bucket policy and public-access configuration.
- A requirement says “minimize operational responsibility”: prefer an appropriate managed service, then configure its customer-owned controls.

## Exam Traps

- Managed does not mean responsibility-free.
- AWS does not classify the customer's data or decide who should access it.
- AWS patches the EC2 hypervisor, not the guest operating system.
- Encryption availability does not mean encryption and key access are automatically configured for every requirement.
- Compliance is shared: AWS provides compliant infrastructure and evidence; customers must configure workloads and meet their own obligations.

## Summary

AWS secures the cloud infrastructure. Customers secure what they put in the cloud and how they configure it. The exact boundary changes by service: EC2 leaves more layers with the customer, while RDS, Lambda, and S3 shift platform operation to AWS without removing responsibility for data, identity, configuration, and architecture.

## Knowledge Check

1. Who patches the guest operating system on an Amazon EC2 instance?
2. Why does AWS Lambda not eliminate customer security responsibilities?
3. Which party controls an Amazon S3 bucket policy?
4. What responsibility shifts from the customer to AWS when moving a database from EC2 to Amazon RDS?
5. What should an architect examine after choosing a managed service?

<details>
<summary>Show answers</summary>

1. The customer.
2. The customer still owns code, dependencies, data, permissions, secrets, configuration, and failure handling.
3. The customer.
4. AWS operates and patches more of the infrastructure, operating system, and managed database platform; the customer retains data, access, configuration, and architecture responsibilities.
5. The remaining customer-owned controls, including IAM, network access, encryption, monitoring, backups, and recovery behavior.

</details>

## References

- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [Shared responsibility in the AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/shared-responsibility.html)
- [AWS Certified Cloud Practitioner CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
- [AWS Certified Solutions Architect – Associate SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html)

Sources checked: **2026-07-22**.
