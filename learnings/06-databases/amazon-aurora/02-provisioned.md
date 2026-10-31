# Aurora Provisioned

## Simple definition

Aurora Provisioned means you run Amazon Aurora using fixed database instances that you choose in advance.

You select the DB instance class, which determines CPU and memory, and Aurora runs your database on that chosen capacity until you scale it up or down.

---

## Core idea in plain English

Think of Aurora Provisioned like renting a car of a specific size.

You choose the size first, pay for that size, and keep using it until you decide to switch to a bigger or smaller one.

This is different from a serverless model, where capacity can adjust more automatically based on demand.

---

## Main use cases

### 1. Predictable workloads

Aurora Provisioned is a strong choice when the workload is stable and the company can estimate how much database capacity it needs.

This helps deliver consistent performance.

### 2. Business-critical applications

It is commonly used for important production systems that need reliability, durability, and high availability.

Examples include payment systems, customer portals, and order-processing applications.

### 3. Applications that need read scaling

If an application has many read requests, Aurora Replicas can be added to increase read capacity.

This is useful for websites, dashboards, and reporting queries.

### 4. Teams that want control over database size

Some companies prefer to choose the exact instance size instead of letting AWS adjust compute automatically.

This gives more predictable capacity planning.

### 5. Relational database workloads

Aurora Provisioned is designed for SQL-based relational applications.

It fits workloads that need tables, relationships, joins, and structured data.

### 6. MySQL- or PostgreSQL-compatible applications

It works well when the application is built for MySQL or PostgreSQL compatibility and the company wants Aurora’s performance and availability benefits.

---

## Key features

### 1. Fully managed relational database

Aurora is a managed AWS database service.

AWS handles many operational tasks such as backups, patching support, monitoring integration, and recovery capabilities.

### 2. Provisioned compute capacity

You choose the DB instance size yourself.

This means the compute power is planned in advance rather than adjusting automatically like serverless.

### 3. Shared cluster storage

Aurora separates compute from storage.

The database instances use shared cluster storage, and Aurora automatically grows storage as data increases.

### 4. High availability across Availability Zones

Aurora stores data across multiple Availability Zones.

This improves durability and supports failover if a problem happens in one location.

### 5. Read scaling with replicas

You can add Aurora Replicas to serve read-only traffic.

This helps improve performance for read-heavy workloads.

### 6. Fast failover support

If the primary writer fails, Aurora can promote a replica to become the new writer.

This reduces downtime compared with traditional database setups.

### 7. MySQL and PostgreSQL compatibility

Aurora supports engines compatible with Aurora MySQL and Aurora PostgreSQL.

That makes it easier to move many relational workloads into Aurora.

---

## How it works

An Aurora Provisioned cluster usually includes:

### 1. One writer instance

The writer handles read and write operations for the main database workload.

### 2. Optional reader instances

Reader instances, also called Aurora Replicas, handle read-only traffic and can improve performance.

### 3. Shared storage layer

All instances in the cluster connect to the same Aurora storage volume.

This storage grows automatically as needed.

### 4. Automatic failover design

If the writer instance fails, Aurora can promote a replica to take over.

This supports higher availability.

### Simple flow

1. You create an Aurora DB cluster.
2. You choose provisioned DB instances.
3. One instance becomes the primary writer.
4. You can add replicas for more read capacity.
5. Aurora stores the data across multiple Availability Zones.
6. If the writer fails, Aurora can fail over to a replica.

### Important exam idea

In Aurora, compute and storage are separate.

You provision the compute instance size, while Aurora storage grows automatically behind the scenes.

---

## Why it is important for the exam

### 1. It tests managed database knowledge

The exam may check whether you understand that Aurora is managed by AWS, even when it is provisioned.

### 2. It tests provisioned vs serverless understanding

A common exam theme is knowing the difference between fixed chosen capacity and automatically adjusting capacity.

### 3. It tests relational database recognition

If the question asks for a managed relational database, Aurora is often a strong answer.

### 4. It tests high availability and scaling concepts

Aurora is often linked with Multi-AZ durability, failover, and read replicas.

---

## Related AWS services and differences

## Amazon RDS for MySQL/PostgreSQL vs Aurora Provisioned

Amazon RDS supports standard managed database engines such as MySQL and PostgreSQL.

Aurora is AWS’s cloud-native relational database built for higher performance, availability, and scalability.

### Simple difference

* **RDS MySQL/PostgreSQL** = managed traditional database engines
* **Aurora Provisioned** = managed AWS-built relational engine with Aurora architecture

## Aurora Provisioned vs Aurora Serverless v2

This is one of the most important comparisons for the exam.

### Aurora Provisioned

1. You choose the DB instance size.
   You control the instance class yourself.

2. Capacity is more fixed until you change it.
   Scaling usually requires modifying the instance configuration.

3. Good for predictable workloads.
   It fits workloads with steady or expected demand.

### Aurora Serverless v2

1. Capacity adjusts more automatically based on demand.
   AWS scales compute within limits you configure.

2. Billing is tied more closely to Aurora capacity usage.
   This is useful when demand changes often.

3. Good for variable or unpredictable workloads.
   It fits applications with changing traffic patterns.

### Easy comparison

* **Provisioned** = choose size yourself
* **Serverless** = AWS adjusts compute capacity within limits you set

## Aurora vs DynamoDB

### Aurora

1. Relational database
   Uses SQL and structured schemas.

2. Supports joins and complex relationships
   Good for traditional application databases.

### DynamoDB

1. NoSQL database
   Designed for key-value and document access patterns.

2. Very high scale and low-latency access
   Good for non-relational workloads.

### Exam shortcut

If the question says **relational database**, think **Aurora or RDS**, not DynamoDB.

## Aurora vs Redshift

### Aurora

1. Transactional relational database
   Built for application workloads such as orders, users, and transactions.

### Redshift

1. Data warehouse
   Built for analytics, reporting, and large-scale query processing.

### Exam shortcut

If the question is about **running an application database**, Aurora is the better fit.

If the question is about **analytics across large datasets**, Redshift is the better fit.

---

## Common exam traps

### Trap 1. Confusing Aurora with DynamoDB

This is wrong because Aurora is a relational database, while DynamoDB is a NoSQL service.

If the question mentions SQL, joins, structured tables, or relational data, Aurora is the more likely answer.

### Trap 2. Thinking provisioned means self-managed

This is wrong because Aurora Provisioned is still fully managed by AWS.

You choose the instance size, but AWS still manages much of the operational work.

### Trap 3. Forgetting that storage is separate from compute

This is a major Aurora concept.

In Aurora, provisioned mainly refers to the compute instances, while the storage layer grows automatically.

### Trap 4. Mixing up Aurora Provisioned and Aurora Serverless

Provisioned means you pick a fixed instance class.

Serverless means compute can scale more automatically.

### Trap 5. Choosing Aurora for non-relational workloads

Aurora is not the best choice when the exam clearly asks for a NoSQL database with key-value or document access at very large scale.

In that case, DynamoDB is usually better.

### Trap 6. Thinking replicas are only for backup

Aurora Replicas are mainly used for read scaling and availability.

They are not just backup copies.

### Trap 7. Confusing Aurora with Redshift

Aurora is for transactional application databases.

Redshift is for analytics and data warehousing.

---

## AWS exam key words for Aurora Provisioned

These are the words and phrases that may appear in exam questions:

### Core identity key words

* Amazon Aurora
* Aurora Provisioned
* Relational database
* Managed database
* Amazon RDS family
* SQL database
* MySQL-compatible
* PostgreSQL-compatible

### Performance and architecture key words

* Provisioned capacity
* DB instance class
* Fixed compute capacity
* Shared storage
* Storage auto-scaling
* Separate compute and storage
* Cluster volume
* High performance
* Low latency

### Availability and scaling key words

* Multi-AZ
* High availability
* Automatic failover
* Aurora Replica
* Read replica
* Read scaling
* Writer instance
* Reader instance
* Business-critical workload

### Comparison key words

* Provisioned vs Serverless
* Predictable workload
* Steady workload
* Variable workload
* Relational vs NoSQL
* Aurora vs DynamoDB
* Aurora vs RDS
* Aurora vs Redshift

### Exam clue phrases

If you see phrases like these, Aurora Provisioned may be a strong answer:

1. **Predictable database workload**
   This suggests fixed chosen capacity may fit well.

2. **Relational database with high availability**
   Aurora is often a strong answer here.

3. **Need read replicas for read-heavy traffic**
   Aurora Replicas are a key clue.

4. **MySQL or PostgreSQL compatible application**
   Aurora supports both compatibility paths.

5. **Need managed database but want to choose instance size**
   This strongly points to Aurora Provisioned.

---

## Easy real-world example

A company runs an online shopping website.

It has steady traffic every day and wants a fast relational database for orders, customers, and payments.

The company chooses Aurora Provisioned because:

### 1. It wants predictable database performance

The company knows roughly how much capacity it needs.

### 2. It wants high availability

Aurora supports durability and failover across Availability Zones.

### 3. It wants read scaling

Aurora Replicas can serve read-heavy traffic such as product browsing and reports.

### 4. It wants managed operations

AWS handles much of the database administration work.

This is a classic Aurora Provisioned use case.

---

## Final summary

Aurora Provisioned is Amazon Aurora running on database instances that you size and choose yourself.

It is a managed relational database designed for high performance, high availability, and read scaling.

The biggest exam idea is this:

**Provisioned means fixed chosen compute capacity, while Aurora still provides managed operations and shared, automatically growing storage.**

---

## Short exam answer

Aurora Provisioned is a fully managed relational database deployment model for Amazon Aurora where you choose fixed DB instance capacity in advance, making it a good fit for predictable workloads that need performance, availability, and read scaling.

---

## Memory trick

## **Provisioned = Pre-picked power**

Use this memory trick:

Provisioned means you **pre-pick** the database size.

So if the exam says the company wants a relational database and wants to choose a known database size for predictable usage, think:

**Aurora Provisioned**.
