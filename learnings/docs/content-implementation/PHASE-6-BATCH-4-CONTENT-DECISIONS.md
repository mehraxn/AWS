# Phase 6 Batch 4 Content Decisions

Checked: 2026-07-23

## AWS-026 — Amazon RDS

### Official requirement

Managed relational database coverage including engines, HA, read scale, recovery, connections, security, monitoring, and cost.

### Canonical target

06-databases/amazon-rds/01-overview.md

### Existing files reviewed

Database index, Aurora lessons, TLS/RDS pattern, service index, Phase 4 maps, and Phase 5 inventory.

### Official sources used

RDS User Guide for engines, backups, Multi-AZ, read replicas, and RDS Proxy; pricing; checked 2026-07-23.

### Gap being resolved

The authorized RDS foundation did not exist.

### CPP content added

Managed relational purpose, engines, responsibilities, pricing factors, backups, and recognition.

### SAA content added

Placement, scaling, Multi-AZ, replicas, PITR/snapshots, RDS Proxy, security, failure, RTO/RPO, and cost.

### Database scenarios or comparisons added

Multi-AZ/read replica/backup/cache decisions; Lambda connection storm and AZ-failure scenarios.

### Existing content preserved

Existing Aurora and TLS material remains canonical and is linked.

### Content removed or corrected

No useful content removed; Multi-AZ, replica, restore, and proxy distinctions made explicit.

### Badge decision

CPP and SAA badges added for substantive dual-depth coverage.

### Remaining work

None for this criterion.

### Validation result

Passed: target structure, badges, official references, scenarios, questions, filenames, links, and acceptance criterion verified.

## AWS-027 — Amazon Aurora

### Official requirement

Scenario-ready Aurora cluster storage, replicas, failover, global/serverless, and cost coverage.

### Canonical target

06-databases/amazon-aurora/01-overview.md

### Existing files reviewed

All three Aurora lessons, Aurora README, RDS material, maps, inventory, and comparison index.

### Official sources used

Aurora overview, storage, endpoint, Serverless v2, Global Database, and pricing docs; checked 2026-07-23.

### Gap being resolved

Existing overview lacked complete endpoint, failure, Serverless v2, Global Database, security, and cost design.

### CPP content added

Aurora relational identity, compatibility, managed benefits, reader and global recognition.

### SAA content added

Writer/readers/endpoints, failover, provisioned/serverless choice, Global Database, backup, security, RTO/RPO, and cost.

### Database scenarios or comparisons added

Writer versus reader routing; variable workload; global relational DR and read scenarios.

### Existing content preserved

Original overview and provisioned/serverless lessons were retained.

### Content removed or corrected

No useful content removed; unsupported universal performance claims avoided and current Serverless v2 context added.

### Badge decision

CPP and SAA badges added to the authorized supplement.

### Remaining work

None for this criterion.

### Validation result

Passed: target structure, badges, official references, scenarios, questions, filenames, links, and acceptance criterion verified.

## AWS-028 — Amazon DynamoDB

### Official requirement

NoSQL design coverage for keys, capacity, indexes, consistency, global tables, streams, DAX, and cost.

### Canonical target

06-databases/amazon-dynamodb/01-overview.md

### Existing files reviewed

Database index, ElastiCache, VPC endpoint lesson, maps, inventory, and database-related cross-references.

### Official sources used

DynamoDB core, consistency, capacity, index, Streams/TTL, backup, Global Tables, DAX, security, and pricing docs; checked 2026-07-23.

### Gap being resolved

The authorized DynamoDB canonical lesson did not exist.

### CPP content added

Managed NoSQL purpose, key-value/document model, capacity recognition, DAX, Global Tables, and pricing.

### SAA content added

Access-pattern keys, hot partitions, Query/Scan, consistency, transactions, LSI/GSI, events, PITR, multi-Region, security, and cost.

### Database scenarios or comparisons added

On-demand/provisioned, LSI/GSI, DAX/ElastiCache, hot-key, and global-table scenarios.

### Existing content preserved

Existing endpoint and cache lessons remain canonical and are linked.

### Content removed or corrected

No useful content removed; strong-read, index, TTL, and replication/backup distinctions made explicit.

### Badge decision

CPP and SAA badges added for substantive recognition and architecture depth.

### Remaining work

None for this criterion.

### Validation result

Passed: target structure, badges, official references, scenarios, questions, filenames, links, and acceptance criterion verified.

## AWS-029 — Amazon ElastiCache

### Official requirement

Raise cache selection and failure content to scenario-ready depth.

### Canonical target

06-databases/amazon-elasticache/01-overview.md

### Existing files reviewed

Complete existing ElastiCache overview, DynamoDB/DAX material, maps, inventory, and database index.

### Official sources used

ElastiCache overview, strategies, Multi-AZ, security, pricing, and DAX docs; checked 2026-07-23.

### Gap being resolved

Existing note was strong for CPP but shallow on engines, patterns, invalidation, eviction, HA, failure, security, and cost.

### CPP content added

Current Valkey/Redis OSS/Memcached recognition, cache purpose, pricing factors, and common confusion.

### SAA content added

Cache-aside/write-through, TTL/eviction/stampede, replication/Multi-AZ, Memcached failure, security, monitoring, DAX choice, and cost.

### Database scenarios or comparisons added

RDS hot-read cache, session HA, rebuildable Memcached, DAX, and freshness scenarios.

### Existing content preserved

The complete beginner-friendly overview was preserved.

### Content removed or corrected

No useful content removed; current engine terminology and Memcached/Multi-AZ behavior clarified.

### Badge decision

CPP and SAA badges added to the authorized supplement.

### Remaining work

None for this criterion.

### Validation result

Passed: target structure, badges, official references, scenarios, questions, filenames, links, and acceptance criterion verified.

## AWS-030 — Database selection guide

### Official requirement

Compare RDS, Aurora, DynamoDB, and ElastiCache by data model, scaling, HA, and cost.

### Canonical target

15-comparisons-and-decision-guides/databases/01-database-selection-guide.md

### Existing files reviewed

All selected Batch 4 targets, Redshift owner, comparison index, maps, inventory, and architecture links.

### Official sources used

Official RDS, Aurora, DynamoDB, ElastiCache, DAX, Redshift, and AWS database-family docs; checked 2026-07-23.

### Gap being resolved

No canonical database decision guide or database comparison index existed.

### CPP content added

Relational/NoSQL/cache/warehouse recognition and commonly confused services.

### SAA content added

Data/access model, consistency, availability, durability, scaling, recovery, security, operations, performance, cost, and trade-offs.

### Database scenarios or comparisons added

RDS/Aurora/DynamoDB/ElastiCache/DAX/Redshift; Multi-AZ/replica/backup/cache; capacity/index/engine selections.

### Existing content preserved

Canonical service owners are linked and not copied wholesale; Redshift remains under analytics.

### Content removed or corrected

No learning owner removed or relocated; selection distinctions consolidated into one authorized guide.

### Badge decision

CPP and SAA badges added; SAA is primary but CPP awareness is meaningful.

### Remaining work

Later specialized comparisons remain outside this acceptance criterion.

### Validation result

Passed: target structure, badges, official references, scenarios, questions, filenames, links, and acceptance criterion verified.
