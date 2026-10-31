# Maintenance and Freshness Guide

## Purpose

Keep the study notes accurate without obscuring provenance or turning every AWS change into a broad rewrite.

## Source priority

1. Current official certification exam guides and official in-scope service lists.
2. Official AWS service, pricing, security, and product documentation.
3. AWS announcements only when needed to establish a dated transition.
4. Third-party sources only as supplements.

## Review cadence

- Before every release: exam guides, service lists, links, filenames, badges, known limitations, and all high-volatility facts.
- Monthly while actively maintained: Support plans, Free Tier, pricing terminology, product names, service availability, and major transitions.
- Quarterly: learning paths, architecture comparisons, AI/responsible-use framing, migration matrices, and references.
- Immediately after a relevant AWS announcement: affected canonical owner, indexes, comparison guides, dashboards, and release limitations.

## High-volatility checklist

- Product and service names, lifecycle, and Regional availability.
- Support plans, response descriptions, Free Tier offers, discounts, and exact prices.
- Quotas, feature matrices, supported migration sources/targets, and hardware offerings.
- AI model availability, provider terms, data handling, guardrails, and responsible-use guidance.
- Certification domains, scope lists, and exam versions.

## Change workflow

1. Inspect `git status` and preserve existing changes.
2. Identify one canonical owner and affected navigation or comparison files.
3. Record the previous claim, corrected claim, official source, and checked date.
4. Make the smallest evidence-backed change; preserve historical wording when it is clearly labeled.
5. Update the relevant dashboard, audit record, migration log for moves, and known limitations.
6. Run filename, link, duplicate, badge, empty-file, claim, and `git diff --check` validation.
7. Request human review before commit, push, tag, or pull request.

## Badge maintenance

Use CPP only for evidenced Cloud Practitioner depth and SAA only for evidenced architecture depth. A badge is not a completeness claim. Re-run the badge audit after content-depth changes.

## Content retirement

Do not silently delete or overwrite useful notes. Compare duplicates, preserve distinct facts, archive superseded material for traceability, use `git mv` for approved moves, and update the migration log.

## Learner feedback

Treat broken routes, ambiguous questions, missing explanations, and outdated terminology as tracked maintenance issues. Do not add recalled live-exam content.
