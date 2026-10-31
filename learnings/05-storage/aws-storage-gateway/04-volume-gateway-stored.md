# AWS Volume Gateway (Stored Mode) — README Study Note

## Simple definition

AWS Volume Gateway (Stored Mode) is an AWS Storage Gateway option that gives your on-premises servers block storage volumes over iSCSI, while keeping the main copy of the data locally and backing it up to AWS.

In simple words your data lives on-premises first, and AWS stores backup snapshots of it.

---

## Core idea in plain English

Think of it like this

 Your company already has local storage in its data center.
 Applications need fast, low-latency access to all data.
 But the company also wants offsite backup in AWS.

So AWS Volume Gateway (Stored Mode) lets you

 keep the full primary dataset locally
 present it to servers as iSCSI block volumes
 send asynchronous backups to AWS for protection and recovery

The big idea is

Store locally, back up to AWS.

---

## Main use cases

AWS Volume Gateway (Stored Mode) is mainly used when

 you need low-latency access to the entire dataset
 you want to keep your primary data on-premises
 you want durable offsite backups in AWS
 you want disaster recovery options without replacing your whole storage system
 you have traditional applications that expect block storage

Common examples

 on-premises databases
 business applications running in a local data center
 systems that cannot tolerate slow access to full datasets
 companies that want cloud backup but are not ready to move primary storage fully to AWS

---

## Key features

### 1. Block storage through iSCSI

Your on-premises servers connect to the gateway using iSCSI.

That means AWS presents storage as block-level volumes, similar to traditional storage systems.

### 2. Primary data stays local

In stored mode, the full main copy of the data is kept in your on-premises storage.

This is the most important point.

### 3. Asynchronous backup to AWS

The gateway backs up your local data to AWS asynchronously, so the backups happen in the background instead of making the application wait for every write.

### 4. Snapshot-based protection

You can create point-in-time snapshots of the volumes for backup and recovery.

### 5. Disaster recovery support

If needed, backups can be used for recovery in AWS, including recovery workflows involving Amazon EBS snapshots.

### 6. Works with existing on-premises applications

You usually do not need to rewrite your application. The application still sees block storage through iSCSI.

---

## How it works

Here is the simple flow

1. You deploy AWS Storage Gateway in your on-premises environment.
2. You configure Volume Gateway in stored mode.
3. You map local disks to the gateway.
4. Your application server connects to the volume using iSCSI.
5. The application reads and writes data locally.
6. AWS stores backup snapshots of that data in the cloud.

So the pattern is

Application → iSCSI volume → local storage first → backup snapshots to AWS

This is why stored mode is good for workloads that need fast local access to everything.

---

## Why it is important for the exam

This topic matters because AWS exam questions often test whether you understand

 where the primary data is stored
 file vs block vs tape storage
 local access vs cloud-backed access
 the difference between stored mode and cached mode

For Cloud Practitioner, the exam usually wants you to recognize the business need first.

### Exam mindset

Choose Volume Gateway (Stored Mode) when the question says

 data must remain on-premises as the primary copy
 the company needs low-latency access to the full dataset
 AWS is wanted mainly for backup or disaster recovery

---

## Related AWS services and differences

### AWS Volume Gateway (Stored Mode) vs Volume Gateway (Cached Mode)

This is the most important comparison.

Stored Mode

 primary data = local
 AWS = backupsnapshots
 best when you need low-latency access to all data locally

Cached Mode

 primary data = AWS
 local site = cache of frequently accessed data
 best when you want to reduce on-premises storage needs

### Volume Gateway vs File Gateway

Volume Gateway gives block storage through iSCSI.

File Gateway gives file storage using protocols like NFS or SMB.

If the question says

 mount as a file share → think File Gateway
 present storage as blocksvolumes to servers → think Volume Gateway

### Volume Gateway vs Tape Gateway

Tape Gateway is for backup applications that use virtual tapes.

If the question talks about

 tape replacement
 virtual tape library
 backup software using tapes

then think Tape Gateway, not Volume Gateway.

### Volume Gateway vs Amazon EBS

Amazon EBS is block storage for EC2 instances in AWS.

Volume Gateway is for giving on-premises servers cloud-connected block storage.

### Volume Gateway vs Amazon EFS

Amazon EFS is a managed file system for AWS.

It is not the same as Volume Gateway because EFS is file storage, not iSCSI block storage.

### Volume Gateway vs Amazon S3

Amazon S3 is object storage.

Volume Gateway is not object storage for the application. It presents storage to the application as a block volume.

---

## Common exam traps

### Trap 1 Confusing stored mode with cached mode

This is the biggest trap.

Remember

 Stored mode = data stored locally first
 Cached mode = data stored in AWS first

### Trap 2 Confusing block storage with file storage

If the workload needs iSCSI volumes, it is Volume Gateway.

If it needs NFSSMB file shares, it is File Gateway.

### Trap 3 Thinking AWS stores the active primary data in stored mode

No. In stored mode, the primary live data is on-premises.

AWS mainly provides backup snapshots and recovery options.

### Trap 4 Picking Tape Gateway for all backup questions

Tape Gateway is only correct when the question specifically involves virtual tapes or existing tape-based backup software.

### Trap 5 Mixing up EBS and Volume Gateway

If the server is on-premises, think Volume Gateway.

If the volume is for an EC2 instance, think EBS.

---

## Easy real-world example

A company has a local ERP system running in its own data center.

The ERP system needs very fast access to all its data because employees use it all day. The company does not want the main data to live in the cloud yet, but it does want cloud backup for protection.

Best fit

AWS Volume Gateway (Stored Mode)

Why

 the primary data stays local
 the application gets low-latency access
 AWS provides offsite backup and recovery support

---

## Side note what “stored mode” really means

The name tells you the answer

 Stored mode = stored locally
 Cached mode = stored in AWS, only some data cached locally

That naming trick helps a lot in the exam.

---

## Final summary

AWS Volume Gateway (Stored Mode) is a hybrid storage service for on-premises workloads.

It gives servers iSCSI block volumes, keeps the main data locally, and sends backup snapshots to AWS.

Use it when a company wants

 fast access to the entire dataset on-premises
 cloud-backed disaster recovery
 offsite backup in AWS
 block storage for existing applications

The main exam idea is simple

Stored Mode = local primary data + AWS backup

---

## Short exam answer

AWS Volume Gateway (Stored Mode) provides iSCSI block storage to on-premises applications, keeps the primary data stored locally, and asynchronously backs it up to AWS for durable offsite backup and disaster recovery.

---

## Memory trick

### Memory trick

Stored = stored on-site

That is not the official wording, but it is a very helpful exam memory trick.

 Stored mode → store primary data on-site
 Cached mode → cloud is primary, local is cache

---

## One-line exam coach rule

If the question says “keep the main data on-premises, but back it up to AWS”, choose AWS Volume Gateway (Stored Mode).

---

## Extra exam tip

When you see these words together, Volume Gateway (Stored Mode) should come to mind

 on-premises
 iSCSI
 block storage
 low latency to full dataset
 backup to AWS
 disaster recovery

Those clues usually point to the correct answer.
