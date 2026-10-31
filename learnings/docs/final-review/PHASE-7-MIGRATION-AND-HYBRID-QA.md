# Phase 7 Migration and Hybrid-Cloud QA

## Scope

Reviewed migration and hybrid-cloud canonical owners, category navigation, related storage and networking comparisons, and learning-path placement.

## Result

Passed with a product-availability limitation. The material keeps these choices distinct:

- AWS DataSync for managed online data movement.
- AWS Database Migration Service for database migration and replication scenarios.
- AWS Snow Family for supported offline/edge-transfer scenarios.
- AWS Storage Gateway for hybrid storage interfaces.
- AWS Outposts, Local Zones, and Wavelength for different infrastructure-placement needs.
- Direct Connect, VPN, Transit Gateway, and PrivateLink for different connectivity requirements.

No unsupported zero-downtime, guaranteed-lossless, universal-availability, or effortless-migration claim was found. Availability, supported sources and targets, appliance offerings, and Regional coverage remain volatile.

## Corrections made in Phase 7

The CPP and SAA paths now explicitly include migration and hybrid-cloud review. No service-content rewrite was justified.

## Human review

Verify current product availability, supported Regions, source/target matrices, and hardware or ordering options against official AWS documentation before release.
