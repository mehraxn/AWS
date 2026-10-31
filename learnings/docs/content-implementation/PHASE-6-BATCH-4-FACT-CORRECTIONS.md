# Phase 6 Batch 4 Fact Corrections

## Multi-AZ is not primarily read scaling

Affected path:

`06-databases/amazon-rds/01-overview.md`

Related backlog ID:

AWS-026

Previous claim:

Distributed or incomplete notes could blur a traditional Multi-AZ standby with a read replica.

Corrected claim:

Traditional RDS Multi-AZ DB instance deployments use a standby primarily for high availability and managed failover; ordinary read replicas use separate endpoints primarily for read scaling and generally replicate asynchronously.

Reason:

The two architectures have different availability, consistency, endpoint, and scaling behavior.

Official source:

Official Amazon RDS Multi-AZ and read replica documentation.

Date checked:

2026-07-23

Severity:

High — directly changes SAA architecture selection.

## RDS Proxy does not cache query results

Affected path:

`06-databases/amazon-rds/01-overview.md`

Related backlog ID:

AWS-026

Previous claim:

Proxying, pooling, read scaling, and caching were not previously separated in a canonical RDS owner.

Corrected claim:

RDS Proxy pools and reuses database connections and can improve failover handling; it is not a query-result cache or read replica.

Reason:

Connection pressure and repeated-query latency require different solutions.

Official source:

Official Amazon RDS Proxy documentation.

Date checked:

2026-07-23

Severity:

High — prevents an incorrect serverless database design.

## DynamoDB index consistency differs

Affected path:

`06-databases/amazon-dynamodb/01-overview.md`

Related backlog ID:

AWS-028

Previous claim:

No canonical lesson distinguished LSI and GSI partition keys, creation timing, capacity, and read consistency.

Corrected claim:

An LSI shares the base partition key, is created with the table, and can support strong reads. A GSI can use a different partition key, can be added later, has separate capacity behavior, and supports eventual reads.

Reason:

Index choice changes access patterns, consistency, throughput, and cost.

Official source:

Official DynamoDB secondary-index and consistency documentation.

Date checked:

2026-07-23

Severity:

High — affects DynamoDB data-model decisions.

## ElastiCache engine and failover terminology

Affected path:

`06-databases/amazon-elasticache/01-overview.md`

Related backlog ID:

AWS-029

Previous claim:

The existing overview listed engines but did not fully distinguish current names or Memcached availability behavior.

Corrected claim:

Use ElastiCache for Valkey, ElastiCache for Redis OSS, and ElastiCache for Memcached. Multi-AZ automatic failover applies to appropriately configured Valkey/Redis OSS replication groups, not Memcached.

Reason:

Engine choice determines replication, failover, persistence, and client failure handling.

Official source:

Official Amazon ElastiCache engine and Multi-AZ documentation.

Date checked:

2026-07-23

Severity:

High — affects cache availability design.
