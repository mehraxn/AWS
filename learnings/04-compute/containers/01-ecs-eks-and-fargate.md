# Amazon ECS, Amazon EKS, AWS Fargate, and Amazon ECR

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Containers package code and dependencies into portable images. AWS separates four decisions: **ECS or EKS** orchestrates containers, **EC2 or Fargate** supplies compute, and **ECR** stores images.

## Core Services

| Service | Role | Choose it when |
|---|---|---|
| Amazon ECS | AWS-native orchestration using clusters, task definitions, tasks, and services | Tight AWS integration is wanted without Kubernetes APIs |
| Amazon EKS | Managed Kubernetes control plane | Kubernetes compatibility, ecosystem, or portability is required |
| AWS Fargate | Serverless container compute for ECS and EKS | Avoiding worker-node administration is important |
| Amazon ECR | Managed private/public image registry with IAM, scanning, and lifecycle policies | ECS or EKS needs an AWS-integrated image source |

ECS can run on EC2 capacity or Fargate. EKS applications run on EC2 worker nodes or supported Fargate profiles. Fargate is neither an orchestrator nor a registry.

## How It Works

An ECS task definition declares images, resources, networking, IAM roles, ports, and logging. A task is one running copy; an ECS service maintains desired count and integrates with load balancers and Service Auto Scaling.

EKS manages the Kubernetes control plane. Customers still configure workloads, access, networking, and the data plane. Managed node groups reduce worker-node operations. Kubernetes flexibility brings added skills and configuration overhead.

ECR controls pull and push access with IAM. Scanning identifies findings and lifecycle policies manage retained images. Customers patch application dependencies and respond to findings.

## EC2 Capacity Versus Fargate

| Concern | EC2 | Fargate |
|---|---|---|
| Control | Instance type, AMI, host agents, placement | Supported task or pod resource choices |
| Operations | Patch, secure, and scale worker nodes | AWS manages hosts |
| Economics | Can suit steady, well-packed fleets | Pay conceptually for allocated resources while running |
| Fit | Host customization or specialized capacity | Standard workloads prioritizing lower operations |

Neither is always cheaper. Include utilization, staffing, data transfer, load balancers, logging, and storage.

## Scaling, Availability, and Security

Run multiple replicas across AZs and let the orchestrator replace failed tasks. Scale the service and, with EC2, worker capacity. A multi-AZ control plane does not make a single replica highly available. Keep durable state outside replaceable containers.

AWS secures managed control planes and Fargate hosts. Customers secure images, dependencies, IAM roles, secrets, networking, workload configuration, logs, and data. With EC2, customers also patch and secure worker instances. Use task or pod roles instead of embedded credentials.

## CPP Knowledge

ECS means AWS-native orchestration, EKS means managed Kubernetes, Fargate avoids managing hosts, and ECR stores images.

## SAA Architecture and Design

- ECS with Fargate suits a stateless API when Kubernetes is unnecessary and low operations matter.
- EKS suits organizational Kubernetes standards and tooling when complexity is acceptable.
- EC2 capacity suits host control, specialized capability, or fleet economics.
- Spread replicas across AZs, use ALB for HTTP routing, and store images in ECR.
- Scaling tasks without sufficient EC2 capacity can leave tasks pending.

## Common Exam Traps

- Fargate works with ECS and EKS; it does not replace them.
- ECR stores images but does not run containers.
- EKS manages its control plane, not every customer workload responsibility.
- Service scaling and EC2 capacity scaling are separate.

## Practice Questions

1. Which service provides Kubernetes compatibility?
2. What worker responsibility does Fargate remove?
3. Which service stores private images?

<details><summary>Answers</summary>

1. EKS. 2. Provisioning, patching, and scaling hosts; workload security remains with the customer. 3. ECR.

</details>

## References

- [Choosing an AWS container service](https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-to-choose/guide.html)
- [What is Amazon ECS?](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
- [What is Amazon ECR?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)

Official references checked: 2026-07-22.
