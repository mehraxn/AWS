# AWS Regions, Availability Zones, and Edge Infrastructure

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

AWS global infrastructure provides geographic and fault-isolation boundaries for running workloads. The main concepts are Regions, Availability Zones, points of presence such as edge locations, and optional infrastructure closer to users such as Local Zones and Wavelength Zones.

These locations serve different purposes. Availability Zones support resilience within a Region; multiple Regions support geographic and regional-disaster requirements; edge infrastructure delivers or processes content closer to users.

## Core Concepts

| Concept | Meaning | Primary design purpose |
|---|---|---|
| AWS Region | Separate geographic area containing multiple Availability Zones | Geographic placement, service scope, residency, and regional isolation |
| Availability Zone (AZ) | One or more discrete data centers with redundant infrastructure, isolated from other AZs in the Region | High availability and fault isolation inside one Region |
| Edge location / point of presence | Site used by edge services such as Amazon CloudFront and Route 53 | Lower-latency delivery, DNS, and edge processing |
| Regional edge cache | Larger CloudFront cache layer between origins and edge locations | Retain less frequently requested content closer to viewers than the origin |
| Local Zone | Extension of a parent Region that places selected services near a metro area | Very low latency for local users and systems |
| Wavelength Zone | AWS infrastructure embedded in a telecommunications provider's 5G network | Ultra-low-latency applications for 5G devices |

## Regions and Service Scope

Most workload resources are regional: they are created in a selected Region and are not automatically replicated to another Region. Some resources are zonal, such as an EC2 instance or EBS volume in a particular AZ. Some services provide a global control plane or global endpoint, but their data and resources can still have regional behavior.

Avoid memorizing “every service is global” or “every service is regional.” Check the service's resource scope and data-residency behavior. IAM is commonly treated as a global service for exam purposes, while resources such as EC2 instances, RDS databases, and Lambda functions are regional.

## Availability Zones and High Availability

Availability Zones within a Region are connected by high-bandwidth, low-latency, redundant networking. Deploying redundant components across AZs can protect a workload from a single-AZ failure.

AWS supplies the AZs; the customer chooses an architecture that uses them. One EC2 instance in one AZ remains a single point of failure. A typical highly available design uses load balancing, capacity in multiple AZs, and a data layer designed for the required failure behavior.

## Edge Delivery

Amazon CloudFront caches content at edge locations so viewers can receive it with lower latency and reduced origin load. Regional edge caches form an additional cache layer. Edge delivery does not replace Multi-AZ or Multi-Region workload design: it improves delivery and can shield the origin, but the origin still needs suitable availability and recovery.

AWS Global Accelerator and Route 53 also use the global edge network for different purposes. Their detailed selection belongs in the networking batch.

## Choosing a Region

Architects evaluate:

- **Compliance and data residency:** where data and processing may legally or contractually occur
- **Latency:** proximity to users, connected systems, and on-premises environments
- **Service and feature availability:** required capabilities can vary by Region
- **Pricing:** service and data-transfer costs can differ by Region
- **Disaster recovery:** distance, independence, recovery objectives, and replication options
- **Sustainability and business policy:** organizational requirements can influence placement

No single factor always wins. A lower-latency Region is unsuitable if it lacks a required service or violates residency requirements.

## Multi-AZ, Multi-Region, and Edge Compared

| Requirement | Typical approach | Main trade-offs |
|---|---|---|
| Survive an AZ failure with low operational disruption | Multi-AZ in one Region | Regional failure remains possible; cross-AZ architecture and transfer costs may apply |
| Recover from or operate through a Region-level disruption | Multi-Region | Greater cost, data-consistency complexity, routing, and operational effort |
| Reduce content-delivery latency and origin load | Edge delivery | Does not by itself make the origin Multi-AZ or Multi-Region |
| Run selected resources near a metro area | Local Zone | Limited service selection; dependency on parent Region must be understood |
| Serve latency-sensitive 5G workloads | Wavelength Zone | Specialized availability, networking, and carrier integration |

## CPP Knowledge

- Region = geographic area.
- Availability Zone = isolated location inside a Region.
- Edge location = content, DNS, or edge-service presence close to users.
- Multiple AZs support high availability within one Region.
- Region choice considers compliance, latency, service availability, and price.
- Customers decide where to deploy and whether to add redundancy.

## SAA Architecture and Design

Begin with the failure requirement. If protection from a single data-center failure is enough, use multiple AZs. If the requirement includes regional disaster recovery, geographic traffic distribution, or regulatory separation, evaluate a Multi-Region design.

Multi-Region is not automatically better. It adds replication lag or conflict handling, certificate and secret distribution, deployment coordination, failover routing, observability, testing, and cost. Select active-active, active-passive, or backup-and-restore behavior from recovery time objective (RTO), recovery point objective (RPO), consistency, and budget requirements.

Also identify zonal dependencies. A workload spread across AZs can still fail if every application instance depends on one zonal resource. Review compute, storage, NAT, endpoints, load balancing, and databases as an end-to-end system.

## Common Exam Scenarios

- “Survive failure of one data center in the Region” → deploy across multiple AZs.
- “Meet a country's data-residency rule” → select an approved Region and verify each service's data behavior.
- “Reduce latency for static content worldwide” → use an edge delivery service such as CloudFront.
- “Recover from loss of an entire Region” → implement and test a Multi-Region recovery strategy.
- “Single-digit-millisecond access for users in a metro area” → evaluate a Local Zone when its supported services and parent-Region dependency fit.

## Exam Traps

- An AZ is not a Region.
- An AZ can contain more than one data center; do not define it as exactly one building.
- Resources are not automatically copied between Regions.
- A single-AZ deployment is not highly available merely because AWS operates redundant facilities.
- CloudFront edge locations do not replace the workload's origin architecture.
- “Global service” is not permission to ignore regional data and resource behavior.

## Summary

Regions provide geographic isolation, AZs provide fault isolation within a Region, and edge infrastructure brings delivery or compute closer to users. Select among Multi-AZ, Multi-Region, and edge approaches from explicit availability, latency, residency, service, cost, and recovery requirements.

## Knowledge Check

1. Which boundary should a workload cross to withstand one AZ failure?
2. Why might an architect choose a more distant Region?
3. Does CloudFront make a single-AZ origin highly available?
4. What additional problem does Multi-Region address compared with Multi-AZ?
5. When might a Wavelength Zone be relevant?

<details>
<summary>Show answers</summary>

1. Deploy redundant components across multiple Availability Zones.
2. Compliance, data residency, required service availability, pricing, or disaster-recovery needs may outweigh proximity.
3. No. CloudFront improves edge delivery, but the origin still needs its own availability design.
4. Regional disruption, geographic distribution, or regulatory separation.
5. For applications requiring ultra-low latency to supported 5G devices through a telecommunications network.

</details>

## References

- [AWS Regions and Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html)
- [AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html)
- [AWS fault-isolation boundaries: points of presence](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/points-of-presence.html)
- [Amazon CloudFront caching content with regional edge caches](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html)
- [CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
- [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html)

Sources checked: **2026-07-22**.
