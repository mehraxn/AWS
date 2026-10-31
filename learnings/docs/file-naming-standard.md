# File Naming Standard

## Rules

- Root categories use `NN-kebab-case`; service directories use lowercase kebab-case.
- Lessons use a two-digit sequence and descriptive kebab-case: `NN-topic.md`.
- Category and service indexes use `README.md`.
- Use current canonical AWS service names; spell acronyms consistently in prose and lowercase them in paths.
- Prefer ASCII hyphens in paths. Avoid spaces, parentheses, duplicate separators, and trailing whitespace.
- Never use `v1`, `v2`, `final`, `new`, `Claude version`, or `Claude Code` as canonical version labels.
- Store text as UTF-8 and follow `.gitattributes` line endings. Unicode punctuation is allowed in prose, but portable ASCII path names are preferred.

## Examples

Valid:

```text
04-compute/amazon-ec2/01-what-is-amazon-ec2.md
05-storage/amazon-s3/03-s3-storage-classes.md
```

Invalid:

```text
Amazon S3 v2 .md
AWS Fargate (Claude version).md
NEW FINAL EC2.md
```

Number lessons in a stable learning order; do not renumber solely to reflect editing chronology.

[Back to documentation index](README.md)
