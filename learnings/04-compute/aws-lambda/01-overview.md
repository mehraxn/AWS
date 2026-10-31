# AWS Lambda

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Simple definition

AWS Lambda is a serverless compute service that lets you run code without managing servers.

You upload your code, set a trigger, and AWS runs it for you.

---

## Core idea in plain English

Think of AWS Lambda like this

“When something happens, run my code automatically.”

You do not need to launch EC2 instances, patch servers, or worry about scaling the infrastructure yourself.

Lambda is mainly about event-driven computing.

---

## Main use cases

AWS Lambda is commonly used for

 Running code when a file is uploaded to Amazon S3
 Processing data from Amazon Kinesis or DynamoDB Streams
 Building serverless APIs with Amazon API Gateway
 Automating background jobs
 Running scheduled tasks with Amazon EventBridge
 Handling IoT messages from connected devices
 Sending notifications or doing small backend tasks

---

## Key features

### 1. Serverless

You do not manage servers. AWS handles the infrastructure.

### 2. Event-driven

Lambda runs when an event happens, such as

 a file upload
 an API request
 a database change
 a scheduled time event

### 3. Automatic scaling

Lambda automatically scales up when many events arrive.

### 4. Pay for use

You pay only when your code runs.

### 5. Supports many languages

You can write Lambda functions in languages such as

 Python
 Node.js
 Java
 C#
 Go
 Ruby
 and custom runtimes

### 6. Fast integration with AWS services

Lambda works very well with services like S3, API Gateway, DynamoDB, EventBridge, SQS, SNS, and CloudWatch.

### 7. Built-in monitoring support

You can monitor logs and metrics using Amazon CloudWatch.

---

## How it works

Here is the simple flow

1. You write a Lambda function
2. You upload the code to AWS Lambda
3. You connect a trigger
4. The trigger sends an event to Lambda
5. Lambda runs your code
6. Lambda returns the result if needed

### Simple example flow

 A user uploads an image to Amazon S3
 S3 triggers a Lambda function
 Lambda resizes the image
 The resized image is saved back to S3

This is a classic exam example.

---

## Why it is important for the exam

AWS Lambda is very important in the Cloud Practitioner exam because it teaches several big AWS ideas

 serverless computing
 event-driven architecture
 automatic scaling
 pay-as-you-go pricing
 reduced operational effort

In exam questions, Lambda is often the best answer when the question asks for

 no server management
 automatic scaling
 cost efficiency for unpredictable workloads
 running backend code in response to events

---

## Related AWS services and differences

### AWS Lambda vs Amazon EC2

 Lambda no server management, event-driven, short-running tasks
 EC2 full server control, you manage the instance

Use Lambda when you want AWS to handle the infrastructure.
Use EC2 when you need full control over the operating system and server setup.

### AWS Lambda vs Amazon ECS  Amazon EKS

 Lambda run individual functions
 ECSEKS run containers

Use Lambda for simpler event-driven workloads.
Use ECS or EKS when you need container orchestration.

### AWS Lambda vs AWS Fargate

 Lambda function-based serverless compute
 Fargate serverless compute for containers

Both are serverless, but they are used differently.

### AWS Lambda vs AWS Batch

 Lambda small, event-driven tasks
 AWS Batch large batch computing jobs

### AWS Lambda vs Step Functions

 Lambda runs one piece of logic
 Step Functions coordinates multiple steps and services into a workflow

Many architectures use both together.

### AWS Lambda vs API Gateway

 Lambda runs code
 API Gateway receives API requests and passes them to Lambda or other backends

These services are often used together, not as replacements.

---

## Common exam traps

### Trap 1 “Serverless” does not mean “no servers exist”

Servers still exist, but AWS manages them for you.

### Trap 2 Lambda is not for everything

Lambda is great for many workloads, but not every workload. Very long-running, highly customized, or full-server workloads may fit EC2, ECS, or EKS better.

### Trap 3 Lambda is event-driven

If the question says

 run code when something changes
 react to an upload
 process a queue message
 run backend logic without managing servers

Lambda should come to mind quickly.

### Trap 4 API Gateway and Lambda are different services

API Gateway receives API calls.
Lambda runs backend code.

### Trap 5 Lambda is compute, not storage

Lambda processes code. It does not store files like S3 or data like DynamoDB.

---

## Easy real-world example

Imagine a photo-sharing app.

When a user uploads a photo

 the photo goes to Amazon S3
 S3 triggers AWS Lambda
 Lambda creates a smaller thumbnail image
 the thumbnail is saved back to S3

Why is this useful
Because the code runs only when needed, scales automatically, and you do not manage servers.

---

## Invocation and Architecture Supplement

A function combines code, runtime, handler, resources, timeout, configuration, and an execution role. Synchronous callers wait. Asynchronous invocation queues events and can retry. Event source mappings poll streams or queues in batches. Retry rules vary, so use idempotency and supported destinations or dead-letter queues.

Lambda creates ephemeral environments as concurrency grows, subject to controls. Environments may be reused, so durable state belongs externally. Cold starts are initialization latency. VPC attachment enables private access but needs correct networking. CloudWatch provides logs and metrics.

AWS secures hosts. Customers secure code, dependencies, data, triggers, configuration, execution roles, and resource policies. The execution role grants outward access; the resource policy controls invocation. Pricing is conceptual: requests plus execution resources and related services.

Automatic scaling does not remove concurrency limits or downstream bottlenecks. Lambda suits variable event-driven work; EC2 or containers may suit long-running, special-host, or steady workloads.

### Knowledge Check

1. What controls invocation permission? **A resource-based policy.**
2. What polls SQS or streams? **An event source mapping.**
3. Where should durable state live? **Outside the execution environment.**

## Official References

- [Lambda concepts](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html)
- [Lambda invocation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html)
- [Lambda concurrency](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html)
- [Handling errors](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html)

Official references checked: 2026-07-22.

## Final summary

AWS Lambda is AWS’s serverless compute service.

It lets you run code without provisioning or managing servers. It works best for event-driven tasks, scales automatically, and charges you only when your code runs.

For the exam, remember Lambda as a top choice for automatic, event-based, serverless execution.

---

## Short exam answer

AWS Lambda is a serverless compute service that runs code in response to events without requiring users to provision or manage servers.

---

## Memory trick

Think

“Lambda = Let AWS run my code when something happens.”

Or even shorter

“No servers, just code.”
