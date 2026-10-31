# Validation and Reporting Scripts

Python utilities used for repository validation, reporting, controlled migration, and evidence generation.

## Script Index

| Script | Purpose |
|---|---|
| [`apply-phase6-batch1-terminology.py`](apply-phase6-batch1-terminology.py) | Apply the approved Batch 1 terminology corrections. |
| [`detect-duplicate-filenames.py`](detect-duplicate-filenames.py) | Report normalized, versioned, case-only, and similar filenames. |
| [`execute-approved-migration.py`](execute-approved-migration.py) | Execute an explicitly approved manifest-driven migration. |
| [`finalize-phase6-batch2-records.py`](finalize-phase6-batch2-records.py) | Finalize and reconcile Phase 6 Batch 2 evidence. |
| [`generate-phase5-audit.py`](generate-phase5-audit.py) | Generate Phase 5 audit records from repository evidence. |
| [`generate-phase6-batch1-records.py`](generate-phase6-batch1-records.py) | Generate supporting records for Phase 6 Batch 1. |
| [`generate-phase6-batch2-records.py`](generate-phase6-batch2-records.py) | Generate supporting records for Phase 6 Batch 2. |
| [`generate-repository-report.py`](generate-repository-report.py) | Generate the repository summary under `reports/generated/`. |
| [`phase4-consolidate.py`](phase4-consolidate.py) | Support the approved Phase 4 canonical consolidation workflow. |
| [`validate-file-names.py`](validate-file-names.py) | Validate canonical filename and path rules. |
| [`validate-markdown-links.py`](validate-markdown-links.py) | Check local Markdown links and heading anchors. |

## Common Validation Commands

### Windows PowerShell

```powershell
python scripts/validate-file-names.py --all
python scripts/validate-markdown-links.py --all
python scripts/detect-duplicate-filenames.py
python scripts/generate-repository-report.py
```

### Unix-like shell

```bash
python3 scripts/validate-file-names.py --all
python3 scripts/validate-markdown-links.py --all
python3 scripts/detect-duplicate-filenames.py
python3 scripts/generate-repository-report.py
```

## Safety

- Review a script before running it.
- Use dry-run modes where available.
- Do not run migration or rewriting utilities without an approved scope.
- Validation warnings do not authorize automatic content changes.
- Keep temporary processing files outside the repository.

[Back to repository home](../README.md)
