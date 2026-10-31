# Amazon EBS

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

## Simple AWS exam explanation

**Amazon EBS** is a **block storage service** in AWS.

The easiest way to remember it is this:

* **Amazon EC2** = the virtual server
* **Amazon EBS** = the virtual hard disk attached to that server

So when you launch an EC2 instance, the operating system, applications, and files can be stored on an **EBS volume**.

---

## 1) What EBS really is

Amazon EBS provides **persistent block storage** for EC2 instances.

Let’s break that down:

### Persistent

This means the data **stays there even if the EC2 instance stops**.

That is very important for the exam.

* If an EC2 instance is **stopped**, EBS data normally remains.
* If an EC2 instance is **restarted**, EBS data remains.
* If an EC2 instance is **terminated**, the EBS volume may be deleted or kept depending on the settings.

### Block storage

Block storage means the storage is presented to the operating system like a **raw disk drive**.

The OS can then:

* create a file system on it
* format it
* mount it
* use it like a normal disk

This is different from:

* **object storage** like Amazon S3
* **file storage** like Amazon EFS

---

## 2) The main idea for the exam

Think of EBS as:

**durable storage for one EC2 instance at a time**

That sentence helps a lot in AWS questions.

### Why?

Because EBS is designed mainly to be attached to **a single EC2 instance** in the same Availability Zone.

So if the question is about:

* a boot disk for EC2
* a database disk for one server
* persistent storage for a virtual machine

then **EBS is often the correct answer**.

---

## 3) Where EBS is used

Amazon EBS is commonly used for:

### Boot volumes

The root volume of an EC2 instance is often an EBS volume.

That means:

* the operating system can be stored on EBS
* the instance can boot from EBS

### Application storage

Applications running on EC2 can store files and data on EBS.

### Databases

Databases need storage with good performance and low latency.
EBS is commonly used for databases running on EC2.

### Long-term persistent data for one server

If a server needs data to survive stop/start, EBS is a strong choice.

---

## 4) EBS vs instance store

This is a very common exam comparison.

### EBS

* persistent
* data survives stop/start
* network-attached storage for EC2
* can be snapshotted
* good for important data

### Instance store

* temporary storage
* data is lost if the instance stops, terminates, or underlying host changes
* physically attached to the host machine
* good for buffers, caches, temporary files, scratch data

### Exam shortcut

* Need **persistent** storage? → **EBS**
* Need **temporary** very short-lived storage? → **Instance store**

---

## 5) EBS vs S3 vs EFS

Another popular exam area.

### EBS

* block storage
* attached to EC2
* usually one instance at a time
* great for boot volumes and databases

### S3

* object storage
* accessed through APIs, not mounted like a normal block disk by default
* ideal for backups, files, media, logs, static website assets

### EFS

* file storage
* shared file system
* multiple EC2 instances can access it at the same time
* ideal when many servers need the same files

### Exam shortcut

* One server needs a disk → **EBS**
* Shared file system for many servers → **EFS**
* Store objects/files at massive scale → **S3**

---

## 6) Important characteristics of EBS

## a) EBS is tied to an Availability Zone

An EBS volume is created in **one Availability Zone (AZ)**.

That means:

* the volume and the EC2 instance must be in the **same AZ** to attach directly
* you cannot directly attach an EBS volume from one AZ to an instance in another AZ

This is very testable.

---

## b) EBS is replicated within its Availability Zone

EBS is designed to be highly available and durable **within the same AZ**.

So AWS protects the volume inside that AZ.

But remember:

* EBS is **not automatically a cross-region service**
* EBS is **not automatically multi-AZ storage**

If you want backup or copy outside the AZ, snapshots are important.

---

## c) EBS supports snapshots

A snapshot is a **backup of an EBS volume** stored in Amazon S3.

Snapshots are very important in the exam.

You can use them to:

* back up a volume
* restore a volume
* create a new volume
* copy data to another AZ or another Region

### Key exam point

**Snapshots are incremental**.
This means after the first full snapshot, later snapshots save only the changed blocks.

---

## d) EBS volumes can be resized

You can modify many EBS volumes without rebuilding everything.

For example, you can often change:

* size
* performance characteristics
* volume type

This gives flexibility when your workload grows.

---

## e) Encryption is supported

EBS supports encryption for data:

* at rest
* in transit between EC2 and EBS (in supported scenarios)
* in snapshots

For the exam, remember this simple idea:

**If security of stored disk data is required, EBS encryption is a common answer.**

---

## 7) Volume types you should know

AWS offers different EBS volume types. For the exam, focus on the idea that some are for **general use**, some for **high performance**, and some for **throughput-heavy HDD workloads**.

## a) SSD-based volumes

These are best when you need fast access and low latency.

### General Purpose SSD

Usually the default choice for many workloads.
Good balance of:

* price
* performance
* flexibility

Use cases:

* boot volumes
* small and medium databases
* development environments
* general application servers

### Provisioned IOPS SSD

Used when you need very high performance and predictable IOPS.

Use cases:

* critical databases
* I/O-intensive applications
* workloads that need consistent performance

---

## b) HDD-based volumes

These are more focused on throughput than low-latency random I/O.

### Throughput Optimized HDD

Good for large sequential workloads.

Use cases:

* big data
* log processing
* streaming workloads

### Cold HDD

Lower-cost option for less frequently accessed data.

Use cases:

* infrequently accessed large datasets
* lower-cost throughput workloads

---

## 8) What EBS is best for

EBS is best when you need:

* a disk for an EC2 instance
* persistent storage
* a boot volume
* low-latency storage for one server
* database storage on EC2
* snapshots and restore capability

---

## 9) What EBS is NOT best for

EBS is usually **not** the best answer when you need:

### Shared storage for many EC2 instances at once

That usually points more to **Amazon EFS**.

### Internet-scale object storage

That usually points to **Amazon S3**.

### Storage that disappears with the instance and is okay to lose

That may point to **instance store**.

### A managed database service

If the question is really asking for the database service itself, that may point to **Amazon RDS**, not EBS.

---

## 10) Common AWS exam traps

## Trap 1: “Persistent storage” vs “temporary storage”

* Persistent → EBS
* Temporary → Instance store

## Trap 2: “Shared by many instances”

* Shared file system → EFS
* Single server disk → EBS

## Trap 3: “Backup of EBS”

* Backup mechanism → Snapshot

## Trap 4: “Across Regions”

EBS volume itself is not a global storage service.
To move or copy, snapshots are commonly used.

## Trap 5: “Boot volume for EC2”

This often points directly to **EBS**.

---

## 11) Easy real-world example

Imagine you launch an EC2 virtual machine for a web application.

You may use:

* one EBS volume for the operating system
* another EBS volume for the application data
* snapshots to back them up

If the server stops and starts again, the data on EBS is still there.

That is why EBS is very useful.

---

## 12) Simple memory trick

Remember this line:

**EBS = Elastic Block Store = EC2 disk**

And another one:

**EBS is to EC2 like a hard drive is to a computer.**

These memory tricks work very well in the AWS exam.

---

## 13) Mini comparison table

| Service        | Storage type            | Main use                                  |
| -------------- | ----------------------- | ----------------------------------------- |
| Amazon EBS     | Block storage           | Disk for one EC2 instance                 |
| Amazon EFS     | File storage            | Shared file system for many EC2 instances |
| Amazon S3      | Object storage          | Scalable object/file storage              |
| Instance store | Temporary block storage | Scratch, cache, buffer                    |

---

## 14) Exam-style summary

If the exam says:

* “persistent block storage for EC2” → **Amazon EBS**
* “boot volume for EC2” → **Amazon EBS**
* “database disk attached to EC2” → **Amazon EBS**
* “backup of an EBS volume” → **snapshot**
* “shared file storage for multiple instances” → **Amazon EFS**
* “temporary storage that can be lost” → **instance store**

---

## 15) Final one-paragraph answer

**Amazon Elastic Block Store (Amazon EBS)** is an AWS service that provides **persistent block storage for Amazon EC2 instances**. It acts like a **virtual hard drive** for a server in the cloud. EBS is commonly used for **boot volumes, application data, and databases**, and it supports **snapshots, resizing, and encryption**. It is usually attached to **one EC2 instance at a time** in the **same Availability Zone**, which makes it a very common answer in AWS exam questions about **persistent disk storage for EC2**.

---

## 16) Super short exam answer

**Amazon EBS is persistent block storage for EC2, like a hard disk attached to a virtual server.**

## Additional Distinct Source Material

## Simple definition

Amazon EBS (Elastic Block Store) is block storage for Amazon EC2 instances.
You can think of it like a virtual hard drive for a cloud server.

## Core idea in plain English

If Amazon EC2 is the computer, then Amazon EBS is the disk attached to that computer.
It stores data such as the operating system, applications, databases, and files.

EBS is persistent storage, which means the data stays even if you stop the EC2 instance.

## Main use cases

 Store the operating system for an EC2 instance
 Run databases that need fast, reliable storage
 Store application files and business data
 Use as boot volumes for EC2
 Backup data with snapshots

## Key features

 Block storage for EC2
 Persistent data storage
 Can be attached, detached, and reattached
 Can be used as a boot volume
 Supports snapshots for backup
 Supports encryption
 Different volume types for different performance needs
 Can increase size and modify some settings later

## How it works

1. You launch an EC2 instance.
2. You create or attach an EBS volume.
3. The EC2 instance sees it like a hard drive.
4. You format and mount it if needed.
5. Your apps read and write data to it.
6. You can create EBS snapshots to back it up.

Important exam idea
An EBS volume is attached to an EC2 instance and is used inside the instance like a disk.

## Why it is important for the exam

Amazon EBS appears very often in Cloud Practitioner questions because it helps test whether you understand

 Block storage vs file storage vs object storage
 Which AWS service is used with EC2
 Which storage is persistent
 Which service is best for databases and boot volumes

## Related AWS services and differences

### Amazon EBS vs Amazon S3

 EBS = block storage for one EC2 instance (or specific special cases)
 S3 = object storage for files, backups, static websites, and large-scale storage
 EBS looks like a disk
 S3 looks like a storage service for objects, not a mounted disk by default

### Amazon EBS vs Amazon EFS

 EBS = block storage, usually for one EC2 instance in one Availability Zone
 EFS = shared file storage that multiple EC2 instances can access at the same time
 EBS is great for databases and boot disks
 EFS is great for shared Linux file systems

### Amazon EBS vs Instance Store

 EBS = persistent
 Instance Store = temporary storage tied to the life of the instance
 If the instance fails or is terminated, Instance Store data is lost
 For important data, choose EBS, not Instance Store

### Amazon EBS vs FSx

 EBS = general block storage for EC2
 FSx = managed file systems for special workloads such as Windows, Lustre, NetApp ONTAP, or OpenZFS

## Common exam traps

 Trap 1 Thinking EBS is object storage
  It is not. EBS is block storage.

 Trap 2 Thinking EBS is temporary
  It is persistent storage.

 Trap 3 Confusing EBS with EFS
  EBS = one server-style disk.
  EFS = shared file system.

 Trap 4 Using EBS for static website storage
  Static websites are more commonly associated with S3, not EBS.

 Trap 5 Forgetting EBS is linked to EC2
  If the question says a storage volume acts like a hard drive for an EC2 instance, that points to EBS.

 Trap 6 Mixing up snapshot and volume
  A volume is the actual storage disk.
  A snapshot is a backup copy of that volume.

## Volume types you should know

You do not need every deep detail for Cloud Practitioner, but know the basic idea

 gp3  gp2 = general purpose SSD, common choice
 io1  io2 = high-performance SSD for critical databases
 st1 = throughput-focused HDD
 sc1 = lowest-cost HDD for less frequently accessed data

Exam shortcut

 General use → gp3gp2
 High IOPS database → io1io2

## Easy real-world example

A company runs an application on Amazon EC2.
The EC2 instance needs

 an operating system disk
 storage for the app
 storage for a database

They attach Amazon EBS volumes to the EC2 instance.
Now the instance has cloud hard drives that keep data even if the instance is stopped.

## SAA Performance and Recovery Supplement

EBS is persistent block storage in one Availability Zone. An EC2 instance normally attaches a volume in the same AZ; create a volume from a snapshot in another AZ for recovery. Multi-Attach exists only for supported volume types and clustered applications and does not make an ordinary file system safe for concurrent writers.

| Category | Selection signal |
|---|---|
| General Purpose SSD (gp) | Balanced price and performance for most workloads |
| Provisioned IOPS SSD (io) | Consistent low latency and provisioned IOPS for critical databases |
| Throughput Optimized HDD (st) | Large sequential, throughput-intensive data |
| Cold HDD (sc) | Infrequently accessed sequential data at lower cost |

IOPS measures operations per second; throughput measures bytes per second. Match both plus latency and workload pattern. Snapshots are point-in-time, stored incrementally at the service level, can create new volumes, and can be copied across Regions/accounts where supported. Encryption protects volume data, snapshots, and data moving between supported instances and EBS. Data Lifecycle Manager automates snapshot/AMI policies; Fast Snapshot Restore addresses initialization latency where justified.

Customers manage IAM, KMS access, OS file systems, backups, and data classification. Cost reflects provisioned capacity/performance, snapshot storage, transfer/copies, and optional features.

### Knowledge Check

1. Can an EBS volume normally attach across AZs? **No.**
2. What measures bytes per second? **Throughput.**
3. How can a snapshot restore into another AZ? **Create a new volume there.**

## Official References

- [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html)
- [EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)
- [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html)

Official references checked: 2026-07-22.

## Final summary

Amazon EBS is persistent block storage for Amazon EC2.
It behaves like a virtual hard disk.
It is commonly used for

 boot volumes
 databases
 application storage
 backups through snapshots

If the exam question talks about a disk attached to an EC2 instance, the answer is usually Amazon EBS.

## Short exam answer

Amazon EBS is persistent block storage for EC2 instances. It acts like a virtual hard drive and is commonly used for boot volumes, databases, and application data.
