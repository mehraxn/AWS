# AWS Snowball Edge

## Simple definition

AWS Snowball Edge is a physical AWS device that you use to move large amounts of data and, in some cases, run compute workloads at the edge or in places with little or no internet.

 Exam update AWS Snowball Edge is no longer available to new customers. Existing customers can still use it. For new customers, AWS points to alternatives such as AWS DataSync for online transfer and AWS Outposts for edge computing.

## Core idea in plain English

Think of Snowball Edge as a rugged box from AWS.

AWS ships the device to your site, you load data onto it, and then you send it back to AWS. This is useful when your internet connection is too slow, too expensive, or not reliable enough to move huge amounts of data online.

Some Snowball Edge devices can also do local processing, which means they can run certain workloads near where the data is created.

## Main use cases

### 1. Large data migration

Move terabytes or petabytes of data into AWS when network transfer would take too long.

### 2. Remote or disconnected locations

Use it in places such as ships, mining sites, military environments, or rural areas where internet is limited.

### 3. Edge computing

Process data locally near the source instead of sending everything immediately to the cloud.

### 4. Temporary local storage and analysis

Store data on-site and run supported compute tasks before sending selected results to AWS.

## Key features

 Physical device from AWS for offline data transfer
 Rugged appliance designed for edge environments
 Encryption by default to protect data at rest and during transport
 High-speed network connections for loading data quickly
 S3-compatible storage on the device
 EC2-compatible compute support on some device types
 Can be used in disconnected or low-connectivity environments
 AWS OpsHub can be used to unlock and manage the device

## How it works

### Step 1 Create a job

You request a Snowball Edge device from AWS.

### Step 2 AWS ships the device

AWS prepares the device and sends it to your location.

### Step 3 Connect and unlock it

You connect it to power and your local network, then unlock it using the Snowball tools or AWS OpsHub.

### Step 4 Copy data or run local workloads

You transfer data to the device. If your job supports it, you can also run local compute workloads.

### Step 5 Return the device

When you finish, you send the device back to AWS.

### Step 6 AWS imports the data

AWS transfers the data into your target AWS storage, usually Amazon S3.

### Step 7 Device is wiped

After the job is complete, AWS securely erases the data from the device.

## Why it is important for the exam

Snowball Edge is important because it teaches a very common exam idea

When network transfer is not practical, AWS can use a physical device instead.

This service often appears in questions about

 very large data migration
 poor or limited connectivity
 secure offline transfer
 edge or remote computing

For the exam, the main message is

Use Snowball Edge when you need to move a lot of data physically, especially when the network is a bottleneck.

## Related AWS services and differences

### AWS Snowcone

 Smaller device than Snowball Edge
 Better for smaller workloads and more portable use cases
 Good when you need a compact edge device

Difference Snowball Edge is larger and stronger for heavier data transfer or edge workloads.

### AWS Snowmobile

 A truck-sized data transfer option
 Used for exabyte-scale migrations

Difference Snowball Edge is for large migrations, but Snowmobile is for extremely massive migrations.

### AWS DataSync

 Online data transfer service over the network
 Good for ongoing or network-based transfers

Difference DataSync uses the network; Snowball Edge is mainly for offline or limited-connectivity transfer.

### AWS Storage Gateway

 Connects on-premises environments to AWS storage
 Useful for hybrid storage access

Difference Storage Gateway is for hybrid integration over the network, not mainly for shipping devices.

### AWS Outposts

 Brings AWS infrastructure and services on-premises
 Good for running AWS-style workloads locally

Difference Outposts is for consistent hybrid cloud infrastructure on-site. Snowball Edge is more about portable edge computing and offline data transfer.

## Common exam traps

### Trap 1 Choosing Snowball Edge for normal internet transfer

Wrong when the network is already fast and stable.

If the question says you have a good connection and need continuous transfer, DataSync may be better.

### Trap 2 Confusing Snowball Edge with Snowcone

Snowcone is the smaller portable option. Snowball Edge is the larger, more powerful device.

### Trap 3 Confusing Snowball Edge with Snowmobile

Snowmobile is for the biggest migrations at an extreme scale.

### Trap 4 Forgetting the edge computing part

Snowball Edge is not only for storage transfer. Some versions can also provide local compute.

### Trap 5 Ignoring the service status update

Older study materials may present Snowball Edge as generally available for all customers.

For current understanding, remember new customers can no longer start using Snowball Edge.

## Easy real-world example

A media company has 800 TB of video files in a remote studio with a slow internet connection.

Uploading everything over the internet would take too long.

So the company orders AWS Snowball Edge, copies the files onto the device, ships it back to AWS, and AWS imports the data into Amazon S3.

That is much faster and more practical than sending the data only over the network.

## Final summary

AWS Snowball Edge is a physical device used to move very large amounts of data to or from AWS when internet transfer is too slow or impractical.

It can also support certain edge computing tasks in remote or disconnected environments.

For the Cloud Practitioner exam, remember it as the AWS service for large offline data transfer and edge use cases.

Also remember the current update it is not available to new customers anymore, but it is still important because it appears in AWS learning materials and exam-style comparisons.

## Short exam answer

AWS Snowball Edge is an AWS physical device used for secure, large-scale offline data transfer and edge computing in locations with limited or no internet connectivity.

## Memory trick

Snowball Edge = “Ship the box when the network is the problem.”

If the internet is too slow, too weak, or unavailable, think Snowball Edge.
