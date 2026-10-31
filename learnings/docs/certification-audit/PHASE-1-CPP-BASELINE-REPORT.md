# Phase 1 CPP Baseline Report

Date: **2026-07-27**  
Scope: AWS Certified Cloud Practitioner **CLF-C02** only  
Repository state at start: clean working tree

## Outcome

Phase 1 established one current requirement-level CPP baseline, canonical ownership for every official in-scope service, an enforceable depth/editorial model, a file-specific implementation backlog, and a dedicated learner start path. It made no broad lesson rewrite, move, merge, deletion, commit, or push.

## Files Inspected

The inspection read the repository tree and the body of every active lesson rather than relying on prior dashboards:

- root control and learner files, including `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `.gitattributes`, `.gitignore`, and Markdown configuration;
- all **232 pre-change active Markdown files** in categories `01-` through `16-`, comprising **189 lessons** and **43 READMEs**;
- all 19 comparison lessons and their 11 category/index READMEs under `15-comparisons-and-decision-guides/`;
- both existing exam-preparation lessons and the exam-preparation README;
- **120 documentation Markdown files** and **56 audit/implementation CSV files** under `docs/` after this phase's additions, including prior baselines, coverage maps, quality audits, reorganization records, implementation history, final review, release records, indexes, standards, and source policy;
- all **12 scripts** and script documentation;
- the existing generated report directory, without regenerating or editing it;
- all **8 archived Markdown files**, classified as history rather than active evidence;
- official AWS CLF-C02 domain, technologies/concepts, in-scope, and out-of-scope pages current on 2026-07-27.

Content inspection included word/depth distribution, badges, heading structure, knowledge-check and reference headings, freshness patterns, placeholders, empty directories, link targets, normalized filenames, and four-word-shingle overlap across all 189 active lessons.

## Files Created

- `docs/certification-audit/CPP-COVERAGE-MATRIX.md`
- `docs/certification-audit/CPP-CANONICAL-CONTENT-MAP.md`
- `docs/certification-audit/CPP-IMPLEMENTATION-BACKLOG.md`
- `docs/content-standards/CPP-CONTENT-AND-STYLE-STANDARD.md`
- `16-exam-preparation/cloud-practitioner/README.md`
- `docs/certification-audit/PHASE-1-CPP-BASELINE-REPORT.md`

## Files Modified

- `README.md` — routes CPP learners to the dedicated path and states that quizzes/mock exams are planned.
- `16-exam-preparation/README.md` — adds the CPP start guide as the first exam-preparation route.
- `docs/README.md` — links the CPP-specific standard.
- `docs/certification-audit/README.md` — links the new authoritative records and explains historical denominators.
- `docs/certification-audit/CPP-COVERAGE-DASHBOARD.md` — adds a current summary while retaining old snapshots for traceability.

## Files Intentionally Left Unchanged

- SAA lessons, SAA dashboards, SAA task maps, and SAA learner-path records.
- The 189 existing active lesson bodies; Phase 1 did not batch-rewrite them.
- Historical Phase 5, Phase 6, Phase 7, reorganization, release, and migration records.
- Archive content.
- Generated reports under `reports/generated/`; regeneration was unnecessary for the requested human-authored audit.
- Empty directories; removal requires an explicit authorized hygiene phase and migration logging.

## Coverage Findings

The current denominator is **134** atomic official criteria: each published knowledge and skill bullet across 19 task statements.

| Domain | Criteria | Complete | Partial | Mention-only | Missing | Strict completion |
|---|---:|---:|---:|---:|---:|---:|
| 1. Cloud Concepts | 18 | 13 | 4 | 1 | 0 | 72.2% |
| 2. Security and Compliance | 31 | 23 | 7 | 0 | 1 | 74.2% |
| 3. Cloud Technology and Services | 57 | 44 | 10 | 1 | 2 | 77.2% |
| 4. Billing, Pricing, and Support | 28 | 24 | 3 | 0 | 1 | 85.7% |
| **Total** | **134** | **104** | **24** | **2** | **4** | **77.6%** |

No criterion received `wrong-depth`, `duplicate-evidence`, or `potentially-outdated` after its best canonical evidence was assessed. Those remain file-level risks and are not interpreted as absent.

The official in-scope list contains **115 services**. The canonical map assigns all 115 an owner: **98 existing owners** and **17 planned owners**.

## Main Findings

### Stronger than the historical baseline

- Cloud benefits and economics, Shared Responsibility, global infrastructure, Well-Architected, core compute/storage/database selection, encryption, operational-service comparison, pricing models, cost tooling, and Support-plan reasoning now have strong current evidence.
- Existing Phase 6 work materially improved the repository, but the old dashboard obscured that improvement by mixing dated deltas with an older denominator.

### High-priority gaps

- No canonical migration-strategy/journey lesson.
- No canonical Console/CLI/SDK/API/IaC and operating-method lesson.
- No meaningful AppStream 2.0, WorkSpaces, or WorkSpaces Secure Browser evidence.
- No canonical Marketplace lesson covering security products and cost/governance/entitlement capabilities.
- BYOL versus included licensing remains mention-only.
- Governance/compliance concepts, location/industry needs, root-only tasks, credential selection, Support Center, and Health API need targeted depth.

### Editorial and structural risks

- Only 50 of 189 active lessons use a recognized knowledge-check heading; many older questions do not explain plausible wrong answers.
- Only 53 of 189 active lessons use a recognized References heading.
- A heuristic found 20 lessons with possible volatile facts and no verification date. Each requires human confirmation; the pattern alone is not proof of outdated content.
- Five active lessons contain multiple H1 headings. Three active files contain heading-level jumps.
- Twenty-six active-category directories are empty. They are not current learner destinations, but they create maintainer noise.
- Badge application is inconsistent: 128 of 189 active lessons had neither recognized CPP nor SAA badge even though many have audit mappings. Badges must be verified, not batch-inferred.
- No exact TODO/TBD/FIXME-style placeholder exists in active learning Markdown.

### Duplication

No exact or substantial near-duplicate lesson pair was detected. Low-level overlap is concentrated where expected: Global Accelerator overview/static IP, Storage Gateway cached/stored volumes, IAM owner/child lessons, and service owners versus comparison guides. These are canonical-link risks rather than safe deletion candidates.

## Learner-Facing Improvements

- A beginner now has one CLF-C02 start page with an essential nine-step route.
- Essential CPP, useful supporting material, and optional SAA-depth material are defined.
- Comparisons, current scenario practice, planned quizzes/mock exams, and final weak-domain review are clearly located.
- The root README no longer implies that mock-exam material exists or that a flat category list is itself a complete learning path.
- Maintainer audit details remain under `docs/` rather than dominating the root learner page.

## Validation Results

| Check | Command or method | Result |
|---|---|---|
| File naming | `python -B scripts/validate-file-names.py --all` | Passed: 438 paths checked in the first post-edit run. |
| Local Markdown links and anchors | `python -B scripts/validate-markdown-links.py --all` | Passed: 366 Markdown files checked. |
| Duplicate filenames | `python -B scripts/detect-duplicate-filenames.py` | Passed: 436 files, no candidates. |
| Coverage-row reconciliation | count rows beginning `CPP-` in the new matrix | Passed: exactly 134. |
| Service-owner reconciliation | count official service rows, including Service Quotas | Passed: 115 total; 17 planned. |
| Near-duplicate learning content | four-word shingle containment across 189 lessons | Passed for substantial duplicates; 10 low-overlap related pairs at an 8% review threshold. |
| Empty files/placeholders | repository scans | Passed for empty learning files and active placeholders; 26 empty active-category directories remain as warnings. |
| Temporary files | extension/name scan | Passed: 0 temporary-file candidates. |
| Generated files accidentally tracked | `git ls-files reports/generated` | Passed: no tracked generated report returned. |
| Heading hierarchy | read-only heading scan | Warning: 10 repository files have multiple H1s, including 5 active lessons; 5 jumps occur across 4 repository files, including 3 active lessons. |
| Whitespace and patch integrity | `git diff --check` | Passed after touched Markdown was normalized to LF. |
| Git safety | `git status --short` and history not mutated | Passed: no commit or push; `.git` not modified. |

The final validation run should be treated as authoritative if its checked counts differ slightly because this report itself adds one Markdown file.

## Known Limitations

- The official service and feature lists are non-exhaustive and can change.
- Status decisions involve editorial judgment; they are conservative and evidence-backed but should receive maintainer review before bulk implementation.
- External links were source-checked for scope decisions, but the local link validator intentionally does not test every external URL.
- The freshness scan is heuristic and can match stable durations or words such as “quota”; backlog work must verify each candidate manually.
- Prior audits use different requirement groupings. Their percentages are historical and not directly comparable with the 134-row baseline.
- Planned canonical paths deliberately do not exist yet; the learner path links only to existing files.
- Knowledge-check detection counts recognized headings, not every informal question embedded in prose.

## Recommended Next Phase

Implement **Batch 2: Cloud Concepts**, beginning with `CPP-B2-01`—the canonical migration-strategy foundation—then licensing economics and link-first cloud-concept consolidation. This closes the only Domain 1 mention-only criterion and resolves a prerequisite for later migration-service recognition.
