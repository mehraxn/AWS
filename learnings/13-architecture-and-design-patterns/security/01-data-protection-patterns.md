# Data Protection Patterns on AWS

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Data protection is an architecture, not a single encryption switch. A sound design classifies data, encrypts it in transit and at rest, separates key administration from key use, avoids hard-coded secrets, rotates credentials, records access, and plans for loss of a key, certificate, or dependency.

## Start with the Data Flow

For each path, identify where plaintext exists, who needs access, and where trust changes:

1. A client establishes TLS to an AWS endpoint.
2. The application authenticates and retrieves configuration or a secret at runtime.
3. The application or AWS service encrypts stored data with a data key.
4. AWS KMS protects the data key and authorizes cryptographic operations.
5. CloudTrail and service logs provide evidence for review and response.

Encryption does not replace authorization. A principal still needs permission to read the protected resource and, when applicable, permission to use its KMS key.

## AWS KMS and Key Ownership

AWS Key Management Service creates and controls KMS keys and performs cryptographic operations. Common ownership choices are:

| Key choice | Control | Operational effort | Typical fit |
|---|---|---|---|
| AWS owned key | AWS owns and manages it across a service | Lowest | Default service encryption when extra key control is unnecessary |
| AWS managed key | Visible service-specific key in the account; AWS manages its lifecycle | Low | Service encryption with limited customization |
| Customer managed key | Customer controls policy, lifecycle, rotation choices, aliases, grants, and monitoring | Higher | Separation of duties, cross-account access, or explicit compliance controls |

A KMS key policy is the primary resource policy for a KMS key. IAM policies and grants can participate only as the key policy permits. Use least privilege for both key administrators and key users; do not make application roles key administrators.

KMS keys are Regional resources. Multi-Region keys can support particular multi-Region designs, but they do not make application data replicate automatically.

## Envelope Encryption

Envelope encryption protects large data efficiently:

1. Generate a plaintext data key and an encrypted copy of that data key.
2. Encrypt the application data locally with the plaintext data key.
3. Remove the plaintext key from memory as soon as practical.
4. Store the ciphertext beside the encrypted data key.
5. On read, KMS decrypts the encrypted data key for an authorized principal; the application then decrypts the data.

The KMS key protects the smaller data key rather than processing every byte of application data. An encryption context can bind a cryptographic request to attributes such as an application or tenant and can be required in key-policy conditions.

## TLS and AWS Certificate Manager

TLS protects data in transit and authenticates endpoints. AWS Certificate Manager (ACM) provisions and manages certificates for supported integrations such as Elastic Load Balancing, API Gateway, and CloudFront. ACM certificates are Regional resources; CloudFront has specific certificate-Region requirements, so verify the consuming service before deployment.

Managed renewal applies only when certificate and validation requirements remain satisfied. Imported certificates and certificates used outside supported managed patterns can require different renewal operations. Monitor renewal status and preserve DNS validation records.

For end-to-end protection, decide whether TLS terminates at an edge service or load balancer and whether a second TLS connection is required to the backend. See [TLS with load balancers and RDS](../transport-layer-security/02-tls-with-load-balancers-and-rds.md).

## Secrets Manager and Parameter Store

| Requirement | Prefer |
|---|---|
| Database credentials, API keys, or tokens with managed lifecycle and rotation | AWS Secrets Manager |
| Hierarchical configuration, feature flags, AMI IDs, or SecureString parameters | Systems Manager Parameter Store |
| Cryptographic keys and encrypt/decrypt authorization | AWS KMS |
| Public or private TLS certificate lifecycle for supported integrations | ACM |

Secrets Manager stores secrets encrypted and supports managed or Lambda-based rotation patterns depending on the secret. Rotation must update both the stored value and the service that validates it. Applications should retrieve secrets at runtime and tolerate version transitions rather than embedding credentials in code or images.

Parameter Store supports configuration values and encrypted `SecureString` values. It is not a universal replacement for Secrets Manager rotation workflows. Both services require least-privilege IAM and KMS permissions, careful logging, and application-side caching decisions.

## Rotation and Failure Behavior

- Test credential rotation with connection pools, caches, replicas, and rollback paths.
- Monitor certificate renewal and secret-rotation failures before expiration causes an outage.
- Prevent accidental key deletion and understand the recovery consequences before scheduling deletion.
- Keep encrypted backups useful by retaining authorized access to the protecting keys.
- Plan cross-account key policies explicitly; resource access alone does not imply key access.
- Treat denied decrypt operations, throttling, or a Regional dependency failure as application failure modes.

## Security and Monitoring

Use separation of duties, encryption-context conditions where appropriate, CloudTrail for KMS and secret-management API activity, service logs, alarms on rotation or certificate issues, and periodic access review. Never place plaintext secrets in logs, traces, user data, source control, or infrastructure outputs.

## Cost Considerations

Cost can include customer managed KMS keys and requests, Secrets Manager secret storage and API calls, rotation functions, private-certificate infrastructure, logging, and cross-Region designs. AWS managed options reduce administration but may provide less policy control. Choose the simplest design that meets the data classification and audit requirements.

## CPP Exam Focus

- KMS: encryption keys and cryptographic operations.
- Secrets Manager: secret storage and rotation.
- Parameter Store: configuration and SecureString parameters.
- ACM: TLS certificates for supported AWS integrations.
- TLS protects data in transit; service encryption protects data at rest.

## SAA Design Scenarios

1. An application needs rotating database credentials: use Secrets Manager with a rotation-compatible database and runtime retrieval.
2. A regulated workload requires separation of key administrators and data readers: use a customer managed KMS key with separate administration and usage permissions.
3. Large objects need client-side encryption: use envelope encryption, storing encrypted data keys with ciphertext.
4. A load-balanced public application needs managed TLS: use ACM with the load balancer and monitor renewal eligibility.
5. A cross-account consumer reads encrypted data: authorize both the data resource and the KMS key; test the full path.

## Common Mistakes

- Assuming an IAM allow always grants KMS use without a compatible key policy.
- Calling KMS a secret database or Secrets Manager a key-management service.
- Rotating the stored password without updating the target system.
- Assuming encryption creates backups, replication, or high availability.
- Assuming ACM manages every certificate deployed on every server.

## Knowledge Check

1. Why are both resource and KMS permissions often required? 2. What does envelope encryption protect with the KMS key? 3. Which service best fits rotating database credentials? 4. Does a Multi-Region KMS key replicate application data? 5. What operational condition can prevent managed certificate renewal?

<details><summary>Answers</summary>

1. Reading ciphertext and decrypting its data key are separate authorization decisions. 2. The data key, while the data key encrypts the payload. 3. Secrets Manager. 4. No. 5. Loss of renewal eligibility, such as broken validation or unsupported use.

</details>

## Related Lessons

- [AWS KMS](../../09-security-and-compliance/aws-kms/01-overview.md)
- [AWS Secrets Manager](../../09-security-and-compliance/aws-secrets-manager/01-overview.md)
- [AWS Certificate Manager](../../09-security-and-compliance/aws-certificate-manager/01-overview.md)
- [IAM](../../03-identity-governance-and-organizations/aws-iam/01-overview.md)

## References

Checked: 2026-07-24.

- [AWS KMS key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)
- [AWS KMS cryptography essentials](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html)
- [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [ACM managed certificate renewal](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html)
