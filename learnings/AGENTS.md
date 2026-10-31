# Repository Instructions for Codex

## Repository Purpose

This repository contains educational notes for AWS Certified Cloud Practitioner (CPP) and AWS Certified Solutions Architect – Associate (SAA).

## Content Preservation

- Preserve useful existing content and avoid rewriting unrelated material.
- Never delete notes without explicit authorization.
- Compare duplicate files before consolidation and preserve every distinct useful fact.
- Archive superseded versions for traceability instead of silently deleting them.
- Maintain the migration log for every approved move, merge, rename, or archive action.

## Git Safety

- Inspect `git status` before changes and preserve pre-existing user changes.
- Do not use destructive Git commands, commit, or push unless explicitly requested.
- Use `git mv` for approved migrations and keep each phase small and reviewable.
- Keep moves separate from content rewrites or duplicate consolidation.

## Certification Labels

CPP badge:

```markdown
![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
```

SAA badge:

```markdown
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)
```

Use the CPP badge only for Cloud Practitioner relevance, the SAA badge only for Solutions Architect Associate relevance, and both when both mappings are supported. Never infer a badge from assumptions alone; mark uncertain mappings for review.

## Required Lesson Structure

Future canonical service notes should generally use this structure:

```markdown
# Service or Topic Name

[Certification badges]

## Overview
## What Problem It Solves
## Core Concepts
## Main Features
## How It Works
## Common Use Cases
## Pricing Fundamentals
## Security and Shared Responsibility
## High Availability and Resilience
## Performance and Scalability
## Cost Optimization
## CPP Knowledge
## SAA Architecture and Design
## Comparison with Similar Services
## Common Exam Scenarios
## Exam Traps
## Summary
## Practice Questions
## References
```

Not every awareness-level service needs every section. Do not add empty headings merely to satisfy the template.

## Content Depth

CPP content focuses on definitions, service purpose, basic benefits and use cases, basic pricing, shared responsibility, service recognition, and general cloud concepts. SAA content additionally covers architecture and integration, high availability, fault tolerance, scalability, performance, security, cost optimization, disaster recovery, networking, storage and database decisions, trade-offs, and scenario-based selection.

## Style

- Use beginner-friendly explanations, accurate AWS terminology, clear headings, short paragraphs, practical examples, and comparison tables where useful.
- Use Mermaid only when it adds real explanatory value.
- Do not make unsupported claims or invent quotas, limits, prices, exam percentages, or references.
- Avoid marketing language, excessive emoji, unnecessary repetition, and large copied passages.

## Naming and Text Rules

- Root category directories: `NN-kebab-case`; service directories: lowercase kebab-case.
- Lesson files: `NN-kebab-case.md`; index files: `README.md`.
- Canonical paths contain no spaces, unnecessary parentheses, or duplicate separators.
- Do not use `v1`, `v2`, `final`, `new`, `Claude version`, or `Claude Code` in canonical filenames.
- Use UTF-8 text, LF line endings (except PowerShell files as configured), and no trailing spaces.

## Sources

- Treat official AWS sources as primary authority, use current service names, and use current official exam guides for scope decisions.
- Add a checked date to date-sensitive claims. Use third-party sources only as supplements.
- Paraphrase and cite; do not copy large copyrighted passages.

## Scope

- Do not expand awareness-level CPP services into excessive implementation depth or reduce SAA topics to simple definitions.
- Do not add unrelated certifications.
- Do not add Kubernetes, Terraform, Ansible, or unrelated DevOps material unless it is directly connected to AWS certification scope and explicitly requested.
- Do not treat every AWS service as equally important.
