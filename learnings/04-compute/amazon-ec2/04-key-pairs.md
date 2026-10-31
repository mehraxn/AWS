# Amazon EC2 Key Pairs

## Simple definition

An Amazon EC2 key pair is a set of two cryptographic keys used to help you securely access an EC2 instance.

It includes

 a public key
 a private key

In AWS, the public key is placed on the EC2 instance, and you keep the private key.

---

## Core idea in plain English

Think of an EC2 instance like a locked computer in the cloud.

A key pair helps prove that you are allowed to enter that computer.

AWS keeps one part of the key on the instance, and you keep the secret part. When you connect, the two parts work together to allow secure access.

For the Cloud Practitioner exam, the big idea is simple

Key pairs are mainly about securely accessing Amazon EC2 instances.

---

## Main use cases

### 1. Secure login to Linux EC2 instances

You commonly use the private key with SSH to connect to a Linux EC2 instance.

### 2. Decrypting the Windows administrator password

For Windows EC2 instances, the key pair is used to help retrieve or decrypt the initial administrator password.

### 3. Avoiding simple password-based access

Key pairs provide stronger and more secure access than using only a normal password.

### 4. Instance launch configuration

When you launch an EC2 instance, AWS can associate a key pair with it so you can access it later.

---

## Key features

 Used mainly with Amazon EC2
 Consists of a public key and a private key
 The public key is stored on the instance
 The private key is kept by the user
 Commonly used for Linux SSH access
 Used for Windows password decryption
 Helps improve secure access to cloud servers
 Key pairs are tied to instance access, not general AWS account login

---

## How it works

### Step 1 Create or choose a key pair

You can create a key pair in AWS or import a public key.

### Step 2 Launch an EC2 instance

When launching the instance, you select the key pair.

### Step 3 AWS places the public key on the instance

The instance keeps the public key so it can verify access requests.

### Step 4 You keep the private key safely

You download and store the private key. AWS does not keep giving it back to you later in the same way, so you must protect it.

### Step 5 Use the private key to connect

 For Linux, you use it with SSH
 For Windows, you use it to decrypt the administrator password

### Step 6 Access is granted if the keys match correctly

If the private key matches the public key on the instance, access works.

---

## Why it is important for the exam

This topic matters because AWS exams often test whether you understand

 what key pairs are used for
 which AWS service they belong to
 the difference between key pairs and passwords
 the difference between key pairs and IAM credentials
 Linux vs Windows EC2 access methods

In the exam, AWS may try to confuse you by mixing up

 EC2 key pairs
 IAM usernames and passwords
 security groups
 KMS encryption keys
 Secrets Manager secrets

You need to keep the purpose of each one clear.

---

## Related AWS services and differences

### Amazon EC2

This is the main service related to key pairs.

Key point
EC2 key pairs are for instance access.

### IAM

IAM manages users, groups, roles, permissions, and account-level access to AWS services.

Difference

 IAM credentials let you access AWS resources and the AWS account
 EC2 key pairs let you access the operating system of an EC2 instance

### Security Groups

Security groups control network traffic to and from an EC2 instance.

Difference

 Security groups decide whether traffic like SSH or RDP is allowed
 Key pairs help prove who can log in after network access is allowed

### AWS KMS

AWS Key Management Service manages encryption keys.

Difference

 KMS keys are for encrypting data
 EC2 key pairs are for instance access

### AWS Secrets Manager

Secrets Manager stores and manages secrets such as passwords and API keys.

Difference

 Secrets Manager stores secrets securely
 EC2 key pairs are specifically used for EC2 access scenarios

### Amazon Lightsail

Lightsail also provides virtual servers and may involve SSH access concepts.

Difference

 EC2 is more flexible and detailed
 Lightsail is simpler and more beginner-friendly
 In the exam, key pairs are most strongly associated with EC2

---

## Common exam traps

### Trap 1 Thinking key pairs are for AWS account login

They are not used to sign in to the AWS Management Console.

### Trap 2 Thinking key pairs are the same as IAM credentials

They are different.
IAM controls access to AWS services.
Key pairs help with operating system access to EC2 instances.

### Trap 3 Confusing key pairs with security groups

A security group allows or denies network traffic.
A key pair helps authenticate access to the instance.

### Trap 4 Confusing key pairs with KMS keys

KMS is for encryption management.
EC2 key pairs are for connecting to instances.

### Trap 5 Forgetting Linux vs Windows differences

 Linux EC2 usually SSH with the private key
 Windows EC2 use the key pair to decrypt the administrator password, then connect with RDP

### Trap 6 Thinking all AWS services use key pairs this way

For Cloud Practitioner, the strongest and most direct connection is

Key pairs = Amazon EC2 access

---

## Easy real-world example

Imagine you rent a private office in a large building.

 The building is AWS
 The office is your EC2 instance
 The door lock is the instance access control
 The key pair is your secure way to open the office door

The office already has one part of the lock setup, and you keep the private key.
If you lose your private key, getting in becomes much harder.

This is why private keys must be stored safely.

---

## If I were an examiner ...

If I were writing Cloud Practitioner exam questions, I would test whether you can correctly connect EC2 key pairs with instance access and not confuse them with other AWS tools.

I would ask things like

### 1. Purpose questions

 What is the main purpose of an EC2 key pair
 Which AWS resource is most directly associated with key pairs

### 2. Difference questions

 What is the difference between an EC2 key pair and IAM user credentials
 What is the difference between a key pair and a security group
 What is the difference between a key pair and a KMS key

### 3. Scenario questions

 A user wants to securely connect to a Linux EC2 instance. What should they use
 A user wants to retrieve the initial administrator password for a Windows EC2 instance. What is used

### 4. Trap questions

 Which service uses key pairs for instance access EC2, S3, Lambda, or DynamoDB
 Which AWS feature controls inbound SSH traffic key pairs or security groups

### 5. Best-answer questions

I would often give answer choices that sound similar, such as

 IAM password
 Security group
 Key pair
 KMS key

Then I would check whether you really know that

Key pairs are for secure EC2 instance access.

---

## Final summary

Amazon EC2 key pairs are a secure access method used mainly with EC2 instances.

They include a public key and a private key.
The public key is placed on the instance, and the private key is kept by the user.

For Linux instances, key pairs are commonly used with SSH.
For Windows instances, they are used to decrypt the initial administrator password.

For the Cloud Practitioner exam, remember that key pairs are not the same as IAM credentials, security groups, or KMS encryption keys.

Their main purpose is simple

secure access to EC2 instances

---

## Short exam answer

Amazon EC2 key pairs are used to securely access EC2 instances.

 Linux usually for SSH access
 Windows used to decrypt the administrator password

---

## Memory trick

Remember this sentence

Key pairs open EC2 doors.

Another easy memory trick

 IAM = access to AWS services
 Security Group = traffic allowed or blocked
 Key Pair = access to the EC2 machine itself
 KMS = encryption keys for data

So if the exam asks about logging in to a cloud server, think

EC2 - Key Pair
