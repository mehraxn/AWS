# IAM User

## Simple definition

An IAM user is a person or application in an AWS account that has its own sign-in details and permissions.

## Core idea in plain English

Think of an IAM user as an individual login inside one AWS account. Instead of everyone using the root account, AWS lets you create separate users for different people or apps and give each one only the permissions they need.

## Main use cases

 Give employees their own AWS login
 Give administrators separate accounts instead of using the root user
 Let applications access AWS with specific permissions
 Control who can do what in the AWS account
 Track actions by individual identity

## Key features

 Has a unique username in the AWS account
 Can have a password for AWS Management Console access
 Can have access keys for CLI, SDK, or API access
 Permissions are controlled with IAM policies
 Can be placed into IAM groups
 Supports MFA for extra security
 Belongs to one AWS account

## How it works

First, an administrator creates an IAM user in AWS Identity and Access Management (IAM).

Then the admin chooses how that user will access AWS. The user may get

 A password for console sign-in
 Access keys for programmatic access
 Both, if needed

Next, permissions are attached through

 Direct policies on the user
 Group permissions
 Sometimes permission boundaries

When the IAM user signs in or makes an API call, AWS checks the policies attached to that user and decides whether to allow or deny the action.

## Why it is important for the exam

IAM is one of the most tested topics in the AWS Certified Cloud Practitioner exam.

You must clearly know that

 The root user has full access and should not be used for daily work
 IAM users are created for individual people or applications
 Permissions are controlled by policies
 MFA should be enabled for better security
 AWS follows the least privilege principle

Exam questions often test whether you know the safest identity to use for daily tasks. The correct answer is usually an IAM identity, not the root user.

## Related AWS services and differences

### IAM User vs Root User

 Root user belongs to the AWS account itself
 IAM user is a separate identity inside the account
 Root has full access by default
 IAM user gets only the permissions that are assigned
 Root should be used only for rare account-level tasks

### IAM User vs IAM Role

 IAM user is usually for one person or one application that needs long-term identity
 IAM role is meant to be assumed temporarily
 Roles are commonly used by AWS services, applications, or federated users
 Roles provide temporary credentials, which is usually more secure than long-term access keys

### IAM User vs IAM Group

 IAM user is one identity
 IAM group is a collection of users
 Groups help assign the same permissions to multiple users more easily

### IAM User vs AWS IAM Identity Center

 IAM user is created directly in one AWS account
 IAM Identity Center is used to manage access across multiple AWS accounts and applications
 In modern environments, Identity Center is often preferred for workforce access

## Common exam traps

 Thinking the root user should be used every day
 Confusing users, groups, and roles
 Forgetting that policies control permissions
 Assuming every IAM user automatically has admin access
 Mixing up console password access with programmatic access keys
 Forgetting that access keys should be protected and rotated
 Missing that MFA is strongly recommended, especially for privileged users

## Easy real-world example

A company has three employees using AWS

 Anna manages billing reports
 Omar deploys EC2 instances
 Sara only uploads files to S3

Instead of sharing one account, the admin creates three IAM users.

Then each person gets only the permissions they need

 Anna gets billing-related access
 Omar gets EC2-related access
 Sara gets S3 upload access

This is safer, easier to manage, and makes activity tracking much clearer.

## Final summary

An IAM user is an individual identity inside an AWS account. It has its own credentials and gets permissions through IAM policies. IAM users are safer than using the root user for daily work because each person or application can get only the access they need.

For the exam, remember that IAM users help AWS apply security best practices such as least privilege, separate identities, and better accountability.

## Short exam answer

An IAM user is an identity in an AWS account for a person or application. It has its own credentials and receives permissions through IAM policies.

## Memory trick

User = Unique login

Think

 Root = account owner
 User = daily personapp login
 Role = temporary borrowed access

A simple memory line

“Root owns the house, user gets a room, role gets a visitor pass.”
