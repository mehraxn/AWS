# AWS Networking – Complete Cloud Practitioner Study Guide 

This README is written as an AWS exam coach would teach it: clearly, carefully, and with the exam traps explained before they hurt you.

It is designed for **AWS Certified Cloud Practitioner (CLF-C02)** study, but it is also strong enough to build good real-world understanding.

---

## How to use this file

Read this file in **three passes**:

**Pass 1 – Understanding**
Read from top to bottom once. Focus on the big picture: **who is connecting to whom, and why**.

**Pass 2 – Service mapping**
Read the comparison tables and the quick mapping section. This builds speed for multiple-choice questions.

**Pass 3 – Trap hunting**
Read the exam traps section carefully. Many AWS networking questions are really testing whether you can avoid a common mistake.

Every section answers these three questions:

1. **What is it?**
2. **What is fixed vs variable?**
3. **When do I choose it?**

---

## Table of contents

1. [The mental model: the six main connectivity situations](#1-the-mental-model-the-six-main-connectivity-situations)
2. [VPC to the internet](#2-vpc-to-the-internet)

   * Internet Gateway (IGW)
   * NAT Gateway
   * Egress-only Internet Gateway
3. [Private access from a VPC to AWS services](#3-private-access-from-a-vpc-to-aws-services)

   * Gateway VPC Endpoints
   * Interface VPC Endpoints / AWS PrivateLink
4. [VPC to VPC inside AWS](#4-vpc-to-vpc-inside-aws)

   * VPC Peering
   * AWS Transit Gateway
5. [On-premises network to AWS](#5-on-premises-network-to-aws)

   * AWS Site-to-Site VPN
   * AWS Direct Connect
   * Direct Connect + VPN
6. [End users to AWS](#6-end-users-to-aws)

   * AWS Client VPN
7. [Supporting concepts you must know](#7-supporting-concepts-you-must-know)
8. [Troubleshooting logic for exam questions](#8-troubleshooting-logic-for-exam-questions)
9. [Fast exam mapping cheat sheet](#9-fast-exam-mapping-cheat-sheet)
10. [Every exam trap catalogued](#10-every-exam-trap-catalogued)
11. [Memory anchors and mnemonics](#11-memory-anchors-and-mnemonics)
12. [One-line summary per service](#12-one-line-summary-per-service)

---

# 1. The mental model: the six main connectivity situations

Before memorizing services, lock this map into your head.

Almost every Cloud Practitioner networking question fits into one of these buckets:

```text
SITUATION                                      BEST FIRST ANSWER TO THINK OF
-----------------------------------------------------------------------------------------------
VPC resource needs public internet access      Internet Gateway (public subnet) or NAT Gateway
Private subnet needs outbound internet         NAT Gateway
VPC needs private access to AWS services       VPC Endpoint
VPC needs private access to another VPC        VPC Peering or Transit Gateway
On-premises network needs AWS access           Site-to-Site VPN or Direct Connect
Remote user laptop needs AWS access            Client VPN
```

Now turn that into a decision question:

* Is the destination the **public internet**?
* Is the destination **another VPC**?
* Is the destination **an AWS managed service** like S3 or SQS?
* Is the source an **office/data center**?
* Is the source an **individual user**?

That one habit will solve a huge percentage of exam questions.

---

# 2. VPC to the internet

This section covers how resources inside a VPC reach the internet, or are reached from the internet.

The key idea is this:

* **Public subnet resources** can use an **Internet Gateway**.
* **Private subnet resources** that need only outbound access usually use a **NAT Gateway**.
* **IPv6 outbound-only internet access** usually uses an **Egress-only Internet Gateway**.

---

## 2A. Internet Gateway (IGW)

### What it is

An **Internet Gateway** is a managed VPC component that allows communication between your VPC and the public internet.

Think of it as the **door between your VPC and the internet**.

It is not an EC2 instance. It is not a firewall. It is not something you patch or scale manually. AWS manages it for you.

### Core idea in plain English

If a resource in your VPC should be publicly reachable, or should directly talk to the internet using a public IP address, your VPC needs an **IGW**.

### What is fixed

* It is **managed by AWS**.
* It is **horizontally scaled, redundant, and highly available**.
* It supports **IPv4 and IPv6**.
* It attaches to **one VPC at a time**.
* It is the normal answer for **public internet connectivity**.
* There is **no separate hourly charge for the IGW itself**.

### What is variable

* Which VPC it is attached to.
* Which route tables point internet-bound traffic to it.
* Which subnets become public because of those route tables.
* Which resources in those subnets have public IPv4 addresses.

### How it works

For an EC2 instance to use an IGW properly, **all of these usually need to be true**:

1. The VPC has an **Internet Gateway attached**.
2. The subnet’s route table has a route like **`0.0.0.0/0 -> igw-id`** for IPv4.
   For IPv6 internet access, it would be **`::/0 -> igw-id`**.
3. The resource has a **public IPv4 address** if IPv4 internet access is needed.
4. Security Groups and NACLs allow the traffic.

### When to choose it

Choose an IGW when:

* An EC2 web server must be reachable from the internet.
* A public-facing ALB must receive traffic from users on the internet.
* A bastion host is placed in a public subnet.
* Public resources need direct internet access.

### Real-world examples

**Example 1 – Public web server**
You launch an EC2 instance that hosts a website. Users around the world must reach it.
That instance belongs in a **public subnet**, and the VPC needs an **IGW**.

**Example 2 – Public Application Load Balancer**
Your ALB must accept traffic from the internet and forward it to application servers in private subnets.
The ALB sits in public subnets that route to the **IGW**.

### What it is not

* It is **not a NAT Gateway**.
* It is **not a firewall**.
* It does **not automatically make all subnets public**.
* It does **not by itself assign public IPs**.

### Exam traps

**Trap 1 – “IGW attached” does not mean “subnet is public.”**
A subnet becomes public because its route table sends internet-bound traffic to the IGW.

**Trap 2 – No public IP, no direct IPv4 internet reachability.**
An EC2 instance in a public subnet without a public IPv4 address is not directly reachable from the IPv4 internet.

**Trap 3 – IGW does not filter traffic.**
Security Groups and NACLs control traffic, not the IGW.

**Trap 4 – One IGW per VPC at a time.**
Do not choose answers that imply multiple IGWs for one VPC for normal design.

---

## 2B. NAT Gateway

### What it is

A **NAT Gateway** is a managed NAT service that lets resources initiate outbound connections while preventing unsolicited inbound connections through that path.

At Cloud Practitioner level, the most common design is:

* Private instances live in **private subnets**.
* They need to go **out** to the internet for updates, package downloads, or external APIs.
* They should **not** be directly reachable from the internet.
* So they use a **NAT Gateway**.

### Core idea in plain English

A NAT Gateway is the **safe outbound door** for private resources.

Your private EC2 instance can go out to the internet, but outside users cannot start a connection back in through the NAT Gateway.

### Important modern clarity

At exam level, you will most often see the classic pattern:

* **Public NAT Gateway** used for internet-bound outbound traffic.
* It is commonly placed in a **public subnet**.
* It uses an **Elastic IP**.

However, in current AWS documentation, NAT gateway options are broader than older study notes often suggest. So do **not** memorize oversimplified statements like “all NAT Gateways always require public subnets and EIPs.”

For **Cloud Practitioner questions**, though, the classic answer is still usually the right one unless the question is very advanced.

### What is fixed

For the common Cloud Practitioner design pattern:

* Private subnet resources send outbound traffic to the NAT Gateway.
* The NAT Gateway then forwards that traffic onward.
* Unsolicited inbound internet connections to those private resources are not allowed through that path.
* NAT Gateway is **managed by AWS**.
* You **pay** for NAT Gateway usage.
* It is usually the best answer over NAT Instance in modern AWS questions.

### What is variable

* Which subnets route to it.
* Which Availability Zone or architecture pattern you deploy.
* Whether it is used for internet egress or other connectivity patterns.
* Cost, based on usage and architecture.

### The standard exam architecture pattern

```text
[Private EC2] -> route table -> [NAT Gateway] -> [Internet Gateway] -> Internet
```

In the standard design:

* The **private subnet route table** sends `0.0.0.0/0` to the NAT Gateway.
* The NAT Gateway has a path onward to the internet.
* The VPC also has an **IGW**.

### When to choose it

Choose NAT Gateway when:

* An EC2 instance in a private subnet needs OS patches from the internet.
* A workload in a private subnet must call a third-party API.
* You want outbound internet access without allowing direct inbound internet access.

### Real-world examples

**Example 1 – Private EC2 downloads updates**
A backend server in a private subnet must install Linux updates.
Use a NAT Gateway for outbound internet access.

**Example 2 – Lambda in a VPC calls an external API**
If Lambda is in private subnets and must call a SaaS API on the public internet, NAT Gateway is the usual solution.

### What it is not

* It is **not a replacement for an IGW** in the classic internet access pattern.
* It is **not for inbound internet access** to private resources.
* It is **not the first answer** when the destination is only S3 or DynamoDB privately.

### Exam traps

**Trap 1 – NAT Gateway is outbound-focused.**
If the question asks how internet users connect inbound to private instances, NAT Gateway is wrong.

**Trap 2 – NAT Gateway vs NAT Instance.**
If the question emphasizes managed service, availability, and low operational effort, choose NAT Gateway.

**Trap 3 – NAT Gateway usually costs money.**
If the question asks for the most cost-effective private access to S3, do not pick NAT Gateway. Pick a **Gateway VPC Endpoint**.

**Trap 4 – Read S3/DynamoDB questions carefully.**
If the destination is S3 or DynamoDB and the requirement is private access without internet, NAT Gateway is usually not the best answer.

**Trap 5 – Do not learn outdated absolutes.**
Older notes often say things like “NAT Gateway is always one-AZ only” or “always IPv4 only.” Current AWS documentation is more nuanced. For CLF-C02, focus on the common pattern: **private subnet outbound internet access**.

---

## 2C. Egress-only Internet Gateway

### What it is

An **Egress-only Internet Gateway** is used for **IPv6 outbound-only internet access** from your VPC.

### Core idea in plain English

It is like the IPv6 version of the “outbound-only” idea.

### What is fixed

* It is for **IPv6**.
* It allows **outbound communication** from your VPC to the internet.
* It prevents the internet from initiating unsolicited inbound IPv6 connections through that path.
* It is managed by AWS.

### What is variable

* Which route tables use it.
* Which VPC it is associated with.
* Which subnets send IPv6 internet traffic to it.

### When to choose it

Choose Egress-only IGW when:

* Your VPC uses IPv6.
* Resources need outbound-only IPv6 internet access.
* You do not want those resources directly reachable inbound over IPv6.

### Real-world example

Your private application servers use IPv6 addresses and must reach internet services outbound, but should not accept inbound connections from the IPv6 internet.
Use an **Egress-only Internet Gateway**.

### Exam trap

Do not confuse it with NAT Gateway.

* **NAT Gateway** is the usual private-subnet outbound internet answer in classic IPv4 questions.
* **Egress-only IGW** is the classic outbound-only answer for **IPv6** internet access.

---

# 3. Private access from a VPC to AWS services

Sometimes your workload does not need the public internet at all.

It only needs to reach AWS services like:

* S3
* DynamoDB
* SQS
* SNS
* Systems Manager
* Secrets Manager
* CloudWatch

In those cases, **VPC Endpoints** are a major exam topic.

The big idea is this:

> “How can my private subnet talk to AWS services without going through the public internet?”

Answer: **VPC Endpoints**.

---

## 3A. Gateway VPC Endpoints

### What it is

A **Gateway VPC Endpoint** is a special type of endpoint used for **Amazon S3** and **Amazon DynamoDB**.

It works through **route tables**.

### Core idea in plain English

If your EC2 instance in a private subnet needs private access to **S3 or DynamoDB**, a Gateway Endpoint is often the most exam-friendly answer.

### What is fixed

* Gateway Endpoints are for **S3 and DynamoDB**.
* They are commonly the best answer for private access to those services from within a VPC.
* They are implemented through **route tables**.
* They do **not** create an ENI in your subnet.
* They do **not** require an IGW or NAT device for that access.
* They are generally the **lowest-cost** answer for this use case.

### Important nuance you should know

Modern AWS supports more than one endpoint option for S3 and DynamoDB.
So the safest way to say it is:

* **Gateway Endpoint** is the classic, free, route-table-based endpoint type for **S3 and DynamoDB**.
* In many Cloud Practitioner questions, it is the right answer for private access to S3 or DynamoDB from a VPC.

### What is variable

* Which subnets and route tables use it.
* Which resources are allowed through policies.
* Whether it is used for S3 or DynamoDB.

### How it works

You create the endpoint and associate it with route tables. Traffic meant for S3 or DynamoDB is then routed privately over the AWS network.

### When to choose it

Choose a Gateway Endpoint when:

* A private EC2 instance needs to access S3 privately.
* A private EMR or application workload needs DynamoDB privately.
* The requirement says **do not use internet** or **do not use NAT** for S3/DynamoDB.
* The requirement says **most cost-effective** for S3 or DynamoDB private access.

### Real-world examples

**Example 1 – Private EC2 reads S3 objects**
An instance in a private subnet must download files from S3 without using the internet.
Use an **S3 Gateway Endpoint**.

**Example 2 – Private application reads DynamoDB**
A private service needs DynamoDB access without NAT Gateway cost.
Use a **DynamoDB Gateway Endpoint**.

### What it is not

* It is **not for every AWS service**.
* It does **not create a private ENI** in your subnet.
* It is **not AWS PrivateLink**.

### Exam traps

**Trap 1 – S3 and DynamoDB are special.**
Most other AWS services use **Interface Endpoints**.

**Trap 2 – Route table matters.**
If a Gateway Endpoint is created but the right route table is not used, the traffic may not work as expected.

**Trap 3 – Cheapest private S3/DynamoDB answer.**
If the question says **cost-effective** and the destination is S3 or DynamoDB, Gateway Endpoint is a strong answer.

---

## 3B. Interface VPC Endpoints / AWS PrivateLink

### What it is

An **Interface VPC Endpoint** is an endpoint powered by **AWS PrivateLink**.

It places an **Elastic Network Interface (ENI)** with a **private IP address** into your subnet so your VPC can privately reach a supported service.

### Core idea in plain English

If your VPC must privately reach **most AWS services other than the classic S3/DynamoDB gateway case**, think **Interface Endpoint / PrivateLink**.

### What is fixed

* It creates an **ENI** in your subnet.
* It gives private connectivity to supported services.
* It is powered by **AWS PrivateLink**.
* It can be used for many AWS services.
* It can also be used to reach services in other AWS accounts or partner services.
* It usually costs money.
* It can use **private DNS** so standard service names resolve to private IPs.

### What is variable

* Which service it connects to.
* Which subnets and AZs contain the endpoint ENIs.
* Whether private DNS is enabled.
* Which security groups are attached to the endpoint ENIs.

### How it works

1. AWS creates an endpoint network interface in your subnet.
2. Your workload sends traffic to the service using private connectivity.
3. The traffic stays on the AWS network instead of going to the public internet.

### When to choose it

Choose an Interface Endpoint when:

* A private EC2 instance needs Systems Manager access.
* A private workload needs SQS, SNS, CloudWatch, Kinesis, Secrets Manager, or many other AWS services.
* The question asks for private service connectivity without internet or NAT.
* You need private connectivity to a provider service through AWS PrivateLink.

### Real-world examples

**Example 1 – Private EC2 uses Systems Manager**
Your EC2 instances have no internet access, but you still want Session Manager and Systems Manager features.
Use Interface Endpoints for the needed SSM-related services.

**Example 2 – Private app sends messages to SQS**
Your app runs in private subnets and must send messages to SQS without internet exposure.
Use an **Interface Endpoint** for SQS.

### PrivateLink vs full network connectivity

This is very important:

* **PrivateLink** gives private access to a **service**.
* **VPC Peering** gives private connectivity between **entire VPC networks**.

### Exam traps

**Trap 1 – PrivateLink is not VPC Peering.**
If the requirement is “my VPC must reach a service privately,” PrivateLink may be right.
If the requirement is “my VPCs need full network connectivity,” peering or TGW is more likely.

**Trap 2 – It is not free in the normal sense.**
Do not choose Interface Endpoint as the cheapest answer for S3 when Gateway Endpoint fits better.

**Trap 3 – DNS matters.**
If private DNS is enabled, the usual public service DNS name can resolve privately through the endpoint.

---

# 4. VPC to VPC inside AWS

Sometimes the source and destination are both VPCs.

Now the question becomes:

* Is it just **two VPCs**?
* Or is it **many VPCs**?
* Do we need **transitive routing**?
* Do we also need to connect **on-premises networks**?

---

## 4A. VPC Peering

### What it is

A **VPC Peering** connection is a private network connection between **two VPCs**.

### Core idea in plain English

Peering is a **direct private link between exactly two VPCs**.

### What is fixed

* It connects **two VPCs**.
* Traffic uses private IP addresses.
* Traffic stays off the public internet.
* The VPC CIDR ranges must not overlap.
* It is **not transitive**.
* Route tables must be updated so traffic knows how to flow.

### What is variable

* Whether the VPCs are in the same account or different accounts.
* Whether they are in the same Region or different Regions.
* Which route tables are updated.
* Which security controls allow the traffic.

### When to choose it

Choose VPC Peering when:

* You need private communication between **two VPCs**.
* The design is simple and not expected to grow into a large mesh.
* You do not need transitive routing.

### Real-world examples

**Example 1 – App VPC to DB VPC**
An application in one VPC must reach a shared database or service in another VPC.
VPC Peering can be a clean answer.

**Example 2 – Shared services VPC**
A team wants a small number of VPCs to reach shared DNS or identity services privately.

### The most important exam fact

**VPC Peering is not transitive.**

If:

* VPC A is peered with VPC B
* VPC B is peered with VPC C

That does **not** mean VPC A can reach VPC C through VPC B.

### When it stops being a good answer

If many VPCs all need connectivity, peering becomes messy because you must create many individual connections.

### Exam traps

**Trap 1 – Not transitive.**
This is one of the most tested networking facts.

**Trap 2 – Overlapping CIDRs break the design.**
If the CIDR blocks overlap, peering is not the right answer.

**Trap 3 – Peering alone is not enough.**
You still need routing and security configuration.

**Trap 4 – Scalability.**
For large multi-VPC environments, Transit Gateway is usually better.

---

## 4B. AWS Transit Gateway

### What it is

**AWS Transit Gateway (TGW)** is a central network hub that connects multiple VPCs and can also connect on-premises networks.

### Core idea in plain English

Transit Gateway is the **hub**. VPCs and networks are the **spokes**.

### What is fixed

* It is a **central routing hub**.
* It supports **transitive routing**.
* It can connect **multiple VPCs**.
* It can also connect **VPNs** and **Direct Connect architectures**.
* It is a strong answer for scalable multi-VPC networking.
* It is a **regional** service conceptually, though cross-region TGW designs can be built.

### What is variable

* Number of VPC attachments.
* Route table segmentation.
* Which accounts attach through multi-account patterns.
* Whether VPN or Direct Connect is also integrated.

### When to choose it

Choose Transit Gateway when:

* Many VPCs must communicate.
* You want centralized routing.
* You need transitive routing.
* You want to connect AWS VPCs and on-premises networks in one network design.

### Real-world examples

**Example 1 – 50 VPC enterprise design**
A company has many VPCs across accounts and needs centralized connectivity.
Transit Gateway is the scalable answer.

**Example 2 – Hybrid network hub**
The company wants VPCs plus on-premises data centers to communicate through one hub.
Transit Gateway is a natural fit.

### Transit Gateway vs VPC Peering

| Factor                          | VPC Peering           | Transit Gateway                 |
| ------------------------------- | --------------------- | ------------------------------- |
| Best for                        | Small number of VPCs  | Many VPCs                       |
| Routing style                   | Point-to-point        | Hub-and-spoke                   |
| Transitive routing              | No                    | Yes                             |
| On-prem integration             | Not the main strength | Yes                             |
| Operational simplicity at scale | Poorer                | Better                          |
| Cost model                      | Usually simpler       | Additional attachment/data cost |

### Exam traps

**Trap 1 – Do not choose TGW for a tiny design unless the question needs scale or transit.**

**Trap 2 – TGW is not “free routing magic.”**
You still manage attachments and routing logic.

**Trap 3 – TGW often wins when the question says “many VPCs,” “hub-and-spoke,” or “transitive routing.”**

---

# 5. On-premises network to AWS

Now the source is not a VPC. It is an office, branch, or data center.

The key question is:

* Do you want something **quick and encrypted over the internet**?
* Or something **dedicated, private, and more consistent**?

That gives you the classic choice:

* **Site-to-Site VPN**
* **Direct Connect**

---

## 5A. AWS Site-to-Site VPN

### What it is

**AWS Site-to-Site VPN** connects your on-premises network to AWS using encrypted **IPSec tunnels** over the public internet.

### Core idea in plain English

It is the usual answer when a company network needs secure access to AWS **quickly** and **without paying for a dedicated physical connection**.

### What is fixed

* It uses **IPSec encryption**.
* It travels over the **public internet**.
* It includes **two tunnels** for redundancy.
* It connects your on-premises side to AWS.
* On the AWS side, the connection can terminate at a **Virtual Private Gateway** or a **Transit Gateway**.
* It is usually faster to set up than Direct Connect.

### What is variable

* Whether routing is static or dynamic.
* Which AWS-side gateway is used.
* Internet latency and performance.
* Which prefixes and networks are advertised.

### When to choose it

Choose Site-to-Site VPN when:

* The question says **encrypted** and **quick to set up**.
* The path can go over the **public internet**.
* Cost matters more than a dedicated line.
* You need hybrid connectivity soon.

### Real-world examples

**Example 1 – Fast hybrid connectivity**
A company must connect its office network to AWS this week.
Use Site-to-Site VPN.

**Example 2 – Backup to Direct Connect**
A company already uses Direct Connect but wants failover.
Use Site-to-Site VPN as backup.

### Customer Gateway and Virtual Private Gateway

These appear often in exam questions.

* **Customer Gateway** = representation of your on-premises VPN device/router side.
* **Virtual Private Gateway (VGW)** = AWS-side VPN endpoint attached to a VPC.
* **Transit Gateway** can also be the AWS-side VPN target in scalable designs.

Important: these are **components** of the VPN solution.
The top-level service answer is usually still **AWS Site-to-Site VPN**.

### Exam traps

**Trap 1 – Encrypted does not mean dedicated.**
VPN is encrypted, but it still goes across the public internet.

**Trap 2 – Two tunnels are already part of the service.**
That is a common built-in availability point.

**Trap 3 – Fast setup usually points to VPN, not Direct Connect.**

**Trap 4 – If the design must scale to many VPCs, Transit Gateway may appear with the VPN design.**

---

## 5B. AWS Direct Connect

### What it is

**AWS Direct Connect** provides a dedicated private network connection from your on-premises environment to AWS.

### Core idea in plain English

This is the answer when the business wants a **private, dedicated, more consistent network path** to AWS.

### What is fixed

* It is a **dedicated private connection**.
* It does **not** use the public internet for the traffic path.
* It generally provides more consistent performance than internet-based VPN.
* It is usually slower to provision than VPN because physical connectivity is involved.
* It is **not encrypted by default**.
* It is a common answer for large data transfer and stable hybrid networking.

### What is variable

* Connection speed.
* Whether it is dedicated or hosted.
* Which DX location and partner model are used.
* Whether additional encryption is layered on top.

### Modern speed note

Older notes often say Direct Connect supports only 1 Gbps and 10 Gbps. That is outdated. Current AWS options are broader.

For Cloud Practitioner, the key exam idea is not memorizing every speed. The key idea is this:

> Direct Connect is the dedicated, private, more consistent hybrid connectivity option.

### When to choose it

Choose Direct Connect when:

* The question says **dedicated** private connection.
* The company wants **consistent performance**.
* There is significant data transfer.
* Setup time of weeks or longer is acceptable.

### Real-world examples

**Example 1 – Media company moving huge files to AWS**
Large regular transfers make Direct Connect attractive.

**Example 2 – Financial workload needing consistent performance**
A dedicated connection can be preferable to internet variability.

### What it is not

* It is **not automatically encrypted**.
* It is **not usually the fastest to provision**.
* It is **not automatically highly available by itself**.

### Exam traps

**Trap 1 – Private does not mean encrypted.**
Direct Connect is private, but encryption is not automatic by default.

**Trap 2 – Slow setup.**
If the question says “immediately” or “as soon as possible,” VPN is often better.

**Trap 3 – One connection alone is not full redundancy.**
Redundancy requires additional design.

**Trap 4 – If the question requires both dedicated and encrypted, think Direct Connect + VPN.**

---

## 5C. Direct Connect + VPN

### What it is

This combined design means one of two things:

1. **Direct Connect as primary + Site-to-Site VPN as backup**, or
2. **VPN over Direct Connect** to add encryption.

### Core idea in plain English

This is the answer when one service alone is not enough.

### When to choose it

Choose this combined idea when the question asks for:

* **Dedicated + encrypted** connectivity
* **Private line + failover**
* **Consistent hybrid path + backup tunnel**

### Exam trap

Read carefully which need is being tested:

* **Backup/failover**?
* **Encryption**?
* **Both**?

---

# 6. End users to AWS

Now the source is not a whole office network.

It is a **person using a laptop or device**.

That changes the answer.

---

## 6A. AWS Client VPN

### What it is

**AWS Client VPN** is a managed VPN service for **individual users and devices**.

### Core idea in plain English

If an employee at home needs secure access to AWS resources, the answer is usually **Client VPN**, not Site-to-Site VPN.

### What is fixed

* It is for **individual users/devices**.
* It is a **managed** AWS service.
* It uses an **OpenVPN-based client model**.
* It can authenticate users through options such as directory-based and federated methods.
* It can provide access to VPC resources and, in broader hybrid designs, to on-premises resources too.

### What is variable

* Authentication method.
* Number of users.
* Route configuration.
* Split-tunnel behavior.

### When to choose it

Choose Client VPN when:

* Remote employees need access to private AWS resources.
* Laptops or user devices are the source.
* The wording says users, employees, or developers working remotely.

### Real-world examples

**Example 1 – Remote developer**
A developer needs secure access from home to EC2 instances in a private subnet.
Use **AWS Client VPN**.

**Example 2 – Finance users access internal app**
Employees need secure access to a private payroll application running in AWS.
Use **Client VPN**.

### Client VPN vs Site-to-Site VPN

| Service          | Connects      | Best clue words                                             |
| ---------------- | ------------- | ----------------------------------------------------------- |
| Client VPN       | Users/devices | employee, laptop, remote user, work from home               |
| Site-to-Site VPN | Networks      | office, branch, corporate network, data center, on-premises |

### Exam traps

**Trap 1 – User vs network.**
This is the big one.

**Trap 2 – Do not answer Site-to-Site VPN when the problem is individual remote-user access.**

---

# 7. Supporting concepts you must know

These are not always the final answer, but networking questions often break because of them.

---

## 7A. Public subnet vs private subnet

### Public subnet

A subnet is public when its route table sends internet-bound traffic to an **Internet Gateway**.

### Private subnet

A subnet is private when it does **not** have that direct internet route.

### Exam lesson

* Public-facing ALBs and public EC2 instances go in **public subnets**.
* Databases and internal application servers usually go in **private subnets**.

### Trap

A subnet is **not** public just because the VPC has an IGW.

---

## 7B. Route tables

A route table decides where traffic goes.

### Key facts

* Every subnet must be associated with a route table.
* A subnet can be associated with **one** route table at a time.
* A route maps a **destination** to a **target**.

### Common targets

* Internet Gateway
* NAT Gateway
* VPC Peering connection
* Transit Gateway
* Virtual Private Gateway
* Gateway Endpoint

### Exam lesson

After creating a connectivity component, the missing step is often:
**update the route table**.

---

## 7C. Security Groups

Security Groups are **stateful virtual firewalls** attached to resources like EC2 or ENIs.

### Key facts

* They allow traffic with **allow rules**.
* They are **stateful**.
* Response traffic is automatically allowed when the original traffic is allowed.
* New security groups usually allow no inbound traffic by default.

### Exam lesson

If the architecture is correct but the traffic still does not flow, Security Groups may be blocking it.

### Trap

Security Groups are not the answer to “which service connects X to Y?”
They are part of the design, not usually the top-level connectivity service.

---

## 7D. Network ACLs (NACLs)

NACLs are **stateless subnet-level filters**.

### Key facts

* They work at the **subnet level**.
* They support **allow and deny** rules.
* Rules are evaluated by **rule number order**.
* Because they are **stateless**, return traffic must also be allowed explicitly.

### Exam lesson

NACLs are often used in questions that want you to know the difference between stateful and stateless controls.

### Trap

If the question says **stateless** or **deny rule**, think **NACL**, not Security Group.

---

## 7E. Customer Gateway and Virtual Private Gateway

### Customer Gateway

An AWS-side configuration object representing your on-premises VPN device.

### Virtual Private Gateway (VGW)

The AWS-side VPN gateway attached to a VPC.

### Exam lesson

They are important pieces of **Site-to-Site VPN**, but if the question asks which AWS service connects the office to AWS, the answer is usually **Site-to-Site VPN**, not VGW.

---

## 7F. Elastic IP (EIP)

An **Elastic IP** is a static public IPv4 address that you allocate in AWS and attach to a supported resource.

### Key facts

* It gives a stable public IPv4 address.
* It is commonly used with public-facing designs and classic public NAT Gateway patterns.
* Modern AWS billing charges for Elastic IP addresses, so old notes saying “free if in use” are outdated.

### Exam lesson

You often see EIP mentioned with:

* public EC2 instances
* NAT Gateway patterns

---

## 7G. VPC Flow Logs

VPC Flow Logs capture information about IP traffic to and from network interfaces in your VPC.

### Exam lesson

If the question asks how to **monitor**, **audit**, or **troubleshoot VPC traffic**, Flow Logs may be the right answer.

It is not a connectivity service. It is an observability and troubleshooting tool.

---

# 8. Troubleshooting logic for exam questions

When AWS gives you a long architecture question, do not panic.

Use this sequence.

## Step 1 – Identify source and destination

Ask:

* Source = EC2? VPC? on-premises network? employee laptop?
* Destination = internet? S3? another VPC? AWS service? office network?

## Step 2 – Identify access style

Ask:

* Public or private?
* Inbound, outbound, or both?
* Encrypted or not?
* Dedicated or internet-based?
* One connection or many networks?

## Step 3 – Pick the top-level service first

Examples:

* Public internet for VPC resource -> **IGW**
* Private subnet outbound internet -> **NAT Gateway**
* Private S3 access -> **Gateway Endpoint**
* Many VPCs -> **Transit Gateway**
* Office network to AWS fast -> **Site-to-Site VPN**
* Remote employees -> **Client VPN**

## Step 4 – Then check the supporting pieces

After picking the top-level answer, ask whether the architecture also needs:

* correct route tables
* public IP or EIP
* security groups
* NACL rules
* DNS/private DNS
* non-overlapping CIDRs

This is where many exam questions hide the real issue.

---

# 9. Fast exam mapping cheat sheet

## If the question says this, think this

| Question wording                                                   | First service to think of            |
| ------------------------------------------------------------------ | ------------------------------------ |
| public internet access for VPC resources                           | Internet Gateway                     |
| private subnet needs outbound internet                             | NAT Gateway                          |
| outbound-only IPv6 internet access                                 | Egress-only Internet Gateway         |
| private access to S3 without internet                              | Gateway VPC Endpoint                 |
| private access to DynamoDB without internet                        | Gateway VPC Endpoint                 |
| private access to SQS, SNS, SSM, Secrets Manager, CloudWatch, etc. | Interface VPC Endpoint / PrivateLink |
| connect two VPCs privately                                         | VPC Peering                          |
| connect many VPCs centrally                                        | Transit Gateway                      |
| transitive routing between VPCs                                    | Transit Gateway                      |
| connect office/data center to AWS quickly and securely             | Site-to-Site VPN                     |
| dedicated private line to AWS                                      | Direct Connect                       |
| dedicated and encrypted hybrid connection                          | Direct Connect + VPN                 |
| remote employees need access                                       | Client VPN                           |

## Elimination logic

When unsure, ask:

1. Is the destination the **internet**?
2. Is the destination **another VPC**?
3. Is the destination an **AWS service**?
4. Is the source an **on-premises network**?
5. Is the source an **individual user**?

That usually gets you to the right family of answers.

---

# 10. Every exam trap catalogued

## Trap category 1 – Similar services are not the same

### Client VPN vs Site-to-Site VPN

* **Client VPN** = users/devices
* **Site-to-Site VPN** = networks

### Internet Gateway vs NAT Gateway

* **IGW** = internet connectivity for public resources
* **NAT Gateway** = outbound internet for private resources

### VPC Peering vs Transit Gateway vs PrivateLink

* **Peering** = direct network connection between two VPCs
* **Transit Gateway** = hub for many VPCs and hybrid networks
* **PrivateLink** = private access to a service, not full network connectivity

### VPN vs Direct Connect

* **VPN** = encrypted, internet-based, faster to set up
* **Direct Connect** = dedicated private path, not encrypted by default, slower to provision

### Gateway Endpoint vs Interface Endpoint

* **Gateway Endpoint** = classic route-table-based private access for S3 and DynamoDB
* **Interface Endpoint** = ENI-based PrivateLink endpoint for many services

---

## Trap category 2 – The service alone is not enough

### IGW alone is not enough

You still need:

* route table to IGW
* public IP for IPv4 internet reachability
* security configuration

### NAT Gateway alone is not enough

You still need correct route tables and the broader internet path.

### Peering alone is not enough

You still need route tables and compatible CIDRs.

### Direct Connect alone is not enough for encryption

If encryption is required, add VPN or another encryption approach.

### Direct Connect alone is not enough for redundancy

A stronger HA design needs more than one path.

---

## Trap category 3 – Transitivity

This is huge.

**VPC Peering is not transitive.**

If the question is really about routing through an intermediary VPC, peering is usually wrong.

---

## Trap category 4 – Supporting components are not the top-level answer

If the question asks:

> “Which AWS service connects the office to AWS?”

The answer is usually:

* **Site-to-Site VPN**

Not:

* Virtual Private Gateway
* Customer Gateway
* Route Table
* Subnet

Those are parts of the solution.

---

## Trap category 5 – Cost assumptions

| Service                | General cost attitude                                       |
| ---------------------- | ----------------------------------------------------------- |
| Internet Gateway       | no separate hourly IGW charge                               |
| NAT Gateway            | paid                                                        |
| Gateway VPC Endpoint   | usually best low-cost answer for private S3/DynamoDB access |
| Interface VPC Endpoint | paid                                                        |
| VPC Peering            | data transfer considerations apply                          |
| Transit Gateway        | paid                                                        |
| Site-to-Site VPN       | paid                                                        |
| Direct Connect         | paid                                                        |
| Client VPN             | paid                                                        |

### High-value exam insight

If the question says:

* **most cost-effective**
* **private access to S3**
* **private subnet**

Then **Gateway VPC Endpoint** should jump into your mind immediately.

---

## Trap category 6 – Setup time

### Usually faster to set up

* Site-to-Site VPN
* Client VPN
* NAT Gateway
* VPC Peering
* IGW

### Usually slower to provision

* Direct Connect

If the question says **immediately**, **quickly**, or **within days**, that strongly points away from Direct Connect.

---

## Trap category 7 – IPv4 vs IPv6 wording

Classic exam memory:

* **NAT Gateway** = common answer for private subnet outbound internet access
* **Egress-only IGW** = common answer for outbound-only IPv6 internet access
* **IGW** = public internet connectivity

Do not mix them up.

---

# 11. Memory anchors and mnemonics

## The “Who is talking to whom?” framework

Every networking question becomes easier if you ask:

1. Who is the source?
2. Who is the destination?
3. Is it public, private, encrypted, or dedicated?
4. Is it one-to-one, or one-to-many?

---

## Mnemonics

### NAT Gateway = one-way door

Private resources go **out**. The internet does not start direct connections **in** through that path.

### VPC Peering = handshake

A handshake is direct between two people. It does not automatically let you reach a third person.

### Transit Gateway = airport hub

Many routes come into one central hub and leave again.

### Direct Connect = private highway

Dedicated, stable, private, but takes more effort to set up.

### VPN = secure tunnel over shared roads

Encrypted, quick, practical, but still using internet-based paths.

### Gateway Endpoint = S3 and DynamoDB special lane

When the destination is S3 or DynamoDB privately, think about the special low-cost route.

### PrivateLink = private link to a service

It connects privately to a **service**, not to an entire remote network.

### Client VPN = people

If the user is a human on a laptop, think **Client VPN**.

### Site-to-Site VPN = buildings

If the source is an office or data center network, think **Site-to-Site VPN**.

---

# 12. One-line summary per service

| Service                              | One-line purpose                                                                                     |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Internet Gateway                     | Enables internet connectivity for public VPC resources                                               |
| NAT Gateway                          | Enables private resources to initiate outbound connectivity without direct inbound internet exposure |
| Egress-only Internet Gateway         | Enables outbound-only IPv6 internet access                                                           |
| Gateway VPC Endpoint                 | Provides classic private route-table-based access to S3 or DynamoDB                                  |
| Interface VPC Endpoint / PrivateLink | Provides private ENI-based access to supported AWS or partner services                               |
| VPC Peering                          | Direct private network connection between two VPCs                                                   |
| Transit Gateway                      | Central hub for connecting many VPCs and hybrid networks                                             |
| Site-to-Site VPN                     | Encrypted IPSec tunnel between on-premises network and AWS over the internet                         |
| Direct Connect                       | Dedicated private connection from on-premises network to AWS                                         |
| Direct Connect + VPN                 | Adds encryption and/or backup to Direct Connect                                                      |
| Client VPN                           | Managed VPN for individual remote users and devices                                                  |

---

# Final study advice

Do not study AWS networking as a random list of services.

Study it as a set of **connection patterns**:

* VPC to internet
* Private VPC to AWS services
* VPC to VPC
* On-premises to AWS
* Users to AWS

If you can identify the pattern first, the correct service becomes much easier to choose.

And for Cloud Practitioner, never forget the highest-value shortlist:

1. Internet Gateway
2. NAT Gateway
3. Gateway VPC Endpoint
4. Interface VPC Endpoint / PrivateLink
5. VPC Peering
6. Transit Gateway
7. Site-to-Site VPN
8. Direct Connect
9. Client VPN

If you master those and the traps around them, you will be in very strong shape for the exam.
