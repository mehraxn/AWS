# AWS Global Accelerator

## Simple definition

AWS Global Accelerator is a networking service that improves the performance, availability, and reliability of applications for users around the world.

## Core idea in plain English

Think of AWS Global Accelerator as a fast global front door for your application.

Instead of sending users over the unpredictable public internet for most of the trip, it brings them into the AWS global network as quickly as possible and routes them to the best healthy application endpoint.

## Main use cases

 Speed up global applications for users in different countries
 Improve availability for multi-Region applications
 Provide static IP addresses for a global application
 Support TCP and UDP applications such as APIs, gaming, VoIP, and real-time apps
 Fail over traffic quickly if one endpoint becomes unhealthy

## Key features

 Static anycast IP addresses for your application
 Uses the AWS global network to improve performance
 Health checks and automatic failover to healthy endpoints
 Supports Application Load Balancers, Network Load Balancers, EC2 instances, and Elastic IP addresses as endpoints
 Works for TCP and UDP traffic
 Can route traffic to the closest healthy Region
 Helps improve application availability and user experience worldwide

## How it works

1. You create a Global Accelerator.
2. AWS gives you static IP addresses that users connect to.
3. Users enter the AWS network through the nearest edge location.
4. Global Accelerator sends traffic across the AWS backbone instead of leaving it on the public internet for longer than necessary.
5. Traffic is routed to the best healthy endpoint in one or more AWS Regions.
6. If an endpoint or Region becomes unhealthy, traffic is shifted to another healthy endpoint.

## Why it is important for the exam

AWS exam questions often test whether you understand that Global Accelerator is about

 improving global application performance
 using static IP addresses
 fast failover across Regions
 routing TCPUDP traffic over the AWS global network

This service matters when the question is about non-cacheable traffic, global users, high availability, or static entry points.

## Related AWS services and differences

### AWS Global Accelerator vs Amazon CloudFront

 Global Accelerator improves performance for applications by routing traffic at the network layer.
 CloudFront is a CDN that caches content closer to users.
 Use CloudFront when the goal is content delivery, caching, websites, images, video, and staticdynamic web content.
 Use Global Accelerator when the goal is better routing for TCPUDP applications, static IPs, and fast failover.

### AWS Global Accelerator vs Amazon Route 53

 Route 53 is a DNS service.
 Route 53 can route users using DNS policies like latency-based routing or failover routing.
 Global Accelerator gives static anycast IPs and routes traffic at the network edge over the AWS backbone.
 Route 53 depends on DNS responses and DNS caching; Global Accelerator can react faster to endpoint health changes.

### AWS Global Accelerator vs Elastic Load Balancing (ALBNLB)

 ALBNLB distribute traffic within or into a Region.
 Global Accelerator sits in front of regional endpoints and helps global users reach the best Region.
 You often use Global Accelerator with ALB or NLB, not instead of them.

## Common exam traps

 Trap 1 Thinking Global Accelerator is the same as CloudFront.
  It is not. CloudFront is mainly for content delivery and caching. Global Accelerator is for routing traffic to applications more efficiently.

 Trap 2 Thinking Route 53 and Global Accelerator do the same thing.
  They are different. Route 53 answers DNS queries. Global Accelerator provides static IPs and network-level traffic acceleration.

 Trap 3 Forgetting that Global Accelerator is useful for TCPUDP, not just websites.

 Trap 4 Assuming it replaces load balancers.
  It usually works with ALB or NLB.

 Trap 5 Missing the phrase static IP addresses.
  This is one of the biggest clues in exam questions.

## Easy real-world example

A company has customers in Europe, Asia, and the US using a live trading app.

The app runs in multiple AWS Regions behind load balancers. The company wants

 faster performance for global users
 automatic failover if one Region has a problem
 fixed IP addresses that customers can allowlist in firewalls

A strong solution is AWS Global Accelerator.

## Final summary

AWS Global Accelerator is a service that helps global users reach your application faster and more reliably.

It works by giving your app static IP addresses, bringing users into the AWS network at the nearest edge location, and routing them to the best healthy endpoint.

For the exam, remember this

 Global users
 better performance
 static IPs
 TCPUDP support
 fast failover across Regions

## Short exam answer

AWS Global Accelerator is a networking service that improves the availability and performance of internet applications by routing users to healthy endpoints over the AWS global network using static anycast IP addresses.

## Memory trick

Global Accelerator = Global fast lane with fixed IPs.

Think

 Global = worldwide users
 Accelerator = faster path
 Fixed IPs = static entry point
 Healthy endpoint routing = better availability
