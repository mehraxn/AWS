# Phase 6 Batch 3 Fact Corrections

## Public subnet reachability is not created by a route alone

Affected path:

`07-networking-and-content-delivery/amazon-vpc/09-subnets-route-tables-and-internet-gateways.md`

Related backlog ID:

AWS-021

Previous claim:

The prior distributed coverage could be read as if an internet-gateway route alone made an IPv4 resource internet reachable.

Corrected claim:

A public subnet has a route to an internet gateway, but an IPv4 instance also needs a public IPv4 address or Elastic IP, compatible security controls, and correct host configuration. The internet gateway provides the address translation for the publicly addressed resource.

Reason:

Subnet classification, resource addressing, routing, and filtering are separate requirements.

Official source:

Official Amazon VPC subnet and internet-gateway documentation.

Date checked:

2026-07-23

Severity:

High — affects reachability and security scenario answers.

## VPC endpoint types are not interchangeable

Affected path:

`07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md`

Related backlog ID:

AWS-023

Previous claim:

Generic endpoint wording did not fully distinguish routing, DNS, security-group, availability, and pricing behavior.

Corrected claim:

Gateway endpoints use route-table integration for supported services. Interface endpoints powered by AWS PrivateLink create subnet ENIs with private IP addresses, can use security groups and private DNS, and have different availability and cost considerations.

Reason:

Choosing an endpoint type is an architecture decision, not only a service-label distinction.

Official source:

Official AWS PrivateLink and VPC endpoint documentation.

Date checked:

2026-07-23

Severity:

High — affects private-connectivity design and cost.

## VPC peering does not provide transitive routing

Affected path:

`15-comparisons-and-decision-guides/networking/02-vpc-connectivity-options.md`

Related backlog ID:

AWS-024

Previous claim:

A basic connectivity list could imply that chained peerings form transit or that overlapping VPC CIDRs are acceptable.

Corrected claim:

VPC peering is a one-to-one, non-transitive relationship; overlapping CIDRs prevent peering, and edge-to-edge routing through a peer is unsupported. Transit Gateway is the routed-hub choice when centralized transitive connectivity is required.

Reason:

Topology and routing constraints determine whether peering or a hub service is appropriate.

Official source:

Official Amazon VPC peering and AWS Transit Gateway documentation.

Date checked:

2026-07-23

Severity:

High — affects multi-VPC routing designs.

No useful existing note was deleted while applying these corrections.
