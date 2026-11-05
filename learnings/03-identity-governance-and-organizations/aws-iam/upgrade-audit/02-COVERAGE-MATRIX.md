# AWS IAM Coverage Matrix

Audit date: **2026-11-05**

Status meanings:

- **COMPLETE** — substantively adequate for current file scope; later freshness checks may still apply.
- **PARTIAL** — useful material exists, but important content, accuracy, evidence, or teaching depth is absent.
- **MISSING** — no meaningful treatment exists.
- **NOT APPLICABLE** — the function does not meaningfully apply to that topic.

> [!NOTE]
> Phase 1 used a proxy because the master specification was unavailable. Phase 2 found and read `AWS_CCP_SAA_GitHub_README_Master_Prompt.txt`; the matrix below now uses its actual 22-function blueprint. Lessons `01`–`06` have completed upgrades; statuses for lessons `07`–`10` remain Phase 1 evidence-based baselines until their dedicated phases.

## Overall document coverage

| File | Topic | Core concepts | CPP coverage | SAA coverage | Comparisons and traps | Practical examples | Practice questions | References | Markdown quality | Important missing material |
|---|---|---|---|---|---|---|---|---|---|---|
| `README.md` | IAM index | PARTIAL | PARTIAL | PARTIAL | MISSING | NOT APPLICABLE | NOT APPLICABLE | MISSING | COMPLETE | Specific outcomes, ownership map, integrated navigation |
| `01-overview.md` | IAM foundations | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; recheck volatile facts during final QA |
| `02-users.md` | IAM users | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; recheck volatile credential/MFA behavior during final QA |
| `03-groups.md` | IAM groups | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; recheck volatile quotas and Identity Center behavior during final QA |
| `04-roles.md` | IAM roles | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; recheck volatile STS, EKS, and service-integration behavior during final QA |
| `05-customer-managed-policies.md` | Customer managed policies | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; recheck volatile quotas, actions/condition keys, and Identity Center behavior during final QA |
| `06-inline-policies.md` | Inline policies | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | No known acceptance blocker; recheck volatile service authorization, CloudFormation, and Organizations behavior during final QA |
| `07-read-only-access-policy.md` | `ReadOnlyAccess` | PARTIAL | PARTIAL | MISSING | PARTIAL | COMPLETE | MISSING | MISSING | PARTIAL | Current policy evidence, data exposure, narrower/security-audit alternatives |
| `08-administrator-access-policy.md` | `AdministratorAccess` | PARTIAL | PARTIAL | PARTIAL | PARTIAL | COMPLETE | MISSING | MISSING | PARTIAL | Valid JSON, RCP/session constraints, escalation risk, controlled admin patterns |
| `09-access-analyzer.md` | IAM Access Analyzer | PARTIAL | PARTIAL | PARTIAL | PARTIAL | COMPLETE | MISSING | MISSING | PARTIAL | Separate analyzer types, API/Region/pricing scope, generation caveats |
| `10-root-user.md` | Root user | PARTIAL | PARTIAL | MISSING | PARTIAL | COMPLETE | MISSING | MISSING | PARTIAL | Root-only tasks, SCP/RCP nuance, centralized root sessions/recovery |

## Master specification 22-function matrix

Abbreviated column labels are filenames: `01` through `10` are the numbered topic lessons. The README is excluded because Phase 1 requested the 22 functions for each topic file.

| # | Master content function | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | What is the topic? | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 2 | What problem does it solve? | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 3 | Core concepts and components | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 4 | How it works, prerequisites, and defaults | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 5 | Key features, capabilities, and restrictions | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 6 | Real-world use cases and when to choose it | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 7 | Visibly separated CPP essentials | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 8 | Visibly separated SAA deep dive | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | MISSING | PARTIAL | PARTIAL | MISSING |
| 9 | Confusable-service/feature comparisons | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 10 | Integration and architecture patterns | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 11 | Security, permissions, compliance, and shared responsibility | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 12 | Observability, auditing, troubleshooting, and failure behavior | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | MISSING | MISSING | PARTIAL | MISSING |
| 13 | Pricing and cost optimization | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | NOT APPLICABLE | NOT APPLICABLE | MISSING | NOT APPLICABLE |
| 14 | Practical configuration/CLI/IaC example | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | MISSING | PARTIAL | MISSING | MISSING |
| 15 | Common exam traps and misconceptions | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | COMPLETE | COMPLETE | COMPLETE |
| 16 | Technical interview questions and answers | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | MISSING | MISSING | MISSING | MISSING |
| 17 | Original exam-style practice questions | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | MISSING | MISSING | MISSING | MISSING |
| 18 | Real-world scenario drills | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 19 | Exam decision tree and keyword recognition | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | MISSING | MISSING | PARTIAL | MISSING |
| 20 | Quick-revision cheat sheet and memory model | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 21 | Official references and currency note | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | MISSING | MISSING | MISSING | MISSING |
| 22 | Closing study takeaway | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | COMPLETE | PARTIAL | PARTIAL | PARTIAL | PARTIAL |

## Evidence and concise reasons by topic

### `01-overview.md`

- **Evidence:** the Phase 2 guide implements all 22 ordered functions, including explicit CPP/SAA tracks, policy anatomy and valid JSON, union/intersection and cross-account evaluation, 3 Mermaid workflows, integrations, security, troubleshooting, pricing, 25 traps, 10 interview questions, 30 explained practice questions, 6 architecture scenarios plus scenario drills, navigation, and 15 official references reviewed on 2026-11-05.
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
- **Reason for COMPLETE ratings:** Phase 6 preserved the source's reusable-template analogy, ownership, support-team example, central-update benefit, least-privilege purpose, policy comparison, revision checklist, memory aids, and exact provenance comment. It corrected the false AWS-managed-versioning claim and malformed table, removed the categorical “best practice” claim, and added complete JSON/action/resource/condition reasoning, shared-policy rollout and rollback, privilege-escalation defenses, policy validation, troubleshooting, auditing, pricing, and deployment architecture. Local QA parsed all JSON and checked anchors, relative links, tables, fences, details blocks, counts, UTF-8/LF, whitespace, Mermaid structure, and diff integrity. CLI syntax was verified against official documentation because no local AWS CLI is installed. The referenced provenance CSV remains absent and was not claimed as verified.

### `06-inline-policies.md`

- **Evidence:** the Phase 7 guide implements all 22 functions in 1,100+ lines: embedded ownership and lifecycle; correct user/group/role beneficiary semantics; seven valid JSON examples; trust, boundary, session, SCP/RCP, resource-policy, and cross-account distinctions; CLI and CloudFormation management; two Mermaid diagrams; 30 traps; 12 interview questions; 30 explained practice questions; exactly 12 architecture scenarios; navigation; and 30 official references reviewed on 2026-11-05.
- **Reason for COMPLETE ratings:** Phase 7 preserved the source's glued-note analogy, one-time correction, supported identities, deletion coupling, `BillingAuditRole` example, comparisons, use cases, exam keywords, and memory aids. It corrected one-to-one ownership versus beneficiary scope and added no-ARN/no-native-version behavior, replacement semantics, complete evaluation, role-session revocation nuance, least-privilege administration, IaC, auditing, troubleshooting, cost, and assessment depth. Local QA parsed all JSON and checked anchors, relative links, tables, fences, details blocks, counts, UTF-8/LF, whitespace, Mermaid structure, and diff integrity. CLI syntax was checked against official documentation because the AWS CLI, Markdown linter, and Mermaid renderer are unavailable.

### `07-read-only-access-policy.md`

- **Evidence:** managed-policy/use-case explanation at lines 3-49; alternatives at 92-112; sensitive-data and combined-policy warnings at 116-136.
- **Reason for PARTIAL/MISSING ratings:** the definition/memory aid overpromise “no changes,” no current policy metadata or official source is provided, and SecurityAudit/data access/effective permissions are underdeveloped; no questions/badges/navigation.

### `08-administrator-access-policy.md`

- **Evidence:** broad-access and least-privilege warnings at lines 41-80; root/PowerUser/Identity Center/SCP comparisons at 99-138; traps at 142-179.
- **Reason for PARTIAL/MISSING ratings:** lines 56-61 are invalid JSON; RCP/session/cross-account nuances and escalation risk are absent; no questions/references/badges/navigation.

### `09-access-analyzer.md`

- **Evidence:** five capability groups at lines 40-90; comparisons at 136-171; Region note at 211-215; example at 219-229.
- **Reason for PARTIAL/MISSING ratings:** one workflow collapses separate analyzer types; internal/API and type-specific Region/pricing constraints are missing; policy generation caveats, questions, sources, badges, and navigation are absent.

### `10-root-user.md`

- **Evidence:** root protection at lines 26-67; identity comparisons at 83-109; centralized-root mention at 144-147.
- **Reason for PARTIAL/MISSING ratings:** full-access/MFA language is overbroad, root-only tasks are not sourced, and centralized credential removal/root sessions/recovery plus SCP/RCP behavior are not taught; no explicit SAA section, questions, references, badges, or navigation.

## Priority view

| Priority | Files | Acceptance blocker |
|---|---|---|
| CRITICAL | `08` | Invalid security-policy JSON |
| HIGH | `07`, `09`, `10` | Security guidance, authorization nuance, or current AWS behavior materially incomplete |
| MEDIUM | `README` | The index still lacks integrated outcomes, ownership, and navigation |
| LOW | All | Final visual polish only after accuracy, scope, and references are resolved |
