# Phase 6 Batch 9 Changelog

## Dependency release

- All seven mandatory Batch 8 records were found and non-empty.
- AWS-044 through AWS-047: 4 completed, 0 partial, 0 blocking.
- Direct dependencies: AWS-006 and AWS-047 are completed.
- Result: Batch 9 may proceed.

## Initial state

- Date: 2026-07-25.
- Branch: `audit/phase5-official-coverage`.
- Commit: `c5b2b62 update`.
- Working tree: dirty with completed, uncommitted Batch 7 and Batch 8 work; all preserved.
- Staged changes: none.
- Batch 9 rows found: 3.
- Selected IDs: AWS-048, AWS-049, AWS-050.
- Priority mix: 0 P0, 0 P1, 2 P2, 1 P3.
- Dependencies: AWS-006 and AWS-047 completed.
- Batch 10 content modified at start: no.

The Batch 9 scope and pre-implementation manifest were created before learning-content changes.

## Analytics foundations

- Added OLTP versus OLAP, data lake versus data warehouse, ETL versus ELT, and batch versus streaming foundations at certification depth in the analytics selection guide.
- Preserved S3, database, and existing detailed analytics owners and linked them rather than duplicating them.

## Query, integration, and governance

- AWS-049 adds Athena and Glue selection, Lake Formation governance awareness, serverless behavior, S3/catalog relationships, IAM, KMS, private access, logging, and cost/performance guidance.
- DataZone and Clean Rooms were not selected and were not expanded.

## Warehousing and big-data processing

- AWS-049 distinguishes Redshift warehousing from Athena query-on-demand and EMR framework processing.
- It covers provisioned/serverless choices, operational control, recovery, workload, and cost trade-offs without creating an administration course.

## Streaming analytics

- AWS-048 creates the authorized Kinesis Data Streams and Amazon Data Firehose owner.
- Added producer/consumer roles, partition-key ordering, capacity choices, replay, buffering, destinations, duplicate handling, idempotency, failure recovery, security, monitoring, and cost.
- Managed Service for Apache Flink, MSK, and Video Streams were not selected for expansion.

## Search and business intelligence

- AWS-049 adds OpenSearch Service and Amazon Quick Sight selection, explains indexed search versus source-of-truth storage, and distinguishes BI visualization from storage/query execution.
- Current Amazon Quick / Amazon Quick Sight terminology was verified on 2026-07-25.

## AI and generative AI

- AWS-050 creates a certification-proportional recognition guide for AI/ML foundations, Bedrock, SageMaker AI, RAG, embeddings, hallucination, responsible AI, privacy, evaluation, guardrails, and human oversight.
- It distinguishes SageMaker AI from the broader next-generation Amazon SageMaker platform and avoids model lists or volatile numeric claims.

## Pretrained AI services

- Added selection cues for Rekognition, Textract, Comprehend, Translate, Transcribe, Polly, Lex, Kendra, and Personalize in the authorized recognition guide.
- Existing detailed service lessons were preserved; missing service-specific lessons were not opportunistically created.

## Other awareness services

No other-awareness-service backlog row was selected.

## Comparison guides

- Created `15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md` for the exact AWS-049 acceptance criterion.
- No unauthorized service-pair comparison was created.

## Navigation and audit updates

- Added analytics and AI/ML local indexes and updated category/comparison indexes, root status, repository map, and implementation index.
- Updated directly affected inventory, CPP/SAA task maps, service/concept matrices, badge audit, depth matrix, architecture-quality audit, terminology audit, out-of-scope audit, and CPP/SAA dashboard deltas.

## Corrections

- Corrected current Data Firehose naming and differentiated its buffered delivery from a replayable stream.
- Qualified ordering, replay, buffering, and duplicate behavior.
- Recorded current Amazon Quick / Quick Sight and SageMaker / SageMaker AI distinctions.
- Added explicit limitations for AI accuracy, RAG, guardrails, privacy generalization, and consequential use.

## Backlog results

- AWS-048: completed; no remaining work; does not block Batch 10.
- AWS-049: completed; no remaining work; does not block Batch 10.
- AWS-050: completed; no remaining work; does not block Batch 10.
- Totals: 3 completed, 0 partially completed, 0 blocked, 0 deferred, 0 manual review.

## Validation

- `python scripts/validate-file-names.py --all`: passed, 384 paths checked after temporary-script cleanup; includes empty-file and duplicate-lesson-number checks.
- `python scripts/validate-markdown-links.py --all`: passed, 326 Markdown files checked.
- `python scripts/detect-duplicate-filenames.py`: passed, 382 files scanned with no candidates.
- `python scripts/generate-repository-report.py`: initial write received a permission error; approved final rerun passed and generated `reports/generated/repository-summary.md` for 383 files.
- Badge and depth review: passed for all three targets; AWS-050 intentionally has CPP only.
- Analytics and AI terminology review: passed; former names appear only in explanatory historical context.
- Unsupported AI accuracy/privacy claim scan: passed with no matches.
- Audit-map and mandatory-record gate: passed for AWS-048, AWS-049, and AWS-050.
- Mermaid: one simple `flowchart LR` reviewed manually; no Mermaid CLI is installed.
- `git diff --check`: passed; only Git line-ending conversion warnings for pre-existing tracked audit files were emitted.
- Broken internal links introduced: 0.
- Duplicate canonical owners introduced: 0.
- Duplicate lesson numbers introduced: 0.
- Empty canonical lessons created: 0.
- Forbidden version filenames created: 0.
- Unsupported AI guarantees introduced: 0.
- Unsupported model-privacy claims introduced: 0.

## Safety confirmation

- Batch 10 items implemented: 0.
- Unrelated canonical lessons rewritten: 0.
- Top-level categories changed: 0.
- Legacy directories recreated: 0.
- Commits created: 0.
- Pushes performed: 0.
