# CPP Content and Style Standard

This standard governs learner-facing material for AWS Certified Cloud Practitioner (CLF-C02). It complements the repository-wide rules in [`AGENTS.md`](../../AGENTS.md) and [`docs/content-standards.md`](../content-standards.md). When guidance differs, use the more specific CPP rule without weakening factual accuracy or SAA material.

## Purpose

A CPP lesson should help a beginner define a concept, recognize it in context, understand why it matters, distinguish nearby options, and make a basic scenario choice. It should not become an architecture implementation manual simply because deeper details are available.

## CPP Depth Model

### Level 1 — Recognition

Use for lower-priority or awareness-level services. A learner should know:

- what the service or concept is;
- its primary purpose;
- one or two common uses;
- the closest common distractor;
- whether it is managed, serverless, or customer-managed when relevant.

Typical Level 1 topics include Amazon SES, Amazon Connect, AppStream 2.0, WorkSpaces Secure Browser, AWS AppSync, AWS Amplify, AWS IoT Core, individual prebuilt AI services, and less central in-scope migration or developer tools.

### Level 2 — Foundational understanding

Use for important CPP concepts and services. A learner should know:

- definition and problem solved;
- high-level operation and main features;
- common uses and business relevance;
- pricing fundamentals without memorizing volatile rates;
- Shared Responsibility implications;
- related services and meaningful distinctions;
- common exam wording and traps.

Typical Level 2 topics include AWS CAF, Well-Architected, IAM identities and policies, AWS Organizations, CloudTrail, CloudWatch, Config, CloudFormation, RDS, DynamoDB, Lambda, ECS/EKS/Fargate, Route 53, AWS Backup, cost-management tools, and Support resources.

### Level 3 — CPP scenario reasoning

Use for heavily tested choices. A learner should be able to read a short business scenario, select the relevant principle or service, explain the fit, reject plausible alternatives, and identify basic cost, security, availability, or operational implications.

Typical Level 3 topics include cloud benefits, Shared Responsibility across EC2/RDS/Lambda, global infrastructure, root-user protection and least privilege, core compute/storage/database/network selection, encryption and security-service selection, pricing models, cost-tool selection, Support-plan selection, and SQS/SNS/EventBridge distinctions.

Level 3 CPP reasoning is not SAA architecture depth. CPP does not require detailed subnet calculations, complex policy evaluation, implementation commands, advanced failure modeling, or multi-service architecture design unless clearly marked as optional deeper reading.

## Canonical Ownership

- Every CPP concept or service has one primary learning owner in the [canonical content map](../certification-audit/CPP-CANONICAL-CONTENT-MAP.md).
- A service lesson defines and teaches the service. A comparison guide teaches a decision across services. An index only navigates.
- Supporting lessons should link to the owner, add context specific to their subject, and avoid copying the full definition.
- Do not merge, archive, or rename learning material without checking links and updating the migration log required by `AGENTS.md`.
- When an owner does not exist, use the planned path in the canonical map rather than creating an alternate filename.

## Language

Learner-facing content must:

- use clear international English and short, direct sentences where practical;
- define an acronym on first use in a lesson;
- explain a concept before comparing it;
- prefer concrete AWS examples over abstract claims;
- distinguish a general cloud principle from an AWS implementation;
- use current official AWS product names;
- avoid marketing language, unexplained jargon, and unnecessary academic detail;
- qualify claims instead of using unsupported `always`, `never`, or `best`;
- explain that requirements determine the answer; keywords alone do not;
- avoid promises of exam success or claims about unverified exam frequency.

## Lesson Patterns

### Important Level 2 or Level 3 lesson

Use the headings that materially help the topic; do not add empty sections.

1. Overview
2. What Problem It Solves
3. Simple Explanation
4. How It Works
5. Main Features
6. Common Use Cases
7. Pricing Fundamentals
8. Security and Shared Responsibility
9. Related Services and Comparisons
10. Common Exam Scenarios
11. Exam Traps
12. Summary
13. Knowledge Check
14. Explained Answers
15. References

SAA content may follow under an explicitly labeled `SAA Architecture and Design` heading. It must not interrupt the CPP explanation.

### Short Level 1 lesson

1. Overview
2. Main Purpose
3. Common Use Cases
4. Key Distinction
5. Exam Tip
6. Knowledge Check
7. Explained Answer
8. References

## Knowledge Checks

Every meaningful check should contain:

- a question;
- answer choices when a service or concept selection is being tested;
- the correct answer;
- why it is correct;
- why each plausible alternative is incorrect;
- a related canonical lesson;
- an official reference when the answer depends on a volatile or easily confused feature.

Questions should test reasoning, not obscure recall. Avoid `all of the above`, trick grammar, leaked or recalled exam content, and choices that are wrong only because of unstated assumptions.

Use this compact pattern:

```markdown
## Knowledge Check

Which option best meets the stated requirement?

A. ...
B. ...
C. ...
D. ...

<details>
<summary>Show explained answer</summary>

**Correct answer: B.** Explain the requirement-to-service match.

- **A:** Explain the plausible but incorrect fit.
- **C:** Explain the plausible but incorrect fit.
- **D:** Explain the plausible but incorrect fit.

Related: [Canonical lesson](relative-path.md).

</details>
```

## Comparison Guides

Use consistent criteria where relevant:

| Criterion | Question to answer |
|---|---|
| Primary purpose | What problem is each option intended to solve? |
| Best fit | Which requirement points to each option? |
| Management responsibility | What does AWS operate and what remains with the customer? |
| Scalability model | How does capacity respond to demand at CPP depth? |
| Availability model | What resilience is inherent and what must the customer configure? |
| Pricing driver | Which usage dimension mainly drives cost? |
| Common wording | What scenario language is useful context, without treating it as a guarantee? |
| Common confusion | Why is a nearby service tempting but wrong? |
| When not to use it | Which requirement rules the option out? |

Use a table only when it improves scanning. Put nuanced reasoning below the table rather than forcing paragraphs into cells.

## Exam Tips and Traps

An exam tip must teach a transferable decision clue and its context. It may say, for example, that a requirement for historical cost analysis points toward Cost Explorer, while an alert threshold points toward Budgets. It must not say that a single keyword guarantees an answer.

An exam trap should explain the misconception and the corrective rule. It must not reconstruct confidential exam material or claim that a topic appears a certain percentage of the time.

## Pricing and Volatile Facts

- Prefer stable pricing drivers and purchasing behavior over exact rates.
- Exact prices, quotas, Free Tier terms, Support-plan features, product availability, Region counts, retirement status, and time limits require a direct official source and `Checked: YYYY-MM-DD`.
- A checked date does not make a claim permanent. Add neutral wording that the detail can change.
- Do not infer current product status from an old lesson or audit.

## References

- Prefer direct official AWS documentation, FAQs, pricing pages, framework pages, and current certification guides.
- Use descriptive Markdown links, not long raw-link dumps.
- Cite the claim nearest the reference when the relationship is not obvious.
- Third-party material may supplement but not decide exam scope or volatile facts.
- Paraphrase. Do not copy large passages from AWS or training providers.

## Badges and Scope Labels

- Use the exact badge syntax in [`docs/certification-labels.md`](../certification-labels.md).
- A CPP badge means meaningful, officially supported CLF-C02 relevance; it does not mean complete coverage.
- Use both badges only when both official mappings are supported.
- Mark uncertain mappings `Classification: review required` rather than guessing.
- Label optional architecture-heavy sections `Optional SAA-depth material` or `SAA Architecture and Design`.

## Editorial Acceptance Checklist

Before a CPP lesson is accepted:

- [ ] Canonical ownership is confirmed.
- [ ] Required depth is identified as L1, L2, or L3.
- [ ] The definition and problem solved are clear to a beginner.
- [ ] Acronyms are defined on first use.
- [ ] Service names and scope are current.
- [ ] Pricing and responsibility are addressed when relevant.
- [ ] Nearby alternatives are distinguished.
- [ ] Exam tips teach reasoning rather than keyword matching.
- [ ] The knowledge check has an explained answer at the required depth.
- [ ] Official references support factual and volatile claims.
- [ ] Local links and heading hierarchy pass repository validation.
- [ ] The lesson does not duplicate its canonical owner or bury CPP content under SAA detail.

## Maintenance

Review this standard when the CLF exam code, official task statements, in-scope service list, repository lesson template, or badge policy changes. Record substantive changes in the relevant phase report rather than silently changing the rules.
