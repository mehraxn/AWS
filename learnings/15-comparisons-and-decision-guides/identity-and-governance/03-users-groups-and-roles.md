# IAM Role vs IAM Group vs IAM User

AWS Certified Cloud Practitioner Study Note

---

## Simple Definitions

### IAM User

An IAM user is an identity in AWS for one specific person or application that needs direct access to AWS.

It can have

 A username and password for the AWS Management Console
 Access keys for CLI or API access
 Permissions attached directly or through groups

### IAM Group

An IAM group is a collection of IAM users.

A group is used to make permission management easier. Instead of giving the same permissions to many users one by one, you put users into a group and assign permissions to the group.

### IAM Role

An IAM role is an AWS identity with permissions that is assumed temporarily.

A role is not usually tied to one permanent person. It is used when a user, AWS service, or external system needs temporary access to AWS resources.

---

## Core Idea in Plain English

 IAM User = one person or app identity
 IAM Group = a permission container for many users
 IAM Role = temporary access you can switch into or assume

Think of them like this

 User = one employee badge
 Group = department membership
 Role = temporary visitor or job badge used for a specific task

---

## Main Purpose of Each

### IAM User

Used to give a specific person or application its own AWS identity.

### IAM Group

Used to manage permissions for multiple IAM users at the same time.

### IAM Role

Used to give temporary permissions to trusted identities such as

 AWS services
 IAM users
 users in another AWS account
 federated users
 applications running on EC2, Lambda, or ECS

---

## Key Differences

### 1. Permanent vs Temporary

 IAM User is usually a long-term identity
 IAM Role is usually temporary
 IAM Group is not an identity at all; it is only for organizing users

### 2. Can Sign In Directly

 IAM User yes
 IAM Group no
 IAM Role not directly like a normal user; it must be assumed

### 3. Has Long-Term Credentials

 IAM User yes, can have password and access keys
 IAM Group no credentials
 IAM Role no long-term credentials; provides temporary security credentials

### 4. Who Can Use It

 IAM User one person or app
 IAM Group many IAM users
 IAM Role whoever is trusted to assume it

### 5. Main Job

 IAM User identity for a personapp
 IAM Group simplify permission management
 IAM Role grant temporary permissions safely

---

## Similarities

All three are part of AWS Identity and Access Management (IAM).

They all relate to controlling

 who can access AWS
 what actions are allowed
 which resources can be used

Also

 Users and roles can have permissions
 Groups help assign permissions to users
 All are used to follow the least privilege principle

---

## When to Use IAM User

Use an IAM user when

 one specific employee needs AWS access
 a person needs console login
 you need a separate identity for auditing and tracking

For the exam, AWS usually prefers modern approaches like federation and roles over creating many long-term IAM users.

---

## When to Use IAM Group

Use an IAM group when

 many users need the same permissions
 you want easier permission management
 you want to avoid attaching the same policy to many users one by one

Example

 Put Alice, Bob, and Carla into a Developers group
 Attach a policy allowing access to development resources

---

## When to Use IAM Role

Use an IAM role when

 an EC2 instance needs access to S3
 a Lambda function needs to read from DynamoDB
 a user needs temporary elevated access
 one AWS account needs to access resources in another AWS account
 users sign in through federation such as AWS IAM Identity Center or an external identity provider

This is one of the most tested IAM ideas in the exam.

---

## Real Exam-Style Decision Rule

Use this rule in the exam

 If the question says one person needs direct AWS access, think IAM user
 If the question says many users need the same permissions, think IAM group
 If the question says temporary access, cross-account access, or AWS service access, think IAM role

Fast shortcut

 Person = User, Team = Group, Temporary access = Role

---

## Side-by-Side Comparison Table

 Feature                     IAM User                     IAM Group                                                   IAM Role                                    
 --------------------------  ---------------------------  ----------------------------------------------------------  ------------------------------------------- 
 What is it                 Identity for one personapp  Collection of IAM users                                     Temporary assumed identity                  
 Can log in to AWS console  Yes                          No                                                          Assumed, not a normal direct login identity 
 Has credentials            Yes                          No                                                          Temporary credentials only                  
 Used for permissions       Yes                          Indirectly, by assigning permissions to users in the group  Yes                                         
 Best for                    Individual access            Managing many users                                         Temporaryservicecross-account access      
 Contains users             No                           Yes                                                         No                                          
 Can be assumed             No                           No                                                          Yes                                         
 Common exam phrase          “An employee needs access”   “A team needs same access”                                  “An EC2 instance needs access”              

---

## Main Use Cases

### IAM User Use Cases

 Employee signs in to AWS Console
 Admin creates separate named identities
 Application uses access keys, although AWS often prefers roles instead

### IAM Group Use Cases

 Developers need same access
 Finance team needs billing read-only access
 Operations team needs monitoring permissions

### IAM Role Use Cases

 EC2 accesses S3 without storing access keys
 Lambda reads from DynamoDB
 Cross-account access
 Temporary admin access
 Federated workforce access

---

## Key Features

### IAM User

 Unique identity
 Password for console access
 Optional access keys
 Can have policies attached directly
 Can be added to groups
 Supports MFA

### IAM Group

 Holds multiple IAM users
 Permissions assigned once to the group
 Users inherit the group permissions
 Cannot be used for login
 Cannot contain other groups

### IAM Role

 No long-term credentials
 Temporary credentials from AWS STS
 Trusted entities can assume it
 Great for AWS services and cross-account access
 More secure than embedding access keys

---

## How Each Works

### How IAM User Works

1. You create a user in IAM
2. You give it credentials
3. You attach permissions directly or through a group
4. The user signs in or uses APICLI access

### How IAM Group Works

1. You create a group
2. You attach policies to the group
3. You add IAM users to the group
4. Those users receive the group permissions

### How IAM Role Works

1. You create a role
2. You define who can assume it in the trust policy
3. You attach permission policies to the role
4. A trusted identity assumes the role
5. AWS provides temporary credentials

---

## Why the Difference Matters for the Exam

AWS exam questions often test whether you can choose the most secure and most scalable option.

This is where many learners get confused

 They choose IAM user when AWS really wants IAM role
 They forget that IAM groups do not have credentials
 They think a group is the same as a role, but it is not

The exam loves these patterns

 EC2 needs access to S3 → use an IAM role, not access keys in the instance
 Several employees need same permissions → use an IAM group
 A named employee needs individual access → use an IAM user

---

## Related AWS Services and Differences

### AWS IAM Identity Center

IAM Identity Center is used for workforce access across AWS accounts and applications.

Difference

 IAM users are identities created directly in IAM
 IAM Identity Center is better for centralized workforce sign-in at scale
 It often works with roles behind the scenes

### AWS STS (Security Token Service)

STS provides temporary credentials.

Difference

 IAM roles commonly use STS
 IAM users can have long-term credentials

### AWS Organizations

Organizations helps manage multiple AWS accounts.

Difference

 IAM roles are often used for cross-account access inside an organization
 Groups only organize users inside IAM; they do not solve cross-account trust

---

## Common Exam Traps

### Trap 1 “EC2 needs access to S3”

Wrong answer create an IAM user and store access keys on the instance

Correct answer attach an IAM role to the EC2 instance

### Trap 2 “A team needs the same permissions”

Wrong answer create separate identical policies for each user

Correct answer use an IAM group

### Trap 3 “A role is just another user”

Wrong answer thinking role and user are basically the same

Correct answer a user is a long-term identity; a role is temporary and assumed

### Trap 4 “Groups can log in”

Wrong answer assuming a group can have credentials

Correct answer only users can sign in directly; groups cannot

### Trap 5 “Use IAM users for everything”

Wrong answer using long-term credentials when temporary credentials are safer

Correct answer AWS often prefers roles for services and temporary access

---

## Easy Real-World Examples

### IAM User Example

Rahul is a cloud administrator. He gets his own AWS login. That is an IAM user.

### IAM Group Example

Rahul, Sara, and Lina all work in support. They all need read-only access to CloudWatch. Put them in a Support group.

### IAM Role Example

An EC2 instance must read files from an S3 bucket. Instead of saving access keys on the server, attach an IAM role to the EC2 instance.

---

## Easy Way to Compare Them

Ask three questions

### Is it one named person or app

Use IAM user.

### Is it many IAM users needing the same permissions

Use IAM group.

### Is it temporary access or service access

Use IAM role.

---

## Final Summary

IAM users, groups, and roles are all part of AWS IAM, but they do different jobs.

 IAM user = identity for one person or application
 IAM group = permission collection for many users
 IAM role = temporary permissions for trusted identities or AWS services

For exam success, remember that AWS strongly prefers roles for temporary and service-based access, while groups are best for managing permissions for teams.

---

## Short Exam Answer

An IAM user is a permanent identity for one person or application. An IAM group is a collection of IAM users that makes permission management easier. An IAM role is a temporary identity that trusted users, AWS services, or accounts can assume to get temporary permissions.

---

## Memory Trick

Remember this

U-G-R = User, Group, Role

 User = You
 Group = Gang
 Role = Rent for a while

Or even shorter

 User = one
 Group = many
 Role = temporary

---

## One-Line Exam Coach Tip

When AWS asks for the most secure way for a service to access another AWS service, the answer is usually IAM role.
