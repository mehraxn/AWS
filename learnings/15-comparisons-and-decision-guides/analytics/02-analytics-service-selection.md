# AWS Analytics Service Selection

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Choose an analytics service by identifying the job: query files, integrate data, run distributed frameworks, maintain a warehouse, search indexed documents, or publish business dashboards. These services often form one pipeline rather than replacing one another.

## Analytics Foundations

- **OLTP** supports frequent application transactions, small reads and writes, and current operational state. Amazon RDS and DynamoDB are common operational stores.
- **OLAP** scans and aggregates historical data for analysis. Amazon Redshift is an analytical warehouse.
- A **data lake** stores raw and curated structured, semi-structured, and unstructured data, commonly in Amazon S3. Governance, metadata, formats, partitions, and permissions turn stored objects into usable analytical data.
- A **data warehouse** organizes analytical data for repeatable SQL reporting and business intelligence.
- **ETL** transforms before loading into the target; **ELT** loads first and transforms using the target's processing capability.
- **Batch** processes bounded data on a schedule. **Streaming** continuously ingests events when lower latency is required.

## Decision Table

| Service | Primary job | Processing model | Choose it when |
|---|---|---|---|
| Amazon Athena | Serverless interactive SQL over data, commonly in S3 | Query on demand | Analysts need SQL without managing warehouse infrastructure |
| AWS Glue | Serverless data integration and metadata catalog | ETL/ELT jobs, crawlers, catalog | Data must be discovered, cataloged, prepared, moved, or transformed |
| Amazon Redshift | Managed cloud data warehouse | Provisioned or serverless SQL analytics | Repeated OLAP, governed warehouse data, BI concurrency, and warehouse performance matter |
| Amazon EMR | Managed big-data framework platform | Clusters, Serverless, or other deployment choices | Spark, Hadoop, Hive, Trino, or flexible distributed processing is required |
| Amazon OpenSearch Service | Managed search and analytics engine | Indexed search and aggregations; domains or Serverless | Full-text search, application search, log analytics, or operational investigation is required |
| Amazon Quick Sight | Business intelligence within Amazon Quick | Serverless dashboards and visualization | People need interactive analyses, reports, embedded analytics, or dashboards |

Amazon QuickSight was rebranded in 2025. Current AWS documentation calls the broader service **Amazon Quick** and its BI capability **Amazon Quick Sight**. Existing APIs and repository paths may still contain `quicksight`.

## Amazon Athena

Athena is a serverless interactive query service. It can use the AWS Glue Data Catalog for table metadata and schema-on-read definitions, execute SQL over data in S3, and write query results to a configured S3 location.

Choose Athena for ad hoc analysis and infrequent queries where managing warehouse compute is unnecessary. Query cost is driven conceptually by data scanned, so partition data, compress it, use columnar formats such as Parquet or ORC, select required columns, and avoid repeatedly scanning irrelevant files.

Athena is not an OLTP database and does not move or transform data merely because a table exists in the catalog.

## AWS Glue

AWS Glue is a serverless data integration service. The Glue Data Catalog stores metadata about datasets; it is not an application database and does not contain the underlying S3 objects. Crawlers can inspect sources and infer metadata. ETL jobs perform transformations, while triggers and workflows coordinate work.

Choose Glue when the requirement is discovery, cataloging, data preparation, managed ETL/ELT, or integration across sources and targets. Choose EMR when the workload needs deeper control of big-data frameworks, versions, cluster behavior, or processing environments.

AWS Lake Formation can add centralized, fine-grained data-lake permissions over cataloged resources and registered data locations. It complements rather than replaces S3, Glue, Athena, or Redshift.

## Amazon Redshift

Amazon Redshift is a managed cloud data warehouse designed for analytical SQL and BI workloads. It uses column-oriented analytical techniques and parallel processing. Customers can choose provisioned data warehouses or Amazon Redshift Serverless.

Choose Redshift for repeated analytical queries, modeled warehouse data, many BI users, or performance that benefits from a managed warehouse. Redshift Spectrum and current data-lake integrations can query external data, but Redshift remains distinct from Athena's direct serverless query-on-demand model.

Design considerations include workload isolation, distribution and sort strategy awareness, snapshots or recovery behavior, encryption, network access, monitoring, and the cost difference between provisioned and serverless capacity.

## Amazon EMR

Amazon EMR runs managed big-data frameworks such as Apache Spark and Hadoop. It is a processing platform rather than a warehouse. Choose it for flexible distributed transformations, large-scale batch processing, custom Spark code, or open-source ecosystem requirements.

EMR on EC2 provides cluster-level choices and operational control. EMR Serverless reduces infrastructure management for supported application frameworks. The decision balances control, startup and runtime behavior, team skills, software compatibility, scaling, and cost.

## Amazon OpenSearch Service

OpenSearch Service supports full-text search, application search, log analytics, observability, and indexed aggregations. A managed domain uses provisioned cluster resources; OpenSearch Serverless uses collections and separates infrastructure management from the customer.

Choose OpenSearch when searches depend on relevance, free-text fields, indexed documents, or rapid operational investigation. It is not a general replacement for Redshift's warehouse SQL, Athena's S3 querying, or CloudWatch Logs Insights' focused investigation of CloudWatch log groups.

## Amazon Quick Sight

Amazon Quick Sight is the BI capability within Amazon Quick. It connects to data sources and turns datasets into analyses, dashboards, reports, and embedded visualizations. It is a presentation and exploration layer, not the pipeline that ingests, catalogs, or warehouses the source data.

Choose it when the consumer is a business user who needs governed dashboards or interactive visualization. Ensure source permissions, row- or column-level access where required, refresh behavior, and dashboard sharing are designed deliberately.

## Common Architecture Patterns

### S3 data lake and ad hoc SQL

Sources deliver data to S3, Glue maintains metadata, Lake Formation can govern access, Athena runs SQL, and Quick Sight visualizes curated results.

### Managed warehouse and BI

Glue prepares data, Redshift stores and serves repeatable analytical models, and Quick Sight publishes dashboards. This pattern trades warehouse cost for predictable analytical capability and concurrency.

### Searchable operational logs

Data Firehose or OpenSearch Ingestion delivers records to OpenSearch. OpenSearch indexes them for search and operational analytics. Preserve an S3 copy when long-term retention, replay, or reprocessing is required.

### Flexible big-data transformation

EMR processes raw S3 datasets with Spark, writes curated output back to S3, and Athena or Redshift exposes results to analysts.

## Security and Governance

- Apply least-privilege IAM roles to jobs, query engines, warehouse access, dashboards, and delivery services.
- Encrypt data at rest and in transit; define AWS KMS key permissions as part of access design.
- Use Lake Formation when centralized fine-grained data-lake permissions are required, while retaining IAM and S3 controls.
- Keep private resources in appropriate VPC paths and control security groups, endpoints, and egress.
- Log administrative activity with CloudTrail and monitor workload health, failures, and costs with CloudWatch and cost tools.
- Classify data before indexing, sharing dashboards, or making catalog resources available across accounts.

## Availability, Scaling, and Failure Behavior

Serverless does not mean failure-free. Athena queries can fail because of invalid metadata or source data. Glue jobs can fail partway through a transformation. EMR applications can fail because of code or capacity. Redshift and OpenSearch still require workload, recovery, and capacity decisions. Quick Sight depends on accessible, refreshed datasets.

Use idempotent pipeline stages, preserve source data, isolate corrupt records, monitor retries, and maintain a recovery path. Choose Multi-AZ or serverless capabilities based on documented service behavior and workload requirements rather than assuming every analytics service has the same availability boundary.

## Cost and Performance Trade-offs

- Athena rewards efficient file layout, partitions, compression, and columnar formats.
- Glue and EMR costs reflect processing resources and runtime; inefficient transformations consume more capacity.
- Redshift trades managed warehouse capacity for repeatable performance and BI concurrency.
- OpenSearch costs include indexing/search compute and storage; excessive indexes, replicas, or retention can raise cost.
- Quick Sight adds author, reader, capacity, or feature costs according to the current offering.
- Data transfer and duplicate storage across the pipeline can be material.

## CPP Recognition

- SQL over S3 without managing a warehouse: Athena.
- Discover, catalog, and transform data: Glue.
- Analytical data warehouse: Redshift.
- Spark/Hadoop processing: EMR.
- Full-text and log search: OpenSearch Service.
- BI dashboards: Quick Sight.

## SAA Scenarios

1. **Infrequent SQL over partitioned S3 logs:** Athena, with Glue Data Catalog metadata.
2. **Nightly Spark transformation needing framework control:** EMR.
3. **Managed ETL with crawlers and a shared catalog:** Glue.
4. **Recurring executive dashboards over modeled historical data:** Redshift plus Quick Sight.
5. **Product catalog relevance search:** OpenSearch Service.
6. **Governed cross-team data lake:** S3, Glue Data Catalog, and Lake Formation, with Athena or Redshift as query consumers.

## Common Mistakes

- A Glue crawler catalogs data; it does not perform the ETL job.
- Quick Sight visualizes data; it is not a warehouse.
- Athena queries data; it does not automatically optimize a poor S3 layout.
- EMR and Redshift can both analyze large data, but one is a framework platform and the other is a warehouse.
- S3 alone is object storage, not a governed data lake architecture.
- OpenSearch is not the default choice for every analytical SQL workload.

## Knowledge Check

1. Which service runs serverless SQL over cataloged S3 data?
2. When would EMR be a better fit than Glue?
3. Why does Quick Sight not replace Redshift or Athena?
4. Which services work together to govern and query an S3 data lake?
5. What requirement makes OpenSearch more suitable than a data warehouse?

## Canonical Links

- [Amazon Athena](../../14-ai-ml-analytics-and-other-services/analytics/amazon-athena/01-overview.md)
- [AWS Glue](../../14-ai-ml-analytics-and-other-services/analytics/aws-glue/01-overview.md)
- [Amazon Redshift](../../14-ai-ml-analytics-and-other-services/analytics/amazon-redshift/01-overview.md)
- [Amazon EMR](../../14-ai-ml-analytics-and-other-services/analytics/amazon-emr/01-overview.md)
- [Amazon Quick Sight](../../14-ai-ml-analytics-and-other-services/analytics/amazon-quicksight/01-overview.md)
- [Kinesis Data Streams and Data Firehose](../../14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md)
- [EMR vs Redshift](01-emr-vs-redshift.md)
- [Data-transfer cost architecture](../../12-billing-pricing-and-support/aws-billing-and-cost-management/03-data-transfer-costs.md)

## References

Checked **2026-07-25**.

- [Choosing an AWS analytics service](https://docs.aws.amazon.com/decision-guides/latest/analytics-on-aws-how-to-choose/analytics-on-aws-how-to-choose.html)
- [Amazon Athena tables, databases, and Data Catalog](https://docs.aws.amazon.com/athena/latest/ug/understanding-tables-databases-and-the-data-catalog.html)
- [What is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Amazon Redshift Serverless and provisioned comparison](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-comparison.html)
- [What is Amazon EMR?](https://docs.aws.amazon.com/emr/latest/ManagementGuide/)
- [What is Amazon OpenSearch Service?](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
- [What is Amazon Quick?](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html)
