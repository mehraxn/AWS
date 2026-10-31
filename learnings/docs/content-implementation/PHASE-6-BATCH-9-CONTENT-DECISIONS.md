# Phase 6 Batch 9 Content Decisions

Verification date for all items: **2026-07-25**.

## AWS-048 — Analytics ingestion

### Official requirement

Teach streams and Firehose, batch versus stream processing, destinations, scaling, and cost.

### Required CPP depth

Recognize Kinesis Data Streams for retained streams with custom consumers and Amazon Data Firehose for managed buffered delivery.

### Required SAA depth

Select by consumer control, ordering scope, replay, latency, scaling, failure behavior, security, and cost.

### Canonical target

`14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md`

### Existing files reviewed

The category index, existing Kinesis service notes, S3 material, application-integration comparison, canonical inventory, Phase 4 maps, and Phase 5 audits were reviewed. No equivalent combined canonical lesson existed.

### Official sources used

Amazon Kinesis Data Streams Developer Guide, Amazon Data Firehose Developer Guide, and the AWS analytics decision guide.

### Gap being resolved

The repository lacked one decision-oriented owner that distinguished a replayable stream from buffered managed delivery.

### CPP content added

Service-recognition cues, batch-versus-stream basics, destination awareness, and a knowledge check were added.

### SAA architecture content added

Partition-key ordering, capacity modes, consumer lag, replay, buffering, duplicates, idempotency, destination failure, security, monitoring, and cost trade-offs were added.

### Analytics or AI scenarios added

Independent consumers, managed log delivery, and consumer recovery scenarios were added.

### Security and governance added

Least-privilege IAM, encryption, KMS, private paths, destination roles, sensitive payloads, and CloudWatch monitoring are addressed.

### Existing content preserved

Existing service-specific lessons remain canonical for their narrower subjects and are linked where useful. No legacy or unrelated lesson was rewritten.

### Content removed or corrected

No existing learning content was removed. The new owner uses the current name Amazon Data Firehose and avoids global-ordering, instant-delivery, and indefinite-retention claims.

### Badge decision

CPP and SAA badges are justified by distinct recognition and architecture sections.

### Navigation and map updates

The category and analytics indexes, canonical inventory, certification maps, matrices, dashboards, and repository navigation were updated.

### Acceptance-criteria result

Completed: streams/Firehose, batch/stream, destinations, scaling, cost, current official sources, CPP recognition, and SAA design depth are present.

### Remaining work

None. This item does not block Batch 10.

### Validation result

Passed filename, internal-link, duplicate, badge, terminology, claim, audit-map, and mandatory-record checks. The single Mermaid flowchart was manually reviewed because no Mermaid CLI is installed.

## AWS-049 — Analytics services

### Official requirement

Teach Athena, EMR, Glue, Redshift, OpenSearch Service, and the current Quick Sight BI capability with use cases and trade-offs.

### Required CPP depth

Recognize each service by its primary analytical job.

### Required SAA depth

Select services by storage location, processing model, operational control, latency, governance, failure behavior, performance, and cost.

### Canonical target

`15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md`

### Existing files reviewed

Existing service notes, the EMR-versus-Redshift guide, category indexes, database and S3 material, Phase 4 maps, inventory, and scope audits were reviewed. The new file owns cross-service selection rather than duplicating service detail.

### Official sources used

The AWS analytics decision guide and current official documentation for Athena, Glue, Redshift, EMR, OpenSearch Service, and Amazon Quick.

### Gap being resolved

The repository had individual notes but lacked a coherent analytics selection guide at the authorized path.

### CPP content added

OLTP/OLAP, lake/warehouse, ETL/ELT, batch/stream definitions and concise recognition cues were added.

### SAA architecture content added

Decision tables, lake and warehouse patterns, serverless/provisioned distinctions, security, availability, pipeline recovery, and cost/performance trade-offs were added.

### Analytics or AI scenarios added

Six selection scenarios cover SQL over S3, Spark transformation, managed ETL, BI warehousing, search, and governed data lakes.

### Security and governance added

IAM, KMS, Lake Formation, S3 controls, private networking, CloudTrail, CloudWatch, classification, and cross-team access are addressed.

### Existing content preserved

All detailed service owners and the existing comparison remain intact and are linked.

### Content removed or corrected

No existing learning content was removed. The guide clarifies that S3 alone is not a governed lake, a Glue crawler is not an ETL job, and Quick Sight is a BI layer rather than storage or query execution.

### Badge decision

CPP and SAA badges are justified by the recognition table and architecture scenarios.

### Navigation and map updates

The comparison indexes, canonical inventory, certification maps, service and concept matrices, dashboards, and repository map were updated.

### Acceptance-criteria result

Completed: all six authorized service families, use cases, trade-offs, official sources, CPP recognition, and SAA design depth are present.

### Remaining work

None. DataZone, Clean Rooms, MSK, Flink, and other unselected services were not expanded. This item does not block Batch 10.

### Validation result

Passed filename, internal-link, duplicate, badge, terminology, claim, audit-map, and mandatory-record checks.

## AWS-050 — AI and ML services

### Official requirement

Provide current service purpose and recognition without implementation-course depth.

### Required CPP depth

Recognize AI/ML concepts, Bedrock, SageMaker AI, and purpose-built pretrained services.

### Required SAA depth

Awareness only where applicable; the selected backlog item does not authorize a new SAA architecture course.

### Canonical target

`14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md`

### Existing files reviewed

Existing pretrained-service notes, category navigation, Phase 4 maps, canonical inventory, badge audit, terminology audit, and out-of-scope classifications were reviewed.

### Official sources used

AWS ML decision guidance, Bedrock and SageMaker AI documentation, Bedrock data-protection documentation, and AWS Responsible AI guidance and policy.

### Gap being resolved

The repository lacked a single certification-proportional service-recognition guide using current names and appropriately qualified AI claims.

### CPP content added

AI, ML, deep learning, training, inference, foundation model, LLM, prompt, token, fine-tuning, embeddings, RAG, Bedrock, SageMaker AI, and pretrained-service cues were added.

### SAA architecture content added

No SAA badge was added. Limited selection context explains when Bedrock, SageMaker AI, or a purpose-built service fits.

### Analytics or AI scenarios added

Ten recognition scenarios and a five-question knowledge check were added.

### Security and governance added

IAM, encryption, KMS, data classification, private connectivity qualification, retention review, hallucination, bias, guardrails, evaluation, monitoring, and human oversight are addressed.

### Existing content preserved

Existing service lessons remain the detailed owners and are linked when present.

### Content removed or corrected

No existing learning content was removed. The guide distinguishes Amazon SageMaker AI from the broader Amazon SageMaker platform and explicitly rejects accuracy, perfect-safety, and generalized privacy guarantees.

### Badge decision

CPP only. The selected item requires recognition/awareness and does not justify an SAA badge.

### Navigation and map updates

The category and AI/ML indexes, canonical inventory, CPP map, service matrix, badge audit, terminology audit, and repository navigation were updated.

### Acceptance-criteria result

Completed: purpose and recognition, certification-proportional depth, current naming, responsible-AI limitations, and official sources are present.

### Remaining work

None. Individual unselected AI services and full implementation guidance remain outside this batch. This item does not block Batch 10.

### Validation result

Passed filename, internal-link, duplicate, badge, current-name, AI-claim, privacy-claim, audit-map, and mandatory-record checks.
