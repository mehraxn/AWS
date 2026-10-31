# Phase 6 Batch 8 Changelog

## Dependency release

- All seven mandatory Batch 7 records were found and non-empty.
- AWS-040 through AWS-043: 4 completed, 0 partial, 0 blocking.
- Direct Batch 8 dependency: AWS-006 for AWS-045 was completed in Batch 1; no dependency remained blocking.
- Result: Batch 8 may proceed.

## Initial state

- Date: 2026-07-25.
- Branch: `audit/phase5-official-coverage`.
- Commit: `c5b2b62 update`.
- Working tree: dirty with the completed, uncommitted Batch 7 implementation.
- Staged changes: none.
- Existing changes: 14 tracked files modified and 11 Batch 7 files untracked; all preserved.
- Batch 8 rows found: 4.
- Selected IDs: AWS-044, AWS-045, AWS-046, AWS-047.
- Priority mix: 0 P0, 2 P1, 2 P2.
- Dependencies: AWS-006 completed; prior compute, networking, monitoring, governance, and resilience lessons are cross-link evidence.
- Batch 9 or Batch 10 content modified at start: no.

The Batch 8 scope and pre-implementation manifest were created before learning-content changes.

## Pricing fundamentals and Free Tier

AWS-044 rewrote the authorized pricing target around cloud economics, cost dimensions, On-Demand, Reserved Instances, four current Savings Plans types, Spot, capacity reservations, dedicated options, storage, databases, transfer, and scenario selection. Unsupported exact values were removed. Free Tier was not selected and remains unchanged.

## Cost estimation and analysis

AWS-046 created a decision owner that separates Pricing Calculator, Cost Explorer, Budgets, Cost Anomaly Detection, and AWS Data Exports/CUR 2.0 by question and time horizon.

## Cost allocation and consolidated billing

The new guide covers tag activation, Cost Categories, chargeback/showback, and consolidated billing while preserving member-account separation.

## Compute purchasing models

AWS-044 now distinguishes commitments, flexibility, interruption, tenancy, discount, and capacity assurance and supplies CPP and SAA scenarios.

## Service and data-transfer pricing

AWS-047 now analyzes complete data paths across AZs, Regions, internet, edge, NAT, endpoints, transit, and inspection without universal free-transfer or stale exact-price claims.

## Cost optimization

Pricing, transfer, and cost-tool lessons add scenario-ready cost decisions that retain availability, security, performance, and operational requirements. Rightsizing is explained and linked to its existing owner. Compute Optimizer, Cost Optimization Hub, storage lifecycle, and workload scheduling are identified as complementary practices; they were not expanded because no separate Batch 8 row authorized a rewrite.

## AWS Support

AWS-045 now uses the current commercial plan lineup, dates the transition from older plans, and corrects Trusted Advisor and AWS Health concepts. Volatile response commitments are linked rather than copied.

## AWS Marketplace

No Marketplace backlog row was selected; Marketplace content and billing claims were unchanged.

## Comparison guides

AWS-046 added `cost/01-cost-management-tool-selection.md` and a local cost index. No unrelated comparison guide was created.

## Navigation and audit updates

Navigation changed in `12-billing-pricing-and-support/README.md`, `15-comparisons-and-decision-guides/README.md`, the new `cost/README.md`, `README.md`, `docs/repository-map.md`, and the implementation index. Audit changes cover the canonical inventory, badge audit, CPP/SAA task maps, technologies matrix, service matrix, depth matrix, pricing/Support freshness audit, SAA architecture-quality audit, and affected-row dashboard notes.

## Corrections

Eight correction families are recorded in `PHASE-6-BATCH-8-FACT-CORRECTIONS.md`; official sources were checked on 2026-07-25.

## Backlog results

Completed: 4. Partially completed: 0. Blocked: 0. Deferred within the 54-row scope ledger: 7 later-batch rows; 43 prior rows are recorded as already completed. Manual review: 0 selected items. Each selected ID appears in scope, pre, post, cumulative status, decisions, corrections, coverage delta, and this changelog.

## Validation

- `python scripts/validate-file-names.py --all`: passed, 371 paths checked.
- `python scripts/validate-markdown-links.py --all`: first run found one new incorrect VPC endpoint path; the link was corrected and the rerun passed, 316 Markdown files checked.
- `python scripts/detect-duplicate-filenames.py`: passed, 369 files and no candidates.
- `python scripts/generate-repository-report.py`: passed after the sandboxed write was retried with approval; 370 files summarized.
- Custom completion gate: passed for mandatory records, selected IDs, targets, CSV parsing, unique inventory ownership, empty Markdown, badges, references, knowledge checks, hashes, exact price/discount patterns, and legacy roots.
- Custom duplicate lesson-number scan: passed.
- Obsolete Support-name scan: only the explicit, sourced 2026 transition section and its knowledge check contain older names.
- `git diff --check`: passed; Git reported only line-ending normalization warnings for existing audit Markdown working copies.
- `git diff --stat` and `git status --short`: reviewed; Batch 7 work remains present and unstaged, Batch 8 files are unstaged, and no Batch 9/10 path is changed.

## Safety confirmation

Batch 7 changes were preserved. No destructive Git operation was performed.

```text
Batch 9 items implemented: 0
Batch 10 items implemented: 0
Unrelated canonical lessons rewritten: 0
Top-level categories changed: 0
Legacy directories recreated: 0
Commits created: 0
Pushes performed: 0
```
