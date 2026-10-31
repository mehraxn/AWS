# AWS Support Plans

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

AWS Support plans determine the level of technical assistance, operational guidance, and account-team engagement. Plan names, prices, response commitments, and entitlements are volatile; use the current official comparison for procurement and incident runbooks.

## Current Commercial Plan Lineup

Verified on 2026-07-25 for standard commercial Regions:

| Plan | Technical-support position | Operations relationship |
|---|---|---|
| Basic Support | Account and billing assistance, documentation, forums, and service-health resources; no technical Support cases | Self-service learning and experimentation |
| AWS Business Support+ | Paid technical support with continuous engineer access and AI-powered contextual assistance | Production operations needing technical cases |
| AWS Enterprise Support | Business Support+ plus a designated Technical Account Manager and proactive guidance | Critical portfolios needing an ongoing AWS relationship |
| AWS Unified Operations | Designated specialists, critical-workload reviews, runbooks, event support, and proactive operations | Large, complex operations requiring an integrated AWS team |

Paid plans use monthly pricing that can depend on AWS charges and plan-specific minimums. Exact prices belong on the current pricing page, not in memorized notes.

## 2026 Transition from Older Plans

Developer Support, the former Business Support plan, and Enterprise On-Ramp are transition plans for existing customers in standard commercial Regions. AWS states that they will be discontinued on **January 1, 2027**. Developer and former Business customers can transition to Business Support+; Enterprise On-Ramp customers are being moved to Enterprise Support during 2026. AWS documents separate availability for AWS GovCloud (US).

Older exam material may mention those names. Recognize them as transitional instead of treating the old five-plan table as current.

## Technical Support and Response Categories

Basic includes account and billing help but not technical troubleshooting cases. Paid plans add technical cases and progressively deeper operational engagement.

AWS maps response objectives to case severity and plan. Verify the current [Support plan comparison](https://aws.amazon.com/premiumsupport/plans/) and [pricing and features](https://aws.amazon.com/premiumsupport/pricing/) when a response objective matters. A response objective is not a resolution-time guarantee.

## Channels and Case Access

- Basic customers use account/billing assistance and self-service resources.
- Business Support+, Enterprise Support, and Unified Operations provide documented technical case channels and Support API access.
- IAM controls who can view plans, open cases, use APIs, and view Trusted Advisor data.
- Do not use the root user for routine Support Center access.

Language and channel availability can vary; check the official comparison for the required locale.

## AWS Trusted Advisor

Trusted Advisor evaluates an account against AWS best practices and produces recommendations; it does not change resources automatically.

- All AWS accounts have selected core checks.
- Business Support+, Enterprise Support, and Unified Operations have all checks under current documentation.
- IAM controls console and API access.

Avoid memorizing an old number of core checks because checks and entitlements change.

## AWS Health

AWS Health presents public events, account-specific events, affected resources, scheduled changes, and notifications. Current documentation provides account and organizational console views. Programmatic AWS Health API access currently requires Business Support+, Enterprise Support, or Unified Operations.

AWS Health reports AWS service and account events. CloudWatch monitors workload metrics and logs; CloudTrail records API activity; Trusted Advisor provides recommendations.

## Account Assistance and Proactive Guidance

- Basic: account and billing assistance.
- Business Support+: production-oriented technical assistance.
- Enterprise Support: designated TAM and proactive strategic engagement.
- Unified Operations: broader designated specialist team and integrated operational capabilities.

Countdown, incident-management, and security-response capabilities have plan-specific terms. Confirm official entitlements instead of inferring them from an older plan.

## Security and Governance

Use least privilege for Support Center, Support Plans, Trusted Advisor, and AWS Health. Cases can contain resource IDs, logs, architecture details, and personal data; restrict access and redact secrets. Protect the root user with MFA and audit subscription changes.

## CPP Exam Focus

- Basic includes account and billing assistance, but not technical Support cases.
- Paid plans add technical support and progressively deeper guidance.
- Trusted Advisor recommends; it does not remediate automatically.
- AWS Health supplies service and account-specific event information.
- Business Support+ is the current production-oriented paid entry plan.

## Selection Scenarios

- **Learning account:** Basic may be enough when self-service troubleshooting is acceptable.
- **Production team needs technical cases:** evaluate Business Support+.
- **Critical portfolio needs a designated TAM:** evaluate Enterprise Support.
- **Large operation needs designated specialists and integrated event operations:** evaluate Unified Operations.
- **Existing Developer, Business, or Enterprise On-Ramp customer:** follow official 2026 transition guidance.

## Common Mistakes

- Reusing the old five-plan table as current.
- Memorizing prices or response times without a date.
- Assuming Basic includes technical troubleshooting.
- Treating Trusted Advisor as automatic remediation.
- Treating AWS Health, CloudWatch, and CloudTrail as interchangeable.
- Assuming Support guarantees availability or resolution.

## Knowledge Check

1. **Which plan is automatically available?** Basic Support.
2. **Which current plan first provides production-oriented technical support?** AWS Business Support+.
3. **Which plan adds a designated TAM?** AWS Enterprise Support.
4. **What happens to Developer, Business, and Enterprise On-Ramp in standard commercial Regions?** AWS documents transition during 2026 and discontinuation on January 1, 2027.
5. **Does Trusted Advisor implement recommendations?** No; the customer evaluates and applies them.

## References

- [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html)
- [AWS Support comparison](https://aws.amazon.com/premiumsupport/plans/)
- [Plan transition notice](https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html)
- [Trusted Advisor access](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html)
- [AWS Health concepts](https://docs.aws.amazon.com/health/latest/ug/aws-health-concepts-and-terms.html)

Checked: 2026-07-25.
