# Phase 6 Batch 8 Content Decisions

## AWS-044 — AWS pricing fundamentals

### Official requirement

Explain AWS pricing dimensions and select among On-Demand, Reserved Instances, Savings Plans, Spot Instances, storage, and transfer options.

### Required CPP depth

Fundamental recognition, purpose, billing drivers, and straightforward selection scenarios.

### Required SAA depth

Scenario-ready cost decisions with commitment, flexibility, interruption, capacity, resilience, security, and operational trade-offs.

### Canonical target

`12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md`

### Existing files reviewed

The target, the Savings Plans guide, EC2 purchasing lessons, cost-management service notes, and the Batch 2 compute selection guide.

### Official sources used

AWS Pricing, the Savings Plans User Guide, and current Amazon EC2 purchasing and pricing documentation.

### Verification date

2026-07-25.

### Gap being resolved

Uneven comparisons and unsafe exact price or discount claims prevented a durable canonical pricing owner.

### CPP content added

Cloud economics, cost dimensions, service drivers, purchasing-model recognition, exam cues, and knowledge checks.

### SAA cost-optimization content added

Commitment scope, discount-versus-capacity separation, interruption tolerance, storage/database dimensions, and cost-aware architecture scenarios.

### Pricing or support scenarios added

Steady compute, variable fleets, fault-tolerant batch, uncertain demand, storage, and transfer scenarios.

### Existing content preserved

Useful fixed-versus-variable cost concepts, purchasing-model distinctions, storage drivers, and exam-oriented reasoning were retained in corrected form.

### Content removed or corrected

Unsupported prices, discount percentages, overbroad transfer claims, and outdated Savings Plans coverage were replaced with current conceptual guidance.

### Badge decision

CPP and SAA badges are supported by fundamental and scenario-ready evidence.

### Navigation and map updates

The billing index, task maps, concept matrix, depth matrix, inventory, badge audit, dashboards, and repository status were updated.

### Acceptance-criteria result

Completed at the exact backlog target.

### Remaining work

None for AWS-044; future exact estimates still require the live pricing pages.

### Validation result

Passed the final Batch 8 validation command set.

## AWS-045 — AWS Support

### Official requirement

Teach the current Support plan lineup, feature distinctions, technical-response source, account assistance, Trusted Advisor, and AWS Health.

### Required CPP depth

Fundamental plan recognition and scenario-based selection.

### Required SAA depth

Awareness only; AWS Support is not mapped as a standalone SAA service requirement in the current audit.

### Canonical target

`12-billing-pricing-and-support/aws-support/02-support-plans.md`

### Existing files reviewed

Both AWS Support lessons, Trusted Advisor and AWS Health lessons, the freshness audit, and the prior Batch 1 security clarification.

### Official sources used

AWS Support plan documentation, the plan-transition notice, Trusted Advisor documentation, and the AWS Health User Guide.

### Verification date

2026-07-25.

### Gap being resolved

The prior lesson used obsolete plan names and volatile prices, response values, and entitlement claims.

### CPP content added

Current plan comparison, selection cues, account-assistance distinctions, Trusted Advisor and Health concepts, mistakes, and knowledge checks.

### SAA cost-optimization content added

None claimed beyond useful awareness of operational support trade-offs.

### Pricing or support scenarios added

Self-service, production technical support, designated account guidance, and broad operations scenarios.

### Existing content preserved

The useful distinctions between self-service, technical support, proactive guidance, and account-team assistance were retained.

### Content removed or corrected

The five-plan legacy comparison, stale prices, copied numeric response targets, and blanket entitlement claims were removed or dated.

### Badge decision

CPP retained; no SAA badge.

### Navigation and map updates

Support navigation and directly affected audits and CPP mappings were updated.

### Acceptance-criteria result

Completed at the exact backlog target with the current commercial lineup.

### Remaining work

None for AWS-045; response commitments must always be read from the linked current AWS comparison.

### Validation result

Passed the final Batch 8 validation command set.

## AWS-046 — Cost management tools

### Official requirement

Compare estimation, analysis, budgets, anomaly monitoring, detailed exports, allocation, and consolidated billing tools.

### Required CPP depth

Fundamental service-purpose recognition and tool selection.

### Required SAA depth

Scenario-ready governance and cost-optimization selection.

### Canonical target

`15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md`

### Existing files reviewed

Pricing Calculator, Budgets, Cost Explorer, cost-allocation tag, CUR, Billing, Organizations, and recommendation-resource lessons.

### Official sources used

AWS Cost Management, Budgets, Data Exports, cost-allocation tag, and consolidated-billing documentation.

### Verification date

2026-07-25.

### Gap being resolved

Facts existed across service notes, but no canonical decision guide separated proactive estimation, reactive analysis, controls, anomaly detection, and detailed data.

### CPP content added

A compact decision table, tool recognition, consolidated billing, allocation, mistakes, and knowledge checks.

### SAA cost-optimization content added

Governance scenarios, proactive/reactive controls, detailed export selection, tag activation, and account-structure trade-offs.

### Pricing or support scenarios added

Pre-deployment estimate, spend investigation, forecast alert, unusual-spend detection, finance export, and chargeback/showback scenarios.

### Existing content preserved

Existing service owners remain canonical for service-specific detail and are linked rather than duplicated wholesale.

### Content removed or corrected

No existing file was removed. The new owner clarifies that Budgets alerts do not inherently stop resources and that CUR 2.0 is delivered through AWS Data Exports.

### Badge decision

CPP and SAA badges are supported.

### Navigation and map updates

A local cost index and category entry were added; all directly affected audit mappings were updated.

### Acceptance-criteria result

Completed at the exact new target.

### Remaining work

None for AWS-046.

### Validation result

Passed the final Batch 8 validation command set.

## AWS-047 — Data transfer costs

### Official requirement

Explain cost direction and architectural paths across AZs, Regions, the internet, edge, NAT, endpoints, transit, and service processing.

### Required CPP depth

Fundamental recognition of major data-transfer cost drivers.

### Required SAA depth

Scenario-ready network cost optimization without weakening availability or security requirements.

### Canonical target

`12-billing-pricing-and-support/aws-billing-and-cost-management/03-data-transfer-costs.md`

### Existing files reviewed

The target, networking guide, VPC endpoint and connectivity guides, and related service pricing references.

### Official sources used

Current EC2 data-transfer, Amazon VPC, AWS PrivateLink, Transit Gateway, and CloudFront pricing pages.

### Verification date

2026-07-25.

### Gap being resolved

The previous lesson contained overbroad free-transfer language and insufficient path-based architectural analysis.

### CPP content added

Conceptual directions, service examples, major cost drivers, exam cues, and knowledge checks.

### SAA cost-optimization content added

AZ and Region paths, NAT and endpoint choices, transit and inspection, edge delivery, replication, resilience trade-offs, and scenarios.

### Pricing or support scenarios added

Private S3 access, cross-AZ traffic, centralized inspection, global delivery, replication, and NAT-heavy workloads.

### Existing content preserved

The useful direction, NAT, VPC endpoint, CloudFront, and cross-Region concepts were retained and reorganized around end-to-end paths.

### Content removed or corrected

Universal free-ingress claims and unsupported exact charges were removed; service-specific and bidirectional processing costs are now explicit.

### Badge decision

CPP and SAA badges are supported.

### Navigation and map updates

Billing navigation, CPP/SAA task maps, concept/depth matrices, inventory, badge audit, and dashboards were updated.

### Acceptance-criteria result

Completed at the exact backlog target.

### Remaining work

None for AWS-047; actual estimates remain Region- and path-specific.

### Validation result

Passed the final Batch 8 validation command set.
