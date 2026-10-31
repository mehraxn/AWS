# Amazon EFS

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

## Simple definition

Amazon EFS is a fully managed file storage service in AWS.
It gives you a shared file system that many AWS resources can use at the same time.

## Core idea in plain English

Think of Amazon EFS like a shared network folder in the cloud.
Multiple Amazon EC2 instances can connect to it and read or write the same files.
AWS manages the storage infrastructure for you, so you do not need to maintain file servers yourself.

## Main use cases

* Shared storage for multiple EC2 instances
* Web servers that need access to the same files
* Content management systems
* Development and test environments
* Big data and analytics workloads
* Home directories for users
* Lift-and-shift applications that need traditional file storage

## Key features

* **Fully managed**: AWS handles the infrastructure and maintenance
* **Elastic**: Storage grows and shrinks automatically as files are added or removed
* **Shared access**: Many instances can access the same file system at once
* **File storage**: Uses a standard file system structure with folders and files
* **Works with Linux**: Commonly mounted on Linux-based systems using NFS
* **Highly available**: Designed for high durability and availability across multiple Availability Zones
* **Pay for what you use**: No need to provision a fixed storage size in advance

## How it works

1. You create an EFS file system in AWS.
2. AWS creates mount targets in the Availability Zones you choose inside your VPC.
3. Your EC2 instances connect to EFS over the network using NFS.
4. The instances can then read and write files as if they are using a normal shared file system.
5. As more files are stored, EFS automatically expands.
6. If files are deleted, the used storage can decrease as well.

In simple words, EFS is network file storage that many servers can share at the same time.

## Why it is important for the exam

Amazon EFS is important because AWS exams often test whether you can recognize the correct **storage type**.

You should quickly remember this:

* **EFS = shared file storage for Linux workloads**
* **EBS = block storage for one EC2 instance at a time in most basic exam questions**
* **S3 = object storage for files stored as objects, not a mounted file system**

If the question says:

* multiple EC2 instances
* shared access
* file system
* Linux
* automatic scaling

then **Amazon EFS** is usually the best answer.

## Related AWS services and differences

### Amazon EFS vs Amazon EBS

**Amazon EFS**

* File storage
* Shared by multiple instances
* Accessed over the network
* Scales automatically

**Amazon EBS**

* Block storage
* Usually attached to a single EC2 instance
* Acts like a hard drive for that instance
* You choose the size

**Exam tip:**
If the question needs a **shared file system**, choose **EFS**, not EBS.

### Amazon EFS vs Amazon S3

**Amazon EFS**

* File storage
* Mounted as a file system
* Good for applications that expect folders and files

**Amazon S3**

* Object storage
* Stores data as objects in buckets
* Great for backups, static files, logs, and large-scale storage

**Exam tip:**
If the application needs a normal file system that can be mounted, that points to **EFS**, not S3.

### Amazon EFS vs Amazon FSx

**Amazon EFS**

* Simple, elastic shared file storage for Linux workloads
* General-purpose managed file system in AWS

**Amazon FSx**

* Managed file systems for specific use cases, such as Windows File Server, Lustre, NetApp ONTAP, or OpenZFS
* Chosen when you need a specific file system type or special enterprise features

**Exam tip:**
For basic Cloud Practitioner questions, if AWS asks for a general shared Linux file system, the answer is often **EFS**.

## Common exam traps

* **Trap 1: Confusing EFS with EBS**
  EBS is like a disk for one server. EFS is a shared file system for many servers.

* **Trap 2: Confusing EFS with S3**
  S3 is object storage, not a mounted file system.

* **Trap 3: Forgetting the shared access part**
  If many EC2 instances need the same files at the same time, EFS is a strong clue.

* **Trap 4: Ignoring the file storage clue**
  If the question says folders, files, mount, or NFS, think EFS.

* **Trap 5: Missing the elasticity clue**
  EFS grows and shrinks automatically, so you do not pre-allocate storage the same way as EBS.

## Easy real-world example

Imagine a company runs a website on several EC2 instances behind a load balancer.
Each server must access the same uploaded images and documents.

If they store these files separately on each server, the data becomes inconsistent.
One server may have a file that another server does not have.

With Amazon EFS, all EC2 instances connect to the same shared file system.
Now every server sees the same files.
That makes the application easier to manage.

## SAA File-System Design Supplement

EFS is managed elastic NFS storage for Linux clients. A Regional file system stores data across AZs; One Zone storage classes trade AZ resilience for cost. Create mount targets in the AZs where clients run and control NFS traffic with security groups. EC2, containers, and supported on-premises clients can share one namespace through appropriate network connectivity.

General Purpose performance fits most applications; other modes/options address specialized scale and throughput needs. Throughput modes let throughput scale with storage/activity or be configured according to current service options. Lifecycle policies move inactive files into eligible lower-cost classes; first-access latency and access charges may differ. Access points provide application-specific entry and identity settings.

AWS manages infrastructure. Customers manage POSIX permissions, IAM where used, security groups, encryption/KMS permissions, backup, and classification. Cost depends on storage class, access, throughput option, and transfer. EBS is block storage for an AZ; FSx is chosen for specific Windows, Lustre, ONTAP, or OpenZFS compatibility.

### Knowledge Check

1. Which protocol does EFS use? **NFS.**
2. Which design provides multi-AZ data resilience? **EFS Regional.**
3. What enables AZ-local network access? **Mount targets.**

## Official References

- [What is Amazon EFS?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
- [EFS storage classes](https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html)
- [EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
- [Mount targets and security groups](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)

Official references checked: 2026-07-22.

## Final summary

Amazon EFS is AWS shared file storage.
It is fully managed, grows automatically, and can be used by multiple EC2 instances at the same time.

For the exam, remember that EFS is the answer when the question asks for:

* shared access
* file storage
* Linux-based workloads
* automatic scaling

## Short exam answer

**Amazon EFS is a fully managed, elastic file storage service that provides a shared file system for multiple AWS resources, especially EC2 instances.**

## Memory trick

**EFS = Elastic Files Shared**

Use this memory trick:

* **E** = Elastic
* **F** = File system
* **S** = Shared by multiple servers

So when you see **shared file storage that grows automatically**, think **Amazon EFS**.
