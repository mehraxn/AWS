# AWS Compliance Programs Page

## Simple definition

The AWS Compliance Programs page is the AWS page that shows which compliance standards, certifications, attestations, and frameworks AWS supports.

It helps customers understand whether AWS has been independently assessed against rules or standards such as SOC, PCI DSS, ISO, HIPAA eligibility, FedRAMP, and others.

## Core idea in plain English

Think of this page as AWS saying

“Here are the compliance programs we support, here is what they mean, and here is how you can check whether AWS services are covered.”

This page is important because many companies must follow legal, security, or industry rules. AWS gives customers information and reports to help them build systems that meet those rules.

## Main use cases

You use the AWS Compliance Programs page when you want to

 Check whether AWS supports a specific compliance program
 Understand whether a service is in scope for a standard
 Prepare for audits or security reviews
 Show auditors that AWS has third-party assessments
 Learn which AWS documents can be downloaded from AWS Artifact
 Compare AWS compliance support for regulated workloads

## Key features

### 1. List of compliance programs

The page groups AWS support across many programs and standards, such as

 SOC reports
 PCI DSS
 ISO certifications
 HIPAA eligible services
 FedRAMP
 Regional or industry-specific programs

### 2. Program details

For each program, AWS usually provides a short explanation of

 What the program is
 Why it matters
 Which reports or certifications exist
 Where to find more details

### 3. Services in scope

The page connects to AWS information showing which AWS services are covered by a specific compliance program.

This is very important because

Not every AWS service is automatically in scope for every compliance program.

### 4. AWS Artifact integration

Many AWS compliance reports can be downloaded through AWS Artifact.

That means customers can get audit reports and agreements on demand instead of opening a support case.

### 5. Shared responsibility context

The page is part of the bigger AWS security and compliance story.

AWS helps by securing and validating the cloud infrastructure, but customers still have their own compliance responsibilities for how they use AWS.

## How it works

Here is the simple flow

1. A customer goes to the AWS Compliance Programs page.
2. They choose a program they care about, such as SOC or PCI.
3. They review what AWS says about that program.
4. They check whether the AWS services they plan to use are in scope.
5. They download reports or agreements from AWS Artifact if needed.
6. They design their own workload to meet their company’s rules and auditor requirements.

So the page does not make your system compliant by itself.

It gives you information, evidence, and starting points.

## Why it is important for the exam

For the Cloud Practitioner exam, this topic matters because AWS often tests whether you know

 AWS supports many compliance programs
 AWS compliance is part of the shared responsibility model
 Customers can access compliance reports through AWS Artifact
 A service being on AWS does not mean your full application is automatically compliant
 You must check whether a specific service is in scope for the required program

## Related AWS services and differences

### AWS Compliance Programs page vs AWS Artifact

 Compliance Programs page = information page about AWS certifications, attestations, and programs
 AWS Artifact = portal where you download reports and manage certain agreements

### AWS Compliance Programs page vs Shared Responsibility Model

 Compliance Programs page = shows what AWS has been assessed against
 Shared Responsibility Model = explains which compliance and security tasks belong to AWS and which belong to the customer

### AWS Compliance Programs page vs AWS Audit Manager

 Compliance Programs page = tells you about AWS compliance support and reports
 AWS Audit Manager = helps you collect evidence and map controls for your own audits

### AWS Compliance Programs page vs AWS Config  Security Hub

 Compliance Programs page = informational and evidence-focused
 AWS Config  Security Hub = help monitor resources and security posture in your environment

## Common exam traps

### Trap 1 “AWS is compliant, so my application is automatically compliant.”

Wrong.

AWS may be certified for many programs, but your workload design, settings, access control, logging, encryption, and data handling are still your responsibility.

### Trap 2 “All AWS services are covered by every compliance program.”

Wrong.

Always check whether the specific service is in scope.

### Trap 3 “Compliance reports are downloaded from Trusted Advisor or Support Center.”

Wrong.

The exam answer is usually AWS Artifact.

### Trap 4 “Compliance means only security.”

Not exactly.

Compliance includes security, but also legal, regulatory, audit, privacy, and industry requirements.

### Trap 5 “The Compliance Programs page is a service that monitors resources.”

Wrong.

It is mainly an information and reference page, not a runtime monitoring service.

## Easy real-world example

A company wants to build a payment application on AWS and must follow PCI DSS.

The team goes to the AWS Compliance Programs page and checks AWS PCI information.
Then they verify which AWS services are in scope.
After that, they use AWS Artifact to download AWS PCI documents for their auditors.

But they still must configure their own application securely, protect cardholder data, control access, and follow PCI rules in their own environment.

So AWS helps, but the customer still has work to do.

## Final summary

The AWS Compliance Programs page helps customers understand which compliance frameworks and certifications AWS supports.

It is a reference page for security and audit information. It helps customers learn about AWS compliance coverage, check which services are in scope, and find reports that can be downloaded from AWS Artifact.

For the exam, remember this

AWS provides compliance information and third-party reports, but customers are still responsible for compliance in how they build and operate their workloads.

## Short exam answer

The AWS Compliance Programs page provides information about AWS compliance certifications, attestations, and frameworks. It helps customers understand AWS compliance support, check services in scope, and find reports through AWS Artifact.

## Memory trick

Compliance Programs = “Proof page”

Use this memory trick

 Compliance Programs page = shows the proof categories
 AWS Artifact = gives you the proof documents
 Customer = must still use AWS correctly to be compliant

A simple line to remember

“Programs explain it, Artifact downloads it, customer applies it.”
