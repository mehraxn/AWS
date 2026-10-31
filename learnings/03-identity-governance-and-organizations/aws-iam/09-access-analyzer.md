# AWS IAM Access Analyzer 

## Simple definition

AWS IAM Access Analyzer is a security feature in AWS Identity and Access Management (IAM) that helps you find who can access your AWS resources and whether that access is too broad, external, or unused.

It is used to analyze permissions, not to create users or run applications.

---

## Core idea in plain English

Think of IAM Access Analyzer like a security reviewer for permissions.

It looks at your policies and access settings and helps answer questions like

 Is this S3 bucket shared with people outside my account
 Does this KMS key allow external access
 Does this IAM role have permissions it never uses
 Is this policy too wide or risky

So the main idea is

“Check access before it becomes a security problem.”

---

## Main use cases

IAM Access Analyzer is mainly used to

 Find external access to AWS resources
 Find internal access paths to important resources
 Find unused access for IAM users and roles
 Validate IAM policies before using them
 Help create least-privilege policies based on actual activity

---

## Key features

### 1. External access findings

It can identify resources that are shared with principals outside your AWS account or AWS Organization.

Example resources include things like

 Amazon S3 buckets
 AWS KMS keys
 Amazon SQS queues
 AWS Secrets Manager secrets
 Amazon ECR repositories
 Amazon SNS topics

This is one of the most important exam ideas.

### 2. Internal access findings

It can help identify possible access paths from IAM users or roles inside your environment to selected resources.

This helps security teams understand who inside the organization might reach sensitive resources.

### 3. Unused access findings

It can find

 Unused IAM roles
 Unused IAM user passwords
 Unused IAM user access keys
 Permissions that were granted but not used

This helps reduce overly broad permissions.

### 4. Policy validation

It checks IAM policies for

 Errors
 Security warnings
 General warnings
 Suggestions
 AWS best-practice issues

This helps catch risky or broken policies before deployment.

### 5. Policy generation

It can review AWS CloudTrail activity and help generate a more precise IAM policy based on what a user or role actually used.

This is useful for moving toward least privilege.

---

## How it works

At a high level, IAM Access Analyzer works like this

1. You create an analyzer.
2. AWS analyzes supported policies and access settings.
3. It produces findings when it detects external, internal, or unused access.
4. You review the findings.
5. You then fix or refine the permissions yourself.

Important exam point

IAM Access Analyzer finds and reports problems. It does not automatically fix them for you.

---

## Why it is important for the exam

For the Cloud Practitioner exam, IAM Access Analyzer matters because AWS often tests whether you understand the difference between

 granting access versus analyzing access
 monitoring permissions versus enforcing permissions
 least privilege versus overly broad permissions

IAM Access Analyzer supports the security best practice of least privilege by helping you discover access that is

 unintended
 too broad
 external
 no longer needed

If a question says something like

 “identify resources shared publicly or cross-account”
 “review unused permissions”
 “validate policies before deployment”
 “refine permissions based on actual usage”

then IAM Access Analyzer should be on your shortlist.

---

## Related AWS services and differences

### IAM

 IAM controls who can do what in AWS.
 IAM Access Analyzer reviews and checks whether those permissions create risky or unnecessary access.

Easy way to remember

 IAM = grants and manages access
 IAM Access Analyzer = inspects and evaluates access

### IAM Policy Simulator

 IAM Policy Simulator tests what a policy would allow for a specific user, group, or role.
 IAM Access Analyzer looks for risky access patterns, unused access, and policy issues.

### AWS Organizations

 AWS Organizations groups and centrally manages multiple AWS accounts.
 IAM Access Analyzer can use an organization as the trusted zone when checking for external access.

### AWS CloudTrail

 CloudTrail records API activity.
 IAM Access Analyzer can use CloudTrail activity to help generate more precise policies.

### AWS Security Hub

 Security Hub centralizes security findings.
 IAM Access Analyzer findings can be sent to Security Hub.

### AWS Config

 AWS Config tracks resource configuration changes and compliance.
 IAM Access Analyzer focuses on permission analysis and access findings.

---

## Common exam traps

### Trap 1 Thinking it grants permissions

It does not grant permissions.

IAM policies, roles, users, and groups grant permissions.

### Trap 2 Thinking it automatically fixes issues

It does not automatically remediate access.

It finds issues, and then you review and fix them.

### Trap 3 Confusing it with CloudTrail

CloudTrail records actions.

IAM Access Analyzer analyzes permissions and can use CloudTrail data for policy generation.

### Trap 4 Confusing it with Security Hub

Security Hub aggregates security findings from multiple services.

IAM Access Analyzer is the service that creates specific access-related findings.

### Trap 5 Assuming it is only for S3

It supports multiple AWS resource types, not just S3 buckets.

### Trap 6 Missing the least-privilege angle

A common exam clue is “reduce permissions to only what is needed.”

That points strongly to IAM Access Analyzer policy generation or unused access analysis.

### Trap 7 Forgetting Region behavior

For external access analysis, IAM Access Analyzer analyzes supported resources in the Region where it is enabled.

So if resources exist in multiple Regions, analyzers may be needed in multiple Regions.

---

## Easy real-world example

Imagine a company stores private reports in an Amazon S3 bucket.

A developer accidentally changes the bucket policy so another AWS account can read the data.

IAM Access Analyzer detects that the bucket is accessible from outside the trusted account or organization and creates a finding.

The security team reviews the finding and fixes the bucket policy.

That is exactly the kind of problem IAM Access Analyzer is built to help detect.

---

## Final summary

AWS IAM Access Analyzer helps you understand whether access in your AWS environment is

 external
 internal
 unused
 overly broad
 risky

It is a permission analysis and least-privilege support tool.

It helps you

 detect unintended sharing
 validate policies
 reduce unused permissions
 generate more precise policies from real usage

Most importantly for the exam

IAM Access Analyzer analyzes access. IAM itself grants and manages access.

---

## Short exam answer

AWS IAM Access Analyzer is a tool that helps identify external, internal, and unused access to AWS resources and helps validate and refine IAM policies for least privilege.

---

## Memory trick

### “Analyzer does not allow — it audits access.”

Or even shorter

### Access Analyzer = checks access, not creates access

That memory trick helps avoid the biggest exam mistake.

---

## Extra exam coach note

If the question asks

 Who should have access → think IAM
 Does someone have too much access → think IAM Access Analyzer
 What actions actually happened → think CloudTrail
 Where are security findings collected → think Security Hub

That separation is very useful in exam questions.
