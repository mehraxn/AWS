# AWS Global Accelerator Static IPs

## Simple definition

AWS Global Accelerator is a networking service that gives your application static IP addresses and routes users to the best healthy AWS endpoint using the AWS global network.

---

## Core idea in plain English

Think of AWS Global Accelerator as a fixed front door for a global application.

Normally, IP addresses can change, DNS failover can take time, and users far away may not get the best path.

With Global Accelerator, your application gets static anycast IP addresses that do not change while the accelerator exists. Users connect to those IPs, and AWS sends the traffic through its global network to the closest healthy regional endpoint.

So the big idea is

One fixed set of IPs + smarter global traffic routing + fast failover.

---

## Main use cases

### 1. Need fixed public IP addresses for a global app

Some clients, partners, or firewalls require allowlisting static IPs. Global Accelerator gives you static entry points.

### 2. Multi-Region application availability

If you run your application in more than one AWS Region, Global Accelerator can route traffic to healthy endpoints and help with failover.

### 3. Better performance for global users

Traffic enters the AWS network closer to the user and travels on the AWS backbone instead of staying longer on the public internet.

### 4. Disaster recovery setup

If one Region becomes unhealthy, Global Accelerator can quickly direct users to another healthy Region.

### 5. Gaming, APIs, and real-time apps

Applications that need low latency and fast failover often use Global Accelerator.

---

## Key features

 Static IP addresses for your application
 Anycast IPs announced from AWS edge locations
 Traffic routing to optimal healthy endpoints
 Works across one or multiple AWS Regions
 Health checks and automatic failover
 Improved global performance
 Supports Application Load Balancers, Network Load Balancers, EC2 instances, and Elastic IP-based endpoints
 Good for TCP and UDP traffic

---

## How it works

### Step 1 Create an accelerator

When you create a standard accelerator, AWS gives you static IP addresses.

### Step 2 Add listeners

Listeners define which ports or protocols the accelerator should accept, such as HTTP, HTTPS, or other TCPUDP traffic.

### Step 3 Add endpoint groups

You choose one or more AWS Regions.

### Step 4 Add endpoints

Inside those Regions, you attach resources such as

 Application Load Balancer
 Network Load Balancer
 EC2 instance
 Elastic IP address

### Step 5 Users connect to the static IPs

Clients always use the same Global Accelerator IP addresses.

### Step 6 AWS sends traffic to the best healthy endpoint

AWS uses the global edge network and routing logic to direct traffic to healthy application endpoints.

If one endpoint or Region fails, traffic can be moved to another healthy location.

---

## Why it is important for the exam

This topic matters because AWS exam questions often test whether you know when static IPs are needed.

A very common exam pattern is

 The company needs fixed IP addresses for clients to allowlist
 The application is global or multi-Region
 The company wants high availability and better performance

In this case, the answer is often AWS Global Accelerator.

It is also important because students often confuse it with Route 53 and CloudFront.

---

## Related AWS services and differences

### AWS Global Accelerator vs Amazon Route 53

Global Accelerator

 Gives static IP addresses
 Routes traffic at the network layer
 Improves performance by using the AWS global network
 Failover is usually faster because clients keep using the same IPs

Route 53

 Is a DNS service
 Routes users by returning DNS answers
 Does not give your app static anycast IPs
 DNS changes may depend on caching and TTL behavior

Easy rule
Use Route 53 for DNS routing. Use Global Accelerator when you need fixed IPs and fast global traffic routing.

### AWS Global Accelerator vs Amazon CloudFront

Global Accelerator

 Improves performance for dynamic, non-cacheable, or TCPUDP applications
 Does not mainly focus on caching content
 Gives static IP addresses

CloudFront

 Is a content delivery network (CDN)
 Best for caching static or cacheable content close to users
 Uses edge locations to deliver content faster
 Main idea is content caching, not static IP entry points

Easy rule
Use CloudFront for caching content. Use Global Accelerator for global application entry with static IPs and smart routing.

### AWS Global Accelerator vs Elastic Load Balancing

Elastic Load Balancing distributes traffic to targets, usually within a Region.

Global Accelerator sits in front of regional endpoints and provides global static IP entry points.

So ELB handles localregional load distribution, while Global Accelerator helps with global access and routing.

---

## Common exam traps

### Trap 1 Confusing Route 53 with Global Accelerator

If the question says DNS routing, domain names, hosted zones, or routing policies, think Route 53.

If the question says static IPs, fast failover, or improving global app performance, think Global Accelerator.

### Trap 2 Choosing CloudFront when the app is not about caching

If the need is cache website content, choose CloudFront.

If the need is static IPs for a global application, choose Global Accelerator.

### Trap 3 Forgetting the words “allowlist” or “whitelist”

If customers or partners must allow specific fixed IPs through firewalls, that is a strong clue for Global Accelerator.

### Trap 4 Thinking the load balancer alone solves the problem

An ALB or NLB helps distribute traffic, but the exam may want the service that provides global static IP addresses in front of those endpoints.

That service is AWS Global Accelerator.

---

## Easy real-world example

A company has an online trading app used by customers in Europe, Asia, and the US.

The app runs behind load balancers in two AWS Regions. Big enterprise customers want to allow only a small set of public IP addresses through their firewalls.

The company uses AWS Global Accelerator.

Now customers connect using the same static IP addresses, AWS routes traffic across its global network, and if one Region has a problem, traffic can move to the other healthy Region.

---

## Final summary

AWS Global Accelerator is the AWS service you use when you want

 static public IP addresses
 better global application performance
 automatic failover to healthy endpoints
 multi-Region traffic routing

It is especially useful for applications that need a fixed global entry point.

For the exam, remember this

Global Accelerator is about static IPs, global routing, and fast failover.

---

## Short exam answer

AWS Global Accelerator provides static anycast IP addresses and routes user traffic to the closest healthy application endpoint over the AWS global network, improving availability and performance.

---

## Memory trick

Global Accelerator = Global app + Accelerator lane + fixed address

Think

 Global = works across Regions
 Accelerator = faster path for users
 Static IPs = fixed front door

A simple memory line

“If the app needs one fixed global front door, use Global Accelerator.”
