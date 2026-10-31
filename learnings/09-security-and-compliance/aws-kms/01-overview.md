# AWS KMS



<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

## Simple definition

AWS KMS is an AWS security service that helps you create, protect, and control encryption keys.

In simple words, it is the AWS service you use when you want AWS to help manage the keys that lock and unlock your data.

---

## Core idea in plain English

Encryption protects data by turning it into unreadable text.

But encryption is only as safe as the key used to lock and unlock that data.

AWS KMS helps you manage those keys securely.

So the big idea is

KMS manages encryption keys, not your main data itself.

Your data may be in Amazon S3, EBS, RDS, or other AWS services. KMS provides and controls the keys used to encrypt that data.

---

## Main use cases

AWS KMS is commonly used when you want to

 Encrypt data stored in AWS services
 Control who can use encryption keys
 Rotate keys for security or compliance
 Audit key usage
 Protect secrets, files, databases, and storage volumes
 Let AWS services encrypt data for you using managed keys

Common examples

 Encrypting files in Amazon S3
 Encrypting disks in Amazon EBS
 Encrypting databases in Amazon RDS
 Protecting secrets in AWS Secrets Manager
 Encrypting application data with your own controlled key

---

## Key features

### 1. Managed encryption keys

AWS KMS lets you create and manage keys used for encryption and decryption.

### 2. Tight AWS integration

KMS works with many AWS services like

 Amazon S3
 Amazon EBS
 Amazon RDS
 AWS Lambda
 AWS Secrets Manager
 Amazon SNS
 Amazon SQS
 Amazon EFS

### 3. Access control

You can control who can use a key through

 Key policies
 IAM policies
 Grants

### 4. Audit trail

KMS usage is logged through AWS CloudTrail, so you can see who used a key and when.

### 5. Key rotation

You can rotate certain KMS keys automatically or on demand to improve security and meet compliance requirements.

### 6. Hardware-backed protection

KMS protects keys using secure hardware security modules (HSMs) managed by AWS.

### 7. Multiple key types

KMS supports

 Symmetric keys
 Asymmetric keys
 Multi-Region keys
 Imported key material in some cases

---

## How it works

Here is the simple flow

1. You create or use a KMS key.
2. An AWS service or your application uses that key.
3. Data is encrypted.
4. When needed, authorized users or services can decrypt the data.
5. AWS logs key usage for auditing.

In many AWS services, this feels easy because the service integrates directly with KMS.

For example

 You upload a file to S3
 You choose SSE-KMS encryption
 S3 uses AWS KMS to protect the encryption process

You do not manually handle all cryptographic steps yourself.

---

## Important KMS key types for the exam

### AWS owned keys

These are fully owned and managed by AWS.

You usually do not see or manage them directly.

### AWS managed keys

These are created and managed by AWS for a specific service in your account.

Example a key automatically created for a service like S3 or EBS.

You can see them, but control is more limited.

### Customer managed keys

These are the most important for the exam.

You create and control them yourself.

You can

 Set permissions
 Enable or disable them
 Rotate them
 Add aliases
 Schedule deletion

Exam tip if the question says you need more control over the key, the answer is usually customer managed key.

---

## Symmetric vs asymmetric keys

### Symmetric key

The same key is used to encrypt and decrypt.

This is the most common type in AWS service encryption.

### Asymmetric key

There is a public key and a private key.

Used for use cases like encryptiondecryption or digital signingverification.

Exam tip most storage encryption questions in Cloud Practitioner are about symmetric keys.

---

## Envelope encryption in simple words

This idea appears often with KMS.

Instead of using a KMS key to directly encrypt large amounts of data every time, AWS often does this

1. KMS creates a data key
2. The data key encrypts the actual data
3. The data key itself is encrypted by the KMS key

This is called envelope encryption.

Why it matters

 Faster for large data
 Secure
 Common in AWS services

---

## Why it is important for the exam

AWS Cloud Practitioner exams often test whether you know

 KMS is for managing encryption keys
 KMS is used with many AWS services for encryption at rest
 Customer managed keys give more control than AWS managed keys
 KMS is different from Secrets Manager
 CloudTrail can audit KMS key usage
 KMS helps with security and compliance

This service is important because AWS security questions often connect encryption, access control, and auditability.

KMS sits right in the middle of all three.

---

## Related AWS services and differences

### AWS KMS vs AWS CloudHSM

 KMS = managed key service, easier to use, integrates deeply with AWS services
 CloudHSM = dedicated HSMs with more direct control and more specialized needs

Easy memory
KMS is easier and more managed. CloudHSM gives deeper control but is more complex.

### AWS KMS vs AWS Secrets Manager

 KMS manages encryption keys
 Secrets Manager stores and rotates secrets like passwords, API keys, and database credentials

Secrets Manager often uses KMS behind the scenes to encrypt the secret.

### AWS KMS vs IAM

 IAM controls who can do what
 KMS manages the encryption keys

IAM controls access, but KMS is the key service itself.

### AWS KMS vs ACM (AWS Certificate Manager)

 KMS manages encryption keys
 ACM manages SSLTLS certificates

KMS is about encryption keys for protecting data. ACM is about certificates for secure network communication.

---

## Common exam traps

### Trap 1 Confusing KMS with Secrets Manager

KMS does not store your database password for retrieval like Secrets Manager does.

KMS manages encryption keys.

### Trap 2 Thinking KMS stores all your data

KMS does not act like a storage service for your files or databases.

It manages the keys used to encrypt them.

### Trap 3 Assuming all keys give the same control

They do not.

 AWS owned keys = least customer control
 AWS managed keys = some visibility, limited control
 Customer managed keys = most control

### Trap 4 Forgetting CloudTrail

KMS usage can be audited with CloudTrail.

This is a common security exam point.

### Trap 5 Mixing KMS and CloudHSM

If the question wants a simple AWS-managed encryption key solution, choose KMS, not CloudHSM.

### Trap 6 Forgetting the word customer managed

When the exam says things like

 full control
 custom permissions
 manual lifecycle control
 schedule deletion
 custom rotation control

it usually points to customer managed KMS keys.

---

## Easy real-world example

Imagine a company stores customer invoices in Amazon S3.

They want

 the files encrypted
 only certain employees to access them
 an audit trail of key usage

Solution

 Store files in Amazon S3
 Use SSE-KMS for encryption
 Control access with IAM + KMS key policy
 Audit usage with CloudTrail

In this example

 S3 stores the files
 KMS manages the encryption key
 IAM controls permissions
 CloudTrail records what happened

---

## Final summary

AWS KMS is the AWS service for managing encryption keys.

It helps you securely create, use, control, and audit keys that protect your data across AWS services.

For the exam, remember these big ideas

 KMS manages keys
 It integrates with many AWS services
 Customer managed keys give the most control
 It supports encryption, access control, auditing, and compliance
 It is often the right answer when the question is about encryption at rest with centralized key management

---

## Short exam answer

AWS KMS is a managed AWS service used to create and control encryption keys for protecting data across AWS services.

---

## Memory trick

Think

KMS = Key Management Service = Keeper of My Keys

It does not store your files.
It does not store your passwords like Secrets Manager.
It mainly protects and controls the keys used to encrypt AWS data.

---

## One-line exam coach tip

When you see encrypt data in AWS with controlled access and audit trail, think AWS KMS.

## Additional Distinct Source Material

## 📚 Types of KMS Keys (Know These!)

 Key Type  Who Creates It  Who Manages It  Cost
------------
 AWS Managed Key  AWS  AWS  Free
 Customer Managed Key (CMK)  You  You  ~$1month
 AWS Owned Key  AWS  AWS (internal)  Free

 💡 Exam tip Customer Managed Keys give you more control (custom policies, rotation control, deletion). AWS Managed Keys are automatic and free but less flexible.

---

## 🔄 Key Rotation

- Customer Managed Keys You can enable automatic rotation every year (optional)
- AWS Managed Keys AWS rotates them automatically every year (you can't turn this off)
- Old key material is kept so old data can still be decrypted — no data loss!

---

## 🏆 Why It's Important for the Exam

The exam loves testing KMS because it appears everywhere encryption is mentioned.
Remember these facts

- KMS = encryption key management
- It integrates with almost every AWS storagedatabase service
- It uses IAM + Key Policies to control access
- All key usage is tracked in CloudTrail
- It is a regional service — keys don't automatically work across regions
- You can use multi-region keys if you explicitly enable it

---

## 🔗 Related AWS Services & Differences

 Service  What It Does  How It Relates to KMS
---------
 AWS CloudHSM  Dedicated hardware security module  You manage the hardware; more control, more cost
 AWS Secrets Manager  Stores secrets (passwords, API keys)  Uses KMS to encrypt the secrets it stores
 AWS Certificate Manager (ACM)  Manages SSLTLS certificates  Not the same as KMS — it's for HTTPS certificates
 AWS IAM  Controls who can do what in AWS  Works with KMS to authorize key usage
 AWS CloudTrail  Logs all API activity  Records every KMS key use automatically

### 🆚 KMS vs CloudHSM — Know the Difference!

  KMS  CloudHSM
---------
 Management  AWS managed  You manage
 Hardware  Shared  Dedicated
 Cost  Low (~$1keymonth)  High (~$1.60hour)
 Use when  Standard encryption needs  Strict compliance requirements

---

## 🚀 Quick Cheat Sheet

```
KMS = Encryption Key Management
CMK = Customer Master Key (your own key)
Automatic rotation = every 365 days
Regional service = keys don't cross regions by default
Audit = CloudTrail logs all key usage
Integrates with = S3, RDS, EBS, Lambda, Secrets Manager, etc.
NOT for = passwords, SSL certs, user credentials
vs CloudHSM = KMS is easier; CloudHSM is dedicated hardware
```

---
