# SSL Termination — Complete README

## 1. What Is SSL Termination

SSL termination is the process where an encrypted HTTPS connection is decrypted at an intermediate device or service, such as a load balancer, reverse proxy, API gateway, or CDN, instead of being decrypted directly by the backend application server.

In simple words

 SSL termination means HTTPS traffic reaches a load balancer or proxy, the load balancer decrypts it, and then forwards the request to the backend server.

Even though the term says SSL, modern systems usually use TLS. However, people still commonly say SSL termination.

So, more accurately, SSL termination means TLS termination.

---

## 2. Before Understanding SSL Termination What Are SSL and TLS

### SSL

SSL stands for Secure Sockets Layer. It was an older security protocol used to encrypt communication between clients and servers.

### TLS

TLS stands for Transport Layer Security. It is the modern and secure replacement for SSL.

Today, when people say

```text
SSL certificate
SSL connection
SSL termination
```

they usually mean TLS in practice.

### Why SSLTLS Exists

SSLTLS protects data moving between a client and a server.

For example, when a user visits

```text
httpsexample.com
```

the browser and server create a secure encrypted connection.

This protects sensitive data such as

 usernames
 passwords
 payment information
 cookies
 API tokens
 personal information

Without SSLTLS, traffic could be read or modified by attackers on the network.

---

## 3. HTTP vs HTTPS

### HTTP

HTTP is plain-text web traffic.

Example

```text
Client → Server using HTTP
```

The problem with HTTP is that the data is not encrypted. Anyone who can intercept the network traffic may be able to read it.

### HTTPS

HTTPS is HTTP protected by SSLTLS encryption.

Example

```text
Client → Server using HTTPS
```

HTTPS provides

 encryption
 authentication
 data integrity

### Simple Difference

```text
HTTP  = not encrypted
HTTPS = encrypted using SSLTLS
```

---

## 4. Basic Architecture Without SSL Termination

In a simple architecture, the backend server itself handles HTTPS.

```text
Client Browser
      
       HTTPS encrypted traffic
      v
Backend Web Server
```

In this case

1. The client connects to the backend server using HTTPS.
2. The backend server stores the SSLTLS certificate.
3. The backend server decrypts the traffic.
4. The backend application processes the request.

This works, but it can become difficult to manage when there are many backend servers.

For example, if you have 20 EC2 instances, you may need to install and manage certificates on all of them.

---

## 5. Basic Architecture With SSL Termination

With SSL termination, the HTTPS connection ends at the load balancer or proxy.

```text
Client Browser
      
       HTTPS encrypted traffic
      v
Load Balancer
      
       HTTP traffic or re-encrypted HTTPS traffic
      v
Backend Servers
```

In this case

1. The client sends HTTPS traffic to the load balancer.
2. The load balancer uses the SSLTLS certificate.
3. The load balancer decrypts the HTTPS request.
4. The load balancer forwards the request to the backend server.
5. The backend server responds to the load balancer.
6. The load balancer sends the response back to the client over HTTPS.

The important point is

 The user still uses HTTPS, but the HTTPS connection terminates at the load balancer.

---

## 6. Why Is It Called “Termination”

It is called termination because the encrypted SSLTLS session ends at that point.

For example

```text
Client → Load Balancer = HTTPS
Load Balancer → Backend = HTTP or HTTPS
```

The first encrypted connection is terminated at the load balancer.

That does not mean the request stops. It means the encryption layer is ended, decrypted, and then the request continues to the backend.

---

## 7. SSL Termination Step by Step

Assume a user visits

```text
httpsapp.example.com
```

The process looks like this

### Step 1 Client Starts HTTPS Connection

The browser connects to the public endpoint, usually a load balancer, using HTTPS on port 443.

```text
Client → Load Balancer  HTTPS port 443
```

### Step 2 Load Balancer Presents Certificate

The load balancer presents an SSLTLS certificate for the domain.

Example certificate domain

```text
app.example.com
```

The browser checks whether the certificate is trusted and valid.

### Step 3 TLS Handshake Happens

The client and load balancer perform a TLS handshake.

During this process, they agree on encryption settings and establish a secure session.

### Step 4 Client Sends Encrypted HTTP Request

The browser sends an encrypted request.

Example

```text
GET products HTTP1.1
Host app.example.com
```

But because it is inside HTTPS, outsiders cannot read it.

### Step 5 Load Balancer Decrypts the Request

The load balancer decrypts the request.

Now it can understand HTTP information such as

```text
Host app.example.com
Path products
Method GET
Headers
Cookies
```

### Step 6 Load Balancer Chooses a Backend Target

The load balancer decides where to send the request.

For example

```text
products → product-service
api      → api-service
admin    → admin-service
```

### Step 7 Load Balancer Sends Request to Backend

The load balancer forwards the request to the backend.

This backend connection can be either

```text
Load Balancer → Backend  HTTP
```

or

```text
Load Balancer → Backend  HTTPS
```

### Step 8 Backend Responds

The backend sends the response to the load balancer.

### Step 9 Load Balancer Encrypts Response Back to Client

The load balancer sends the response back to the client over the original HTTPS connection.

---

## 8. Important Traffic Patterns

There are three common traffic patterns.

---

## 8.1 Pattern 1 HTTPS From Client, HTTP To Backend

```text
Client
  
   HTTPS
  v
Load Balancer
  
   HTTP
  v
Backend Server
```

This is one of the most common forms of SSL termination.

### Meaning

The client-to-load-balancer connection is encrypted.

The load-balancer-to-backend connection is not encrypted.

### Why Use This

This is simpler because the backend servers do not need SSL certificates.

The load balancer handles

 certificate management
 TLS negotiation
 encryption and decryption

### When Is This Acceptable

This is often acceptable when the backend servers are inside a private trusted network, such as a private VPC subnet.

However, for highly sensitive systems, organizations may still require HTTPS between the load balancer and backend.

---

## 8.2 Pattern 2 HTTPS From Client, HTTPS To Backend

```text
Client
  
   HTTPS
  v
Load Balancer
  
   HTTPS
  v
Backend Server
```

This is sometimes called end-to-end encryption, although technically the load balancer still decrypts and then re-encrypts the traffic.

### Meaning

The load balancer terminates the client HTTPS connection, decrypts the request, and then creates a new HTTPS connection to the backend.

### Why Use This

This provides encryption on both network segments

```text
Client → Load Balancer
Load Balancer → Backend
```

### When Is This Useful

This is useful when

 compliance requires encryption everywhere
 backend traffic crosses less trusted networks
 the application handles sensitive data
 company security policy requires HTTPS all the way to the backend

---

## 8.3 Pattern 3 TCP Pass-Through Without SSL Termination

```text
Client
  
   HTTPS
  v
Load Balancer
  
   HTTPS still encrypted
  v
Backend Server
```

In this pattern, the load balancer does not decrypt the traffic.

It simply forwards encrypted TCP traffic to the backend.

The backend server performs SSLTLS decryption.

### Meaning

The SSLTLS session is terminated at the backend server, not at the load balancer.

### When Is This Used

This is used when

 the backend must own the certificate
 the load balancer should not inspect HTTP traffic
 true end-to-end TLS is required
 the load balancer operates at Layer 4 only

---

## 9. SSL Termination in AWS

In AWS, SSL termination is commonly done using

 Application Load Balancer
 Network Load Balancer
 CloudFront
 API Gateway

The most common exam-related example is an Application Load Balancer.

---

## 10. SSL Termination With Application Load Balancer

An Application Load Balancer, or ALB, operates at Layer 7 of the OSI model.

Layer 7 means the ALB understands HTTP and HTTPS.

A typical ALB HTTPS setup looks like this

```text
Client Browser
      
       HTTPS  443
      v
Application Load Balancer
      
       HTTP  80 or HTTPS  443
      v
Target Group
      
      v
EC2  ECS  IP  Lambda
```

### ALB Components Involved

To configure SSL termination on an ALB, you usually need

1. An HTTPS listener
2. An SSLTLS certificate
3. A target group
4. Backend targets
5. Listener rules

---

## 11. ALB HTTPS Listener

A listener checks for incoming connection requests.

For SSL termination, the ALB usually has a listener like this

```text
Protocol HTTPS
Port 443
```

This means the ALB accepts HTTPS traffic from clients.

The ALB needs a certificate to prove its identity to browsers.

---

## 12. SSLTLS Certificate in AWS

In AWS, certificates are commonly managed using AWS Certificate Manager, also called ACM.

For example, you may request a certificate for

```text
app.example.com
```

or

```text
.example.com
```

The certificate is attached to the ALB HTTPS listener.

So the ALB, not the EC2 instance, presents the certificate to the client.

---

## 13. ALB Target Group

A target group is a group of backend destinations that receive traffic from the load balancer.

Targets can be

 EC2 instances
 IP addresses
 ECS tasks
 Lambda functions

Example

```text
ALB HTTPS Listener  443
        
        v
Target Group web-servers
        
        v
EC2 Instance 1
EC2 Instance 2
EC2 Instance 3
```

The target group has its own protocol and port.

For example

```text
Target Group Protocol HTTP
Target Group Port 80
```

or

```text
Target Group Protocol HTTPS
Target Group Port 443
```

---

## 14. ALB SSL Termination Example

Example configuration

```text
ALB Listener
Protocol HTTPS
Port 443
Certificate app.example.com certificate from ACM

Target Group
Protocol HTTP
Port 80
Targets EC2 instances
```

Traffic flow

```text
User Browser
   
    HTTPS  443
   v
ALB
   
    HTTP  80
   v
EC2 instances
```

Meaning

 the browser communicates securely with the ALB
 the ALB decrypts the HTTPS request
 the ALB forwards plain HTTP to the EC2 instances
 the EC2 instances do not need the public SSL certificate

---

## 15. Can ALB Forward HTTPS To The Backend

Yes.

An ALB can terminate HTTPS from the client and then forward traffic to the backend using HTTPS.

Example

```text
ALB Listener
Protocol HTTPS
Port 443

Target Group
Protocol HTTPS
Port 443
```

Traffic flow

```text
User Browser
   
    HTTPS
   v
ALB
   
    HTTPS
   v
EC2 instances
```

In this design, the ALB decrypts the original client connection and then creates a new encrypted connection to the backend.

This is more secure than forwarding plain HTTP inside the VPC, but it requires certificate handling on the backend side too.

---

## 16. Why SSL Termination Is Useful

SSL termination is useful for several reasons.

### 16.1 Centralized Certificate Management

Instead of installing certificates on every backend server, you install or attach the certificate only to the load balancer.

Without SSL termination

```text
Certificate on EC2 1
Certificate on EC2 2
Certificate on EC2 3
Certificate on EC2 4
```

With SSL termination

```text
Certificate on ALB only
```

This makes certificate management much easier.

---

### 16.2 Easier Certificate Renewal

SSLTLS certificates expire.

If certificates are installed on many servers, renewal can become difficult.

With AWS Certificate Manager and ALB, certificate renewal can be automated for public ACM certificates.

This reduces operational work.

---

### 16.3 Backend Servers Are Simpler

Backend servers can focus on application logic.

They do not need to handle

 public certificates
 TLS handshakes
 cipher suites
 certificate renewal
 HTTPS listener configuration

The load balancer handles these tasks.

---

### 16.4 Load Balancer Can Understand HTTP Requests

When the ALB decrypts HTTPS traffic, it can inspect HTTP-level information.

For example

```text
Host header
Path
HTTP method
Headers
Cookies
Query string
```

This allows advanced routing.

Example

```text
api      → API target group
images   → image target group
admin    → admin target group
```

If the ALB could not decrypt the traffic, it could not easily perform Layer 7 routing based on HTTP content.

---

### 16.5 Better Routing Decisions

Because ALB can see inside the HTTP request after decryption, it can route traffic based on

 host-based rules
 path-based rules
 header-based rules
 query string rules
 HTTP method rules

Example

```text
app.example.com      → frontend target group
api.example.com      → API target group
admin.example.com    → admin target group
```

---

### 16.6 Reduced Work on Backend Servers

TLS encryption and decryption require CPU resources.

By terminating SSLTLS at the load balancer, backend servers do not need to spend as much CPU power on TLS processing.

This can improve backend efficiency.

---

### 16.7 Security Policy Control

The load balancer can enforce specific TLS policies.

For example, it can control

 supported TLS versions
 supported cipher suites
 certificate selection
 HTTPS-only access

This gives centralized security control.

---

## 17. SSL Termination and Ports

Common ports

```text
HTTP  = port 80
HTTPS = port 443
```

With SSL termination, a common setup is

```text
Client → ALB      HTTPS on port 443
ALB → Backend     HTTP on port 80
```

Another secure setup is

```text
Client → ALB      HTTPS on port 443
ALB → Backend     HTTPS on port 443
```

---

## 18. SSL Termination and Security Groups in AWS

When using an ALB with SSL termination, security groups are important.

Example setup

### ALB Security Group

Allow inbound HTTPS from the internet

```text
Inbound
HTTPS TCP 443 from 0.0.0.00
```

Optionally allow HTTP for redirecting HTTP to HTTPS

```text
Inbound
HTTP TCP 80 from 0.0.0.00
```

### EC2 Security Group

Allow inbound traffic only from the ALB security group.

If the target group uses HTTP port 80

```text
Inbound
HTTP TCP 80 from ALB security group
```

If the target group uses HTTPS port 443

```text
Inbound
HTTPS TCP 443 from ALB security group
```

This is more secure than allowing the whole internet to access the EC2 instances directly.

---

## 19. HTTP to HTTPS Redirect

Many applications should force users to use HTTPS.

A common ALB setup is

```text
Listener 1 HTTP   80  → redirect to HTTPS  443
Listener 2 HTTPS  443 → forward to target group
```

Traffic flow

```text
User enters httpapp.example.com
        
        v
ALB receives HTTP request on port 80
        
        v
ALB redirects user to httpsapp.example.com
        
        v
User connects using HTTPS on port 443
```

This ensures users access the application securely.

---

## 20. SSL Termination vs End-to-End Encryption

These two ideas are related but different.

### SSL Termination

```text
Client → Load Balancer = HTTPS
Load Balancer → Backend = HTTP
```

The encrypted connection ends at the load balancer.

### End-to-End Encryption

```text
Client → Load Balancer = HTTPS
Load Balancer → Backend = HTTPS
```

Traffic is encrypted on both sides.

However, if the load balancer decrypts and re-encrypts the traffic, then the load balancer can still inspect the request.

### True TLS Pass-Through

```text
Client → Load Balancer → Backend = same encrypted TLS session
```

The load balancer does not decrypt the request. The backend terminates TLS.

---

## 21. SSL Termination vs SSL Passthrough

### SSL Termination

The load balancer decrypts the traffic.

```text
Client HTTPS → Load Balancer decrypts → Backend
```

The load balancer can inspect HTTP data.

### SSL Passthrough

The load balancer does not decrypt the traffic.

```text
Client HTTPS → Load Balancer forwards encrypted traffic → Backend decrypts
```

The load balancer cannot inspect HTTP paths, headers, cookies, or methods.

### Comparison Table

 Feature                                          SSL Termination  SSL Passthrough 
 -----------------------------------------------  ---------------  --------------- 
 Where TLS ends                                   Load balancer    Backend server  
 Load balancer sees HTTP content                  Yes              No              
 Backend needs certificate                        Not always       Yes             
 Supports Layer 7 routing                         Yes              Limited or no   
 Easier certificate management                    Yes              No              
 Strongest end-to-end privacy from load balancer  No               Yes             

---

## 22. SSL Termination With CloudFront

CloudFront can also perform SSLTLS termination.

CloudFront is AWS's content delivery network.

A common flow is

```text
Client
  
   HTTPS
  v
CloudFront
  
   HTTP or HTTPS
  v
Origin ALB  S3  EC2  API Gateway
```

CloudFront terminates HTTPS at the edge location closest to the user.

Then CloudFront forwards the request to the origin using either HTTP or HTTPS, depending on configuration.

---

## 23. SSL Termination With API Gateway

API Gateway can also terminate HTTPS.

Example

```text
Client
  
   HTTPS
  v
API Gateway
  
   Integration request
  v
Lambda  HTTP backend  AWS service
```

The client communicates with API Gateway over HTTPS. API Gateway handles the TLS connection and then forwards the request to the configured backend integration.

---

## 24. SSL Termination With Network Load Balancer

A Network Load Balancer, or NLB, operates mainly at Layer 4.

NLB can handle TCP, UDP, TLS, and TCP_UDP traffic depending on configuration.

For TLS listeners, an NLB can terminate TLS.

Example

```text
Client
  
   TLS
  v
Network Load Balancer
  
   TCP or TLS
  v
Backend targets
```

However, unlike ALB, NLB is not designed for advanced HTTP routing such as path-based routing.

Use ALB when you need Layer 7 HTTP features.

Use NLB when you need very high performance, static IP support, low latency, or Layer 4 behavior.

---

## 25. Why ALB Needs To Decrypt HTTPS For Layer 7 Routing

ALB is a Layer 7 load balancer.

Layer 7 routing depends on HTTP information.

For example

```text
products
apiusers
admin
```

These paths are inside the HTTP request.

When HTTP is protected by TLS, this information is encrypted.

So, before ALB can route based on path or host, it must decrypt the HTTPS request.

That is why SSL termination is important for ALB.

---

## 26. Real-World Example

Imagine an e-commerce application.

It has three backend services

```text
Frontend service
Product service
Payment service
```

You can configure an ALB like this

```text
HTTPS Listener  443
Certificate     shop.example.com

Rules
             → frontend target group
products   → product target group
payments   → payment target group
```

Traffic flow

```text
Customer Browser
      
       HTTPS
      v
ALB terminates SSLTLS
      
       Routes based on path
      v
Correct backend service
```

Because the ALB decrypts the traffic, it can see the path and send the request to the right service.

---

## 27. Common Misunderstanding

### Misunderstanding

 If SSL is terminated at the load balancer, then the website is not secure.

### Correct Understanding

The website is still secure from the user's browser to the load balancer.

The question is whether the traffic between the load balancer and backend is encrypted.

So the real design choice is

```text
Client → Load Balancer HTTPS
Load Balancer → Backend HTTP or HTTPS
```

For many private VPC architectures, HTTP from ALB to backend may be acceptable.

For stricter security requirements, use HTTPS from ALB to backend too.

---

## 28. Another Misunderstanding

### Misunderstanding

 SSL termination means the load balancer removes HTTPS permanently.

### Correct Understanding

The client still uses HTTPS.

SSL termination only means the first TLS session ends at the load balancer.

The backend connection can still be HTTPS if you configure it that way.

---

## 29. Advantages of SSL Termination

Main advantages

 centralized certificate management
 simpler backend servers
 easier certificate renewal
 reduced TLS workload on backend servers
 support for HTTP routing rules
 easier HTTPS enforcement
 centralized TLS security policies
 simpler scaling of backend servers

---

## 30. Disadvantages or Considerations

SSL termination also has some considerations.

### 30.1 Backend Traffic May Be Unencrypted

If the load balancer forwards traffic to the backend using HTTP, then that internal segment is not encrypted.

This may not be acceptable for all environments.

### 30.2 Load Balancer Can See Decrypted Traffic

Because the load balancer decrypts the traffic, it can see the HTTP request contents.

This is necessary for Layer 7 routing, but it means the load balancer becomes a trusted component.

### 30.3 Compliance Requirements

Some compliance or security requirements may require encryption all the way to the backend.

In that case, use HTTPS between the load balancer and the backend.

### 30.4 Backend Certificate Management May Still Be Needed

If you use HTTPS from the load balancer to the backend, backend servers still need certificates.

---

## 31. SSL Termination in One Diagram

```text
                    Public Internet
                          
                           HTTPS encrypted traffic
                          v
                +---------------------+
                  Load Balancer      
                  SSLTLS ends here  
                  Certificate here   
                +---------------------+
                          
                           HTTP or HTTPS
                          v
                +---------------------+
                 Backend Application 
                 EC2  ECS  Lambda  
                +---------------------+
```

---

## 32. AWS Exam Perspective

For AWS exams such as Cloud Practitioner, Solutions Architect Associate, and Solutions Architect Professional, remember these points

1. SSL termination commonly happens at a load balancer.
2. ALB supports HTTPS listeners with certificates from ACM.
3. SSL termination allows ALB to inspect HTTP requests.
4. ALB can route based on host, path, headers, methods, and query strings.
5. Backend traffic can be HTTP or HTTPS.
6. ACM simplifies certificate management.
7. HTTP port 80 can redirect to HTTPS port 443.
8. SSL passthrough means the load balancer does not decrypt the traffic.
9. ALB is best for Layer 7 HTTPHTTPS routing.
10. NLB is better for Layer 4 performance-oriented use cases.

---

## 33. Example AWS Configuration

A common secure web application setup

```text
Route 53
   
   v
Application Load Balancer
   - Listener HTTP 80 redirects to HTTPS 443
   - Listener HTTPS 443 uses ACM certificate
   - Forwards to target group
   
   v
Target Group
   - Protocol HTTP
   - Port 80
   
   v
EC2 instances in private subnets
```

Security groups

```text
ALB security group
- Allow HTTPS 443 from internet
- Allow HTTP 80 from internet only for redirect

EC2 security group
- Allow HTTP 80 only from ALB security group
```

This means users can access the application securely, but EC2 instances are not directly exposed to the internet.

---

## 34. Simple Analogy

Imagine a locked envelope.

The client sends a locked envelope to the load balancer.

The load balancer has the key, so it opens the envelope, reads the request, and decides which backend server should handle it.

Then it sends the request to that backend server.

That opening of the locked envelope at the load balancer is SSL termination.

---

## 35. Very Short Definition

SSL termination is when a load balancer or proxy decrypts incoming HTTPS traffic, handles the SSLTLS certificate, and forwards the request to backend servers using HTTP or HTTPS.

---

## 36. Final Summary

SSL termination is a key concept in modern web architecture and AWS load balancing.

It allows a load balancer, such as an Application Load Balancer, to handle the HTTPS connection from users. The load balancer presents the SSLTLS certificate, decrypts the request, applies routing rules, and forwards the request to backend targets.

The backend connection can be plain HTTP or encrypted HTTPS, depending on your security requirements.

The main benefit is simplicity certificates and HTTPS handling are centralized at the load balancer. This makes backend servers easier to manage and enables powerful Layer 7 routing features such as path-based and host-based routing.

For AWS exams, remember this core idea

 SSL termination usually means HTTPS ends at the load balancer, and the load balancer forwards traffic to backend targets using HTTP or HTTPS depending on the target group configuration.
