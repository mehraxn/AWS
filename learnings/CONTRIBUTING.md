# Contributing

This repository develops accurate, reviewable study notes for AWS Certified Cloud Practitioner and AWS Certified Solutions Architect – Associate.

## Proposing or Updating a Lesson

Before proposing a lesson, search the inventory, canonical categories, comparisons, and archive for the same topic. Explain the certification relevance and intended depth. For an update, preserve useful material, identify outdated terminology or claims, cite the current official source, and avoid unrelated rewrites.

Report outdated AWS terminology with the file, old term, current term, official evidence, and verification date. Add official AWS documentation, FAQ, pricing, or exam-guide references as descriptive Markdown links under `## References`; do not repeat raw URLs unnecessarily.

## Classification and Structure

Use CPP for supported Cloud Practitioner fundamentals, SAA for supported Solutions Architect Associate design material, and both when official scope supports both. Mark uncertain cases for review. Follow the lesson structure in [AGENTS.md](AGENTS.md), omitting headings that would be empty. Keep CPP fundamentals distinct from SAA architecture depth.

## Files, Links, and Duplicates

Use `NN-kebab-case` categories, lowercase kebab-case service directories, `NN-kebab-case.md` lesson files, and `README.md` indexes. Use UTF-8, configured line endings, and relative links for repository content. Every local link must resolve; anchors should match the target heading. Never create a version-suffixed copy to avoid comparing existing content. Compare candidates and record an approved consolidation in the migration log.

## Validation Commands

```text
python scripts/validate-file-names.py --foundation-only
python scripts/validate-markdown-links.py --foundation-only
python scripts/detect-duplicate-filenames.py
python scripts/generate-repository-report.py
```

Use `--all` on the first two tools for a repository-wide audit; expected legacy warnings do not authorize automatic changes.

## Pull Request Checklist

- [ ] I checked for an existing note on the same topic.
- [ ] I used the repository naming convention.
- [ ] I added the correct CPP and/or SAA badge.
- [ ] I separated CPP fundamentals from SAA design depth.
- [ ] I used current AWS terminology.
- [ ] I added official AWS references.
- [ ] I did not invent pricing, quotas, limits, or exam scope.
- [ ] I ran the repository validation scripts.
- [ ] I checked internal links.
- [ ] I avoided unnecessary duplication.
