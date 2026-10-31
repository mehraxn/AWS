# Amazon Relational Database Service (Amazon RDS)

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Amazon RDS is a managed service for relational databases. Applications retain SQL, tables, schemas, keys, joins, constraints, and transactions, while AWS manages much of the infrastructure provisioning, supported-engine patching, backups, and replacement of failed infrastructure. A database on EC2 offers more OS and engine control but leaves these operations to the customer.

AWS currently documents RDS engines for IBM Db2, MariaDB, Microsoft SQL Server, MySQL, Oracle Database, and PostgreSQL. Features, versions, licensing, Regions, replica behavior, and RDS Proxy support differ by engine, so always verify the intended combination.

## Core Resources and Placement

| Resource | Purpose |
|---|---|
| DB instance | Managed compute and memory running the engine |
| DB subnet group | Subnets in multiple Availability Zones available for placement |
| Security group | Stateful network access control for database clients |
| Parameter group | Engine configuration; some changes require reboot |
| Option group | Supported engine-specific capabilities |
| Endpoint | DNS name applications use instead of a fixed IP |

Private subnets are the normal production placement, but private placement alone is not security. Routes, security groups, credentials, database users, encryption, monitoring, and backup protection still matter.

## Storage, Scaling, and Connections

- Changing DB instance class is vertical scaling and can interrupt service depending on the operation and topology.
- Select an engine-supported storage type and capacity. Storage Auto Scaling can grow configured storage but cannot correct inefficient queries.
- Eligible read-heavy workloads can scale horizontally with read replicas; traditional relational writes remain centered on a writer.
- Application connection pooling avoids exhausting finite database connections.

### RDS Proxy

RDS Proxy is a managed, highly available proxy that pools and reuses connections. It is valuable for Lambda and bursty workloads that would otherwise create connection storms, and can improve application recovery during failover. Authentication can use Secrets Manager and supported IAM database authentication patterns.

RDS Proxy does **not** cache query results and is not a read replica. It has separate cost, and engine/version/Region support must be checked. Direct connections can remain suitable for stable workloads with effective application-side pooling.

## Backups, Snapshots, and Recovery

Automated backups follow a configured retention period and combine snapshots and transaction logs to support point-in-time recovery. Manual DB snapshots have a customer-controlled lifecycle and remain until deleted. Supported snapshots can be copied across Regions and manual snapshots can be shared with appropriate encryption and AWS KMS permissions.

A restore normally creates a new DB instance or cluster; it does not rewind the running resource in place.

| Requirement | Correct mechanism |
|---|---|
| Recover to a time in the retention window | Automated backup and point-in-time restore |
| Retain a release recovery point until explicitly removed | Manual snapshot |
| Automatic service failover after an AZ problem | Multi-AZ, not a backup |
| Scale read-only reporting | Read replica, not a backup |

Replication can copy accidental changes, so it does not replace backups. RTO is the acceptable restoration time; RPO is the acceptable amount of recent data loss.

## Multi-AZ versus Read Replicas

RDS Multi-AZ is primarily for high availability and failover. In the traditional DB-instance topology, RDS maintains a synchronous standby in another Availability Zone and redirects the same logical endpoint after failover. The standby is not a general read target. RDS also offers supported Multi-AZ DB clusters with a different topology, so identify the deployment type.

Read replicas are primarily for read scaling. Engine-native replication is generally asynchronous, so lag is possible. Replicas have independent endpoints, serve eligible read-only traffic, and can be promoted. Supported engines can offer same-Region or cross-Region replicas.

| Dimension | Traditional Multi-AZ standby | Read replica |
|---|---|---|
| Goal | Availability and failover | Read scaling; possible DR component |
| Replication | Synchronous conceptually | Generally asynchronous |
| Endpoint | Same logical endpoint after failover | Separate endpoint |
| Ordinary read traffic | No | Yes |
| Transition | Managed failover | Explicit promotion |

## Security and Shared Responsibility

AWS manages the RDS service infrastructure. Customers manage data classification, engine configuration, database users, credentials, IAM, security groups, public-access settings, encryption choices, recovery objectives, and restore testing.

- Prefer private placement and allow only application security groups on the database port.
- Use AWS KMS encryption at rest and supported TLS in transit.
- Store/rotate secrets with Secrets Manager where appropriate; IAM database authentication is configuration dependent.
- Apply least privilege in IAM and within the engine.
- Protect snapshot sharing and KMS key policy as data-access decisions.
- Use RDS events, CloudWatch metrics, database logs, Enhanced Monitoring, and current performance-analysis features as appropriate.

## Availability, Performance, and Cost

Combine Multi-AZ with resilient application clients and tested restores. Multi-AZ is not automatically multi-Region DR. Cross-Region replicas or copied snapshots can support DR, but promotion, DNS, RTO, RPO, and failback still require design.

Cost factors include engine licensing, instance class/runtime, topology, storage and I/O, backup storage, replicas, cross-AZ/Region transfer, monitoring, and RDS Proxy. A standby, replica, proxy, and cache each solve different problems.

## CPP Exam Focus

- RDS is a managed relational database service using familiar engines.
- Multi-AZ means availability; read replicas mean read scaling.
- Automated backups support PITR; manual snapshots have a user-controlled lifecycle.
- Managed does not remove customer responsibility for data, access, and configuration.

## SAA Scenarios

1. **Production orders must survive an AZ failure without manual promotion:** use an appropriate Multi-AZ deployment.
2. **Reporting overloads the writer:** add eligible read replicas and route tolerant reads to replica endpoints.
3. **Thousands of Lambda invocations cause connection pressure:** evaluate RDS Proxy, not a query cache.
4. **A release needs a retained recovery point plus PITR:** keep automated backups and take a manual snapshot.
5. **The workload needs OS access or unsupported extensions:** consider self-managed EC2 and accept its operational burden.

## Common Mistakes

- Treating Multi-AZ as read scaling or a replica as a backup.
- Expecting restore to overwrite the running DB instance.
- Assuming every engine supports every RDS feature.
- Assuming a private subnet alone secures the database.
- Confusing connection pooling with caching.

## Knowledge Check

1. Which feature primarily provides automatic AZ failover?
2. What is the main purpose of a read replica?
3. Why might Lambda use RDS Proxy?
4. How do automated backups and manual snapshots differ?
5. Does an RDS restore normally modify the running instance in place?

<details><summary>Answers</summary>

1. An appropriate RDS Multi-AZ deployment.
2. Scaling read-only workloads, accounting for replication lag.
3. To pool and reuse connections and reduce connection pressure.
4. Automated backups follow retention; manual snapshots remain until deleted.
5. No, restore creates a new resource.

</details>

## References

Checked 2026-07-23.

- [What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [RDS automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
- [RDS Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
- [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
- [RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)
- [RDS pricing](https://aws.amazon.com/rds/pricing/)
