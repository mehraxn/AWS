# Tape Gateway

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

## Simple definition

AWS Tape Gateway is a cloud-based virtual tape library (VTL) service. It lets companies keep using their existing backup software, but store backup tapes in AWS instead of using physical tapes.

## Core idea in plain English

Think of Tape Gateway as a fake tape library that looks real to your backup system.

Your backup application thinks it is writing data to normal backup tapes. But in reality, the data is being stored in AWS.

This helps companies move away from physical tapes without changing everything they already use.

## Main use cases

Tape Gateway is mainly used when a company

 already uses tape-based backup software
 wants to replace physical tapes with cloud storage
 needs long-term backup and archive storage
 wants a cheaper and easier way to keep backups for compliance or disaster recovery

## Key features

 Presents itself as a Virtual Tape Library (VTL)
 Works with existing backup applications that support tape
 Stores active virtual tapes in AWS
 Archives tapes to Amazon S3 Glacier Flexible Retrieval or Amazon S3 Glacier Deep Archive
 Reduces the need for physical tape hardware and offsite tape transport
 Supports durable, scalable cloud storage
 Helps with backup retention and disaster recovery

## How it works

### 1. Deploy the gateway

You deploy Tape Gateway as a virtual appliance on-premises or in supported infrastructure.

### 2. Connect backup software

Your existing backup software sees the gateway as a normal tape library with tape drives and tapes.

### 3. Write backups to virtual tapes

Backups are written to virtual tapes instead of physical tapes.

### 4. Store and archive in AWS

The virtual tapes are stored in AWS. When they are no longer actively used, they can be archived to lower-cost archival storage.

### 5. Retrieve when needed

If you need an archived tape again, you retrieve it from archive storage and make it available to your backup application.

## Why it is important for the exam

Tape Gateway appears in exam questions when AWS wants to test whether you can identify

 a tape backup migration scenario
 a company that wants to keep its existing backup software
 a need for long-term archive storage in AWS
 a replacement for physical tape infrastructure

The exam often gives clues like

 “virtual tape library”
 “backup application already uses tapes”
 “replace physical tapes”
 “archive backup data in AWS”

Those clues usually point to AWS Tape Gateway.

## Related AWS services and differences

### Tape Gateway vs File Gateway

 Tape Gateway is for backup tapes  VTL workflows
 File Gateway gives file access using NFS or SMB

Use Tape Gateway when the company is talking about backup software and tapes, not shared files.

### Tape Gateway vs Volume Gateway

 Tape Gateway is for virtual tapes and backup archives
 Volume Gateway provides block storage volumes for applications

Use Volume Gateway for disk volumes. Use Tape Gateway for tape-style backup systems.

### Tape Gateway vs Amazon S3 Glacier

 Tape Gateway is the gateway service that makes cloud storage look like tapes
 Amazon S3 Glacier is the low-cost storage layer used for archive

Tape Gateway is the interfaceworkflow. Glacier is the archive storage destination.

### Tape Gateway vs AWS DataSync

 Tape Gateway is for tape-based backup workflows
 AWS DataSync is for moving files between on-premises and AWS

If the question is about backup tapes, choose Tape Gateway, not DataSync.

## Common exam traps

### Trap 1 Choosing File Gateway

If the question mentions shared files, use File Gateway.
If it mentions backup tapes or VTL, use Tape Gateway.

### Trap 2 Choosing Volume Gateway

If the question needs block storage volumes, use Volume Gateway.
If it needs virtual tape backup, use Tape Gateway.

### Trap 3 Choosing Glacier alone

Glacier is storage, but it does not replace the tape library behavior by itself.
If the company wants to keep using existing tape-based backup software, Tape Gateway is the better answer.

### Trap 4 Missing the word “existing backup software”

This is one of the biggest clues. If the company already has a backup app designed for tapes, Tape Gateway is usually the answer.

## Easy real-world example

A bank has an old backup system that writes nightly backups to physical tapes. Staff then ship those tapes to an offsite location for storage.

The bank wants to stop managing physical tapes but does not want to replace its backup software.

The solution is AWS Tape Gateway.

The backup software keeps working almost the same way, but the tapes are now virtual and stored in AWS.

## Final summary

AWS Tape Gateway lets companies keep using tape-based backup software while replacing physical tapes with cloud-based virtual tapes.

It is best for organizations that want

 backup modernization
 long-term archive storage
 less tape hardware management
 easier disaster recovery

For the exam, remember this

If the question says virtual tape library, tape backups, or replace physical tapes, think Tape Gateway.

## Short exam answer

AWS Tape Gateway is a Storage Gateway service that presents a virtual tape library to existing backup software and stores backup tapes in AWS, with archival options in S3 Glacier.

## Memory trick

Tape = old-style backup tapes moved to the cloud.

Or even shorter

Tape Gateway = “my old tape backup system, but on AWS.”

## Additional Distinct Source Material

## 📝 Why It's Important for the Exam

The AWS CCP exam tests whether you understand which AWS service to use for which problem. Tape Gateway appears in questions like

- A company uses tape backups and wants to migrate to the cloud without changing their workflow — what should they use
- What is AWS Storage Gateway Tape Gateway used for
- How can a company achieve low-cost long-term archival while keeping their existing backup software

The key exam concept Tape Gateway = cloud replacement for physical tape backup systems.

---

## 🔗 Related AWS Services & Differences

 Service  What It Does  Key Difference
---------
 Tape Gateway  Replaces physical tape libraries  For backup software using VTLiSCSI
 S3 File Gateway  Maps files to S3 as NFSSMB share  For file storage, not backup tapes
 Volume Gateway  Presents cloud storage as iSCSI block volumes  For block storage  disk volumes
 Amazon S3  Object storage  Tape Gateway stores into S3
 Amazon Glacier  Cold archival storage  Tape Gateway archives to Glacier
 AWS Backup  Centralized backup management  Policy-driven, not tape-based

 💡 Remember All three gateways (Tape, File, Volume) are part of AWS Storage Gateway — one family, three different use cases.

---
