# AWS Database Migration Service (AWS DMS) — Study Note

## Simple definition

AWS Database Migration Service (AWS DMS) is an AWS service that helps you move data from one database to another with minimal downtime.

## Core idea in plain English

Think of AWS DMS as a moving service for databases.

It helps copy data from your old database to a new one. While users are still using the old database, DMS can keep copying new changes too. This helps you switch to the new database without stopping the application for a long time.

## Main use cases

 Migrate an on-premises database to AWS
 Move from one AWS database to another
 Upgrade from an old database engine to a modern one
 Replicate ongoing database changes
 Support database modernization projects

## Key features

 Minimal downtime migration
 Continuous data replication
 Supports many popular database engines
 Works for homogeneous migrations and heterogeneous migrations
 Managed AWS service
 Can migrate ongoing changes after the first full load
 Helps move data to services like Amazon RDS, Amazon Aurora, Amazon Redshift, Amazon S3, and more

## How it works

AWS DMS usually works in a simple flow

1. You choose a source database.
2. You choose a target database.
3. You create the migration setup in AWS DMS.
4. DMS copies the existing data.
5. DMS can continue copying new changes from the source to the target.
6. When the target is ready, you switch the application to the new database.

A simple way to remember it is
Source → DMS → Target

## Homogeneous vs heterogeneous migration

### Homogeneous migration

This means moving between the same type of database.

Example

 MySQL to Amazon RDS for MySQL
 PostgreSQL to Amazon RDS for PostgreSQL

This is usually easier because the database engine stays the same.

### Heterogeneous migration

This means moving between different types of databases.

Example

 Oracle to Amazon Aurora PostgreSQL
 Microsoft SQL Server to MySQL

This is harder because the database engines are different.

Important exam point
AWS DMS moves the data, but schema conversion may also be needed when the source and target use different database engines.

## Why it is important for the exam

AWS Cloud Practitioner questions often test whether you know the correct migration service.

AWS DMS is the right answer when the question is about

 Moving database data to AWS
 Migrating databases with minimal downtime
 Ongoing replication during migration
 Moving from commercial databases to AWS-managed databases

If the exam asks about moving a database with as little interruption as possible, AWS DMS is often the best answer.

## Related AWS services and differences

### AWS DMS vs AWS Schema Conversion Tool (AWS SCT)

 AWS DMS moves the data
 AWS SCT helps convert the schema, code, and database structure

Easy rule

 DMS = data moves
 SCT = structure changes

### AWS DMS vs AWS DataSync

 AWS DMS is for databases
 AWS DataSync is for files and object storage

### AWS DMS vs AWS Snowball Edge

 AWS DMS is for logical database migration and replication
 AWS Snowball Edge is for transferring large amounts of data physically with an AWS device

### AWS DMS vs BackupRestore

 DMS is better when you want minimal downtime and ongoing replication
 BackupRestore is simpler in some cases, but usually causes more downtime

## Common exam traps

### Trap 1 Thinking DMS converts everything automatically

Not always.

For migrations between different database engines, you may also need AWS Schema Conversion Tool (AWS SCT).

### Trap 2 Confusing data migration with file migration

If the question is about databases, think AWS DMS.

If the question is about files, shared storage, or NFS/SMB (Network File System /Server Message Block), think AWS DataSync.

### Trap 3 Forgetting the “minimal downtime” clue

When the exam says

 minimal downtime
 ongoing replication
 source database stays available

That strongly points to AWS DMS.

### Trap 4 Confusing DMS with database hosting services

AWS DMS does not host your production database.

It helps you move data between databases. Services like Amazon RDS and Amazon Aurora host the database.

## Easy real-world example

A company runs an old Oracle database in its office.

They want to move to Amazon Aurora PostgreSQL to reduce cost and modernize their application.

They can use

 AWS SCT to help convert the schema from Oracle format to PostgreSQL format
 AWS DMS to move the actual data and keep copying changes until cutover

This lets the company migrate with very little downtime.

## Final summary

AWS DMS is a managed AWS service for migrating database data.

Its biggest value is that it helps move data with minimal downtime. It supports many source and target databases and can continue replicating changes while the migration is happening.

For same-engine migrations, DMS is usually simpler. For different-engine migrations, DMS often works together with AWS SCT.

## Short exam answer

AWS DMS is used to migrate databases to AWS or between databases with minimal downtime. It can perform full loads and ongoing replication, and for heterogeneous migrations it may be used together with AWS Schema Conversion Tool.

## Memory trick

DMS = Database Moving Service

That is not the official name, but it is a great exam memory trick.

 D = Database
 M = Move
 S = Smooth switch with minimal downtime

So when you see database migration + minimal downtime, think AWS DMS.
