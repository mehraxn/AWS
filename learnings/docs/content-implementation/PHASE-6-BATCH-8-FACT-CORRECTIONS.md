# Phase 6 Batch 8 Fact Corrections

## Correction — Current AWS Support plan lineup

Affected path: `12-billing-pricing-and-support/aws-support/02-support-plans.md`

Related backlog ID: AWS-045

Previous claim: The current lineup was presented as Basic, Developer, Business, Enterprise On-Ramp, and Enterprise.

Corrected claim: The current commercial lineup is Basic Support, AWS Business Support+, AWS Enterprise Support, and AWS Unified Operations. Older plans are identified only in a dated transition section.

Reason: AWS introduced replacement plans and announced end-of-support transitions for the older lineup.

Official source: [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) and [support-plan end-of-support notice](https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html), checked 2026-07-25.

## Correction — Support response commitments

Affected path: `12-billing-pricing-and-support/aws-support/02-support-plans.md`

Related backlog ID: AWS-045

Previous claim: Volatile numeric response times and prices were embedded as durable study facts.

Corrected claim: The lesson teaches response-category and plan-selection concepts and links to the current AWS plan comparison for contractual response targets.

Reason: Prices and response commitments are date-sensitive and should not be memorized from an undated note.

Official source: [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html), checked 2026-07-25.

## Correction — Trusted Advisor and AWS Health access

Affected path: `12-billing-pricing-and-support/aws-support/02-support-plans.md`

Related backlog ID: AWS-045

Previous claim: Entitlements were presented as blanket all-or-nothing access and used older Health terminology.

Corrected claim: All accounts can receive selected core Trusted Advisor checks; Business Support+, Enterprise Support, and Unified Operations provide all checks. AWS Health exposes public and account-specific events, while API access depends on an eligible paid plan.

Reason: Access differs by check, feature, and plan.

Official source: [Trusted Advisor access](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html) and [AWS Health concepts](https://docs.aws.amazon.com/health/latest/ug/aws-health-concepts-and-terms.html), checked 2026-07-25.

## Correction — Savings Plans types and scope

Affected path: `12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md`

Related backlog ID: AWS-044

Previous claim: Savings Plans coverage relied on older categories and unsupported maximum discount percentages.

Corrected claim: The lesson identifies Compute, EC2 Instance, Database, and SageMaker AI Savings Plans and teaches scope and flexibility without unsupported percentages.

Reason: AWS documentation now lists four plan types, and exact savings claims are volatile.

Official source: [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html), checked 2026-07-25.

## Correction — Discount and capacity are separate decisions

Affected path: `12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md`

Related backlog ID: AWS-044

Previous claim: Discount mechanisms and capacity assurance were insufficiently separated.

Corrected claim: Savings Plans and Reserved Instances are discount mechanisms; On-Demand Capacity Reservations address EC2 capacity assurance and do not inherently provide a usage discount.

Reason: Cost optimization and capacity planning solve different requirements.

Official source: [Amazon EC2 On-Demand pricing and capacity reservations](https://aws.amazon.com/ec2/pricing/on-demand/), checked 2026-07-25.

## Correction — Data transfer is path-specific

Affected path: `12-billing-pricing-and-support/aws-billing-and-cost-management/03-data-transfer-costs.md`

Related backlog ID: AWS-047

Previous claim: Data transfer in was described as universally free and service processing was underemphasized.

Corrected claim: Charges depend on source, destination, direction, AZ, Region, service, and intermediaries; NAT Gateway, PrivateLink, Transit Gateway, inspection, and edge services can add processing or transfer dimensions.

Reason: A universal ingress rule is unsafe across AWS services and architectures.

Official source: [EC2 data transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer), [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/), [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/), and [Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/), checked 2026-07-25.

## Correction — Budgets and detailed cost data

Affected path: `15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md`

Related backlog ID: AWS-046

Previous claim: Scattered notes did not clearly distinguish alerts from enforcement or legacy CUR from current detailed exports.

Corrected claim: AWS Budgets can alert on actual or forecast thresholds and can initiate configured actions, but a budget does not inherently stop resources. AWS Data Exports provides CUR 2.0, the recommended current detailed cost-and-usage export; legacy CUR remains available.

Reason: Tool selection depends on whether the requirement is notification, action, interactive analysis, or detailed data delivery.

Official source: [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) and [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html), checked 2026-07-25.

## Correction — Cost-allocation tag activation and consolidated billing

Affected path: `15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md`

Related backlog ID: AWS-046

Previous claim: Resource tagging, billing activation, and consolidated payment responsibilities were not consistently separated.

Corrected claim: User-defined tags must be activated as cost-allocation tags before they appear as billing dimensions. In AWS Organizations consolidated billing, the management account pays the combined bill while member accounts remain separate accounts.

Reason: These distinctions are central to correct chargeback, showback, and account governance.

Official source: [Activating cost-allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) and [consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html), checked 2026-07-25.

AWS Free Tier and AWS Marketplace billing were not selected Batch 8 backlog targets and were not changed.
