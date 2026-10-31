# AWS Organizations

## Simple definition

AWS Organizations is an AWS service that helps you centrally manage multiple AWS accounts.

It allows you to group accounts, apply governance rules across them, and simplify billing from one central place.

---

## Core idea in plain English

Think of AWS Organizations as a control center for many AWS accounts.

Instead of managing each AWS account separately, a company can place accounts inside one organization, group them in a logical structure, and apply rules from the top.

This makes large AWS environments easier to manage, more secure, and more organized.

---

## Main use cases

### 1. Manage many AWS accounts centrally

A company may have many AWS accounts for different teams or projects. AWS Organizations lets the company manage them under one structure instead of treating each account separately.

### 2. Separate environments such as dev, test, and production

Many companies use separate AWS accounts for development, testing, and production. This improves organization and reduces the risk of one environment affecting another.

### 3. Apply central security guardrails

You can use Service Control Policies (SCPs) to limit what accounts are allowed to do. This helps enforce company-wide security rules.

### 4. Use consolidated billing

AWS Organizations allows one management account to view and pay the bills for multiple member accounts. This simplifies cost tracking and financial management.

### 5. Organize accounts by team, department, or business unit

Accounts can be grouped into Organizational Units (OUs). For example, you can group accounts for Finance, Security, and Engineering separately.

### 6. Support a multi-account strategy at scale

Large organizations often need many accounts for better security, governance, and workload separation. AWS Organizations provides the structure to support that strategy.

---

## Key features

### 1. Central account management

One management account can control the overall organization. This makes it easier to manage a large AWS environment from a central place.

### 2. Organizational Units (OUs)

OUs are logical groups of AWS accounts. They help you organize accounts by purpose, environment, department, or project.

### 3. Service Control Policies (SCPs)

SCPs are permission guardrails that define the maximum permissions available in member accounts.

Important exam point: SCPs do **not** grant permissions. They only limit permissions. IAM policies are still needed to allow actions.

### 4. Consolidated billing

You can combine billing across multiple AWS accounts into one payment structure. This makes it easier to track costs and can simplify financial reporting.

### 5. Account creation and account invitation

You can create new AWS accounts directly inside the organization or invite existing AWS accounts to join it.

### 6. Policy application at multiple levels

Policies can be applied at the root level, OU level, or account level. This gives flexible control across the organization.

### 7. Delegated administration

Some AWS services allow you to assign administrative responsibilities to a member account instead of keeping everything only in the management account.

### 8. Integration with other AWS governance services

AWS Organizations works with services such as AWS Control Tower and AWS IAM Identity Center to help build secure and governed multi-account environments.

---

## How it works

1. You begin with one AWS account that becomes the **management account**.
2. You create an **organization**.
3. You add other AWS accounts as **member accounts**.
4. You group accounts into **Organizational Units (OUs)**.
5. You apply policies at the **root**, **OU**, or **account** level.
6. These policies act as guardrails across the accounts in that structure.
7. Billing can also be managed centrally through the organization.

---

## Important terms to know

### Management account

This is the main AWS account that creates and manages the organization.

### Member accounts

These are the AWS accounts that belong to the organization.

### Organizational Units (OUs)

These are folder-like groups used to organize accounts.

### Service Control Policies (SCPs)

These are organization-level guardrails that define the maximum permissions available in member accounts.

Very important exam point: SCPs do **not** grant permissions. They only restrict what IAM users and roles can do.

### Consolidated billing

This is the feature that combines billing and payment across multiple accounts in the same organization.

---

## Why it is important for the exam

AWS Cloud Practitioner questions often test whether you understand:

1. How AWS manages multiple accounts at scale.
2. The difference between AWS Organizations and IAM.
3. The purpose of SCPs.
4. The meaning of consolidated billing.
5. Why companies use a multi-account strategy.

This topic is common in the exam because it connects governance, billing, security, and account structure.

---

## Related AWS services and differences

### AWS Organizations vs IAM

* **AWS Organizations** manages multiple AWS accounts.
* **IAM** manages users, groups, and roles inside a single AWS account.

**Easy rule:**

Need control across many accounts → **AWS Organizations**
Need access control inside one account → **IAM**

### AWS Organizations vs AWS Control Tower

* **AWS Organizations** provides the basic multi-account structure.
* **AWS Control Tower** builds on AWS Organizations and adds automated setup and governance.

**Easy rule:**

Organizations = foundation
Control Tower = managed landing zone on top of the foundation

### AWS Organizations vs Consolidated Billing

* **Consolidated billing** is a feature inside AWS Organizations.
* AWS Organizations is broader because it also includes account grouping, governance, and SCPs.

---

## Common exam traps

### Trap 1: Thinking SCPs grant permissions

This is one of the most common mistakes.

SCPs do **not** give permissions to users or roles. They only define the maximum permissions that can exist in a member account. To actually allow an action, you still need an IAM policy.

### Trap 2: Confusing AWS Organizations with IAM

Students often mix these two services.

IAM is used to control access **inside one AWS account**. AWS Organizations is used to manage and govern **multiple AWS accounts together**.

### Trap 3: Thinking AWS Organizations is only for billing

This is incomplete.

Consolidated billing is an important feature, but AWS Organizations is also about governance, account structure, policy control, and multi-account management.

### Trap 4: Forgetting the role of the management account

Every organization has one management account.

This account is the central account that creates the organization and manages the overall structure. It is important to remember this on the exam.

### Trap 5: Assuming SCPs replace IAM policies

They do not.

SCPs set permission boundaries, but IAM policies are still needed to allow actions. You should think of SCPs as a ceiling, not as direct permission grants.

### Trap 6: Thinking all accounts should stay in one big AWS account

In the real world, AWS best practice is often to separate workloads into multiple accounts.

AWS Organizations exists to make that multi-account approach easier and safer.

---

## Easy real-world example

Imagine a company with separate teams for Development, Security, and Finance.

Instead of putting everything in one AWS account, the company creates separate accounts for:

* Development
* Production
* Security logging
* Billing review

Then the company uses AWS Organizations to:

* Group accounts by purpose
* Apply security guardrails across them
* Keep billing centralized
* Control what each account is allowed to do

This is safer, cleaner, and easier to manage than using one very large AWS account for everything.

---

## AWS exam keywords

These are important words and phrases you may see in the exam:

* AWS Organizations
* Multi-account management
* Management account
* Member account
* Organizational Units (OUs)
* Service Control Policies (SCPs)
* Consolidated billing
* Governance
* Centralized account management
* Guardrails
* Policy inheritance
* Root, OU, and account level
* Delegated administrator
* Multi-account strategy
* Central billing

---

## Final summary

AWS Organizations helps businesses manage multiple AWS accounts from one central place.

It lets you:

* Group accounts
* Apply governance rules
* Use SCPs as permission guardrails
* Combine billing
* Support a secure multi-account setup

For the exam, the most important idea is this:

**AWS Organizations is about multi-account management, governance, and centralized control.**

---

## Short exam answer

AWS Organizations is an AWS service that helps you centrally manage and govern multiple AWS accounts. It supports features such as Organizational Units, Service Control Policies, and consolidated billing.

---

## Memory trick

**Organizations = organize many AWS accounts**

Think of it like this:

* **IAM** = who can do what inside one house
* **AWS Organizations** = how the whole neighborhood of houses is structured and controlled

Simple memory line:

**IAM controls access inside one house; AWS Organizations manages the whole neighborhood.**
