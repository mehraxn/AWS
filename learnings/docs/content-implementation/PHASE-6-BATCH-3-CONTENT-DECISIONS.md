# Phase 6 Batch 3 Content Decisions

Checked: 2026-07-23

## AWS-020 — Amazon VPC

### Official requirement

Foundational VPC coverage for CPP and SAA.

### Canonical target

07-networking-and-content-delivery/amazon-vpc/01-overview.md

### Existing files reviewed

VPC README and focused security, logging, endpoint, peering, NAT, and connectivity lessons.

### Official sources used

Amazon VPC User Guide, routing, security, and pricing docs; checked 2026-07-23.

### Gap being resolved

No canonical foundation connected VPC scope, addressing, routing, controls, resilience, and cost.

### CPP content added

Service purpose, connectivity types, shared responsibility, recognition, and pricing concepts.

### SAA content added

CIDR planning, AZ subnets, routing/security, HA, observability, connectivity trade-offs, and failure design.

### Networking scenarios or comparisons added

Multi-AZ tiered VPC; component and connectivity selection.

### Existing content preserved

All accurate focused VPC lessons.

### Content removed or corrected

No useful content removed; public exposure and private-subnet security caveats clarified.

### Badge decision

CPP and SAA: both depths are substantive.

### Remaining work

None for this criterion.

### Validation result

Passed: canonical ownership, preservation, badges, official references, scenarios, questions, filenames, and internal links verified.

## AWS-021 — VPC routing

### Official requirement

Subnet, route, internet-access, controlled-egress, HA, and cost coverage.

### Canonical target

07-networking-and-content-delivery/amazon-vpc/09-subnets-route-tables-and-internet-gateways.md

### Existing files reviewed

VPC index plus NAT, peering, security, and comparison lessons.

### Official sources used

Official VPC subnet, route table, IGW, NAT, and egress-only IGW docs; checked 2026-07-23.

### Gap being resolved

Routing concepts were scattered rather than scenario ready.

### CPP content added

Public/private/isolated recognition; IGW/NAT/IPv6 egress purpose.

### SAA content added

Main/custom tables, longest prefix, route targets, propagation, blackholes, zonal NAT, HA, and cost.

### Networking scenarios or comparisons added

Multi-AZ tiers; public/private; IGW/NAT; route-target scenarios.

### Existing content preserved

Existing NAT, peering, and security owners.

### Content removed or corrected

Corrected the idea that an IGW route alone gives an IPv4 resource internet access.

### Badge decision

CPP and SAA: recognition and design depth are present.

### Remaining work

No extra unbacklogged comparison created.

### Validation result

Passed: canonical ownership, preservation, badges, official references, scenarios, questions, filenames, and internal links verified.

## AWS-022 — Security groups versus network ACLs

### Official requirement

Authorized stateful-versus-stateless control comparison.

### Canonical target

15-comparisons-and-decision-guides/networking/03-security-groups-vs-network-acls.md

### Existing files reviewed

Security-group owner, VPC overview/index, and networking comparisons.

### Official sources used

Official VPC security-group and network-ACL docs; checked 2026-07-23.

### Gap being resolved

No side-by-side owner covered scope, rules, return traffic, evaluation, and ephemeral ports.

### CPP content added

Resource/ENI versus subnet scope, allow/deny, defense in depth.

### SAA content added

State, bidirectional rules, numbered evaluation, ephemeral ports, least privilege, troubleshooting.

### Networking scenarios or comparisons added

Decision table and layered web/application/database scenarios.

### Existing content preserved

The focused security-group lesson.

### Content removed or corrected

No accurate content removed; scope and return-traffic wording clarified.

### Badge decision

CPP and SAA: recognition and architecture troubleshooting are present.

### Remaining work

None for this criterion.

### Validation result

Passed: canonical ownership, preservation, badges, official references, scenarios, questions, filenames, and internal links verified.

## AWS-023 — VPC endpoints and PrivateLink

### Official requirement

Expand private-service connectivity at the authorized owner.

### Canonical target

07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md

### Existing files reviewed

Existing endpoint lesson, VPC index/overview, and connectivity guide.

### Official sources used

Official PrivateLink, gateway/interface endpoint, endpoint-service, and private-DNS docs; checked 2026-07-23.

### Gap being resolved

Gateway/interface selection, DNS, security, availability, and cost were incomplete.

### CPP content added

Private AWS service access and endpoint/PrivateLink recognition.

### SAA content added

Route-table versus ENI integration, policies/security groups, zonal placement, provider/consumer, DNS, HA, cost.

### Networking scenarios or comparisons added

Gateway/interface; endpoint/NAT/peering; cross-account private service.

### Existing content preserved

The complete pre-existing lesson, with a bounded supplement appended.

### Content removed or corrected

Clarified that endpoint types have different routing, DNS, security, HA, and cost models.

### Badge decision

CPP and SAA: substantive dual-certification coverage.

### Remaining work

None for this criterion.

### Validation result

Passed: canonical ownership, preservation, badges, official references, scenarios, questions, filenames, and internal links verified.

## AWS-024 — Hybrid and multi-VPC connectivity

### Official requirement

Expand peering, Transit Gateway, VPN, and Direct Connect selection.

### Canonical target

15-comparisons-and-decision-guides/networking/02-vpc-connectivity-options.md

### Existing files reviewed

Existing guide plus peering, VPN, Direct Connect, VPC, and index owners.

### Official sources used

Official peering, Transit Gateway, Site-to-Site VPN, Direct Connect, and RAM docs; checked 2026-07-23.

### Gap being resolved

Topology, routing, overlap, resilience, encryption, operations, and cost depth was incomplete.

### CPP content added

Private VPC, hub, encrypted-internet, and dedicated-hybrid service recognition.

### SAA content added

Peering limits, TGW routing/sharing, VPN tunnels, DX VIF/gateway/resilience, failures, trade-offs.

### Networking scenarios or comparisons added

Mesh/hub; centralized services/egress; VPN backup; admin alternatives.

### Existing content preserved

The complete pre-existing guide and focused service lessons.

### Content removed or corrected

Made peering non-transitivity, overlap, and edge-to-edge limits explicit.

### Badge decision

CPP and SAA: both recognition and architecture selection are present.

### Remaining work

Inspection implementation and unrelated admin lessons remain later work.

### Validation result

Passed: canonical ownership, preservation, badges, official references, scenarios, questions, filenames, and internal links verified.

## AWS-025 — Route 53 and CloudFront

### Official requirement

Connect DNS routing, CDN caching, and global network acceleration.

### Canonical target

15-comparisons-and-decision-guides/networking/04-dns-edge-and-global-routing.md

### Existing files reviewed

Route 53, CloudFront, Global Accelerator, category, and comparison owners.

### Official sources used

Official Route 53, CloudFront, and Global Accelerator docs; checked 2026-07-23.

### Gap being resolved

No owner joined DNS, caching, health routing, anycast entry, failure, security, and cost.

### CPP content added

Service recognition, hosted zones/aliases, CDN versus accelerator, pricing factors.

### SAA content added

Policy/health selection, cache/origin control, signed access, endpoint groups/dials, failure, security, cost.

### Networking scenarios or comparisons added

DNS failover; CDN front door; anycast multi-Region; three-service comparison.

### Existing content preserved

Focused service lessons remain canonical and linked.

### Content removed or corrected

Clarified dynamic CloudFront delivery and that Global Accelerator does not cache.

### Badge decision

CPP and SAA: recognition and design selection are substantive.

### Remaining work

API Gateway is cross-reference only; its later lesson was not edited.

### Validation result

Passed: canonical ownership, preservation, badges, official references, scenarios, questions, filenames, and internal links verified.
