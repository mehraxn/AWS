# Security Groups vs Network ACLs

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Security groups and network access control lists (network ACLs) filter traffic at different boundaries. They complement routing, IAM, application authorization, encryption, and monitoring; neither creates a route.

## Decision Table

| Dimension | Security group | Network ACL |
|---|---|---|
| Scope | Associated with supported resources or network interfaces | Associated with a subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow and deny |
| Evaluation | All rules collectively | Lowest numbered matching rule first |
| Return traffic | Automatically allowed for an allowed flow | Must be explicitly allowed in the opposite direction |
| References | Can reference security groups in supported scenarios | Uses CIDRs and other supported network-rule fields, not security-group references |
| Primary use | Least-privilege resource communication | Subnet guardrail and explicit blocking/defense in depth |

## Defaults

- A new security group has no inbound rules and an outbound allow rule. Removing outbound permissions restricts new outbound flows; response traffic for an allowed stateful flow is still tracked.
- The default network ACL allows all inbound and outbound traffic.
- A new custom network ACL denies all inbound and outbound traffic until rules are added.

Always inspect the actual rules instead of relying on the word “default.”

## Return Traffic and Ephemeral Ports

Security groups track allowed connections, so response traffic does not need a mirror rule. Network ACLs are stateless: both request and response directions must match allow rules. Clients normally use ephemeral source ports, so a network ACL may need an appropriate ephemeral-port range in the return direction. Use the operating system and application behavior to select the range rather than memorizing one universal range.

## Scenario Selection

| Requirement | Better starting control | Reason |
|---|---|---|
| Database accepts traffic only from application tier | Security group | Reference the application security group; stateful return traffic |
| Explicitly deny a known source CIDR for an entire subnet | Network ACL | Supports deny rules at the subnet boundary |
| Allow HTTPS to a load balancer, then app traffic to targets | Security groups | Chain least-privilege resource relationships |
| Add a coarse subnet guardrail in addition to resource rules | Network ACL | Separate stateless defense-in-depth boundary |
| Troubleshoot a return path allowed inbound but blocked outbound | Inspect network ACL | Stateless controls need rules in both directions |

## Availability, Performance, Cost, and Operations

Both controls are VPC features without a separate hourly resource charge, but complex rule sets increase operational risk. Security-group references adapt better than changing CIDR lists for dynamic tiers. Network ACL numbering requires change space between rules; a low-numbered deny can override a later allow. Test rule changes and use Flow Logs to observe accepted or rejected traffic metadata.

## CPP Recognition

- **Stateful + resource level + allow only** means security group.
- **Stateless + subnet level + allow and deny** means network ACL.

## SAA Design Guidance

Use security groups as the primary least-privilege control for application tiers. Add network ACLs when an independent subnet guardrail or explicit CIDR deny has a justified requirement. Do not duplicate every security-group rule mechanically in a network ACL; account for stateless return paths and operational complexity.

## Common Mistakes

- Expecting a security group deny rule.
- Forgetting outbound or ephemeral return traffic in a custom network ACL.
- Assuming a permissive network ACL overrides a restrictive security group.
- Treating either control as a replacement for routes, IAM, WAF, Network Firewall, or host security.
- Calling security groups “instance only”; many AWS resources apply them through network interfaces or resource integrations.

## Knowledge Check

1. Which control can explicitly deny a CIDR?
2. Which control automatically allows response traffic?
3. Which network ACL rule is evaluated first?
4. Why do ephemeral ports matter to network ACLs?

<details><summary>Answers</summary>

1. A network ACL. 2. A security group for a tracked allowed flow. 3. The lowest-numbered matching rule. 4. A stateless return path must allow the client's ephemeral destination port range in the opposite direction.

</details>

## Canonical Lessons

- [Amazon VPC foundations](../../07-networking-and-content-delivery/amazon-vpc/01-overview.md)
- [Security groups](../../07-networking-and-content-delivery/amazon-vpc/02-security-groups.md)
- [VPC Flow Logs](../../07-networking-and-content-delivery/amazon-vpc/03-flow-logs.md)

## References

- [Control traffic using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- [Security-group rule basics](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)
- [Control subnet traffic using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [Network ACL rules](https://docs.aws.amazon.com/vpc/latest/userguide/nacl-rules.html)

Official references checked: 2026-07-23.
