# Amazon EC2 Instance Store

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Simple definition

Amazon EC2 Instance Store is **temporary block storage** that is **physically attached to the host machine** running your EC2 instance.

This means the storage is located on the same server as the instance, not on a separate network storage system.

---

## Core idea in plain English

Think of EC2 Instance Store like a **local hard drive inside the computer** where your EC2 instance is running.

It is usually **very fast**, but it is also **temporary**.
If the instance stops, is terminated, or the underlying host changes, the data in the instance store can be lost.

So the big idea is:

**Instance Store = fast temporary storage for one EC2 instance**

---

## Main use cases

EC2 Instance Store is useful when you need storage that is:

* very fast
* temporary
* easy to replace
* not critical if lost

Common use cases:

### 1. Cache

You can store temporary cached data that can be rebuilt later.

### 2. Buffers and scratch data

Good for temporary files created while processing data.

### 3. Temporary content during computation

Useful for workloads that create intermediate files during analysis or batch jobs.

### 4. High-speed local storage

Good when an application needs very low latency local disk access.

### 5. Data that is replicated elsewhere

If the data already exists in another safe place, instance store can be used as a fast working area.

---

## Key features

### Temporary storage

The data is **not meant for long-term storage**.

### Physically attached to the host

It is directly connected to the server hosting the EC2 instance.

### High performance

Because it is local to the machine, it can provide very fast input/output performance.

### No separate storage charge in the usual exam explanation

For exam thinking, instance store is usually presented as storage that comes **with certain instance types** rather than as a separately attached volume like EBS.

### Cannot be detached and moved like EBS

It is tied to that specific host and instance.

### Data loss risk

If the instance is stopped, terminated, or fails in a way that moves it to another host, the data may disappear.

---

## How it works

When you launch certain EC2 instance types, AWS may provide one or more instance store volumes.

These volumes are:

* local to the physical host
* available only while that instance is running on that host
* designed for temporary data

A simple flow:

1. You launch an EC2 instance.
2. The instance gets access to local instance store disks if the instance type supports them.
3. Your application writes temporary data there.
4. The data stays available while the instance and host remain in place.
5. If the instance is terminated, or if the storage is lost because of host-level change, the data is gone.

Important exam point:

**Do not use instance store for data you must keep.**

---

## Why it is important for the exam

This topic appears in AWS Cloud Practitioner because it tests whether you understand the difference between:

* **temporary local storage**
* **persistent cloud storage**

In many exam questions, AWS wants you to know when to choose:

* **EC2 Instance Store** for speed and temporary data
* **Amazon EBS** for persistent block storage
* **Amazon S3** for object storage

The exam often checks whether you can identify that:

**Instance Store is fast but ephemeral.**

The word **ephemeral** means **temporary and not guaranteed to stay**.

---

## Related AWS services and differences

## EC2 Instance Store vs Amazon EBS

### EC2 Instance Store

* temporary storage
* physically attached to the host
* data can be lost
* very fast local access
* cannot be kept independently of the instance

### Amazon EBS

* persistent block storage
* network-attached to EC2
* data remains after stopping the instance in many normal cases
* can be detached and attached to another instance
* better for important data and boot volumes

**Easy exam rule:**
If the data must survive, choose **EBS**, not instance store.

---

## EC2 Instance Store vs Amazon S3

### EC2 Instance Store

* block storage
* attached to one EC2 instance
* temporary
* used by running workloads directly

### Amazon S3

* object storage
* highly durable
* accessed over the network
* good for backups, files, logs, media, and long-term storage

**Easy exam rule:**
If you need durable storage for files and objects, choose **S3**.

---

## EC2 Instance Store vs Amazon EFS

### EC2 Instance Store

* local to one host
* temporary
* not shared storage

### Amazon EFS

* shared file storage
* scalable
* can be mounted by multiple EC2 instances
* persistent network file system

**Easy exam rule:**
If multiple instances need shared files, choose **EFS**, not instance store.

---

## Common exam traps

### Trap 1: Confusing instance store with EBS

This is the biggest trap.

* **Instance Store** = temporary, local, data can be lost
* **EBS** = persistent, separate block storage

### Trap 2: Choosing instance store for databases

Databases usually need persistent storage.

For most exam questions, instance store is **not** the right choice for important database data.

### Trap 3: Forgetting the word “temporary”

If the question says:

* temporary files
* buffer
* cache
* scratch space
* high-speed local processing

Then instance store may be correct.

### Trap 4: Thinking all EC2 instances automatically have instance store

Not every EC2 instance type uses instance store in the same way.
On the exam, focus on the idea that **some instance types provide it**.

### Trap 5: Using instance store for backup or long-term data

That is wrong.
For backup or long-term durable storage, think of **S3** or **EBS**, depending on the situation.

---

## Easy real-world example

Imagine a video processing company.

A program running on an EC2 instance downloads a large video, processes it, creates temporary working files, and then uploads the final result to Amazon S3.

Those temporary working files do not need to be kept forever.
They only need fast local storage while the job is running.

That is a good case for **EC2 Instance Store**.

But the final video should be saved in **Amazon S3**, because S3 is durable.

---

## Failure and Design Supplement

Instance store is physically attached to the host. Data survives a reboot but is lost when the instance stops, hibernates, terminates, or the underlying host fails. Therefore use it only for caches, buffers, scratch data, or replicated data that can be rebuilt. The application owns replication, rehydration, and fault-tolerant behavior.

Instance store can offer high local performance without a separate volume charge, but only supported instance types provide it and its capacity follows the instance. EBS is network-attached, persists independently of an EC2 instance, and supports snapshots; choose EBS for boot volumes and durable application data.

### Knowledge Check

1. Does instance-store data survive reboot? **Yes.**
2. Does it survive stop or host failure? **No.**
3. What data fits it? **Disposable or replicated cache/scratch data.**

## Official References

- [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Instance store lifetime](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-lifetime.html)

Official references checked: 2026-07-22.

## Final summary

EC2 Instance Store is **fast local temporary storage** for an EC2 instance.

Use it when:

* speed matters
* the data is temporary
* the data can be lost and recreated

Do not use it when:

* the data is important
* the data must survive instance stop/termination/host issues
* you need long-term or shared storage

The most important comparison is:

**Instance Store = temporary**
**EBS = persistent**

---

## Short exam answer

**Amazon EC2 Instance Store is temporary block storage physically attached to the host running the EC2 instance. It provides high-speed local storage for temporary data such as cache, buffers, and scratch files, but the data can be lost if the instance stops, terminates, or moves to another host.**

---

## Memory trick

Remember this line:

**Instance Store = inside the machine, fast, but forgetful.**

Or even shorter:

**Store for speed, not for safety.**

---

## Mini exam coach note

When you see a question, ask yourself:

**Does the data need to survive?**

* If **yes**, think **EBS**, **EFS**, or **S3**.
* If **no**, and speed matters, think **EC2 Instance Store**.
