# AWS IAM (Identity and Access Management)

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Simple definition

AWS IAM is the AWS service that helps you control who can access AWS resources and what they are allowed to do.

## Core idea in plain English

Think of IAM as the security guard and permission system for your AWS account.

It answers two big questions

 Who are you
 What are you allowed to do

With IAM, you can create users, groups, and roles, then give them the right permissions.

## Main use cases

IAM is commonly used for

 Giving employees their own AWS login
 Controlling access to services like S3, EC2, and RDS
 Giving applications permission to use AWS services securely
 Allowing temporary access instead of sharing passwords
 Applying security best practices like least privilege
 Managing access for admins, developers, and auditors

## Key features

### 1. Users

An IAM user represents one person or application that needs long-term access to AWS.

A user can have

 A password for the AWS Management Console
 Access keys for the AWS CLI or API

### 2. Groups

A group is a collection of IAM users.

Instead of giving permissions to each user one by one, you can place users in a group and assign permissions to the group.

Example

 Admins group
 Developers group
 ReadOnly group

### 3. Policies

Policies are JSON documents that define permissions.

They say what actions are allowed or denied on which AWS resources.

Example ideas

 Allow reading an S3 bucket
 Allow starting EC2 instances
 Deny deleting databases

### 4. Roles

An IAM role is an identity that AWS services, applications, or users can assume temporarily.

Roles are very important in AWS.

Examples

 An EC2 instance uses a role to access S3
 A Lambda function uses a role to write logs to CloudWatch
 One AWS account can assume a role in another AWS account

### 5. Multi-Factor Authentication (MFA)

IAM supports MFA for extra security.

This means users need a second step when signing in, such as a code from an authenticator app.

### 6. Temporary credentials

IAM roles usually provide temporary credentials instead of permanent access keys.

This is safer and is a common AWS best practice.

## How it works

Here is the simple flow

1. You create an identity in IAM, such as a user or role.
2. You attach permissions using policies.
3. The identity tries to access an AWS resource.
4. AWS checks the policy.
5. AWS allows or denies the action.

IAM follows the idea of authentication and authorization

 Authentication = proving who you are
 Authorization = deciding what you can do

By default, new IAM users have no permissions until permissions are granted.

## Why it is important for the exam

IAM is one of the most important topics in the AWS Certified Cloud Practitioner exam.

You need to understand that

 IAM controls access in AWS
 IAM is a global service, not tied to one Region
 Users are for people or apps needing direct access
 Groups are for organizing users
 Roles are for temporary access
 Policies define permissions
 Root user should not be used for everyday tasks
 MFA should be enabled, especially for the root user

## Related AWS services and differences

### IAM vs Root user

 Root user = the original account owner with full access
 IAM user = a separate identity with limited permissions

Use the root user only for a few account-level tasks. Use IAM users or roles for daily work.

### IAM vs IAM Identity Center

 IAM manages users, groups, roles, and permissions inside AWS
 IAM Identity Center helps provide centralized access to multiple AWS accounts and applications

Identity Center is better for workforce access across many accounts.

### IAM vs Resource-based policies

 IAM policies are attached to users, groups, or roles
 Resource-based policies are attached directly to resources like S3 buckets

Both control access, but they are attached in different places.

### IAM vs Security Groups

 IAM controls who can do actions in AWS
 Security Groups control network traffic to resources like EC2

IAM is about identity and permissions. Security Groups are about network access.

## Common exam traps

### Trap 1 Thinking IAM is regional

Wrong. IAM is a global service.

### Trap 2 Confusing users and roles

 Users usually have long-term credentials
 Roles usually provide temporary credentials

### Trap 3 Using the root user for normal work

This is bad practice. The exam often expects you to choose IAM users or roles instead.

### Trap 4 Thinking groups can contain other groups

IAM groups contain users, not other groups.

### Trap 5 Forgetting least privilege

AWS recommends giving only the permissions needed to do a job, nothing more.

### Trap 6 Confusing authentication with authorization

 Authentication = sign in
 Authorization = permissions after sign-in

## Easy real-world example

A company has three employees

 Anna is an admin
 Ben is a developer
 Carla only needs to view reports

The company creates

 An Admins group with full admin permissions
 A Developers group with EC2 and S3 access
 A ReadOnly group for viewing resources only

Each employee gets their own IAM user and is placed into the correct group.

Later, the company launches an EC2 instance that needs to read files from S3. Instead of storing access keys on the server, they attach an IAM role to the EC2 instance.

That is the AWS best-practice approach.

## Final summary

AWS IAM is the main service for controlling access in AWS.

It helps you securely manage identities and permissions by using

 Users
 Groups
 Roles
 Policies
 MFA

For the exam, remember that IAM is global, root user access should be limited, and roles are commonly used for temporary and secure access.

## Policy Types and Permission Guardrails

| Policy or control | Purpose | Grants permissions by itself? |
|---|---|:---:|
| AWS managed policy | Reusable policy created and maintained by AWS | Yes, when attached and applicable |
| Customer managed policy | Reusable, customer-controlled policy | Yes, when attached and applicable |
| Inline policy | One-to-one policy embedded in one identity | Yes, when applicable |
| Identity-based policy | Defines what a user, group, or role may do | Yes |
| Resource-based policy | Defines which principals may access a supported resource | Yes, subject to evaluation context |
| Permissions boundary | Maximum an identity policy may grant to a user or role | No |
| Service control policy (SCP) | Maximum available permissions in affected member accounts | No |

Customer managed policies are preferable to inline policies when permissions should be reused, reviewed, and centrally updated. Resource-based policies, such as S3 bucket policies, attach to resources rather than identities.

## Policy Evaluation

Requests are implicitly denied by default. An applicable allow can grant access, but:

> An explicit deny overrides an allow.

Permissions boundaries, session policies, and SCPs can further limit effective permissions. A broad identity-policy allow cannot bypass a relevant explicit deny.

## AWS STS, Temporary Credentials, and Role Assumption

AWS Security Token Service (AWS STS) issues temporary security credentials. A role has a **trust policy** that identifies who may assume it and permissions policies that define what the resulting session may do.

Use roles for EC2 applications, Lambda functions, federated workforce users, and cross-account access instead of embedding permanent access keys. Temporary credentials reduce long-term secret exposure, but the role still needs least-privilege permissions and secure session conditions.

## Federation and IAM Identity Center

Federation lets people authenticate with an external identity provider and obtain temporary AWS access. AWS IAM Identity Center is the preferred foundation for centrally managing workforce access to multiple AWS accounts and supported applications. It complements IAM roles and policies inside each account.

## Cross-Account Access

Prefer a trusted role or an appropriate resource-based policy instead of duplicate IAM users. Cross-account role assumption normally requires a target-role trust policy, source permission to call `sts:AssumeRole`, target-role permissions for the requested actions, and compliance with applicable conditions, boundaries, session policies, and SCPs.

## AWS Organizations and SCPs

AWS Organizations groups accounts for centralized governance. Organizational units (OUs) arrange accounts so controls can be applied consistently.

An SCP is an organization-level permissions guardrail. It can restrict principals in affected member accounts, but it does not grant permissions. An IAM or resource-based policy must still allow the action.

## SAA Architecture and Design

| Requirement | Preferred starting point | Reasoning |
|---|---|---|
| Application on EC2 reads one S3 bucket | EC2 role with a narrow policy | Avoid embedded long-term keys |
| Employees access many AWS accounts | IAM Identity Center and federation | Central lifecycle and temporary access |
| Vendor needs temporary access to another account | Cross-account role with conditions | Auditable and revocable sessions |
| Developers may create roles but not administrators | Permissions boundary plus controlled policies | Limits delegated maximum permissions |
| Prohibit risky services in an OU | SCP plus necessary IAM allows | An SCP alone grants nothing |

Protect the root user with MFA, do not create root access keys, and use root only for required tasks. Design controlled emergency access, log activity, and test policy changes before retiring existing access paths.

## Additional Exam Traps

- A permissions boundary does not grant permissions.
- An SCP does not grant permissions.
- A role is assumed; a group is a collection of IAM users.
- AWS managed policies are not automatically least privilege.
- Network controls such as security groups do not replace IAM authorization.

## Knowledge Check

1. Does a permissions boundary grant access?
2. What happens when an applicable allow conflicts with an explicit deny?
3. Which service centralizes workforce access across multiple AWS accounts?
4. Does an SCP give a member-account role permission to call an API?
5. Why should an EC2 workload use a role instead of stored access keys?

<details>
<summary>Show answers</summary>

1. No. It limits the maximum permissions identity policies can grant.
2. The request is denied.
3. AWS IAM Identity Center.
4. No. It limits permissions; an IAM or resource-based policy must allow the action.
5. A role supplies temporary credentials and avoids distributing long-term secrets.

</details>

## References

- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)
- [IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
- [Temporary credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
- [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
- [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html)

Sources checked: **2026-07-22**.

## Short exam answer

AWS IAM is a global AWS service that controls authentication and authorization by letting you manage users, groups, roles, and permissions through policies.

## Memory trick

IAM = Identity And Management of access

An easy memory line

“IAM decides who gets in and what they can do.”
