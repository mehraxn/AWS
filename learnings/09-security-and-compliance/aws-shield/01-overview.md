# AWS Shield

## Simple definition

AWS Shield is an AWS security service that protects applications and AWS resources from **DDoS attacks**

A DDoS attack tries to overwhelm a website or application with huge amounts of traffic so real users cannot access it.

---

## Core idea in plain English

Think of AWS Shield as a **traffic protection service**.

If bad traffic tries to flood your application, AWS Shield helps absorb, detect, and reduce that attack so your app stays available.

For the exam, the most important idea is this:

* **AWS Shield = DDoS protection**
* **Shield Standard = automatic basic protection**
* **Shield Advanced = extra protection and expert help**

---

## Main use cases

AWS Shield is commonly used when you want to protect:

* Public websites
* Web applications
* APIs
* Applications behind Elastic Load Balancing
* Content delivered through CloudFront
* DNS with Amazon Route 53

It is especially important for businesses that cannot afford downtime during an attack.

---

## Key features

### 1. Protection against DDoS attacks

Shield is designed to defend against Distributed Denial of Service attacks.

### 2. AWS Shield Standard

This is included automatically for AWS customers at no extra cost.

It provides basic protection against common network and transport layer DDoS attacks.

### 3. AWS Shield Advanced

This is the paid version.

It provides:

* More advanced DDoS detection and mitigation
* Better visibility into attacks
* Help from the **AWS Shield Response Team (SRT)**
* Cost protection for scaling charges caused by DDoS events
* Closer integration with AWS WAF for application-layer protection

### 4. Works with important AWS services

Shield is commonly associated with services such as:

* Amazon CloudFront
* Route 53
* Elastic Load Balancing (ELB)
* AWS Global Accelerator
* Amazon EC2 Elastic IP resources

---

## How it works

AWS Shield monitors traffic going to supported AWS resources.

If AWS detects traffic that looks like a DDoS attack, it automatically applies protections to reduce the impact.

### With Shield Standard

AWS gives automatic always-on protection against common DDoS attacks.

### With Shield Advanced

You get stronger detection, more detailed monitoring, and expert support during attacks.

For application-layer attacks, Shield Advanced can work with **AWS WAF** to help filter malicious web requests.

---

## Why it is important for the exam

AWS Cloud Practitioner questions often test whether you know the difference between security services.

AWS Shield is important because it is the main AWS service for **DDoS protection**.

You should remember these exam points:

* If the question says **DDoS attack**, think **AWS Shield**
* If the question asks for **web request filtering**, think **AWS WAF**
* If the question is about **finding vulnerabilities**, think **Amazon Inspector**
* If the question is about **threat detection in AWS accounts**, think **Amazon GuardDuty**

---

## Related AWS services and differences

### AWS Shield vs AWS WAF

* **AWS Shield** protects mainly against DDoS attacks
* **AWS WAF** filters and blocks specific web requests based on rules

Easy way to remember:

* **Shield = absorbs attack traffic**
* **WAF = filters web traffic**

### AWS Shield vs Amazon GuardDuty

* **Shield** protects against DDoS attacks
* **GuardDuty** detects suspicious activity and threats in AWS accounts and workloads

### AWS Shield vs Amazon Inspector

* **Shield** protects running applications from DDoS attacks
* **Inspector** scans workloads for software vulnerabilities and exposures

### AWS Shield vs AWS Firewall Manager

* **Shield** provides the DDoS protection itself
* **Firewall Manager** helps manage security rules and protections across multiple accounts and resources

---

## Common exam traps

### Trap 1: Confusing Shield with WAF

Many questions try to make you mix these up.

* **Shield** = DDoS protection
* **WAF** = application request filtering

### Trap 2: Thinking Shield Advanced is automatic for everyone

It is not.

Only **Shield Standard** is included automatically.

**Shield Advanced** is a paid subscription.

### Trap 3: Thinking Shield solves every security problem

It does not.

Shield focuses on **availability protection from DDoS**, not malware scanning, patching, identity control, or vulnerability assessment.

### Trap 4: Forgetting the keyword “DDoS”

When the exam says:

* large traffic flood
* denial of service
* keep website available during attack

The answer is often **AWS Shield**.

---

## Easy real-world example

Imagine you run an online store on AWS.

One day, attackers send a huge flood of fake traffic to your website so real customers cannot open it.

AWS Shield helps protect your application from this traffic flood.

If you use **Shield Standard**, you get automatic baseline protection.

If you use **Shield Advanced**, you get stronger protection, better visibility, and AWS experts to help during serious attacks.

---

## Final summary

AWS Shield is AWS’s service for protection against DDoS attacks.

Its main job is to keep applications available when attackers try to overwhelm them with traffic.

There are two versions:

* **Shield Standard**: automatic basic DDoS protection at no extra cost
* **Shield Advanced**: paid advanced protection with more features and expert support

For the exam, remember that AWS Shield is the correct answer whenever the problem is about **DDoS protection**.

---

## Short exam answer

**AWS Shield is a managed AWS service that protects applications and AWS resources against DDoS attacks. Shield Standard is included automatically, while Shield Advanced provides enhanced protection and expert support.**

---

## Memory trick

Think:

**Shield = protects your app like a shield protects a soldier**

And more specifically:

**AWS Shield = shield against DDoS traffic floods**
