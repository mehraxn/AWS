# AWS Pricing Fundamentals and Purchasing Models

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

AWS pricing combines usage-based charges with optional commitments, capacity controls, and service-specific dimensions. Cloud does not automatically make every workload cheaper: the result depends on architecture, utilization, licensing, data movement, operational effort, and whether commitments match real demand.

## Core Cost Concepts

| Term | Meaning |
|---|---|
| Price | Published rate or pricing rule for a service dimension |
| Usage | Measured consumption, such as runtime, storage, requests, or transferred data |
| Cost | Price applied to usage, commitments, and other chargeable dimensions |
| Billing | How charges, credits, taxes, discounts, and payments are presented and settled |
| Total cost of ownership | Direct charges plus staffing, operations, facilities, licensing, migration, risk, and indirect costs |
| Cost optimization | Continuous work to meet requirements at the lowest appropriate total cost |

Traditional infrastructure often requires capital expenditure before demand is known. AWS commonly shifts spending toward operational expenditure and variable usage. Elasticity can reduce idle capacity, but provisioned resources, commitments, retained storage, and managed-network paths can still create ongoing charges.

Economies of scale, tiered pricing, volume pricing, and commitment pricing can reduce unit cost for eligible usage. These benefits are conditional and service-specific. Regional prices can differ.

## EC2 Purchasing Decision Table

| Option | Commitment | Capacity assurance | Interruption | Best-fit signal |
|---|---|---|---|---|
| On-Demand Instances | No long-term usage commitment | No separate guarantee | No Spot interruption behavior | New, short-lived, variable, or uncertain workloads |
| Savings Plans | Hourly eligible-usage commitment for a term | Does not reserve EC2 capacity | No Spot interruption behavior | Predictable baseline usage |
| Reserved Instances | Billing discount tied to documented attributes and term | Applicable zonal EC2 RI behavior can reserve capacity | No Spot interruption behavior | Stable eligible usage fitting RI attributes |
| Spot Instances | No long-term commitment | Uses spare EC2 capacity | Can be interrupted | Flexible, fault-tolerant, checkpointable work |
| On-Demand Capacity Reservations | No discount by itself | Reserves EC2 capacity in a selected AZ | No Spot interruption behavior | Capacity assurance at a location |
| Dedicated Hosts | Host allocated to one customer | Depends on the purchase or reservation arrangement | No Spot interruption behavior | Host-level licensing, placement, or compliance |
| Dedicated Instances | Dedicated hardware without host-level control | Not a Capacity Reservation | No Spot interruption behavior | Dedicated hardware requirement |

Discount and capacity are separate. Savings Plans reduce eligible rates without reserving capacity. Capacity Reservations assure EC2 capacity without reducing the rate by themselves. Eligible discount instruments can apply to matching reserved-capacity usage.

## On-Demand Instances

On-Demand avoids a long-term commitment. It fits uncertain demand, short projects, frequently changing configurations, and usage above a committed baseline.

Stopping an EC2 instance stops instance runtime charges, but attached EBS volumes, snapshots, public IPv4 addresses, load balancers, data transfer, and retained services can continue to incur charges.

## Savings Plans

Savings Plans exchange an hourly eligible-usage commitment for lower prices. Unused commitment is still paid; usage above it uses the applicable pricing model. AWS currently documents four types:

- **Compute Savings Plans:** eligible EC2, Fargate, and Lambda usage with broad flexibility.
- **EC2 Instance Savings Plans:** an EC2 instance family in a selected Region, with documented flexibility.
- **Database Savings Plans:** eligible usage across supported AWS database services and configurations.
- **SageMaker AI Savings Plans:** eligible SageMaker AI instance usage across documented components and configurations.

Verify plan terms, eligible services, payment choices, and flexibility before purchase. Savings Plans do not reserve EC2 capacity.

## Reserved Instances

Reserved Instances are primarily a billing benefit, not a purchased server. Standard and Convertible options differ in flexibility. A Regional EC2 RI provides a billing discount and documented size flexibility where applicable; a Zonal EC2 RI can also reserve capacity in its Availability Zone.

Other services have their own reservation models. Do not apply EC2 RI rules unchanged to RDS, ElastiCache, OpenSearch Service, Redshift, or another service.

## Spot Instances

Spot uses spare EC2 capacity and can be interrupted. Suitable workloads tolerate restart, replacement, or delay—for example batch jobs, stateless workers, testing, and flexible analytics. Use diversified capacity choices, queues, checkpointing, idempotency, Auto Scaling, and interruption handling. Do not keep irreplaceable state only on Spot capacity.

## Storage and Database Cost Dimensions

- **Object storage:** class, capacity, requests, retrieval, lifecycle conditions, replication, and transfer.
- **Block storage:** volume type, provisioned capacity/performance, snapshots, and unattached resources.
- **File storage:** stored capacity, throughput/performance mode, lifecycle, and access pattern.
- **Databases:** capacity mode, storage, I/O, backup retention, replicas, Multi-AZ, global replication, licensing, and transfer.

Reducing redundancy may violate availability, durability, or recovery requirements. Preserve the required reliability and security posture.

## Data Transfer Cost Dimensions

Cost depends on service, Region, direction, source, destination, AZs, and intermediate services. Common drivers include internet egress, cross-AZ or cross-Region traffic, NAT Gateway and Transit Gateway processing, interface endpoints, load balancers, replication, and backup copies.

Use the [data-transfer cost guide](03-data-transfer-costs.md) and current pricing pages. Do not apply one universal “inbound is free” or “same Region is free” rule.

## Cost-Aware Architecture

1. Measure baseline usage separately from bursts.
2. Keep uncertain usage On-Demand until evidence supports a commitment.
3. Commit conservatively and monitor coverage and utilization.
4. Use Spot only for interruption-tolerant capacity.
5. Right-size and scale when the application supports it.
6. Remove idle and orphaned resources with safeguards.
7. Model storage access, retention, and transfer paths.
8. Revisit decisions after demand, pricing, or architecture changes.

## Security and Governance

Grant Billing access with least privilege instead of routinely using the root user. Protect the root user with MFA, separate procurement approval from implementation where appropriate, govern cost-allocation tags, and audit commitment and capacity changes.

## CPP Exam Focus

- Pay-as-you-go converts many fixed infrastructure expenses into variable operational expenses.
- On-Demand emphasizes flexibility; commitments trade flexibility for eligible pricing benefits.
- Spot fits interruption-tolerant work.
- Savings Plans do not reserve EC2 capacity.
- Capacity Reservations address capacity assurance, not a discount by themselves.
- Stopping compute does not necessarily remove storage and networking charges.

## SAA Cost-Optimization Scenarios

- **Uncertain new service:** use On-Demand while measuring demand.
- **Stable baseline plus seasonal peaks:** commit conservatively for the baseline and retain flexible peak capacity.
- **Checkpointable batch queue:** diversify Spot capacity and retain fallback when deadlines require it.
- **Must launch in one AZ:** use a Capacity Reservation and evaluate a separate matching discount instrument.
- **Cross-AZ bill rises after adding resilience:** preserve Multi-AZ and optimize chatty paths instead of removing fault isolation blindly.

## Common Mistakes

- Treating every AWS cost as zero when usage stops.
- Treating a discount commitment as a capacity guarantee.
- Assuming every RI reserves capacity.
- Using Spot for irreplaceable state.
- Buying a commitment from an optimistic forecast.
- Removing required backups or Multi-AZ resources only to reduce cost.

## Knowledge Check

1. **Which option fits unpredictable usage with no commitment tolerance?** On-Demand.
2. **Does a Savings Plan reserve EC2 capacity?** No; use a capacity mechanism when assurance is required.
3. **When can an EC2 RI reserve capacity?** With applicable zonal RI behavior and matching attributes.
4. **Why might a stopped instance still cost money?** Storage, snapshots, networking resources, and retained services are billed separately.
5. **What makes a workload suitable for Spot?** It can tolerate interruption through replacement, retry, checkpointing, or flexible completion.

## Related Lessons

- [Amazon EC2 Reserved Instances](../../04-compute/amazon-ec2/03-reserved-instances.md)
- [EC2 Auto Scaling](../../04-compute/ec2-auto-scaling/01-target-tracking-scaling.md)
- [Amazon S3](../../05-storage/amazon-s3/01-overview.md)
- [Database selection](../../15-comparisons-and-decision-guides/databases/01-database-selection-guide.md)
- [Highly available web applications](../../13-architecture-and-design-patterns/01-highly-available-web-applications.md)

## References

- [AWS pricing](https://aws.amazon.com/pricing/)
- [Amazon EC2 purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)
- [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html)
- [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)
- [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html)

Checked: 2026-07-25.
