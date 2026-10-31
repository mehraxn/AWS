# AWS WAF

## Simple definition

AWS WAF stands for Web Application Firewall. It is a security service that helps protect your web applications from common web attacks.

## Core idea in plain English

Think of AWS WAF like a smart security guard in front of your website or web app. It checks incoming web requests and decides whether to allow, block, or monitor them based on rules you define.

## Main use cases

AWS WAF is mainly used to protect websites and APIs from harmful traffic.

Common use cases

 Blocking SQL injection attacks
 Blocking cross-site scripting (XSS)
 Limiting requests from bots or abusive users
 Allowing or blocking traffic from specific IP addresses or countries
 Protecting public applications from common web threats

## Key features

 Rule-based filtering of web traffic
 Allow, block, or count requests
 Managed rules provided by AWS and AWS Partners
 IP-based rules
 Geographic blocking
 Rate-based rules to reduce abuse and traffic floods
 Integration with AWS services like CloudFront, Application Load Balancer, API Gateway, and App Runner
 Visibility through Amazon CloudWatch and AWS WAF logs

## How it works

AWS WAF works by inspecting HTTP and HTTPS requests sent to your application.

You create a web ACL (Access Control List), which is a set of rules.
Each rule checks for conditions such as

 IP address
 HTTP headers
 URI string
 Query string
 Request body
 Request rate
 Country of origin

When a request reaches the protected resource, AWS WAF checks it against the rules in the web ACL.
Then AWS WAF takes an action such as

 Allow the request
 Block the request
 Count the request for monitoring

Example flow

1. A user sends a request to a website.
2. AWS WAF inspects the request.
3. The request is compared against rules.
4. Malicious traffic is blocked, and safe traffic is allowed through.

## Why it is important for the exam

AWS Cloud Practitioner exams often test whether you know which AWS security service protects web applications from common web attacks.

This is where AWS WAF is important.

You should remember

 AWS WAF protects Layer 7 traffic, meaning HTTPHTTPS web traffic
 It is used to filter web requests before they reach your application
 It helps protect against common attacks like SQL injection and XSS

If the question mentions protecting a website, API, or application from malicious web requests, AWS WAF is often the correct answer.

## Related AWS services and differences

### AWS WAF vs AWS Shield

 AWS WAF protects against common web application attacks using custom or managed rules
 AWS Shield protects against DDoS attacks

Easy memory rule

 WAF = web request filtering
 Shield = DDoS protection

### AWS WAF vs Network ACL

 AWS WAF works at the web application level for HTTPHTTPS traffic
 Network ACL works at the subnet level inside a VPC and controls network traffic

### AWS WAF vs Security Groups

 AWS WAF filters web requests using application-layer rules
 Security Groups control inbound and outbound traffic for EC2 instances and other resources

### AWS WAF vs Firewall Manager

 AWS WAF is the protection rule engine for web apps
 AWS Firewall Manager helps centrally manage firewall rules across multiple AWS accounts and resources

## Common exam traps

 Confusing AWS WAF with AWS Shield

   WAF is for web request filtering
   Shield is for DDoS protection

 Thinking AWS WAF protects all network traffic

   It mainly protects web applications using HTTPHTTPS

 Mixing AWS WAF with Security Groups or Network ACLs

   WAF is application-layer protection
   Security Groups and NACLs are network-layer controls

 Forgetting that AWS WAF uses a web ACL

   The web ACL is the collection of rules attached to a resource

## Easy real-world example

Imagine an online store hosted on AWS.
Hackers try to send malicious requests to the login page and search box.

The company uses AWS WAF with managed rules to

 Block SQL injection attempts
 Block XSS attempts
 Rate-limit repeated bad requests from the same IP

Result normal shoppers can use the site, but malicious web requests are blocked before reaching the application.

## Final summary

AWS WAF is a web security service that protects websites, APIs, and web applications from common web attacks.
It works by inspecting incoming HTTPHTTPS requests and applying rules to allow, block, or count traffic.
For the exam, remember that AWS WAF is the AWS service used to protect applications from threats like SQL injection, XSS, bad bots, and abusive request patterns.

## Short exam answer

AWS WAF is a web application firewall that protects web applications from common web exploits by filtering HTTPHTTPS requests based on rules.

## Memory trick

Think
WAF = Web App Filter

It stands in front of your website and filters bad web traffic before it gets in.
