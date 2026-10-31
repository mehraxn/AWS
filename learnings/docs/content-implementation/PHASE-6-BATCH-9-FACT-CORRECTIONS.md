# Phase 6 Batch 9 Fact Corrections

## Correction 1 — Current Data Firehose name and role

Affected path: `14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md`

Related backlog ID: AWS-048

Previous claim: No canonical combined target existed; older repository naming could suggest that Kinesis Data Firehose remained the current name or that Firehose was equivalent to a replayable stream.

Corrected claim: The current product name is **Amazon Data Firehose**. It buffers and delivers streaming records to supported destinations; it is not a general replayable event log equivalent to Kinesis Data Streams.

Reason: AWS renamed the service, and the distinction is material to certification service selection.

Official source: [What is Amazon Data Firehose?](https://docs.aws.amazon.com/firehose/latest/dev/)

Date checked: 2026-07-25

Severity: high

## Correction 2 — Ordering, replay, and delivery guarantees

Affected path: `14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md`

Related backlog ID: AWS-048

Previous claim: The missing owner left ordering scope, replay, buffering, and duplicate behavior unclear.

Corrected claim: Kinesis Data Streams ordering applies within a shard for records routed by partition key; replay is limited to retained records. Data Firehose buffers delivery, retries according to destination behavior, and downstream systems must not assume duplicates are impossible.

Reason: Global ordering, immediate delivery, indefinite replay, and exactly-once assumptions would produce unsafe designs.

Official source: [Kinesis Data Streams concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html); [Data delivery in Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html)

Date checked: 2026-07-25

Severity: high

## Correction 3 — Current business-intelligence terminology

Affected path: `15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md`

Related backlog ID: AWS-049

Previous claim: Existing paths and older notes use Amazon QuickSight without explaining the 2025 product change.

Corrected claim: Current documentation presents **Amazon Quick** as the broader service and **Amazon Quick Sight** as its business-intelligence capability. Existing `amazon-quicksight` paths are retained for link stability pending separately authorized migration work.

Reason: The new guide must use current terminology without creating duplicate owners or renaming unrelated content.

Official source: [What is Amazon Quick?](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html)

Date checked: 2026-07-25

Severity: medium

## Correction 4 — SageMaker product distinction

Affected path: `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md`

Related backlog ID: AWS-050

Previous claim: Using “Amazon SageMaker” alone can conflate the renamed ML service with the broader next-generation SageMaker platform.

Corrected claim: **Amazon SageMaker AI** is the managed service for building, training, and deploying ML models; **Amazon SageMaker** is also the name of the broader next-generation data, analytics, and AI platform.

Reason: Current product naming materially affects service recognition.

Official source: [What is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html); [What is Amazon SageMaker?](https://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/what-is-sagemaker.html)

Date checked: 2026-07-25

Severity: high

## Correction 5 — AI accuracy, guardrails, RAG, and privacy

Affected path: `14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md`

Related backlog ID: AWS-050

Previous claim: The repository lacked a selected canonical guide that explicitly qualified generative-AI accuracy, RAG, guardrails, and service-specific data-protection statements.

Corrected claim: Foundation-model output can be incorrect; RAG does not guarantee truth; guardrails do not guarantee perfect safety; consequential uses require evaluation, safeguards, testing, and appropriate human oversight. Bedrock-specific data-protection statements are not generalized to every AWS AI service or configuration.

Reason: Unsupported accuracy, safety, and privacy guarantees are technically unsafe and outside official guidance.

Official source: [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html); [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/)

Date checked: 2026-07-25

Severity: high

No exact prices, unsupported quotas, fixed model lists, accuracy percentages, context limits, latency guarantees, or generalized privacy guarantees were introduced.
