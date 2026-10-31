# Phase 6 Batch 1 Changelog

## Initial state

- Date: 2026-07-22
- Branch: `audit/phase5-official-coverage`
- Git status before Batch 1: modified `README.md` and `docs/repository-map.md`; untracked `docs/certification-audit/`, `docs/reorganization/PHASE-5-CHANGELOG.md`, and `scripts/generate-phase5-audit.py`.
- Pre-existing changes: Phase 5 audit work, including 16 insertions and 1 deletion across the two tracked modified files; no staged changes.
- Recent tip: `8bfc169 chore: checkpoint canonical repository before Phase 5 audit`.
- Branches inspected: current audit branch, `main`, `refactor/canonical-aws-notes`, two backup branches, and remote tracking references.
- Phase 5 authority files confirmed: all six mandatory files were present and non-empty.
- Batch 1 backlog rows found: AWS-001 through AWS-006.
- Selected items: AWS-001, AWS-002, AWS-003, AWS-004, AWS-005, AWS-006.
- Blocked items at preflight: none.
- Dependencies: AWS-003 and AWS-005 depend on AWS-002; all other Batch 1 rows have no backlog dependency.
- Initial `git diff --stat`: 2 files changed, 16 insertions, 1 deletion.
- Initial `git diff --cached --stat`: empty.

## Lessons created

### `01-cloud-fundamentals/01-shared-responsibility-model.md`

- Backlog ID: AWS-001
- Certification relevance: CPP fundamentals and SAA architecture
- Official requirement: responsibility allocation and service-model shifts
- Main sections: AWS/customer/shared responsibilities; EC2, RDS, Lambda, and S3 comparison; CPP scenarios; SAA implications; knowledge check
- Official references: AWS Shared Responsibility Model, Well-Architected Security Pillar, CLF-C02, and SAA-C03

### `01-cloud-fundamentals/02-cloud-concepts-and-benefits.md`

- Backlog ID: AWS-002
- Certification relevance: CPP core
- Official requirement: cloud value proposition
- Main sections: benefits, economics, service/deployment models, scenarios, traps, and knowledge check
- Official references: CLF-C02 Domain 1, AWS cloud-value guidance, and Well-Architected definitions

### `02-global-infrastructure/01-regions-availability-zones-and-edge.md`

- Backlog ID: AWS-003
- Certification relevance: CPP fundamentals and SAA architecture
- Official requirement: Regions, AZs, edge, scope, availability, and selection trade-offs
- Main sections: infrastructure concepts, service scope, Region selection, Multi-AZ/Multi-Region/edge comparison, SAA decisions, and knowledge check
- Official references: AWS Regions and AZs, fault-isolation guidance, CloudFront, CLF-C02, and SAA-C03

## Lessons updated

### `03-identity-governance-and-organizations/aws-iam/01-overview.md`

- Backlog ID: AWS-004
- Main changes: managed and inline policies, identity/resource policies, boundaries, explicit deny, STS, federation, cross-account access, Organizations/SCPs, SAA scenarios, knowledge check, and references
- Existing content preserved: original beginner definitions, examples, comparisons, summary, and memory aids remain
- Corrections made: clarified that boundaries and SCPs do not grant permissions and that explicit deny overrides allow

### `13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md`

- Backlog ID: AWS-005
- Main changes: pillar decision table, architecture foundations, review milestones, trade-offs, SAA scenarios, knowledge check, and references
- Existing content preserved: original definitions, six-pillar descriptions, comparisons, example, summary, and memory aids remain
- Corrections made: no prior false claim removed; missing architecture depth was added

### AWS-006 allowlisted active notes

- Main changes: Amazon Quick and Quick Sight transition, Amazon SageMaker AI, and AWS Health Dashboard terminology
- Existing content preserved: explanations and historical provenance remain; only verified active branding changed
- Corrections made: 11 active learning/navigation files received source-verified terminology changes

## Corrections

- Factual corrections: 4 documented correction families, including IAM guardrails and 3 product-name families
- Terminology corrections: Amazon Quick Sight/Amazon Quick, Amazon SageMaker AI, and AWS Health Dashboard
- Badge corrections: IAM and Well-Architected now have evidence-supported CPP and SAA badges; three new lessons use backlog-supported badges
- Navigation corrections: affected category indexes, IAM local index, service index, repository map, root README, and direct analytics labels

## Backlog result

- Completed: 6
- Partially completed: 0
- Blocked: 0
- Deferred: 48 later-batch rows
- Manual review required: 0; AWS-006 manual targeting was resolved through the audit and official-source review

## Validation

- Filename validation: passed; 285 paths checked
- Link validation: passed; 255 Markdown files checked; 0 broken internal links
- Duplicate scan: passed; 283 files checked; 0 candidates
- Lesson-number validation: passed; 0 duplicate numeric prefixes within a directory
- Empty-file validation: passed; 0 empty Markdown files
- Badge review: passed for all five lesson targets; AWS-002 correctly has CPP only
- Reference review: passed; every new or substantially expanded target has focused official references and a 2026-07-22 checked date
- Terminology review: passed; remaining old names occur only in explicit history, audit, or provenance records
- Repository report: passed with 284 files summarized after an approved write outside the default sandbox
- Helper-script syntax check: passed
- `git diff --check`: passed; line-ending conversion warnings are informational and no whitespace errors were reported

## Safety confirmation

```text
Batch 2 items implemented: 0
Batch 3–10 items implemented: 0
Unrelated canonical lessons rewritten: 0
Top-level categories changed: 0
Legacy directories recreated: 0
Commits created: 0
Pushes performed: 0
```
