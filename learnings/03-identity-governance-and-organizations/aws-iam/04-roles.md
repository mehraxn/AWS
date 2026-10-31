# AWS IAM Role

## Simple definition

An IAM role is an AWS identity that has permissions, but it is not tied to one specific person or long-term login.

## Core idea in plain English

Think of an IAM role like a temporary access badge.

A user, application, or AWS service can assume the role when it needs to do something. After that, AWS gives it temporary credentials so it can work with the allowed resources.

So the big idea is
roles give temporary permission without sharing permanent usernames and passwords.

## Main use cases

IAM roles are used when

 An AWS service needs to act on your behalf
 An EC2 instance needs permission to access S3 or DynamoDB
 A Lambda function needs permission to read from SQS or write logs to CloudWatch
 A user from another AWS account needs access to your resources
 A company uses temporary access instead of long-term access keys
 Applications sign in users through identity federation

## Key features

 Temporary credentials instead of long-term credentials
 No permanent password or access keys for the role itself
 Can be assumed by trusted entities
 Permissions are defined by policies
 Trust policy controls who can assume the role
 Works for cross-account access
 Common for AWS services like EC2, Lambda, and ECS

## How it works

An IAM role works in two main parts

### 1. Permission policy

This defines what the role can do.

Example

 Read files from an S3 bucket
 Write logs to CloudWatch
 Access a DynamoDB table

### 2. Trust policy

This defines who is allowed to assume the role.

Example

 EC2 can assume this role
 Lambda can assume this role
 Another AWS account can assume this role

### Basic flow

1. You create the IAM role
2. You attach permissions to it
3. You define who can assume it
4. A trusted user, service, or application assumes the role
5. AWS provides temporary security credentials
6. The role is used only within the allowed permissions

## Why it is important for the exam

IAM roles are a very important exam topic because they are one of the main security best practices in AWS.

The exam often checks whether you understand that

 Roles are for temporary access
 Roles are often used by AWS services
 Roles are safer than storing long-term access keys in code
 Roles support cross-account access
 Roles are different from IAM users

A common exam idea is
If an AWS service needs permissions, use an IAM role.

## Related AWS services and differences

### IAM User vs IAM Role

 IAM User = usually represents one person or application with long-term credentials
 IAM Role = temporary identity that is assumed when needed

### IAM Policy vs IAM Role

 IAM Policy = the permission document
 IAM Role = the identity that receives those permissions

### IAM Group vs IAM Role

 IAM Group = collection of IAM users
 IAM Role = assumable identity with temporary credentials

### STS vs IAM Role

 AWS STS (Security Token Service) issues the temporary credentials
 IAM Role is the identity being assumed

### EC2 Instance Profile vs IAM Role

 An instance profile is the container that allows an IAM role to be attached to an EC2 instance
 In simple exam language, people often say “attach a role to EC2,” but technically EC2 uses an instance profile

## Common exam traps

 Thinking an IAM role has a username and password like an IAM user
 Thinking roles are only for people
 Forgetting that AWS services can assume roles
 Confusing permission policy with trust policy
 Using access keys in an app when the better answer is an IAM role
 Mixing up IAM roles and resource-based policies

## Easy real-world example

A company runs an application on an EC2 instance.

The app needs to read images from an S3 bucket.

Bad approach
Store AWS access keys directly inside the server.

Better approach
Create an IAM role with permission to read from the S3 bucket, then attach that role to the EC2 instance.

Now the app gets temporary credentials automatically and does not need hard-coded secrets.

## Final summary

An IAM role is an AWS identity with permissions that can be assumed temporarily by trusted users, applications, or AWS services.

It is mainly used to provide secure temporary access without storing long-term credentials.

For the exam, remember this rule
services usually use roles, people often use users, and temporary access usually means roles.

## Short exam answer

An IAM role is an AWS identity with permission policies that can be assumed by trusted entities to get temporary security credentials.

## Memory trick

User = you

Role = borrowed permission

Or remember
“Users log in, roles are assumed.”
