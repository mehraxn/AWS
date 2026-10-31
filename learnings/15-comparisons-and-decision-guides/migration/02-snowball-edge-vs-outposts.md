# AWS Snowball Edge vs AWS Outposts

## Simple definition

### AWS Snowball Edge

AWS Snowball Edge is a physical AWS device with storage and some compute power. It is shipped to your location so you can move large amounts of data or run limited workloads locally, especially when the network is slow, unavailable, or unreliable.

### AWS Outposts

AWS Outposts is AWS infrastructure installed at your site. It brings AWS hardware, AWS services, APIs, and tools into your data center or on-premises location so you can run AWS-style workloads locally.

> **Important current note:** AWS documentation says Snowball Edge is no longer available to new customers. For new edge-compute use cases, AWS points customers toward AWS Outposts. For exam study, the comparison is still very useful because the concepts are classic AWS hybrid-cloud ideas.

---

## Core idea in plain English

* **Snowball Edge = AWS in a rugged box that you ship.**
* **Outposts = AWS installed in your building.**

This is the easiest way to remember the difference.

---

## Main purpose of each service

### Snowball Edge main purpose

Its main purpose is to **move huge amounts of data physically** when sending data over the internet would be too slow, too expensive, or impossible.

It can also do some **local edge computing**, but that is not the first thing to think of in most exam questions.

### Outposts main purpose

Its main purpose is to **extend AWS into your on-premises environment** so you can run AWS workloads locally with **low latency**, **local processing**, and a **consistent hybrid cloud experience**.

---

## Key differences

### 1) Temporary device vs installed infrastructure

* **Snowball Edge:** usually a device AWS ships to you and you later return.
* **Outposts:** installed at your site as long-term AWS infrastructure.

### 2) Data transfer vs hybrid cloud

* **Snowball Edge:** mainly about moving very large data sets and handling disconnected edge environments.
* **Outposts:** mainly about running AWS services on premises.

### 3) Disconnected vs connected

* **Snowball Edge:** useful when connectivity is limited or even absent.
* **Outposts:** designed for environments with a constant connection back to an AWS Region.

### 4) Limited local AWS compatibility vs broader AWS experience

* **Snowball Edge:** supports selected local compute and storage features.
* **Outposts:** gives a much more native AWS experience on premises, using AWS APIs, tools, and services.

### 5) Mobility vs permanence

* **Snowball Edge:** portable and rugged.
* **Outposts:** fixed on-premises deployment.

### 6) Shipping data vs extending a VPC

* **Snowball Edge:** you copy data onto the device and ship it.
* **Outposts:** you extend your AWS environment, such as your VPC, into your site.

---

## Similarities

Both services:

* bring AWS capability closer to where data is created or used
* can support local processing
* are used in hybrid or edge scenarios
* help when low latency or local data handling matters
* connect to the larger AWS ecosystem in different ways

---

## When to use AWS Snowball Edge

Use Snowball Edge when:

* you need to transfer **terabytes or petabytes** of data
* the network is too slow for practical transfer
* the location has **limited or no connectivity**
* you need a **rugged physical device** for remote environments
* you want to collect, process, or move data in places like ships, mines, remote sites, or temporary field locations

### Good exam clue words

Look for phrases like:

* "move petabytes of data"
* "internet is too slow"
* "offline"
* "remote site"
* "disconnected environment"
* "ship device"

---

## When to use AWS Outposts

Use Outposts when:

* you need AWS infrastructure **on premises**
* your applications need **very low latency** to local systems
* you must keep data processing local for **residency**, compliance, or operational reasons
* you want a **consistent AWS experience** in your own facility
* you need long-term hybrid architecture, not just one-time data transfer

### Good exam clue words

Look for phrases like:

* "run AWS services on premises"
* "consistent hybrid cloud"
* "low latency to local applications"
* "data residency"
* "AWS-managed rack/server at customer site"
* "extend VPC on premises"

---

## Real exam-style decision rule

Use this rule:

* **If the question is about moving huge data with poor or no network, choose Snowball Edge.**
* **If the question is about running AWS infrastructure and services inside the customer site, choose Outposts.**

### One-line memory rule

**Ship the box = Snowball Edge**
**Install the rack = Outposts**

---

## Side-by-side comparison table

| Topic               | AWS Snowball Edge                                    | AWS Outposts                                   |
| ------------------- | ---------------------------------------------------- | ---------------------------------------------- |
| Basic idea          | Physical device shipped to you                       | AWS infrastructure installed at your site      |
| Main goal           | Large-scale data transfer and remote edge processing | Run AWS workloads on premises                  |
| Connectivity        | Works well with limited or no connectivity           | Requires reliable connection to an AWS Region  |
| Deployment style    | Temporary / portable device                          | Permanent / long-term installation             |
| Best for            | Offline transfer, rugged edge locations              | Hybrid cloud, low-latency on-prem apps         |
| AWS experience      | Selected local storage and compute capabilities      | Much more native AWS services, APIs, and tools |
| Data movement model | Copy data onto device and ship it                    | Keep workloads running locally in your site    |
| Physical form       | Rugged appliance                                     | Rack or server installed on premises           |
| Typical scale       | Massive data migration or remote edge jobs           | Continuous business operations on premises     |
| Exam keyword        | "petabytes", "offline", "ship device"                | "hybrid", "low latency", "on premises AWS"     |

---

## Main use cases

### Snowball Edge use cases

* moving backups, archives, or datasets into AWS
* transferring data from remote industrial or research sites
* collecting data in disconnected environments
* doing limited local processing before data is sent to AWS

### Outposts use cases

* modernizing on-premises apps with AWS services
* factory, hospital, telecom, or retail systems needing local latency
* workloads with local data processing or residency requirements
* hybrid cloud applications tightly integrated with on-site systems

---

## Key features

### Snowball Edge key features

* physical device shipped by AWS
* large storage capacity
* can process data locally
* supports selected compute capability
* encrypted and tamper-resistant design
* useful for environments with little or no network connectivity

### Outposts key features

* AWS-managed hardware on customer premises
* consistent AWS APIs and tools
* local compute and storage
* integrates with AWS Region and VPC networking
* designed for low latency and local processing
* supports long-term hybrid cloud architecture

---

## How each service works

### How Snowball Edge works

1. You create a Snowball job in AWS.
2. AWS ships the device to your site.
3. You connect it to your local network.
4. You copy data to or from the device, or run local edge workloads.
5. You return the device to AWS.
6. AWS transfers the data into AWS services such as Amazon S3.

### How Outposts works

1. AWS installs Outposts hardware at your site.
2. The Outpost stays connected to an AWS Region.
3. You create AWS resources on the Outpost using familiar AWS tools.
4. Your workloads run locally on the Outpost.
5. You still manage them with AWS-style APIs, consoles, and services.

---

## Why the difference matters for the exam

Many students confuse these two because both sound like "AWS outside the Region."

But the exam usually tests the **reason** you are using them:

* **Snowball Edge** is about **data transport** and **disconnected edge environments**.
* **Outposts** is about **hybrid cloud infrastructure** and **running AWS services on premises**.

If you focus on the business need, the answer becomes easier.

---

## Related AWS services and differences

### Snowball Edge vs AWS DataSync

* **Snowball Edge:** physical device for offline or poor-network transfer
* **DataSync:** online data transfer over the network

### Snowball Edge vs Snowcone

* **Snowball Edge:** larger, more powerful, for bigger jobs
* **Snowcone:** smaller device for lighter edge or transfer needs

### Outposts vs Local Zones

* **Outposts:** AWS hardware in the customer site
* **Local Zones:** AWS infrastructure near a metro area, but still in AWS locations, not in your building

### Outposts vs Availability Zones

* **Availability Zone:** AWS-managed data center location inside a Region
* **Outposts:** AWS hardware physically installed in your site, but linked to a Region

### Outposts vs VMware Cloud on AWS

* **Outposts:** native AWS infrastructure on premises
* **VMware Cloud on AWS:** VMware environment running on AWS infrastructure

---

## Common exam traps

### Trap 1: "On-premises" does not always mean Outposts

If the question is really about **moving huge data physically**, the answer is likely **Snowball Edge**, even though the device sits on premises temporarily.

### Trap 2: "Edge" does not always mean Snowball Edge

If the question says the company wants **AWS services running locally as part of a long-term hybrid model**, the answer is likely **Outposts**.

### Trap 3: Confusing data transfer with application hosting

* **Need to transfer massive data offline?** Snowball Edge.
* **Need to host AWS workloads locally for low latency?** Outposts.

### Trap 4: Ignoring connectivity requirements

* **Little or no connectivity:** think Snowball Edge.
* **Continuous connection to AWS Region:** think Outposts.

### Trap 5: Thinking both are equal AWS environments

They are not.
Snowball Edge offers selected capabilities on a device. Outposts is much closer to a real AWS on-premises extension.

---

## Easy real-world examples

### Snowball Edge example

A research team in a remote desert collects 500 TB of video and sensor data. Internet upload would take too long. AWS ships a Snowball Edge device, the team copies the data onto it, and ships it back to AWS.

### Outposts example

A hospital runs medical applications that need very low latency to local equipment and must process some data on site. It wants the same AWS tools and APIs used in the cloud. AWS Outposts is installed in the hospital's data center.

---

## Final summary

AWS Snowball Edge and AWS Outposts are both used outside the normal AWS Region environment, but they solve different problems.

Snowball Edge is mostly about **physically moving large data** and helping in **remote or disconnected environments**.

Outposts is about **bringing AWS infrastructure and services into your own site** for **low latency**, **local processing**, and **hybrid cloud consistency**.

For the exam, do not just ask, "Is it on premises?"
Ask, **"Are they shipping data, or are they running AWS locally long term?"**

---

## Short exam answer

**Snowball Edge** is a physical device used mainly for large-scale offline data transfer and some edge computing in remote or disconnected environments.
**Outposts** is AWS-managed infrastructure installed on premises to run AWS workloads locally with a consistent hybrid cloud experience.

---

## Memory trick

### The easiest memory trick

* **Snowball Edge = ship it**
* **Outposts = install it**

### Another memory trick

* **Snowball Edge = move data**
* **Outposts = run AWS there**

### Mini exam shortcut

If you see:

* **petabytes, shipping, offline, remote** → **Snowball Edge**
* **hybrid, low latency, data residency, AWS on premises** → **Outposts**
