# Volume Gateway cached mode

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

## Simple definition

Volume Gateway (cached) is an AWS Storage Gateway option that gives your on-premises servers block storage volumes through iSCSI (Internet Small Computer Systems Interface), while storing the main data in AWS.

It keeps frequently accessed data locally as a cache, so applications can still get fast access to commonly used data.

---

## Core idea in plain English

Think of it like this

 Your company uses servers in its own building
 Those servers need block storage
 But you do not want to keep buying lots of local storage hardware
 So AWS lets you keep the full dataset in Amazon S3
 Only the most-used data stays on-premises for quick access

So the main idea is

Store most data in AWS, keep hot data locally, and save on local storage costs.

---

## Main use cases

Volume Gateway (cached) is useful when

 You want to extend on-premises storage into AWS
 You need block storage for on-premises applications
 Your dataset is large and growing
 You want to reduce the amount of physical storage hardware on site
 You still need low-latency access to frequently used data
 You want backup and recovery options in AWS

---

## Key features

### 1. Block storage for on-premises servers

It presents volumes as iSCSI block storage.

This means your on-premises applications can use it like a normal block storage volume.

### 2. Primary data stored in AWS

The main copy of the data is stored in Amazon S3.

This helps reduce local storage needs.

### 3. Local cache for frequently accessed data

Recently or often used data is kept locally for faster access.

### 4. Cloud-backed scalability

Because the main data is stored in AWS, you can handle large datasets without constantly expanding local disks.

### 5. Snapshot support

You can create point-in-time snapshots for protection and recovery.

These snapshots are stored in AWS and can help with restore and disaster recovery.

### 6. Hybrid storage

It connects on-premises environments with AWS cloud storage.

---

## How it works

Here is the simple flow

1. You deploy a Storage Gateway Volume Gateway in your data center or environment.
2. Your on-premises servers connect to it using iSCSI.
3. Applications read and write data as if they are using local block storage.
4. The gateway stores the full dataset in Amazon S3.
5. Frequently accessed data is kept in the local cache.
6. You can also create snapshots in AWS for backup and recovery.

### Easy mental model

 On-prem app sees a block storage volume
 Local site keeps cached hot data
 AWS keeps the full main data

---

## Why it is important for the exam

This topic matters because AWS exams often test whether you understand

 hybrid storage
 block vs file vs tape storage
 where the primary data lives
 when to use local cache vs full local storage

For the exam, the big point is this

 In cached Volume Gateway, the primary data is in AWS, and only frequently accessed data is stored locally.

That is the key fact to remember.

---

## Related AWS services and differences

### Volume Gateway (cached) vs Volume Gateway (stored)

#### Cached

 Primary data is stored in AWS
 Frequently used data is cached locally
 Best when you want to minimize on-premises storage

#### Stored

 Primary data is stored locally
 AWS stores asynchronous backups
 Best when you need the full dataset on-premises with low-latency access

### Volume Gateway vs File Gateway

#### Volume Gateway

 Provides block storage
 Uses iSCSI
 Good for applications that need volumes

#### File Gateway

 Provides file-based access
 Uses NFS or SMB
 Good for shared file access to data in S3

### Volume Gateway vs Tape Gateway

#### Volume Gateway

 Used for block storage workloads

#### Tape Gateway

 Used for backup applications that normally use tapes
 Replaces physical tape infrastructure with virtual tapes in AWS

### Volume Gateway vs Amazon EBS

#### Volume Gateway

 For hybrid storage between on-premises and AWS
 Used by on-premises applications through a gateway

#### Amazon EBS

 Block storage for Amazon EC2 instances in AWS
 Not designed as on-premises gateway storage

### Volume Gateway vs Amazon S3 directly

#### Volume Gateway

 Lets traditional on-premises apps use block storage

#### Amazon S3 directly

 Object storage accessed through APIs, SDKs, or services
 Not presented as iSCSI block volumes

---

## Common exam traps

### Trap 1 Confusing cached with stored

This is the most common trap.

 Cached = main data in AWS, hot data local
 Stored = main data local, backup in AWS

### Trap 2 Mixing up block and file storage

If the question says

 iSCSI or block storage → think Volume Gateway
 NFSSMB or file share → think File Gateway

### Trap 3 Thinking it is only backup

Cached Volume Gateway is not just backup.
It provides active block storage for applications.

### Trap 4 Choosing EBS for on-premises block storage

EBS is for EC2 in AWS, not for giving on-premises servers cloud-backed block storage.

---

## Easy real-world example

A hospital has on-premises imaging systems that generate a lot of data.

The hospital wants

 fast access to recently used scans
 less local storage hardware
 cloud-backed storage growth

A cached Volume Gateway is a good fit because

 recent scans can stay in the local cache
 the main dataset is stored in AWS
 the hospital does not need to keep expanding local storage arrays

---

## Final summary

Volume Gateway (cached) is a hybrid block storage service in AWS Storage Gateway.

It gives on-premises applications iSCSI block volumes, stores the main data in Amazon S3, and keeps frequently accessed data locally for faster access.

It is best when you want to

 reduce on-premises storage
 keep large datasets in AWS
 still provide fast access to hot data
 connect traditional on-premises applications to cloud-backed storage

---

## Short exam answer

Volume Gateway (cached) provides iSCSI block storage to on-premises applications, stores the primary data in AWS, and keeps frequently accessed data locally for low-latency access.

---

## Memory trick

Cached = Cloud copy is primary.

A simple memory trick

 Cached → Cloud first, cache local
 Stored → Stored local, backup cloud

Another quick exam memory line

Cached = hot data here, full data in AWS.

## Additional Distinct Source Material

## 🧪 Why It's Important for the Exam

The AWS CCP exam tests whether you can identify the right storage solution for a hybrid cloud scenario. You need to know

- When to use Volume Gateway vs. other gateways
- The difference between Cached Mode vs. Stored Mode
- That it solves the problem of extending on-premises storage to the cloud
- It is part of the AWS Storage Gateway service (not a standalone service)

 ⚠️ Exam Tip If the question says on-premises applications need to access cloud storage as a local disk — think Volume Gateway.

---

## 🔗 Related AWS Services & Differences

### AWS Storage Gateway Family

 Gateway Type  What It Does  Primary Storage
---------
 Volume Gateway (Cached)  On-prem apps use S3 as primary storage, cache locally  ☁️ Amazon S3
 Volume Gateway (Stored)  Full data stored on-premises, async backup to S3  🏠 On-premises
 File Gateway  NFSSMB access to S3 (file-based, not block storage)  ☁️ Amazon S3
 Tape Gateway  Virtual tape library backed by S3Glacier  ☁️ S3  Glacier

### Volume Gateway vs. AWS Direct Connect

 Feature  Volume Gateway  AWS Direct Connect
---------
 Purpose  Hybrid storage  Dedicated network connection
 Data Type  Block storage  Any AWS service
 Use Case  Store data in cloud  Low-latency private connectivity

### Volume Gateway vs. Amazon EFS

 Feature  Volume Gateway  Amazon EFS
---------
 Access  On-premises via iSCSI  Cloud-native via NFS
 Use Case  Hybridlegacy apps  Cloud-native apps

---
