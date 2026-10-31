# Phase 6 Batch 5 Changelog

## Dependency release

- Date: 2026-07-23.
- Phase 5 authority and Batch 4 implementation records: present and non-empty.
- AWS-026 through AWS-030: 5 completed, 0 blocking.
- AWS-010 Lambda dependency: completed and non-blocking.
- Result: Batch 5 may proceed.

## Initial state

- Branch: `audit/phase5-official-coverage`.
- Commit: `502acf2 update`.
- Working tree: clean; staged changes: none; pre-existing changes: none.
- Selected authority rows: AWS-031 through AWS-034; 4 P1, 0 P0/P2.
- Blockers: 0.
- Batch 6 or later learning content modified: no.

Scope and pre-implementation records were created before learning edits.

## AWS-031 implementation

- Created the canonical SQS vs SNS vs EventBridge decision guide.
- Covered queue, topic, and event-bus selection; delivery and ordering semantics; retries, dead-letter queues, fanout, failure isolation, security, cost drivers, scenarios, and exam traps.

## AWS-032 implementation

- Created the canonical Amazon EventBridge lesson.
- Covered event buses, rules, targets, schemas, retries, dead-letter queues, archive and replay, Scheduler, security, cost, and architecture scenarios.

## AWS-033 implementation

- Created the canonical AWS Step Functions lesson.
- Covered workflow types, state-machine concepts, service integrations, Retry and Catch, orchestration patterns, execution semantics, security, operations, cost, and scenarios.

## AWS-034 implementation

- Preserved the existing Amazon API Gateway lesson and appended a Batch 5 architecture supplement.
- Added REST, HTTP, and WebSocket API decisions; endpoint types; integrations; authentication and authorization; throttling; caching; resilience; security; cost; and scenarios.

## Navigation and audit updates

- Updated the root status, category and comparison indexes, repository map, and service index.
- Updated the canonical inventory, service-scope matrix, CPP and SAA task maps, technologies-and-concepts matrix, depth matrix, coverage dashboards, and badge audit for affected Batch 5 evidence only.

## Corrections

- Scoped delivery guarantees by service and configuration instead of claiming universal exactly-once delivery.
- Distinguished current EventBridge Scheduler guidance from legacy scheduled-rule behavior.
- Distinguished Step Functions workflow execution semantics from downstream side-effect idempotency.
- Removed implied feature parity among API Gateway REST, HTTP, and WebSocket APIs.

## Backlog results

- Selected: 4; completed: 4; blocked: 0; deferred within Batch 5: 0.
- Priority mix: P0 0, P1 4, P2 0.
- AWS-031 through AWS-034 are recorded as completed; Batch 6 and later rows remain unchanged.

## Validation

- Filename validation: passed; 337 paths checked.
- Internal-link validation: passed; 291 Markdown files checked.
- Duplicate detection: passed; 335 files checked and no candidates found.
- Lesson-number validation: passed; 0 duplicate numbers.
- Empty-file validation: passed; 0 empty Markdown files.
- Badge review: passed for all four selected targets.
- Official-reference review: passed; each selected target has current official AWS references checked 2026-07-23.
- Map and dashboard review: passed for inventory, CPP/SAA maps, service and technology matrices, depth matrix, badge audit, and dashboards.
- Mandatory completion gate: passed; all eight records exist and are non-empty, and AWS-031 through AWS-034 reconcile across scope, manifests, and cumulative status.
- `git diff --check`: passed; line-ending conversion warnings are informational.

## Safety confirmation

- Batch 6 items implemented: 0.
- Batch 7–10 items implemented: 0.
- Unrelated canonical lessons rewritten: 0.
- Top-level categories changed: 0.
- Legacy directories recreated: 0.
- Commits created: 0.
- Pushes performed: 0.
