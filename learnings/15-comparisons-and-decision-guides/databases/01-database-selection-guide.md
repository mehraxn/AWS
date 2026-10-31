# AWS Database and Cache Selection Guide

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Start with the Workload

Choose a data service from its data model, access patterns, transactions/consistency, latency, availability, scaling, recovery, security, operational effort, and cost—not from a single performance slogan.

Relational databases organize structured data with schemas, rows, keys, joins, and ACID transactions. NoSQL databases optimize particular access models such as key-value, document, graph, or time series. In-memory caches keep hot or temporary data close to applications. Data warehouses optimize analytical (OLAP) queries rather than ordinary transactional (OLTP) application traffic.

## Core Decision Table

| Service | Primary purpose | Data/query model | Availability and durability | Scaling | Choose when |
|---|---|---|---|---|---|
| Amazon RDS | Managed relational database | SQL and supported engines | Backups/PITR; Multi-AZ options | Vertical/storage scaling; read replicas | Existing engine compatibility, SQL, joins, transactions |
| Amazon Aurora | AWS-designed relational database | MySQL/PostgreSQL-compatible SQL | Multi-AZ cluster storage; replicas; Global Database option | Reader scaling; provisioned or Serverless v2 compute | Cloud-oriented relational HA/read scale or Aurora global/serverless needs |
| Amazon DynamoDB | Serverless NoSQL database | Key-value/document; key-based APIs | Multi-AZ Regional service; PITR/backups; Global Tables | Horizontal by partition design; on-demand/provisioned | Known access patterns, key-value/document scale, serverless operations |
| Amazon ElastiCache | General-purpose in-memory cache | Valkey/Redis OSS structures or Memcached key-values | Depends on engine/topology; cache must tolerate loss | Nodes, replicas, shards, or supported serverless choices | Sessions, hot data, repeated database reads, rich cache structures |
| DAX | DynamoDB-specific in-memory cache | DynamoDB-compatible API | Cache cluster in front of DynamoDB | Cache nodes/clusters | Eligible eventually consistent DynamoDB reads need lower latency |
| Amazon Redshift | Analytics warehouse | SQL over analytical data | Warehouse recovery/HA features | Analytical compute/storage architecture | OLAP and warehouse analytics, not primary OLTP ownership |

## Important Comparisons

### RDS versus Aurora

Use RDS for supported standard-engine compatibility and engine-specific requirements. Use Aurora when MySQL/PostgreSQL compatibility plus Aurora cluster storage, endpoints, replicas, Serverless v2, or Global Database better fits. Aurora is part of the RDS service family but is not identical to standard RDS engines.

### RDS Multi-AZ versus Read Replica versus Backup versus Cache

| Need | Choice |
|---|---|
| Automatic database failover | Multi-AZ |
| More read-query capacity | Read replica |
| Recover an earlier state | Backup, snapshot, or PITR |
| Avoid repeated reads at very low latency | Cache |

These controls complement one another; none universally replaces the others.

### RDS/Aurora versus DynamoDB

Choose relational services for joins, relational constraints, SQL compatibility, and transactional schemas. Choose DynamoDB when key-based access patterns, NoSQL data, horizontal partitioning, and serverless operations dominate. Do not select DynamoDB merely because the workload is large or Aurora merely because the workload is important.

### DynamoDB Capacity and Indexes

- **On-demand:** variable/unpredictable traffic and low capacity-management effort.
- **Provisioned:** predictable traffic and deliberate capacity/cost control.
- **LSI:** same partition key, alternate sort key, created with table, optional strong reads.
- **GSI:** alternate partition key, can be added later, eventual reads, separate capacity behavior.

### ElastiCache versus DAX

Choose DAX for DynamoDB-compatible acceleration of eligible reads. Choose ElastiCache for general application caching, sessions, custom structures, or multiple systems of record. Neither is durable primary storage in normal designs.

### Valkey/Redis OSS versus Memcached

Choose Valkey or Redis OSS when replication, Multi-AZ failover, richer structures, or supported persistence features matter. Choose Memcached for a simple distributed, rebuildable key-value cache where independent-node behavior is acceptable.

## Availability, Consistency, and Recovery

- High availability is not backup; replicas can copy corruption or accidental writes.
- Asynchronous replicas can lag. Decide whether a read can tolerate stale data.
- Caches can be stale, evicted, or lost. The application needs a correct miss path.
- Multi-Region replication adds routing, conflict/consistency, security, transfer cost, failover, RTO/RPO, and failback decisions.
- Restores usually create new resources, so recovery procedures require application and DNS planning.

## Security and Cost

Use private placement where appropriate, restrictive security groups, least-privilege IAM, database users/roles, Secrets Manager, AWS KMS, TLS, logging, and protected backups. Managed services reduce infrastructure operations but do not transfer data governance or application security to AWS.

Compare total architecture cost: compute/capacity, storage, I/O/requests, replicas, Multi-AZ/Multi-Region resources, backups, transfer, proxy/cache nodes, licenses, and operational labor. There is no universally cheapest database.

## CPP Recognition

- **RDS:** managed relational engines.
- **Aurora:** AWS-designed MySQL/PostgreSQL-compatible relational cluster.
- **DynamoDB:** serverless key-value/document NoSQL database.
- **ElastiCache:** general-purpose in-memory cache.
- **DAX:** DynamoDB-compatible cache.
- **Redshift:** analytics warehouse.

## SAA Scenarios

1. **Traditional SQL application requiring Oracle compatibility:** evaluate RDS for Oracle, not Aurora.
2. **MySQL-compatible global relational application:** evaluate Aurora Global Database with recovery/routing design.
3. **Serverless shopping cart with known key access and variable volume:** evaluate DynamoDB on-demand.
4. **Repeated catalog reads overload a relational writer:** add cache-aside ElastiCache; consider replicas for query/report workloads.
5. **Eventually consistent DynamoDB reads need API-compatible acceleration:** evaluate DAX.
6. **Large analytical scans and aggregations:** evaluate Redshift rather than using an OLTP database as a warehouse.

## Common Traps

- Selecting by “fastest” without the data model or access pattern.
- Treating Multi-AZ, read replicas, backups, and caches as interchangeable.
- Treating replication as recovery from logical corruption.
- Assuming a managed service removes customer security responsibility.
- Creating a duplicate Redshift owner under databases.

## Knowledge Check

1. Which service best matches a managed standard relational engine?
2. Which option is a DynamoDB-compatible cache?
3. What primarily distinguishes Multi-AZ from read replicas?
4. When is a GSI more flexible than an LSI?
5. Which service is primarily an OLAP warehouse?

<details><summary>Answers</summary>

1. Amazon RDS.
2. DAX.
3. Multi-AZ targets availability/failover; read replicas target read scaling.
4. When the access pattern needs a different partition key or an index added after table creation.
5. Amazon Redshift.

</details>

## Canonical Lessons

- [Amazon RDS](../../06-databases/amazon-rds/01-overview.md)
- [Amazon Aurora](../../06-databases/amazon-aurora/01-overview.md)
- [Amazon DynamoDB](../../06-databases/amazon-dynamodb/01-overview.md)
- [Amazon ElastiCache](../../06-databases/amazon-elasticache/01-overview.md)
- [Amazon Redshift](../../14-ai-ml-analytics-and-other-services/analytics/amazon-redshift/01-overview.md)

## References

Checked 2026-07-23.

- [Amazon RDS documentation](https://docs.aws.amazon.com/rds/)
- [Amazon Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
- [Amazon DynamoDB documentation](https://docs.aws.amazon.com/dynamodb/)
- [Amazon ElastiCache documentation](https://docs.aws.amazon.com/elasticache/)
- [AWS database services](https://aws.amazon.com/products/databases/)
