# Amazon DynamoDB

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Amazon DynamoDB is a serverless, fully managed NoSQL database for key-value and document data. It suits operational applications needing predictable low-latency access at scale without managing database servers. Design starts with required access patterns, not normalized relational schemas.

## Data Model and Access Patterns

- A **table** contains **items**; items contain named **attributes**.
- A simple primary key has only a **partition key**.
- A composite primary key combines a partition key and **sort key**. Items sharing the partition key form an ordered item collection.
- DynamoDB uses partition-key values to distribute data. Low-cardinality or extremely hot keys can concentrate traffic and throttle even when aggregate capacity appears sufficient.

DynamoDB does not offer arbitrary relational joins. Denormalization and purpose-designed item collections are normal. A `Query` targets a partition-key value and can narrow with sort-key conditions. A `Scan` reads an entire table or index before filters discard items; filters do not remove that read work.

## Capacity Modes

| Mode | Management | Best fit | Trade-off |
|---|---|---|---|
| On-demand | DynamoDB handles request capacity; pay per request | New, variable, unpredictable workloads | Simple operations; can cost more than tuned provisioned capacity for steady traffic |
| Provisioned | Configure read/write capacity; Auto Scaling can adjust it | Predictable traffic and deliberate cost control | Requires monitoring; insufficient capacity throttles requests |

Capacity mode cannot compensate for a hot partition key. Indexes, transactions, Streams, backups, Global Tables, and DAX also affect usage and cost.

## Consistency and Transactions

Eventually consistent reads may not immediately show a recent successful write and consume less read capacity than strong reads. Strongly consistent reads request the latest successful value but are not supported by every read path. Global secondary indexes and DynamoDB Streams are eventually consistent.

DynamoDB transactions group supported reads or writes into all-or-nothing ACID operations. They help when several items must change atomically, but cost more resources than nontransactional requests and do not make DynamoDB a relational join engine.

## Local and Global Secondary Indexes

| Dimension | LSI | GSI |
|---|---|---|
| Partition key | Same as the base table | Can differ from the base table |
| Sort key | Alternate sort key | Optional alternate sort key |
| Creation | With the table | Can be added later |
| Read consistency | Eventual or strong | Eventual only |
| Capacity | Shares base-table capacity model | Has separate capacity behavior and cost considerations |
| Scope | One partition-key item collection | Whole table by index key |

Indexes are updated from base-table writes. An underprovisioned or poorly distributed GSI can bottleneck writes. Project only attributes required by the access pattern to reduce storage and write amplification.

## Streams and TTL

DynamoDB Streams captures item-level changes for a limited window and can invoke consumers such as Lambda. Use it for event processing and derived views, not as a permanent audit archive. Consumers must handle retries and duplicate delivery safely.

Time to Live (TTL) marks items for asynchronous expiration by timestamp. Deletion is not immediate, so applications must not rely on an exact deletion second.

## Backup, Recovery, and Global Tables

- On-demand backups are full, user-initiated backups retained until deleted.
- Point-in-time recovery continuously protects a table within the supported recovery window and restores to a new table.
- Replication can propagate accidental changes and does not replace backups.
- Global Tables replicate table data across AWS Regions. Account for the configured consistency mode, concurrent writes, application routing, Regional failure, permissions, and replicated cost.

Global Tables provide distributed availability and local access; backups/PITR restore an earlier state. They solve different problems.

## DynamoDB Accelerator (DAX)

DAX is a managed, DynamoDB-compatible in-memory cache for read-heavy DynamoDB workloads. It accelerates cacheable, eventually consistent reads without a general-purpose cache API. DAX is not durable primary storage, cannot rescue a poor key design, and is not the normal choice for strongly consistent reads.

Use ElastiCache when a general-purpose cache, sessions, custom data structures, or several source systems are involved. Use DAX when DynamoDB API compatibility and DynamoDB read acceleration are central.

## Security and Shared Responsibility

DynamoDB access is IAM based rather than database-user based. Apply least privilege and verify any fine-grained authorization model. Data is encrypted at rest with service key choices including supported customer-managed AWS KMS keys, and clients use TLS in transit. Use CloudTrail for API activity and CloudWatch for metrics.

A gateway VPC endpoint can provide private supported access without NAT. Customers still own data classification, keys/access patterns, IAM, KMS policies, backup testing, application validation, and safe event processing.

## Availability, Performance, and Cost

DynamoDB is Regional and redundantly stores data across multiple Availability Zones; Global Tables extend to multiple Regions. Performance depends on key distribution, item size, access pattern, consistency, capacity, indexes, and retry/backoff behavior.

Cost includes requests or provisioned capacity, storage, indexes, Streams, backups/PITR, Global Tables, transfer, and DAX nodes. Scans, unused indexes, hot keys, and unnecessary replicas waste capacity and money.

## CPP Exam Focus

- Managed NoSQL key-value/document database with serverless operations.
- On-demand and provisioned are capacity choices.
- DynamoDB is durable storage; DAX is an optional cache.
- Global Tables provide multi-Region data; backups and PITR provide recovery.

## SAA Scenarios

1. **A new service has unpredictable request volume and known key lookups:** start with on-demand and a high-cardinality partition key.
2. **Steady volume is predictable and monitored:** provisioned capacity with Auto Scaling can improve cost control.
3. **Orders must be read by customer and date:** use a suitable composite key or index, not recurring scans.
4. **Eventually consistent reads need DynamoDB-compatible acceleration:** evaluate DAX.
5. **Users need local access in several Regions:** evaluate Global Tables plus routing, consistency/conflict, backup, and cost design.

## Common Mistakes

- Creating a schema before identifying access patterns.
- Using Scan instead of Query or an index.
- Assuming every read path supports strong consistency.
- Assuming TTL deletes immediately.
- Treating Global Tables as backups or DAX as durable storage.
- Ignoring GSI capacity and hot-key behavior.

## Knowledge Check

1. What distinguishes a composite primary key?
2. Why is Query usually preferable to Scan?
3. Which index may use a different partition key?
4. When is on-demand capacity attractive?
5. What does DAX accelerate?
6. Do Global Tables replace backups?

<details><summary>Answers</summary>

1. It combines partition and sort keys.
2. Query targets key-defined data; Scan reads the entire table or index.
3. A GSI.
4. New, variable, or unpredictable traffic where simplicity matters.
5. Eligible DynamoDB reads through a compatible in-memory cache.
6. No; replication and point-in-time recovery solve different risks.

</details>

## References

Checked 2026-07-23.

- [DynamoDB core components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)
- [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)
- [DynamoDB capacity modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html)
- [DynamoDB secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)
- [DynamoDB backup and restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html)
- [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
- [DynamoDB Accelerator](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html)
- [DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/)
