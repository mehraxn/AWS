# AWS Fargate



<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

## Simple definition


## Core idea in plain English

Think of AWS Fargate like this:

You give AWS your container, tell it how much CPU and memory it needs, and AWS runs it for you.

You do not choose EC2 instance types, build server clusters, patch servers, or manage capacity.

So the main idea is:

**Fargate runs containers for you, while AWS manages the infrastructure underneath.**

---

## Main use cases

AWS Fargate is commonly used for:

* Running containerized web applications
* Running APIs and backend services
* Running microservices
* Running batch jobs and background workers
* Running containers when you want less infrastructure management
* Running containers with Amazon ECS or Amazon EKS

---

## Key features

### 1. Serverless for containers

You do not manage the underlying servers.

### 2. Works with ECS and EKS

You can use Fargate with:

* Amazon ECS, AWS’s container orchestration service
* Amazon EKS, AWS’s managed Kubernetes service

### 3. Pay for what you use

You pay based on the CPU and memory resources your containers use.

### 4. No capacity planning

You do not need to decide how many EC2 instances to launch.

### 5. Better operational simplicity

AWS handles much of the infrastructure work, so your team can focus more on the application.

### 6. Supports scaling

Your container tasks or pods can scale without you managing the server fleet.

---

## How it works

Here is the beginner-friendly flow:

1. You package your application into a container image.
2. You store that image in a registry such as Amazon ECR.
3. You create a task or pod definition that says how much CPU and memory the container needs.
4. You choose Fargate as the compute option.
5. AWS launches and runs the container for you.
6. If demand grows, AWS can run more container tasks based on your configuration.

The important exam idea is:

**You manage the container settings. AWS manages the servers.**

---

## Why it is important for the exam

AWS Cloud Practitioner questions often test whether you can choose the correct service based on how much infrastructure management is needed.

Fargate matters because it represents this decision:

* Need containers
* Do not want to manage servers
* Choose Fargate

This is one of the easiest container-service decision points on the exam.

---

## Related AWS services and differences

### AWS Fargate vs Amazon EC2

* Fargate: No server management
* EC2: You manage the virtual machines

Use EC2 when you want more control over the underlying servers.
Use Fargate when you want simplicity.

### AWS Fargate vs Amazon ECS

* ECS is the container orchestration service
* Fargate is the compute engine that runs the containers

A common beginner mistake is thinking they are the same thing.
They are not.

A simple way to remember it:

* ECS = organizes containers
* Fargate = provides serverless compute for containers

### AWS Fargate vs Amazon EKS

* EKS is managed Kubernetes
* Fargate can provide serverless compute for EKS workloads

So EKS is the orchestration platform, while Fargate is one way to run the workloads.

### AWS Fargate vs AWS Lambda

* Fargate: For containers that may run as services, APIs, or jobs
* Lambda: For event-driven functions without managing servers

Choose Lambda when the workload fits the function model.
Choose Fargate when you specifically need containers.

### AWS Fargate vs AWS Elastic Beanstalk

* Elastic Beanstalk: Platform service for deploying applications
* Fargate: Container compute engine

Elastic Beanstalk is more about application deployment automation.
Fargate is specifically about running containers without managing servers.

---

## Common exam traps

### Trap 1: Thinking Fargate is a container orchestration service

It is not.

Fargate is the compute engine.
ECS and EKS are the orchestration services.

### Trap 2: Thinking Fargate is the same as EC2

It is not.

With EC2, you still manage servers.
With Fargate, AWS manages the servers.

### Trap 3: Confusing Fargate with Lambda

Both are serverless, but they are for different models:

* Lambda = functions
* Fargate = containers

### Trap 4: Forgetting that Fargate is for containers

If the question is not about containers, Fargate is probably not the best answer.

### Trap 5: Choosing Fargate when the question wants full server control

If the scenario says you need control over the operating system, instance type, or host-level configuration, EC2 may be a better fit.

---

## Easy real-world example

A company builds an online ordering app using containers.

They want:

* Fast deployment
* No server patching
* No cluster management
* Automatic scaling for traffic spikes

They store the container image in Amazon ECR and run it using Amazon ECS with AWS Fargate.

Result:
The company focuses on the application, while AWS handles the infrastructure behind the containers.

---

## Final summary

AWS Fargate is a serverless compute engine for containers.

It works with Amazon ECS and Amazon EKS.
Its biggest value is that it lets you run containers without managing servers.

For the exam, the main signal is simple:

**If the workload uses containers and the company does not want to manage infrastructure, AWS Fargate is a strong answer.**

---

## Short exam answer

**AWS Fargate is a serverless compute engine for containers that works with Amazon ECS and Amazon EKS, allowing you to run containers without managing servers or clusters.**

---

## Memory trick

**Fargate = Far from servers.**

If your containers should run far away from server management, think AWS Fargate.

---

## Extra exam coach note

When you see a question about:

* Containers
* No server management
* Simple scaling
* Pay for used resources

think:

**ECS or EKS plus Fargate**
