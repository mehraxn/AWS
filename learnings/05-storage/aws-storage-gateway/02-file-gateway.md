# README AWS File Gateway

## Simple definition

AWS File Gateway is a type of AWS Storage Gateway that lets your on-premises servers use file protocols like NFS or SMB while storing the data in AWS.

For the Cloud Practitioner exam, think of it as a bridge between your local file system and AWS storage.

## Core idea in plain English

Your company already has apps and users that expect to open files from a normal shared folder.

Instead of changing those apps, AWS File Gateway lets them keep using a file share they already understand. Behind the scenes, the files are stored in AWS.

So the big idea is

Keep the familiar file-share experience, but move the storage into AWS.

## Main use cases

### 1. File backup to AWS

A company wants to store shared files in the cloud without changing how users access them.

### 2. Hybrid cloud storage

A business still has on-premises servers, but wants AWS storage in the background.

### 3. Low-latency access with cloud storage

Frequently used files can be cached locally for faster access.

### 4. Migration from on-premises file storage

A company wants to reduce local storage and gradually move files to AWS.

### 5. Archive and cost optimization

Older files can live in AWS storage instead of expensive on-premises hardware.

## Key features

 Uses NFS and SMB file protocols
 Presents cloud storage like a normal file share
 Stores data in AWS instead of only on local disks
 Keeps a local cache for faster access
 Helps with hybrid cloud setups
 Integrates with existing on-premises applications
 Managed by AWS as part of AWS Storage Gateway

## How it works

### Easy step-by-step view

1. You deploy a File Gateway appliance in your environment.
2. Your users or applications connect to it using NFS or SMB.
3. They read and write files like they normally do.
4. The gateway sends the data to AWS storage.
5. Frequently accessed data can stay in a local cache for faster performance.

## Important exam picture

Think of File Gateway as

On-premises app → File share (NFSSMB) → File Gateway → AWS storage

That is the exam-friendly mental model.

## Why it is important for the exam

AWS exams often test whether you can choose the right storage type.

File Gateway is important because it solves a very specific problem

I have on-premises systems that need file-based access, but I want AWS storage behind the scenes.

You should recognize File Gateway when the question mentions

 on-premises environment
 hybrid storage
 NFS or SMB
 file shares
 local cache
 moving file storage to AWS

## Related AWS services and differences

### AWS Storage Gateway

This is the bigger service family.

File Gateway is one type of AWS Storage Gateway.
Other types include

 Volume Gateway for block storage
 Tape Gateway for virtual tape backups

### File Gateway vs Volume Gateway

 File Gateway = file storage access
 Volume Gateway = block storage access

If the exam mentions files, file shares, NFS, SMB, think File Gateway.
If it mentions block storage or volumes, think Volume Gateway.

### File Gateway vs Tape Gateway

 File Gateway = file shares
 Tape Gateway = virtual tapes for backup software

If the question talks about tape replacement, think Tape Gateway, not File Gateway.

### File Gateway vs Amazon S3

Amazon S3 is object storage, not a traditional file share.

File Gateway helps users and apps access AWS-backed storage through file protocols.

Exam mindset

 S3 alone = object storage
 File Gateway = file-style access to AWS-backed storage

### File Gateway vs Amazon EFS

 Amazon EFS is a native AWS file storage service for workloads running in AWS.
 File Gateway is mainly for connecting on-premises environments to AWS using file protocols.

If the question is about hybrid or on-premises access, File Gateway is often the better answer.
If the question is about AWS cloud-native shared file storage for EC2, think EFS.

### File Gateway vs AWS DataSync

 File Gateway gives ongoing file-based access to AWS-backed storage.
 AWS DataSync is mainly for moving or copying data.

If the question is about a persistent hybrid file access layer, think File Gateway.
If it is about fast transfer or migration, think DataSync.

## Common exam traps

### Trap 1 Mixing up file, block, and object storage

This is one of the biggest AWS exam traps.

 File Gateway = file
 Volume Gateway = block
 S3 = object

### Trap 2 Forgetting the hybrid part

File Gateway is usually about connecting on-premises systems with AWS.

If the workload is fully inside AWS, another service like EFS may be a better fit.

### Trap 3 Thinking users access S3 directly as a file share

S3 is object storage.

Users usually do not mount S3 directly like a normal file server in basic exam questions. File Gateway gives the familiar file-share interface.

### Trap 4 Confusing migration with ongoing access

 If the goal is continuous hybrid file access, think File Gateway.
 If the goal is moving data quickly, think DataSync.

### Trap 5 Ignoring protocol clues

If you see NFS or SMB, that is a strong clue for File Gateway.

## Easy real-world example

A small company has a Windows file server in its office.
Employees save documents to a shared folder every day.

The company wants to reduce local storage costs and use AWS, but it does not want to retrain employees or rewrite applications.

So it deploys AWS File Gateway.
Employees still use the shared folder in the normal way.
The files are stored in AWS, and commonly used files can be cached locally for faster access.

## Final summary

AWS File Gateway is a hybrid storage service that gives file-based access to AWS-backed storage.

It is best when

 you still have on-premises systems
 you need NFS or SMB access
 you want a familiar file-share experience
 you want AWS storage behind the scenes

For exam thinking, remember

File Gateway = on-premises file access + AWS storage + local cache

## Short exam answer

AWS File Gateway is a type of AWS Storage Gateway that lets on-premises applications access AWS-backed storage using file protocols like NFS and SMB, with local caching for low-latency access.

## Memory trick

### File = Folder

If the question sounds like users want a shared folder or file share, think File Gateway.

### V = Volume = Block

If the question sounds like a disk volume, think Volume Gateway.

### Tape = Backup library

If the question sounds like old-style backup tapes, think Tape Gateway.

### One-line memory trick

File Gateway = familiar office file share, but AWS stores the data.
