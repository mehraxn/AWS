# AWS Directory Service

## Simple definition

AWS Directory Service is an AWS service that helps you use Microsoft Active Directory (AD) in AWS.

It lets you either

 run a managed directory in AWS, or
 connect AWS to your existing on-premises Active Directory.

---

## Core idea in plain English

Think of AWS Directory Service as a way to bring your company login system into AWS.

If a company already uses Active Directory for employees, usernames, passwords, groups, and Windows computers, AWS Directory Service helps those same identities work with AWS resources.

So instead of creating separate users everywhere, you can use a directory-based identity system to manage access more easily.

---

## Main use cases

AWS Directory Service is commonly used for

 Connecting AWS applications to an existing Active Directory
 Letting users sign in with their company credentials
 Joining Amazon EC2 Windows instances to a domain
 Running Windows workloads that need Active Directory
 Managing users, groups, and policies in the AWS Cloud
 Supporting directory-aware AWS services such as Amazon WorkSpaces and some Microsoft-based workloads

---

## Key features

### 1. Multiple directory options

AWS Directory Service is not just one single directory type. It gives you different options depending on your need.

#### AWS Managed Microsoft AD

 Real Microsoft Active Directory as a managed AWS service
 Good when you want a full AD environment in AWS
 Supports domain join, Group Policy, trusts, and directory-aware workloads

#### AD Connector

 A gateway to your existing on-premises Microsoft AD
 Does not store directory data in AWS
 Good when you want AWS to use your current AD without creating a separate directory in the cloud

#### Simple AD

 A lower-cost, basic directory option
 Good for smaller or simpler environments
 Has basic Active Directory compatibility, but it is not the same as full Microsoft AD

### 2. Managed service benefits

With AWS managed directory options, AWS handles much of the infrastructure work, such as availability and operational maintenance.

### 3. Integration with AWS services

AWS Directory Service can work with services and workloads that need directory-based authentication and identity management.

### 4. Identity and access support

It helps organize users and groups so applications and systems can decide who can sign in and what they can access.

---

## How it works

At a simple level, AWS Directory Service works like this

1. You choose a directory type.
2. You connect it to your AWS environment, usually inside a VPC.
3. Users, groups, and directory information are used for authentication and access.
4. AWS resources or applications use that directory to verify identities.

### Example flow with AWS Managed Microsoft AD

1. A company creates an AWS Managed Microsoft AD directory.
2. AWS sets up highly available directory infrastructure in the VPC.
3. The company joins Windows EC2 instances to the domain.
4. Employees sign in using directory credentials.
5. Admins manage users, groups, and policies from the directory.

### Example flow with AD Connector

1. A company already has Active Directory on-premises.
2. It creates an AD Connector in AWS.
3. AWS forwards authentication requests to the on-premises AD.
4. Users keep using existing usernames and passwords.
5. AWS resources can rely on that existing directory.

---

## Why it is important for the exam

For the Cloud Practitioner exam, the main point is to understand that AWS Directory Service helps with directory-based identity management, especially for Microsoft Active Directory use cases.

You should remember

 It is about directories, users, groups, authentication, and WindowsAD environments
 It is useful when companies already use Active Directory
 AWS offers different directory options depending on whether you want a fully managed AD or a connection to an existing AD
 It is not the same thing as IAM

Exam questions often test whether you know when to choose

 AWS Managed Microsoft AD
 AD Connector
 another identity service like IAM or IAM Identity Center

---

## Related AWS services and differences

### AWS Directory Service vs IAM

 IAM controls permissions for AWS resources
 AWS Directory Service handles directory-based identities and Active Directory integration

Easy way to think about it

 IAM = permissions inside AWS
 Directory Service = directory users and AD-based sign-in support

### AWS Directory Service vs IAM Identity Center

 IAM Identity Center is for workforce access to AWS accounts and applications
 AWS Directory Service can provide or connect the Active Directory source behind that access in some setups

So

 Directory Service helps with the directory
 IAM Identity Center helps with centralized sign-in and access to AWS accountsapps

### AWS Directory Service vs Amazon Cognito

 Cognito is mainly for app users, especially web and mobile applications
 Directory Service is mainly for enterprise directory and Microsoft AD-related use cases

### AWS Managed Microsoft AD vs AD Connector

 AWS Managed Microsoft AD = AWS runs an actual managed Microsoft AD in the cloud
 AD Connector = AWS connects to your existing on-premises AD and forwards requests

This is one of the most important differences for the exam.

---

## Common exam traps

### Trap 1 Confusing Directory Service with IAM

These are not the same.

IAM is for managing AWS permissions.
Directory Service is for directory identities and AD integration.

### Trap 2 Thinking AD Connector creates a full directory in AWS

It does not.

AD Connector is mainly a bridge or gateway to your existing on-premises Active Directory.

### Trap 3 Thinking Simple AD equals full Microsoft AD

It does not.

Simple AD has basic compatibility, but it is not the full-featured Microsoft AD experience.

### Trap 4 Using Cognito for employee Windows domain needs

Cognito is usually for application users.
For enterprise Microsoft AD and Windows directory scenarios, Directory Service is the better fit.

### Trap 5 Forgetting the keyword “existing Active Directory”

If the question says the company already has on-premises Active Directory and wants AWS to use it, that is a strong clue for AD Connector.

If the question wants a managed Microsoft Active Directory in AWS, that points to AWS Managed Microsoft AD.

---

## Easy real-world example

A company already has Microsoft Active Directory in its office.
All employees use the same company username and password to sign in to their Windows computers.

Now the company moves some Windows servers to AWS and wants employees to keep using the same login.

The company can use AWS Directory Service.

 If it wants to keep using the office Active Directory, it can use AD Connector
 If it wants AWS to run a managed Active Directory in the cloud, it can use AWS Managed Microsoft AD

This makes identity management easier and avoids creating a separate login system for the new AWS environment.

---

## Final summary

AWS Directory Service helps organizations use Microsoft Active Directory with AWS.

Its main value is bringing directory-based identity management into the cloud.

The most important exam idea is that AWS Directory Service gives you different options

 AWS Managed Microsoft AD for a managed AD in AWS
 AD Connector to connect to an existing on-premises AD
 Simple AD for smaller basic directory needs

It is mainly used for enterprise identity, Windows environments, domain join, and directory-aware applications.

---

## Short exam answer

AWS Directory Service is an AWS service that helps organizations use Microsoft Active Directory in AWS, either by running a managed directory in the cloud or by connecting AWS resources to an existing on-premises Active Directory.

---

## Memory trick

Remember this

Directory Service = company login system in AWS

And for the options

 Managed Microsoft AD = AWS runs the directory
 AD Connector = AWS connects to your existing directory
 Simple AD = basic smaller directory option

A simple phrase

“Manage, Connect, or Keep it Simple.”

 Manage = AWS Managed Microsoft AD
 Connect = AD Connector
 Keep it Simple = Simple AD
