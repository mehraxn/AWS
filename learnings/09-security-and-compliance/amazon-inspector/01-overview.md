# Amazon Inspector

## Simple definition

Amazon Inspector is an AWS security service that automatically looks for software vulnerabilities and unintended network exposure in your AWS workloads.

## Core idea in plain English

Think of Amazon Inspector as an automatic security checker for parts of your AWS environment. It keeps looking for known weaknesses, such as unpatched software or risky exposure, and then tells you what it finds.

It helps you discover security problems without manually checking every server, container image, or function yourself.

## Main use cases

* Find software vulnerabilities in Amazon EC2 instances
* Scan container images stored in Amazon ECR
* Check AWS Lambda functions for vulnerabilities
* Identify unintended network exposure
* Help security teams prioritize what to fix first
* Improve overall security posture across AWS accounts

## Key features

* **Automatic discovery** of supported workloads
* **Continuous scanning** instead of one-time manual checks
* **Findings and alerts** when vulnerabilities are detected
* **Risk prioritization** so teams can focus on more important issues first
* **Integration with AWS Organizations** for multi-account environments
* **Covers EC2, ECR, and Lambda**

## How it works

Amazon Inspector is enabled in your AWS environment.

After that, it automatically discovers supported resources such as EC2 instances, container images in Amazon ECR, and Lambda functions.

It then continuously scans them for known software vulnerabilities and possible unintended network exposure.

When it finds a problem, it creates a **finding**. A finding is a report that explains the issue, the affected resource, and the risk level.

Your team can review the findings, decide which issues matter most, and fix them.

## Why it is important for the exam

Amazon Inspector is important because AWS exams often test whether you can identify the right **security service** for a specific job.

You should know that Amazon Inspector is mainly about:

* vulnerability management
* continuous security scanning
* identifying weaknesses in workloads

For the exam, the key idea is simple:

**If the question is about finding vulnerabilities in EC2, container images, or Lambda, Amazon Inspector is a strong answer.**

## Related AWS services and differences

### Amazon Inspector vs Amazon GuardDuty

* **Amazon Inspector** looks for vulnerabilities and exposure in workloads.
* **Amazon GuardDuty** detects suspicious activity and threats in AWS accounts and workloads.

Easy way to remember:

* **Inspector = checks for weaknesses**
* **GuardDuty = watches for attacks or suspicious behavior**

### Amazon Inspector vs AWS Security Hub

* **Amazon Inspector** produces security findings about vulnerabilities.
* **AWS Security Hub** helps collect and view findings from multiple security services in one place.

Easy way to remember:

* **Inspector finds issues**
* **Security Hub organizes and centralizes findings**

### Amazon Inspector vs AWS Trusted Advisor

* **Amazon Inspector** focuses on security vulnerabilities and exposure in workloads.
* **AWS Trusted Advisor** gives general best-practice recommendations about cost, security, performance, fault tolerance, and service limits.

Easy way to remember:

* **Inspector = deep vulnerability scanning**
* **Trusted Advisor = broad best-practice checks**

### Amazon Inspector vs Amazon Macie

* **Amazon Inspector** checks workloads for vulnerabilities.
* **Amazon Macie** helps discover and protect sensitive data, especially in Amazon S3.

Easy way to remember:

* **Inspector = workload security**
* **Macie = sensitive data discovery**

## Common exam traps

* **Trap 1: Confusing Inspector with GuardDuty**
  Inspector finds vulnerabilities. GuardDuty detects suspicious or malicious activity.

* **Trap 2: Thinking Inspector is for DDoS protection**
  It is not. AWS Shield is for DDoS protection.

* **Trap 3: Thinking Inspector is mainly for compliance documents**
  It is not. AWS Artifact is for compliance reports and agreements.

* **Trap 4: Thinking Inspector is a firewall**
  It is not. Security Groups and NACLs control traffic. Inspector checks for weaknesses.

* **Trap 5: Forgetting the supported resource types**
  Focus on EC2, ECR container images, and Lambda.

## Easy real-world example

A company runs a web application on Amazon EC2, stores container images in Amazon ECR, and uses Lambda for small background tasks.

The company wants to know whether any of these resources have known software vulnerabilities.

They enable Amazon Inspector.

Amazon Inspector scans the supported workloads continuously and reports findings such as outdated software packages or risky exposure.

The security team reviews the findings and patches the most serious issues first.

## Final summary

Amazon Inspector is an AWS vulnerability management service.

It automatically discovers supported workloads and continuously scans them for software vulnerabilities and unintended network exposure.

For the Cloud Practitioner exam, remember that Amazon Inspector helps you **find security weaknesses** in workloads like EC2, ECR images, and Lambda.

## Short exam answer

**Amazon Inspector is an AWS service that automatically discovers and continuously scans workloads such as EC2 instances, ECR container images, and Lambda functions for software vulnerabilities and unintended network exposure.**

## Memory trick

**Inspector inspects.**

If a question asks:

* "Which service checks for vulnerabilities?"
* "Which service scans workloads for weaknesses?"

Think:

**Amazon Inspector = the AWS security inspector that looks for problems.**
