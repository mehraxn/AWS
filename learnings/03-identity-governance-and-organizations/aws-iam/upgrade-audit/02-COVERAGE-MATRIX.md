# AWS IAM Coverage Matrix

Audit date: **2026-11-06**

Status meanings:

- **COMPLETE** — substantively adequate for current file scope; later freshness checks may still apply.
- **PARTIAL** — useful material exists, but important content, accuracy, evidence, or teaching depth is absent.
- **MISSING** — no meaningful treatment exists.
- **NOT APPLICABLE** — the function does not meaningfully apply to that topic.

> [!NOTE]
> Phase 1 used a proxy because the master specification was unavailable. Phase 2 found and read `AWS_CCP_SAA_GitHub_README_Master_Prompt.txt`; the matrix below now uses its actual 22-function blueprint. Phase 13 independently reassessed all ten lessons and the main README. The QA process is complete; the release is publication-ready with the tooling limitations recorded in `04-FINAL-QA-REPORT.md`.

## Overall document coverage

| File | Topic | Core concepts | CCP coverage | SAA coverage | Comparisons and traps | Practical examples | Practice questions | References | Markdown quality | Important missing material |
|---|---|---|---|---|---|---|---|---|---|---|
| `README.md` | IAM learning hub | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | NOT APPLICABLE | COMPLETE | COMPLETE | No known acceptance blocker; static Mermaid validation passed, but no local renderer was available |
| `01-overview.md` | IAM foundations | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; ongoing source-freshness review still applies |
| `02-users.md` | IAM users | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; ongoing credential/MFA freshness review still applies |
| `03-groups.md` | IAM groups | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; ongoing quota and Identity Center freshness review still applies |
| `04-roles.md` | IAM roles | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; current STS and EKS claims were rechecked; ongoing freshness review still applies |
| `05-customer-managed-policies.md` | Customer managed policies | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; provenance map and current quota/version claims were verified |
| `06-inline-policies.md` | Inline policies | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; ongoing service-authorization and IaC freshness review still applies |
| `07-read-only-access-policy.md` | `ReadOnlyAccess` | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; current v191 metadata was rechecked and the external-ID example was repaired |
| `08-administrator-access-policy.md` | `AdministratorAccess` | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; current v1/PowerUserAccess metadata was rechecked and the RCP diagram was repaired |
| `09-access-analyzer.md` | IAM Access Analyzer | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; current types, APIs, resources, Regions, and pricing model were rechecked |
| `10-root-user.md` | Root user | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; current centralized-root behavior was rechecked and malformed CLI syntax was repaired |

## Master specification 22-function matrix

Abbreviated column labels are filenames: `01` through `10` are the numbered topic lessons. The README is excluded because Phase 1 requested the 22 functions for each topic file.

| # | Master content function | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | What is the topic? | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 2 | What problem does it solve? | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 3 | Core concepts and components | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 4 | How it works, prerequisites, and defaults | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 5 | Key features, capabilities, and restrictions | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 6 | Real-world use cases and when to choose it | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 7 | Visibly separated CCP essentials | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 8 | Visibly separated SAA deep dive | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 9 | Confusable-service/feature comparisons | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 10 | Integration and architecture patterns | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 11 | Security, permissions, compliance, and shared responsibility | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 12 | Observability, auditing, troubleshooting, and failure behavior | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 13 | Pricing and cost optimization | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 14 | Practical configuration/CLI/IaC example | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 15 | Common exam traps and misconceptions | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 16 | Technical interview questions and answers | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 17 | Original exam-style practice questions | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 18 | Real-world scenario drills | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 19 | Exam decision tree and keyword recognition | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 20 | Quick-revision cheat sheet and memory model | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 21 | Official references and currency note | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| 22 | Closing study takeaway | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE |

## Evidence and concise reasons by topic

### `README.md`

- **Evidence:** the Phase 12 learning hub integrates exactly ten canonical lessons in a 571-line GitHub-native index with verified summaries, separate CCP and SAA learning paths, 18 stable TOC anchors, two Mermaid architecture maps, ten required comparison families, a qualified policy-evaluation model, a 16-case decision guide, 18 cross-topic misconceptions, 40 verified assessment-section links, six learning checkpoints, an organization reference architecture, keyword recognition, quick revision, study workflow, source transparency, and eight official references reviewed on 2026-11-06.
- **Reason for COMPLETE ratings:** Phase 12 preserves the original overview, objectives, order, certification focus, study tips, and surrounding repository navigation while replacing generic lesson descriptions with evidence-based learning guidance. Phase 13 independently resolved 161 README-local links and 480 local links across the full educational set, checked tables, fences, badges, UTF-8/LF, whitespace, and static Mermaid structure, and reviewed the final diff. The provenance CSV was found and verified; no material cross-lesson contradiction or acceptance blocker remains.

### `01-overview.md`

- **Evidence:** the Phase 2 guide implements all 22 ordered functions, including explicit CCP/SAA tracks, policy anatomy and valid JSON, union/intersection and cross-account evaluation, 3 Mermaid workflows, integrations, security, troubleshooting, pricing, 25 traps, 10 interview questions, 30 explained practice questions, 6 architecture scenarios plus scenario drills, navigation, and 15 official references reviewed on 2026-11-05.
- **Reason for COMPLETE ratings:** Phase 2 corrected the federation-first baseline, added RCP/resource-principal/effectiveness nuances, qualified global/Regional behavior, and passed the documented local structure/JSON/link checks. Volatile facts still require final-release freshness review.

### `02-users.md`

- **Evidence:** the Phase 3 guide implements all 22 functions in 1,000+ lines: three credential categories and safe key replacement, current password/MFA behavior, full user/group/resource/guardrail evaluation, federation-first workforce guidance, three Mermaid diagrams, operational commands, incident response, 28 traps, 10 interview questions, 30 explained practice questions, 10 architecture drills, navigation, and 22 official references reviewed on 2026-11-05.
- **Reason for COMPLETE ratings:** Phase 3 preserved the useful original definition, identity comparisons, Anna/Omar/Sara example, and memory model while correcting the employee/application default, long-term-key assumptions, and oversimplified permission evaluation. Local QA parsed both JSON blocks and checked anchors, links, tables, fences, details blocks, UTF-8/LF, and whitespace. Mermaid received static syntax/balance review because no renderer is installed.

### `03-groups.md`

- **Evidence:** the Phase 4 guide implements all 22 functions in 1,100+ lines: group lifecycle and constraints, inherited permission evaluation, managed and inline policy patterns, non-principal status, Identity Center distinction, two Mermaid diagrams, two valid JSON policies, a safe CLI tutorial, 28 traps, 10 interview questions, 28 explained practice questions, 10 architecture drills, navigation, and 24 official references reviewed on 2026-11-05.
- **Reason for COMPLETE ratings:** Phase 4 preserved useful group fundamentals while correcting the implied single-source permission model and adding direct grants, resource policies, boundaries, SCPs/RCPs, explicit denies, cross-account roles, stale-reference deletion risk, audit/troubleshooting, pricing, and federation-first workforce design. Local QA parsed JSON and checked anchors, links, tables, fences, details blocks, UTF-8/LF, whitespace, and diff integrity. CLI syntax was checked against official command documentation and Mermaid received static syntax/balance review because the corresponding local tools are unavailable.

### `04-roles.md`

- **Evidence:** the Phase 5 guide implements all 22 functions in 1,600+ lines: role/session and trust/permissions separation, STS API distinctions, session duration and chaining, cross-account and federation architecture, EC2/Lambda/ECS/EKS patterns, service-linked roles, `PassRole`, confused-deputy defenses, revocation, two Mermaid diagrams, seven valid JSON policies, 34 traps, 12 interview questions, 32 explained practice questions, exactly 12 architecture scenarios, navigation, and 37 official references reviewed on 2026-11-05.
- **Reason for COMPLETE ratings:** Phase 5 preserved the useful role definition, temporary-badge analogy, trust/permissions split, STS and instance-profile distinctions, and EC2-to-S3 example while correcting the implied one-step authorization model. It adds same-account/cross-account nuances, source identity and tags, full effective-permission reasoning, workload credential delivery, regional STS, failure diagnosis, and incident response. Local QA parsed every JSON block and checked anchors, links, tables, fences, details blocks, UTF-8/LF, whitespace, and diff integrity. CLI syntax was checked against official command documentation and Mermaid received static syntax/balance review because the corresponding local tools are unavailable.

### `05-customer-managed-policies.md`

- **Evidence:** the Phase 6 guide implements all 22 functions in 1,300+ lines: standalone/account-scoped policy behavior, complete IAM JSON semantics, AWS/customer/inline comparisons, the five-version/default/rollback lifecycle, attachment and deletion behavior, boundaries, effective permissions, least privilege, multi-account and Identity Center patterns, defensive version administration, two Mermaid diagrams, eight valid JSON policies, 32 traps, 12 interview questions, 30 explained practice questions, exactly 12 architecture scenarios, navigation, and 25 official references reviewed on 2026-11-05.
- **Reason for COMPLETE ratings:** Phase 6 preserved the source's reusable-template analogy, ownership, support-team example, central-update benefit, least-privilege purpose, policy comparison, revision checklist, memory aids, and exact provenance comment. It corrected the false AWS-managed-versioning claim and malformed table, removed the categorical “best practice” claim, and added complete JSON/action/resource/condition reasoning, shared-policy rollout and rollback, privilege-escalation defenses, policy validation, troubleshooting, auditing, pricing, and deployment architecture. Phase 13 reconfirmed the JSON, navigation, quotas, and version semantics and verified the referenced provenance CSV and its canonical row at `learnings/docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv`.

### `06-inline-policies.md`

- **Evidence:** the Phase 7 guide implements all 22 functions in 1,100+ lines: embedded ownership and lifecycle; correct user/group/role beneficiary semantics; seven valid JSON examples; trust, boundary, session, SCP/RCP, resource-policy, and cross-account distinctions; CLI and CloudFormation management; two Mermaid diagrams; 30 traps; 12 interview questions; 30 explained practice questions; exactly 12 architecture scenarios; navigation; and 30 official references reviewed on 2026-11-05.
- **Reason for COMPLETE ratings:** Phase 7 preserved the source's glued-note analogy, one-time correction, supported identities, deletion coupling, `BillingAuditRole` example, comparisons, use cases, exam keywords, and memory aids. It corrected one-to-one ownership versus beneficiary scope and added no-ARN/no-native-version behavior, replacement semantics, complete evaluation, role-session revocation nuance, least-privilege administration, IaC, auditing, troubleshooting, cost, and assessment depth. Local QA parsed all JSON and checked anchors, relative links, tables, fences, details blocks, counts, UTF-8/LF, whitespace, Mermaid structure, and diff integrity. CLI syntax was checked against official documentation because the AWS CLI, Markdown linter, and Mermaid renderer are unavailable.

### `07-read-only-access-policy.md`

- **Evidence:** the Phase 8 guide implements all 22 functions in 800+ lines: current AWS managed-policy metadata and lifecycle; action-level metadata/content distinctions; S3, DynamoDB, KMS, and logs exposure; full effective-permission evaluation with seven required cases; `ViewOnlyAccess`, `SecurityAudit`, IAM/service-specific, customer-managed, inline, and Identity Center comparisons; cross-account architecture; four valid JSON examples; two Mermaid diagrams; 32 traps; 12 interview questions; 30 explained practice questions; exactly 12 scenario drills; navigation; and 23 official references reviewed on 2026-11-05.
- **Reason for COMPLETE ratings:** Phase 8 preserves the useful visitor-pass analogy and auditor, manager, support, training, attachment, AWS-maintenance, consultant-role, sensitive-information, and policy-combination lessons while replacing the inaccurate “See everything, change nothing” model. It adds exact current evidence, data confidentiality, AWS update/change-control behavior, full guardrail/resource/KMS evaluation, federation-first delivery, least-privilege replacement, auditing, troubleshooting, cost, and assessment depth. Local QA parsed all JSON and checked headings, anchors, relative links, tables, fences, details blocks, counts, UTF-8/LF, whitespace, Mermaid structure, and diff integrity. CLI syntax was checked against official documentation because local tool availability is documented in the tracker.

### `08-administrator-access-policy.md`

- **Evidence:** the Phase 9 guide implements all 22 functions in 1,100+ lines: exact verified AdministratorAccess JSON and v1 metadata; identity delivery; root, PowerUser, read/view/audit, custom/inline, role, Identity Center, boundary, SCP/RCP, KMS, resource-policy, service-linked-role, and break-glass comparisons; ten required effective-permission cases; Organizations, cross-account, Identity Center, delegated-boundary, `PassRole`, privilege-escalation, and emergency architecture; six valid JSON examples; two Mermaid diagrams; 32 traps; 12 interview questions; 30 explained practice questions; exactly 14 architecture scenarios; navigation; and 29 official references reviewed on 2026-11-06.
- **Reason for COMPLETE ratings:** Phase 9 preserves the original master-badge analogy, setup/admin/emergency/sandbox use cases, startup growth example, AWS ownership/attachments, least-privilege warning, and explicit-deny/SCP/boundary teaching while replacing malformed JSON and qualified “almost everything” slogans. It adds exact wildcard semantics, root-only and centralized-root behavior, full effective authorization, production privileged-access security, multi-account federation, auditing, troubleshooting, pricing, and assessment depth. Local QA parsed all JSON and checked explicit anchors, links, tables, fences, details blocks, counts, UTF-8/LF, whitespace, Mermaid structure, and diff integrity. CLI syntax was checked against official documentation because AWS CLI, Markdownlint, and Mermaid CLI are unavailable.

### `09-access-analyzer.md`

- **Evidence:** the Phase 10 guide implements all 22 functions in 1,000+ lines: three separately configured analyzer types; zone-of-trust and finding lifecycle; current external/internal resource support; type-specific scope, Region, pricing, and APIs; policy validation, paid custom checks, access previews, and policy generation caveats; multi-account delegated administration; EventBridge and Security Hub integration; safe CLI workflows; 4 Mermaid diagrams; 2 valid JSON examples; 35 traps; 12 interview questions; 32 explained practice questions; exactly 16 required architecture scenarios; navigation; and 23 official references reviewed on 2026-11-06.
- **Reason for COMPLETE ratings:** Phase 10 preserves the security-reviewer analogy, analysis-not-enforcement rule, external/internal/unused concepts, S3 sharing example, related-service distinctions, and memory model while correcting the unified-analyzer misconception. It adds current supported resources, zone behavior, archive versus resolve semantics, V2 finding APIs, reanalysis timing, policy-development capabilities, organization administration, service-linked roles, auditing, troubleshooting, costs, and assessment depth. Local QA parsed all JSON and checked 22 anchors/headings, links, tables, fences, details blocks, counts, UTF-8/LF, whitespace, Mermaid structure, and protected-file hashes. CLI syntax was checked against official documentation because AWS CLI, Markdownlint, and Mermaid CLI are unavailable.

### `10-root-user.md`

- **Evidence:** the Phase 11 guide implements all 22 functions in 1,100+ lines: root identity/account-principal semantics; conventional and project/member account qualifications; MFA enforcement and eight-device support; root keys and temporary `aws login`; verified root-only task matrix; seven authorization cases; SCP/RCP and management-account exceptions; centralized credential removal and recovery; all five root-task policies; Regional `AssumeRoot` with 900-second maximum; CloudTrail sign-in/session correlation; security monitoring, incident response, billing, safe CLI workflows; 4 Mermaid diagrams; 3 valid JSON examples; 35 traps; 12 interview questions; 33 explained practice questions; exactly 18 prescribed scenarios; navigation; and 24 official references reviewed on 2026-11-06.
- **Reason for COMPLETE ratings:** Phase 11 preserves the master-key analogy, rare-use guidance, root/IAM/admin distinctions, MFA/key protection, initial-account example, and memory model while removing unsafe “universally full access” and static-MFA assumptions. It adds root ARN delegation semantics, account-type-specific tasks/recovery, current MFA enforcement, central member credential elimination, task-scoped privileged sessions, exact policy/API/endpoint limits, organization architecture, audit evidence, costs, and complete assessment depth. Local QA parsed all JSON and checked 22 anchors/headings, links, tables, fences, details blocks, counts, UTF-8/LF, whitespace, Mermaid structure, diff integrity, and protected-file hashes. CLI syntax was checked against official documentation because AWS CLI, Markdownlint, and Mermaid CLI are unavailable.

## Priority view

| Priority | Files | Acceptance blocker |
|---|---|---|
| LOW | All | Final visual polish only after accuracy, scope, and references are resolved |
