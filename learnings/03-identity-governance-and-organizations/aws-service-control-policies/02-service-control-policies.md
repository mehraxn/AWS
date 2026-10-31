# Service Control Policy (SCP) 

## Simple definition

A **Service Control Policy (SCP)** is a policy in **AWS Organizations** that sets the **maximum permissions** available for member accounts in an organization.

It is a **guardrail**, not a permission grant.

---

## Core idea in plain English

Think of an SCP like a **company-wide rulebook** for AWS accounts.

Even if a user, role, or even the root user inside a member account has an IAM policy that says **Allow**, the action can still be blocked if the SCP does not allow it or explicitly denies it.

So SCPs do **not** give access.
They only control the **outer boundary** of what accounts in the organization are allowed to do.

A very important memory line is:

**IAM gives permissions. SCP limits permissions.**

---

## Main use cases

### 1. Blocking dangerous services or actions

A company can use SCPs to stop accounts from performing risky actions.

For example, the company may want to block actions like deleting CloudTrail logs, turning off GuardDuty, or disabling security monitoring tools. This helps protect the environment from accidental or malicious changes.

### 2. Restricting AWS Regions

A company may allow workloads to run only in approved Regions.

This is useful for compliance, data residency, governance, or cost control. An SCP can stop users from launching resources in Regions the company does not approve.

### 3. Enforcing company-wide security rules

SCPs help a central security team apply the same restrictions across many AWS accounts.

Instead of configuring each account one by one, the organization can attach one SCP to an OU and make the rule apply to all accounts inside that OU.

### 4. Preventing accidental changes

An SCP can block sensitive administrative actions even if someone has broad permissions inside an account.

For example, a company may want to stop teams from deleting backup settings, changing audit configurations, or disabling encryption-related controls.

### 5. Controlling sandbox or junior-admin accounts

Some accounts are used for testing, learning, or temporary projects.

With SCPs, the company can limit what those accounts are allowed to do, such as blocking expensive services, preventing production-like changes, or restricting admin-level actions.

### 6. Standardizing governance across many accounts

Large companies often have many AWS accounts for development, production, security, billing, and shared services.

SCPs help apply one central governance model across all of them, which is a very common multi-account AWS design pattern.

---

## Key features

### 1. Works with AWS Organizations

SCPs are a feature of **AWS Organizations**.

They are not standalone IAM policies. If there is no AWS Organization, there is no SCP use case.

### 2. Applies to roots, OUs, and accounts

You can attach SCPs at different levels:

* the **root** of the organization
* an **Organizational Unit (OU)**
* or a specific **member account**

This gives you flexibility in how broadly you want the rule to apply.

### 3. Sets the maximum available permissions

This is the most important feature.

An SCP defines the **maximum permission boundary** for member accounts. Even if IAM inside the account says **Allow**, the action still fails if the SCP does not allow it.

### 4. Does not grant permissions

An SCP never gives access by itself.

If a user needs access to Amazon S3, EC2, or any other service, they still need an IAM policy or role in their own account that grants that access.

### 5. Uses JSON syntax similar to IAM

SCPs use a JSON format that looks similar to IAM policies.

This makes them easier to recognize in exam questions, but you must remember that their job is different from IAM policies.

### 6. Can use explicit deny rules

An explicit **Deny** in an SCP is very powerful.

If the SCP explicitly denies an action, that action is blocked for affected accounts even if IAM permissions inside the account allow it.

### 7. Inherits through the organization structure

If an SCP is attached to the root or an OU, child OUs and member accounts under that path are affected.

This inheritance is important because one policy can impact many accounts at once.

### 8. Affects member-account principals broadly

SCPs affect principals in member accounts, including IAM users, IAM roles, and the member account root user.

This is why SCPs are considered strong organization-level guardrails.

### 9. Supports central governance at scale

SCPs are especially useful when a business has many AWS accounts.

They reduce the need to manually enforce the same restriction in every single account.

---

## How it works

### Step 1. Create an organization

You first use **AWS Organizations** to manage multiple AWS accounts under one structure.

### Step 2. Organize accounts into OUs

You can group accounts into Organizational Units such as:

* Production
* Development
* Security
* Sandbox

This makes it easier to apply different rules to different groups of accounts.

### Step 3. Attach an SCP

You attach the SCP to:

1. the organization root,
2. an OU,
3. or a specific member account.

The level you choose determines how widely the SCP applies.

### Step 4. AWS evaluates access requests

When a principal in a member account tries to perform an action, AWS evaluates:

1. the IAM permissions inside that account,
2. and the SCP restrictions from AWS Organizations.

The action works only if it is allowed by IAM **and** not blocked by the SCP.

### Very important rule

An SCP **never grants permission by itself**.

So this statement is wrong:

> “I attached an SCP, so now the user can access S3.”

That is incorrect because the user still needs IAM permission inside the account.

---

## Why it is important for the exam

SCP is important because AWS exam questions often test whether you understand the difference between:

* **granting permissions**
* and **limiting permissions**

This is one of the most common exam traps.

You should remember these points very clearly:

1. SCPs are part of **AWS Organizations**.
2. SCPs are used for **multi-account governance**.
3. SCPs do **not** grant permissions.
4. SCPs define the **maximum allowed permissions**.
5. IAM permissions inside the account are still needed.
6. SCPs are mainly used for **central control at scale**.

---

## Related AWS services and differences

### 1. AWS Organizations vs SCP

**AWS Organizations** is the overall service used to manage multiple AWS accounts.

An **SCP** is one type of policy used inside AWS Organizations.

So the relationship is:

* **Organizations** = the multi-account management service
* **SCP** = the guardrail policy inside that service

### 2. IAM policies vs SCP

This is the most important comparison.

**IAM policies**:

* grant or deny permissions to users, groups, or roles
* work inside one AWS account
* are used for day-to-day access control

**SCPs**:

* do not grant permissions
* set the outer permission limit for member accounts
* are used for central governance across multiple accounts

Easy memory line:

**IAM = what a principal can do**

**SCP = the maximum that account principals are allowed to do**

### 3. Permission boundaries vs SCP

Students often mix these up because both are limits.

**Permission boundaries**:

* limit a specific IAM user or role
* work inside one account

**SCPs**:

* limit all principals in member accounts
* work at the organization, OU, or account level

### 4. IAM Identity Center vs SCP

**IAM Identity Center** helps users sign in and access AWS accounts and applications.

**SCP** does not manage sign-in. It only limits what actions are allowed after access already exists.

### 5. AWS Control Tower vs SCP

**AWS Control Tower** helps set up and govern a multi-account environment.

It uses AWS Organizations in the background and may use guardrails based on organization controls. SCPs are one of the tools that can support that governance model.

### 6. AWS Config vs SCP

**AWS Config** records and evaluates resource configurations.

**SCP** prevents certain actions from happening at the permission level.

So:

* **Config** = detect and assess compliance
* **SCP** = prevent certain actions

---

## Common exam traps

### 1. Thinking SCP grants permissions

This is the biggest trap.

An SCP never gives a user or role access to a service. It only limits what could be allowed. The user still needs IAM permissions.

### 2. Confusing SCP with IAM policy

IAM policies are attached to users, groups, and roles.

SCPs are attached to the organization root, OUs, or accounts. So the scope and purpose are different.

### 3. Thinking SCP is only for one user

SCP is not designed for one individual user.

It works at the organization structure level and affects principals broadly inside member accounts.

### 4. Forgetting the multi-account context

If the question mentions **many AWS accounts**, **central governance**, **organization-wide restriction**, or **OU-based control**, SCP should come to your mind quickly.

### 5. Thinking SCP replaces IAM

It does not replace IAM.

You still need IAM roles, users, and policies inside each account for actual access management.

### 6. Forgetting that SCP can affect the member account root user

Exam questions may try to trick you into thinking the root user escapes SCP restrictions.

For member accounts, SCPs can still limit what the root user can do.

### 7. Confusing SCP with compliance or auditing tools

SCP is about **prevention**.

It is not mainly for auditing, logging, recording history, or checking resource configuration. Services like AWS Config or CloudTrail are used for those purposes.

### 8. Choosing SCP when the problem is only inside one account

If the scenario is about controlling one user, one team, or one role inside a single account, IAM is often the better answer, not SCP.

### 9. Missing words like “maximum permissions”

In AWS exam questions, phrases like **maximum available permissions**, **guardrail**, **member accounts**, or **AWS Organizations** strongly suggest SCP.

---

## Easy real-world example

A company has **50 AWS accounts**.

The security team wants to make sure nobody in development accounts can disable security services or launch resources in unapproved Regions.

They create an OU called **Development** and attach an SCP to that OU.

Now even if a developer has broad IAM permissions inside one development account, AWS still blocks the actions that the SCP restricts.

This gives the company one central control across many accounts.

---

## AWS exam key words for SCP

These are the words and phrases that often point to SCP in AWS exam questions:

### 1. Multi-account governance

This usually suggests AWS Organizations and centralized control.

### 2. Maximum permissions

This is one of the strongest SCP clues.

### 3. Guardrails

AWS often describes SCPs as permission guardrails.

### 4. AWS Organizations

If the question directly mentions AWS Organizations, SCP becomes much more likely.

### 5. Organizational Units (OUs)

If the question talks about applying a rule to an OU, SCP is a top candidate.

### 6. Centralized restriction across accounts

This strongly suggests SCP rather than IAM.

### 7. Restrict services or Regions

Questions about blocking certain services or limiting Region usage often point to SCP.

### 8. Member accounts

This phrase is very important because SCP is mainly about organization member accounts.

### 9. Deny actions across all accounts in a group

That kind of large-scope control is a classic SCP use case.

### 10. Do not grant permissions

If the exam asks for something that limits but does not grant access, SCP is a strong answer.

### 11. Root, OU, or account attachment

These attachment points are strong hints that the question is about SCP.

### 12. Central security policy

When one central security team wants to control many accounts, think of SCP.

---

## If I were an examiner ...

Here are the kinds of things I would ask about SCP in the exam.

### 1. Do you know what SCP really does?

I may ask which AWS feature sets the **maximum available permissions** for accounts in AWS Organizations.

### 2. Do you know that SCP does not grant permissions?

I may give a scenario where a user still cannot access a service even though an SCP exists. The correct idea is that the user still needs IAM permission.

### 3. Can you choose between IAM and SCP?

If the problem is about one user in one account, IAM is usually the better answer. If the problem is about many accounts and central governance, SCP is usually the better answer.

### 4. Can you identify the multi-account governance use case?

If the company wants one restriction applied across many AWS accounts, I would expect you to think of AWS Organizations with SCPs.

### 5. Do you understand prevention versus auditing?

If the question is about **preventing actions**, SCP may fit. If it is about **recording, auditing, or checking configuration**, another service such as AWS Config or CloudTrail may fit better.

### 6. Can you spot misleading wording?

If an answer choice says “grant permissions across all accounts,” that is suspicious because SCP does not grant permissions.

### 7. Can you recognize attachment scope?

If the question mentions attaching a policy to the root, an OU, or an account, I may be testing whether you recognize SCP behavior.

---

## Final summary

A **Service Control Policy (SCP)** is a central permission guardrail used with **AWS Organizations**.

It helps companies control what AWS accounts in the organization are allowed to do.

It is especially useful in **multi-account environments** where a central team wants to apply security or compliance restrictions across many accounts.

The most important thing to remember is this:

**SCP does not grant permissions. It only limits the maximum permissions.**

IAM policies are still needed to actually allow actions.

---

## Short exam answer

A **Service Control Policy (SCP)** is an AWS Organizations policy that sets the **maximum permissions** for member accounts in an organization. It is used for **central governance across multiple accounts** and **does not grant permissions by itself**.

---

## Memory trick

Remember this:

**SCP = Security Ceiling Policy**

It acts like a ceiling above the account.
Even if IAM says yes, the principal cannot go above the ceiling.

Another easy memory line:

**IAM gives. SCP limits.**
