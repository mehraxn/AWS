# AWS IAM Identity Center

## Simple definition

AWS IAM Identity Center is an AWS service that helps you give workforce users secure access to multiple AWS accounts and business applications from one central place.

It is the AWS service for single sign-on (SSO) and centralized access management.

## Core idea in plain English

Think of IAM Identity Center as a main login door for your company staff.

Instead of creating separate usernames and permissions again and again in every AWS account, you manage access once in a central place. Then users sign in one time and get access only to the AWS accounts and applications they are allowed to use.

So the big idea is

one sign-in, one central place to manage access, many AWS accounts and apps.

## Main use cases

 Give employees access to multiple AWS accounts
 Provide single sign-on access to AWS applications and cloud apps
 Centrally manage user and group access across an AWS Organization
 Connect an existing identity provider like Microsoft Active Directory, Okta, or Entra ID
 Reduce the need to create separate IAM users in every account

## Key features

 Centralized access management for multiple AWS accounts
 Single sign-on for workforce users
 Permission sets to define what users can do
 Support for users and groups
 Integration with external identity sources
 AWS access portal for easy sign-in
 Works well with AWS Organizations
 Temporary credentials are used after sign-in instead of long-term access keys for normal console access

## How it works

### 1. Set up IAM Identity Center

You enable IAM Identity Center in your AWS environment.

### 2. Choose an identity source

You can either

 create users directly in IAM Identity Center, or
 connect an existing identity provider or directory

### 3. Create permission sets

A permission set is a package of permissions.

It defines what a user or group can do in an AWS account, such as read-only access or administrator access.

### 4. Assign users or groups

You assign users or groups to one or more AWS accounts and attach the right permission set.

### 5. Users sign in once

Users go to the AWS access portal, sign in one time, and then choose the AWS account or application they need.

### 6. IAM roles are used in the target account

Behind the scenes, IAM Identity Center creates and manages the needed roles in the AWS accounts based on the permission sets.

## Why it is important for the exam

For the Cloud Practitioner exam, IAM Identity Center matters because AWS often tests whether you understand the difference between

 managing workforce access across many AWS accounts, and
 managing identities and permissions inside one AWS account

IAM Identity Center is the correct answer when the question talks about

 single sign-on
 centralized access
 multiple AWS accounts
 AWS Organizations
 employees signing in with existing corporate credentials

## Related AWS services and differences

### IAM vs IAM Identity Center

AWS IAM manages users, groups, roles, and permissions mainly inside a single AWS account.

AWS IAM Identity Center manages workforce access centrally across multiple AWS accounts and applications.

Easy rule

 IAM = permissions system inside AWS accounts
 IAM Identity Center = central login and access hub across accounts and apps

### IAM Roles

IAM roles give temporary permissions to identities or services.

IAM Identity Center often uses roles in target AWS accounts behind the scenes after a user signs in.

### AWS Organizations

AWS Organizations helps you manage multiple AWS accounts together.

IAM Identity Center works very well with Organizations to give centralized access across those accounts.

### Amazon Cognito

Amazon Cognito is mainly for application end users, such as customers signing in to a mobile app or website.

IAM Identity Center is mainly for workforce users, such as employees, admins, and developers.

## Common exam traps

### Trap 1 Confusing IAM with IAM Identity Center

If the question says multiple AWS accounts, SSO, or centralized workforce access, the answer is usually IAM Identity Center, not plain IAM.

### Trap 2 Thinking it is mainly for application customers

If the users are customers of an app, the exam may want Amazon Cognito.

If the users are company staff using AWS accounts, the exam may want IAM Identity Center.

### Trap 3 Forgetting permission sets

In IAM Identity Center, access to AWS accounts is commonly managed using permission sets.

### Trap 4 Missing the AWS SSO rename

Older materials may still say AWS Single Sign-On (AWS SSO).

That service was renamed to AWS IAM Identity Center.

## Easy real-world example

A company has 50 employees and 6 AWS accounts

 one for development
 one for testing
 one for production
 and others for security and logging

The company does not want to create separate IAM users in every account.

So it uses IAM Identity Center.

Employees sign in once with company credentials. A developer can open the development account with developer permissions. A finance employee can open only billing-related tools. A security engineer can access the security account.

Everything is managed from one central place.

## Final summary

AWS IAM Identity Center is the AWS service for centralized workforce access.

It helps organizations give employees single sign-on access to multiple AWS accounts and applications. It works especially well with AWS Organizations and uses permission sets to control access.

For the exam, remember it as the service for SSO + centralized access across many AWS accounts.

## Short exam answer

AWS IAM Identity Center is used to centrally manage workforce user access and provide single sign-on to multiple AWS accounts and applications.

## Memory trick

Identity Center = one center for many identities and many accounts.

Or even shorter

IAM = one account permissions

IAM Identity Center = many accounts, one login
