# IAM Group

## Simple definition

An IAM group is a collection of IAM users.

You use a group to give the same permissions to multiple users at the same time.

## Core idea in plain English

Instead of giving permissions to users one by one, you put users into a group and give the group the permissions.

This makes access management easier, faster, and cleaner.

Think of it like this

 Put all developers in a Developers group
 Put all finance staff in a Finance group
 Give each group the permissions that match their job

## Main use cases

IAM groups are mainly used when

### 1. Many users need the same access

If several employees need the same AWS permissions, place them in one group.

### 2. You want easier permission management

You can update the group once instead of updating each user separately.

### 3. You want cleaner security administration

Groups help you organize access by team, job role, or department.

## Key features

### Group contains IAM users

An IAM group can contain multiple IAM users.

### One user can be in multiple groups

A user can belong to more than one group if needed.

Example
A user could be in both Developers and ReadOnlyAudit.

### Permissions are usually attached through policies

You attach IAM policies to the group, and the users in that group receive those permissions.

### Groups do not have login credentials

A group is not a person and does not sign in.

### Groups are not for roles

Groups are for IAM users only.

### Groups cannot be nested

You cannot put one IAM group inside another IAM group.

## How it works

Here is the simple flow

1. Create IAM users
2. Create a group
3. Attach permissions policies to the group
4. Add users to the group
5. Those users get the permissions from the group

If you later remove a user from the group, that user loses the group-based permissions.

## Why it is important for the exam

IAM groups are important in the Cloud Practitioner exam because AWS often tests the basic differences between

 IAM user
 IAM group
 IAM role
 Root user

You should clearly remember that

 IAM user = one identity for one person or application
 IAM group = a collection of IAM users
 IAM role = temporary access that can be assumed
 Root user = full account owner identity

The exam also likes the idea of managing permissions efficiently. IAM groups are a classic example of that.

## Related AWS services and differences

### IAM User vs IAM Group

IAM user is an individual identity with credentials.

IAM group is a container for users. It helps manage permissions for many users together.

### IAM Group vs IAM Role

IAM group is used to organize IAM users.

IAM role is assumed temporarily and is often used by AWS services, applications, or federated users.

A group does not get assumed.
A role does.

### IAM Group vs Root User

The root user is the original account owner and has full control over the AWS account.

An IAM group is just a permission-management tool for IAM users.

### IAM Group vs IAM Identity Center

IAM groups are inside IAM and are mainly for IAM users in one AWS account environment.

IAM Identity Center is used for workforce access across AWS accounts and applications, especially in larger organizations.

For the exam, remember that IAM Identity Center is the more modern service for centralized workforce access.

## Common exam traps

### Trap 1 Thinking a group is a login identity

Wrong. A group does not sign in.
Only users sign in with user credentials.

### Trap 2 Thinking groups are used for AWS services

Wrong. AWS services usually use IAM roles, not groups.

### Trap 3 Thinking you can put roles into groups

Wrong. Groups contain users only.

### Trap 4 Thinking groups can contain groups

Wrong. IAM groups cannot be nested.

### Trap 5 Thinking all users automatically belong to a default group

Wrong. There is no automatic default group for all users.

## Easy real-world example

A company has 10 developers.

All 10 developers need access to

 Amazon S3 for code artifacts
 Amazon CloudWatch for logs
 AWS CodeCommit read access

Instead of assigning these permissions to each developer one by one, the admin

1. Creates a group called Developers
2. Attaches the right policies to that group
3. Adds all 10 developer IAM users to the group

Now all developers get the correct access.

When a new developer joins, the admin only needs to add that user to the Developers group.

## Final summary

An IAM group is a simple way to manage permissions for multiple IAM users at once.

It does not have credentials.
It does not represent an AWS service.
It is not a role.

Its main purpose is to make permission management easier and more organized.

For the exam, remember
Groups are for users, roles are for temporary access.

## Short exam answer

An IAM group is a collection of IAM users that makes it easier to assign the same permissions to multiple users.

## Memory trick

User = one person

Group = many users together

Role = temporary access

Easy memory line
“Users join groups. Users and services assume roles.”
