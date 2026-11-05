# AWS IAM Documentation Completeness Audit

Audit date: **2026-11-05**

Scope: `aws-iam/README.md` and ten numbered IAM lessons

> [!WARNING]
> The Phase 1 prompt was supplied as an attachment, but the separate master specification named similarly to `AWS_CCP_SAA_GitHub_README_Master_Prompt.txt` was not present in the IAM directory or repository filename scan. The audit therefore uses the Phase 1 prompt, repository `AGENTS.md`, current official AWS documentation, and official CLF-C02/SAA-C03 guides. All master-specification-specific judgments are **UNVERIFIED**.

## Executive summary

The collection has a useful beginner-first skeleton and strong topic ordering. Every lesson defines its subject, gives an analogy or example, and flags common misconceptions. `01-overview.md` is substantially stronger than the other lessons: it already covers guardrails, STS, federation, cross-account access, SAA scenarios, knowledge checks, and official references.

The set is not ready to be treated as complete CPP+SAA material. Eight topic files have no certification badge, nine have no official references, only the overview contains explained knowledge-check answers, and most files have no explicit SAA section. Many apparent lists are plain indented text rather than Markdown lists. Important policy and architecture qualifications are absent. The highest-risk defects are invalid AdministratorAccess JSON, incorrect managed-policy versioning, workforce guidance that still defaults to IAM users, incomplete policy-evaluation rules, and oversimplified Access Analyzer/root-user behavior.

Priority totals from this audit:

- **CRITICAL:** 2 defects that can teach invalid syntax or a false product fact.
- **HIGH:** 10 cross-cutting accuracy/completeness issues affecting security decisions or certification objectives.
- **MEDIUM:** substantial missing SAA depth, practice, citations, and Markdown consistency in every short lesson.
- **LOW:** title normalization, navigation polish, and restrained visual improvements.

## Inventory and inspection record

All paths are relative to the IAM directory. All 11 files were read in full.

| File | Lines | Current role | Notable existing strength | Main weakness |
|---|---:|---|---|---|
| `README.md` | 41 | Directory index | Correct lesson order and working sibling links | Generic descriptions; no per-lesson outcomes or previous/next integration |
| `01-overview.md` | 320 | IAM foundation | Broad coverage, both badges, scenarios, explained check, 11 official links | Two stitched teaching layers; limited policy-structure detail and evaluation nuance |
| `02-users.md` | 140 | IAM users | Clear credentials/user/role distinctions | Outdated workforce baseline; little lifecycle/security depth |
| `03-groups.md` | 196 | IAM groups | Correct non-nesting and users-only limitations | Missing union/deny/effective-permission behavior and SAA reasoning |
| `04-roles.md` | 155 | IAM roles | Trust/permissions split, STS, instance-profile distinction | Cross-account, session, federation, and confused-deputy mechanics too shallow |
| `05-customer-managed-policies.md` | 261 | Customer managed policies | Reuse/least-privilege focus and provenance comment | Incorrect version table, malformed table, duplication, missing official sources |
| `06-inline-policies.md` | 396 | Inline policies | Most complete comparison and misconception coverage after overview | Very repetitive; no actual JSON example, references, explained practice set, or SAA section |
| `07-read-only-access-policy.md` | 185 | `ReadOnlyAccess` | Notes sensitive-data risk and policy combinations | Treats policy too much like a semantic guarantee; omits current policy evidence and alternatives |
| `08-administrator-access-policy.md` | 231 | `AdministratorAccess` | Deny/SCP/boundary warnings and root distinction | JSON is invalid; policy interactions and escalation risk are underexplained |
| `09-access-analyzer.md` | 285 | IAM Access Analyzer | Covers external/internal/unused, validation, generation, and comparisons | Collapses separate analyzers; incomplete Region, API, pricing, and generation limitations |
| `10-root-user.md` | 181 | Root user | Strong protection message and centralized-root mention | “Full access” and MFA language need qualifications; centralized behavior is not properly taught |

## Current strengths

- File order progresses logically from IAM foundations through identities, policies, analysis, and root protection.
- Existing filenames follow repository naming rules and README links resolve locally.
- Analogies and short summaries are beginner-friendly.
- Core distinctions—user/group/role, trust versus permissions policies, managed versus inline, root versus admin—are mostly directionally correct.
- `01-overview.md` preserves substantial advanced material and a dated official reference set.
- `05-customer-managed-policies.md` contains a provenance comment that must be preserved pending investigation.
- `06-inline-policies.md` explicitly corrects several common misconceptions.
- `07` and `08` correctly warn that managed policies combine with other applicable policies and are not automatically least privilege.
- `09` correctly distinguishes access analysis from permission grants and CloudTrail activity logging.

## Confirmed technical errors and material inaccuracies

| Priority | Location | Finding | Required correction/evidence |
|---|---|---|---|
| **CRITICAL** | `08-administrator-access-policy.md:56-61` | The fenced block is invalid JSON: property names/strings are unquoted and `Action`/`Resource` have no values. | Replace with the current official document containing `"Version": "2012-10-17"`, `"Effect": "Allow"`, `"Action": "*"`, and `"Resource": "*"`. |
| **CRITICAL** | `05-customer-managed-policies.md:231-238` | The comparison says AWS managed policies have no versioning. AWS creates versions when it updates AWS managed policies; customers cannot edit them or choose their versions as they can with customer managed policies. | Explain ownership/control separately from version history. Preserve the valid five-saved-version rule for customer managed policies. |
| **HIGH** | `02-users.md:5,9,13-17,53-59`; also `01-overview.md:25,36` | The material presents IAM users as the normal employee/daily-access pattern. Current AWS best practice requires human users to use federation and temporary credentials, recommending IAM Identity Center for centralized workforce access. | Reframe IAM users as account-scoped long-term identities for exceptions/legacy/specific workloads; lead with federation for workforce users. |
| **HIGH** | `05-customer-managed-policies.md:231-238` | The “table” is plain text and labels customer managed policies categorically “Best practice” and AWS managed policies “For beginners.” This is not a valid decision rule. | Compare customer control, reuse, update owner, versions, and least-privilege fit without absolute recommendations. |
| **HIGH** | `09-access-analyzer.md:94-106` | “Create an analyzer” is presented as producing external, internal, or unused findings from one configuration. AWS requires separate analyzer types; internal, external, and unused analysis have different scopes and behavior. | Teach three analyzer types and their separate configuration explicitly. |
| **HIGH** | `09-access-analyzer.md:211-215` | Region behavior mentions only external access. External and internal analyzers are Regional; unused-access findings do not vary by Region and do not require one analyzer per resource Region. | Replace with a type-by-type Region table. |
| **HIGH** | `10-root-user.md:5,32-35,75` | Unqualified “full access to everything” can imply root bypasses every guardrail. A member-account root user is affected by applicable SCPs and RCPs; identity policies and permissions boundaries cannot be attached to root. | Explain root’s inherent account permissions and the organization-policy exceptions. |
| **HIGH** | `10-root-user.md:77` | “MFA must be enabled” states a recommendation as an automatic requirement. | Say AWS strongly recommends MFA; distinguish best practice from enforced configuration. |

## High-impact omissions and misleading simplifications

| Priority | Location | Gap or risk |
|---|---|---|
| **HIGH** | `01-overview.md:229-235`; `06-inline-policies.md:123-125` | The “allow unless explicit deny” shorthand omits important unions/intersections, RCPs, same-account resource-principal exceptions, cross-account two-sided authorization, and the fact that boundaries/session policies can limit without an explicit deny. |
| **HIGH** | `04-roles.md:51-68` | Cross-account assumption lacks the two halves: target trust plus caller permission to call `sts:AssumeRole`, followed by session effective permissions. No external ID or `aws:SourceArn`/`aws:SourceAccount` confused-deputy protection. |
| **HIGH** | `07-read-only-access-policy.md:5-7,54-72,179` | “Look but not edit”/“See everything, change nothing” is too absolute. `ReadOnlyAccess` is the current enumerated AWS policy, can expose data and security/billing metadata, changes when AWS updates it, and does not constrain permissions granted by other policies. |
| **HIGH** | `09-access-analyzer.md:57-61` | Internal findings lack the current constraints: selected supported resources, separate analyzer, effective-path analysis, and API-specific availability considerations. |
| **HIGH** | `09-access-analyzer.md:86-90` | Policy generation omits its CloudTrail-trail/service-role prerequisites and major caveats (for example action-level coverage limits, no S3 data-event action identification, `iam:PassRole` omission, and manual review). |
| **HIGH** | `10-root-user.md:144-147` | Centralized root access is only a trap note. It needs a full explanation: after enablement, new Organizations member accounts have no root credentials by default; existing credentials can be removed; some privileged tasks can use short-term root sessions; recovery can be temporarily allowed for remaining root-only tasks. |
| **MEDIUM** | `03-groups.md:43-76` | Missing effective-permission union across group/direct policies, explicit-deny precedence, removal effects when another allow remains, and the difference from Identity Center groups/permission sets. |
| **MEDIUM** | `05-customer-managed-policies.md:65-76` | Missing policy ARN, default version, editing as a new version, rollback, attachment blast radius, validation, safe rollout, and detach/delete lifecycle. |
| **MEDIUM** | `06-inline-policies.md:95-134` | Describes JSON but supplies no valid policy document. Missing full effective-permission context and limitations/operational trade-offs. |
| **MEDIUM** | `08-administrator-access-policy.md:69-80` | Missing RCPs and session-policy limits; “resource-based policy situations” is too vague. It also does not explain privilege escalation/pass-role risk, permission-set use, or controlled emergency access. |

## File-by-file assessment and upgrade checklist

### `README.md` — MEDIUM priority

**Assessment:** structurally sound index, but too generic to guide study or expose certification depth.

- Preserve lesson order and working parent links.
- Replace repeated “study notes and decision points” text with specific outcomes.
- State the federation-first workforce baseline and identify where policy evaluation, cross-account access, and root management are taught.
- Add concise use guidance and integrated previous/next navigation after lessons stabilize.
- Do not turn the README into a duplicate IAM lesson.

### `01-overview.md` — HIGH priority

**Assessment:** strongest file and a viable foundation, but **PARTIAL**, not complete.

- Reconcile the early employee-IAM-user example with later Identity Center guidance.
- Add the complete policy document anatomy (`Version`, `Statement`, `Sid`, `Effect`, `Principal` where supported, `Action`/`NotAction`, `Resource`/`NotResource`, `Condition`).
- Expand policy types to include RCPs, VPC endpoint policies, resource-based trust policies, and session policies without overloading CPP.
- Teach evaluation as a request-context decision: default deny, grants, intersections/guardrails, explicit deny, same-account resource-policy nuances, and cross-account two-sided allow.
- Qualify IAM global scope versus Regional STS endpoints and Regional Access Analyzer behavior.
- Separate CPP recognition from SAA architecture; retain federation, Identity Center, STS, cross-account, SCP, boundaries, and scenarios.
- Normalize headings into repository structure and add navigation.

### `02-users.md` — HIGH priority

**Assessment:** clear beginner definition, but current access guidance is materially outdated and SAA depth is **MISSING**.

- Define console password, access keys, MFA devices/passkeys/security keys, signing certificates/service-specific credentials only where relevant.
- Make federation/Identity Center the workforce default and roles the workload default; document legitimate IAM-user exceptions.
- Cover creation defaults (no permissions and credentials only when configured), account scope, direct/group policies, permissions boundary, tags, credential report, access advisor, and CloudTrail attribution.
- Explain secure access-key creation/storage/rotation/deactivation/deletion and why “rotate routinely” is not a substitute for removing long-term keys.
- Add password-policy scope and MFA enforcement through policy conditions where appropriate.
- Add CPP/SAA sections, decision scenarios, questions, official sources, and sibling links.

### `03-groups.md` — MEDIUM priority

**Assessment:** core restrictions are correct; policy behavior and architecture relevance remain **PARTIAL**.

- Explain that groups are not principals, cannot appear as `Principal`, have no credentials, contain only IAM users, and cannot nest.
- Cover multiple memberships and union of applicable allows, with explicit deny and other guardrails taking precedence.
- Explain that removal from one group may not remove access granted elsewhere.
- Compare IAM groups with Identity Center groups plus permission sets and with roles.
- Add safe joiner/mover/leaver examples, troubleshooting, CPP/SAA distinction, questions, and official references.

### `04-roles.md` — HIGH priority

**Assessment:** good conceptual base; critical SAA architecture detail is **PARTIAL/MISSING**.

- Define principal, trust policy, permissions policies, role session, session name, duration, role chaining, and temporary credential components.
- Explain the `AssumeRole` request and effective session permissions, including optional session policies/tags and applicable boundaries/SCPs/RCPs.
- Cover service roles, service-linked roles, EC2 instance profiles, Lambda execution roles, ECS task roles, federation, web identity, and cross-account roles at appropriate depth.
- Teach two-sided cross-account authorization and confused-deputy defenses: third-party `ExternalId`; service `aws:SourceArn`, `aws:SourceAccount`, or organization keys when supported.
- Add troubleshooting failure cases, CloudTrail session attribution, comparisons, valid trust-policy example, questions, and sources.

### `05-customer-managed-policies.md` — CRITICAL priority

**Assessment:** useful facts are mixed with a confirmed false comparison and malformed imported material.

- Correct AWS-managed-policy versioning and rebuild the plain-text comparison as valid Markdown.
- Preserve the provenance comment; its target `docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv` was not found and requires investigation.
- Explain standalone policy ARN, attachments, permissions-boundary use, default version, five saved versions, rollback, nondefault deletion, and change blast radius.
- Add valid least-privilege JSON, Access Analyzer validation, testing/deployment workflow, and when an inline or AWS managed policy is preferable.
- Remove repetition only after preserving every distinct fact. Add SAA change-management scenarios, explained questions, sources, and navigation.

### `06-inline-policies.md` — MEDIUM priority

**Assessment:** broad and generally correct, but verbose and unsupported by examples/references.

- Preserve the one-to-one, lifecycle, identity-based, and “not automatically safer” explanations.
- Add one validated JSON example and show how it combines with other applicable policies.
- Clarify that an inline policy is embedded in one user, group, or role; it is not a standalone object or permissions boundary.
- Add operational drawbacks: discovery, review, duplication, drift, and reuse; give a precise narrow-use decision rule.
- Convert examiner prompts into original practice questions with explained/distractor answers.
- Add CPP/SAA separation, official references, badges after scope validation, and navigation.

### `07-read-only-access-policy.md` — HIGH priority

**Assessment:** sound cautionary intent, but policy behavior is oversimplified.

- Cite current policy ARN/version/date and explain it is an enumerated AWS-maintained policy, not a semantic enforcement boundary.
- Explicitly warn that it can read data in services such as S3/DynamoDB and exposes security/billing/operational metadata.
- Explain effective permissions when other policies allow writes and when denies/guardrails restrict reads.
- Compare `ReadOnlyAccess`, service-specific read-only policies, `IAMReadOnlyAccess`, `SecurityAudit`, and a customer policy by use case.
- Add sensitive-data scenario, least-privilege decision framework, practice questions, official sources, and navigation.

### `08-administrator-access-policy.md` — CRITICAL priority

**Assessment:** central message is correct, but the invalid JSON makes the file unsafe as a technical reference.

- Replace the JSON with the exact validated policy and add ARN/version metadata.
- Teach what can restrict an admin: explicit denies, SCPs, RCPs, permissions boundaries, session policies, and cross-account resource trust.
- Explain that it is not root and cannot perform root-only tasks; root in a member account can itself be restricted by organization policies.
- Cover privilege escalation, `iam:PassRole`, credential compromise impact, Identity Center permission sets, just-in-time/emergency access, MFA, logging, and narrower alternatives.
- Recheck `PowerUserAccess` against its current policy rather than relying on a slogan.
- Add failure scenarios, questions, sources, and navigation.

### `09-access-analyzer.md` — HIGH priority

**Assessment:** good feature inventory but insufficiently precise for current product behavior.

- Separate external, internal, and unused analyzer configuration, scope, pricing, and Region behavior.
- Define zone of trust, account versus organization analyzers, delegated administrator, supported resource types, finding states, archive rules, and remediation ownership.
- Add internal-analysis selected-resource/API constraints and distinguish policy reasoning from activity evidence.
- Explain policy validation categories, custom policy checks, access previews, and policy generation prerequisites/limitations.
- Compare Policy Simulator, CloudTrail, Config, Security Hub CSPM, and Access Analyzer by question answered.
- Add cost fundamentals, realistic failures, questions, current official sources, and navigation.

### `10-root-user.md` — HIGH priority

**Assessment:** strong beginner security message; modern Organizations behavior and permission qualifications are **PARTIAL**.

- Distinguish standalone/management-account root credentials from centrally managed member-account root access.
- Explain inherent root permissions, SCP/RCP applicability, and why identity policies/boundaries cannot be attached to root.
- Replace broad task examples with a sourced list of tasks that actually require root credentials versus tasks delegable to IAM/billing identities.
- Cover phishing-resistant MFA where possible, no root access keys, secure recovery channels, monitoring, and emergency procedures.
- Explain centralized root credential removal, root sessions for supported privileged tasks, temporary recovery, and post-task credential removal.
- Compare root, AdministratorAccess, Identity Center administrators, and organization management; add questions and official sources.

## Missing CPP coverage

The official CLF-C02 Domain 2 guide explicitly includes IAM, root-user protection, least privilege, IAM Identity Center, access keys, password policies, credential storage, MFA, cross-account roles, users/groups/custom and managed policies, root-only tasks, and federation. The largest gaps are:

- Federation/Identity Center as the preferred human-access pattern is not consistently taught.
- Access-key/password lifecycle and storage are too shallow in `02`.
- Root-only task recognition and modern root protection are too vague in `10`.
- Managed/custom/inline distinctions contain a false versioning claim in `05`.
- Most lessons lack explicit CPP quick revision and explained questions.

## Missing SAA coverage

The official SAA-C03 Task 1.1 includes secure access across multiple accounts, federation/Identity Center, least privilege, flexible users/groups/roles/policies, STS and role switching, cross-account access, SCPs, resource policies, and directory federation. The largest gaps are:

- Accurate effective-permission and cross-account evaluation model.
- Role-session mechanics, session policies/tags, duration/chaining, and confused-deputy protections.
- Multi-account delegated administration, SCP/RCP interactions, and centralized root access.
- Architecture trade-offs and realistic failure/troubleshooting scenarios.
- Operational policy change/version/testing workflow.
- Purposeful selection among Access Analyzer, Policy Simulator, CloudTrail, Config, and Security Hub.

## Exam-oriented, formatting, and navigation gaps

- Nine topic files have neither official references nor checked dates; only `01` cites official sources.
- Only `01` has a collapsible answer set. `06` has interview-style prompts but no distractor reasoning; the rest have no practice questions.
- CPP/SAA separation is absent outside the overview; many files name only Cloud Practitioner despite meaningful SAA relevance.
- Eight topic files have no badge; `05` has CPP only and `01` has both. Badges must be supported after content upgrades, not added mechanically.
- Most bullet-like lines lack `-`, so GitHub renders them as wrapped prose rather than lists.
- `05` has an invalid plain-text table and duplicated “related services” material; `08` has invalid JSON.
- Only the IAM README has navigation. Topic files need stable index/previous/next links.
- The repository uses SAA badge color `#0969DA`; the Phase 1 prompt’s `#2374D9` must not override it.
- No Mermaid diagram is currently required. A single policy-evaluation flow in `01` may add value; repeating diagrams would not.

## Cross-file inconsistencies

- `01` eventually recommends Identity Center, while its early example and `02` teach direct IAM users for employees as the default.
- `01` calls AWS managed policies versioned indirectly through citations/current behavior, while `05` explicitly says they have no versioning.
- `07` says “read-only” broadly prevents changes, while correctly admitting another policy can grant writes; the policy-versus-effective-permission distinction needs one consistent model.
- `08` says admin is constrained by boundaries/SCPs but omits session policies/RCPs; `10` describes root as unlimited without organization-policy qualifications.
- Policy terminology varies (`permission policy`, `IAM policy`, `managed policy`) without consistently distinguishing attachment, grant, and guardrail roles.
- The overview has current references dated 2026-07-22; the other files provide no evidence for recent Access Analyzer or root-management claims.

## Claims requiring future re-verification

These were checked against official sources on 2026-11-05 but are volatile and must be rechecked when their file is upgraded:

- Current JSON/version/change date for `ReadOnlyAccess`, `AdministratorAccess`, `PowerUserAccess`, `SecurityAudit`, and service-specific managed policies.
- IAM Access Analyzer supported resources, internal-access interface/API availability, analyzer quotas, pricing, Regions, policy-generation action coverage, and Security Hub integration.
- Centralized root access supported privileged tasks, recovery behavior, Organizations prerequisites, and member-account defaults.
- Exact IAM quotas such as customer managed policy saved versions.
- Current CLF-C02 and SAA-C03 guide revisions and in-scope services.

Unresolved source limitations:

- The separate master specification was not found; exact compliance and its exact 22-function mapping cannot be verified.
- The provenance file named in `05-customer-managed-policies.md:5` was not found by repository filename scan.

## Official verification set

Checked **2026-11-05**:

- [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM policy types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Cross-account evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html)
- [Confused deputy protections](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html)
- [Managed policy versioning](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
- [`AdministratorAccess` reference](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html)
- [AWS managed job-function policies (`ReadOnlyAccess`)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)
- [IAM Access Analyzer concepts](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html)
- [IAM Access Analyzer setup and Region behavior](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html)
- [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)
- [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)
- [CLF-C02 Domain 2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html)
- [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html)

## Readiness decision

The repository is **ready for Prompt 2 with limitations**: the actual overview and its dependencies have been audited, upgrade rules and ownership boundaries exist, and no original file was changed. Before claiming master-specification compliance, locate/provide the missing master specification and reconcile its exact 22 content functions with the proxy matrix in `02-COVERAGE-MATRIX.md`.
