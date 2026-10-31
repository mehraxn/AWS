# Phase 6 Batch 9 Coverage Delta

Checked: **2026-07-25**.

## Scope

Batch 9 selected exactly three authoritative backlog rows: AWS-048, AWS-049, and AWS-050. This is an affected-requirement reconciliation, not a whole-repository rescore. Batch 10 and unselected awareness services remain untouched.

## CPP delta

| Requirement | Before | After | Evidence |
|---|---|---|---|
| CPP-3.7-01 — streaming ingestion recognition | missing/fragmented | complete, fundamental | `14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md` |
| CPP-3.7-02 — analytics service selection | missing/fragmented | complete, fundamental | `15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md` |
| CPP-3.7-03 — AI/ML service recognition | missing/fragmented | complete, fundamental | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md` |
| CPP-3.7-04 — generative-AI and responsible-use awareness | partial | complete, fundamental | `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md` |

Resolved CPP requirements: **4**. Partially improved: **0**. No unrelated dashboard baseline was rescored.

## SAA delta

| Requirement | Before | After | Evidence |
|---|---|---|---|
| SAA-3.5-01 — data-ingestion selection | partial | complete, architecture-and-design | Kinesis/Data Firehose lesson |
| SAA-3.5-02 — analytics storage/query selection | partial | complete, architecture-and-design | analytics selection guide |
| SAA-3.5-03 — data integration and processing | partial | complete, architecture-and-design | analytics selection guide |
| SAA-3.5-04 — streaming behavior and recovery | partial | complete, architecture-and-design | Kinesis/Data Firehose lesson |
| SAA-3.5-06 — analytical security and governance | partial | complete, architecture-and-design | both analytics targets |
| SAA-3.5-07 — analytics cost/performance trade-offs | partial | complete, architecture-and-design | both analytics targets |

Resolved SAA requirements: **6**. AWS-050 remains intentionally CPP-badged awareness content and did not inflate SAA architecture scoring.

## Service and concept coverage

- Added a canonical combined decision owner for Kinesis Data Streams and Amazon Data Firehose.
- Added a canonical comparison owner for Athena, Glue, Redshift, EMR, OpenSearch Service, and Amazon Quick Sight selection.
- Added a canonical CPP recognition owner for Bedrock, SageMaker AI, and selected pretrained AI-service cues.
- Added complete coverage evidence for streaming and batch ingestion while preserving supplementary classifications.

## Badge and depth result

- AWS-048: CPP and SAA, justified by recognition plus architecture/design depth.
- AWS-049: CPP and SAA, justified by recognition plus architecture/design depth.
- AWS-050: CPP only; SAA badge intentionally withheld.

## Remaining gaps

Unselected analytics, AI/ML, awareness, migration, hybrid-cloud, and final-exam work remains governed by the backlog. No remaining Batch 9 item blocks Batch 10.
