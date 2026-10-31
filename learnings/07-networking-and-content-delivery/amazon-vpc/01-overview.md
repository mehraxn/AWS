# Amazon VPC Foundations

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Amazon Virtual Private Cloud (Amazon VPC) provides a logically isolated virtual network for AWS resources. A VPC belongs to one AWS Region and can span that Region's Availability Zones. Subnets divide the VPC address space, but each subnet belongs to exactly one Availability Zone.

VPC design determines how workloads receive addresses, find destinations, reach public or private services, cross security boundaries, and survive failures.

## Core Components

| Component | Scope | Purpose |
|---|---|---|
| VPC | Region | Addressing and network boundary for resources |
| Subnet | One Availability Zone | Places resources in an AZ and associates them with a route table and network ACL |
| Route table | VPC resource associated with subnets or supported gateways | Selects a target for destination traffic |
| Internet gateway | Attached to a VPC | Provides a route target for internet-routable IPv4 and IPv6 traffic |
| NAT gateway | One Availability Zone | Allows initiated outbound IPv4 connections while preventing unsolicited inbound sessions |
| Egress-only internet gateway | VPC | Provides outbound-only internet connectivity for IPv6 workloads |
| Elastic network interface | Availability Zone | Carries private addresses and security groups for a supported resource |
| Security group | Resource or network-interface level | Stateful allow rules |
| Network ACL | Subnet level | Stateless numbered allow and deny rules |
| VPC Flow Logs | VPC, subnet, or network-interface scope | Records network-flow metadata for accepted or rejected traffic |

## CIDR and Address Planning

Classless Inter-Domain Routing (CIDR) combines an address with a prefix length. In `10.20.0.0/16`, `/16` identifies the network prefix; the remaining address space can be divided into subnet CIDRs.

- Plan non-overlapping CIDRs before connecting VPCs or on-premises networks.
- Private IPv4 addresses identify resources inside private networks. A public IPv4 address or Elastic IP maps public reachability to a resource's private address where supported.
- An Elastic IP is a public IPv4 address allocated to an AWS account and explicitly associated with a supported resource. It is stable across stop/start when retained and reassociated, but public IPv4 usage has a cost dimension.
- IPv6 addresses are globally unique rather than translated by a NAT gateway. Control exposure with routes, security groups, network ACLs, and an egress-only internet gateway when outbound-only behavior is required.
- Poor address planning can prevent peering, complicate Transit Gateway and hybrid routing, and force renumbering or translation designs.

Avoid memorizing arbitrary subnet sizes for the exam. Focus on whether address ranges overlap, whether capacity allows future growth, and whether routes can distinguish destinations.

## How Traffic Moves

1. A resource sends traffic through its network interface.
2. Security-group rules determine whether the traffic is allowed at the resource boundary.
3. The subnet route table selects the most specific matching destination and its target.
4. A network ACL evaluates traffic as it enters or leaves the subnet.
5. The target might be local routing, an internet or NAT gateway, a VPC endpoint, a peering connection, a Transit Gateway, or a VPN gateway.

Every VPC route table has local routing for its VPC CIDRs. A route alone never overrides a security control, and a security rule never creates a route.

## Public, Private, and Hybrid Connectivity

- A **public subnet** has a route to an internet gateway. An IPv4 resource also needs a public IPv4 address and permissive security controls to communicate with the internet.
- A **private subnet** has no direct route to an internet gateway. A public NAT gateway can provide outbound IPv4 internet access when the private route table targets it.
- A **VPC endpoint** privately reaches a supported service without requiring an internet gateway or NAT gateway for that service traffic.
- **VPC peering** directly connects two non-overlapping VPCs and is not transitive.
- **Transit Gateway** acts as a Regional hub for many VPC and hybrid attachments.
- **Site-to-Site VPN** provides encrypted connectivity over IPsec tunnels; **Direct Connect** provides dedicated connectivity and can be combined with VPN for encryption or backup designs.

## Security and Shared Responsibility

AWS operates the physical network, VPC control plane, and managed gateway infrastructure. Customers are responsible for address plans, routes, security groups, network ACLs, endpoint policies, IAM, encryption, operating-system and application security, and monitoring.

A private subnet is not automatically secure. A workload can still be exposed through overly broad routes, load balancers, security rules, credentials, or vulnerable software. Apply least privilege, separate tiers, prefer private service access where justified, encrypt traffic when required, and analyze Flow Logs and service logs.

## Availability, Performance, and Cost

- Deploy application subnets in multiple Availability Zones and place replaceable targets behind a load balancer.
- A NAT gateway is AZ-scoped. One NAT gateway per active AZ avoids depending on another AZ, but increases hourly cost. A shared NAT design reduces hourly resources but adds cross-AZ dependency and possible data-transfer cost.
- Interface endpoints should use multiple AZs when access must survive an AZ impairment. Gateway endpoints use route tables rather than endpoint ENIs.
- Account for public IPv4 addresses, NAT gateway time and processing, interface endpoints, Transit Gateway attachments and processing, inter-AZ or inter-Region transfer, VPN, Direct Connect, and logging destinations.
- Centralized networking can simplify inspection and governance but adds routing, cost-allocation, and failure-domain decisions.

## CPP Exam Focus

Recognition clues:

- **VPC**: isolated AWS network.
- **Subnet**: AZ-scoped section of a VPC.
- **Route table**: chooses where destination traffic goes.
- **Internet gateway**: public internet route target.
- **NAT gateway**: initiated outbound IPv4 access for private workloads.
- **Security group**: stateful resource firewall.
- **Network ACL**: stateless subnet filter.
- **Flow Logs**: traffic metadata, not packet payload.

Example: Private EC2 instances need software updates but must not accept inbound internet sessions. Place them in private subnets and route outbound IPv4 traffic to a public NAT gateway.

## SAA Design Scenarios

### Highly available web application

Use public subnets in multiple AZs for an internet-facing load balancer and private application subnets in those AZs for Auto Scaling targets. Keep databases in private database subnets, chain security groups by tier, and choose resilient outbound connectivity.

### Many accounts and VPCs

Use non-overlapping address plans. A few direct relationships can use VPC peering; a growing hub-and-spoke topology can use Transit Gateway shared through AWS Resource Access Manager.

### Private access to AWS APIs

Choose a gateway endpoint for supported gateway services or an interface endpoint for a service integrated with PrivateLink. Compare endpoint cost and scope with NAT gateway processing and broader internet access.

### Hybrid network

Use Site-to-Site VPN for encrypted internet-based connectivity or as a rapid/backup path. Use Direct Connect when dedicated connectivity and consistent network performance are primary requirements; design redundant connections and dynamic routing for production resilience.

## Common Mistakes

- Calling a subnet public because an instance has a public IP; the subnet also needs an internet-gateway route.
- Assuming a route grants permission or a security group creates connectivity.
- Sending IPv6 traffic to a NAT gateway; use IPv6 routes and, for outbound-only internet access, an egress-only internet gateway.
- Using overlapping CIDRs for networks that must peer or route together.
- Treating one NAT gateway as multi-AZ simply because the VPC spans AZs.
- Treating a private subnet as a complete security boundary.

## Knowledge Check

1. What is Regional: a VPC or a subnet?
2. What makes a subnet public?
3. Which control is stateful: a security group or network ACL?
4. Why do connected networks need non-overlapping CIDRs?
5. Which managed component provides outbound-only IPv4 internet access for private workloads?

<details><summary>Answers</summary>

1. A VPC is Regional; a subnet is limited to one AZ. 2. Its associated route table has a route to an internet gateway. An IPv4 resource still needs a public address and allowed traffic. 3. A security group. 4. Routing must unambiguously identify the destination network. 5. A public NAT gateway, with the private route table targeting it.

</details>

## Related Lessons

- [Subnets, route tables, and internet gateways](09-subnets-route-tables-and-internet-gateways.md)
- [Security groups](02-security-groups.md)
- [VPC Flow Logs](03-flow-logs.md)
- [VPC endpoints and PrivateLink](04-endpoint-services.md)
- [VPC peering](05-vpc-peering.md)
- [Security groups versus network ACLs](../../15-comparisons-and-decision-guides/networking/03-security-groups-vs-network-acls.md)
- [Hybrid and multi-VPC connectivity](../../15-comparisons-and-decision-guides/networking/02-vpc-connectivity-options.md)

## References

- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [IP addressing for VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)
- [VPC route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
- [NAT devices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html)
- [VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

Official references checked: 2026-07-23.
