# AWS Service Catalog

## Simple definition

AWS Service Catalog is an AWS service that lets organizations create and manage a catalog of approved AWS products that users can deploy in a controlled way.

A product can be something like a virtual machine, a database setup, a web application stack, or another approved infrastructure template.

---

## Core idea in plain English

Think of AWS Service Catalog like an internal cloud shop for a company.

Instead of letting every employee create anything they want in AWS, the company prepares a list of approved cloud solutions. Users then choose from that list and launch only what the company allows.

So the main idea is

self-service for users + control and governance for administrators.

---

## Main use cases

### 1. Standardizing deployments

A company wants all teams to use the same approved EC2 setup, database setup, or network pattern.

### 2. Safe self-service provisioning

Developers or business teams can launch resources themselves without needing full admin access.

### 3. Governance and compliance

The organization can make sure users deploy only approved and compliant resources.

### 4. Multi-account consistency

Large organizations can share approved products across many AWS accounts.

### 5. Controlled infrastructure at scale

Admins can offer ready-made infrastructure products so teams move faster without breaking company rules.

---

## Key features

 Catalog of approved products for AWS users
 Self-service provisioning
 Portfolios to organize products
 Fine-grained access control
 Constraints to limit how products are launched
 Versioning of products
 Integration with infrastructure as code
 Support for AWS CloudFormation-based products
 Support for Terraform-based products in AWS Service Catalog
 Sharing across accounts and organizations

---

## How it works

### Step 1 Admin creates products

An administrator creates products based on approved infrastructure templates.

These products often use AWS CloudFormation templates. Service Catalog also supports Terraform-based products.

### Step 2 Admin groups products into portfolios

A portfolio is a collection of products.

For example

 Portfolio for developers
 Portfolio for data team
 Portfolio for finance team

Each group can see only the products meant for them.

### Step 3 Admin applies permissions and constraints

The admin decides

 who can access the portfolio
 which product versions they can use
 what limits apply during launch

This helps keep deployments safe and standardized.

### Step 4 End user launches an approved product

The user opens the catalog, chooses an approved product, enters allowed parameters, and launches it.

### Step 5 AWS provisions the resources

Behind the scenes, AWS creates the actual infrastructure based on the approved template.

So users get self-service, but only within company rules.

---

## Why it is important for the exam

For the AWS Certified Cloud Practitioner exam, the most important point is this

AWS Service Catalog helps organizations offer approved AWS resources for self-service use while keeping governance and control.

You should recognize it in questions about

 approved products
 standardized deployments
 self-service with guardrails
 centralized governance
 controlled provisioning for users

This service is less about building infrastructure itself and more about controlling how approved infrastructure is offered to users.

---

## Related AWS services and differences

### AWS CloudFormation

 CloudFormation creates and manages infrastructure from templates.
 Service Catalog presents approved CloudFormation or Terraform products to users in a controlled catalog.

Easy way to remember
CloudFormation is the template engine.
Service Catalog is the approved storefront.

### AWS Organizations

 AWS Organizations manages multiple AWS accounts and governance at the account level.
 Service Catalog manages approved products users can deploy.

Organizations is about account management and governance structure.
Service Catalog is about approved deployment choices.

### AWS Control Tower

 Control Tower sets up and governs a multi-account AWS environment.
 Service Catalog gives users approved products to launch.

Control Tower helps create the governed environment.
Service Catalog helps control what users launch inside it.

### AWS Marketplace

 AWS Marketplace is a marketplace for third-party software and solutions.
 Service Catalog is an internal catalog of approved products for your organization.

Marketplace is like a public store.
Service Catalog is like your company’s private approved store.

### AWS Systems Manager

 Systems Manager helps manage and operate resources.
 Service Catalog helps offer approved resources for deployment.

Systems Manager is about managing resources after or during operation.
Service Catalog is about controlled provisioning.

---

## Common exam traps

### Trap 1 Confusing it with CloudFormation

Service Catalog does not mainly exist to write templates.
CloudFormation is the main service for defining infrastructure as code.

### Trap 2 Confusing it with AWS Marketplace

Service Catalog is not the public AWS software store.
It is for organization-approved products.

### Trap 3 Thinking it is only for cost control

It can help indirectly with governance and standardization, but its main purpose is approved self-service provisioning, not cost tracking.

### Trap 4 Thinking it replaces IAM

IAM controls permissions.
Service Catalog uses permissions and constraints, but it does not replace IAM.

### Trap 5 Thinking end users get unlimited freedom

The whole point is actually the opposite
users get limited, approved choices.

### Trap 6 Confusing it with Control Tower

Control Tower governs account setup and landing zones.
Service Catalog governs approved deployable products.

---

## Easy real-world example

A company has 500 developers.

The cloud team does not want every developer creating random servers, databases, and networks.
So the cloud team creates approved products such as

 a standard Linux EC2 server
 a preconfigured test database
 a small web application stack

These are placed in AWS Service Catalog.

Now developers can launch what they need by themselves, but only from the approved list.

This makes the company faster, safer, and more consistent.

---

## If I were an examiner ...

Here are the kinds of things I would ask about AWS Service Catalog in the exam

### 1. Do you understand the main purpose

I may ask

Which AWS service helps organizations provide approved AWS resources for self-service deployment by end users

Expected idea AWS Service Catalog

### 2. Do you know the core benefit

I may ask

A company wants developers to deploy only approved infrastructure templates without giving them full administrative freedom. Which service should they use

Expected idea AWS Service Catalog

### 3. Can you separate it from similar services

I may ask

Which service is used to define infrastructure as code templates, while another service is used to present approved templates to end users

Expected idea

 AWS CloudFormation defines the templates
 AWS Service Catalog offers approved products based on them

### 4. Do you know the exam keywords

I may hide the answer behind phrases like

 approved products
 self-service provisioning
 governance
 standardized deployments
 centrally managed catalog

If you see these phrases together, think AWS Service Catalog.

---

## Final summary

AWS Service Catalog is a service for creating a controlled catalog of approved AWS products.

It helps organizations give users self-service access to cloud resources, but only within approved rules.

This makes deployments more standardized, secure, and compliant.

For the exam, remember that it is about

approved products, self-service, and governance.

---

## Short exam answer

AWS Service Catalog allows organizations to create and manage catalogs of approved AWS products that users can deploy through self-service while maintaining governance and control.

---

## Memory trick

Service Catalog = company-approved cloud shop

 Catalog = list of approved products
 Service = ready-to-use IT servicesresources
 Users can shop from the list
 Admins stay in control

So remember

“Users can choose, but only from the approved menu.”
