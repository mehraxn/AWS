# Networking Decision Guides

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white) ![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Choose networking services from traffic direction, protocol, latency, reachability, scale, and security requirements.

## Guide Order

| Order | Topic | What it covers |
|---:|---|---|
| 1 | [Amazon CloudFront vs AWS Global Accelerator](01-cloudfront-vs-global-accelerator.md) | Study notes and decision points for Amazon CloudFront vs AWS Global Accelerator. |
| 2 | [VPC Endpoint vs VPC Peering vs AWS Transit Gateway](02-vpc-connectivity-options.md) | Study notes and decision points for VPC Endpoint vs VPC Peering vs AWS Transit Gateway. |
| 3 | [Security Groups vs Network ACLs](03-security-groups-vs-network-acls.md) | Study notes and decision points for Security Groups vs Network ACLs. |
| 4 | [DNS, Edge Delivery, and Global Routing Decisions](04-dns-edge-and-global-routing.md) | Study notes and decision points for DNS, Edge Delivery, and Global Routing Decisions. |

## Decision Questions

- Is the problem DNS, content delivery, global acceleration, VPC connectivity, or packet filtering?
- Is traffic public, private, internet-bound, or hybrid?
- Does the design require transitive routing, static IPs, caching, or stateful filtering?

## Recommended Method

1. Extract the requirement and constraints.
2. Identify two or three plausible services.
3. Compare them across functionality, availability, security, operations, performance, and cost.
4. State why the rejected options fail the requirement.

[Back to all comparisons](../README.md) · [Repository home](../../README.md)
