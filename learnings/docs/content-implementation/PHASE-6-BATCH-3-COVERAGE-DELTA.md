# Phase 6 Batch 3 Coverage Delta

Checked: 2026-07-23

## Dependency Resolution

The Batch 2 final reconciliation records were present. All 13 Batch 2 rows were complete, none were partial or blocked, and none blocked Batch 3. AWS-020 through AWS-025 were released.

## Networking Requirements Improved

Added a VPC foundation and routing lesson, a security-group-versus-NACL guide, and expanded endpoints/PrivateLink and hybrid/multi-VPC selection. Coverage connects addressing, subnets, routing, internet/IPv6 egress, controls, Flow Logs awareness, private connectivity, peering, Transit Gateway, VPN, Direct Connect, resilience, and cost.

## Content Delivery Requirements Improved

Added a guide connecting Route 53 records, aliases, policies, health/failover; CloudFront origins, behaviors, caching, and access controls; and Global Accelerator anycast endpoints, health, and traffic controls.

## CPP Requirements Fully Resolved

AWS-020 through AWS-025 now provide service purpose, recognition cues, connectivity distinctions, security roles, conceptual pricing, common confusions, and simple scenarios.

## CPP Requirements Partially Improved

Related navigation improved. No Batch 3 criterion remains partial, but later-batch and whole-repository CPP gaps are not claimed as resolved.

## SAA Requirements Fully Resolved

The six selected criteria now cover scope, routing, AZ/Regional behavior, security, HA, failures, cost, performance, operations, alternatives, trade-offs, and architecture scenarios.

## SAA Requirements Partially Improved

Cross-service architecture discoverability improved. Centralized-inspection implementation details and unrelated later-batch lessons remain outside Batch 3.

## New Scenario-Ready Topics

Multi-AZ tiered VPCs, controlled IPv4/IPv6 egress, stateful/stateless troubleshooting, endpoint selection, mesh versus hub connectivity, redundant hybrid access, DNS failover, CDN front doors, and anycast multi-Region entry.

## New Comparison Guides

Created 03-security-groups-vs-network-acls.md and 04-dns-edge-and-global-routing.md. Expanded 02-vpc-connectivity-options.md. Routing and endpoint owners also contain decision tables without duplicate owners.

## Factual Corrections

Clarified public-subnet IPv4 reachability, endpoint-type behavior, and peering non-transitivity/overlap. Details are in PHASE-6-BATCH-3-FACT-CORRECTIONS.md.

## Terminology Corrections

Used current AWS terms for gateways, endpoint types, PrivateLink, Transit Gateway routing, customer gateways, CloudFront origin access control, and Global Accelerator endpoint groups.

## Badge Corrections

CPP and SAA badges were added only to the six selected targets or bounded supplements, with meaningful content for both certification depths.

## Navigation Improvements

Expanded the VPC index, networking category index, networking comparison index, root progress summary, service index, and repository map. Canonical owners are cross-linked rather than duplicated.

## Remaining Networking Gaps

No AWS-020 through AWS-025 criterion remains. Later-batch networking gaps require their own authority and dependency gates.

## Remaining Content Delivery Gaps

No AWS-025 criterion remains. API Gateway appears only as integration context; its later-batch lesson was not changed.

## Deferred Batch 4 and Later Work

All Batch 4 and later content remains untouched. Batch 3 completed 6 items, with 0 partial, 0 blocked, 0 deferred inside the batch, and 0 manual review.
