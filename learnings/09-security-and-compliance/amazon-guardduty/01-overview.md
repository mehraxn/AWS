# Amazon GuardDuty

## Simple definition

Amazon GuardDuty is an AWS threat detection service that continuously monitors your AWS environment for suspicious activity and possible security threats.

## Core idea in plain English

Think of GuardDuty as a smart security watcher for your AWS account.

It looks at activity in your AWS environment, notices behavior that seems dangerous or unusual, and then alerts you with findings.

It does **not** fix the problem by itself. Its main job is to **detect and alert**.

## Main use cases

* Detect stolen or misused AWS credentials
* Detect suspicious API calls in your AWS account
* Detect unusual network activity involving EC2 workloads
* Detect threats related to S3 data access
* Detect suspicious activity in EKS environments
* Detect suspicious behavior involving Lambda and some database activity
* Identify malware-related risks in supported workloads and storage use cases

## Key features

* Fully managed AWS security service
* Continuous threat detection
* Uses machine learning and threat intelligence
* Produces security findings when suspicious activity is detected
* Helps monitor AWS accounts, workloads, and data
* Integrates with other AWS security and response services
* Can work across multiple AWS accounts through centralized management

## How it works

GuardDuty collects and analyzes security-related activity from AWS data sources.

It looks for patterns that may indicate threats such as account compromise, reconnaissance, malware activity, suspicious access, or data exfiltration.

When it finds something suspicious, it creates a **finding**.

A finding is a security alert that tells you:

* what GuardDuty found
* which resource may be affected
* how severe the issue may be
* what kind of threat it might be

You can then investigate and respond using other AWS tools or your own security process.

## Why it is important for the exam

For the Cloud Practitioner exam, GuardDuty is important because AWS likes to test whether you know the difference between:

* **detecting threats**
* **blocking traffic**
* **auditing actions**
* **checking compliance**

GuardDuty is mainly about **intelligent threat detection**.

If an exam question asks which service helps identify suspicious or malicious activity in an AWS account, GuardDuty is often the right answer.

## Related AWS services and differences

### GuardDuty vs Amazon Inspector

* **GuardDuty** detects suspicious activity and threats in your AWS environment.
* **Inspector** assesses workloads for software vulnerabilities and unintended network exposure.

Easy way to remember:

* **GuardDuty = watches for threats and strange behavior**
* **Inspector = checks systems for weaknesses**

### GuardDuty vs AWS Security Hub

* **GuardDuty** generates threat findings.
* **Security Hub** brings security findings from multiple services into one central place.

Easy way to remember:

* **GuardDuty finds problems**
* **Security Hub organizes and aggregates findings**

### GuardDuty vs Amazon Macie

* **GuardDuty** looks for threats and suspicious activity.
* **Macie** helps discover and protect sensitive data, especially in S3.

Easy way to remember:

* **GuardDuty = threat detection**
* **Macie = sensitive data discovery**

### GuardDuty vs AWS Shield

* **GuardDuty** detects security threats in AWS environments.
* **Shield** protects mainly against DDoS attacks.

Easy way to remember:

* **GuardDuty = notices threats**
* **Shield = helps protect against DDoS attacks**

### GuardDuty vs AWS WAF

* **GuardDuty** detects suspicious behavior.
* **AWS WAF** filters and blocks unwanted web traffic to web applications.

Easy way to remember:

* **GuardDuty = detection**
* **WAF = filtering/blocking web requests**

### GuardDuty vs AWS CloudTrail

* **GuardDuty** analyzes activity and creates threat findings.
* **CloudTrail** records API activity for auditing and tracking.

Easy way to remember:

* **CloudTrail records actions**
* **GuardDuty analyzes for threats**

## Common exam traps

### Trap 1: Thinking GuardDuty prevents attacks automatically

GuardDuty mainly **detects** and **alerts**.

It is not mainly described as a service that directly blocks attacks.

### Trap 2: Confusing GuardDuty with Inspector

Inspector looks for vulnerabilities and exposure.

GuardDuty looks for suspicious activity and active threats.

### Trap 3: Confusing GuardDuty with CloudTrail

CloudTrail logs API calls.

GuardDuty uses security-related data and analysis to identify suspicious behavior.

### Trap 4: Confusing GuardDuty with Security Hub

Security Hub is a central dashboard for security posture and findings.

GuardDuty is one of the services that can feed findings into it.

### Trap 5: Thinking GuardDuty is a person or AWS support team

GuardDuty is a **managed AWS security service**, not a human advisor or support plan.

## Easy real-world example

Imagine a company stores application data in AWS.

One day, an attacker uses stolen credentials and starts making unusual requests from a suspicious location. At the same time, there is strange access behavior around the company’s AWS resources.

GuardDuty notices the unusual activity, analyzes it as potentially malicious, and generates a finding.

The security team then investigates and responds.

So in simple words:
**GuardDuty is the alarm system that notices suspicious behavior.**

## Final summary

Amazon GuardDuty is a fully managed AWS threat detection service.

It continuously monitors your AWS environment, uses machine learning and threat intelligence, and creates findings when it detects suspicious or malicious activity.

For the exam, remember this main idea:
**GuardDuty detects threats; it does not mainly act as a blocking firewall, logging service, or vulnerability scanner.**

## Short exam answer

Amazon GuardDuty is a fully managed threat detection service that continuously monitors AWS accounts, workloads, and data sources to identify suspicious activity and generate security findings.

## Memory trick

**GuardDuty = “Guard on Duty.”**

A guard watches, notices danger, and raises an alert.

That is exactly how to remember GuardDuty:

* **Guard** = security watcher
* **Duty** = always on duty, always monitoring
