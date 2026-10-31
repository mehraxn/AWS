# AWS Migration Hub

## Simple definition

AWS Migration Hub is an AWS service that gives you one central place to plan, track, and monitor migrations from on-premises environments to AWS.

It helps you see what you are migrating, group resources into applications, and follow migration progress across different AWS migration tools.

 Exam note AWS Migration Hub has historically been the central dashboard for migration tracking. As of late 2025, AWS notes that it is no longer open to new customers, but the exam concept is still mainly about migration visibility and tracking in one place.

---

## Core idea in plain English

Think of AWS Migration Hub like a control tower for migration projects.

When a company moves servers, databases, and applications to AWS, many tools and many steps can be involved. Migration Hub helps by showing the migration in one view instead of forcing you to check many separate tools.

So the key idea is

Migration Hub does not do every migration task itself. It helps you organize, discover, and track migrations in one central place.

---

## Main use cases

### 1. Tracking migration progress

A company wants to see how many servers and applications have started, are in progress, or are completed.

### 2. Grouping servers into applications

Some servers belong to the same business application. Migration Hub helps group them so teams can migrate them together.

### 3. Planning a migration portfolio

Before moving to AWS, a company needs to discover its current environment and understand what exists.

### 4. Using multiple migration tools together

A business might use one tool for servers and another for databases. Migration Hub gives a single place to monitor them.

### 5. Migration visibility for large enterprises

Big organizations often migrate many workloads at the same time. Migration Hub helps keep the project organized.

---

## Key features

### Central migration dashboard

Shows migration status across supported migration tools.

### Application grouping

Lets you group related servers into applications.

### Discovery integration

Works with discovery tools to collect information about on-premises servers and applications.

### Progress tracking

Tracks whether migrations are not started, in progress, completed, and more.

### Portfolio visibility

Helps you understand your migration estate at a higher level.

### Integration with related migration services

Works alongside services that actually perform migration tasks.

---

## How it works

### Step 1 Discover your environment

You first collect information about your on-premises servers, applications, and dependencies.

### Step 2 Import or gather migration data

Migration Hub can use discovered data or imported information about your environment.

### Step 3 Group resources into applications

You can organize servers that belong together into one application group.

### Step 4 Use migration tools

You then use AWS migration services such as server or database migration tools to move workloads.

### Step 5 Track everything in one place

Migration Hub shows progress and status so you can monitor the migration journey more easily.

---

## Why it is important for the exam

For the AWS Certified Cloud Practitioner exam, AWS Migration Hub matters because it tests whether you understand the difference between

 a service that performs migration
 and a service that tracks and organizes migration

This is the key exam idea

AWS Migration Hub is mainly for visibility, planning, and tracking — not for directly copying application data or running the migration itself.

If a question asks for a service that gives a single place to monitor migrations, Migration Hub is often the right answer.

---

## Related AWS services and differences

### AWS Migration Hub vs AWS Application Migration Service (AWS MGN)

 Migration Hub = tracks and monitors migrations
 AWS MGN = actually migrates servers to AWS

Use Migration Hub for the dashboard.
Use AWS MGN for lift-and-shift server migration.

### AWS Migration Hub vs AWS Database Migration Service (AWS DMS)

 Migration Hub = central tracking view
 AWS DMS = migrates databases

Use DMS when the question is about moving database data.

### AWS Migration Hub vs AWS Application Discovery Service

 Migration Hub = tracks and organizes migration portfolio
 Application Discovery Service = collects data about on-premises servers and dependencies for planning

Discovery helps you understand what you have.
Migration Hub helps you manage and track the migration.

### AWS Migration Hub vs Migration Hub Strategy Recommendations

 Migration Hub = visibility and migration tracking
 Strategy Recommendations = suggests migration strategies like rehost, replatform, or refactor

One tracks the journey.
The other helps choose the best migration path.

### AWS Migration Hub vs AWS Transform

 Migration Hub = older central migration tracking service
 AWS Transform = newer AWS service for similar and broader migrationmodernization capabilities

For exam prep, still remember Migration Hub as the classic answer for central migration tracking.

---

## Common exam traps

### Trap 1 Thinking Migration Hub performs the migration

It usually does not do the actual migration work.
It mainly tracks and organizes migration progress.

### Trap 2 Confusing it with AWS MGN

If the question says lift and shift servers, that is usually AWS Application Migration Service, not Migration Hub.

### Trap 3 Confusing it with AWS DMS

If the question is about moving databases, that is usually AWS DMS.

### Trap 4 Confusing discovery with tracking

Discovery tools help you learn about your current environment.
Migration Hub helps you see and track the overall migration.

### Trap 5 Picking Migration Hub when the question asks for recommendations

If the question focuses on which migration strategy to choose, Strategy Recommendations may be the better answer.

---

## Easy real-world example

A company has

 120 on-premises servers
 15 business applications
 some SQL databases
 different teams handling different parts of the migration

They use

 AWS Application Migration Service for servers
 AWS DMS for databases
 discovery tools to understand dependencies

Instead of checking each tool separately, the company uses AWS Migration Hub to

 group servers into applications
 see migration progress
 track which workloads are finished
 manage the migration more clearly

So Migration Hub acts like the project dashboard for the migration.

---

## Final summary

AWS Migration Hub is a central place to discover, organize, and track migrations to AWS.

Its main value is visibility.
It helps companies understand what they are migrating and monitor progress across different migration tools.

For the exam, remember this

Migration Hub is for migration tracking and portfolio visibility, not for doing the actual migration itself.

---

## Short exam answer

AWS Migration Hub is a central service used to plan, organize, and track application migrations to AWS across multiple migration tools.

---

## Memory trick

Migration Hub = migration dashboard hub

Think

 Hub = central place
 Migration = moving workloads
 so Migration Hub = the central place that shows the migration journey

A simple memory line

MGN moves. DMS migrates databases. Migration Hub watches the whole trip.
