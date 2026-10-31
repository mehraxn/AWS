# Git, Line-Ending, and Encoding Audit

## Required Git baseline

- Branch: `main`
- Recent commits (newest first): `17b7be3`, `32c6ba8`, `717b495`, `7ce614f`, `19dbea9`, `d79a638`, `305b471`, `568c562`, `357a49f`, `c62cca7` (all have subject “update”).
- Initial `git status --short`:

```text
?? "COPY PASTE PROMPT OF CLAUDE (BOTH CONTENT AND STYLE ).txt"
?? "g)ELB & ASG/"
?? "h) RDS/"
```

The working tree was dirty before Phase 1. The untracked prompt and the two untracked study-note directories may contain valuable work; this plan does not modify or dismiss them.

## Line endings

- CRLF-only files: **185**
- LF-only files: **0**
- Mixed-line-ending files: **0**
- Files without line breaks: **0**

This is consistent rather than internally mixed, but differs from the proposed LF convention. Do not mass-normalize in Phase 1. In Phase 2, make line-ending conversion a separately reviewable operation (preferably governed by a reviewed `.gitattributes`) so moves and textual churn can be distinguished.

## Content and filename encoding

- All 185 files decode successfully as strict UTF-8.
- Unicode punctuation and emoji are present intentionally in content and some filenames.
- The attachment used to convey this task displayed a mojibake dash (“â€“”), but no repository file failed UTF-8 validation.
- Several filenames contain trailing spaces before extensions, doubled spaces, parentheses, ampersands, and Unicode dashes. These are portability and shell-quoting risks, not evidence of corrupt content.
- No malformed on-disk filename was proven. Preserve exact source paths and use literal-path-aware tooling in Phase 2.

## Suspicious deletions and untracked replacements

- No tracked deletion or tracked modification appeared in the initial status.
- The two untracked directories are not paired with tracked deletions in the baseline, so there is no evidence that they are filename replacements; nevertheless, preserve and review them as uncommitted work.
- No exact-content duplicate was found between tracked and untracked files.

## Safe Phase 2 preparation

1. Commit or stash the user's current untracked work only with the user's explicit decision; do not clean it.
2. Re-run status, branch, log, and a full SHA-256 inventory immediately before migration.
3. Review every medium-confidence/manual-review and merge group.
4. Add and review a narrow `.gitattributes` change separately if LF normalization is desired.
5. Perform renames with `git mv`, in small topic-based batches.
6. Keep moves separate from content merges; use one reviewable change set per duplicate group.
7. After each batch, verify source count, destination count, hashes for move-only files, and `git diff --summary`.
8. Never infer disposability from version/Claude labels or timestamps.

