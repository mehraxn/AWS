# Amazon CloudFront

## Simple Definition

Amazon CloudFront is AWS’s content delivery network (CDN). It helps deliver websites, videos, APIs, and files to users faster by caching content closer to them at edge locations around the world.

## Core Idea in Plain English

Instead of making every user request travel all the way to your main server, CloudFront keeps copies of content in many places around the world. That means users get content from a nearby location, so it loads faster.

## Main Use Cases

 Speed up website delivery for global users
 Deliver static content such as images, CSS, JavaScript, and videos
 Improve performance for dynamic websites and APIs
 Protect web applications with AWS security services
 Stream live or on-demand video content

## Key Features

 Global edge location network
 Caching of content close to users
 Low latency and faster delivery
 HTTPS support for secure delivery
 Integration with AWS Shield for DDoS protection
 Integration with AWS WAF for web application firewall rules
 Works with Amazon S3, Elastic Load Balancing, EC2, and custom origins
 Supports CloudFront Functions and Lambda@Edge for edge logic
 Can restrict access to content

## How It Works

1. You create a CloudFront distribution.
2. You choose an origin, which is the source of your content.

    This could be an S3 bucket
    An Application Load Balancer
    An EC2-based web server
    Another custom HTTP server
3. A user requests your website or file.
4. CloudFront sends the request to the nearest edge location.
5. If the content is already cached there, CloudFront sends it immediately.
6. If it is not cached, CloudFront fetches it from the origin, returns it to the user, and stores a copy in the cache for future requests.

## Why It Is Important for the Exam

CloudFront is important because AWS exams often test

 The idea of a CDN
 How to improve global performance
 How to reduce latency
 How AWS services work together for security and content delivery

For the Cloud Practitioner exam, remember this

CloudFront = faster content delivery through global caching at edge locations.

## Related AWS Services and Differences

### Amazon S3 vs CloudFront

 Amazon S3 stores files and objects
 CloudFront delivers those files faster to users worldwide
 S3 is storage, CloudFront is delivery

### Elastic Load Balancing vs CloudFront

 Elastic Load Balancing distributes traffic across servers
 CloudFront caches and delivers content globally
 Load Balancer helps inside your application architecture, CloudFront helps users get content faster from nearby edge locations

### AWS Global Accelerator vs CloudFront

 CloudFront is mainly for caching and content delivery
 Global Accelerator improves performance for non-cacheable applications by routing traffic through the AWS global network
 CloudFront is best when caching content helps

### AWS WAF and AWS Shield vs CloudFront

 AWS WAF protects web apps using filtering rules
 AWS Shield protects against DDoS attacks
 CloudFront is the delivery service, but it can work together with WAF and Shield for better protection

### Route 53 vs CloudFront

 Route 53 is DNS and routing
 CloudFront is content delivery and caching
 Route 53 helps users find the right endpoint, CloudFront helps deliver content faster once they get there

## Common Exam Traps

 Thinking CloudFront is a storage service. It is not. S3 stores data; CloudFront delivers it.
 Confusing CloudFront with Elastic Load Balancing. CloudFront is a CDN, not a traffic balancer for backend servers.
 Confusing CloudFront with Global Accelerator. CloudFront focuses on cached content delivery. Global Accelerator focuses on routing traffic for applications.
 Forgetting that CloudFront can use S3 or custom origins.
 Missing the keyword edge locations. This is one of the biggest CloudFront exam clues.

## Easy Real-World Example

A company has a website hosted in the US, but customers are in Europe, Asia, and South America.

Without CloudFront, every user request goes all the way to the US server, which can be slower.

With CloudFront, copies of the website’s images, videos, and files are cached at edge locations around the world. Users get the content from a nearby location, so the website loads much faster.

## Final Summary

Amazon CloudFront is AWS’s CDN service. It speeds up delivery of websites, APIs, videos, and static files by caching content at global edge locations. It improves performance, reduces latency, and can also improve security when combined with AWS Shield and AWS WAF. For the exam, the most important idea is that CloudFront makes content delivery faster for users around the world.

## Short Exam Answer

Amazon CloudFront is a content delivery network (CDN) that caches content at edge locations worldwide so users can access websites, APIs, and files with lower latency and faster performance.

## Memory Trick

CloudFront = Content in front of the user

Think

 Cloud = AWS global network
 Front = sits in front of your origin server
 It brings content closer to users

So remember

CloudFront puts content closer to users at the front edge of the network.
