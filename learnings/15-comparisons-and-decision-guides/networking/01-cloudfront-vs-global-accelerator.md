# Amazon CloudFront vs AWS Global Accelerator

## Simple definition of each service

### Amazon CloudFront

Amazon CloudFront is a content delivery network (CDN). It speeds up delivery of websites, videos, images, APIs, and other web content by caching content at AWS edge locations close to users.

### AWS Global Accelerator

AWS Global Accelerator is a global traffic routing service. It improves the performance and availability of internet applications by sending users into the AWS global network quickly and routing them to the best healthy regional endpoint.

---

## Core idea in plain English

CloudFront is mainly about delivering content faster, especially when content can be cached at the edge.

Global Accelerator is mainly about getting users to the right application endpoint faster and more reliably, even across multiple AWS Regions.

A simple way to remember it

 CloudFront = fast content delivery
 Global Accelerator = fast global application routing

---

## Main purpose of each service

### CloudFront

The main purpose of CloudFront is to reduce latency for web content by storing copies of content closer to users.

### Global Accelerator

The main purpose of Global Accelerator is to improve availability and performance for applications by using AWS’s global network and static anycast IP addresses.

---

## Key differences

### 1. Main job

 CloudFront Content delivery and caching
 Global Accelerator Traffic routing and failover

### 2. Works at what level

 CloudFront Mainly HTTP and HTTPS web traffic
 Global Accelerator TCP and UDP application traffic

### 3. Caching

 CloudFront Yes, caching is a core feature
 Global Accelerator No, it does not cache content

### 4. Entry method

 CloudFront Users access a distribution by DNS name
 Global Accelerator Users connect through static anycast IP addresses

### 5. Best fit

 CloudFront Websites, static assets, video delivery, API acceleration
 Global Accelerator Global apps needing low latency, static IPs, health-based routing, and multi-Region failover

### 6. Failover style

 CloudFront Can improve performance globally, but it is not mainly a traffic failover service
 Global Accelerator Built for routing users to optimal healthy endpoints across Regions

---

## Similarities

Both services

 Use the AWS global network
 Help reduce latency for global users
 Use AWS edge locations
 Improve user experience for internet-facing applications
 Can be used together in some architectures

---

## When to use Amazon CloudFront

Use CloudFront when

 You want to speed up a website globally
 You need to cache static files like images, CSS, JavaScript, and videos
 You want to protect and accelerate content from an S3 bucket, ALB, EC2 instance, or custom origin
 You want edge security features for web delivery
 You want to improve API performance over HTTPHTTPS

### Typical CloudFront use cases

 Static website delivery
 Streaming and video distribution
 Global web application acceleration
 Secure content delivery
 Edge processing with CloudFront Functions or Lambda@Edge

---

## When to use AWS Global Accelerator

Use Global Accelerator when

 You have users around the world connecting to an application over TCP or UDP
 You want static global IP addresses for your application
 You need automatic failover between multiple Regions
 You want better performance for non-cacheable traffic
 You want users routed to the nearest healthy application endpoint

### Typical Global Accelerator use cases

 Multi-Region applications
 Gaming applications
 Real-time communications
 Financial trading or latency-sensitive systems
 Applications that need fixed public IP addresses

---

## Real exam-style decision rule

Use this simple rule in the exam

 If the question is about caching content at edge locations, choose Amazon CloudFront.
 If the question is about static IPs, global traffic routing, health checks, or multi-Region failover, choose AWS Global Accelerator.

Another easy rule

 Content problem = CloudFront
 Routing problem = Global Accelerator

---

## Side-by-side comparison table

 Feature                Amazon CloudFront                      AWS Global Accelerator                             
 ---------------------  -------------------------------------  -------------------------------------------------- 
 Main role              Content delivery network               Global traffic accelerator                         
 Primary goal           Deliver content faster                 Route application traffic faster and more reliably 
 Caching                Yes                                    No                                                 
 Protocol focus         HTTPHTTPS                             TCPUDP                                            
 Uses edge locations    Yes                                    Yes                                                
 Static anycast IPs     No                                     Yes                                                
 Multi-Region failover  Not the main feature                   Major feature                                      
 Best for               Websites, APIs, media, static content  Global applications, gaming, real-time apps        
 Works with             S3, ALB, EC2, custom origins           ALB, NLB, EC2, Elastic IP                          
 Exam memory            CDN                                    Global app entry point                             

---

## Main use cases

### CloudFront use cases

 Accelerating websites
 Delivering static content
 Serving video and media globally
 Securing content delivery
 Improving API delivery over HTTPHTTPS

### Global Accelerator use cases

 Improving global application availability
 Directing traffic to healthy regional endpoints
 Providing static entry IP addresses
 Reducing latency for global TCPUDP applications
 Supporting disaster recovery and failover designs

---

## Key features

### CloudFront key features

 Global edge caching
 Fast delivery for static and dynamic content
 HTTPS support
 Integration with S3, EC2, ALB, Route 53, WAF, and Shield
 Signed URLs and signed cookies
 CloudFront Functions and Lambda@Edge

### Global Accelerator key features

 Static anycast IP addresses
 Traffic enters AWS network close to the user
 Endpoint health checks
 Fast failover across Regions
 Traffic dials for traffic control
 Works with Application Load Balancers, Network Load Balancers, EC2, and Elastic IPs

---

## How each service works

### How CloudFront works

1. A user requests content.
2. The request goes to the nearest CloudFront edge location.
3. If the content is already cached, CloudFront returns it immediately.
4. If not cached, CloudFront gets it from the origin.
5. CloudFront can cache it for future requests.

### How Global Accelerator works

1. A user connects to the application using static anycast IP addresses.
2. Traffic enters the AWS edge network at the nearest location.
3. Global Accelerator sends the traffic over the AWS global backbone.
4. It routes traffic to the best healthy endpoint in one or more Regions.
5. If one endpoint or Region fails, traffic is redirected to another healthy endpoint.

---

## Why the difference matters for the exam

This comparison matters because these services sound similar. Both improve global performance, and both use AWS edge infrastructure, so students often confuse them.

The exam usually tests the main purpose

 CloudFront is for faster content delivery
 Global Accelerator is for faster and more reliable application routing

If you remember that one is a CDN and the other is a network traffic accelerator, you will avoid many mistakes.

---

## Related AWS services and differences

### Amazon Route 53 vs Global Accelerator

 Route 53 is a DNS service
 Global Accelerator provides static anycast IPs and routes traffic over the AWS global network
 Route 53 can do DNS-based routing, but it does not work the same way as Global Accelerator

### CloudFront vs S3

 S3 stores objects
 CloudFront delivers them faster around the world

### CloudFront vs Elastic Load Balancing

 CloudFront sits closer to users and can cache content
 ELB distributes traffic across backend targets inside a Region

### Global Accelerator vs ELB

 ELB balances traffic within a Region
 Global Accelerator routes traffic globally across Regions to the best endpoint

### CloudFront and Global Accelerator together

They are not always competitors. In some architectures, you can use both

 CloudFront for web content delivery and caching
 Global Accelerator for global routing to regional application endpoints

---

## Common exam traps

### Trap 1 Both improve performance, so they are the same

They are not the same.

 CloudFront improves delivery of content
 Global Accelerator improves routing of application traffic

### Trap 2 Global Accelerator caches content

Wrong. Global Accelerator does not cache content.

### Trap 3 CloudFront gives static IP addresses

Wrong. Static anycast IPs are a feature of Global Accelerator.

### Trap 4 CloudFront is only for static content

Not fully true. CloudFront is best known for caching static content, but it can also accelerate dynamic content and APIs over HTTPHTTPS.

### Trap 5 Route 53 and Global Accelerator are identical

Wrong. Route 53 is DNS-based routing. Global Accelerator uses static IPs and the AWS global network for traffic routing.

---

## Easy real-world examples

### CloudFront example

A company has a global shopping website with lots of images, videos, CSS, and JavaScript files. Users in Asia, Europe, and America should load the site quickly.

Use Amazon CloudFront to cache and deliver the website content from edge locations close to users.

### Global Accelerator example

A gaming company runs its backend in multiple AWS Regions. Players worldwide need low latency and automatic failover if one Region has a problem.

Use AWS Global Accelerator to route players to the nearest healthy endpoint using the AWS global network.

---

## Final summary

Amazon CloudFront and AWS Global Accelerator both improve global performance, but they solve different problems.

CloudFront is mainly a CDN. It makes websites and content faster by caching data close to users.

Global Accelerator is mainly a traffic routing service. It improves application availability and performance by using static anycast IPs and routing traffic to the best healthy endpoint.

For the exam, remember this

 Choose CloudFront for content delivery and caching
 Choose Global Accelerator for global routing, static IPs, and failover

---

## Short exam answer

Amazon CloudFront is a CDN that speeds up delivery of static and dynamic web content by caching content at edge locations.

AWS Global Accelerator improves performance and availability for global applications by routing TCPUDP traffic through the AWS global network to the best healthy endpoint using static anycast IP addresses.

---

## Memory trick

Think of it like this

 CloudFront = Front door for content
 Global Accelerator = Fast highway for application traffic

Or even shorter

 CloudFront caches
 Global Accelerator routes
