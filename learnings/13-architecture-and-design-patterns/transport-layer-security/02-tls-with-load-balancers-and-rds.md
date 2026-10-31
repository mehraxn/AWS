# 🔐 SSLTLS with Load Balancer and RDS

 Core idea SSLTLS is not only for Load Balancers — it's a general way to encrypt network traffic between any two endpoints.

---

## 📋 Table of Contents

- [What is SSLTLS](#-what-is-ssltls)
- [SSL vs TLS](#-ssl-vs-tls)
- [Case 1 User → Load Balancer → EC2](#-case-1-user--load-balancer--ec2)
- [Case 2 Application → RDSAurora](#-case-2-application--rdsaurora)
- [Comparing the Two Cases](#-comparing-the-two-cases)
- [Quick Analogy](#-quick-analogy)
- [Exam Cheat Sheet](#-exam-cheat-sheet)

---

## 🌐 What is SSLTLS

SSLTLS protects data while it travels over a network — this is called in-flight encryption or encryption in transit.

```
# Without TLS
Client sends data  ──────────────────────────►  Server
                       (readable in transit)

# With TLS
Client sends data  ══════════════════════════►  Server
                       (encrypted in transit)
```

If someone intercepts the traffic, they cannot read the data.

---

## 🔄 SSL vs TLS

 Term  Meaning 
---------------
 SSL  Older name — still commonly used 
 TLS  Modern secure protocol — what's actually running today 

 When someone says SSL certificate, they almost always mean the certificate used for a TLSHTTPS connection.

---

## ⚖️ Case 1 User → Load Balancer → EC2

### Architecture

```
User Browser
     │
     │  HTTPS  TLS encrypted
     ▼
Application Load Balancer
     │
     │  HTTP or HTTPS
     ▼
EC2 Instance
```

The user connects to the ALB over HTTPS. The ALB performs TLS termination — it decrypts the traffic, then forwards the request to EC2.

---

### Option A — ALB decrypts → sends plain HTTP to EC2

```
User Browser
     │
     │  HTTPS  🔒 encrypted
     ▼
Application Load Balancer  ◄── decrypts here
     │
     │  HTTP  🔓 unencrypted
     ▼
EC2 Instance
```

✅ Traffic from user → ALB is encrypted  
⚠️ Traffic from ALB → EC2 is not encrypted  
 May be acceptable inside a private VPC, but is less secure end-to-end.

---

### Option B — ALB decrypts → re-encrypts to EC2 ✅ Recommended

```
User Browser
     │
     │  HTTPS  🔒 encrypted
     ▼
Application Load Balancer  ◄── decrypts here
     │
     │  HTTPS  🔒 encrypted again
     ▼
EC2 Instance
```

✅ Traffic from user → ALB is encrypted  
✅ Traffic from ALB → EC2 is also encrypted  
 The ALB creates a brand new TLS connection to EC2. More secure than Option A.

---

### TLS is not exclusive to Load Balancers

TLS can be used anywhere two systems communicate over a network

 Connection  TLS Applies 
---------------
 Browser → Load Balancer  ✅ 
 Load Balancer → EC2  ✅ 
 EC2 → RDS  ✅ 
 Lambda → RDS  ✅ 
 Service → Service  ✅ 

---

## 🗄️ Case 2 Application → RDSAurora

### Architecture

```
EC2  Lambda  Application
          │
          │  TLS encrypted database connection
          ▼
   RDS  Aurora Database
```

There is no Load Balancer between the app and the database. The application connects directly to the RDSAurora endpoint.

---

### What gets encrypted

The actual database queries and responses

```sql
SELECT  FROM users;
INSERT INTO orders VALUES (...);
UPDATE accounts SET balance = 100;
```

Without TLS → this traffic could theoretically be intercepted and read.  
With TLS → the traffic is encrypted between your app and the database.

---

### How decryption works

```
Application encrypts the query
          │
          │  encrypted traffic travels over the network
          ▼
RDS  Aurora receives it
          │
          ▼
RDS  Aurora decrypts it
          │
          ▼
Database processes the query
```

 For RDSAurora, TLS protects the traffic between your application and the database.

---

### Is ELB involved here

No. Normal RDSAurora traffic flows like this

```
Application  ──────────────────────►  RDS  Aurora
```

Not like this

```
Application  ──►  Load Balancer  ──►  RDS  Aurora  ✗
```

---

## 📊 Comparing the Two Cases

  Case 1 Load Balancer TLS  Case 2 RDSAurora TLS 
---------
 Flow  `User → ALB → EC2`  `App → RDSAurora` 
 Purpose  Protect webapp traffic  Protect database traffic 
 Who decrypts  ALB (then optionally re-encrypts to EC2)  The database endpoint 
 Example  `httpsexample.com`  MySQLPostgres connection with TLS 

---

## 💡 Quick Analogy

Think of TLS like sending a locked box over a network.

### Load Balancer case
```
User puts message in locked box
          │
          ▼
Load Balancer unlocks the box
          │
          ▼
Forwards it (locked or unlocked) to EC2
```

### RDSAurora case
```
App puts database query in locked box
          │
          ▼
RDSAurora unlocks the box
          │
          ▼
Database reads and processes the query
```

Same idea — encrypted in transit. Different destination — one ends at the Load Balancer, one ends at the database.

---

## 📝 Exam Cheat Sheet

### In-flight vs At-rest

 Type  What it protects  Technology 
-----------------------------------
 In-flight encryption  Data moving over the network  TLSSSL 
 At-rest encryption  Data stored on disk  AWS KMS 

### RDSAurora at-rest encryption covers

- 📁 Database storage
- 💾 Backups
- 📸 Snapshots
- 📖 Read replicas
- 📋 Transaction logs

---

### ⚠️ Don't confuse these two

```
TLS  →  protects data while MOVING    →  EC2 ──► RDS connection
KMS  →  protects data while STORED    →  RDS database files on disk
```

---

### 🧠 One-line memory trick

```
ELB TLS  =  protects webapp traffic
RDS TLS  =  protects database traffic
KMS      =  protects stored database data
```

---

 Final summary TLS encrypts traffic between two endpoints.
 Sometimes the endpoint is a Load Balancer. Sometimes the endpoint is a database.