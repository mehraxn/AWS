# AWS Control Tower

## Simple definition

AWS Control Tower is a service that helps you quickly set up and govern a secure multi-account AWS environment using AWS best practices.

It is mainly used when an organization wants many AWS accounts, but also wants central control, standardization, and governance.

---

## Core idea in plain English

Think of AWS Control Tower as a manager for a multi-account AWS environment.

Instead of building everything manually, AWS Control Tower helps you create a ready-made starting environment called a landing zone.

Inside that environment, it helps you

 organize accounts
 apply governance rules
 create new accounts in a standard way
 monitor whether accounts follow company rules

So the big idea is this

AWS Control Tower helps you set up AWS accounts correctly from the beginning and keep them aligned with rules over time.

---

## Main use cases

### 1. Setting up a multi-account AWS environment

A company may want separate accounts for production, development, testing, security, or different teams.

AWS Control Tower helps create and organize that structure in a guided and standardized way.

### 2. Applying governance across many AWS accounts

When a company has many accounts, it becomes hard to enforce the same rules everywhere.

AWS Control Tower helps apply governance controls across organizational units and accounts.

### 3. Standardized account creation

New AWS accounts can be created with pre-approved settings instead of being built manually each time.

This reduces mistakes and keeps accounts consistent.

### 4. Improving security and compliance posture

AWS Control Tower helps organizations follow best practices for logging, auditing, identity, and account structure.

It is useful when a company wants stronger governance from the start.

### 5. Central visibility for administrators

Cloud administrators can use the dashboard to see which accounts are governed and whether resources are compliant or not.

---

## Key features

### 1. Landing zone

A landing zone is a well-architected multi-account AWS environment.

It provides the basic structure for governance, security, shared accounts, and organization-wide setup.

This is one of the most important ideas in AWS Control Tower.

### 2. Controls

Controls are governance rules used by AWS Control Tower.

Older exam materials may call them guardrails.

These controls help prevent bad actions, detect noncompliance, or check resources before deployment.

#### Types of controls

 Preventive controls stop certain actions from happening
 Detective controls detect noncompliance after it exists
 Proactive controls check resources before they are provisioned

#### Guidance levels

 Mandatory applied by default and cannot be turned off
 Strongly recommended best-practice controls that AWS recommends
 Elective optional controls you choose based on need

### 3. Account Factory

Account Factory helps provision new AWS accounts using standardized templates.

This makes account creation faster, more repeatable, and more controlled.

### 4. Dashboard

The AWS Control Tower dashboard gives central administrators visibility into

 provisioned accounts
 enabled controls
 policy violations
 noncompliant resources

### 5. Built on other AWS services

AWS Control Tower works by orchestrating other AWS services such as

 AWS Organizations
 AWS IAM Identity Center
 AWS Service Catalog
 AWS Config
 AWS CloudTrail

So Control Tower is not replacing all of them. It coordinates them to create a governed environment.

### 6. Shared security accounts

When AWS Control Tower is set up, it creates core shared accounts for governance, especially

 Audit account
 Log archive account

These help centralize security and logging functions.

---

## How it works

### Step 1. Create or use an AWS Organization

AWS Control Tower works with AWS Organizations.

You can use an existing organization or let AWS Control Tower help set up the structure.

### Step 2. Set up the landing zone

AWS Control Tower creates the landing zone.

This gives you a multi-account environment with recommended organizational structure and governance foundations.

### Step 3. Create core accounts and organizational units

AWS Control Tower sets up important shared accounts such as the Audit account and Log archive account.

It also creates recommended organizational units for governance.

### Step 4. Apply controls

AWS Control Tower applies mandatory controls automatically and allows you to enable more controls as needed.

These help enforce or monitor security and compliance rules.

### Step 5. Provision new accounts with Account Factory

When teams need a new AWS account, they can provision one through Account Factory.

The account is created with approved configurations instead of starting from scratch.

### Step 6. Monitor the environment

Administrators use the dashboard to monitor compliance and governance status across the environment.

---

## Why it is important for the exam

AWS exams often test whether you understand the difference between

 a service that creates and governs a multi-account environment
 a service that only monitors security findings
 a service that only manages identities
 a service that only organizes accounts

AWS Control Tower is important because it is the AWS service most closely associated with

 landing zones
 multi-account governance
 Account Factory
 controls  guardrails
 standardized account setup

For the Cloud Practitioner exam, the main thing to remember is

If the question is about setting up and governing a secure multi-account AWS environment using best practices, AWS Control Tower is usually the best answer.

---

## Related AWS services and differences

### 1. AWS Organizations

AWS Organizations lets you group AWS accounts, manage consolidated billing, and apply service control policies.

Difference
AWS Organizations is the foundation.
AWS Control Tower adds automation, landing zones, governance setup, and easier multi-account management.

### 2. AWS IAM Identity Center

IAM Identity Center helps manage user access to multiple AWS accounts and applications.

Difference
IAM Identity Center focuses on sign-in and access management.
AWS Control Tower uses it, but AWS Control Tower itself is about environment setup and governance.

### 3. AWS Service Catalog

AWS Service Catalog helps users launch approved products and templates.

Difference
AWS Control Tower uses Service Catalog behind the scenes for Account Factory.
Service Catalog alone is not the full multi-account governance solution.

### 4. AWS Security Hub

AWS Security Hub helps collect and view security findings across AWS accounts and services.

Difference
Security Hub is about security posture and findings.
AWS Control Tower is about setting up and governing the whole multi-account environment.

### 5. AWS Config

AWS Config records configuration changes and evaluates resources against rules.

Difference
AWS Config focuses on resource configuration tracking and compliance checks.
AWS Control Tower uses governance concepts at the multi-account level.

### 6. AWS CloudTrail

AWS CloudTrail records API activity and account actions.

Difference
CloudTrail is for activity logging.
AWS Control Tower is for multi-account setup and governance.

---

## Common exam traps

### Trap 1. Confusing AWS Control Tower with AWS Organizations

Many students choose AWS Organizations too quickly.

Remember

 Organizations = account grouping and policy foundation
 Control Tower = governed landing zone plus automation on top of Organizations

### Trap 2. Confusing AWS Control Tower with AWS Security Hub

If the question is about security findings and alerts, think Security Hub.

If the question is about setting up and governing many AWS accounts, think Control Tower.

### Trap 3. Confusing AWS Control Tower with IAM Identity Center

If the main topic is user access and SSO, think IAM Identity Center.

If the main topic is multi-account governance, think Control Tower.

### Trap 4. Missing the meaning of landing zone

When the exam says landing zone, that is a strong hint for AWS Control Tower.

### Trap 5. Forgetting that controls used to be called guardrails

Older materials and some explanations may say guardrails.

In modern AWS Control Tower wording, the preferred term is controls.

### Trap 6. Thinking Control Tower is only for creating accounts

It does more than create accounts.

It also governs, monitors, standardizes, and helps keep accounts aligned with best practices.

### Trap 7. Thinking all controls are optional

Not true.

Some controls are mandatory and are applied automatically.

---

## Easy real-world example

Imagine a company with these separate AWS accounts

 one for production
 one for development
 one for testing
 one for security
 one for logging

Without AWS Control Tower, the cloud team would need to manually create accounts, organize them, apply policies, set up logging, and check compliance.

With AWS Control Tower, the company can create a landing zone, apply built-in governance, and let teams request new accounts through Account Factory.

This gives the company a cleaner, safer, and more standardized AWS environment.

---

## Final summary

AWS Control Tower is an AWS service for setting up and governing a secure multi-account environment.

Its most important ideas are

 landing zone
 controls
 Account Factory
 multi-account governance
 central dashboard

It builds on services like AWS Organizations, IAM Identity Center, and Service Catalog.

For the exam, think of AWS Control Tower as the service that helps organizations follow AWS best practices when managing many AWS accounts.

---

## Short exam answer

AWS Control Tower is a service that helps organizations quickly set up and govern a secure multi-account AWS environment based on AWS best practices.

---

## Memory trick

### Control Tower = tower that watches many accounts

Picture an airport control tower.

It does not build the airplanes.
It does not fly them.
It does not inspect only one seat.

It oversees and controls the whole environment.

That is how AWS Control Tower works.
It helps oversee and govern many AWS accounts from a central place.

---

## If I were an examiner ...

If I were writing AWS exam questions about AWS Control Tower, I would test whether you can recognize these ideas

### 1. The main purpose

I would ask

Which AWS service helps set up and govern a secure multi-account AWS environment based on best practices

Expected answer AWS Control Tower

### 2. The landing zone concept

I would ask

Which AWS service is strongly associated with creating a landing zone

Expected answer AWS Control Tower

### 3. The difference from AWS Organizations

I would ask

A company already uses AWS Organizations but wants an easier way to standardize account creation and apply governance across accounts. Which service should they use

Expected answer AWS Control Tower

### 4. The difference from Security Hub

I would ask

A company wants a service to set up a governed multi-account environment, not just collect security findings. Which service fits best

Expected answer AWS Control Tower

### 5. The account provisioning feature

I would ask

What AWS Control Tower feature helps provision standardized new AWS accounts

Expected answer Account Factory

### 6. The controls idea

I would ask

What are the governance rules in AWS Control Tower called

Expected answer Controls

And I may try to confuse you by using the older word guardrails.

### 7. The exam language clue

If I put phrases like these in a question, I would expect you to think of AWS Control Tower

 landing zone
 multi-account governance
 governed environment
 standardized account provisioning
 controls or guardrails
 AWS best practices across accounts

---

## One-line coaching tip

When you see multi-account setup + governance + landing zone, your brain should quickly think

AWS Control Tower
