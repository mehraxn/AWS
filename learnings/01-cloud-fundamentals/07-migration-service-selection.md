# AWS Migration Service Selection

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Migration strategy answers **what type of change** a workload needs. Migration services answer **how applications and data can be discovered, moved, converted, replicated, or tracked**.

Do not choose a service only because the word “migration” appears in its name. First identify:

- what is moving: application server, database, files, objects, or a whole platform;
- whether the transfer is online or offline;
- available network bandwidth;
- data volume and transfer window;
- allowed downtime;
- whether source and target database engines differ;
- whether ongoing replication is required;
- whether the need is discovery, movement, conversion, or tracking.

Review [Cloud Migration Journey and the 7 Rs](06-cloud-migration-journey-and-7-rs.md) before this lesson.

## Service Map

| Need | Typical AWS service or capability |
|---|---|
| Discover on-premises servers and dependencies | AWS Application Discovery Service |
| Rehost servers or virtual machines | AWS Application Migration Service |
| Migrate or continuously replicate database data | AWS Database Migration Service (AWS DMS) |
| Convert database schema and code for a different engine | AWS Schema Conversion Tool (AWS SCT) or current AWS DMS schema-conversion capabilities, depending on the workflow |
| Transfer files or objects online between storage systems and AWS | AWS DataSync |
| Transfer very large data sets when network transfer is impractical | AWS Snowball devices |
| Track migrations across applications and tools | AWS Migration Hub |
| Extend AWS infrastructure and services to an on-premises location | AWS Outposts; this is hybrid infrastructure, not a general migration-transfer service |

Detailed service lessons are available in [Migration and Hybrid Cloud](../11-migration-and-hybrid-cloud/README.md).

## Discovery and Planning

### AWS Application Discovery Service

Use Application Discovery Service to collect information about on-premises servers and support migration planning.

It helps answer questions such as:

- What servers exist?
- What are their resource and utilization characteristics?
- Which systems communicate with each other?
- Which applications should move together?

Repository lesson: [AWS Application Discovery Service](../11-migration-and-hybrid-cloud/aws-application-discovery-service/01-overview.md)

**Do not confuse:** discovery finds and analyzes the environment; it does not itself migrate the application.

### AWS Migration Hub

Migration Hub provides a central place to view migration progress from supported tools and workflows.

Repository lesson: [AWS Migration Hub](../11-migration-and-hybrid-cloud/aws-migration-hub/01-overview.md)

**Do not confuse:** Migration Hub tracks and coordinates visibility. It is not the data-transfer mechanism and does not automatically select a migration strategy.

## Application and Server Migration

### AWS Application Migration Service

AWS Application Migration Service is used to move supported source servers to AWS through replication and conversion into AWS-based machines.

Typical use:

- rehost physical, virtual, or cloud-hosted servers;
- maintain ongoing replication before cutover;
- test migrated servers before final cutover;
- reduce the length of the final outage compared with a one-time manual copy.

The target architecture still needs review. A replicated single server does not automatically become elastic, Multi-AZ, or well architected.

## Database Migration

### AWS Database Migration Service

AWS DMS moves or replicates database data between supported sources and targets. It can support one-time migration and ongoing change replication for reduced-downtime cutovers.

Repository lesson: [AWS Database Migration Service](../11-migration-and-hybrid-cloud/aws-database-migration-service/01-overview.md)

Typical scenarios:

- migrate an on-premises database to an AWS database target;
- keep source and target synchronized while testing the target;
- migrate between compatible or different database engines, subject to supported combinations;
- support continuous replication use cases.

AWS DMS moves data. It does not automatically redesign application queries, convert every database object, or verify application compatibility.

### AWS Schema Conversion Tool and Schema Conversion

When the source and target use different database engines, schemas, stored procedures, functions, and application SQL might need conversion.

Repository lesson: [AWS Schema Conversion Tool](../11-migration-and-hybrid-cloud/aws-schema-conversion-tool/01-overview.md)

Use the following reasoning:

- **Same or compatible engine:** schema conversion might be minimal; focus on data movement, replication, validation, and cutover.
- **Different engine:** assess and convert schema and code, then migrate data and test application compatibility.

**Exam distinction:** AWS DMS is primarily associated with data movement and replication. Schema-conversion capabilities address database objects and code when changing engines.

## File and Object Data Transfer

### AWS DataSync

AWS DataSync is an online data-transfer service for moving data between supported on-premises storage, edge locations, other clouds in supported patterns, and AWS storage services.

Repository lesson: [AWS DataSync](../11-migration-and-hybrid-cloud/aws-datasync/01-overview.md)

Typical use:

- transfer large file sets over available network connectivity;
- automate recurring transfers;
- migrate data into services such as Amazon S3, Amazon EFS, or Amazon FSx where supported;
- reduce the custom scripting required for copying and verification.

Choose DataSync when an online network transfer is practical and the data type and endpoints are supported.

### AWS Snowball devices

Snowball devices support offline or disconnected data transfer by shipping a secure physical device between the customer and AWS.

Repository lesson: [AWS Snowball Edge](../11-migration-and-hybrid-cloud/aws-snowball-edge/01-overview.md)

Typical use:

- the data set is very large;
- network bandwidth is limited or expensive;
- an online transfer would take too long;
- a physical transfer meets the security and timing requirements.

Snowball reduces dependence on the network, but shipping, device handling, import time, and final data synchronization must be included in the plan.

## Online versus Offline Transfer

A useful first estimate is:

```text
transfer time = data size / effective throughput
```

Effective throughput is lower than a connection's advertised maximum because of protocol overhead, contention, latency, throttling, encryption, small-file behavior, and operational limits.

### Example reasoning

A company has a very large archive and a slow connection. The estimated online transfer would exceed the project deadline. Snowball is likely more appropriate for the bulk data.

If the data continues changing, the team might:

1. transfer the initial bulk data;
2. use an online service or replication mechanism for the final changes;
3. validate completeness;
4. perform cutover.

The correct design can combine services rather than forcing one service to solve every phase.

## Database Replication versus Physical Transfer

CLF-C02 explicitly expects learners to distinguish migration approaches such as database replication and AWS Snowball.

| Requirement | Better starting point |
|---|---|
| Database remains active and downtime must be reduced | AWS DMS or another supported replication approach |
| Large file or object archive and adequate bandwidth exists | AWS DataSync |
| Huge data volume and network transfer misses the deadline | AWS Snowball device |
| Need to identify server dependencies before planning waves | Application Discovery Service |
| Need centralized migration status visibility | Migration Hub |

Snowball is not a replacement for database change replication. Database replication is not a general solution for moving arbitrary file systems.

## Hybrid Infrastructure versus Migration

### AWS Outposts

AWS Outposts provides AWS infrastructure and selected services at an on-premises or edge location for workloads that require local processing, local data residency, or low-latency access to on-premises systems.

Repository lesson: [AWS Outposts](../11-migration-and-hybrid-cloud/aws-outposts/01-overview.md)

Outposts can be part of a hybrid-cloud strategy, but it is not a physical data-transfer appliance like Snowball and not a general migration-tracking service like Migration Hub.

## Decision Process

1. Identify the workload and data type.
2. Identify source and target environments.
3. Measure data size, change rate, and effective bandwidth.
4. Define downtime and cutover requirements.
5. Determine whether ongoing replication is needed.
6. Determine whether schema or application conversion is needed.
7. Select discovery, transfer, conversion, and tracking services separately.
8. Test with representative data and workloads.
9. Validate security, completeness, performance, and recovery.
10. Plan rollback and post-cutover monitoring.

## CPP Scenario Reasoning

| Scenario wording | Likely answer |
|---|---|
| “Discover on-premises server dependencies” | Application Discovery Service |
| “Track multiple application migrations in one place” | Migration Hub |
| “Move databases with ongoing replication and reduced downtime” | AWS DMS |
| “Convert schema while changing database engines” | Schema-conversion tooling |
| “Move file data online to AWS storage” | DataSync |
| “Move a massive data set where the network is too slow” | Snowball device |
| “Bring AWS infrastructure to an on-premises facility” | Outposts |

## SAA Architecture and Design

For SAA, include:

- encrypted connectivity and secure device handling;
- source and target performance capacity;
- replication lag and data consistency;
- cutover criteria and rollback;
- DNS, connection, and application configuration changes;
- database object and query compatibility;
- validation checksums or reconciliation;
- final change synchronization;
- post-cutover monitoring and backup;
- cost of transfer, appliances, staging storage, and parallel environments.

A migration service solves a movement or planning problem. It does not replace target architecture design.

## Common Exam Traps

- Migration Hub tracks; it does not transfer all workload data.
- Application Discovery Service discovers; it does not perform the migration.
- DataSync is an online transfer service; Snowball uses physical devices for offline transfer.
- AWS DMS moves and replicates database data; changing engines can also require schema and code conversion.
- Outposts extends AWS infrastructure on premises; it is not the same as Snowball.
- Rehosting a server does not automatically modernize or make it highly available.
- Advertised network speed is not equal to sustained application-level transfer throughput.

## Summary

Choose AWS migration services by the specific job: discover dependencies, replicate servers, migrate database data, convert schemas, transfer files online, transfer bulk data offline, or track progress. The correct solution often combines multiple services across assessment, replication, validation, cutover, and post-migration optimization.

## Knowledge Check

1. Which service helps discover on-premises servers and dependencies?
2. Which service is primarily used for database data migration and ongoing replication?
3. Which approach fits a very large data set when network transfer would miss the deadline?
4. What is the difference between DataSync and Snowball?
5. What is Migration Hub's primary role?
6. Why might changing database engines require more than AWS DMS data movement?
7. Is Outposts primarily a data-transfer appliance?

<details>
<summary>Show answers</summary>

1. AWS Application Discovery Service.
2. AWS Database Migration Service (AWS DMS).
3. An AWS Snowball device, subject to the full transfer and shipping plan.
4. DataSync transfers supported data online over network connectivity; Snowball uses shipped physical devices for offline or bandwidth-constrained transfer.
5. Central migration tracking and visibility.
6. Schema, stored procedures, functions, queries, and application behavior might require conversion and compatibility testing.
7. No. Outposts extends AWS infrastructure and selected services to an on-premises or edge location.

</details>

## References

- [Choosing AWS migration services and tools](https://docs.aws.amazon.com/decision-guides/latest/migration-on-aws-how-to-choose/migration-on-aws-how-to-choose.html)
- [AWS Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
- [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
- [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [AWS Snow Family](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html)
- [AWS Migration Hub](https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html)
- [CLF-C02 Domain 1: Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html)

Sources checked: **2026-08-01**.
