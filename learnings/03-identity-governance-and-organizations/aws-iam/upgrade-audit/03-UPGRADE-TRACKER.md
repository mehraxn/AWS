# AWS IAM Upgrade Tracker

Audit baseline: **2026-11-05**

> [!WARNING]
> Phase 1 could not find the master specification. Phase 2 found and read `AWS_CCP_SAA_GitHub_README_Master_Prompt.txt`, reconciled the rules and 22-function matrix, and preserved the higher-priority repository SAA badge color `#0969DA` instead of the master's `#2374D9`.

## Phase status

| Order | Phase | File or scope | Status | Primary dependency |
|---:|---|---|---|---|
| 1 | IAM Overview | `01-overview.md` | COMPLETE | Completed 2026-11-05; establishes shared terminology and policy-evaluation model |
| 2 | IAM Users | `02-users.md` | COMPLETE | Completed 2026-11-05; establishes user credentials, lifecycle, exception use, and workforce alternatives |
| 3 | IAM Groups | `03-groups.md` | COMPLETE | Completed 2026-11-05; establishes group membership, inherited permissions, and the Identity Center distinction |
| 4 | IAM Roles | `04-roles.md` | COMPLETE | Completed 2026-11-05; establishes trust, STS sessions, workload/service roles, and cross-account design |
| 5 | Customer Managed Policies | `05-customer-managed-policies.md` | COMPLETE | Completed 2026-11-05; establishes reusable policies, JSON, versioning, boundaries, rollout, and multi-account deployment |
| 6 | Inline Policies | `06-inline-policies.md` | COMPLETE | Completed 2026-11-05; establishes embedded ownership, beneficiary scope, lifecycle, evaluation, and operational trade-offs |
| 7 | ReadOnlyAccess | `07-read-only-access-policy.md` | NOT STARTED | Current AWS managed-policy reference |
| 8 | AdministratorAccess | `08-administrator-access-policy.md` | NOT STARTED | Current policy JSON and guardrail explanations |
| 9 | IAM Access Analyzer | `09-access-analyzer.md` | NOT STARTED | Analyzer types, current scope, pricing, and Region behavior |
| 10 | Root User | `10-root-user.md` | NOT STARTED | Current centralized root-access documentation |
| 11 | Main IAM README integration | `README.md` | NOT STARTED | All ten canonical lessons stable |
| 12 | Final cross-document QA | Entire IAM directory | NOT STARTED | README integration complete and all topic phases complete |

## Per-file acceptance criteria

Every upgraded lesson must satisfy all applicable criteria:

- [ ] Accurate title, supported CPP/SAA badges, and stable filename.
- [ ] Beginner definition plus accurate technical definition and problem statement.
- [ ] Topic-specific concepts, prerequisites, defaults, constraints, and exceptions.
- [ ] Valid step-by-step behavior and effective-permission explanation where relevant.
- [ ] Clear when-to-use and when-not-to-use guidance.
- [ ] Explicit CPP recognition material and SAA design reasoning at suitable depth.
- [ ] At least one useful scenario; comparisons and decision table where they add value.
- [ ] Accurate exam traps, quick revision aid, and original explained practice questions.
- [ ] Valid JSON, Markdown, links, anchors, callouts, and Mermaid (if used).
- [ ] Official AWS references supporting material claims and a checked date for volatile facts.
- [ ] Existing unique facts and provenance preserved or deliberately reconciled.
- [ ] Previous/next/index navigation works; terminology agrees with sibling files.
- [ ] Diff reviewed and original unrelated material unchanged.

## Dependencies and cross-file conflicts

| Issue | Files affected | Resolution rule |
|---|---|---|
| IAM user versus federated workforce guidance | `01`, `02`, `03`, `10` | Identity Center/federation is the preferred human-access baseline; IAM users are exceptions |
| Effective-permission wording | `01`, `03`, `05`, `06`, `07`, `08` | Own the full model in `01`; use precise, linked topic-specific subsets elsewhere |
| Role assumption and cross-account access | `01`, `04` | `04` owns the mechanics and confused-deputy controls; `01` summarizes |
| AWS managed-policy behavior | `05`, `07`, `08` | Cite current policy reference; distinguish AWS updates from customer-managed versions |
| Root versus administrator | `08`, `10` | `10` owns root-only tasks and centralized root access; `08` owns policy restrictions |
| Access Analyzer versus Policy Simulator/CloudTrail/Security Hub | `09` | Use a decision table and avoid claiming equivalent enforcement or audit functions |
| SAA badge color conflict | All files | Repository `AGENTS.md` (`#0969DA`) overrides Phase 1 prompt (`#2374D9`) |
| Missing provenance map referenced by comment | `05` | Locate/recover the source map before editing or preserve the comment with a documented limitation |
| Master specification reconciliation | All phases | Completed in Phase 2; use the actual 22 functions and repository badge convention |

## Verified corrections and unresolved issues log

Add one row after every future prompt. Do not mark a correction verified without an official source or a reproducible validation.

| Date | Prompt/file | Verified corrections | Unresolved issues | Sources checked | Reviewer/status |
|---|---|---|---|---|---|
| 2026-11-05 | Phase 1 audit | Baseline only; no original lesson changed | Master specification and referenced provenance map not found | Official IAM, Organizations, Access Analyzer, managed-policy, CLF-C02, and SAA-C03 docs | Audit complete; upgrades NOT STARTED |
| 2026-11-05 | Phase 2 / `01-overview.md` | Federation-first workforce guidance; complete policy anatomy; union/intersection and resource-principal nuances; cross-account two-sided evaluation; RCPs; regional STS; current root and Access Analyzer behavior | Provenance map for file `05` remains missing; Mermaid renderer unavailable, so diagrams received static syntax/balance review only; recheck volatile claims during final QA | 20 official AWS pages resolved; 3 JSON blocks parsed; anchors, links, tables, fences, HTML, counts, and whitespace checked | IAM Overview COMPLETE; remaining topics NOT STARTED |
| 2026-11-05 | Phase 3 / `02-users.md` | Federation-first workforce baseline; console/long-term/temporary credential separation; two-key staged replacement; current password/MFA behavior; complete permission evaluation; lifecycle, audit, troubleshooting, and compromise response | AWS CLI, Mermaid renderer, and Markdown linter unavailable; CLI syntax checked against official command documentation and Mermaid received static syntax/balance review; recheck volatile credential/MFA facts during final QA | 22 official AWS references; 2 JSON blocks parsed; 3 Mermaid blocks, 22 anchors/TOC links, 30 question details, tables, relative links, UTF-8/LF, whitespace, and diff checked | IAM Users COMPLETE; topics `03`–`10` remain NOT STARTED |
| 2026-11-05 | Phase 4 / `03-groups.md` | Account-local, non-principal group model; multi-group inherited permission evaluation; explicit deny and guardrail behavior; group policy types and deletion cleanup; cross-account role pattern; federation-first Identity Center distinction; lifecycle, audit, troubleshooting, and least-privilege operations | AWS CLI, Mermaid renderer, and Markdown linter unavailable; CLI syntax checked against official command documentation and Mermaid received static syntax/balance review; recheck volatile quotas and Identity Center behavior during final QA | 24 official AWS references; 2 JSON blocks parsed; 2 Mermaid blocks, 22 anchors/TOC links, 28 question details, 28 traps, 10 interview questions, 10 scenarios, tables, relative links, UTF-8/LF, whitespace, and diff checked | IAM Groups COMPLETE; topics `04`–`10` remain NOT STARTED |
| 2026-11-05 | Phase 5 / `04-roles.md` | Persistent role versus temporary session; trust versus service authorization; same-account and cross-account assumption; STS operations, duration, chaining, policies, tags, and source identity; EC2/Lambda/ECS/EKS credential patterns; federation and Identity Center; service and service-linked roles; scoped `PassRole`; third-party and cross-service confused-deputy defenses; auditing, troubleshooting, and revocation | AWS CLI, Mermaid renderer, and Markdown linter unavailable; CLI syntax checked against official command documentation and Mermaid received static syntax/balance review; recheck volatile STS limits, EKS platform support, service principals, and integration-specific condition keys during final QA | 37 official AWS references; 7 JSON blocks parsed; 2 Mermaid blocks, 22 anchors/TOC links, 32 question details, 34 traps, 12 interview questions, exactly 12 scenarios, tables, relative links, UTF-8/LF, whitespace, and diff checked | IAM Roles COMPLETE; topics `05`–`10` remain NOT STARTED |
| 2026-11-05 | Phase 6 / `05-customer-managed-policies.md` | Correct AWS/customer managed versioning distinction; policy-language versus saved-version IDs; five-version/default/rollback behavior; standalone account-scoped ARN and attachments; valid JSON/action/resource/condition examples; boundaries and full effective permissions; shared-policy blast radius; defensive version/attachment administration; multi-account IaC and Identity Center references; validation, auditing, troubleshooting, and least-privilege lifecycle | Referenced provenance CSV remains absent and was not claimed as verified; AWS CLI, Mermaid renderer, and Markdown linter unavailable; CLI syntax checked against official documentation and Mermaid received static syntax/balance review; recheck volatile quotas, service authorization data, Identity Center behavior, pricing, and exam scope during final QA | 25 official AWS references resolved; 8 JSON blocks parsed; 2 Mermaid blocks, 22 anchors/TOC links, 30 question details, 32 traps, 12 interview questions, exactly 12 scenarios, tables, relative links, UTF-8/LF, whitespace, and diff checked | Customer Managed Policies COMPLETE; topics `06`–`10` remain NOT STARTED; ready for Prompt 7 |
| 2026-11-05 | Phase 7 / `06-inline-policies.md` | Correct embedded-versus-attached terminology; one-to-one ownership versus group-member and role-session beneficiaries; user/group/role support; no standalone ARN or native managed-policy versions; create-or-replace modification; identity deletion coupling; role trust separation; boundaries, session policies, SCPs/RCPs, resource policies, and cross-account evaluation; role-session revocation; CLI/IaC inventory; least-privilege administration, auditing, and troubleshooting | AWS CLI, Mermaid renderer, and Markdown linter unavailable; CLI syntax checked against official documentation and Mermaid received static syntax/balance review; recheck volatile service authorization data, CloudFormation behavior, Organizations controls, pricing, and exam scope during final QA | 30 official AWS references resolved; 7 JSON blocks parsed; 2 Mermaid blocks, 22 anchors/TOC links, 30 question details, 30 traps, 12 interview questions, exactly 12 scenarios, tables, relative links, UTF-8/LF, whitespace, and diff checked | Inline Policies COMPLETE; topics `07`–`10` remain NOT STARTED; ready for Prompt 8 |

## Final QA checklist

- [x] Master specification found and its exact 22 functions reconciled with the Phase 1 proxy audit.
- [ ] All ten topic phases and README integration marked complete with evidence.
- [ ] No contradictory definitions, duplicated generic blocks, or broken sibling links.
- [ ] Current AWS managed policies and date-sensitive root/Access Analyzer claims rechecked.
- [ ] Certification badges and CPP/SAA depth reviewed against current official guides.
- [ ] Repository validators run; JSON and Mermaid examples independently validated.
- [ ] `git diff` contains only approved content changes; no commit or push performed.
