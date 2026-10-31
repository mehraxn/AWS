# AWS Artifact

## Simple definition

AWS Artifact is an AWS service that gives you on-demand access to AWS security and compliance reports and lets you review and accept certain agreements with AWS.

---

## Core idea in plain English

Think of AWS Artifact as AWS's compliance document library.

If a company wants proof that AWS meets certain security or compliance standards, it can use AWS Artifact to download official reports such as SOC reports, ISO certifications, and PCI-related documents.

It can also be used to review and manage some agreements with AWS.

So the main idea is simple
AWS Artifact helps customers access compliance documents and agreements without opening support tickets.

---

## Main use cases

### 1. Downloading compliance reports

A company can download AWS audit and compliance reports when auditors, security teams, or customers ask for proof of AWS compliance.

### 2. Reviewing AWS security posture

Teams can read AWS-published compliance documents to better understand AWS security and control environments.

### 3. Accepting agreements with AWS

Organizations can review, accept, and manage some legal or compliance-related agreements directly through AWS Artifact.

### 4. Supporting audits

When an auditor asks for AWS compliance evidence, Artifact is one of the main places to get that documentation.

### 5. Multi-account agreement management

Organizations using AWS Organizations can manage some agreements across multiple accounts.

---

## Key features

 On-demand access to AWS compliance reports
 Access to documents such as SOC, ISO, PCI, and other compliance-related reports
 Self-service portal in the AWS Management Console
 Agreement review and acceptance for certain AWS agreements
 Support for organization-level agreement management in some cases
 Access to some third-party or ISV compliance reports related to AWS Marketplace offerings
 No infrastructure to manage
 Provided at no extra charge

---

## How it works

1. You sign in to the AWS Management Console.
2. You open AWS Artifact.
3. You browse available reports or agreements.
4. You download the compliance document you need or review an agreement.
5. You share the report securely with auditors, compliance teams, or internal reviewers when needed.

At a high level, Artifact is not a tool that scans your environment.
It is a portal that gives you access to AWS compliance evidence and agreements.

That point is very important for the exam.

---

## Why it is important for the exam

For the AWS Certified Cloud Practitioner exam, AWS Artifact matters because AWS often tests whether you understand

 Which service gives access to compliance and audit reports
 Which service helps with legalcompliance agreements with AWS
 The difference between AWS compliance documents and customer responsibilities
 The difference between AWS Artifact and other security or audit services

A classic exam-style idea is
A customer needs AWS compliance reports for an auditor. Which service should they use
The answer is AWS Artifact.

---

## Related AWS services and differences

### AWS Artifact vs AWS Audit Manager

 AWS Artifact gives you access to AWS compliance reports and agreements.
 AWS Audit Manager helps automate evidence collection for your own audits.

Easy way to remember

 Artifact = get AWS documents
 Audit Manager = help manage your audit process

### AWS Artifact vs AWS Config

 AWS Artifact provides compliance documents from AWS.
 AWS Config records and evaluates configuration changes in your AWS resources.

Artifact does not track whether your S3 bucket is public.
Config can help with that.

### AWS Artifact vs AWS Security Hub

 AWS Artifact is for compliance reports and agreements.
 AWS Security Hub helps view and manage security findings across services.

Artifact is about documents.
Security Hub is about security visibility and findings.

### AWS Artifact vs AWS IAM

 AWS Artifact is where you access reports and agreements.
 AWS IAM controls who is allowed to access Artifact and other AWS services.

IAM manages permissions.
Artifact provides the documents.

### AWS Artifact vs AWS Organizations

 AWS Artifact can help manage agreements across accounts.
 AWS Organizations is the service used to centrally manage multiple AWS accounts.

Organizations is the account management service.
Artifact is the complianceagreement portal.

### AWS Artifact vs AWS CodeArtifact

 AWS Artifact is for compliance documents and agreements.
 AWS CodeArtifact is a package repository for software dependencies.

This is a very common exam trap because the names sound similar.

---

## Common exam traps

### Trap 1 Thinking AWS Artifact performs audits

It does not perform audits.
It provides reports and agreements.

### Trap 2 Mixing it up with AWS Audit Manager

Audit Manager helps collect and organize evidence for audits.
Artifact gives access to AWS compliance documents.

### Trap 3 Thinking it monitors your resources

Artifact does not monitor EC2, S3, or VPC settings.
Services like AWS Config, Security Hub, or CloudTrail are used for monitoring and tracking.

### Trap 4 Thinking it makes your workload automatically compliant

Artifact gives you AWS compliance documentation.
It does not make your whole application automatically compliant.
You still have customer-side responsibilities under the shared responsibility model.

### Trap 5 Confusing Artifact with CodeArtifact

AWS Artifact = compliance reports and agreements.
AWS CodeArtifact = software package repository.

### Trap 6 Assuming it is a storage service for documents

It is not a general document storage service like Amazon S3.
It is a specialized portal for AWS compliance and agreement documents.

---

## Easy real-world example

A company is preparing for a security audit.
The auditor asks for AWS SOC reports to verify the compliance posture of the AWS infrastructure being used.

The company logs in to AWS Artifact, downloads the needed compliance reports, and securely shares them with the auditor.

That is a perfect real-world use of AWS Artifact.

---

## Final summary

AWS Artifact is a self-service AWS service for accessing compliance reports, certifications, and certain agreements with AWS.

Its main purpose is to help customers get AWS audit and compliance documents quickly and manage some agreements without manual back-and-forth.

For the exam, remember that AWS Artifact is mainly about

 Compliance reports
 Audit documents
 Agreements with AWS

It is not a monitoring service, not a configuration tracking service, and not an audit automation engine.

---

## Short exam answer

AWS Artifact is the AWS service that provides on-demand access to AWS compliance reports, certifications, and certain agreements with AWS.

---

## Memory trick

Think
Artifact = official paper evidence

Like an old historical artifact that proves something existed, AWS Artifact gives you official documents that prove AWS compliance and controls.

Another quick memory line
Artifact = audit papers from AWS

---

## If I were an examiner ...

If I were writing Cloud Practitioner exam questions, I would ask things like these

### 1. Which AWS service should a customer use to download AWS SOC reports

Expected idea AWS Artifact

### 2. Which service lets a company review and accept certain agreements with AWS

Expected idea AWS Artifact

### 3. A company wants a service that helps collect evidence for its own audit assessments. Is that AWS Artifact

Expected idea No, that is closer to AWS Audit Manager

### 4. A company wants to monitor resource configuration changes for compliance. Is AWS Artifact the best answer

Expected idea No, that is closer to AWS Config

### 5. Which service name is often confused with AWS Artifact because it sounds similar but is actually for software packages

Expected idea AWS CodeArtifact

### 6. Does AWS Artifact automatically make a customer's workloads compliant

Expected idea No, customers still have responsibilities under the shared responsibility model

### 7. What is the main exam keyword for AWS Artifact

Expected idea compliance reports and agreements

---

## Exam coach tip

When you see words like these in a question

 audit report
  n- SOC report
 ISO certification
 compliance documentation
 agreement with AWS
 evidence for auditors

You should strongly think of AWS Artifact.

When you see words like

 collect audit evidence automatically
 audit framework
 assessment management

You should think more about AWS Audit Manager, not Artifact.
