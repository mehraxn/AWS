# CPP Coverage Dashboard

## Authoritative Phase 1 baseline — 2026-07-27

This summary is derived from the current [134-criterion coverage matrix](CPP-COVERAGE-MATRIX.md), not from the historical Phase 5 or Phase 6 estimates below. A criterion counts as complete only when the repository supports definition, recognition, relevance, distinction, and basic application at the required CPP depth.

### Repository totals

| Status | Count | Share |
|---|---:|---:|
| Complete | 104 | 77.6% |
| Partial | 24 | 17.9% |
| Mention-only | 2 | 1.5% |
| Missing | 4 | 3.0% |
| Wrong-depth | 0 | 0.0% |
| Duplicate-evidence | 0 | 0.0% |
| Potentially outdated | 0 | 0.0% |
| **Total** | **134** | **100.0%** |

Percentages are unweighted criterion counts and may not sum to exactly 100.0% after rounding. They are not an exam-readiness score. File-level freshness and duplication risks remain even where a requirement's best evidence is complete.

### Domain completion

| Domain | Official exam weight | Criteria | Complete | Partial | Mention-only | Missing | Strict completion |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1. Cloud Concepts | 24% | 18 | 13 | 4 | 1 | 0 | 72.2% |
| 2. Security and Compliance | 30% | 31 | 23 | 7 | 0 | 1 | 74.2% |
| 3. Cloud Technology and Services | 34% | 57 | 44 | 10 | 1 | 2 | 77.2% |
| 4. Billing, Pricing, and Support | 12% | 28 | 24 | 3 | 0 | 1 | 85.7% |

### Highest-priority weaknesses

1. There is no canonical CPP lesson for migration strategies and the migration journey (`CPP-1.3-K1`, `K2`, and `S2`).
2. Console, CLI, SDK, API, infrastructure as code, and one-time versus repeatable operations lack one beginner canonical owner (`CPP-3.1`).
3. AppStream 2.0, WorkSpaces, and WorkSpaces Secure Browser have no meaningful learner evidence (`CPP-3.8-K5` and `S5`).
4. AWS Marketplace lacks canonical coverage of security products and cost/governance/entitlement capabilities (`CPP-2.4-S2`, `CPP-4.3-S8`).
5. Governance versus compliance, location/industry requirements, and service-specific compliance responsibilities remain fragmented (`CPP-2.2`).
6. BYOL versus included licensing is only mentioned, not taught (`CPP-1.4-S3`).
7. Older lessons are inconsistent: 139 of 189 active lessons lack a recognized knowledge-check heading, 136 lack a recognized References heading, and 20 contain freshness-sensitive patterns without a verification date. These are file-level editorial findings, not automatic requirement failures.

### Inventory context

- Active learning Markdown files: **232**.
- Active lessons excluding READMEs: **189**.
- Active section or service READMEs: **43**.
- Empty active-category directories: **26**; none are linked as lessons.
- Archived Markdown files: **8**; archive and process-history files are excluded from coverage totals.
- Exact placeholder tokens found in active Markdown: **0**.
- Meaningful knowledge checks detected: **50/189**; many use collapsible answers rather than a separate answer heading.
- Official/reference sections detected: **53/189**.

## Historical snapshots

The entries below are retained for traceability. They used different denominators and scoring rules and must not be combined with the 2026-07-27 baseline.

## Phase 6 Batch 7 affected-requirement delta — 2026-07-24

AWS-040 through AWS-043 add fundamental CPP evidence for Availability Zones, high availability, disaster-recovery concepts, application integration, and serverless recognition. CPP-3.2-02 and CPP-3.3-03 are now complete; broader cloud-benefit rows receive supporting evidence but are not rescored here.

## Phase 6 Batch 6 affected-requirement delta — 2026-07-24

AWS-035 through AWS-039 add fundamental CPP evidence for encryption, logging and auditing, governance, security-service selection, observability, and operations management. Four directly affected partial criteria are now complete; this is an affected-row delta, not a whole-repository rescore.

## Phase 6 Batch 5 affected-requirement delta — 2026-07-23

AWS-031 through AWS-034 now meet their required CPP fundamental or awareness depth. This records four affected criteria and does not claim whole-repository completion.

Audit date: **2026-07-21**. Scores are evidence metrics, not guaranteed exam-readiness scores.

Scoring: complete 1.0, partial 0.5, mention-only 0.1, wrong-depth 0.25, missing 0.0; outdated is capped at 0.25.

| Domain | Weight | Complete | Partial | Missing | Evidence-based score |
|---|---|---|---|---|---|
| Cloud Concepts | 24% | 2 | 17 | 1 | 44.5% |
| Security and Compliance | 30% | 9 | 12 | 0 | 69.5% |
| Cloud Technology and Services | 34% | 14 | 32 | 0 | 64.3% |
| Billing, Pricing, and Support | 12% | 10 | 7 | 0 | 79.4% |

## Supporting Metrics

- Complete tasks: 0
- Partial tasks: 19
- Missing tasks: 0
- Complete requirements: 35
- Partial/mention/wrong-depth requirements: 68
- Missing requirements: 1
- Beginner-ready files: 6
- Files below fundamental depth: 183
- Listed-service representation: 108/115
- P0 backlog gaps: 10
- P1 backlog gaps: 20

Separate quality dimensions: task coverage above; beginner/architecture depth from inventory; service representation from scope matrix; terminology and navigation in their dedicated audits.

## Phase 6 Batch 8 affected-requirement delta — 2026-07-25

AWS-044 through AWS-047 add fundamental CPP evidence for pricing models, major cost drivers, cost-management tool selection, data-transfer pricing, Support plan selection, Trusted Advisor, and AWS Health. Seventeen directly affected rows were reconciled to complete. Free Tier, Marketplace, re:Post, and other unselected findings were not rescored.

## Phase 6 Batch 9 affected-requirement delta — 2026-07-25

AWS-048 through AWS-050 add fundamental CPP evidence for streaming ingestion, analytics-service selection, AI/ML service recognition, and responsible generative-AI awareness. Four directly affected CPP-3.7 requirements were reconciled to complete. Unselected awareness services and Batch 10 findings were not rescored.

## Phase 6 final evidence snapshot — 2026-07-25

AWS-051 adds cross-domain original scenario practice; AWS-053 and AWS-054 reconcile badge and navigation evidence. No official task row was promoted merely because an exam-preparation guide links to it.

| Domain | Requirements | Complete | Partial | Mention-only | Missing | Evidence score |
|---|---:|---:|---:|---:|---:|---:|
| Cloud Concepts | 20 | 3 | 12 | 4 | 1 | 47.0% |
| Security and Compliance | 21 | 13 | 7 | 1 | 0 | 79.0% |
| Cloud Technology and Services | 46 | 21 | 24 | 1 | 0 | 72.0% |
| Billing, Pricing, and Support | 17 | 16 | 1 | 0 | 0 | 97.1% |

- Complete requirements: **53/104**.
- Partial requirements: **44**.
- Mention-only requirements: **6**.
- Missing requirements: **1**.
- Complete tasks: **3/19**; partial tasks: **16**.
- Phase 6 backlog: **54/54 completed**.

The implementation backlog is complete, but the official task map still records shallow or missing evidence. Phase 6 completion is therefore not a claim of exhaustive CPP exam coverage or guaranteed readiness.
