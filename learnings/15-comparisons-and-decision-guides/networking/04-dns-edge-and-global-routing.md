# DNS, Edge Delivery, and Global Routing Decisions

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Amazon Route 53, Amazon CloudFront, and AWS Global Accelerator can all direct global users, but they act at different layers. Route 53 answers DNS queries, CloudFront delivers and caches HTTP content, and Global Accelerator provides fixed anycast entry addresses and network-path optimization to Regional endpoints.

## Core Decision Table

| Dimension | Route 53 | CloudFront | Global Accelerator |
|---|---|---|---|
| Primary role | Authoritative DNS, domain registration, health-aware DNS routing | Content delivery network and HTTP edge proxy/cache | Global TCP/UDP traffic accelerator |
| Client entry | DNS name and records | Distribution domain or alternate domain name | Static anycast IP addresses and accelerator DNS name |
| Caching | DNS answers are cached by resolvers; no application-content cache | Yes, according to cache behavior and cache key | No content caching |
| Endpoint decision | Routing policy when answering DNS | Cache behavior selects an origin; origin groups can support failover | Endpoint groups, health, weights, and traffic dials |
| Best signal | DNS, hosted zones, aliases, policy-based answers | HTTP(S), S3/ALB/API/custom origin, cache, OAC, signed access | Static IP allowlisting, TCP/UDP, fast Regional endpoint failover |
| Failure consideration | DNS TTL and resolver caching affect change visibility | Cached objects may remain available; origin and cache behavior determine misses | Existing fixed entry addresses remain; health routing changes endpoints |

## Route 53 Foundations

- A **public hosted zone** answers on the public internet; a **private hosted zone** answers through Route 53 Resolver for associated VPCs.
- Common records include A (IPv4), AAAA (IPv6), CNAME (name to name), MX, TXT, NS, and SOA.
- An **alias record** is an AWS Route 53 extension that can point to supported AWS resources and can be used at the zone apex where a CNAME cannot.
- Health checks can monitor endpoints or calculated health. Alias records can evaluate target health for supported targets.
- Route 53 is a global service, while many destinations it names are Regional.

## Route 53 Routing Policies

| Policy | Decision basis | Health behavior | Typical use | Common trap |
|---|---|---|---|---|
| Simple | One resource or a set returned without policy weighting | Health-check association is limited compared with health-aware policies | Single application endpoint | Not active-passive failover |
| Weighted | Relative weights | Can omit unhealthy records when checks/evaluate-target-health apply | Blue/green, canary, controlled split | Weights are relative, not guaranteed per-request percentages |
| Latency-based | AWS Region expected to provide lowest latency | Can exclude unhealthy endpoints | Multi-Region performance | Not the geographically closest Region by distance |
| Failover | Primary then secondary | Health determines when secondary is returned | Active-passive recovery | DNS caches can delay client observation |
| Geolocation | User DNS-query location | Can combine with health checks | Localization, compliance, content licensing | Routes by user location, not resource proximity |
| Geoproximity | Resource location plus optional bias | Can combine with health-aware records | Shift geographic boundaries between resources | Different from geolocation; bias changes the catchment area |
| Multi-value answer | Returns multiple healthy records | Health checks supported | Simple DNS-level distribution across addresses | Not a replacement for a load balancer |

## CloudFront Foundations

- A **distribution** has one or more origins and cache behaviors. Origins can include S3, load balancers, API Gateway endpoints, EC2/custom HTTP servers, and other supported sources.
- A cache behavior matches a path pattern, selects an origin, defines allowed methods and viewer protocol policy, and uses cache/origin-request policies.
- The cache key determines which viewer request values create distinct cached objects. Forward only values the origin needs to improve cache efficiency.
- TTL settings and origin cache headers control freshness. Invalidation removes selected paths before normal expiry and has a cost/operations dimension.
- Origin Access Control (OAC) is the preferred protected-access design for supported S3 origins; it lets CloudFront reach the bucket without public read access.
- Signed URLs are well suited to individual files or client-specific access. Signed cookies are useful for access to multiple restricted files without changing every URL.
- CloudFront supports static and dynamic HTTP content, HTTPS, AWS WAF integration, and AWS Shield protections. It is not object storage.

## Global Accelerator Foundations

- A standard accelerator provides fixed anycast IP addresses that enter the AWS global network near clients.
- Listeners accept TCP or UDP ports and send traffic to endpoint groups. Each endpoint group is associated with one AWS Region.
- Supported standard endpoints include Application Load Balancers, Network Load Balancers, EC2 instances, and Elastic IP addresses.
- Health checks and endpoint weights select healthy endpoints. A traffic dial changes how much of the traffic already directed to an endpoint group is allowed to reach that Region.
- Global Accelerator does not cache content. It is valuable for non-cacheable application traffic, fixed-IP allowlists, multi-Region endpoints, and rapid network-level failover.

## Scenario Decisions

### Global website with S3 images and private bucket access

Use CloudFront with an S3 origin and OAC. Use Route 53 alias records for the application domain. Global Accelerator is unnecessary when CDN caching and HTTP edge delivery solve the requirement.

### Multi-Region TCP application with fixed client allowlists

Use Global Accelerator in front of healthy Regional endpoints. Route 53 can name the accelerator, but DNS-only failover does not provide the same fixed anycast entry addresses or network path.

### Active-passive application with a recovery endpoint

Route 53 failover routing is suitable when DNS-based recovery and its TTL behavior meet requirements. Global Accelerator is an alternative when supported endpoints, fixed IPs, and faster health-based network redirection matter. Neither repairs the application or data tier.

### Gradual release

Use weighted Route 53 records for DNS-level distribution between endpoints. Use a Global Accelerator traffic dial to reduce or increase traffic sent to an endpoint group after the accelerator has selected a Region. Use CloudFront continuous deployment or behavior/origin controls only when the HTTP delivery requirement fits.

## Security, Availability, Performance, and Cost

- Protect CloudFront origins so users cannot bypass edge controls. Require HTTPS, restrict origin access, and attach WAF where application-layer filtering is needed.
- Route 53 health checks and Global Accelerator checks need reachable, meaningful health endpoints. A shallow check can route traffic to an application that is technically up but unusable.
- Design multi-Region data consistency and failover; routing services do not replicate data.
- Costs differ: Route 53 hosted zones, queries and health checks; CloudFront requests, transfer and invalidations; Global Accelerator usage and data transfer. Compare end-to-end architecture rather than assuming one is always cheaper.

## CPP Recognition

- DNS, domain registration, hosted zone, alias: Route 53.
- CDN, edge cache, distribution, origin: CloudFront.
- Static anycast IPs, TCP/UDP, healthy Regional endpoint: Global Accelerator.

## Common Mistakes

- Saying CloudFront supports only static content.
- Expecting Global Accelerator to cache files.
- Treating multi-value Route 53 routing as an application load balancer.
- Forgetting DNS TTL and resolver caches during failover.
- Making an S3 origin public instead of using OAC for a supported protected-origin design.
- Assuming global routing automatically provides multi-Region data resilience.

## Knowledge Check

1. Which service provides a CDN cache?
2. Which Route 53 policy implements active-passive DNS failover?
3. Which service supplies fixed anycast entry IPs for supported Regional endpoints?
4. What is the difference between geolocation and geoproximity routing?
5. Why use CloudFront OAC with an S3 origin?

<details><summary>Answers</summary>

1. CloudFront. 2. Failover routing. 3. Global Accelerator. 4. Geolocation uses the user's location; geoproximity uses resource locations and optional bias to shift traffic boundaries. 5. To let CloudFront access a supported S3 origin without granting public bucket read access.

</details>

## Canonical Lessons

- [Amazon Route 53](../../07-networking-and-content-delivery/amazon-route-53/01-overview.md)
- [Amazon CloudFront](../../07-networking-and-content-delivery/amazon-cloudfront/01-overview.md)
- [AWS Global Accelerator](../../07-networking-and-content-delivery/aws-global-accelerator/01-overview.md)
- [CloudFront vs Global Accelerator](01-cloudfront-vs-global-accelerator.md)

## References

- [Choosing a Route 53 routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
- [Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
- [Route 53 alias records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-aws-resources.html)
- [CloudFront cache behavior settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesCacheBehavior.html)
- [Restrict access to an S3 origin with OAC](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
- [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-choosing-signed-urls-cookies.html)
- [How Global Accelerator works](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works.html)
- [Global Accelerator endpoint groups](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html)

Official references checked: 2026-07-23.
