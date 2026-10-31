# Elastic Load Balancing

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Elastic Load Balancing (ELB) is a managed service that distributes traffic across healthy targets. A load balancer can be internet-facing or internal, listens on configured ports and protocols, and forwards requests through target groups. Targets can include EC2 instances, IP addresses, containers, and, where supported, Lambda functions.

## Types and Selection

| Type | Layer and protocols | Best fit | Important capabilities |
|---|---|---|---|
| Application Load Balancer (ALB) | Layer 7; HTTP and HTTPS | Web applications, APIs, containers | Host-, path-, header-, method-, and query-based routing; WebSockets; Lambda targets |
| Network Load Balancer (NLB) | Layer 4; TCP, UDP, and TLS | High-throughput or low-latency traffic | Static IP per enabled AZ, source-IP considerations, TLS termination or pass-through patterns |
| Gateway Load Balancer (GWLB) | Layer 3 gateway plus GENEVE | Virtual firewalls and inspection appliances | Transparent insertion and scaling of appliance fleets |
| Classic Load Balancer | Earlier generation | Legacy workloads only | Historical awareness; prefer a current type for new designs |

ALB understands HTTP semantics. NLB makes transport-level decisions. GWLB is for appliances, not an application endpoint.

## Core Concepts and How It Works

- A **listener** accepts a protocol and port and evaluates forwarding rules.
- A **target group** defines destinations, health-check settings, and routing behavior.
- A **health check** decides whether a target receives new traffic; application repair still needs replacement automation.
- **Cross-zone load balancing** controls distribution to targets in other enabled AZs. Defaults and charging behavior vary by type, so verify current documentation.
- **TLS termination** can use a certificate on an ALB or NLB listener. Configure encryption to targets separately when required.

## High Availability and Resilience

Enable at least two Availability Zones and place healthy targets in each. ELB provides a managed endpoint but does not create targets or make stateful applications fault tolerant. Combine it with Auto Scaling or another replacement mechanism. Deregistration delay lets in-flight requests finish when a target is removed.

## Security and Shared Responsibility

AWS operates the service. Customers choose public or internal exposure, listener protocols, TLS policies and certificates, security groups where supported, target reachability, logging, and application authorization. Restrict target security groups to the load balancer where possible.

## Performance, Scalability, and Cost

ELB scales as a managed service; targets must scale independently. Charges are based conceptually on running load balancer time and processed capacity or usage dimensions. Data transfer and related services add cost. Select by protocol and routing requirements, not a blanket cost rule.

## CPP Knowledge

Recognition clues are **managed traffic distribution**, **health checks**, and **one endpoint for multiple targets**. ELB routes traffic; EC2 Auto Scaling changes capacity.

## SAA Architecture and Design

- Use ALB for HTTPS APIs with content-based routing.
- Use NLB for TCP/UDP, static-IP requirements, or demanding connection performance.
- Use GWLB to insert a scalable fleet of security appliances.
- Use an internal load balancer for private tiers and an internet-facing one for public entry.
- Pair multi-AZ targets, meaningful health checks, and automated replacement.

## Common Exam Traps

- Health checks stop routing; they do not repair a target.
- ELB and Auto Scaling solve different problems and are often paired.
- ALB does not normally provide fixed IPs; NLB supports static per-AZ IPs.
- GWLB distributes traffic to appliances, not HTTP microservices.

## Practice Questions

1. Which type supports host- and path-based HTTP routing?
2. Which type transparently inserts virtual firewalls?
3. Does ELB alone guarantee application fault tolerance?

<details><summary>Answers</summary>

1. ALB. 2. GWLB. 3. No; resilient targets, replacement, and fault-tolerant application and data tiers are also required.

</details>

## References

- [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
- [Elastic Load Balancing features](https://aws.amazon.com/elasticloadbalancing/features/)
- [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)

Official references checked: 2026-07-22.
