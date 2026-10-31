# AWS NAT Gateway

## Simple definition

A NAT Gateway is an AWS managed network service that lets resources in a private subnet send traffic out to the internet or to other networks, while preventing the internet from initiating unsolicited inbound connections to those resources.

---

## Core idea in plain English

Think of a NAT Gateway as a one-way door for outbound traffic.

Your private EC2 instances can go out to download updates, call APIs, or reach external services. But outside systems cannot directly start a new connection back to those private instances.

That is why a NAT Gateway is commonly used when servers must stay private but still need outbound access.

---

## Main use cases

### 1. Private EC2 instances downloading software updates

Private EC2 instances often need access to operating system patches, package repositories, or security updates. A NAT Gateway allows them to reach those external update sources without assigning public IP addresses to the instances.

### 2. App servers in private subnets calling external APIs

Application servers may need to connect to third-party services such as payment gateways, mapping APIs, email providers, or identity providers. A NAT Gateway allows those outbound calls while keeping the application servers private.

### 3. Private workloads pulling packages from the internet

Servers in private subnets may need to download application dependencies, libraries, containers, or installation files. A NAT Gateway makes this possible without exposing the workload directly to the internet.

### 4. Sending outbound traffic while keeping instances without public IPs

A common AWS design is to keep backend servers in private subnets with no public IP addresses. A NAT Gateway gives them outbound connectivity while preserving that private design.

### 5. Replacing a NAT instance with a simpler managed option

Older architectures sometimes used a NAT instance, which is an EC2 instance configured for NAT. A NAT Gateway is usually preferred because AWS manages it and it generally provides easier scaling and less administration.

---

## Key features

### 1. Managed by AWS

AWS operates and manages the NAT Gateway for you. You do not need to maintain an operating system, patch the service, or manage the underlying instance.

### 2. Used mainly for outbound traffic from private subnets

Its main purpose is to let resources in private subnets start outbound connections to the internet or other external destinations.

### 3. Prevents unsolicited inbound internet connections

A NAT Gateway does not allow the internet to initiate new inbound connections to your private instances. It supports return traffic only for connections that started from inside.

### 4. Common internet-access design uses a public NAT Gateway

In the classic exam setup, the NAT Gateway is created in a public subnet so that it can reach the internet through an Internet Gateway.

### 5. A public NAT Gateway uses an Elastic IP

When used for internet access, a public NAT Gateway is associated with an Elastic IP address. This gives it a public-facing address for outbound communication.

### 6. Scales better and needs less administration than a NAT instance

A NAT Gateway is usually the better exam answer when compared with a NAT instance because it is managed by AWS and reduces operational work.

### 7. Works with route tables

A NAT Gateway does nothing by itself unless the private subnet route table sends the desired outbound traffic to it. Routing is a key part of the design.

---

## How it works

### Classic exam setup

1. You create a NAT Gateway in a public subnet.
2. That public subnet has a route to an Internet Gateway.
3. Your private subnet route table sends internet-bound traffic (`0.0.0.0/0`) to the NAT Gateway.
4. Private instances send outbound traffic through the NAT Gateway.
5. Response traffic returns through the NAT Gateway.
6. Outside systems still cannot directly initiate a connection to those private instances.

### Easy picture in words

* Public subnet contains the NAT Gateway.
* Private subnet contains your EC2 app servers.
* Internet Gateway gives internet access to the NAT Gateway.
* Route table tells private subnet traffic to go to the NAT Gateway.

---

## Why it is important for the exam

NAT Gateway is one of the most common AWS networking exam topics.

AWS exam questions often test whether you understand this rule:

**Private subnet resources need outbound internet access but should not be publicly reachable — use a NAT Gateway.**

This is a very common decision point in Cloud Practitioner questions.

---

## Related AWS services and differences

### NAT Gateway vs Internet Gateway

* **Internet Gateway:** allows resources with public IPs in a public subnet to communicate with the internet.
* **NAT Gateway:** is used for resources in a private subnet that need outbound internet access without becoming publicly reachable.

### NAT Gateway vs NAT Instance

* **NAT Gateway:** managed by AWS.
* **NAT Instance:** an EC2 instance that you configure and manage yourself.
* In exam questions, NAT Gateway is usually the better answer because it is simpler, more scalable, and requires less maintenance.

### NAT Gateway vs Egress-Only Internet Gateway

* **NAT Gateway:** mainly used for **IPv4** outbound access.
* **Egress-only Internet Gateway:** used for **IPv6** outbound-only internet access.

### NAT Gateway vs VPC Endpoint

* **NAT Gateway:** used for general outbound access to the internet or external networks.
* **VPC Endpoint:** lets you privately connect to supported AWS services without going through the public internet.
* If the question is specifically about private access to services like **Amazon S3** or **DynamoDB**, a **VPC Endpoint** may be the better answer.

### Public NAT Gateway vs Private NAT Gateway

* **Public NAT Gateway:** used for internet access and has an Elastic IP.
* **Private NAT Gateway:** used for private connectivity to other VPCs or on-premises networks, not for direct internet access.

---

## Common exam traps

### 1. Thinking a NAT Gateway allows inbound connections

This is wrong. A NAT Gateway is mainly for outbound connections started by resources inside the private subnet. It does not make private instances publicly reachable from the internet.

### 2. Putting the NAT Gateway in a private subnet

This is wrong for the classic internet-access architecture. For the normal exam design, the NAT Gateway should be placed in a **public subnet** so it can use the Internet Gateway.

### 3. Forgetting the Internet Gateway

A NAT Gateway alone is not enough for internet access. In the classic public NAT design, the VPC must also have an **Internet Gateway** attached.

### 4. Confusing NAT Gateway with a Bastion Host

A Bastion Host is used for administrative access such as **SSH** or **RDP** into private instances. A NAT Gateway is not for admin login access; it is for outbound network traffic.

### 5. Using NAT Gateway when the question is really about private AWS service access

If the goal is private connectivity to AWS services such as **S3** or **DynamoDB**, the correct answer may be a **VPC Endpoint**, not a NAT Gateway.

### 6. Missing the route table requirement

Even if a NAT Gateway exists, it will not be used unless the private subnet route table points the outbound traffic to it.

### 7. Confusing NAT Gateway with public subnet internet access

If an EC2 instance already has a public IP and is in a public subnet, it typically uses the **Internet Gateway** directly. NAT Gateway is mainly for **private subnet** resources.

---

## Easy real-world example

A company has application servers in a private subnet.

The servers must download operating system updates and call a third-party payment API, but the company does not want those servers exposed directly to the internet.

### Solution

1. Put the EC2 instances in a private subnet.
2. Create a NAT Gateway in a public subnet.
3. Add a route in the private subnet route table to send internet traffic to the NAT Gateway.

Now the servers can reach the internet for outbound requests, but no one on the internet can directly start a connection to them.

---

## AWS exam keywords for NAT Gateway

These are common words and phrases that may signal **NAT Gateway** in AWS exam questions:

* private subnet
* outbound internet access
* internet access for private instances
* no public IP
* keep servers private
* download updates
* software patches
* external API calls
* outbound-only access
* prevent inbound connections
* managed NAT
* Elastic IP
* public subnet NAT
* route table to NAT Gateway
* `0.0.0.0/0` route
* Internet Gateway required
* NAT instance replacement
* backend servers in private subnet
* IPv4 outbound access
* private resources need internet

### Typical exam clue sentence

**Resources in a private subnet need to access the internet, but they must not be directly reachable from the internet.**

This is one of the strongest clues that the answer may be **NAT Gateway**.

---

## Final summary

A NAT Gateway is an AWS managed service used mainly to give private subnet resources outbound internet access.

It is the standard answer when workloads must stay private but still need to reach the internet.

Remember the classic pattern:

1. NAT Gateway in a public subnet
2. Private subnet route table points to the NAT Gateway
3. Internet Gateway attached to the VPC

This is one of the most important VPC ideas for the AWS Cloud Practitioner exam.

---

## Short exam answer

A NAT Gateway lets instances in a private subnet access the internet outbound, without allowing unsolicited inbound internet connections.

---

## Memory trick

**NAT = Not Available To the internet from outside**

Or even simpler:

**Private servers go OUT through NAT. The internet cannot come IN through NAT.**
