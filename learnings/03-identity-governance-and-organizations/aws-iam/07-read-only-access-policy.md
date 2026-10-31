# ReadOnlyAccess

## Simple definition

ReadOnlyAccess is an AWS managed IAM policy that gives permission to view AWS services and resources without allowing changes.

In simple words it lets someone look, but not edit.

---

## Core idea in plain English

Think of ReadOnlyAccess like giving a person a visitor pass to your AWS account.

They can open the dashboard, inspect settings, check resources, and read information.
But they should not be able to create, delete, or modify resources.

This is useful when someone needs visibility into AWS but should not be allowed to make changes.

---

## Main use cases

### 1. Auditors and reviewers

A company may want an auditor to inspect resources and settings without changing anything.

### 2. Managers or team leads

A manager may need to see billing-related resources, architectures, or service usage without operating the environment.

### 3. Support and troubleshooting observation

A team member may need to investigate what exists in the account before requesting changes from an admin.

### 4. Training and learning

A beginner can safely explore an AWS environment without the risk of accidentally deleting or changing resources.

---

## Key features

 AWS managed policy maintained by AWS
 Grants read-only access across many AWS services
 Can be attached to IAM users, groups, and roles
 Easier than writing a large custom read-only policy yourself
 AWS updates it over time as services change

---

## How it works

When you attach ReadOnlyAccess to an IAM identity, AWS allows that identity to perform actions that read or list information.

Examples include actions such as

 viewing resources
 listing services or objects
 describing configurations
 checking status and metadata

But it should not allow actions that

 create resources
 update settings
 delete resources
 manage permissions

AWS checks the permissions in the policy whenever the user or role tries to do something.
If the action is read-only, it is usually allowed.
If the action would change something, it is usually denied unless another policy allows it.

---

## Why it is important for the exam

This is important because AWS exam questions often test whether you understand the difference between

 viewing resources
 managing resources
 managing permissions

For the exam, remember this idea

ReadOnlyAccess = visibility without modification.

It is a classic IAM permissions question.

---

## Related AWS services and differences

### ReadOnlyAccess vs AdministratorAccess

 ReadOnlyAccess can view resources
 AdministratorAccess can do almost everything in the account

### ReadOnlyAccess vs PowerUserAccess

 ReadOnlyAccess view only
 PowerUserAccess can use many AWS services, but has limited IAMorganization permission management

### ReadOnlyAccess vs IAMReadOnlyAccess

 ReadOnlyAccess read-only across many AWS services
 IAMReadOnlyAccess read-only mainly for IAM

### ReadOnlyAccess vs custom IAM policy

 ReadOnlyAccess quick and broad, managed by AWS
 Custom policy more precise and follows least privilege better when you only want access to specific services

---

## Common exam traps

### Trap 1 Thinking read-only means no risk

Read-only access still lets a user see information. That can include useful or sensitive operational details.

### Trap 2 Confusing read-only with limited admin access

Read-only does not mean the user can restart, delete, update, or deploy resources.

### Trap 3 Forgetting that it is AWS managed

Because it is an AWS managed policy, AWS maintains it. You do not manually manage every permission inside it.

### Trap 4 Assuming it is the best least-privilege option

For real production security, a custom policy is often better if the user only needs to view one service, such as S3 or EC2.

### Trap 5 Ignoring policy combinations

If another attached policy grants write permissions, then the identity may do more than read-only. IAM permissions are evaluated together.

---

## Easy real-world example

A company hires an external security consultant to review its AWS setup.

The consultant needs to

 inspect EC2 instances
 check S3 buckets
 review VPC settings
 look at CloudWatch dashboards

But the company does not want the consultant to change anything.

So the company attaches ReadOnlyAccess to a role and lets the consultant assume that role.

That way, the consultant can examine the environment safely.

---

## Final summary

ReadOnlyAccess is an AWS managed IAM policy that allows users, groups, or roles to view AWS resources and configurations without making changes.

It is commonly used for auditors, observers, learners, and anyone who needs visibility but not control.

For the Cloud Practitioner exam, the main thing to remember is

It is for reading, not doing.

---

## Short exam answer

ReadOnlyAccess is an AWS managed IAM policy that provides read-only access to AWS services and resources, allowing users to view but not modify them.

---

## Memory trick

ReadOnlyAccess = “See everything, change nothing.”

Think of it like a museum visitor

 you can walk around
 you can look closely
 you cannot touch the exhibits
