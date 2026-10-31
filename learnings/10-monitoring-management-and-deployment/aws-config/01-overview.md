# AWS Config

## Simple definition

AWS Config is an AWS service that records the configuration of your AWS resources, tracks how they change over time, and checks whether those resources follow rules you define.

## Core idea in plain English

Think of AWS Config as a configuration history tracker and compliance checker for your AWS environment.

It helps you answer questions like

 What did this resource look like before
 Who changed it
 Is it configured the way my company wants
 Which resources are non-compliant

AWS Config is about visibility, history, auditing, and compliance.

## Main use cases

### 1. Track resource changes

AWS Config records changes to supported AWS resources over time.

Example You can see when a security group was modified and what changed.

### 2. Audit compliance

You can create AWS Config Rules to check whether resources meet company or security standards.

Example Check whether S3 buckets are publicly accessible.

### 3. Troubleshooting

If something breaks after a change, AWS Config helps you look back at the configuration history.

### 4. Governance at scale

Large organizations use AWS Config to monitor many accounts and Regions for policy compliance.

### 5. Security and operational monitoring

It helps security and operations teams spot risky or incorrect settings.

## Key features

 Configuration recording for supported AWS resources
 Configuration history to see past states of resources
 Configuration snapshots for point-in-time views
 AWS Config Rules to evaluate compliance
 Managed rules provided by AWS
 Custom rules for your own checks
 Compliance dashboard showing compliant and non-compliant resources
 Resource relationships to understand how resources connect
 Conformance Packs to group rules and remediation actions
 Multi-account and multi-Region visibility with aggregators

## How it works

### Step 1 AWS Config records resource configurations

AWS Config watches supported resources in your account and records their configuration details.

This creates a history of how resources looked over time.

### Step 2 Changes are stored

When a supported resource changes, AWS Config creates a new configuration record.

This lets you compare the old and new versions.

### Step 3 Rules evaluate compliance

AWS Config Rules check whether resources follow your desired settings.

Examples

 EBS volumes should be encrypted
 Security groups should not allow unrestricted SSH access
 IAM password policy should meet company requirements

### Step 4 Compliance results are shown

AWS Config marks resources as

 Compliant
 Non-compliant
 Not applicable

### Step 5 Optional remediation

You can combine AWS Config with Systems Manager Automation or other tools to help fix non-compliant resources.

## Why it is important for the exam

AWS Cloud Practitioner questions often test whether you can identify the AWS service used for

 Recording configuration changes
 Auditing resource settings
 Checking compliance against rules
 Viewing configuration history

This is exactly what AWS Config does.

A common exam pattern is

 “Which service helps assess, audit, and evaluate the configurations of AWS resources”

The answer is AWS Config.

## Related AWS services and differences

### AWS Config vs CloudTrail

 AWS Config records what the resource configuration is and how it changes over time.
 CloudTrail records API activity and user actions in the account.

Easy memory rule

 Config = what changed in the resource
 CloudTrail = who did the action and when

### AWS Config vs CloudWatch

 AWS Config focuses on resource configuration and compliance
 CloudWatch focuses on metrics, logs, alarms, and performance monitoring

### AWS Config vs Security Hub

 AWS Config evaluates resources against configuration rules
 Security Hub gives a broader security posture view by bringing findings together from multiple services

### AWS Config vs AWS Trusted Advisor

 AWS Config continuously checks configuration compliance using rules
 Trusted Advisor gives best-practice recommendations related to cost, security, fault tolerance, performance, and service limits

### AWS Config vs AWS Systems Manager

 AWS Config detects and evaluates configuration state
 Systems Manager helps manage and automate operational tasks on resources

## Common exam traps

### Trap 1 Mixing up AWS Config and CloudTrail

If the question asks

 “Who made the API call” → CloudTrail
 “What is the current or past configuration of the resource” → AWS Config

### Trap 2 Mixing up compliance and monitoring

If the question is about

 performance metrics, CPU, memory, alarms → CloudWatch
 policy compliance and configuration history → AWS Config

### Trap 3 Thinking AWS Config prevents changes

AWS Config mainly records, evaluates, and reports.
It does not automatically prevent all bad changes by itself.

### Trap 4 Forgetting that rules can be managed or custom

AWS gives you managed rules, but you can also create custom ones for your own policies.

### Trap 5 Assuming it is only for security

AWS Config helps with security, but also with auditing, operations, governance, and troubleshooting.

## Easy real-world example

A company has a rule that no security group should allow SSH access from the entire internet (`0.0.0.00`).

AWS Config checks security groups against that rule.
If one becomes too open, AWS Config marks it as non-compliant.

The team can then investigate or automatically remediate it.

## Final summary

AWS Config helps you record resource configurations, track configuration changes, view history, and evaluate compliance using rules.

For the exam, remember it as the AWS service for configuration auditing and compliance checking.

If CloudTrail tells you who did something, AWS Config tells you what the resource looked like and whether it follows policy.

## Short exam answer

AWS Config is the AWS service that records resource configurations, tracks configuration changes over time, and evaluates resources against compliance rules.

## Memory trick

Config = Configuration + Compliance

Say it like this

 AWS Config checks if my AWS setup is configured correctly and stays compliant.
