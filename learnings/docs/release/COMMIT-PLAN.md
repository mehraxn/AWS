# Commit Plan

## Current Branch

`audit/phase5-official-coverage`

## Working-Tree State

Dirty by design, with unstaged Phase 7 final-review records, release documentation, navigation corrections, and deletion of two tracked temporary helper scripts. The base commit is `f24d1b6`; no file is staged.

## Recommended Strategy

Use one cohesive documentation and cleanup commit after human review. Phase 6 implementation is already in the base commit; the current diff completes Phase 7 and the human handoff.

## Recommended Commit Count

1

## Commit 1

### Suggested Commit Message

`docs: complete final QA and release-candidate handoff`

### Purpose

Add the remaining Phase 7 QA evidence and release-candidate handoff, correct root repository-map facts, and remove temporary report generators from release content.

### Files Included

All 34 rows marked `include_in_commit=yes` in `RELEASE-CANDIDATE-MANIFEST.csv`. The two temporary-script artifacts are marked `no` because their contents must not be committed; during staging, the human should retain their tracked deletion as cleanup rather than restoring them.

### Files Excluded

Ignored caches, `.pyc` files, environment files, editor metadata, credentials, backups, and any restored temporary-script content.

### Human Checks Before Commit

- Review every manifest row and the complete diff.
- Confirm the two temporary-script deletions.
- Verify high-volatility official facts and current certification guides.
- Confirm the target branch and remote.
- Confirm all human checklist items that are prerequisites for committing.

## Commit 2

Not recommended. The remaining diff is one coherent final-QA and handoff unit.

## Files That Must Not Be Committed

Temporary helper-script contents, ignored `scripts/__pycache__/`, `.pyc`, local configuration, credentials, editor files, backups, and unrelated generated output.

## Validation Before Commit

Run filename, link, duplicate-filename, repository-report, reconciliation, secret, placeholder, merge-marker, and `git diff --check` validation.

## Validation After Commit

Re-run the validators and confirm `git status --short` shows only intentionally excluded local artifacts, if any.

## Push Checklist

- [ ] Human approved the commit and reviewed its exact contents.
- [ ] Human confirmed the remote and branch.
- [ ] Post-commit validation passed.
- [ ] No secret or excluded artifact is present.

## Pull-Request Checklist

- [ ] Human confirmed the base branch.
- [ ] Final pull-request body matches the committed diff.
- [ ] Known limitations and volatile-fact maintenance remain explicit.
- [ ] CI results will be reviewed before merge.

This plan does not authorize staging, committing, pushing, or creating a pull request.
