# IAM Documentation Upgrade Rules

> [!IMPORTANT]
> These rules were reconciled on 2026-11-05 with `AWS_CCP_SAA_GitHub_README_Master_Prompt.txt`, the Phase 1 and Phase 2 prompts, and repository `AGENTS.md`. Phase 1's missing-specification limitation is historical and no longer blocks later phases.

## Purpose and authority

Apply these rules to later upgrades of the ten IAM lessons and the IAM directory README. In a conflict, follow repository instructions first, then the active phase prompt, then the master specification, then this file. A phase prompt's explicit target filename overrides the master's generic output contract, so do not create a duplicate `README.md` when a numbered lesson is the only authorized target. Preserve useful facts and provenance; do not silently discard distinct material.

## Visual and Markdown conventions

- Use one H1 with the current AWS topic name and a logical H2/H3 hierarchy.
- Use the repository badges exactly as defined in `AGENTS.md`. CPP uses `#2EA44F`; SAA uses the repository-approved badge color `#0969DA`. The master specification requests SAA blue `#2374D9`, but the higher-priority repository convention controls unless the repository rule is changed.
- Add a badge only when the file contains supported coverage for that certification. Mark uncertain mappings for review.
- Use valid CommonMark lists, fenced code blocks with language identifiers, and compact tables only when comparison is clearer than prose.
- Use GitHub callouts sparingly: `NOTE` for useful context, `TIP` for decisions, `IMPORTANT` for exam/security essentials, `WARNING` for risk, and `CAUTION` for destructive or high-impact outcomes.
- Use Mermaid only when a relationship or evaluation flow is materially clearer as a diagram. Keep labels short, syntax GitHub-compatible, and provide explanatory prose.
- Include relative previous/next or IAM-index navigation. Keep existing stable filenames and relative links.
- Use UTF-8, LF line endings, and no trailing whitespace. Avoid decorative emoji and repeated horizontal rules.

## Required teaching progression

Use only sections meaningful to the topic; never add empty headings for template compliance.

1. Overview: simple and accurate technical definitions.
2. What problem it solves and a bounded analogy.
3. Core concepts, terminology, prerequisites, defaults, limitations, and ownership.
4. How it works step by step, with policy or request evaluation where relevant.
5. Common use cases, when to use it, and when not to use it.
6. Security, shared responsibility, operations, cost/pricing, resilience, performance, or scalability only where meaningful.
7. Explicit `CPP Knowledge` and `SAA Architecture and Design` sections at appropriate depth.
8. Comparisons, scenarios, exam traps, summary, original practice questions with explained answers, and official references.

## Master specification's 22 learning functions

Address each function where it meaningfully applies; state `NOT APPLICABLE` rather than inventing content for a narrow topic.

1. What the topic is: simple/technical definitions, analogy, memory model, and at-a-glance facts.
2. Problem solved: before/after, realistic uses, and why basic alternatives are insufficient.
3. Core concepts and components: terminology, resources, policies, credentials, and relationships.
4. How it works: setup-to-operation sequence, examples, prerequisites, defaults, and a useful workflow diagram.
5. Key features and capabilities: function, example, exam meaning, restrictions, and conditions.
6. Real-world use cases: selection and rejection criteria.
7. Visibly separated CPP essentials: facts, keywords, recognition scenarios, misconceptions, and 30-second recap.
8. Visibly separated SAA deep dive: architecture, trade-offs, security, failure behavior, and substantial scenarios.
9. Comparison with similar/confusable AWS services or features.
10. Integration and architecture patterns.
11. Security, permissions, compliance, and shared responsibility.
12. Observability, auditing, troubleshooting, and failure behavior.
13. Pricing and cost optimization, or a clear explanation when pricing is not meaningful.
14. Safe, syntactically correct practical configuration/CLI/IaC example where useful.
15. Meaningful exam traps with the mechanism behind harder cases.
16. Increasingly difficult technical interview questions with answers.
17. Original exam-style practice questions with collapsible explained answers and distractor analysis.
18. Real-world scenario drills.
19. Exam-question decision tree and keyword recognition.
20. Quick-revision cheat sheet, memory model, and one-sentence exam answer.
21. Official references, inline citations for nuanced claims, and an accurate review date.
22. Closing study takeaway for both certification levels.

Numeric ranges in the master are quality targets for broad topics, not filler quotas. Scale them to topic scope as the master instructs.

## File ownership boundaries

| File | Primary responsibility | Cross-link rather than duplicate |
|---|---|---|
| `01-overview.md` | IAM mental model, policy types and structure, evaluation, federation, Identity Center, STS, cross-account access, SCPs, RCPs, boundaries, and session policies | Detailed identity/policy examples owned below |
| `02-users.md` | IAM-user credentials, legitimate exceptions, MFA, password/access-key lifecycle, group permissions, and migration to temporary credentials | Role mechanics and broad policy taxonomy |
| `03-groups.md` | Membership, inherited permissions, multiple-group union, deny precedence, non-nesting, and Identity Center group comparison | General user credential management |
| `04-roles.md` | Trust versus permissions policies, STS sessions, service roles, instance profiles, federation, cross-account trust, and confused-deputy defenses | Full policy evaluation taxonomy |
| `05-customer-managed-policies.md` | Reusable customer policies, JSON, versions/default version, attachment, change impact, and least privilege | Inline-policy detail |
| `06-inline-policies.md` | One-to-one embedding, lifecycle, supported identities, JSON, evaluation, and managed/resource-policy comparison | Managed-policy versioning |
| `07-read-only-access-policy.md` | Current `ReadOnlyAccess` behavior, sensitive-data exposure, effective permissions, and narrower alternatives | Generic IAM basics |
| `08-administrator-access-policy.md` | Exact policy behavior, effective restrictions, escalation risk, root distinction, Identity Center permission sets, and safer alternatives | Root-only operations |
| `09-access-analyzer.md` | External, internal, and unused analyzers; scope, Region behavior, findings, validation, checks, generation, pricing, and comparisons | General policy evaluation |
| `10-root-user.md` | Root identity, required tasks, recovery, MFA, no long-term keys, root versus admin, and centralized root access | Routine IAM/Identity Center administration |
| `README.md` | Accurate learning order, concise objectives, certification focus, and navigation | Lesson-level teaching content |

## Certification depth

- CPP material must prioritize recognition: IAM purpose; users, groups, roles, and policies; access keys and passwords; MFA; least privilege; federation and IAM Identity Center; cross-account roles; root protection and root-only tasks. Do not imply implementation or architecture depth is required by CLF-C02.
- SAA material must add design reasoning: temporary credentials, trust boundaries, identity- and resource-based authorization, cross-account two-sided evaluation, effective-permission guardrails, multi-account controls, confused-deputy defenses, troubleshooting, and scenario trade-offs.
- Separate the two levels explicitly. Do not label a generic paragraph as SAA coverage merely because it mentions an AWS service.

## Accuracy and terminology

- Distinguish authentication, authorization, principal, identity, credentials, policy, and effective permissions.
- State that implicit deny is the default and applicable explicit deny wins, but teach unions/intersections and same-account versus cross-account/resource-principal nuances before using slogans.
- Never say a boundary, SCP, RCP, or session policy grants permissions. Explain what principal/resource each limits.
- Distinguish a role trust policy from its permissions policies and distinguish an IAM role from its STS role session.
- Recommend federation and IAM Identity Center with temporary credentials for workforce access. Present IAM users and long-term access keys as exception-based, not the modern default.
- Qualify “IAM is global”: IAM resources are global within an AWS account, while STS endpoints, IAM Access Analyzer analyzers/findings, and service resources can have Regional behavior.
- Treat AWS managed policies as mutable dependencies maintained by AWS, not inherently least privilege.
- Verify current managed-policy JSON and metadata immediately before publication.
- Treat quotas, prices, supported Regions/resources/actions, exam scope, and recent root-access behavior as date-sensitive. Add `Sources checked: YYYY-MM-DD`.

## Examples, comparisons, and assessment

- Examples must be technically valid, original, least-privilege-oriented, and clearly marked as examples. Validate all JSON; use `"Version": "2012-10-17"` where appropriate.
- Comparison tables must answer a decision, not repeat definitions. Include meaningful dimensions such as credential duration, attachment location, trust, reuse, effective-permission impact, or operational ownership.
- Include realistic success and failure scenarios. Explain why each option is correct or unsafe.
- Practice questions must be original, aligned to the named certification level, and use collapsible answers where helpful. Explain the correct answer and the key distractors; do not reproduce recalled exam questions.
- Exam keywords and traps must be accurate clues, not claims about exam frequency.
- Quick revision aids must summarize decisions and exceptions rather than repeat entire sections.

## Sources and preservation

- Cite official AWS documentation and current official CLF-C02/SAA-C03 exam guides as primary sources. Use deep links supporting the nearby claim.
- Paraphrase; do not reproduce AWS course slides or large copyrighted passages. Treat private course material only as background.
- Never invent features, policy syntax, prices, quotas, Regions, APIs, exam frequency, customer stories, or references.
- Preserve existing useful unique content, comments, links, and provenance. The existing provenance comment in `05-customer-managed-policies.md` points to a file not found in the repository scan; investigate before changing it.
- Keep content moves separate from rewrites. For any later approved move, merge, rename, or archive, use `git mv` and update the repository migration log.
- Before and after every upgrade, inspect `git status`, review the diff, validate links/anchors/JSON/Mermaid, and record verified corrections and unresolved issues in `upgrade-audit/03-UPGRADE-TRACKER.md`.

## Acceptance floor

A lesson is complete only when it is accurate, self-contained for its topic, appropriately scoped for CPP and SAA, free of invalid examples, supported by official references, navigable, and tested for Markdown quality. A heading alone does not satisfy a function. Meaningful topic depth takes priority over numeric targets or repeated generic material.
