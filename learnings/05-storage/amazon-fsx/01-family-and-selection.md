# Amazon FSx Family and Selection

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Amazon FSx provides managed file systems based on established file-system technologies. Choose a family from protocol, application compatibility, performance, availability, and migration needs—not merely because the workload needs “files.”

## Family Selection

| Family | Interfaces and strengths | Typical selection |
|---|---|---|
| FSx for Windows File Server | SMB, Windows ACLs, Microsoft Active Directory integration | Windows shares, home directories, and Windows applications; Multi-AZ options support resilient designs |
| FSx for Lustre | Parallel file system, high throughput, optional S3 data-repository integration | HPC, machine learning, media processing, and burst processing; scratch and persistent deployment choices have different durability goals |
| FSx for NetApp ONTAP | NFS, SMB, and iSCSI awareness; snapshots, cloning, and storage efficiency | Enterprise NAS migration and multiprotocol NetApp workloads |
| FSx for OpenZFS | NFS and OpenZFS data-management capabilities | Linux workloads that need OpenZFS compatibility, snapshots, or cloning |

## Availability, Performance, and Integration

Deployment types and supported features differ by family. Multi-AZ is valuable when the selected family and mode support automatic failover; a Single-AZ deployment can suit scratch or recoverable data. Select throughput capacity, storage type, and other performance settings from workload measurements. FSx for Lustre can process data associated with S3, but it is a file system rather than an S3 replacement.

## Security and Shared Responsibility

AWS manages file-server infrastructure. Customers manage identities and permissions, network reachability, security groups, directory integration, encryption choices, backups, data classification, and client configuration. Use private networking and least privilege.

## Cost Optimization

Cost depends on family, stored capacity, throughput capacity, deployment type, backups, and data transfer. Higher resilience or provisioned performance may cost more but can satisfy recovery and latency requirements. Remove unneeded backups and size from observed demand.

## CPP Knowledge

Recognize FSx as managed file storage for a specific file-system ecosystem: Windows/SMB, Lustre/HPC, NetApp ONTAP, or OpenZFS. EFS is the simpler elastic NFS choice for many Linux applications.

## SAA Architecture and Design

- Use Windows File Server for SMB and Active Directory-dependent applications.
- Use Lustre for parallel, throughput-intensive processing and S3-connected data workflows.
- Use ONTAP when multiprotocol access or NetApp migration features drive the design.
- Match Single-AZ or Multi-AZ choices to failure tolerance and recovery objectives.
- EFS and FSx are shared file services; EBS is AZ-scoped block storage for EC2.

## Common Exam Traps

- FSx is a family, not one universal file system.
- Lustre integration does not turn S3 objects into a general-purpose POSIX replacement without a file-system workflow.
- Managed file servers still require customer permissions, network controls, and backup decisions.

## Practice Questions

1. Which family best matches Windows SMB and Active Directory?
2. Which family is commonly selected for parallel HPC processing?
3. What should drive EFS versus FSx selection?

<details><summary>Answers</summary>

1. FSx for Windows File Server. 2. FSx for Lustre. 3. Required protocol, application compatibility, performance, availability, and operational features.

</details>

## References

- [What is Amazon FSx?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
- [Amazon FSx file-system options](https://aws.amazon.com/fsx/when-to-choose-fsx/)
- [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)
- [FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)

Official references checked: 2026-07-22.
