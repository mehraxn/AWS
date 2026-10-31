# Amazon Verified Permissions

## Simple definition

Amazon Verified Permissions is a fully managed AWS service that helps you control who can do what inside the applications you build.

It is mainly used for **authorization**, especially **fine-grained permissions**.

---

## Core idea in plain English

Think of it like this:

* **Authentication** answers: **Who are you?**
* **Authorization** answers: **What are you allowed to do?**

Amazon Verified Permissions focuses on the second question.

It helps your application decide things like:

* Can this user view this document?
* Can this manager approve this request?
* Can this customer edit only their own data?
* Can this tenant admin manage users in their own company only?

Instead of hardcoding these rules inside your app, you place them in a central permission system.

---

## Main use cases

### 1. Fine-grained access control in custom applications

Use Amazon Verified Permissions when different users need different levels of access inside your application.

**Example:** In a project management app, an owner can delete a project, an editor can update it, and a viewer can only read it.

### 2. Multi-tenant SaaS applications

It is useful when one application serves many customers and each customer should only access their own users, data, and resources.

**Example:** Company A should not be able to view or manage Company B’s records inside the same SaaS platform.

### 3. Role-based and attribute-based permissions

You can build authorization rules based on roles or based on attributes.

* **RBAC** = Role-Based Access Control
* **ABAC** = Attribute-Based Access Control

**Example:** A manager can approve requests in their region, or an employee can view only documents from their department.

### 4. API and backend authorization

Your application backend or API can call Verified Permissions before allowing an action to happen.

**Example:** Before updating a record, the backend checks whether the signed-in user is allowed to perform the **update** action on that specific resource.

### 5. Centralizing authorization logic outside application code

It is helpful when you want permission rules stored in one managed place instead of spreading them across many services, APIs, or code files.

**Benefit:** This makes permission changes easier to manage, audit, and maintain.

---

## Key features

### 1. Fine-grained authorization

Verified Permissions supports detailed decisions at the action and resource level.

It is not just about broad access to the whole app. It can evaluate specific actions like **view**, **edit**, **approve**, **share**, or **delete** on specific resources.

### 2. Centralized policy management

Permission rules are stored in a central policy store instead of being hardcoded in your application.

This makes authorization more consistent and easier to update.

### 3. Uses Cedar policy language

Permissions are written using **Cedar**, which is AWS’s policy language for application authorization.

Cedar is designed to express authorization logic clearly and safely.

### 4. Supports RBAC and ABAC

You can define access using roles, user attributes, resource attributes, or a mix of both.

This gives flexibility for simple and advanced authorization models.

### 5. Policy store

Policies are stored in a **policy store**, which your application queries when it needs an authorization decision.

This separates permission logic from app logic.

### 6. Real-time authorization decisions

Your application sends a request with details such as principal, action, resource, and context.

Verified Permissions evaluates the request and returns **Allow** or **Deny** in real time.

### 7. Works with identity sources

It can work with identity providers such as **Amazon Cognito**.

That means a user can first sign in through an identity service, and then Verified Permissions decides what that authenticated user can do.

### 8. Helps reduce authorization logic in code

Instead of writing many if-else permission checks inside your code, you move those rules into policies.

This can make applications easier to manage and scale.

---

## How it works

### Step 1. The user signs in

The user is authenticated by an identity system such as Amazon Cognito or another identity provider.

### Step 2. The app receives a request

**Example:** Ali wants to edit Document A.

### Step 3. The app asks Verified Permissions

The app sends details such as:

* **Principal** = the user
* **Action** = edit
* **Resource** = Document A
* **Context** = extra details like department, owner, tenant, time, or status

### Step 4. Verified Permissions checks the policies

It evaluates the request against the stored Cedar policies.

### Step 5. It returns a decision

The service returns:

* **Allow**
* **Deny**

### Step 6. The app enforces the result

If the result is **Allow**, the app continues.

If the result is **Deny**, the app blocks the action.

---

## Why it is important for the exam

For exam purposes, the biggest lesson is understanding what Amazon Verified Permissions is designed for.

It is mainly for:

* authorization inside custom applications
* fine-grained permission decisions
* centralized permission policies
* role-based and attribute-based access control

It is **not** mainly for:

* signing users in
* storing usernames and passwords
* granting permissions to AWS services like S3 or EC2
* workforce access across AWS accounts

### Exam mindset

If a question talks about:

* controlling what users can do inside an application
* checking permissions like **view**, **edit**, **approve**, **share**, or **delete**
* needing **fine-grained authorization**
* managing authorization policies centrally

then **Amazon Verified Permissions** is a strong match.

### Cloud Practitioner note

This service is useful to understand at a high level, mainly to avoid confusion with **IAM** and **Amazon Cognito**.

It is usually less central in Cloud Practitioner than services such as IAM, Cognito, KMS, GuardDuty, or AWS Artifact, but it can still appear as a comparison or distractor option.

---

## Related AWS services and differences

## Amazon Verified Permissions vs IAM

### IAM

IAM controls access to AWS resources such as:

* S3 buckets
* EC2 instances
* Lambda functions
* DynamoDB tables

### Verified Permissions

Verified Permissions controls access **inside your own application**.

### Easy difference

* **IAM** = permissions for AWS services and AWS resources
* **Verified Permissions** = permissions for actions inside custom apps

---

## Amazon Verified Permissions vs Amazon Cognito

### Cognito

Cognito mainly handles user authentication and user identity for applications.

It helps with things like:

* sign-up
* sign-in
* user directory
* tokens
* federation

### Verified Permissions

Verified Permissions decides what that signed-in user is allowed to do.

### Easy difference

* **Cognito** = who the user is
* **Verified Permissions** = what the user can do

---

## Amazon Verified Permissions vs AWS IAM Identity Center

### IAM Identity Center

IAM Identity Center is mainly for workforce users such as employees who need access to:

* multiple AWS accounts
* AWS applications
* third-party business applications

### Verified Permissions

Verified Permissions is for authorization inside custom-built apps.

### Easy difference

* **IAM Identity Center** = workforce access across AWS accounts and business apps
* **Verified Permissions** = fine-grained access decisions inside an app

---

## Amazon Verified Permissions vs AWS KMS

### AWS KMS

AWS KMS manages encryption keys.

### Verified Permissions

Verified Permissions manages authorization rules.

### Easy difference

* **KMS** = protects data with encryption
* **Verified Permissions** = controls who can perform actions

---

## Common exam traps

### 1. Confusing authentication with authorization

This is the most common trap.

If the question is about **signing in**, **user pools**, **login**, or **identity**, think **Amazon Cognito** or another identity provider.

If the question is about what a signed-in user can do **after login**, think **Amazon Verified Permissions**.

### 2. Thinking it replaces IAM

Verified Permissions does **not** replace IAM.

IAM is still used for controlling access to AWS services and AWS resources. Verified Permissions is used for permissions **inside applications**.

### 3. Thinking it stores users and passwords

Verified Permissions is not your user directory and not your sign-in service.

It evaluates authorization rules. It does not mainly manage usernames, passwords, or sign-in flows.

### 4. Thinking it is mainly for AWS account access

If the question is about employees accessing AWS accounts, think **IAM**, **IAM Identity Center**, or related AWS access services.

Verified Permissions is more about app-level authorization than AWS account administration.

### 5. Missing the phrase “fine-grained permissions”

In exam questions, phrases like **fine-grained access control**, **application authorization**, or **centralized authorization policies** are strong clues for Verified Permissions.

### 6. Confusing it with encryption services

Verified Permissions does not encrypt data and does not manage keys.

If the question is about encryption keys, key rotation, or protecting data cryptographically, think **AWS KMS**, not Verified Permissions.

### 7. Ignoring application context in the question

If the question includes details such as **document owner**, **department**, **tenant**, **project status**, or **region**, that suggests attribute-based authorization logic.

That is a clue pointing toward **Verified Permissions**.

---

## AWS exam keywords and clue words

These are the kinds of words and phrases that may appear in exam questions and point toward Amazon Verified Permissions:

### Strong clue words

* fine-grained authorization
* fine-grained permissions
* application authorization
* centralized authorization
* policy-based authorization
* user can perform action on resource
* allow or deny decision
* role-based access control
* RBAC
* attribute-based access control
* ABAC
* policy store
* Cedar
* principal, action, resource, context
* multi-tenant application
* SaaS authorization
* custom application permissions
* app-level access control

### Action words often seen in scenarios

* view
* edit
* approve
* delete
* share
* manage
* update
* read
* write

### Resource examples that may appear

* document
* project
* record
* request
* invoice
* ticket
* user profile
* tenant data

### Identity-related clue pairing

A common exam pattern is:

* **Cognito** for authentication
* **Verified Permissions** for authorization

If a question describes both sign-in and post-login permissions, the correct design may include **both services together**.

---

## Easy real-world example

Imagine you build a document-sharing app.

There are four types of users:

* Admin
* Manager
* Editor
* Viewer

Rules:

* Admin can do everything
* Manager can approve and view documents in their department
* Editor can edit documents they created
* Viewer can only read approved documents

Instead of writing all these rules directly in your application code, you store them in Amazon Verified Permissions.

Whenever a user tries to do something, your app asks:

**Is this user allowed to do this action on this document?**

Verified Permissions checks the policies and answers **Allow** or **Deny**.

---

## Final summary

Amazon Verified Permissions is an AWS service for **fine-grained authorization in custom applications**.

It helps developers separate permission logic from application code and manage it in a central place.

It uses **Cedar policies** and can make real-time decisions like whether a user can **view**, **edit**, **approve**, or **delete** something inside an app.

Remember the simple distinction:

* **Cognito** = sign in the user
* **Verified Permissions** = decide what the user can do
* **IAM** = control access to AWS resources

---

## Short exam answer

Amazon Verified Permissions is a fully managed AWS service that provides fine-grained authorization for custom applications using centralized policies.

---

## Memory tricks

* **Verified Permissions = Verify permission inside the app**
* **Cognito = Who are you?**
* **Verified Permissions = What can you do?**
* **IAM = What can access AWS?**
