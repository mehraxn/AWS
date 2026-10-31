# Customer Gateway (CGW)

## Simple definition

A **Customer Gateway (CGW)** is an AWS resource that represents **your side** of a **Site-to-Site VPN** connection.

It tells AWS about your on-premises VPN device, such as its **public IP address**, **routing type**, and **BGP settings** if dynamic routing is used.

---

## Core idea in plain English

Think of a Customer Gateway as the **AWS record of your company’s router or firewall**.

Your real router or firewall stays in your office, branch, or data center. In AWS, you create a **Customer Gateway resource** so AWS knows how to connect to that device.

So the big exam idea is:

* **Customer gateway device** = the real physical or software VPN device on your side
* **Customer Gateway (CGW)** = the AWS resource that represents that device inside AWS

This difference is very important in the exam.

---

## Main use cases

### 1. Connecting an office network to a VPC

A company may want its office users to access private AWS resources without exposing them to the public internet. A Customer Gateway helps set up the customer side of that secure connection.

### 2. Connecting a data center to AWS

Many companies keep some systems on premises and some in AWS. A Customer Gateway is used when building a Site-to-Site VPN between the corporate data center and AWS.

### 3. Building a hybrid cloud environment

A business may run databases, legacy apps, or internal tools on premises while also using AWS services. The Customer Gateway is part of the hybrid networking setup that links both environments.

### 4. Extending private corporate networking into AWS

A company may want EC2 instances in a VPC to behave like another part of the internal company network. A Customer Gateway helps make that secure network extension possible.

### 5. Creating backup or secondary connectivity

Some organizations use VPN as a backup to AWS Direct Connect. In that design, the Customer Gateway is still needed on the customer side for the VPN connection.

---

## Key features

### 1. Used with AWS Site-to-Site VPN

The Customer Gateway is a core component of a Site-to-Site VPN setup. It is not a standalone connectivity service by itself.

### 2. Represents the customer side of the VPN

It identifies **your side** of the connection inside AWS. AWS uses it to know where and how to establish the VPN tunnels.

### 3. Works with a real customer gateway device

The actual router, firewall, or software VPN appliance is located on premises. The CGW in AWS represents that real device.

### 4. Supports static routing or dynamic routing

You can configure the VPN using **static routes** or **BGP** for dynamic routing, depending on your network design.

### 5. Requires a public IP address for the VPN endpoint

AWS needs the public IP address of your on-premises VPN device so the VPN tunnels can be established over the internet.

### 6. Works with an AWS-side gateway

The Customer Gateway is used together with an AWS-side component such as a **Virtual Private Gateway (VGW)** or **Transit Gateway (TGW)**.

### 7. Helps create secure IPsec VPN tunnels

The Customer Gateway is part of the setup that allows encrypted communication between your on-premises network and AWS.

---

## How it works

Here is the simple flow:

1. You have a router or firewall in your office or data center.
2. In AWS, you create a **Customer Gateway** resource that points to that device.
3. On the AWS side, you create a **Virtual Private Gateway** or use a **Transit Gateway**.
4. Then you create a **Site-to-Site VPN** connection between AWS and your network.
5. AWS provides the VPN tunnel configuration details.
6. Your network administrator configures the real router or firewall.
7. Traffic can now move securely between your on-premises network and your VPC.

In simple words:

* **Customer Gateway = your side**
* **VGW or TGW = AWS side**
* **Site-to-Site VPN = the secure connection between both sides**

---

## Why it is important for the exam

This topic matters because AWS exam questions often test whether you understand **hybrid connectivity**.

You should know these points very clearly:

* A Customer Gateway is used in **Site-to-Site VPN** scenarios
* It is **not** the same thing as AWS Direct Connect
* It represents the **customer side**, not the AWS side
* It is an **AWS resource**, not the actual router or firewall

A common exam trick is to mix up the terms **Customer Gateway**, **Customer Gateway Device**, **Virtual Private Gateway**, and **Site-to-Site VPN**.

---

## Related AWS services and differences

### Customer Gateway vs Customer Gateway Device

* **Customer Gateway** = AWS resource
* **Customer Gateway Device** = your real router, firewall, or software VPN appliance

This is one of the most important distinctions for the exam.

### Customer Gateway vs Virtual Private Gateway (VGW)

* **Customer Gateway** = customer side of the VPN
* **Virtual Private Gateway** = AWS side of the VPN attached to one VPC

### Customer Gateway vs Transit Gateway (TGW)

* **Customer Gateway** = represents the customer-side VPN endpoint in AWS
* **Transit Gateway** = AWS network hub that can connect multiple VPCs and on-premises networks

### Customer Gateway vs Site-to-Site VPN

* **Customer Gateway** = one component in the design
* **Site-to-Site VPN** = the full encrypted connection using VPN tunnels

### Customer Gateway vs AWS Direct Connect

* **Customer Gateway** is used with VPN-based connectivity over the internet
* **Direct Connect** is a dedicated private network connection, not a VPN over the public internet

Sometimes companies use **Direct Connect + VPN** together for backup or extra security.

### Customer Gateway vs Client VPN

* **Customer Gateway + Site-to-Site VPN** = connects entire networks to AWS
* **Client VPN** = connects individual users or devices to AWS

---

## Common exam traps

### 1. Thinking the Customer Gateway is the VPN tunnel itself

This is incorrect. The **VPN connection** is the overall secure link. The **Customer Gateway** is only one component of that setup.

### 2. Thinking the Customer Gateway is on the AWS side

This is incorrect. The Customer Gateway represents the **customer side**. The AWS side is usually a **VGW** or **TGW**.

### 3. Confusing Customer Gateway with Customer Gateway Device

This is a very common exam trap. The **device** is the real router or firewall. The **Customer Gateway** is the AWS resource that represents it.

### 4. Confusing Customer Gateway with Virtual Private Gateway

These are not the same. The **CGW** is the customer side. The **VGW** is the AWS side.

### 5. Thinking Customer Gateway is for remote users

This is incorrect. A Customer Gateway is for **network-to-network VPN**. For individual users connecting remotely, AWS uses **Client VPN**.

### 6. Thinking Customer Gateway is the same as Direct Connect

This is incorrect. Direct Connect is a **dedicated private line**. Customer Gateway is part of a **VPN-based connection**.

### 7. Thinking Site-to-Site VPN works without both sides being defined

You need both the **customer side** and the **AWS side**. The Customer Gateway alone is not enough.

**Exam shortcut:**

* **Customer side = Customer Gateway**
* **AWS side = VGW or TGW**
* **Connection = Site-to-Site VPN**

---

## AWS exam keywords you should recognize

These are important words and phrases that may appear in AWS exam questions about Customer Gateway:

* **Customer Gateway (CGW)**
* **Customer gateway device**
* **Site-to-Site VPN**
* **Virtual Private Gateway (VGW)**
* **Transit Gateway (TGW)**
* **On-premises network**
* **Hybrid cloud**
* **Router**
* **Firewall**
* **IPsec VPN**
* **Static routing**
* **Dynamic routing**
* **BGP**
* **Public IP address**
* **AWS side**
* **Customer side**
* **Data center connectivity**
* **Branch office connectivity**
* **Encrypted tunnel**
* **Direct Connect backup**

When you see words like **on-premises**, **VPN**, **customer side**, **router**, or **BGP**, there is a good chance the question is testing Customer Gateway knowledge.

---

## Easy real-world example

A company has its main office in Rome and its application servers in AWS.

The company wants employees in the office to access private resources in a VPC.

The company already has a firewall or router in the office.

What happens:

* That office router or firewall is the **customer gateway device**
* In AWS, the company creates a **Customer Gateway** resource for it
* AWS uses a **Virtual Private Gateway** or **Transit Gateway** on its side
* A **Site-to-Site VPN** is created between the office and AWS

Now the office network and AWS can communicate securely.

---

## If I were an examiner ...

If I were writing exam questions, I would ask things like:

* Which AWS component represents the customer side of a Site-to-Site VPN connection?
* What is the difference between a Customer Gateway and a Virtual Private Gateway?
* Is a Customer Gateway the actual physical device or an AWS resource?
* Which AWS service securely connects an on-premises network to a VPC over the internet?
* Which component is on the customer side, and which component is on the AWS side?
* What is the difference between Site-to-Site VPN and Client VPN?
* When would you use Transit Gateway instead of Virtual Private Gateway?
* Does a Customer Gateway provide remote access for individual users?

An examiner may try to trick you by mixing these terms together.

---

## Final summary

A **Customer Gateway** is an AWS resource that represents your on-premises VPN device in a **Site-to-Site VPN** setup.

It is **not the tunnel itself**, and it is **not the AWS-side gateway**.

For the exam, remember this very clearly:

* **Customer Gateway = customer side in AWS**
* **Customer Gateway Device = real router or firewall on premises**
* **VGW or TGW = AWS side**
* **Site-to-Site VPN = secure connection between both sides**

---

## Short exam answer

A **Customer Gateway** is an AWS resource that represents the customer’s on-premises VPN device and is used with **AWS Site-to-Site VPN** to connect an on-premises network to AWS.

---

## Memory trick

Think:

* **C = Customer side**
* **V = Vendor or AWS side**

Or even simpler:

* **Customer Gateway = my company’s side**
* **Virtual Private Gateway = AWS side**

Another memory trick:

**CGW tells AWS about your router.**

It does not replace your router. It only represents it inside AWS.
