# AWS Application Discovery Service

## Simple definition

AWS Application Discovery Service is an AWS service that helps you collect information about your on-premises servers, applications, and dependencies before a migration to AWS.

In simple words, it helps you understand what you currently have in your data center so you can plan migration better.

---

## Core idea in plain English

Before moving to AWS, a company needs answers to questions like

 What servers do we have
 What applications are running on them
 How much CPU, memory, and storage do they use
 Which servers talk to each other

AWS Application Discovery Service helps discover this information.

So the core idea is

You cannot migrate well if you do not first understand your current environment.

This service gives visibility into your existing systems so migration planning becomes easier, safer, and more accurate.

---

## Main use cases

### 1. Inventory discovery before migration

It helps companies identify their on-premises servers, workloads, and system details before moving to AWS.

### 2. Dependency mapping

It helps show which servers and applications communicate with each other.

This is very important because moving one server without the systems it depends on can break an application.

### 3. Migration planning

It helps migration teams estimate what resources they need in AWS.

For example, it can help answer whether a workload should move to EC2, how large the instance should be, and how systems should be grouped.

### 4. Data for migration tools

The discovered information can be used together with migration planning processes and AWS migration services.

### 5. Reducing migration risk

Because you understand the environment better, there is less chance of forgetting an important dependency or underestimating infrastructure needs.

---

## Key features

### 1. Server discovery

It collects information about on-premises servers, such as configuration and usage data.

### 2. Application dependency visibility

It helps identify communication between servers and applications.

This is useful for understanding which systems belong together.

### 3. Agent-based and agentless collection options

AWS provides more than one way to collect discovery data, depending on the migration approach and environment.

### 4. Performance data collection

It can gather metrics such as CPU utilization, memory usage, and network activity.

This helps size AWS resources more accurately.

### 5. Migration planning support

The collected data supports decision-making for migration waves, application grouping, and target infrastructure design.

### 6. Integration with migration workflows

It is part of the AWS migration journey and supports broader migration assessment and planning activities.

---

## How it works

### Option 1 Agentless discovery

In some environments, discovery can be performed without installing agents on every server.

This can make initial discovery easier in certain setups.

### Option 2 Agent-based discovery

Agents can be installed on servers to collect more detailed system and performance information.

This is useful when you need deeper visibility.

### Basic flow

1. A company connects its on-premises environment to AWS discovery tools.
2. AWS collects information about servers, running workloads, and dependencies.
3. The collected data is stored and organized.
4. Migration teams review the data.
5. The team uses that information to plan migration groups, timelines, and AWS target resources.

So the service is mostly about understanding first, migrating second.

---

## Why it is important for the exam

For the AWS Certified Cloud Practitioner exam, the main point is not deep technical setup.

The exam usually cares about what problem the service solves.

You should remember this

AWS Application Discovery Service is used before migration to gather information about on-premises systems and their dependencies.

If a question describes

 moving from a data center to AWS
 discovering servers and applications
 understanding dependencies
 collecting migration planning data

then AWS Application Discovery Service is a strong answer.

---

## Related AWS services and differences

### AWS Migration Hub

AWS Migration Hub helps you track and manage migrations across AWS tools.

Difference
Application Discovery Service helps you discover and assess the environment.
Migration Hub helps you monitor and manage migration progress.

### AWS Application Migration Service (MGN)

AWS Application Migration Service helps move servers to AWS.

Difference
Application Discovery Service helps you learn about what to migrate.
Application Migration Service helps you actually migrate the servers.

### AWS Database Migration Service (AWS DMS)

AWS DMS helps migrate databases.

Difference
Application Discovery Service is for discovering application and server environments.
DMS is specifically for moving databases.

### AWS DataSync

AWS DataSync transfers data between on-premises storage and AWS storage services.

Difference
Application Discovery Service does not move files.
DataSync moves data.

### AWS Server Migration Service (historical exam context)

Older materials may mention AWS Server Migration Service.

Difference
That service was for server migration workflows, while Application Discovery Service is about discovery and planning.

For exam thinking, focus on the role

 Discovery Service = assess and map
 Migration services = move

---

## Common exam traps

### Trap 1 Confusing discovery with migration

AWS Application Discovery Service does not actually migrate your servers.

It helps you understand your environment before migration.

### Trap 2 Confusing it with Migration Hub

Migration Hub is for tracking migration progress.

Application Discovery Service is for collecting server and dependency information.

### Trap 3 Confusing it with AWS DMS

DMS is for databases.

Application Discovery Service is broader discovery for servers and applications.

### Trap 4 Thinking it is a monitoring service

It collects data for migration planning, but it is not the same as normal operational monitoring tools like Amazon CloudWatch.

### Trap 5 Thinking it is only about hardware inventory

It is not just a list of servers.

A key value is dependency mapping and understanding how applications are connected.

---

## Easy real-world example

A company has 120 servers in its office data center and wants to move to AWS.

The IT team does not fully know

 which application runs on which server
 which servers communicate with each other
 how much CPU and memory each server really uses

If they migrate blindly, they might move systems in the wrong order and break the application.

So they use AWS Application Discovery Service.

It helps them discover the servers, understand dependencies, and plan migration waves correctly.

After that, they can choose the right AWS migration tools to perform the actual move.

---

## If I were an examiner ...

Here are the kinds of things I would test about AWS Application Discovery Service.

### 1. Do you know the main purpose

I may ask

Which AWS service helps a company collect information about its on-premises servers and application dependencies before migration

Expected thinking
That is AWS Application Discovery Service.

### 2. Do you know where it fits in the migration journey

I may ask

Which service is useful in the assessment and planning phase of migration rather than the execution phase

Expected thinking
Application Discovery Service is used before actual migration.

### 3. Can you separate discovery from movement

I may ask

A company wants to understand server relationships before moving workloads. Which service should they use

Expected thinking
Use Application Discovery Service, because the key phrase is understand relationships and dependencies.

### 4. Can you distinguish it from other migration services

I may ask

Which AWS service discovers on-premises application data, and which service tracks migration progress

Expected thinking
Application Discovery Service discovers.
Migration Hub tracks.

### 5. Can you spot the keyword clues

I may build a question using words like

 assess
 discover
 inventory
 dependency mapping
 migration planning
 on-premises environment

Those words should make you think of AWS Application Discovery Service.

---

## Final summary

AWS Application Discovery Service is a migration assessment service.

Its main job is to help organizations understand their on-premises environment before moving to AWS.

It discovers servers, usage information, and dependencies between applications.

This helps teams plan migration safely and choose the right migration strategy.

The most important exam idea is

It helps you discover and plan, not directly migrate.

---

## Short exam answer

AWS Application Discovery Service helps organizations collect information about on-premises servers, applications, and dependencies so they can assess and plan migrations to AWS.

---

## Memory trick

Think

Discovery comes before migration.

Or even shorter

Discover first, move later.

If the exam question talks about understanding the current environment before migration, think of AWS Application Discovery Service.

---

## Exam keywords

Watch for these words in exam questions

 discover
 inventory
 assess
 migration planning
 dependency mapping
 on-premises servers
 application relationships
 pre-migration analysis
 server usage data
 migration assessment

---

## One-line comparison memory aid

 Application Discovery Service = find and understand what exists
 Migration Hub = track migration progress
 Application Migration Service = move servers
 DMS = move databases
 DataSync = move files and data

---

## Quick coach note

For Cloud Practitioner level, do not overcomplicate this service.

You usually only need to remember

 It is used before migration
 It discovers servers and dependencies
 It helps with planning
 It does not do the actual migration itself
