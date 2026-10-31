# AWS customer managed policies

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

## Simple definition

Customer managed policies are IAM policies that you create and manage in your own AWS account.

They are standalone JSON permission documents that you can attach to IAM users, groups, and roles.

---

## Core idea in plain English

Think of a customer managed policy as a custom permission template you build yourself.

AWS gives you the IAM system, but you decide exactly what access rules go inside the policy.

Then, instead of writing the same permissions again and again for different users or roles, you create the policy once and attach it wherever needed.

So the big idea is

Create your own reusable permission policy and manage it centrally.

---

## Main use cases

### 1. Give custom access to a team

A company wants developers to view EC2 and S3, but not delete anything.

### 2. Reuse the same permissions for many identities

You want the same permission set for several IAM users, groups, or roles.

### 3. Follow least privilege

You want to allow only the exact actions that are needed.

### 4. Customize beyond AWS managed policies

AWS managed policies may be too broad, so you create a narrower policy for your own environment.

### 5. Standardize permissions across the account

You want the same rule set used consistently across many IAM identities.

---

## Key features

 Created by you in your AWS account
 Managed by you, not by AWS
 Reusable across multiple IAM users, groups, and roles
 Standalone policy with its own identity in IAM
 Editable whenever you need to update permissions
 Written in JSON
 Helps enforce least privilege

---

## How it works

1. You create a policy document in JSON.
2. Inside the policy, you define

    Effect Allow or Deny
    Action what API calls are allowed or denied
    Resource which AWS resources are affected
    sometimes Condition extra rules such as IP, MFA, tags, or time
3. AWS stores that policy as a standalone managed policy in your account.
4. You attach it to an IAM user, group, or role.
5. When that identity makes a request, AWS evaluates the policy and decides whether access is allowed.

---

## Why it is important for the exam

For the Cloud Practitioner exam, you must clearly know the difference between

 AWS managed policies
 Customer managed policies
 Inline policies

This topic is tested because it connects to security, permissions, least privilege, and IAM best practices.

The exam often checks whether you understand that customer managed policies are

 customized by the customer
 reusable
 centrally managed
 usually better than inline policies when the same permissions are needed more than once

---

## Related AWS services and differences

### IAM

IAM is the service that uses these policies.

Customer managed policies are one way IAM permissions are assigned.

### AWS managed policies vs customer managed policies

AWS managed policies are created and maintained by AWS.

Customer managed policies are created and maintained by you.

Use AWS managed policies when you want quick, general permissions.

Use customer managed policies when you need more control.

### Inline policies vs customer managed policies

Inline policies are attached directly to only one user, group, or role.

They are not designed for reuse.

Customer managed policies are separate standalone policies that can be attached to multiple identities.

### SCPs in AWS Organizations

Service Control Policies (SCPs) are different.

SCPs set the maximum allowed permissions for accounts in an AWS Organization.

They do not directly grant permissions like IAM customer managed policies do.

---

## Common exam traps

### Trap 1 Thinking customer managed policies are the same as inline policies

They are not the same.

Customer managed policies are standalone and reusable.

Inline policies are one-to-one.

### Trap 2 Thinking AWS managed policies are always best

AWS managed policies are convenient, but they can be broader than needed.

Customer managed policies are better when you need custom least-privilege access.

### Trap 3 Confusing “managed” with “managed by AWS” only

A managed policy can be either

 AWS managed, or
 customer managed

So “managed” does not automatically mean AWS created it.

### Trap 4 Forgetting central change management

If one customer managed policy is attached to many identities, updating the policy updates permissions for all attached identities.

### Trap 5 Thinking policies grant access by themselves without attachment

A policy must be attached to a user, group, or role to affect permissions.

---

## Easy real-world example

A company has 20 support employees.

They need to

 view EC2 instances
 view S3 buckets
 read CloudWatch logs
 but not delete resources

Instead of creating separate permissions for each employee, the admin creates one customer managed policy called `SupportReadOnlyCustom`.

Then the admin attaches it to a group called `SupportTeam`.

Now everyone in that group gets the same controlled permissions.

If the company later wants to add read access to RDS, the admin edits the policy once, and everyone using it gets the update.

---

## Final summary

Customer managed policies are custom IAM managed policies created by you inside your AWS account.

They are reusable, editable, and centrally managed.

They are very useful when AWS managed policies are too broad and when inline policies are too limited.

For the exam, remember this idea

Customer managed policies give you custom, reusable permission control.

---

## Short exam answer

Customer managed policies are IAM policies created and administered by the customer in their own AWS account. They are reusable managed policies that can be attached to multiple users, groups, or roles.

---

## Memory trick

Customer managed = customer makes it, customer manages it.

Also remember

 AWS managed = made by AWS
 Customer managed = made by you
 Inline = built directly into one identity

A simple memory line

“Custom and reusable Customer managed.”

## Additional Distinct Source Material

## 🔄 Related AWS Services & Differences

### The 3 Types of IAM Policies — Side by Side

 Feature  AWS Managed Policy  Customer Managed Policy  Inline Policy
------------------------------------------------------------------
 Who creates it  AWS  YOU  YOU
 Reusable  ✅ Yes  ✅ Yes  ❌ No (1-to-1 only)
 Versioning  ❌ No  ✅ Yes (up to 5)  ❌ No
 Customizable  ❌ Limited  ✅ Fully  ✅ Fully
 Best for  Quick setup  Fine-grained control  Special one-off cases
 Recommended  For beginners  ✅ Best practice  Only when necessary

### Related Services to Know
- IAM (Identity and Access Management) — where all policies live
- AWS Organizations — use SCPs (Service Control Policies) alongside IAM policies
- CloudTrail — logs all policy-related actions for auditing
- AWS Config — checks if your policies comply with rules

---

## 🔑 Quick Revision Checklist

- [ ] I know what a Customer Managed Policy is
- [ ] I can explain the difference between the 3 policy types
- [ ] I understand least privilege
- [ ] I know policies can be attached to users, groups, and roles
- [ ] I know Customer Managed Policies support up to 5 versions
- [ ] I can recognize exam traps about policy types

---

📚 Study Tip When you see most control, customizable, or reusable policy in an exam question — think Customer Managed Policy!

---
