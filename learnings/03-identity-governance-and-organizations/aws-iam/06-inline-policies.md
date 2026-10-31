# IAM Inline Policy

## Simple definition

An **IAM inline policy** is a policy written directly inside **one IAM user, group, or role**.

It gives permissions only to that single identity and stays attached only to that identity.

---

## Core idea in plain English

Think of an inline policy like a **special note glued to one person’s file**.

It is made for **one specific user, group, or role**.
You do **not reuse it** somewhere else.
If that identity is deleted, the inline policy is deleted too.

Important: **inline policy does not mean one-time use**. It can be used again and again by that same identity until you remove it or change it.

---

## Main use cases

### 1. Giving one role a unique permission

Sometimes one IAM role needs a permission that no other role needs.

Example: one special audit role can read a certain S3 path, but no other role should have that access.

### 2. Giving one user a custom exception

A company may have standard permissions for most users, but one person may need an extra action.

Example: one finance employee needs permission to view a billing report.

### 3. Adding a special permission to one group only

A group might need one custom permission that is not useful anywhere else.

Example: one operations group needs permission to restart a specific EC2 instance.

### 4. Keeping a strict one-to-one relationship

Some companies want the permission to stay tightly tied to one identity only.

This helps when the permission is very specific and should not be reused by mistake.

---

## Key features

### 1. Attached to only one IAM identity

An inline policy belongs to **one user, one group, or one role** only.

It is not shared across multiple identities.

### 2. Can be used with users, groups, or roles

Inline policies are not only for users.

They can be attached to:

* IAM users
* IAM groups
* IAM roles

### 3. Not reusable

Unlike managed policies, an inline policy is **not a separate reusable IAM object**.

It lives directly inside the identity.

### 4. Deleted with the identity

If you delete the user, group, or role, the inline policy disappears too.

This is one of the easiest exam points to test.

### 5. Written in JSON

Like most IAM permissions, inline policies use JSON.

They define actions, resources, effects, and sometimes conditions.

### 6. Used for identity-based permissions

An inline policy is attached to an identity, so it tells AWS **what that identity is allowed or denied to do**.

---

## How it works

An inline policy contains JSON that defines:

### 1. Effect

This says whether the policy **Allows** or **Denies** access.

### 2. Action

This says **what operation** the identity can perform.

Examples:

* `s3:GetObject`
* `ec2:StartInstances`
* `dynamodb:PutItem`

### 3. Resource

This says **which AWS resource** the action applies to.

Example: one S3 bucket, one EC2 instance, or one DynamoDB table.

### 4. Condition

Sometimes the policy includes extra rules.

Example: allow access only from a certain IP range or only during a specific time.

AWS evaluates the request against the inline policy together with other IAM rules.

If the action is allowed, and nothing else blocks it with an explicit deny, the request can succeed.

### Simple example

A role could have an inline policy that allows:

* `s3:GetObject`
* on one specific S3 bucket

That means the role can read objects from that bucket only.

---

## Why it is important for the exam

For the AWS Certified Cloud Practitioner exam, the main idea is:

**Inline policy = one identity only**

You should recognize that inline policies are different from managed policies because:

### 1. They are not shared

They are attached to one identity only.

### 2. They are not reusable

You cannot attach the same inline policy object to many users or roles.

### 3. They are best for special cases

They are usually used when permissions are unique and very specific.

### 4. They are deleted with the identity

This is a classic exam detail.

---

## Related AWS services and differences

### IAM Inline Policy vs Customer Managed Policy

#### Inline policy

1. Belongs to one user, group, or role.
2. Cannot be reused across many identities.
3. Deleted with the identity.
4. Good for special one-off permissions.

#### Customer managed policy

1. Created as a separate IAM policy object.
2. Can be attached to many users, groups, and roles.
3. Easier to manage at scale.
4. Better when many identities need the same permissions.

### IAM Inline Policy vs AWS Managed Policy

#### Inline policy

1. Created by you.
2. Embedded directly into one identity.
3. Used for special custom permissions.

#### AWS managed policy

1. Created and maintained by AWS.
2. Reusable across identities.
3. Good for common job roles and AWS access patterns.

### IAM Inline Policy vs Resource-based Policy

#### Inline policy

1. Attached to an identity.
2. Says what that identity can do.

#### Resource-based policy

1. Attached to a resource.
2. Says who can access that resource.
3. Common examples: S3 bucket policy, SNS topic policy, SQS queue policy.

### IAM Inline Policy vs Permissions Boundary

#### Inline policy

1. Grants or denies permissions to the identity.
2. Is part of the identity’s effective permissions.

#### Permissions boundary

1. Sets the maximum permissions an identity can have.
2. Does not itself grant access unless another policy also allows it.
3. Uses a managed policy, not an inline policy.

---

## Common exam traps

### 1. Thinking inline policy means one-time use

That is wrong.

An inline policy keeps working for that same identity until you remove or edit it.

### 2. Thinking inline policies are reusable

That is wrong.

They are tied to one user, group, or role only.

### 3. Confusing inline policies with managed policies

This is very common.

Managed policies are separate IAM objects that can be attached to many identities.
Inline policies live directly inside one identity.

### 4. Thinking inline automatically means more secure

That is not always true.

Inline only describes **how the policy is attached**, not that it is safer by default.

### 5. Forgetting deletion behavior

If the IAM identity is deleted, the inline policy is deleted too.

This is a favorite AWS exam detail.

### 6. Choosing inline policy when many identities need the same access

That is usually the wrong design choice.

If many users or roles need the same permissions, a **customer managed policy** is usually better.

### 7. Mixing identity-based and resource-based policies

An inline policy is identity-based.

It is not the same as an S3 bucket policy or another resource-based policy.

---

## Easy real-world example

A company has one special admin role called `BillingAuditRole`.

This role needs permission to:

1. View billing reports
2. Read one specific S3 folder

No other role needs this exact permission set.

Instead of creating a reusable policy for many identities, the company adds an inline policy directly to that role.

That is a good inline policy use case because the permission is unique to one identity.

---

## Exam keywords you may see

These are words and phrases that may appear in AWS exam questions about inline policies:

### Core keywords

* inline policy
* embedded policy
* one-to-one relationship
* attached directly to user, group, or role
* non-reusable policy
* identity-based policy
* deleted when identity is deleted

### Comparison keywords

* managed policy
* customer managed policy
* AWS managed policy
* reusable
* shared across identities
* central management

### Permission evaluation keywords

* Allow
* Deny
* explicit deny
* JSON policy
* Action
* Resource
* Condition
* least privilege

### Exam clue phrases

* "specific to one role"
* "custom exception for one user"
* "not intended to be reused"
* "deleted automatically with the IAM identity"
* "best for unique permissions"

---

## If I were an examiner, what would I ask?

### 1. What is the biggest difference between an inline policy and a managed policy?

I would expect you to say:

**Inline policy is attached to only one identity and is not reusable. Managed policy is a separate policy object and can be reused across many identities.**

### 2. When is an inline policy a good choice?

I would expect you to say:

**When one specific user, group, or role needs a unique permission set that should not be shared.**

### 3. What happens to an inline policy if the IAM identity is deleted?

I would expect you to say:

**The inline policy is deleted automatically with that identity.**

### 4. Is an inline policy identity-based or resource-based?

I would expect you to say:

**Identity-based.**

### 5. If multiple roles need the same permissions, should you usually choose inline policy?

I would expect you to say:

**No. Usually a customer managed policy is better because it is reusable and easier to manage.**

---

## Final summary

IAM inline policies are identity-based policies embedded directly into **one IAM user, group, or role**.

They are:

1. For one identity only
2. Not reusable
3. Deleted with the identity
4. Best for special or unique permissions

Remember the exam idea:

**Inline = inside one identity**

---

## Short exam answer

An IAM inline policy is a policy embedded directly in a single IAM user, group, or role. It is used for one specific identity, is not reusable across multiple identities, and is deleted when that identity is deleted.

---

## Memory trick

**Inline = in the line of one identity**

So remember:

* **Inline = inside one identity**
* **Managed = shared and reusable**
