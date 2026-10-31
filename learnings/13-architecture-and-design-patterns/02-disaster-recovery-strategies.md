# Disaster Recovery Strategies

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Disaster recovery (DR) prepares a workload to restore acceptable service after a major disruption. It is one part of business continuity and is different from routine high availability: Multi-AZ redundancy can absorb many component or zonal failures, while DR addresses an event that prevents a workload from meeting business objectives in its primary location.

## Resilience Terms

| Term | Meaning |
|---|---|
| Availability | Whether the workload is accessible and functioning when required |
| Durability | Likelihood that stored data remains intact over time |
| Reliability | Ability to perform correctly and consistently and recover from failure |
| High availability | Redundancy, detection, and failover used to reduce downtime |
| Fault tolerance | Continued operation despite a failure, generally with more redundancy and cost |
| Disaster recovery | Restoration after a major disruption |
| Business continuity | Maintaining critical business operations during and after disruption |

These terms overlap, but they are not synonyms.

## RTO and RPO

- **Recovery Time Objective (RTO):** maximum acceptable delay between interruption and restoration.
- **Recovery Point Objective (RPO):** maximum acceptable amount of data loss expressed as time since the last usable recovery point.

An RTO of four hours means the architecture and operating procedure should support restoration within four hours. An RPO of fifteen minutes means the business accepts losing no more than approximately fifteen minutes of changes. These are business objectives—not automatic AWS guarantees.

Lower objectives usually require more frequent or continuous replication, automation, pre-provisioned capacity, testing, cost, and operational discipline.

## Strategy Decision Table

| Strategy | Recovery environment before disaster | Relative recovery interruption | Relative data-loss potential | Steady-state cost | Complexity |
|---|---|---|---|---|---|
| Backup and restore | Backups and deployment artifacts | Highest of these strategies | Depends on backup frequency and usability | Lowest | Lower steady-state; restore procedure still must be engineered |
| Pilot light | Core data/services active; most application capacity absent or stopped | Lower than backup/restore when prepared | Often reduced with continuous replication plus backups | Low to medium | Requires deployment and scale-out during recovery |
| Warm standby | Reduced-capacity but functional environment | Lower than pilot light | Based on replication and recovery design | Medium to high | Requires routing and scale-up |
| Multi-site active-active | Multiple environments actively serve traffic | Lowest potential interruption for many infrastructure failures | Depends on replication, consistency, and the failure type | Highest | Highest routing, data, deployment, and operations complexity |

The table is relative, not a promise of exact RTO or RPO.

## Backup and Restore

Back up data, configuration, application artifacts, and infrastructure definitions. During recovery, restore data and deploy capacity in the recovery location.

- Good fit when longer RTO/RPO and lower steady-state infrastructure cost are acceptable.
- Infrastructure as Code reduces configuration error and recovery time.
- Cross-Region or cross-account backup copies can improve isolation.
- Restore testing is essential; a successful backup job does not prove that a workload can be restored.
- Point-in-time backups can protect against corruption in ways that blindly replicated current state may not.

## Pilot Light

Keep critical data and core services current in the recovery Region while most application capacity is not running. Recovery provisions or starts the missing components and scales them to production capacity.

Pilot light usually offers a lower potential RTO than backup and restore, but depends on control-plane operations, service quotas, synchronized configuration, and tested automation. Continuous replication needs point-in-time backups as a separate defense against replicated corruption or deletion.

## Warm Standby

Run a complete but reduced-capacity copy of the workload in the recovery Region. It can handle limited traffic and scales up during recovery.

Warm standby costs more than pilot light but removes more provisioning work from the critical recovery path. Verify that it can accept traffic, scale to production load, access current secrets and keys, and operate without hidden dependencies on the failed Region.

## Multi-Site Active-Active

Multiple Regions serve production traffic at the same time. Traffic management removes an unhealthy Region and the remaining environment absorbs its load.

This can minimize interruption for some failures, but it creates the hardest data-consistency, conflict-resolution, deployment, quota, security, and operational problems. Backups remain necessary for corruption or malicious change. Never describe active-active as guaranteeing zero downtime or zero data loss.

## Failover and Failback

Failover is only half of recovery. A runbook should define:

1. Detection and authority to declare a disaster.
2. Protection against false or oscillating failover.
3. Data recovery or replication validation.
4. Capacity activation and configuration checks.
5. Traffic routing and application verification.
6. Stakeholder communication and evidence capture.
7. Failback after the primary location is safe, including data reconciliation and a controlled traffic shift.

Automatic failover can reduce delay but can also amplify a bad health signal. Choose manual, automated, or approval-gated execution based on risk.

## Backup Versus Replication

Replication keeps another copy current for availability or recovery, but can also copy unwanted changes. Backups preserve recovery points and are useful for corruption, deletion, or ransomware scenarios. High availability, replication, and backup solve different failure modes; mature workloads often need all three.

## Security

- Encrypt backups and replicas and control KMS key access in every recovery Region/account.
- Separate duties for backup administration and restore approval where required.
- Use cross-account isolation and immutable controls when the threat model justifies them.
- Keep secrets, certificates, IAM roles, network controls, and logging available in recovery.
- Test recovery without exposing production data or weakening access controls.

## Monitoring and Recovery Testing

Monitor backup completion, replication health and lag indicators, recovery-environment drift, health checks, service quotas, and application business metrics. Test restores and full workload recovery on a schedule. Exercises should verify RTO/RPO evidence, dependencies, scale-up, traffic movement, security, communications, and failback.

## Cost and Trade-Offs

Lower recovery objectives generally increase storage, replication, compute, data-transfer, testing, and staff costs. Compare that cost with the business impact of downtime and data loss. The simplest strategy that satisfies verified requirements is usually preferable to an untested active-active design.

## CPP Exam Focus

- RTO concerns acceptable recovery time; RPO concerns acceptable data loss measured in time.
- Backups, replication, high availability, and disaster recovery are related but different controls.
- More continuously running recovery infrastructure generally increases cost and reduces potential recovery delay.

## SAA Design Scenarios

- **Long recovery window and cost priority:** backup and restore with automated infrastructure deployment and tested recovery.
- **Core database must remain replicated but compute can wait:** pilot light.
- **Recovery environment must immediately handle limited traffic:** warm standby.
- **Both Regions must normally serve users:** active-active, after resolving consistency and conflict behavior.
- **Protection against accidental deletion:** retain independent recovery points rather than relying only on replication.

## Common Mistakes

- Treating RTO or RPO as an AWS service guarantee.
- Calling Multi-AZ high availability a complete Regional DR plan.
- Assuming replication replaces backup.
- Testing traffic failover without testing data recovery and failback.
- Keeping recovery infrastructure but not its IAM, KMS, secrets, quotas, or current configuration.

## Knowledge Check

1. **What is the main difference between RTO and RPO?** RTO limits acceptable restoration delay; RPO limits acceptable data loss expressed as time.
2. **Why does replication not replace backup?** Replication can propagate corruption or deletion, while backups preserve earlier recovery points.
3. **How does pilot light differ from warm standby?** Pilot light needs application components provisioned or started before serving; warm standby is already functional at reduced capacity.
4. **Why test failback?** Returning service can require data reconciliation and traffic changes that create a second outage if unplanned.
5. **Does active-active eliminate backups?** No. Data corruption and malicious changes still require recoverable points.

## Related Services

- [AWS Backup](../05-storage/aws-backup/01-overview.md)
- [Amazon Route 53](../07-networking-and-content-delivery/amazon-route-53/01-overview.md)
- [Amazon RDS](../06-databases/amazon-rds/01-overview.md)
- [Data-protection patterns](security/01-data-protection-patterns.md)

## References

- [AWS Disaster Recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html)
- [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
- [Back up data—Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/back-up-data.html)
- [Test resiliency as part of deployment](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_tracking_change_management_resiliency_testing.html)

Checked: 2026-07-24.
