# Phase 6 Batch 10 Content Decisions

Verification date for all selected items: **2026-07-25**.

## AWS-051 — CPP exam preparation

### Official requirement

Provide domain-linked CPP scenarios, distractor reasoning, and no leaked questions.

### Required CPP depth

Fundamental cross-domain reasoning and service recognition.

### Required SAA depth

Not applicable.

### Canonical target

`16-exam-preparation/01-cpp-scenario-reasoning.md`

### Existing files reviewed

The exam-preparation index, CPP baseline and task map, service index, comparison guides, prior coverage deltas, and canonical lessons linked by the new guide were reviewed. No equivalent guide existed.

### Official sources used

Official CLF-C02 exam guide, official CLF-C02 in-scope service list, and AWS Certification preparation page.

### Gap being resolved

The repository lacked an original, domain-linked method for extracting CPP requirements and eliminating plausible distractors.

### CPP content added

Official domain mapping, a four-step method, original scenarios across all four domains, service-selection traps, five explained knowledge checks, and exam-integrity guidance.

### SAA architecture content added

None; the lesson is CPP-specific.

### Migration or hybrid scenarios added

None. No migration or hybrid backlog row was selected.

### Security and validation guidance added

Shared responsibility, API auditing, compliance resources, source checking, and prohibition of recalled exam content are addressed.

### Existing content preserved

All canonical service and comparison lessons remain owners of detailed content and are linked rather than copied.

### Content removed or corrected

No existing learning content was removed. The empty category index was expanded after the new target was created.

### Badge decision

CPP only, justified by fundamental CLF-C02 scenario depth. No SAA badge.

### Navigation and map updates

Exam index, root navigation, service index, repository map, inventory, badge audit, scope audit, depth matrix, quality audit, and dashboard were updated.

### Acceptance-criteria result

Completed: domain-linked original scenarios, distractor reasoning, current official references, fundamental CPP depth, filename compliance, and link integrity are present.

### Remaining work

None for AWS-051; it does not block Phase 6 closure.

### Validation result

Recorded in the post-implementation manifest and final validation report.

## AWS-052 — SAA exam preparation

### Official requirement

Provide requirements, constraints, option elimination, trade-offs, and domain links at scenario-ready SAA depth.

### Required CPP depth

Awareness only where cross-domain context overlaps; the target itself is SAA-specific.

### Required SAA depth

Scenario-ready architecture reasoning.

### Canonical target

`16-exam-preparation/02-saa-architecture-scenario-reasoning.md`

### Existing files reviewed

The exam-preparation index, SAA baseline and task map, architecture patterns, service-selection guides, prior coverage deltas, and directly linked canonical lessons were reviewed.

### Official sources used

Official SAA-C03 exam guide, official SAA-C03 in-scope service list, and AWS Certification preparation page.

### Gap being resolved

The repository lacked a cross-domain guide for separating mandatory constraints from preferences and eliminating architecture options explicitly.

### CPP content added

No CPP badge or dedicated CPP section was added.

### SAA architecture content added

Requirement extraction, constraint ranking, data-flow analysis, option elimination, survivor comparison, original scenarios for all four domains, a cross-domain design, traps, review checklist, and explained knowledge checks.

### Migration or hybrid scenarios added

None. No migration or hybrid backlog row was selected.

### Security and validation guidance added

Cross-account roles, least privilege, trust boundaries, monitoring, recovery, cost, current-feature verification, and prohibition of recalled exam content are addressed.

### Existing content preserved

Detailed service and architecture lessons remain canonical and are linked.

### Content removed or corrected

No existing learning content was removed.

### Badge decision

SAA only, justified by scenario-ready architecture depth. No CPP badge.

### Navigation and map updates

Exam index, root navigation, service index, repository map, inventory, badge audit, scope audit, depth matrix, architecture-quality audit, and dashboard were updated.

### Acceptance-criteria result

Completed: requirements, constraints, option elimination, trade-offs, official sources, scenario-ready SAA depth, filename compliance, and link integrity are present.

### Remaining work

None for AWS-052; it does not block Phase 6 closure.

### Validation result

Recorded in the post-implementation manifest and final validation report.

## AWS-053 — Certification badges

### Official requirement

Apply only evidence-supported badge corrections and preserve CPP/SAA depth distinctions.

### Required CPP depth

A CPP badge requires official relevance plus meaningful page-level recognition or fundamental content.

### Required SAA depth

An SAA badge requires official relevance plus meaningful architecture/design or scenario depth.

### Canonical target

`docs/certification-audit/BADGE-ACCURACY-AUDIT.csv`

### Existing files reviewed

All badge-audit rows were reconciled against actual Markdown badge state, the certification-label policy, inventory evidence, official baselines, service scope, and Batches 1–9 decisions.

### Official sources used

Official CLF-C02 and SAA-C03 exam guides and service lists, plus the repository certification-label policy.

### Gap being resolved

The Phase 5 audit contained stale actual flags and automatic depth recommendations explicitly awaiting manual scope review.

### CPP content added

The new CPP scenario guide received one justified CPP badge.

### SAA architecture content added

The new SAA scenario guide received one justified SAA badge.

### Migration or hybrid scenarios added

None.

### Security and validation guidance added

Badge decisions now distinguish page-level depth from mere service-list presence; a badge cannot substitute for content.

### Existing content preserved

Existing learning content and prior evidence-supported badges were retained. No badge was mass-added from an automated recommendation.

### Content removed or corrected

Actual badge flags were synchronized, stale recommendations were retired conservatively, and every audit row now has a resolved action.

### Badge decision

Two Batch 10 lesson badges were added. All other rows were reconciled to actual supported state; unresolved automatic additions/removals were rejected rather than guessed.

### Navigation and map updates

Badge audit and inventory were synchronized; the two new targets were added to the inventory and scope audit.

### Acceptance-criteria result

Completed: no pending badge action remains, actual badge state agrees with files, and CPP/SAA depth distinctions are preserved.

### Remaining work

Future service or exam-scope changes require a new dated review but do not block Phase 6 closure.

### Validation result

Recorded in the final validation report.

## AWS-054 — Repository navigation

### Official requirement

Update category READMEs, service index, repository map, and validate links after implementation.

### Required CPP depth

Navigation must expose the CPP learning path and badge meaning without overstating coverage.

### Required SAA depth

Navigation must expose SAA architecture and decision paths without equating links with scenario depth.

### Canonical target

`README.md`, with directly affected indexes and maps.

### Existing files reviewed

Root and category READMEs, service index, repository map, implementation index, structure audit, and final reconciliation requirements were reviewed.

### Official sources used

Repository governance and validated Phase 6 evidence; no service fact was introduced.

### Gap being resolved

The root still described Batch 10 as pending, the exam index was empty, and final records were not linked.

### CPP content added

Added an explicit CPP learning path and scenario-guide link.

### SAA architecture content added

Added an explicit SAA learning path and architecture-guide link.

### Migration or hybrid scenarios added

None.

### Security and validation guidance added

The root distinguishes backlog completion from official task-map completeness and warns that volatile facts require current verification.

### Existing content preserved

The numbered hierarchy and all established navigation links remain intact.

### Content removed or corrected

Replaced the obsolete “Batch 10 gaps remain” status and corrected the exam-category file count.

### Badge decision

Navigation explains badge meaning; no badge was added to a navigation-only index.

### Navigation and map updates

Root README, exam README, service index, repository map, implementation index, structure audit, and final-record links were updated.

### Acceptance-criteria result

Completed subject to the final link validator.

### Remaining work

None for AWS-054; future content additions require ordinary navigation maintenance.

### Validation result

Recorded in the final validation report.
