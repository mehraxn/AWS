# AWS DataSync

## Simple definition

AWS DataSync is a managed AWS service that helps you move data quickly and securely between on-premises storage, AWS storage services, and sometimes other cloud storage.

## Core idea in plain English

Think of AWS DataSync as a smart moving service for files and objects. Instead of copying data manually, writing scripts, or using slow tools, DataSync automates the transfer for you.

It is built for large-scale data movement. You choose the source, choose the destination, and DataSync handles the transfer, scheduling, encryption in transit, and data validation.

## Main use cases

 Move file data from on-premises servers to AWS
 Migrate data into Amazon S3, Amazon EFS, or Amazon FSx
 Copy data between AWS storage services
 Replicate data on a schedule for backup or disaster recovery
 Transfer data for hybrid cloud workloads
 Move cold data into lower-cost storage classes for archiving

## Key features

 Fully managed data transfer service
 High-speed transfer compared with basic manual copy methods
 Supports scheduling for repeated transfers
 Encrypts data in transit
 Validates data integrity during transfer
 Can preserve metadata, permissions, and timestamps where supported
 Includes filtering and bandwidth control
 Gives monitoring and task reporting through AWS

## How it works

### 1. Choose the source and destination

You define where the data comes from and where it should go.

Examples

 On-premises NAS to Amazon S3
 On-premises file server to Amazon EFS
 Amazon EFS to Amazon S3
 One AWS storage service to another

### 2. Deploy an agent if needed

For many on-premises or self-managed storage transfers, you deploy a DataSync agent near your storage.

The agent is a virtual machine that reads data and sends it securely.

Important exam point an agent is often needed for on-premises or self-managed storage, but not for every transfer type. Some AWS-to-AWS transfers do not need an agent.

### 3. Create locations

A location is the source or destination storage endpoint.

### 4. Create a task

A task tells DataSync what to copy and how to copy it.

You can set options such as

 schedule
 filters
 bandwidth limits
 verification settings
 how to handle deleted files

### 5. Run the task

You can run it once or on a schedule. DataSync transfers the data, checks integrity, and shows progress and results.

## Why it is important for the exam

AWS likes to test whether you know which service is best for moving data.

DataSync is the correct answer when the question is about

 moving large amounts of file or object data
 transferring data between on-premises and AWS
 automating recurring data transfers
 using a managed service instead of custom scripts

For the Cloud Practitioner exam, the big idea is
DataSync = online, managed, automated data transfer service.

## Related AWS services and differences

### AWS DataSync vs AWS Snowball Edge

 DataSync online transfer over the network
 Snowball Edge physical device shipped to move data offline

Use Snowball Edge when the network is too slow, unreliable, or transferring massive data online would take too long.

### AWS DataSync vs AWS Storage Gateway

 DataSync moves or syncs data
 Storage Gateway gives hybrid access between on-premises environments and AWS storage

Storage Gateway is for ongoing hybrid storage access. DataSync is for transfer and synchronization tasks.

### AWS DataSync vs AWS Transfer Family

 DataSync managed bulk data transfer and synchronization
 Transfer Family managed FTP, FTPS, and SFTP access into AWS

Transfer Family is about file transfer protocols for users and applications. DataSync is about large-scale managed movement of data.

### AWS DataSync vs Amazon S3 Transfer Acceleration

 DataSync managed data migrationsynchronization service
 S3 Transfer Acceleration speeds up uploads to S3 over long distances

S3 Transfer Acceleration helps upload to S3 faster. DataSync is broader and handles task management, scheduling, validation, and syncing.

## Common exam traps

 Confusing DataSync with Snowball

   DataSync is online
   Snowball is offline using a physical device

 Confusing DataSync with Storage Gateway

   DataSync moves data
   Storage Gateway extends storage into AWS for hybrid use

 Thinking DataSync is mainly for databases

   DataSync is mainly for file and object data transfer

 Forgetting the word managed

   AWS handles much of the complexity for you

 Assuming an agent is always required

   Many on-premises transfers use an agent, but not every DataSync transfer needs one

## Easy real-world example

A company has 80 TB of files on an on-premises NAS device and wants to move them into Amazon S3 for long-term storage and future analytics.

They use AWS DataSync to connect the on-premises storage to AWS, create a transfer task, and move the data securely. Later, they schedule regular sync jobs so any new files are also copied to AWS.

## Final summary

AWS DataSync is a managed AWS service for moving file and object data quickly, securely, and with less manual work.

It is commonly used to move data from on-premises systems to AWS storage services such as Amazon S3, Amazon EFS, and Amazon FSx. It can also automate recurring sync jobs.

For the exam, remember that DataSync is best when the question is about online bulk data transfer, migration, or synchronization.

## Short exam answer

AWS DataSync is a managed service that automates and accelerates online data transfers between on-premises storage, AWS storage services, and some other storage locations.

## Memory trick

DataSync = Data + Sync

If the question says

 move lots of data
 do it online
 do it regularly
 avoid custom scripts

Think AWS DataSync.
