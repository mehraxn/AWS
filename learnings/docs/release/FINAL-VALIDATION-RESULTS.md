# Final Validation Results

## Validation Scope

Final working-tree diff, untracked files, mandatory Phase 6 and Phase 7 records, canonical hierarchy, learner routes, high-volatility facts, exam integrity, hygiene, and release documentation. Checked 2026-07-25.

## Filename Validation

- Command: `python scripts/validate-file-names.py --all`.
- Initial exit: 1; two mandated `FINAL-*` release records triggered the general version-marker rule.
- Correction: added the exact mandated handoff paths to the existing control-record allowlist.
- Final exit: 0; 429 paths checked; remaining: 0; blocking: no after correction.
- Evidence: `scripts/validate-file-names.py` and final command output.

## Markdown-Link Validation

- Command: `python scripts/validate-markdown-links.py --all`.
- Exit: 0; 358 Markdown files checked; initial issues: 0; corrected: 0; remaining: 0; blocking: no.
- Evidence: validator output.

## Anchor Validation

- Method: the Markdown-link validator resolves and slug-checks local heading fragments.
- Exit: 0; 427 files checked; issues before/corrected/remaining: 0/0/0; blocking: no.
- Evidence: `scripts/validate-markdown-links.py` and link-validator output.

## Duplicate-Filename Validation

- Command: `python scripts/detect-duplicate-filenames.py`.
- Exit: 0; issues before/corrected/remaining: 0/0/0; blocking: no.

## Duplicate-Lesson Validation

- Method: repository-wide filename validator's per-directory lesson-number check.
- Exit: 0; issues before/corrected/remaining: 0/0/0; blocking: no.

## Canonical-Ownership Validation

- Method: re-read all 210 rows in `PHASE-7-CANONICAL-OWNERSHIP-QA.csv`, validate service-index targets, and verify completed Phase 6 targets.
- Result: 0 conflict, 0 failed ownership row, 0 missing service-index target, and 0 missing concrete completed target; blocking: no.

## Empty-File Validation

- Method: repository-wide Markdown size scan and mandatory-record size checks.
- Result: 0 empty Markdown file and 0 missing/empty mandatory record; blocking: no.

## Badge Validation

- Method: re-read 206 rows in `PHASE-7-BADGE-QA.csv`.
- Result: 0 failed row; blocking: no.

## AWS-Terminology Validation

- Method: Phase 7 terminology evidence plus focused current-name scan and official-source review.
- Initial issue: 1 outdated legacy Support grouping in a Trusted Advisor table.
- Corrected: 1, using current qualitative access wording, an official reference, and checked date.
- Remaining: historical/audit terminology and documented product transitions only; blocking: no.

## Product-Status Validation

- Method: official AWS documentation review for Snowball Edge, Wavelength, SageMaker AI, Support, Free Tier, and certification guides.
- Result: active notes already warn that Snowball Edge is unavailable to new customers; Wavelength remains location-specific; SageMaker AI terminology is current; volatility remains documented.
- Issues before/corrected/remaining: 0/0/documented freshness risk; blocking: no.

## Pricing and Support Validation

- Method: Phase 7 pricing QA, current AWS Support/Trusted Advisor/Free Tier pages, and exact-claim scan.
- Initial issue: 1 stale Trusted Advisor access table; corrected: 1; remaining: Free Tier and entitlements require live review; blocking: no.

## CPP Coverage Validation

- Method: Phase 6 reconciliation and CPP task-map/dashboard comparison.
- Result: 104 rows: 53 complete, 44 partial, 6 mention-only, and 1 missing. Dashboard agrees; 51 below-complete rows are non-blocking limitations.

## SAA Coverage Validation

- Method: Phase 6 reconciliation and SAA task-map/dashboard comparison.
- Result: 109 rows: 51 complete, 37 partial, 4 mention-only, and 17 wrong-depth. Dashboard agrees; 58 below-complete rows are non-blocking limitations.

## Mermaid Validation

- Method: five-file Phase 7 manual review and `where.exe mmdc`.
- Result: manual review passed; Mermaid CLI unavailable. Remaining: 1 low-severity tool limitation; blocking: no.

## Exam-Integrity Validation

- Method: 37-row Phase 7 integrity audit plus suspicious-source phrase scan.
- Result: 0 copied-exam indicator, 0 dump, 0 ambiguity. Nine files have explained answers; 28 lack explanations. Blocking: no; editorial limitation remains.

## Secret and Hygiene Validation

- Method: changed/untracked content scan for credentials, keys, tokens, local paths, binaries, caches, backups, and temporary files.
- Result: 36 changed or untracked paths reviewed, 0 secret or sensitive finding. Two tracked temporary generators remain marked for deletion; blocking: no.

## Merge-Conflict Marker Scan

- Method: anchored scan for `<<<<<<<`, `=======`, and `>>>>>>>`.
- One match was a deliberate long equals-sign separator in a prompt template, not a conflict marker. Actionable issues remaining: 0; blocking: no.

## Placeholder Scan

- Method: case-insensitive whole-word scan for TODO, TBD, FIXME, COMING SOON, PLACEHOLDER, INSERT HERE, and TO BE WRITTEN.
- One expected match names the scan terms in this validation report itself. Unresolved placeholder: 0; blocking: no.

## Git Diff Check

- Command: `git diff --check`.
- Exit: 0; issues before/corrected/remaining: 0/0/0; blocking: no. Git emitted a non-blocking warning that one pre-existing CRLF lesson will be normalized to LF when Git next writes it.

## Remaining Critical Issues

None.

## Remaining High Issues

None. High-volatility facts require human review but no high-severity defect remains.

## Remaining Medium Issues

- 28 knowledge checks without explained answers.
- 51 CPP and 58 SAA task-map rows below complete evidence depth.
- 13 reference-QA rows without dedicated References headings.

## Remaining Low Issues

- Five Mermaid files lack automated render validation.
- Ignored local `scripts/__pycache__/` content must remain excluded.

## Release Blockers

None.

## Final Decision

Passed. The release candidate is ready for final human review, subject to the pending human checklist.
