# AWS Systems Manager Session Manager

## Simple definition

AWS Systems Manager Session Manager is a feature of AWS Systems Manager that lets you securely connect to and manage EC2 instances and other managed nodes without opening inbound ports or using a bastion host.

## Core idea in plain English

Think of Session Manager as a safer remote access door into your servers.

Instead of opening SSH port 22 or RDP port 3389 to the internet, AWS lets you start a secure session through Systems Manager. This reduces security risk and makes access easier to control.

## Main use cases

 Connect to a private EC2 instance without opening inbound ports
 Access Windows or Linux instances more securely
 Replace or reduce the need for a bastion host
 Troubleshoot servers in private subnets
 Manage on-premises servers or hybrid machines that are registered with Systems Manager
 Centralize access control and session logging

## Key features

 Browser-based shell access from the AWS Console
 Command-line access from the AWS CLI
 No need to open inbound SSH or RDP ports
 No need to manage SSH keys for normal Session Manager sessions
 IAM-based access control
 Session logging to Amazon S3 or CloudWatch Logs
 Support for EC2 instances and other managed nodes
 Port forwarding support for some advanced access scenarios

## How it works

1. Your EC2 instance must be a managed node in AWS Systems Manager.
2. The instance needs the SSM Agent installed and an IAM role that allows Systems Manager access.
3. A user with the right IAM permissions starts a session from the AWS Console or AWS CLI.
4. Systems Manager creates a secure connection to the instance.
5. The user gets shell access without exposing the instance directly to the public internet.

## Why it is important for the exam

This topic is important because AWS exam questions often test secure administration of EC2 instances.

The exam likes answers that

 reduce the attack surface
 avoid opening unnecessary inbound ports
 avoid public access when possible
 use managed AWS services instead of self-managed infrastructure

Session Manager is often the best answer when the question asks for secure, simple, auditable remote access to EC2 instances.

## Related AWS services and differences

### AWS Systems Manager vs Session Manager

 AWS Systems Manager is the bigger service
 Session Manager is one feature inside Systems Manager

Systems Manager includes many tools such as Patch Manager, Run Command, Automation, Parameter Store, and Session Manager.

### Session Manager vs SSH

 SSH usually needs port 22 open and often uses SSH keys
 Session Manager does not require opening inbound ports for standard sessions

For exam questions, Session Manager is usually the more secure and more managed answer.

### Session Manager vs RDP

 RDP is commonly used to access Windows servers and usually needs port 3389
 Session Manager avoids opening that inbound port for administrative access

### Session Manager vs Bastion Host

 Bastion host is a jump server that you manage yourself
 Session Manager is AWS-managed and reduces the need for a bastion host

For Cloud Practitioner, AWS usually prefers the managed option when security and simplicity matter.

### Session Manager vs EC2 Instance Connect

 EC2 Instance Connect is mainly for quick SSH access to Linux EC2 instances
 Session Manager is broader and more security-focused for managed node access
 Session Manager also supports logging and works without opening inbound ports for standard sessions

### Session Manager vs Run Command

 Session Manager is for interactive access
 Run Command is for sending commands without opening an interactive shell

## Common exam traps

### Trap 1 Thinking Session Manager is a separate AWS service

It is not a separate standalone service. It is a capability of AWS Systems Manager.

### Trap 2 Forgetting the security benefit

The big exam keyword is no inbound ports required for standard sessions.

### Trap 3 Mixing it up with bastion hosts

A bastion host is still a server you manage. Session Manager is a managed AWS feature that can replace or reduce bastion host usage.

### Trap 4 Assuming it works automatically on every EC2 instance

The instance must be configured correctly

 SSM Agent must be installed
 the instance needs the right IAM role
 the instance must be reachable by Systems Manager endpoints

### Trap 5 Assuming all session types are logged the same way

Standard Session Manager sessions can be logged, but SSH and port-forwarding sessions do not provide the same session content logging.

## Easy real-world example

A company has EC2 instances in a private subnet. The admin team needs to log in for troubleshooting.

Instead of opening SSH to the internet or building a bastion host, the company uses Session Manager.

Admins sign in to AWS, start a session, and safely access the instance. This is simpler, safer, and easier to control with IAM.

## Final summary

AWS Systems Manager Session Manager is a secure way to access EC2 instances and other managed nodes.

Its biggest exam value is that it lets you connect without opening inbound ports, without relying on bastion hosts, and with IAM-based control.

For the exam, remember that Session Manager is usually the best answer when AWS wants secure administrative access with less operational overhead.

## Short exam answer

Session Manager is a feature of AWS Systems Manager that provides secure remote access to EC2 instances and other managed nodes without opening inbound ports or managing bastion hosts.

## Memory trick

Session Manager = safe server session without open doors

Or even shorter

Session Manager = connect privately, not publicly
