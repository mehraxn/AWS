# Amazon API Gateway

## Simple definition

Amazon API Gateway is a fully managed AWS service that helps you create, publish, secure, monitor, and manage APIs.

In simple words, it is the front door that lets apps, users, or systems send requests to your backend services.

---

## Core idea in plain English

Think of Amazon API Gateway like a receptionist in front of your application.

Clients send requests to API Gateway.
API Gateway then sends those requests to the correct backend, such as:

* AWS Lambda
* Amazon EC2
* containers running on Amazon ECS or Amazon EKS
* applications behind a load balancer
* other AWS services

It also helps control who can access the API, how many requests are allowed, and how requests are monitored.

---

## Main use cases

### 1. Create APIs for mobile and web applications

API Gateway is commonly used when apps need a secure and managed way to communicate with backend systems.

It gives developers a single front door for application requests.

### 2. Build serverless applications with AWS Lambda

One of the most common uses of API Gateway is to expose Lambda functions as API endpoints.

This is a very popular serverless design pattern in AWS.

### 3. Expose backend services securely

A company may want to let customers, partners, or internal teams access backend services through APIs.

API Gateway helps secure and control this access.

### 4. Support microservices architectures

In a microservices environment, different services often need a clean and managed API layer.

API Gateway can act as the entry point for these services.

### 5. Build real-time applications

API Gateway supports WebSocket APIs, which are useful for two-way real-time communication.

Examples include chat apps, live dashboards, and real-time notifications.

### 6. Manage traffic and protect backends

API Gateway can throttle requests and help protect backend services from too many incoming calls.

This is useful for both performance and stability.

---

## Key features

### 1. Fully managed API service

AWS manages the infrastructure behind API Gateway.

This means you do not need to provision or manage servers just to expose APIs.

### 2. Supports multiple API types

API Gateway supports REST APIs, HTTP APIs, and WebSocket APIs.

This gives flexibility depending on whether you need advanced features, lower-cost APIs, or real-time communication.

### 3. Strong Lambda integration

API Gateway works very naturally with AWS Lambda.

This makes it a core service in many serverless application designs.

### 4. Authentication and authorization support

API Gateway can help control who is allowed to call your APIs.

This is important for protecting backend systems and sensitive application functions.

### 5. Throttling and traffic control

API Gateway can limit how many requests clients can send.

This helps protect backends from overload and supports fair API usage.

### 6. Monitoring with Amazon CloudWatch

You can monitor API performance and usage through CloudWatch.

This helps teams observe API health and troubleshoot issues.

### 7. Request validation and API management features

Some API types support features such as request validation, API keys, and usage plans.

These features are especially important in more advanced API management scenarios.

### 8. Caching support

API Gateway can cache responses in some cases to improve performance.

This can reduce calls to backend systems and lower response times.

### 9. Deployment stages

You can create stages such as dev, test, and prod.

This helps teams manage different versions and environments of an API.

### 10. Custom domain names

API Gateway supports custom domain names for APIs.

This gives applications a more professional and user-friendly API endpoint.

### 11. Flexible backend integration

API Gateway can connect to Lambda, EC2-based apps, containers, load-balanced apps, and some AWS service integrations.

This makes it useful in many architectures, not only serverless ones.

---

## How it works

### Basic flow

1. A client sends a request to an API endpoint.
2. Amazon API Gateway receives the request.
3. API Gateway checks things like authentication, authorization, and throttling.
4. It forwards the request to the backend service.
5. The backend processes the request.
6. API Gateway returns the response to the client.

### Example backend targets

* AWS Lambda function
* application running on Amazon EC2
* containerized service
* AWS service integration

### API types you should know

#### 1. REST API

This is the more feature-rich API type.

Use it when you need advanced API management features such as:

* API keys
* usage plans
* request validation
* more advanced controls

#### 2. HTTP API

This is a simpler and lower-cost option for many modern APIs.

Use it when you want:

* simple API proxying
* low latency
* serverless integrations
* common modern API use cases

#### 3. WebSocket API

Use this for two-way real-time communication.

Examples:

* chat applications
* live dashboards
* real-time notifications

---

## Why it is important for the exam

Amazon API Gateway is important because AWS exam questions often test whether you understand:

* which AWS service exposes APIs securely
* which service works naturally with Lambda for serverless APIs
* the difference between API Gateway and services like Elastic Load Balancing
* when to use API Gateway for mobile, web, and microservices access
* when WebSocket APIs are needed for real-time communication

For Cloud Practitioner, the exam usually tests the main purpose of API Gateway, not deep developer configuration.

The key exam idea is:

**API Gateway is used to create, publish, secure, monitor, and manage APIs.**

---

## Related AWS services and differences

### API Gateway vs AWS Lambda

* Lambda runs the code.
* API Gateway receives API requests and sends them to Lambda or other backends.

**Easy memory line:**
API Gateway is the front door. Lambda is the worker behind the door.

### API Gateway vs Elastic Load Balancing

* Elastic Load Balancing distributes traffic across targets.
* API Gateway is specifically for creating and managing APIs.

**Exam trap:**
If the question is about publishing and managing APIs, choose API Gateway, not ELB.

### API Gateway vs AWS AppSync

* AppSync is mainly for GraphQL APIs.
* API Gateway is for REST, HTTP, and WebSocket APIs.

### API Gateway vs Amazon CloudFront

* CloudFront is a content delivery network.
* API Gateway manages API requests.

They can work together, but they are not the same service.

### API Gateway vs AWS WAF

* AWS WAF protects web applications and APIs from common web exploits.
* API Gateway manages the API itself.

### API Gateway vs Amazon Cognito

* Cognito helps with user authentication and identity.
* API Gateway can use authentication methods and protect access to APIs.

---

## Common exam traps

### 1. Confusing API Gateway with AWS Lambda

This is one of the most common mistakes.

API Gateway does not run your business logic. It receives the request and sends it to a backend such as Lambda.

### 2. Confusing API Gateway with Elastic Load Balancing

These services can both sit in front of applications, but they are used for different purposes.

If the question is about creating, publishing, securing, and managing APIs, think of API Gateway.
If the question is about distributing traffic across servers or targets, think of ELB.

### 3. Thinking API Gateway is only for serverless applications

API Gateway is strongly associated with Lambda, but it is not limited to Lambda.

It can also connect to EC2-based apps, containers, and other backend systems.

### 4. Forgetting WebSocket support

Some learners only remember REST-style APIs.

But API Gateway also supports WebSocket APIs for real-time two-way communication such as chat systems and live updates.

### 5. Mixing REST API and HTTP API

For Cloud Practitioner, remember this simple rule:

* REST API = more features and more advanced API management
* HTTP API = simpler, lower cost, and often lower latency for common use cases

You usually do not need very deep detail beyond that for this exam.

### 6. Thinking API Gateway and CloudFront do the same job

CloudFront focuses on content delivery and caching closer to users.

API Gateway focuses on handling and managing API requests.

### 7. Forgetting security and traffic control features

API Gateway is not only about routing requests.

It also helps with throttling, authorization, monitoring, and controlling API access.

---

## Easy real-world example

Imagine a food delivery app.

The mobile app needs to:

* log in users
* show restaurants
* place orders
* track order status

The app sends requests to Amazon API Gateway.
API Gateway sends each request to the correct backend service or Lambda function.

So:

* `/restaurants` gets restaurant data
* `/orders` creates an order
* `/tracking` returns delivery status

API Gateway helps secure the APIs, limit traffic, and monitor usage.

---

## If I were an examiner ...

Here are the kinds of questions I would ask to test your understanding.

### Question 1

Which AWS service is used to create, publish, maintain, monitor, and secure APIs?

**Expected answer:** Amazon API Gateway

### Question 2

A company wants to build a serverless backend for a mobile application. Which AWS service can expose Lambda functions as API endpoints?

**Expected answer:** Amazon API Gateway

### Question 3

Which API Gateway API type is used for real-time two-way communication such as chat applications?

**Expected answer:** WebSocket API

### Question 4

A company wants a fully managed service that acts as the front door for backend services and applications. Which AWS service should they choose?

**Expected answer:** Amazon API Gateway

### Question 5

What is the main difference between API Gateway and Elastic Load Balancing?

**Expected answer:** API Gateway is for creating and managing APIs, while ELB distributes traffic across targets.

### Question 6

A question mentions API keys, usage plans, and advanced API management. Which API Gateway type should you think about first?

**Expected answer:** REST API

---

## Exam keywords to remember

These are important keywords and phrases that may appear in AWS exam questions about API Gateway:

* create APIs
* publish APIs
* manage APIs
* secure APIs
* monitor APIs
* front door for applications
* API endpoint
* serverless API
* Lambda integration
* REST API
* HTTP API
* WebSocket API
* real-time communication
* chat application
* throttling
* authentication
* authorization
* usage plans
* API keys
* request validation
* CloudWatch monitoring
* custom domain name
* backend integration
* expose services through APIs

---

## Final summary

Amazon API Gateway is the AWS service used to build and manage APIs.

It acts like the front door for applications and backend services.
It accepts requests from clients, applies security and traffic controls, sends requests to the correct backend, and returns responses.

For the exam, remember these big ideas:

* API Gateway is for APIs
* it is commonly used with Lambda
* it supports REST, HTTP, and WebSocket APIs
* it helps with security, monitoring, and traffic control

---

## Short exam answer

Amazon API Gateway is a fully managed AWS service for creating, publishing, securing, monitoring, and managing APIs at scale.

---

## Memory trick

**API Gateway = the gate for API traffic**

Or even simpler:

Clients knock on the gate. API Gateway decides where the request goes.

---

## One last exam coach tip

When you see words like:

* create APIs
* publish APIs
* secure APIs
* monitor APIs
* front door for applications
* expose Lambda through an API
* WebSocket chat application

Your mind should quickly go to:

**Amazon API Gateway**

## Batch 5 API Architecture Supplement

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

Checked against current official AWS documentation on 2026-07-23.

### API Types

| Type | Best fit | Important distinction |
|---|---|---|
| REST API | Feature-rich REST management and REST-specific capabilities | Supports features such as REST API stage caching; verify feature support |
| HTTP API | Lower-complexity/lower-cost HTTP front door | Not every REST API feature is available |
| WebSocket API | Stateful two-way real-time messaging | Routes connection/message events rather than ordinary request/response only |

### Endpoints and Integrations

REST APIs can use Regional, edge-optimized, or private endpoint types where supported. HTTP/WebSocket endpoint choices differ; never assume feature parity. Private REST APIs use interface VPC endpoints. VPC links connect supported APIs privately to VPC backends such as load balancers. [VPC endpoint details](../../07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md) remain in the networking owner.

Backends include Lambda proxy/non-proxy integrations, public HTTP services, supported AWS service integrations, VPC links, and REST mock integrations. API Gateway invokes Lambda only when the function resource policy permits it; private integrations also need correct network and backend security.

### Authentication and Authorization

Options depend on API type and include IAM/SigV4, Cognito user-pool authorizers, JWT authorizers for HTTP APIs, Lambda authorizers, resource policies, and mutual TLS/custom domains where supported. Authentication establishes identity; authorization decides allowed operations. API keys and usage plans identify/measure clients but are not primary authentication by themselves.

### Throttling, Caching, and Resilience

Token-bucket throttling protects API and backend capacity but limits are best-effort targets; clients handle `429` with bounded backoff. Usage plans/quotas apply to supported REST API designs. REST API stage caching can reduce backend requests but introduces TTL, invalidation, cache-key, sensitive-data, and cost decisions; do not claim HTTP or WebSocket APIs have the same caching feature.

API Gateway is managed and Regional in control/data placement according to endpoint type, but backend resilience still matters. Use multi-AZ backends, Lambda retry/idempotency as appropriate, client timeouts/retries, health-aware Regional architecture, and explicit multi-Region routing when required.

### Security and Cost

Use least-privilege invoke/admin IAM, authorizers, resource policies, TLS, AWS WAF where supported, access/execution logs, CloudTrail, backend permissions, validation, and throttling. Avoid logging credentials or sensitive payloads. Cost depends on API type, requests/messages/connection duration, transfer, REST caching, logging, and backend services.

### CPP and SAA Scenarios

1. Public serverless HTTP API with straightforward JWT auth: compare HTTP API plus Lambda.
2. Feature-rich managed REST API requiring REST stage cache/usage plans: evaluate REST API.
3. Chat with bidirectional connections: WebSocket API.
4. Private REST API callable through a VPC endpoint: private REST endpoint with resource policy.
5. Private load-balanced VPC backend: supported VPC Link integration.

### Common Mistakes

- Assuming every API type supports every feature.
- Using API keys as authentication.
- Treating throttling as a guaranteed hard ceiling.
- Enabling cache without freshness/security design.
- Assuming API Gateway makes an unhealthy backend highly available.

### Knowledge Check

1. Which API type is for bidirectional real-time communication? 2. Which API type supports REST stage caching? 3. Are API keys primary authentication? 4. What does VPC Link solve? 5. What should clients do after throttling?

<details><summary>Answers</summary>

1. WebSocket. 2. REST API. 3. No. 4. Private integration to supported VPC backends. 5. Handle 429 responses with bounded backoff/retry.

</details>

## References

- [API Gateway API types](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html)
- [Choosing HTTP or REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)
- [API Gateway authorization](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)
- [Private APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)
- [API caching](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)
- [API Gateway pricing](https://aws.amazon.com/api-gateway/pricing/)
