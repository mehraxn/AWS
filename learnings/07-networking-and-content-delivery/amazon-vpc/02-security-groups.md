# Amazon VPC Security Groups

## Simple definition

Amazon VPC Security Groups are virtual firewalls that control inbound and outbound traffic for AWS resources such as Amazon EC2 instances.

In simple words, a security group decides what traffic is allowed to reach a resource and what traffic is allowed to leave it.

---

## Core idea in plain English

Think of a security group as a gatekeeper attached to a server.

It checks the traffic trying to enter or leave that server.
If the rule allows the traffic, it passes.
If there is no rule allowing it, it is blocked.

A very important point is this
Security groups only have allow rules.
They do not have deny rules.

Another very important point
Security groups are stateful.
That means if you allow incoming traffic, the response is automatically allowed back, even if there is no separate outbound rule for that response.

---

## Main use cases

 Allow web traffic to a web server on port 80 or 443
 Allow SSH access to an EC2 instance on port 22
 Allow RDP access to a Windows server on port 3389
 Allow an application server to talk to a database server
 Restrict access so only certain IP addresses or other security groups can connect
 Protect resources inside a VPC by controlling network access

---

## Key features

 Works at the instance level or attached resource level
 Acts as a virtual firewall
 Supports inbound and outbound rules
 Supports rules based on

   Protocol
   Port number
   Source
   Destination
 Stateful behavior
 Only allow rules, no deny rules
 Can reference another security group as the source
 A resource can have multiple security groups attached

---

## How it works

When you launch an EC2 instance in a VPC, you can attach one or more security groups to it.

Each security group contains rules.
These rules say

 what traffic can come in
 what traffic can go out
 from where it can come
 to where it can go
 on which ports and protocols

For example

 Allow inbound HTTP on port 80 from anywhere
 Allow inbound HTTPS on port 443 from anywhere
 Allow inbound SSH on port 22 only from your office IP

If a request matches an allowed rule, AWS lets it pass.
If it does not match an allowed rule, AWS blocks it.

Because security groups are stateful, return traffic is automatically allowed.

Example
If you allow inbound traffic from a user to your web server, the reply from your server to that user is automatically allowed back.

---

## Why it is important for the exam

Security groups are one of the most tested VPC security topics in the AWS Certified Cloud Practitioner exam.

You must remember these core exam points

 Security groups are stateful
 Security groups have allow rules only
 Security groups control traffic at the resource level
 Default behavior blocks traffic unless it is explicitly allowed
 You can use security groups to control communication between EC2 instances and databases

In exam questions, AWS often checks whether you know the difference between security groups and network ACLs.
That is one of the biggest traps.

---

## Related AWS services and differences

### Security Groups vs Network ACLs

This is the most important comparison.

#### Security Groups

 Work at the instanceresource level
 Are stateful
 Support allow rules only
 Usually used to protect EC2 instances and other attached resources

#### Network ACLs

 Work at the subnet level
 Are stateless
 Support both allow and deny rules
 Require separate handling for return traffic

Easy way to remember

 Security Group = around the instance
 NACL = around the subnet

### Security Groups vs AWS WAF

 Security Groups filter traffic based on IP, port, and protocol
 AWS WAF protects web applications from HTTP and HTTPS threats such as SQL injection or cross-site scripting

So security groups are basic network traffic controls, while AWS WAF is application-layer protection.

### Security Groups vs AWS Shield

 Security Groups control allowed traffic to resources
 AWS Shield protects against DDoS attacks

So they are not the same thing.
Security groups are access control, while Shield is DDoS protection.

---

## Common exam traps

### Trap 1 Thinking security groups are stateless

Wrong.
Security groups are stateful.

### Trap 2 Thinking security groups can deny traffic

Wrong.
Security groups only have allow rules.

### Trap 3 Confusing security groups with network ACLs

Very common.

Remember

 Security groups = stateful, instance level, allow only
 NACLs = stateless, subnet level, allow and deny

### Trap 4 Forgetting default behavior

If traffic is not explicitly allowed, it is blocked.

### Trap 5 Thinking return traffic needs its own matching rule

For security groups, return traffic is automatically allowed because they are stateful.

### Trap 6 Mixing up security groups with IAM

IAM controls who can use AWS resources.
Security groups control network traffic to and from resources.

---

## Easy real-world example

Imagine you run a small online store.

You have

 one web server
 one database server

You configure the web server security group like this

 allow HTTP from anywhere
 allow HTTPS from anywhere
 allow SSH only from your IP address

You configure the database security group like this

 allow MySQL traffic only from the web server security group

This means

 customers can access the website
 random users cannot directly access the database
 only the web server can talk to the database
 only you can log in for administration

This is exactly how security groups improve protection inside a VPC.

---

## If I were an examiner ...

If I were writing Cloud Practitioner exam questions, I would ask things like these

### Question style 1

A company wants to control traffic to an EC2 instance at the instance level. Which service or feature should they use

Expected idea
Security group

### Question style 2

Which feature is stateful security groups or network ACLs

Expected idea
Security groups are stateful

### Question style 3

A company wants to explicitly deny certain IP addresses at the subnet level. What should they use

Expected idea
Network ACL, not security group

### Question style 4

A database should only accept traffic from an application server. How can AWS do this simply

Expected idea
Use a security group reference so the DB accepts traffic only from the app server’s security group.

### Question style 5

Which statement is true about security groups

Expected idea
They support allow rules only and are stateful.

As an examiner, I would test whether you can

 identify the correct layer of protection
 distinguish security groups from NACLs
 remember stateful vs stateless
 remember allow-only vs allow-and-deny

---

## Final summary

Amazon VPC Security Groups are virtual firewalls for AWS resources.
They control what traffic can enter and leave resources such as EC2 instances.

Their most important traits are

 stateful
 allow rules only
 resource level protection

For the exam, always remember that security groups are different from network ACLs.
That difference appears again and again in AWS questions.

---

## Short exam answer

Amazon VPC Security Groups are stateful virtual firewalls attached to AWS resources that control inbound and outbound traffic using allow rules only.

---

## Memory trick

Remember this sentence

Security Group = Server Guard

Why
Because it stands close to the server or resource and guards who can come in and go out.

And remember this pair

 SG = Stateful + Guarding the instance
 NACL = Not stateful + Controls the subnet

A second quick memory trick

SG = Say Yes only

That helps you remember
security groups have allow rules only.

---

## Exam coach note

When you see words like these in a question, think about security groups first

 instance level
 EC2 traffic
 allow web access
 allow SSH
 allow database access from app server
 stateful firewall
 virtual firewall

When you see words like these, think carefully about whether the answer is instead a network ACL

 subnet level
 deny specific traffic
 stateless

That small difference is often the key to getting the question right.
