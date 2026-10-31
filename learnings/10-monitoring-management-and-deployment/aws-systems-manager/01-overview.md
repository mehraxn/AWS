# AWS Systems Manager

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Simple definition

AWS Systems Manager is an AWS service that helps you manage, patch, configure, and automate your servers and other compute resources from one central place.

## Core idea in plain English

Think of AWS Systems Manager as a control center for your machines.

Instead of logging in to each server one by one, you can use Systems Manager to run commands, apply patches, store configuration values, and automate maintenance tasks across many machines at once.

## Main use cases

 Managing EC2 instances at scale
 Running commands on many servers remotely
 Patching operating systems automatically
 Storing configuration values and secrets with Parameter Store
 Opening secure remote sessions without using SSH or bastion hosts
 Automating common admin tasks
 Managing hybrid environments such as on-premises servers together with AWS resources

## Key features

### Run Command

Run commands on one or many managed instances without manually signing in.

### Session Manager

Connect securely to instances without opening inbound ports or managing SSH keys.

### Patch Manager

Automate patching for operating systems and keep instances compliant.

### Parameter Store

Store configuration values, database strings, and other settings in a central place.

### Automation

Use runbooks to automate repeated operational tasks.

### Inventory and compliance

Collect information about your managed nodes and check whether they follow patch or configuration rules.

## How it works

First, your EC2 instance or server becomes a managed node.

To do that, it usually needs

 The SSM Agent installed
 An IAM role or permissions that allow Systems Manager access
 Network access to communicate with the Systems Manager service

Once connected, Systems Manager can send instructions to the managed node.

For example, it can

 Run shell or PowerShell commands
 Start a secure session
 Apply patches
 Store and retrieve parameters
 Trigger automation workflows

This lets administrators manage many systems from one place instead of handling each one separately.

## Why it is important for the exam

AWS Cloud Practitioner questions often test whether you know which service is used to

 Manage EC2 instances centrally
 Patch instances automatically
 Access instances securely without opening SSH ports
 Store configuration values centrally
 Automate operational tasks

Systems Manager is important because it combines several operations tools under one service.

## Related AWS services and differences

### AWS Systems Manager vs Amazon EC2

EC2 gives you virtual servers.

Systems Manager helps you manage those servers after they are running.

### AWS Systems Manager vs AWS OpsWorks

OpsWorks is mainly for configuration management using Chef or Puppet.

Systems Manager is the more general AWS-native service for operational management, patching, automation, and remote access.

### AWS Systems Manager Parameter Store vs AWS Secrets Manager

Parameter Store stores configuration data and secrets.

Secrets Manager is more specialized for managing secrets and supports built-in secret rotation.

Exam tip if the question focuses on automatic secret rotation, the answer is usually Secrets Manager, not Parameter Store.

### AWS Systems Manager vs Amazon CloudWatch

CloudWatch monitors metrics, logs, and alarms.

Systems Manager manages and automates operational tasks on your machines.

### AWS Systems Manager vs AWS Config

AWS Config records and evaluates resource configuration changes.

Systems Manager helps operate and manage servers and nodes.

## Common exam traps

### Trap 1 Confusing Systems Manager with CloudWatch

CloudWatch watches and alerts.

Systems Manager acts and manages.

### Trap 2 Confusing Parameter Store with Secrets Manager

Parameter Store can store secrets, but Secrets Manager is the better answer when automatic rotation is required.

### Trap 3 Thinking Systems Manager is only for EC2

It can also help manage on-premises servers, edge devices, and some multicloud environments.

### Trap 4 Forgetting Session Manager security benefits

Session Manager can access instances without opening inbound ports and without using bastion hosts or SSH keys.

### Trap 5 Forgetting the agent

Systems Manager usually depends on the SSM Agent and correct permissions.

## Easy real-world example

A company has 200 EC2 instances.

The operations team needs to patch them every month, run a script to update software, and sometimes connect to a server to troubleshoot a problem.

Instead of logging in to each machine manually, they use AWS Systems Manager

 Patch Manager to apply patches
 Run Command to run scripts on many servers
 Session Manager to open secure remote sessions
 Parameter Store to keep shared configuration values

This saves time and improves security.

## Final summary

AWS Systems Manager is the AWS service for central operational management of servers and managed nodes.

It helps you run commands, patch systems, automate tasks, store parameters, and connect securely to instances.

For the exam, remember it as the service that helps you manage infrastructure at scale.

## Short exam answer

AWS Systems Manager is a centralized service used to manage, patch, automate, and securely access EC2 instances and other managed nodes across AWS and hybrid environments.

## Memory trick

Systems Manager = system control panel for your servers

Or even shorter

SSM = See, Secure, and Manage machines

 See your managed nodes
 Secure access with Session Manager
 Manage commands, patches, and automation

## Batch 6 Operations Architecture Supplement

The original overview above introduces Systems Manager. This supplement adds the architecture, security, hybrid-management, failure, and selection depth required for Batch 6.

### Managed Nodes and Prerequisites

A managed node can be an EC2 instance, on-premises server, virtual machine, edge device, or supported machine in another cloud that is configured for Systems Manager. Management normally requires:

- A supported SSM Agent or applicable agentless capability.
- An IAM instance profile for EC2 or credentials established through a hybrid activation for non-EC2 nodes.
- Network connectivity to required Systems Manager and related service endpoints, directly or through VPC endpoints where supported.
- Operating-system permissions and trusted repositories appropriate to the requested operation.

Registration is not proof that every operation will succeed. Agent health, permissions, endpoint access, document parameters, maintenance windows, and the target operating system all influence execution.

### Inventory

Systems Manager Inventory collects metadata such as installed applications, files, components, network configuration, services, and patch state from managed nodes. Resource Data Sync and central S3/Athena patterns can support cross-account or cross-Region analysis.

Inventory observes metadata; it does not automatically patch or enforce the desired state. Use the evidence to find unsupported software, missing agents, and configuration differences, then invoke an appropriate maintenance workflow.

### Patch Manager

Patch Manager scans managed nodes for missing patches and installs approved patches for supported operating systems and applications. Patch baselines define approval and rejection rules. Patch policies, maintenance windows, tags, and resource groups help schedule and target work.

Patching is an availability change. Test patches, group nodes into waves, preserve application capacity, define reboot behavior, monitor failures, and retain rollback or replacement procedures. A reported compliant patch state does not prove the application remains healthy.

### Run Command, State Manager, and Automation

- **Run Command** performs commands remotely across selected managed nodes without interactive login.
- **State Manager** uses associations to keep managed nodes in a defined configuration state on a schedule.
- **Automation** executes runbooks with steps, branching, approvals, and integrations for repeatable operational workflows.

Use Run Command for controlled actions, State Manager for recurring desired state, and Automation for multi-step workflows such as AMI updates, remediation, or recovery. Documents and runbooks are powerful code: review versions, restrict who can execute or modify them, validate parameters, and record output safely.

### Parameter Store

Parameter Store organizes configuration in hierarchical names and supports plaintext `String`/`StringList` values and encrypted `SecureString` values. Access to a SecureString can require both Systems Manager and KMS permissions.

Use parameter policies, versions, labels, and least-privilege paths where appropriate. Prefer Secrets Manager when a credential needs a specialized secret lifecycle or managed rotation workflow. Do not place secret values in command output, logs, or unprotected environment dumps.

### Session Manager

Session Manager provides controlled interactive or port-forwarding access to managed nodes without requiring inbound SSH/RDP ports, public IP addresses, or bastion-host SSH keys. IAM authorizes the session and CloudTrail records session API activity; configure session logging where permitted and required.

Session Manager reduces network exposure but does not make administrator access inherently least privilege. Restrict target nodes, session documents, port forwarding, shell profiles, and KMS/log destinations. See the dedicated [Session Manager lesson](02-session-manager.md).

### Hybrid and Multicloud Operations

Hybrid activations register non-EC2 machines as managed nodes. Use dedicated service roles, activation limits appropriate to enrollment, network egress or private connectivity, consistent tags, and clear ownership. Central management can standardize inventory and patching, but differences in operating systems, repositories, latency, and local controls still require testing.

### Security and Audit

- Separate document authors, approvers, and operators.
- Restrict actions by tags, resource groups, document ARN, and allowed parameters where practical.
- Use VPC endpoints to avoid internet traversal when the architecture requires private connectivity.
- Encrypt parameters, command output, inventory destinations, and session logs as required.
- Send API activity to CloudTrail and operational output/metrics to CloudWatch and protected storage.
- Prevent users from choosing arbitrary privileged documents or exfiltration destinations.

Systems Manager performs customer-authorized administration. AWS secures the managed service; customers control node IAM, operating-system privileges, patch policy, targeting, documents, network access, and response to failed operations.

### Failure and Operational Behavior

Commands can partially succeed across a fleet. Design for per-node status, concurrency and error thresholds, retries only for safe operations, idempotent scripts, and a way to quarantine or roll back failed nodes. A disconnected agent receives no live instruction until connectivity and service conditions allow the workflow to continue according to its semantics.

Use maintenance windows and staged deployments to preserve service capacity. For immutable workloads, replacing an instance or image may be safer than repairing it in place.

### Cost Considerations

Some Systems Manager capabilities have no separate base charge, while advanced parameters, higher-throughput parameter use, Automation steps, OpsCenter/Explorer features, logging, storage, KMS, data transfer, and related services can add cost. Verify current pricing for the selected capabilities and compare automation cost with manual operational risk.

### CPP Exam Focus

- Inventory collects managed-node metadata.
- Patch Manager scans and installs approved patches.
- Run Command runs remote commands at scale.
- Automation runs multi-step operational runbooks.
- Parameter Store stores configuration and SecureString parameters.
- Session Manager provides managed access without inbound SSH/RDP.

### SAA Design Scenarios

1. Patch a large fleet while preserving availability: patch baselines/policies, maintenance windows, tags, staged waves, and health validation.
2. Administer private EC2 instances without a bastion: Session Manager with private endpoints and protected session logging.
3. Remediate a Config finding: EventBridge triggers a reviewed Automation runbook with least-privilege role and rollback.
4. Manage on-premises servers alongside EC2: hybrid activation, agent/connectivity design, consistent tags, and central inventory.
5. Store nonsecret application settings: Parameter Store hierarchy; use Secrets Manager when secret rotation is central.

### Knowledge Check

1. Which capability gathers software metadata? 2. Which capability maintains recurring desired state? 3. Why can fleet commands partially fail? 4. What two permission layers can a SecureString require? 5. Does Session Manager remove the need for IAM restrictions?

<details><summary>Answers</summary>

1. Inventory. 2. State Manager. 3. Nodes can differ in connectivity, agent health, permissions, OS state, or command outcome. 4. Systems Manager parameter access and KMS decrypt authorization. 5. No; IAM and session controls remain essential.

</details>

## References

Checked: 2026-07-24.

- [Using AWS Systems Manager tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-tools.html)
- [Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html)
- [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html)
- [Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
