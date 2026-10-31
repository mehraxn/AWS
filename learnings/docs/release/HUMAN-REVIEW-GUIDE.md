# Human Review Guide

## Purpose

Provide an evidence-first order for approving the release candidate without implying that human review is complete.

## Review Order

1. Security findings and release blockers.
2. Root README and navigation.
3. Phase 6 final reconciliation.
4. CPP and SAA dashboards.
5. High-risk factual records and their source links.
6. Exam-preparation integrity.
7. Release documentation.
8. Remaining learning content as needed.
9. The complete Git diff and excluded-file decisions.

## Critical Files

- `docs/release/FINAL-SECURITY-AND-HYGIENE-REVIEW.md`
- `docs/release/FINAL-VALIDATION-RESULTS.md`
- `docs/release/RELEASE-CANDIDATE-MANIFEST.csv`
- `docs/content-implementation/PHASE-6-FINAL-BACKLOG-RECONCILIATION.csv`
- `docs/final-review/PHASE-7-FINAL-VALIDATION.md`

## High-Risk Factual Files

- `docs/final-review/PHASE-7-TERMINOLOGY-AND-PRODUCT-STATUS-QA.md`
- `docs/final-review/PHASE-7-PRICING-AND-SUPPORT-QA.md`
- `docs/final-review/PHASE-7-AI-RESPONSIBLE-USE-QA.md`
- `docs/final-review/PHASE-7-MIGRATION-AND-HYBRID-QA.md`
- `docs/release/FINAL-HANDOFF-CHANGELOG.md`

## Root Navigation Review

Review `README.md`, `docs/README.md`, `docs/repository-map.md`, `docs/service-index.md`, and `16-exam-preparation/README.md`. Confirm that links, category counts, phase status, and limitation wording agree.

## CPP Learning-Path Review

Start at `16-exam-preparation/README.md`, follow the CPP sequence, then inspect `01-cpp-scenario-reasoning.md` and `CPP-COVERAGE-DASHBOARD.md`.

## SAA Learning-Path Review

Follow the SAA sequence through architecture patterns and comparisons, then inspect `02-saa-architecture-scenario-reasoning.md` and `SAA-COVERAGE-DASHBOARD.md`.

## Coverage Dashboard Review

Confirm that 51 CPP and 58 SAA task-map rows below complete depth remain described as limitations rather than backlog blockers.

## Pricing and Support Review

Recheck Free Tier account-date distinctions, Support plan names and transitions, Trusted Advisor access, AWS Health eligibility, and any exact pricing immediately before approval.

## AI and Responsible-Use Review

Confirm current SageMaker AI/Bedrock terminology, privacy framing, guardrails, evaluation, human oversight, and the absence of permanent model lists or automatic-accuracy guarantees.

## Migration and Product-Status Review

Confirm Snowball Edge's new-customer restriction, Wavelength location availability, and current migration source/target support.

## Exam-Integrity Review

Review the two scenario guides and the Phase 7 integrity CSV. Do not reproduce or add recalled live-exam questions. Decide whether the documented 28 knowledge checks without explained answers are acceptable for this release.

## Git Diff Review

Review every manifest row, then compare `git diff --name-status`, `git diff`, and the untracked-file list. Pay special attention to the deletion of the temporary report scripts and the corrected repository-map counts.

## Files That Must Not Be Committed

- Any restored copy or content of `.tmp_phase7_inventory.py` or `.tmp_phase7_qa_csvs.py`; only their deletion should be retained.
- `scripts/__pycache__/`, `.pyc`, editor metadata, environment files, credentials, backups, and other local artifacts.

## Recommended Validation Re-Run

Run the four repository validators, the Phase 6 reconciliation checks, the security scan, and `git diff --check` immediately before committing and again after committing.

## Approval Checklist

- [ ] Security and blockers reviewed.
- [ ] Root navigation reviewed.
- [ ] CPP and SAA paths sampled.
- [ ] High-volatility facts verified.
- [ ] Exam integrity accepted.
- [ ] Manifest and excluded files confirmed.
- [ ] Complete diff reviewed.
- [ ] Target branch and remote confirmed.
- [ ] Commit, push, and pull-request creation approved.
