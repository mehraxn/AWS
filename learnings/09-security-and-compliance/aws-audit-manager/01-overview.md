# AWS Audit Manager

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

## Simple definition

AWS Audit Manager is an AWS service that helps you automatically collect and organize audit evidence for compliance and risk assessments.

It reduces the manual work of preparing for audits.

---

## Core idea in plain English

Think of AWS Audit Manager as an audit helper.

Normally, during an audit, teams spend a lot of time collecting screenshots, configuration details, logs, and proof that security controls are working.

AWS Audit Manager helps by automatically gathering evidence from your AWS environment and organizing it based on audit frameworks and controls.

So instead of chasing documents manually, you get a more structured and repeatable audit process.

---

## Main use cases

### 1. Preparing for compliance audits

A company can use Audit Manager to collect evidence for standards such as security and compliance frameworks.

### 2. Reducing manual audit work

Security and compliance teams can save time because evidence is collected automatically from AWS data sources.

### 3. Tracking internal controls

Organizations can review whether their controls, policies, and procedures are being followed.

### 4. Building audit-ready reports

Teams can generate reports and share them with internal reviewers or external auditors.

### 5. Multi-account auditing

Large companies using multiple AWS accounts can centralize evidence collection across accounts.

---

## Key features

### Automated evidence collection

Audit Manager automatically collects evidence from AWS services instead of requiring you to gather everything by hand.

### Prebuilt frameworks

It provides standard frameworks that map controls to common compliance requirements.

### Custom frameworks and controls

You can also create your own frameworks and controls if your company has internal requirements.

### Assessment reports

You can generate audit reports from the collected evidence.

### Evidence review workflow

Teams can review controls, add comments, upload manual evidence, and track progress.

### Multi-account support

It can work across accounts in AWS Organizations, which is useful for enterprise environments.

### Continuous evidence collection

Evidence collection continues while an assessment is active.

---

## How it works

Here is the simple flow

1. You choose a framework.
2. You create an assessment.
3. You define the AWS accounts and services that are in scope.
4. Audit Manager starts collecting evidence automatically.
5. The evidence is mapped to controls.
6. Reviewers can inspect the evidence, add comments, and upload manual files if needed.
7. You generate an assessment report for the audit.

### Important words to know

 Framework = a collection of controls based on a standard or requirement
 Control = a specific requirement that must be checked
 Assessment = the audit project you create in Audit Manager
 Evidence = the proof collected to show a control is being met

---

## Why it is important for the exam

For the Cloud Practitioner exam, the main idea is simple

AWS Audit Manager helps automate evidence collection for audits and compliance reviews.

This matters because exam questions often test whether you can identify the service that

 reduces manual effort during audits
 helps with compliance evidence
 organizes evidence by controls and frameworks
 creates audit-ready reports

You should also remember that Audit Manager is part of the governance, risk, and compliance area of AWS.

---

## Related AWS services and differences

### AWS Audit Manager vs AWS Artifact

 Audit Manager helps you collect evidence about your own AWS usage
 AWS Artifact gives you AWS compliance reports and agreements such as AWS certifications and audit documents

Easy way to remember

 Artifact = documents from AWS
 Audit Manager = evidence about your environment

### AWS Audit Manager vs AWS Config

 AWS Config records and evaluates resource configurations
 Audit Manager uses evidence, including from services like Config, to support audits

Config checks resource settings. Audit Manager organizes evidence for audit work.

### AWS Audit Manager vs AWS CloudTrail

 CloudTrail records API activity and account actions
 Audit Manager can use such information as audit evidence

CloudTrail logs actions. Audit Manager manages evidence.

### AWS Audit Manager vs AWS Security Hub

 Security Hub shows security findings and security posture
 Audit Manager focuses on audit evidence and compliance assessments

Security Hub is for security visibility. Audit Manager is for audit preparation.

---

## Common exam traps

### Trap 1 Thinking Audit Manager proves compliance automatically

This is the biggest trap.

Audit Manager does not certify that you are compliant.

It helps collect and organize evidence, but people still need to review the evidence and make compliance decisions.

### Trap 2 Confusing it with AWS Artifact

If the question asks for downloading AWS compliance reports from AWS, the answer is AWS Artifact, not Audit Manager.

### Trap 3 Confusing it with AWS Config

If the question is about checking whether a resource configuration follows a rule, that is more likely AWS Config.

### Trap 4 Confusing it with CloudTrail

If the question is about logging API calls or user actions, that is AWS CloudTrail.

### Trap 5 Assuming everything is fully automatic

Audit Manager automates a lot, but teams may still need to add manual evidence and review results.

---

## Easy real-world example

Imagine a company is preparing for a security audit.

The auditor asks for proof that

 important AWS resources are configured correctly
 changes are tracked
 certain controls are reviewed regularly

Without Audit Manager, the team might spend days collecting screenshots, logs, spreadsheets, and emails.

With Audit Manager, the company creates an assessment, selects the framework, and lets AWS automatically gather much of the needed evidence. The team then reviews it and generates a report for the auditor.

---

## Final summary

AWS Audit Manager is a service that helps organizations prepare for audits faster by automating evidence collection and organizing that evidence around frameworks, controls, and assessments.

It is useful for compliance teams, security teams, and organizations that want a more structured audit process.

For the exam, remember this key message

Audit Manager helps with audit evidence and compliance readiness, but it does not itself guarantee compliance.

---

## Short exam answer

AWS Audit Manager is a service that automates the collection of audit evidence to help organizations simplify risk and compliance assessments and generate audit-ready reports.

---

## Memory trick

Audit Manager = “Manage my audit evidence.”

Or even shorter

Artifact gives AWS documents. Audit Manager gathers your audit proof.

## Additional Distinct Source Material

## 🤔 Wait — What Is an Audit and What Is Audit Evidence

Before anything else, let's make sure these two words are crystal clear. They are the heart of this service.

---

### 🏫 What Is an Audit

An audit is simply an official check-up.

Think of it like this

 A school inspector visits your school to check Are you actually following all the education rules
 They don't just take your word for it — they want proof.

In the businesscloud world, an audit is when an external authority (a regulator, a customer, or an internal team) comes to check
 Is your company actually following the security and privacy rules you're supposed to follow

Examples of rules (called compliance frameworks) they might check
- HIPAA → Are you protecting patient health data
- PCI DSS → Are you handling credit card data safely
- SOC 2 → Are your systems secure, available, and private
- GDPR → Are you handling EU citizens' personal data correctly

The audit can happen once a year, or continuously. Either way, you must prove you are following the rules.

---

### 🗂️ What Is Audit Evidence

Audit evidence is the proof you show to the auditor.

It answers the question How do I know you're actually following the rules — and not just saying you are

Here are real examples of audit evidence in AWS

 Rule (Control)  Evidence That Proves It
------
 Only authorized users can access your systems  CloudTrail log showing who logged in and when
 Your S3 buckets are not publicly exposed  AWS Config report showing all buckets are private
 You have encryption enabled on your databases  A configuration snapshot showing RDS encryption is ON
 You are monitoring for suspicious activity  GuardDuty findings report showing active monitoring

 💡 In plain English Evidence = screenshots, logs, reports, and records that say Yes, we did the thing we were supposed to do.

---

### 🔗 So Where Does AWS Audit Manager Fit In

Normally, collecting all this evidence is painful and manual
- Someone has to log into AWS every day
- Download logs, take screenshots, export reports
- Organize everything into folders for the auditor
- Hope they didn't miss anything

AWS Audit Manager does ALL of this automatically. It knows which rules you need to follow (based on the framework you choose), and it goes and collects the right evidence from CloudTrail, Config, Security Hub — every single day — and organizes it for you.

 🤖 Audit Manager = the employee who never sleeps, never forgets, and always has your evidence ready.

---

## 🎓 If I Were an Examiner...

As your AWS exam tutor, here's what I would ask to test your understanding of AWS Audit Manager

---

Q1 — Classic scenario question
 A company needs to continuously collect evidence that their AWS environment complies with HIPAA regulations for an upcoming audit. Which AWS service should they use
 → Answer AWS Audit Manager

---

Q2 — Differentiation trap
 A security team wants to download AWS's own compliance reports and certifications to show a customer that AWS meets ISO 27001. Which service should they use
 → Answer AWS Artifact (not Audit Manager — Artifact is for AWS's own compliance docs)

---

Q3 — Use case identification
 Which AWS service helps automate the process of preparing audit-ready reports by collecting evidence from AWS Config, CloudTrail, and Security Hub
 → Answer AWS Audit Manager

---

Q4 — Wrong answer distractor
 A company wants to detect unauthorized access and suspicious activity in their AWS environment before their annual compliance audit. Which service should they use
 → Answer Amazon GuardDuty (not Audit Manager — GuardDuty detects threats; Audit Manager collects compliance evidence)

---

Q5 — Framework understanding
 An organization uses AWS Audit Manager and selects a pre-built framework. What does this framework represent
 → Answer A set of compliance controls based on a regulatory standard (e.g., HIPAA, SOC 2, PCI DSS)

---

📌 Examiner's tip The exam will almost always test Audit Manager in a prove compliance  collect evidence  automate audit scenario. If the question mentions auditors, evidence, compliance frameworks, or audit-ready reports — think AWS Audit Manager.

---

📘 Study Note prepared by your AWS Exam Coach  AWS Certified Cloud Practitioner Prep
