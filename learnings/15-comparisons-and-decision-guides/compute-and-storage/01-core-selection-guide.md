# Core Compute and Storage Selection Guide

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Use this guide after learning the canonical services. It compares decision dimensions without duplicating their full explanations.

## Compute Decision Table

| Need | EC2 | Lambda | ECS/EKS containers |
|---|---|---|---|
| Unit | Virtual server | Event-driven function | Containerized task, service, or pod |
| Control | Highest OS and runtime control | Function code and configuration | Image and workload control; host control depends on EC2/Fargate |
| Scaling | Customer configures capacity and Auto Scaling | Automatic concurrency within configured limits | Service/workload scaling plus capacity scaling when on EC2 |
| Availability | Design instances across AZs | Regional managed service; design retries and downstream resilience | Spread replicas across AZs and replace failed workloads |
| Operations | Patch OS and applications | Patch code/dependencies; AWS manages hosts | Orchestrator plus image operations; EC2 nodes add host work |
| Cost concept | Running instance, purchase model, storage, transfer | Requests and execution resources | EC2 fleet or allocated Fargate resources plus supporting services |
| Best signal | Legacy software, long-running process, special host control | Short event-driven processing | Portable packaged services or Kubernetes requirements |

## Storage Decision Table

| Need | S3 | EBS | EFS | Instance store |
|---|---|---|---|---|
| Model | Object | Block | Shared NFS file | Ephemeral block |
| Scope | Regional | Availability Zone | Regional or One Zone class/design | Physical EC2 host |
| Attachment/access | API/HTTP object access | Normally attached to EC2 in its AZ | Multiple Linux clients | Only supported instance host |
| Failure behavior | Designed for durable multi-AZ object storage | Persists independently of instance; snapshots aid recovery | Managed elastic file system | Lost on stop, hibernate, terminate, or host loss |
| Performance fit | Massive object scale and request patterns | Low-latency disks, databases, boot volumes | Shared file namespace | High-performance disposable cache/scratch data |
| Cost concept | Class, capacity, requests, retrieval, transfer | GB, provisioned performance, snapshots | Capacity/class, throughput options, transfer | Included with supported instance; replication is customer work |

## Selection Sequence

1. Identify interface: server, event, container; object, block, or file.
2. Define availability, recovery, latency, throughput/IOPS, and sharing needs.
3. Identify customer-control and operational requirements.
4. Apply security boundaries and data-classification requirements.
5. Compare total cost, including idle capacity, transfer, backups, and operations.

## CPP Recognition

- EC2: virtual servers. Lambda: run code on events. ECS/EKS: orchestrate containers; Fargate supplies serverless container capacity.
- S3: objects. EBS: an EC2 disk. EFS: shared Linux files. Instance store: temporary host-attached data.

## SAA Scenario Patterns

- A variable event stream that performs brief independent transformations: Lambda plus durable event handling.
- A continuously running application requiring custom OS software: EC2, normally behind ELB and across AZs.
- Kubernetes-standard microservices: EKS, with EC2 or Fargate chosen separately.
- Static assets and data-lake objects: S3.
- A database volume attached to one EC2 instance: EBS with snapshots and an application-level availability plan.
- Shared Linux web content across AZs: EFS Regional.
- Rebuildable high-speed scratch data: instance store with replication or regeneration.

## Common Traps

- “Serverless” does not mean no configuration, security, limits, or cost management.
- EBS persistence does not make a single-AZ application highly available.
- Instance store is not a backup location.
- Replication and backup are not synonyms.

## Canonical Lessons

- [Amazon EC2](../../04-compute/amazon-ec2/01-overview.md)
- [AWS Lambda](../../04-compute/aws-lambda/01-overview.md)
- [Containers](../../04-compute/containers/01-ecs-eks-and-fargate.md)
- [Amazon S3](../../05-storage/amazon-s3/01-overview.md)
- [Amazon EBS](../../05-storage/amazon-ebs/01-overview.md)
- [Amazon EFS](../../05-storage/amazon-efs/01-overview.md)
- [EC2 instance store](../../05-storage/ec2-instance-store/01-overview.md)

## Knowledge Check

1. Which storage is appropriate for shared Linux files across AZs? **EFS Regional.**
2. Which compute choice provides operating-system control? **EC2.**
3. Which storage is appropriate only for disposable, recoverable data? **Instance store.**

## References

- [AWS compute decision guide](https://docs.aws.amazon.com/decision-guides/latest/compute-on-aws-how-to-choose/compute-on-aws-how-to-choose.html)
- [AWS storage decision guide](https://docs.aws.amazon.com/decision-guides/latest/storage-on-aws-how-to-choose/storage-on-aws-how-to-choose.html)
- [AWS containers decision guide](https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-to-choose/guide.html)

Official references checked: 2026-07-22.
