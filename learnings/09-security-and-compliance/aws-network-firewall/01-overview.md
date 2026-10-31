# AWS Network Firewall

## Simple definition

AWS Network Firewall is a managed network security service that helps you inspect, allow, or block traffic going in and out of your Amazon VPC.

In simple words, it is like a security checkpoint for network traffic inside your AWS environment.

---

## Core idea in plain English

Think of AWS Network Firewall like a smart security gate placed in the traffic path of your VPC.

It checks network traffic and decides

 allow it
 drop it
 alert on it

It can inspect traffic using

 stateless rules for simple packet filtering
 stateful rules for deeper inspection of connections and traffic flows

This makes it useful when you want stronger network-level protection than basic VPC controls alone.

---

## Main use cases

AWS Network Firewall is commonly used to

 protect VPCs from unwanted inbound and outbound traffic
 control internet-bound traffic from private subnets
 block traffic to known malicious destinations
 filter traffic between networks connected by VPN or Direct Connect
 inspect traffic in centralized security architectures
 enforce company security rules across workloads
 add intrusion detection and intrusion prevention at the VPC level

---

## Key features

 Fully managed service
 Stateful firewall for connection-aware inspection
 Stateless firewall for simple high-speed filtering
 Intrusion detection and prevention capabilities
 Domain and IP filtering
 Suricata-compatible rule support for advanced stateful inspection
 Traffic logging for monitoring and analysis
 High availability across Availability Zones
 Scales automatically with traffic
 Can inspect traffic related to

   internet gateway
   NAT gateway
   VPN
   Direct Connect
   Transit Gateway architectures

---

## How it works

### 1. You create the firewall

You deploy AWS Network Firewall inside a VPC.

### 2. You choose firewall subnets

You place firewall endpoints in dedicated subnets, usually across multiple Availability Zones for high availability.

### 3. You create rules and policies

You define what traffic should be allowed, blocked, or logged.

These rules can be

 stateless
 stateful
 domain list based
 advanced inspection rules

### 4. You update route tables

This is a very important exam point.

Traffic is not inspected automatically just because the firewall exists.

You must route traffic through the firewall endpoints using VPC route tables.

### 5. The firewall inspects traffic

When traffic passes through the firewall path, AWS Network Firewall checks it against the policy and takes the configured action.

---

## Why it is important for the exam

AWS exams like to test whether you understand

 the difference between network-level protection and application-level protection
 that AWS Network Firewall protects VPC traffic
 that it works using firewall endpoints and route tables
 that it provides stateful inspection
 that it is different from security groups, network ACLs, and AWS WAF

For the Cloud Practitioner exam, you usually do not need deep configuration details.

But you do need to know when to choose it in a scenario question.

---

## Related AWS services and differences

### AWS Network Firewall vs Security Groups

Security Groups

 work at the instance or ENI level
 are stateful
 allow rules only, not explicit deny rules
 protect specific resources

AWS Network Firewall

 works at the VPC traffic path level
 can inspect broader network traffic flows
 can allow, drop, or alert
 is used for centralized network traffic inspection

### AWS Network Firewall vs Network ACLs

Network ACLs

 work at the subnet level
 are stateless
 support allow and deny rules
 are more basic filtering tools

AWS Network Firewall

 provides deeper inspection
 supports stateful inspection
 is more advanced and more flexible for security policy enforcement

### AWS Network Firewall vs AWS WAF

AWS WAF

 protects web applications
 works at Layer 7
 filters HTTPHTTPS requests
 is used with CloudFront, Application Load Balancer, API Gateway, and similar services

AWS Network Firewall

 protects network traffic in a VPC
 works more at the networkperimeter traffic level
 is not mainly for web request filtering

### AWS Network Firewall vs AWS Shield

AWS Shield

 protects against DDoS attacks
 focuses on availability during attacks

AWS Network Firewall

 filters and inspects traffic based on rules and policies
 is not the same as DDoS protection

### AWS Network Firewall vs AWS Firewall Manager

AWS Firewall Manager

 helps centrally manage firewall and security rules across accounts and resources

AWS Network Firewall

 is the actual firewall service doing traffic inspection

### AWS Network Firewall vs Gateway Load Balancer

Gateway Load Balancer

 helps deploy and scale third-party virtual network appliances

AWS Network Firewall

 is an AWS-managed firewall service
 you do not manage your own firewall appliance fleet

---

## Common exam traps

### Trap 1 Confusing it with AWS WAF

If the question is about web requests, SQL injection, or HTTPHTTPS filtering, the answer is often AWS WAF, not AWS Network Firewall.

### Trap 2 Confusing it with Security Groups

If the question is about controlling access to one EC2 instance, one database, or one ENI, the answer may be Security Groups, not AWS Network Firewall.

### Trap 3 Forgetting route tables

A very common point

AWS Network Firewall only inspects traffic that is routed through it.

### Trap 4 Confusing subnet-level filtering with advanced inspection

If the question only needs a basic subnet allowdeny list, Network ACLs may be enough.

If the question asks for managed, scalable, advanced inspection, then AWS Network Firewall is stronger.

### Trap 5 Thinking it is only for inbound traffic

It can also inspect outbound traffic and traffic going through architectures such as VPN or Direct Connect.

### Trap 6 Thinking it automatically protects every VPC resource

It does not magically protect everything by default.
You must design routing and policies correctly.

---

## Easy real-world example

A company has private application servers in a VPC.

These servers access the internet through a NAT gateway to download updates.
The company wants to

 block access to known malicious destinations
 inspect outbound traffic
 log suspicious connections

They deploy AWS Network Firewall in dedicated firewall subnets, create filtering rules, and route the traffic through the firewall endpoints.

Now all outbound traffic is inspected before reaching the internet.

---

## Final summary

AWS Network Firewall is a managed, scalable, VPC-level network firewall service.

It helps inspect, allow, block, and log traffic flowing through your VPC environment.

It is stronger than basic security groups or network ACLs when you need centralized, advanced network inspection.

For the exam, remember this idea

Security Groups protect resources.
NACLs protect subnets.
AWS WAF protects web apps.
AWS Network Firewall protects VPC network traffic paths.

---

## Short exam answer

AWS Network Firewall is a managed stateful network firewall and intrusion detectionprevention service for Amazon VPC that inspects and filters inbound and outbound network traffic using firewall rules, policies, and VPC routing.

---

## Memory trick

Think

Network Firewall = network traffic police for the whole VPC path

 Security Group = bodyguard for one resource
 NACL = gate at the subnet door
 WAF = web app shield
 Network Firewall = highway checkpoint for VPC traffic

---

## If I were an examiner ...

If I were an examiner, I would ask questions like these

### 1. Which AWS service provides managed network traffic inspection inside a VPC

Expected answer AWS Network Firewall

### 2. What must be configured so that AWS Network Firewall can inspect traffic

Expected answer VPC route tables must route traffic through the firewall endpoints

### 3. What is the difference between AWS Network Firewall and AWS WAF

Expected answer Network Firewall protects VPC network traffic, while AWS WAF protects web applications and HTTPHTTPS requests

### 4. What is the difference between AWS Network Firewall and Security Groups

Expected answer Security Groups protect individual resources or ENIs, while AWS Network Firewall inspects traffic at the VPC traffic-path level

### 5. In a scenario asking for advanced managed inspection of inbound and outbound VPC traffic, which service fits best

Expected answer AWS Network Firewall

### 6. Is AWS Network Firewall stateful or stateless

Expected answer It supports both stateless and stateful rule processing

### 7. When would you choose Network ACLs instead of AWS Network Firewall

Expected answer When simple subnet-level stateless allowdeny control is enough

---

## Small exam coach note

When you see keywords like these, think about AWS Network Firewall

 inspect VPC traffic
 managed network firewall
 inbound and outbound filtering
 intrusion prevention
 route traffic through firewall
 centralized traffic inspection
 advanced network security in a VPC

When you see HTTP requests, web attacks, SQL injection, or cross-site scripting, think first about AWS WAF, not AWS Network Firewall.
