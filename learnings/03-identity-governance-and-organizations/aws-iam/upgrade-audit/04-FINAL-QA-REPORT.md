# AWS IAM Final QA Report

## A. Executive summary

| Item | Result |
|---|---|
| Audit date | 2026-11-06 |
| Module path | `learnings/03-identity-governance-and-organizations/aws-iam` |
| Educational files inspected | 11 of 11 |
| Supporting project files inspected | Master prompt, `IAM_UPGRADE_RULES.md`, completeness audit, coverage matrix, and upgrade tracker |
| Release status | **PUBLICATION-READY WITH DOCUMENTED LIMITATIONS** |
| Findings | 0 blockers, 3 major, 2 minor; all 5 repaired |
| Remaining material issues | 0 |

The final audit independently reread the ten IAM lessons and the main README, compared shared concepts across the set, checked current official AWS documentation for material and volatile claims, validated all fenced JSON, reviewed command examples, inspected every Mermaid diagram, resolved every relative Markdown link, and reviewed all 305 original practice questions and answers.

The principal repairs were: correcting the certification abbreviation from CCP's accidental `CPP` form; correcting who generates a third-party external ID; making an RCP diagram target resources instead of IAM roles; repairing an invalid `AssumeRoot` task-policy ARN; and locating and verifying the provenance CSV that earlier phases reported as missing.

Important limitations are transparent and nonblocking:

- AWS CLI was not installed, so command blocks received manual syntax and semantic review against current official command/API documentation but were not executed against an AWS account.
- Mermaid CLI and a dedicated Markdown linter were unavailable. Diagrams received static structural checks and manual semantic review, but no local image render was produced.
- No live IAM, Organizations, root, MFA, Access Analyzer, or policy-changing operation was run.
- All 304 external Markdown references were inventoried. Material current claims were checked by retrieving their authoritative AWS sources, but this was not a bulk live-HTTP crawl of every external URL.

## B. Audit scope

The following canonical educational files were inspected completely:

1. [`README.md`](../README.md)
2. [`01-overview.md`](../01-overview.md)
3. [`02-users.md`](../02-users.md)
4. [`03-groups.md`](../03-groups.md)
5. [`04-roles.md`](../04-roles.md)
6. [`05-customer-managed-policies.md`](../05-customer-managed-policies.md)
7. [`06-inline-policies.md`](../06-inline-policies.md)
8. [`07-read-only-access-policy.md`](../07-read-only-access-policy.md)
9. [`08-administrator-access-policy.md`](../08-administrator-access-policy.md)
10. [`09-access-analyzer.md`](../09-access-analyzer.md)
11. [`10-root-user.md`](../10-root-user.md)

The audit was limited to this IAM module plus the project requirements, audit/tracking documents, and the repository provenance map needed to verify this module. It was not an audit of every AWS learning module in the repository.

## C. Verification methodology

- **Manual review:** Read every required document and every educational file, including definitions, policy evaluation, security guidance, comparisons, diagrams, traps, questions, scenarios, revision material, and references.
- **Automated checks:** Used a purpose-built temporary validator for strict UTF-8 decoding, LF line endings, trailing whitespace, fences, HTML details/summary balance, JSON parsing, local paths, fragments, and static Mermaid delimiters/declarations. The temporary scripts were removed after use.
- **Official AWS documentation:** Retrieved current primary sources for IAM quotas, managed policies, role external IDs, EKS Pod Identity, RCPs, Access Analyzer types/resources/APIs/pricing, centralized root access, `AssumeRoot`, and the current CLF-C02 and SAA-C03 exam guides.
- **Technical comparison:** Compared shared explanations of users, groups, roles, policies, permissions boundaries, SCPs, RCPs, resource policies, cross-account access, root, Access Analyzer, Identity Center, and explicit-deny behavior.
- **Code validation:** Parsed 44 complete JSON blocks. Reviewed 41 Bash/PowerShell command blocks and their surrounding safety classification.
- **Navigation validation:** Parsed 784 Markdown links; resolved all 480 relative file/fragment links from their source files and inventoried 304 external references.
- **Question review:** Reviewed 305 practice-question details blocks and their answers, distractor explanations, assumptions, exceptions, and certification level.

## D. Per-file audit results

| Filename | Technical accuracy | CCP coverage | SAA coverage | Examples | Questions | Navigation | Sources | Final status |
|---|---|---|---|---|---|---|---|---|---|
| `README.md` | PASS after terminology normalization | PASS | PASS | PASS | N/A; routes to lesson assessments | PASS: 161 local links | PASS for stated integration claims | READY |
| `01-overview.md` | PASS | PASS | PASS | 3 JSON, 3 Mermaid: PASS | 30 reviewed: PASS | PASS | Current model and exam scope rechecked | READY |
| `02-users.md` | PASS | PASS | PASS | 2 JSON, 3 Mermaid: PASS | 30 reviewed: PASS | PASS | Credential/MFA sources reviewed | READY |
| `03-groups.md` | PASS | PASS | PASS | 2 JSON, 2 Mermaid: PASS | 28 reviewed: PASS | PASS | Group and quota sources reviewed | READY |
| `04-roles.md` | PASS | PASS | PASS | 7 JSON, 2 Mermaid: PASS | 32 reviewed: PASS | PASS | STS, external ID, and EKS claims rechecked | READY |
| `05-customer-managed-policies.md` | PASS; provenance status corrected | PASS | PASS | 8 JSON, 2 Mermaid: PASS | 30 reviewed: PASS | PASS | Quotas/versioning and provenance verified | READY |
| `06-inline-policies.md` | PASS | PASS | PASS | 7 JSON, 2 Mermaid: PASS | 30 reviewed: PASS | PASS | IAM/IaC behavior reviewed | READY |
| `07-read-only-access-policy.md` | PASS after external-ID correction | PASS | PASS | 4 JSON, 2 Mermaid: PASS | 30 reviewed: PASS | PASS | `ReadOnlyAccess` v191 verified | READY |
| `08-administrator-access-policy.md` | PASS after RCP diagram correction | PASS | PASS | 6 JSON, 2 Mermaid: PASS | 30 reviewed: PASS | PASS | AdministratorAccess v1 and PowerUserAccess v12 verified | READY |
| `09-access-analyzer.md` | PASS | PASS | PASS | 2 JSON, 4 Mermaid: PASS | 32 reviewed: PASS | PASS | Current APIs, resources, Regions, and pricing model rechecked | READY |
| `10-root-user.md` | PASS after CLI correction | PASS | PASS | 3 JSON, 4 Mermaid: PASS | 33 reviewed: PASS | PASS | Current centralized-root and `AssumeRoot` behavior rechecked | READY |

No passing status above relies only on a heading or count. Each combines full manual review, cross-file comparison, reproducible structural validation, and relevant official-source checks.

## E. Cross-document consistency

### Concepts compared

The audit compared identity versus permission, authentication versus authorization, user/group/role semantics, trust versus permissions, identity/resource policy grant paths, permissions boundaries, session policies, SCPs, RCPs, explicit denies, cross-account authorization, managed versus inline policy lifecycle, root versus AdministratorAccess, Access Analyzer versus enforcement/audit tools, and federation-first workforce access.

### Contradictions discovered and fixed

- The external-ID narrative correctly said the provider supplies a customer-unique value, but one JSON placeholder said customer-generated. The placeholder now agrees with the narrative and AWS's confused-deputy guidance.
- An AdministratorAccess architecture diagram connected RCPs to account roles even though RCPs constrain supported resources. The diagram now separates role sessions from development, staging, and production resources and connects RCPs to the resources.
- Certification material used `CPP` while the intended abbreviation was `CCP`. The educational set and active matrix/tracker terminology are now consistent.
- Current documentation said the provenance map was absent. A repository-wide search found and verified it, and current statements now reflect that evidence.

### Remaining concerns

No material contradiction remains. Differences in CCP and SAA depth are intentional: CCP emphasizes recognition and safe defaults, while SAA adds authorization paths, architecture, failure behavior, and trade-offs.

## F. Technical findings

| Issue ID | Severity | File | Heading or line reference | Problem | Evidence | Correction | Status |
|---|---|---|---|---|---|---|---|
| IAM-F13-001 | MINOR | All 11 educational files; active matrix/tracker | Certification badges, headings, question labels, and summaries | `CPP` was used where the intended AWS Certified Cloud Practitioner abbreviation was `CCP` | Phase 13 explicitly required the correction; the official exam guide names CLF-C02 as AWS Certified Cloud Practitioner | Replaced standalone `CPP`/`cpp` terminology and anchors with `CCP`/`ccp`; retained green `#2EA44F` and SAA blue `#0969DA` | FIXED |
| IAM-F13-002 | MAJOR | `07-read-only-access-policy.md` | Cross-account auditor trust-policy example | JSON implied the customer generated a provider-specific external ID, contradicting the surrounding provider-supplied guidance | AWS's third-party role guidance requires the provider to generate a unique customer identifier | Changed the example to `provider-generated-customer-specific-value` | FIXED |
| IAM-F13-003 | MAJOR | `08-administrator-access-policy.md` | Multi-account workforce administration Mermaid diagram | RCP arrows ended at IAM account roles, visually teaching a principal-side control | AWS Organizations documents RCPs as maximum permissions for supported resources in member accounts | Added environment resource nodes; retained SCP-to-role edges and moved RCP edges to resources | FIXED |
| IAM-F13-004 | MAJOR | `10-root-user.md` | Illustrative `AssumeRoot` command | `--task-policy-arn arn=arn:aws:...` was invalid CLI argument syntax | `AssumeRoot` requires the root-task policy ARN value `arn:aws:iam::aws:policy/root-task/...` | Removed the extra `arn=` prefix | FIXED |
| IAM-F13-005 | MINOR | `05-customer-managed-policies.md`, matrix, tracker | Provenance status | Current text repeated an incomplete search result and called the CSV absent | Repository-wide search found `learnings/docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv`; its canonical lesson row lists two consolidated sources and `content_verified=yes` | Corrected current lesson/matrix status and added a Phase 13 tracker resolution while preserving Phases 1-12 history | FIXED |

## G. AWS policy and CLI verification

- **Complete JSON examples checked:** 44.
- **Shell/CLI blocks reviewed:** 41.
- **Syntax validation:** Every JSON block parsed successfully after final repairs. Command names, required arguments, quoting, continuations, placeholder intent, mutability warnings, and documented endpoint/task restrictions were reviewed manually.
- **Semantic review:** Policy type, `Principal` placement, action/resource scope, conditions, deny behavior, boundaries, session policies, SCP/RCP scope, KMS/resource-policy caveats, cross-account two-sided authorization, managed-policy lifecycle, and root-task scope were compared across examples and official documentation.
- **Confirmed problems:** One semantic policy-example problem (external-ID ownership) and one CLI syntax problem (duplicated ARN prefix).
- **Corrections:** Both confirmed problems were repaired and reread; all 44 JSON blocks re-parsed afterward.
- **Unavailable tooling:** AWS CLI is not installed. No commands were sent to AWS, so this report does not claim live account or service execution.

Two suspected issues were explicitly rejected after current-source verification rather than changed: the current managed-policy attachment quotas are user 10/20, group 10/10, and role 20/25; and V2 Access Analyzer finding APIs still authorize with `access-analyzer:ListFindings` and `access-analyzer:GetFinding`.

## H. Markdown and link validation

| Check | Result |
|---|---|
| Educational files checked | 11 |
| Markdown links parsed | 784 |
| Relative links fully resolved | 480 |
| README relative links independently recounted | 161 |
| External references inventoried | 304 |
| Broken internal links found | 0 |
| Broken internal links fixed | 0 |
| Remaining unresolved internal links | 0 |
| Anchor issues | 0 |
| Table issues found in manual/structural review | 0 |
| Code-fence issues | 0 |
| Details/summary balance issues | 0 |
| UTF-8, LF, or trailing-whitespace issues | 0 |

The earlier README metric of 143 did not include the same link categories as the final resolver. The final count is not forced to match it: 161 relative links are now counted in the README and 480 across the educational set.

A dedicated Markdown linter was unavailable. GitHub-oriented structure was therefore checked with the custom validator, manual source review, and `git diff --check`.

## I. Exam material validation

- **Practice questions reviewed:** 305.
- **Materially incorrect answers found:** 0.
- **Ambiguous questions requiring repair:** 0.
- **Answer corrections made:** 0.
- **Exam-trap findings:** Core traps consistently distinguish group versus principal, trust versus permissions, allow versus limiter, read-only versus confidentiality/effective permissions, AdministratorAccess versus root, and Access Analyzer versus enforcement. The certification abbreviation was normalized to CCP.
- **Certification-scope concerns:** No unresolved scope issue. CCP material focuses on service recognition, security concepts, safe identity choices, and shared responsibility; implementation, troubleshooting, and architecture details are identified as SAA depth rather than mandatory CCP memorization.
- **Exam guides checked:** Current CLF-C02 and SAA-C03 official guides were retrieved on 2026-11-06.

The questions are original study material and do not claim to reproduce actual AWS exam questions or guarantee exam appearance.

## J. Mermaid validation

- **Diagrams inspected:** 28.
- **Syntax checks:** Every fenced Mermaid block has a recognized diagram declaration and balanced square, round, and curly delimiters.
- **Semantic checks:** Identity flow, trust, policy evaluation, Organizations guardrails, Access Analyzer observation, root workflows, and architecture edges were reviewed manually.
- **Confirmed problem:** One RCP diagram incorrectly ended RCP edges at role nodes.
- **Correction:** RCP edges now terminate at explicit resource nodes; SCP edges remain principal-side.
- **Renderer availability:** Mermaid CLI was unavailable and was not installed during this audit.
- **Remaining limitation:** Static and semantic checks do not prove GitHub's renderer will produce an ideal visual layout. No known syntax or meaning defect remains.

## K. Source/provenance review

### Official reference checks

The audit retrieved authoritative current pages for:

- IAM and STS quotas.
- `ReadOnlyAccess` v191, edited 2026-10-30.
- `AdministratorAccess` v1 and `PowerUserAccess` v12.
- Third-party external IDs and confused-deputy prevention.
- EKS Pod Identity account and platform restrictions.
- RCP resource-side scope and current support.
- Access Analyzer external/internal/unused analyzer behavior, V2 findings authorization actions, supported resource types, Regions, and pricing model.
- Centralized root credential management, the five root-task policies, Regional `AssumeRoot`, and the 900-second session maximum.
- CLF-C02 and SAA-C03 exam scope.

### Time-sensitive claims

Managed-policy versions/edit times, quotas, Access Analyzer resources/pricing, EKS support, root tasks/MFA/CLI behavior, and certification versions remain date-sensitive. The lessons already carry currency notes where appropriate; future maintenance is still required.

### Provenance CSV

The CSV is **not missing**. It was found at:

`learnings/docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv`

The row for `03-identity-governance-and-organizations/aws-iam/05-customer-managed-policies.md` identifies two consolidated source files, records `source_count=2`, `merge_type=consolidated`, and `content_verified=yes`, and points to checkpoint `70818e2` for recovery. The lesson's comment is legitimate non-navigational metadata relative to the learning-content root.

### Source verification limitations

The 304 external links were inventoried, and significant/volatile claims were checked by retrieving current official sources. This audit did not perform a bulk availability request for every external URL, and inaccessible future URLs would not by themselves disprove the documented AWS behavior.

## L. Release gate results

| Gate | Result | Evidence or limitation |
|---|---|---|
| 1 — File completeness | PASS | All 11 canonical educational files exist and were inspected |
| 2 — Technical accuracy | PASS | All 5 findings fixed; no known unresolved blocker or major error |
| 3 — Cross-document consistency | PASS | Shared IAM concepts compared; four contradictions/status conflicts repaired |
| 4 — IAM policy correctness | PASS | 44 JSON blocks parse and received semantic review |
| 5 — Navigation | PASS | All 480 relative links resolve, including fragments and surrounding-repository links |
| 6 — GitHub presentation | LIMITED | No blocking source issue found; dedicated Markdown linting and Mermaid rendering unavailable |
| 7 — Certification coverage | PASS | CCP/SAA terminology, badges, depth, and current exam guides reviewed |
| 8 — Assessment correctness | PASS | 305 answers reviewed; no known material error or ambiguity |
| 9 — Security guidance | PASS | External ID, root, guardrail, federation, and least-privilege guidance checked; one security example repaired |
| 10 — Repository safety | PASS | No deletions, destructive commands, commit, or push; Phases 1-12 history preserved |
| 11 — Source transparency | PASS | Date-sensitive claims and tool limits disclosed; provenance dependency verified |
| 12 — Audit traceability | PASS | Findings, repairs, counts, gates, limitations, and release decision recorded here and in the tracker |

The Gate 6 limitation is nonblocking because every source-level structural and semantic check available locally passed, and the missing executables are disclosed rather than treated as successful renders/lints.

## M. Unresolved issue register

No unresolved blocker, major, minor, technical, navigation, assessment, or provenance issue remains from this audit.

The following are validation limitations, not known repository defects:

| Limitation ID | Description | Impact | Disposition |
|---|---|---|---|
| LIM-001 | No local AWS CLI or live AWS account execution | Commands were not end-to-end executed | Static/manual review against official command/API documentation |
| LIM-002 | No Mermaid renderer | Rendered layout not observed | Static structure plus manual semantic review; maintain renderer check in CI if available |
| LIM-003 | No dedicated Markdown linter | Tool-specific style rules were not run | Custom structural validation, manual review, and `git diff --check` passed |
| LIM-004 | No bulk live crawl of all 304 external URLs | Not every URL received a current HTTP availability result | Material claims were checked from retrieved authoritative pages; monitor links periodically |

## N. Final release recommendation

**PUBLICATION-READY WITH DOCUMENTED LIMITATIONS**

All twelve critical release gates pass or have a narrowly documented, nonblocking tooling limitation. All five audit findings were repaired, all final structural regression checks pass, the provenance dependency is verified, and no unresolved material issue remains. The qualified recommendation avoids claiming live AWS execution, Mermaid rendering, dedicated linting, or exhaustive external-URL availability testing that did not occur.

## O. Future maintenance recommendations

- Recheck AWS-managed policy documents and edit dates when AWS publishes new defaults.
- Recheck IAM Access Analyzer resource support, analyzer behavior, APIs, Regions, integrations, and pricing during scheduled reviews.
- Recheck centralized root management, MFA enforcement, root-only tasks, root-task policies, sign-in logging, and CLI minimum versions.
- Recheck the official CLF-C02 and SAA-C03 guides for revisions or successor exams.
- Add periodic internal and external broken-link monitoring.
- Run a focused technical/source review on a predictable cadence and after material AWS IAM or Organizations announcements.
- If CI tooling becomes available, add Markdown linting and Mermaid rendering without expanding lesson scope.
