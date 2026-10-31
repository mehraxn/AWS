# CPP Implementation Backlog

This is the authorized file-level backlog derived from the 2026-07-27 [coverage matrix](CPP-COVERAGE-MATRIX.md). Items are ordered by dependency and learner value. `P0` closes missing or path-blocking evidence; `P1` closes important partial depth; `P2` standardizes or maintains complete evidence.

Every content item must follow the [CPP content and style standard](../content-standards/CPP-CONTENT-AND-STYLE-STANDARD.md), preserve useful existing facts, use official AWS sources, and pass local link, naming, and Markdown checks. A batch may be split into smaller reviewable changes.

## Batch 2: Cloud Concepts

### CPP-B2-01 — Migration strategy foundation

- **Domain / official requirement:** Domain 1; Task 1.3 cloud adoption strategies, migration resources, AWS CAF outcomes, and strategy selection.
- **Current status / priority:** `partial`; P0.
- **Canonical file:** create `11-migration-and-hybrid-cloud/01-cpp-migration-strategies.md`.
- **Files to modify:** `11-migration-and-hybrid-cloud/README.md`, CAF overview, Migration Hub, DMS, SCT, Snowball Edge, and root/CPP learner navigation.
- **Depth / size:** Level 3; large.
- **Exact content and style changes:** explain migration journey, business benefits, CAF outcomes, common strategy families, online replication versus offline transfer, and resource-to-stage selection; keep implementation detail optional.
- **Knowledge check / comparison:** three original scenarios with explained alternatives; include a strategy-to-tool comparison.
- **Official-source requirement:** CLF-C02 Domain 1, AWS CAF, AWS migration strategy guidance, DMS, and Snow Family documentation.
- **Acceptance criteria:** all four Task 1.3 rows reach complete; canonical map links resolve; no tool lesson repeats the full strategy definition.
- **Dependencies:** none.

### CPP-B2-02 — Licensing economics

- **Domain / official requirement:** Domain 1; Task 1.4 BYOL versus included licensing.
- **Current status / priority:** `mention-only`; P1.
- **Canonical file:** modify `01-cloud-fundamentals/02-cloud-concepts-and-benefits.md`.
- **Files to modify:** pricing study guide; create `12-billing-pricing-and-support/aws-license-manager/01-overview.md` for Level 1 service recognition.
- **Depth / size:** Level 2 concept plus Level 1 service; medium.
- **Exact content and style changes:** define Bring Your Own License (BYOL), license-included, mobility/eligibility caveats, Dedicated Host relevance, and License Manager purpose without legal advice.
- **Knowledge check / comparison:** one BYOL-versus-included scenario with explained answer; compact comparison required.
- **Official-source requirement:** CLF-C02 Domain 1 and current AWS License Manager/licensing documentation.
- **Acceptance criteria:** learner can distinguish purchasing the AWS resource from software licensing; no unsupported license eligibility claim.
- **Dependencies:** none.

### CPP-B2-03 — Cloud-concepts link consolidation

- **Domain / official requirement:** Domain 1; Tasks 1.1, 1.2, and 1.4.
- **Current status / priority:** `complete` with duplicate-evidence risk; P2.
- **Canonical file:** keep current owners in the canonical map.
- **Files to modify:** `01-cloud-fundamentals/README.md`, billing README, Well-Architected overview, and relevant comparison links.
- **Depth / size:** Levels 2–3; small.
- **Exact content and style changes:** identify each canonical owner in navigation and replace repeated introductory definitions with short context plus links where safe.
- **Knowledge check / comparison:** no new questions required; retain existing checks.
- **Official-source requirement:** existing official sources are sufficient; recheck touched volatile claims.
- **Acceptance criteria:** no broken links; definitions remain in canonical owners; no useful fact is removed.
- **Dependencies:** CPP-B2-01.

## Batch 3: Security and Compliance

### CPP-B3-01 — Governance and compliance overview

- **Domain / official requirement:** Domain 2; Task 2.2 governance, compliance, geographic/industry needs, and service-dependent requirements.
- **Current status / priority:** `partial`; P0.
- **Canonical file:** modify `09-security-and-compliance/security-and-compliance-overview/01-overview.md`.
- **Files to modify:** security README, Artifact, Audit Manager, compliance programs, and Shared Responsibility links.
- **Depth / size:** Level 3; large.
- **Exact content and style changes:** distinguish governance, compliance, assurance evidence, and customer obligations; add Region/industry and EC2/RDS/S3 examples; replace repetitive broad claims with precise links.
- **Knowledge check / comparison:** three explained scenarios; Artifact versus Audit Manager versus general compliance resources comparison.
- **Official-source requirement:** CLF-C02 Domain 2, AWS Compliance, Artifact, Audit Manager, and Shared Responsibility documentation.
- **Acceptance criteria:** CPP-2.2-K1, S2, and S6 become complete; every volatile program claim is sourced and dated or removed.
- **Dependencies:** none.

### CPP-B3-02 — Credential and root-user decision guidance

- **Domain / official requirement:** Domain 2; Task 2.3 access keys, password policies, credential storage, and root-only tasks.
- **Current status / priority:** `partial`; P1.
- **Canonical file:** modify `03-identity-governance-and-organizations/aws-iam/01-overview.md`.
- **Files to modify:** root-user lesson, Identity Center overview, Secrets Manager, Systems Manager, IAM README.
- **Depth / size:** Level 3; medium.
- **Exact content and style changes:** compare human/workload access, temporary/long-term credentials, password policies, Secrets Manager/Parameter Store purpose, and a short current list of root-only tasks.
- **Knowledge check / comparison:** two credential-selection scenarios plus one root-only-task question with explained alternatives.
- **Official-source requirement:** IAM root-user and security credential best-practice documentation, checked on implementation date.
- **Acceptance criteria:** CPP-2.3-S1 and S4 become complete; no absolute claim that conflicts with newer centralized root-access capabilities.
- **Dependencies:** none.

### CPP-B3-03 — Security information and Marketplace resources

- **Domain / official requirement:** Domain 2; Task 2.4 security documentation and third-party security products.
- **Current status / priority:** one `missing`, two `partial`; P0.
- **Canonical file:** modify `09-security-and-compliance/README.md`; link to the Marketplace owner from CPP-B6-03.
- **Files to modify:** security overview, Trusted Advisor, and CPP learner path.
- **Depth / size:** Level 2; medium.
- **Exact content and style changes:** distinguish Security Center, Security Blog, Knowledge Center/re:Post knowledge resources, official service docs, and third-party Marketplace products.
- **Knowledge check / comparison:** one resource-location scenario and one AWS-service-versus-third-party scenario.
- **Official-source requirement:** official AWS security resources and Marketplace documentation.
- **Acceptance criteria:** CPP-2.4-K2, S2, and S3 become complete; links are direct and descriptive.
- **Dependencies:** CPP-B6-03.

### CPP-B3-04 — Awareness security services

- **Domain / official requirement:** Domain 2 supporting in-scope recognition.
- **Current status / priority:** service ownership planned; P2.
- **Canonical file:** create `09-security-and-compliance/aws-cloudhsm/01-overview.md` and `09-security-and-compliance/amazon-detective/01-overview.md`.
- **Files to modify:** security README, service index, security comparison.
- **Depth / size:** Level 1; medium.
- **Exact content and style changes:** purpose, use cases, closest distractor, management boundary, and short exam tip; CloudHSM versus KMS and Detective versus GuardDuty/Security Hub distinctions.
- **Knowledge check / comparison:** one explained recognition question per service; comparison links required.
- **Official-source requirement:** current CloudHSM and Detective documentation.
- **Acceptance criteria:** both planned canonical paths exist, use CPP badges only when mapping remains official, and avoid SAA implementation depth.
- **Dependencies:** none.

## Batch 4: Core Technology and Services

### CPP-B4-01 — AWS access, provisioning, and operations

- **Domain / official requirement:** Domain 3; all Task 3.1 criteria.
- **Current status / priority:** one `mention-only`, three `partial`; P0.
- **Canonical file:** create `10-monitoring-management-and-deployment/01-access-deployment-and-operations.md`.
- **Files to modify:** category README, CloudFormation, cloud fundamentals, and CPP learner path.
- **Depth / size:** Level 3; large.
- **Exact content and style changes:** define Console, CLI, SDK, API, and infrastructure as code; compare human interactive, scripted, application, and repeatable provisioning; link cloud/hybrid/on-premises models.
- **Knowledge check / comparison:** four scenarios with explained distractors; method-selection comparison required.
- **Official-source requirement:** CLF-C02 Domain 3, AWS Management Console, CLI, SDK/tooling, API, and CloudFormation documentation.
- **Acceptance criteria:** all six Task 3.1 rows are complete; CLI and Console planned service ownership is satisfied.
- **Dependencies:** none.

### CPP-B4-02 — Route 53 beginner refocus

- **Domain / official requirement:** Domain 3; Task 3.5 purpose of Route 53.
- **Current status / priority:** `partial`; P1.
- **Canonical file:** modify `07-networking-and-content-delivery/amazon-route-53/01-overview.md`.
- **Files to modify:** networking README and DNS/edge comparison.
- **Depth / size:** Level 2; medium.
- **Exact content and style changes:** lead with authoritative DNS, domain registration, health checks, and routing; move advanced routing detail below CPP material; correct heading hierarchy.
- **Knowledge check / comparison:** one Route 53 versus CloudFront/Global Accelerator question with explained alternatives.
- **Official-source requirement:** Route 53 Developer Guide and FAQs.
- **Acceptance criteria:** CPP-3.5-S3 becomes complete and beginner section is reachable in one click from CPP path.
- **Dependencies:** none.

### CPP-B4-03 — Core service ownership links

- **Domain / official requirement:** Domain 3; Tasks 3.3–3.6.
- **Current status / priority:** `complete` with navigation and duplication risk; P2.
- **Canonical file:** existing compute/storage/database/network owners.
- **Files to modify:** category READMEs, core selection guide, database selection guide, service index.
- **Depth / size:** Levels 2–3; medium.
- **Exact content and style changes:** label essential CPP owners, supporting detail, and optional SAA-depth lessons; remove no content.
- **Knowledge check / comparison:** no new checks required; ensure comparison links use consistent criteria.
- **Official-source requirement:** recheck only factual claims touched.
- **Acceptance criteria:** every core topic has one visible owner and supporting links; internal link validation passes.
- **Dependencies:** CPP-B4-01 and CPP-B4-02.

## Batch 5: Secondary and Awareness-Level Services

### CPP-B5-01 — Additional category recognition guide

- **Domain / official requirement:** Domain 3; Task 3.8 all categories.
- **Current status / priority:** six `partial`, two `missing`; P0.
- **Canonical file:** create `14-ai-ml-analytics-and-other-services/01-cpp-additional-service-recognition.md`.
- **Files to modify:** category README and CPP learner path.
- **Depth / size:** Levels 1–2; large.
- **Exact content and style changes:** provide a category-to-business-need map for application integration, business applications, customer enablement, developer tools, end-user computing, frontend/mobile, and IoT; link service owners instead of duplicating long definitions.
- **Knowledge check / comparison:** at least seven explained recognition scenarios, one per category.
- **Official-source requirement:** CLF-C02 Task 3.8 and current in-scope service pages.
- **Acceptance criteria:** every Task 3.8 requirement has a visible path; the guide remains recognition-focused.
- **Dependencies:** CPP-B5-02 through B5-05.

### CPP-B5-02 — End-user computing recognition

- **Domain / official requirement:** Domain 3; Task 3.8 AppStream 2.0, WorkSpaces, and WorkSpaces Secure Browser.
- **Current status / priority:** `missing`; P0.
- **Canonical file:** create `14-ai-ml-analytics-and-other-services/end-user-computing/01-service-recognition.md`.
- **Files to modify:** category README and additional category guide.
- **Depth / size:** Level 2 for selection; medium.
- **Exact content and style changes:** distinguish application streaming, managed virtual desktops, and secure browser access; explain what reaches the endpoint.
- **Knowledge check / comparison:** three scenarios with explained alternatives; required three-way comparison.
- **Official-source requirement:** official documentation for all three services.
- **Acceptance criteria:** CPP-3.8-K5 and S5 become complete; no unsupported device or protocol claims.
- **Dependencies:** none.

### CPP-B5-03 — Missing database, analytics, and container recognition

- **Domain / official requirement:** Domain 3 supporting service recognition.
- **Current status / priority:** planned ownership; P1.
- **Canonical files:** create OpenSearch Service, DocumentDB, Neptune, and ECR paths specified in the canonical map.
- **Files to modify:** analytics, database, and compute READMEs plus selection guides.
- **Depth / size:** Level 1; large.
- **Exact content and style changes:** purpose, common use, closest distractor, management model, and concise exam tip for each service.
- **Knowledge check / comparison:** one explained question per service; link to category comparison.
- **Official-source requirement:** current official service overviews and FAQs.
- **Acceptance criteria:** four paths exist; names are current; no implementation walkthroughs are added.
- **Dependencies:** none.

### CPP-B5-04 — Missing migration and disaster-recovery services

- **Domain / official requirement:** Domains 1 and 3 supporting migration/transfer recognition.
- **Current status / priority:** planned ownership; P1.
- **Canonical files:** create Application Migration Service, Migration Evaluator, and Elastic Disaster Recovery paths from canonical map.
- **Files to modify:** migration README, migration strategy owner, DR strategy lesson.
- **Depth / size:** Level 1; large.
- **Exact content and style changes:** distinguish discovery/assessment, server migration, database migration, and continuous replication for disaster recovery.
- **Knowledge check / comparison:** three explained recognition questions and a compact selection table.
- **Official-source requirement:** current MGN, Migration Evaluator, and DRS documentation.
- **Acceptance criteria:** no use of retired service names as current products; all canonical links resolve.
- **Dependencies:** CPP-B2-01.

### CPP-B5-05 — SNS, IoT Core, business applications, and developer lifecycle

- **Domain / official requirement:** Domain 3; Task 3.8 integration, business, developer, and IoT skills.
- **Current status / priority:** `partial`; P1.
- **Canonical file:** create `08-serverless-and-application-integration/amazon-sns/01-overview.md`; modify IoT Core, Connect, SES, CodeBuild, CodePipeline, and X-Ray navigation.
- **Files to modify:** relevant READMEs and comparison guides.
- **Depth / size:** Levels 1–3; large.
- **Exact content and style changes:** give SNS a service owner; add Connect-versus-SES, build-versus-pipeline-versus-tracing, and IoT Core-versus-Greengrass distinctions.
- **Knowledge check / comparison:** one explained scenario for each decision set.
- **Official-source requirement:** official service docs and current out-of-scope list for Greengrass context.
- **Acceptance criteria:** CPP-3.8-K1/K2/K4/K7 and S1/S2/S4/S7 are complete without expanding out-of-scope services.
- **Dependencies:** none.

## Batch 6: Billing, Pricing, and Support

### CPP-B6-01 — Reserved Instance organization behavior

- **Domain / official requirement:** Domain 4; Task 4.1 Reserved Instance behavior in Organizations.
- **Current status / priority:** `partial`; P1.
- **Canonical file:** modify pricing study guide.
- **Files to modify:** Reserved Instances lesson and Organizations overview.
- **Depth / size:** Level 2; small.
- **Exact content and style changes:** explain discount sharing/scope at CPP depth, distinguish capacity from discount behavior, and date the claim.
- **Knowledge check / comparison:** one multi-account scenario with explained alternatives.
- **Official-source requirement:** current EC2 billing/RI and Organizations documentation.
- **Acceptance criteria:** CPP-4.1-S3 becomes complete; no fixed discount percentage is introduced.
- **Dependencies:** none.

### CPP-B6-02 — Support Center and Health API

- **Domain / official requirement:** Domain 4; Task 4.3 Support Center and Trusted Advisor/Health/Health API.
- **Current status / priority:** `partial`; P1.
- **Canonical file:** modify `12-billing-pricing-and-support/aws-support/02-support-plans.md`.
- **Files to modify:** Health Dashboard, Trusted Advisor, support README.
- **Depth / size:** Level 3; medium.
- **Exact content and style changes:** define case management via Support Center, distinguish public Service Health from account-specific Health, and explain Health API purpose/access without hard-coded entitlements.
- **Knowledge check / comparison:** two resource-selection scenarios with explained alternatives.
- **Official-source requirement:** current AWS Support and Health documentation, with checked date.
- **Acceptance criteria:** CPP-4.3-K4 and S4 become complete; volatile plan facts remain dated.
- **Dependencies:** none.

### CPP-B6-03 — AWS Marketplace canonical lesson

- **Domain / official requirement:** Domains 2 and 4; third-party security products and Marketplace cost/governance/entitlement capabilities.
- **Current status / priority:** `missing`; P0.
- **Canonical file:** create `12-billing-pricing-and-support/aws-marketplace/01-overview.md`.
- **Files to modify:** billing README, security resources, partner lesson, service index.
- **Depth / size:** Level 2; medium.
- **Exact content and style changes:** define catalog/procurement purpose, seller types, software/security products, private offers/entitlements/governance at stable conceptual depth, and distinguish Marketplace from APN and Support.
- **Knowledge check / comparison:** two explained scenarios; Marketplace/APN/Support comparison required.
- **Official-source requirement:** current AWS Marketplace documentation and CLF-C02 Domains 2/4.
- **Acceptance criteria:** CPP-2.4-S2 and CPP-4.3-S8 become complete; no commercial claim lacks an official source.
- **Dependencies:** none.

### CPP-B6-04 — Billing freshness pass

- **Domain / official requirement:** Domain 4; pricing and Support evidence quality.
- **Current status / priority:** file-level freshness risk; P1.
- **Canonical file:** existing billing owners.
- **Files to modify:** the 12-billing lessons flagged in the phase report, only where a volatile claim is confirmed.
- **Depth / size:** Level 2; large.
- **Exact content and style changes:** replace unnecessary exact figures with stable drivers; add checked dates and direct sources where exact facts are educationally necessary.
- **Knowledge check / comparison:** update questions only if their answer depends on changed facts.
- **Official-source requirement:** direct official pricing, Support, Free Tier, Health, or product-status sources.
- **Acceptance criteria:** no confirmed volatile claim remains undated; no stable lesson receives decorative dates.
- **Dependencies:** CPP-B6-01 through B6-03.

## Batch 7: Comparisons and Decision Guides

### CPP-B7-01 — Apply the comparison standard

- **Domain / official requirement:** Cross-domain CPP scenario selection.
- **Current status / priority:** inconsistent criteria; P1.
- **Canonical file:** all 19 active comparison lessons under `15-comparisons-and-decision-guides/`.
- **Files to modify:** comparison README and only guides missing decision criteria.
- **Depth / size:** Levels 2–3; large.
- **Exact content and style changes:** normalize purpose, best fit, responsibility, scalability, availability, pricing driver, wording, confusion, and when-not-to-use criteria where relevant.
- **Knowledge check / comparison:** each Level 3 guide receives at least one explained scenario.
- **Official-source requirement:** direct official service docs for material distinctions.
- **Acceptance criteria:** no large prose-in-table regressions; every guide names its canonical service owners.
- **Dependencies:** content batches 2–6.

### CPP-B7-02 — Link-first duplicate consolidation

- **Domain / official requirement:** Cross-domain canonical ownership.
- **Current status / priority:** duplicate-evidence risk; P1.
- **Canonical file:** owners in canonical map.
- **Files to modify:** IAM child lessons, pricing/RI/Savings Plans, support resources, networking guide, migration guides, AI catalog.
- **Depth / size:** all; large.
- **Exact content and style changes:** replace repeated full definitions with context and canonical links only after fact-by-fact comparison; preserve every distinct useful fact.
- **Knowledge check / comparison:** retain checks at the file where the decision is taught.
- **Official-source requirement:** reverify facts moved into owners.
- **Acceptance criteria:** consolidation log records every merge/archive decision; no content deletion without explicit authorization; links pass.
- **Dependencies:** CPP-B7-01 and all planned owners used by a consolidation.

## Batch 8: Content and Style Standardization

### CPP-B8-01 — Heading, acronym, and badge normalization

- **Domain / official requirement:** Cross-domain editorial quality.
- **Current status / priority:** inconsistent; P1.
- **Canonical file:** all active CPP-relevant lessons.
- **Files to modify:** begin with the five multi-H1 files and the 128 lessons without recognized badges; change badges only after scope verification.
- **Depth / size:** all; large.
- **Exact content and style changes:** one H1, logical heading increments, acronym-first-use, current product spelling, and accurate badges/classification review markers.
- **Knowledge check / comparison:** no forced question additions in this mechanical pass.
- **Official-source requirement:** official scope maps for badges and official product pages for names.
- **Acceptance criteria:** Markdown structure check passes; no badge inferred from filename alone.
- **Dependencies:** canonical map accepted.

### CPP-B8-02 — References and volatile-claim normalization

- **Domain / official requirement:** Cross-domain source quality.
- **Current status / priority:** 136 lessons without recognized References heading; 20 freshness candidates without a date; P1.
- **Canonical file:** active CPP owners first, then supporting lessons.
- **Files to modify:** file-level list in phase report and subsequent validator output.
- **Depth / size:** all; large.
- **Exact content and style changes:** add descriptive official references, remove raw link dumps, date verified volatile facts, and avoid adding empty/reference-only headings.
- **Knowledge check / comparison:** cite volatile answer rationale when useful.
- **Official-source requirement:** official AWS only for scope and volatile facts.
- **Acceptance criteria:** every Level 2/3 canonical CPP owner has official references; all confirmed volatile claims have context.
- **Dependencies:** batches 2–7.

### CPP-B8-03 — Empty directory and navigation hygiene

- **Domain / official requirement:** Repository maintainability.
- **Current status / priority:** 25 empty active-category directories; P2.
- **Canonical file:** repository map and service index.
- **Files to modify:** no content files unless an empty directory becomes a planned service owner.
- **Depth / size:** not applicable; small.
- **Exact content and style changes:** review empty directories against planned destinations; remove only empty directories when explicitly authorized, or populate them through prior backlog items.
- **Knowledge check / comparison:** not applicable.
- **Official-source requirement:** not applicable.
- **Acceptance criteria:** no linked empty directory; any removal is logged; no learning content is deleted.
- **Dependencies:** batches 2–6.

## Batch 9: Domain Quizzes and Mock Exams

### CPP-B9-01 — Explained domain quizzes

- **Domain / official requirement:** All domains; apply official skills.
- **Current status / priority:** no canonical domain quiz set; P1.
- **Canonical files:** create `16-exam-preparation/cloud-practitioner/01-cloud-concepts-quiz.md` through `04-billing-pricing-and-support-quiz.md`.
- **Files to modify:** CPP learner path and exam-preparation README.
- **Depth / size:** Level 3; large.
- **Exact content and style changes:** original questions balanced across matrix criteria; scenario first, service trivia only for Level 1 requirements.
- **Knowledge check / comparison:** every question includes correct rationale, plausible-alternative rationale, related lesson, and useful official source.
- **Official-source requirement:** current CLF-C02 guide and official service docs; no dumps or recalled questions.
- **Acceptance criteria:** all 134 criteria have at least one traceable quiz mapping across the set; integrity review passes.
- **Dependencies:** content batches 2–8.

### CPP-B9-02 — Full mock exams and weak-domain review

- **Domain / official requirement:** Cross-domain readiness practice.
- **Current status / priority:** mock exams absent; P1.
- **Canonical files:** create two or more original mock exam files under `16-exam-preparation/cloud-practitioner/mock-exams/` and a weak-domain review worksheet.
- **Files to modify:** learner path.
- **Depth / size:** Level 3; large.
- **Exact content and style changes:** mix domains approximately in official weight proportions without claiming exact exam reproduction; provide separate explained answers and remediation links.
- **Knowledge check / comparison:** mock format itself; all distractors explained.
- **Official-source requirement:** official guide for domain weights and scope.
- **Acceptance criteria:** no confidential/recalled content; every question maps to a matrix ID; learner can calculate weak-domain results.
- **Dependencies:** CPP-B9-01.

## Batch 10: Final CPP Verification and Release

### CPP-B10-01 — Requirement-level re-audit

- **Domain / official requirement:** all 134 criteria.
- **Current status / priority:** final gate; P0.
- **Canonical file:** update coverage matrix and dashboard from current evidence.
- **Files to modify:** canonical map, backlog statuses, service index, known limitations.
- **Depth / size:** all; large.
- **Exact content and style changes:** rescore from lesson bodies, record evidence headings and checked dates, and retain unresolved statuses honestly.
- **Knowledge check / comparison:** verify quiz mapping, not merely question counts.
- **Official-source requirement:** recheck current exam guide, technologies/concepts, and service lists.
- **Acceptance criteria:** denominator and status counts reconcile automatically/manual double-check; every requirement has an owner or destination.
- **Dependencies:** batches 2–9.

### CPP-B10-02 — Final validation and learner-path release review

- **Domain / official requirement:** repository quality gates.
- **Current status / priority:** final gate; P0.
- **Canonical file:** create a release validation record under `docs/final-review/`.
- **Files to modify:** root README, CPP path, documentation index only if validation exposes issues.
- **Depth / size:** not applicable; medium.
- **Exact content and style changes:** run link, naming, duplicate, heading, placeholder, empty-directory, temp/generated, badge, reference, and exam-integrity checks; document failures without hiding them.
- **Knowledge check / comparison:** verify explained-answer standard on a sample and aggregate report.
- **Official-source requirement:** confirm scope check date.
- **Acceptance criteria:** all blocking validators pass; non-blocking warnings have owners; no commit or push occurs without explicit authorization.
- **Dependencies:** CPP-B10-01.
