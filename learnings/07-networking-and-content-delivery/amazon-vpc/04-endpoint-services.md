# VPC Endpoint Services

## Simple definition

A **VPC endpoint service** is a way to **privately share your own service** with other VPCs using **AWS PrivateLink**. It lets consumers connect to your service **without using the public internet**.

## Core idea in plain English

Think of it like this:

* You have an application running in AWS.
* You want other AWS accounts or VPCs to use it.
* But you do **not** want to expose it with a public IP or over the internet.

A VPC endpoint service solves this by letting you publish your service privately. Other VPCs create **interface endpoints** to reach it.

### Important note about the terminology

For exam study, it helps to split the **AWS PrivateLink** model into **two main parts**:

* **VPC endpoint service** = the **provider side**
* **Interface VPC endpoint** = the **consumer side**

So, when people discuss **private VPC endpoint connectivity for custom services**, they often describe it as these two sides working together.

However, remember that **VPC endpoints** in AWS more broadly also include **gateway endpoints** for **Amazon S3** and **Amazon DynamoDB**. So do **not** think that all VPC endpoints are only endpoint services and interface endpoints.

## Main use cases

* Share an internal application privately with another AWS account
* Offer a SaaS service securely to customers
* Keep traffic inside the AWS network
* Reduce exposure to the internet
* Control who can connect to your service

## Key features

* Built on **AWS PrivateLink**
* Provides **private connectivity** between consumer VPCs and your service
* Traffic stays on the **AWS network**
* Usually backed by a **Network Load Balancer (NLB)**
* Can also be used with **Gateway Load Balancer (GWLB)** in special appliance scenarios
* Supports **access control**, so you choose who can connect
* Can require **manual acceptance** of connection requests
* Can use **private DNS names** for easier access

## How it works

### 1. Service provider side

The service owner creates:

* a service running in a VPC
* a **Network Load Balancer** in front of that service
* a **VPC endpoint service** connected to that load balancer

### 2. Service consumer side

The customer or other AWS account creates an:

* **interface VPC endpoint**

This creates elastic network interfaces with private IP addresses inside the consumer VPC.

### 3. Private connection happens

The consumer sends traffic to the interface endpoint.
That traffic is routed privately through **AWS PrivateLink** to the provider’s endpoint service.

### 4. Access is controlled

The provider can:

* allow only specific AWS accounts
* require endpoint connection approval
* monitor and manage the service centrally

## Why it is important for the exam

This topic matters because AWS exams often test whether you understand:

* **private connectivity** vs public internet access
* the difference between **endpoint service** and **VPC endpoint**
* when to use **AWS PrivateLink** instead of other networking options
* how to share services securely across accounts or VPCs

For the exam, remember this:

> **Endpoint service = provider side**
>
> **Interface endpoint = consumer side**

That is one of the most important ideas.

A good way to memorize it is this:

* **PrivateLink setup for your own service** = endpoint service + interface endpoint
* **Gateway endpoint** = separate endpoint type for S3 and DynamoDB

## Related AWS services and differences

### VPC endpoint service vs Interface VPC endpoint

* **VPC endpoint service** = the service being offered privately
* **Interface VPC endpoint** = the private connection a consumer creates to reach that service

Provider publishes. Consumer connects.

### VPC endpoint service vs Gateway endpoint

* **Endpoint service** uses **AWS PrivateLink**
* **Gateway endpoint** is only for **Amazon S3** and **Amazon DynamoDB**
* Gateway endpoints are not used to publish your own service

### VPC endpoint service vs VPC peering

* **Endpoint service / PrivateLink** connects to a specific service
* **VPC peering** connects whole VPCs at the network level
* PrivateLink is more controlled and service-focused

### VPC endpoint service vs Transit Gateway

* **PrivateLink / endpoint service** is for private access to a specific application or service
* **Transit Gateway** is for connecting many networks together, such as multiple VPCs and on-premises networks

### VPC endpoint service vs Internet Gateway / NAT Gateway

* **Endpoint service** keeps traffic private inside AWS
* **Internet Gateway** and **NAT Gateway** are used when resources need internet access

## Common exam traps

### Trap 1: Confusing endpoint service with endpoint

Many questions mix these up.

* **Endpoint service** = provider side
* **Interface endpoint** = consumer side

### Trap 2: Thinking all VPC endpoints are the same

They are not.

* **Interface endpoint** = powered by PrivateLink
* **Gateway endpoint** = for S3 and DynamoDB only
* **Endpoint service** = lets you publish your own service privately

### Trap 3: Choosing VPC peering when only one service needs to be shared

If the goal is to expose **one application privately**, PrivateLink is often the better answer.

### Trap 4: Thinking it uses the public internet

It does not. Traffic stays on the AWS network.

### Trap 5: Forgetting the load balancer

A VPC endpoint service is commonly backed by a **Network Load Balancer**.

## Easy real-world example

A company has a billing application running in a private VPC.
Its partner companies need access to that billing API.

The company does not want to make the API public.
So it:

* places the application behind a **Network Load Balancer**
* creates a **VPC endpoint service**
* allows partner AWS accounts to connect

Each partner creates an **interface VPC endpoint** in its own VPC.
Now the partners can use the billing API privately, without using the internet.

## Final summary

A VPC endpoint service lets you **privately publish your own service** to other VPCs using **AWS PrivateLink**. It is mainly a **provider-side** concept. Consumers access it by creating **interface VPC endpoints**. It is useful when you want **secure, private, service-level connectivity** without exposing services to the public internet.

## Short exam answer

**A VPC endpoint service is a provider-side AWS PrivateLink resource that lets you privately expose a service, usually behind a Network Load Balancer, so other VPCs can connect through interface endpoints without using the public internet.**

## Memory trick

**Service serves, endpoint enters.**

* **Endpoint service** = the service provider shares
* **Interface endpoint** = the consumer enters through it

Another memory line:

**PrivateLink = private path to a service, not full network-to-network access.**

## Batch 3 Endpoint Selection Supplement

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

### Gateway and Interface Endpoints

| Dimension | Gateway endpoint | Interface endpoint |
|---|---|---|
| Connectivity | Supported gateway services | AWS services, endpoint services, Marketplace services, and other supported PrivateLink targets |
| VPC implementation | Route-table target | Endpoint network interfaces with private IP addresses in selected subnets |
| Security | Endpoint policy plus destination resource/IAM policies | Security groups on endpoint ENIs plus endpoint and service policies |
| DNS | Service routes use destination prefix lists | Regional/zonal endpoint DNS; private DNS can map the normal Regional service name to endpoint ENIs |
| Cost concept | No endpoint hourly or data-processing charge for the gateway endpoint itself under current pricing | Charged per endpoint AZ-hour and data processed; verify current pricing |
| Availability | Associate required route tables | Select multiple AZs for resilient production access |

Gateway endpoints currently support Amazon S3 and DynamoDB. They add service-prefix routes to associated route tables and do not use security groups. They are not reachable through VPC peering, Transit Gateway, VPN, or Direct Connect from another network; create appropriate endpoints or use a supported alternative in the network that needs access.

Interface endpoints are powered by AWS PrivateLink. AWS creates an endpoint network interface in each selected subnet, one subnet per Availability Zone. Private DNS requires VPC DNS support and hostnames; when enabled for an AWS service, the ordinary Regional service hostname can resolve to the endpoint's private addresses inside the VPC.

### PrivateLink Provider and Consumer

For a privately published application, the provider places service targets behind a supported load balancer and creates an endpoint service. The provider grants principals permission and may require connection acceptance. A consumer creates an interface endpoint in its VPC and controls access with endpoint security groups and policies.

PrivateLink exposes a specific service rather than providing full, transitive network connectivity. This reduces route exchange and overlapping-CIDR concerns compared with peering, but consumers still need DNS, authorization, resilient endpoint placement, and application-layer security.

### Endpoint, NAT Gateway, or Peering

- Choose a **gateway endpoint** for private access to a supported gateway service when its route-table model fits.
- Choose an **interface endpoint** for a supported PrivateLink service, private API, partner service, or provider endpoint service.
- Choose a **NAT gateway** when private workloads need broader outbound IPv4 access to public endpoints or the internet.
- Choose **VPC peering or Transit Gateway** when workloads need routed access to many resources in another network rather than one published service.

### Security and Resilience

- Apply least-privilege endpoint policies, IAM and resource policies; an endpoint does not bypass service authorization.
- Restrict interface endpoint security groups to intended clients and ports.
- Use private DNS deliberately and test split-horizon/on-premises resolution with Route 53 Resolver where hybrid clients need access.
- Place interface endpoint ENIs in multiple AZs when an AZ impairment must not remove access.
- Monitor connection, application, DNS and Flow Log evidence; PrivateLink is not a packet-inspection service.

### SAA Scenarios

1. Private EC2 instances need S3 without NAT processing: use an S3 gateway endpoint and a least-privilege endpoint/bucket policy.
2. An internal API must be shared across accounts without full network routing: publish an endpoint service and let consumers create interface endpoints.
3. Hybrid clients must use an interface endpoint's private name: design Route 53 Resolver inbound endpoints/rules and verify DNS paths rather than assuming VPC-only DNS is visible on premises.
4. A production service depends on an interface endpoint: select endpoint subnets in multiple AZs and use the Regional DNS name/private DNS behavior.

### Knowledge Check

1. Which endpoint type adds routes rather than ENIs? **Gateway endpoint.**
2. Which endpoint type accepts security groups? **Interface endpoint.**
3. Does PrivateLink create transitive VPC routing? **No; it provides service-oriented private connectivity.**
4. Does a VPC endpoint replace IAM or resource policies? **No.**

### Official References

- [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/index.html)
- [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html)
- [Access AWS services through PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html)
- [Configure an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html)
- [Create an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html)

Official references checked: 2026-07-23.
