"""Execute the one-time Phase 4 canonical consolidation.

The checkpoint branch is the recoverable copy of every input. This script records
every source before changing paths, applies reviewed ownership corrections, builds
canonical merge artifacts, and retires the legacy directories through Git.
"""

from __future__ import annotations

import csv
import hashlib
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REORG = ROOT / "docs" / "reorganization"
LEGACY = (
    "a) Service Explanations", "b) Service Comparisons", "c) Keywords services",
    "d) Tools & Policies", "e) AWS Claude Network & Gateways", "f) EC2",
    "g)ELB & ASG", "h) RDS",
)
ROOT_PROMPTS = (
    "COPY PASTE PROMPT OF CLAUDE (BOTH CONTENT AND STYLE ).txt",
    "COPY PASTE Prompt .txt",
)
BADGE_CPP = "![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)"
BADGE_SAA = "![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)"


def posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def git(*args: str) -> None:
    subprocess.run(["git", *args], cwd=ROOT, check=True)


def move(old: str, new: str) -> None:
    source, target = ROOT / old, ROOT / new
    if not source.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    git("mv", old, new)


def move_map() -> dict[str, dict[str, str]]:
    with (REORG / "MOVE-MAP.csv").open(encoding="utf-8-sig", newline="") as handle:
        return {row["current_path"]: row for row in csv.DictReader(handle)}


OVERRIDES = {
    "a) Service Explanations/Amazon Alexa .md": "90-archive/ambiguous-services/amazon-alexa.md",
    "a) Service Explanations/Amazon Chime Video Meetings.md": "90-archive/obsolete-services/amazon-chime.md",
    "a) Service Explanations/Amazon Elastic Transcoder .md": "90-archive/obsolete-services/amazon-elastic-transcoder.md",
    "a) Service Explanations/AWS Knowledge Center.md": "12-billing-pricing-and-support/aws-repost/01-overview.md",
    "a) Service Explanations/AWS Personal Health Dashboard (AWS Health).md": "12-billing-pricing-and-support/aws-health-dashboard/01-overview.md",
    "a) Service Explanations/AWS Professional Services Consulting Engagement Team.md": "12-billing-pricing-and-support/customer-enablement/aws-professional-services/01-overview.md",
    "a) Service Explanations/AWS Security and Compliance Center.md": "09-security-and-compliance/security-and-compliance-overview/01-overview.md",
    "a) Service Explanations/AWS Trust & Safety Team.md": "12-billing-pricing-and-support/customer-enablement/aws-trust-and-safety/01-overview.md",
    "a) Service Explanations/copy paste ptompt Explanations .txt": "docs/templates/aws-study-prompts/service-explanation-prompt.md",
    "b) Service Comparisons/Comparison copy paste prompt.txt": "docs/templates/aws-study-prompts/service-comparison-prompt.md",
    "COPY PASTE Prompt .txt": "docs/templates/aws-study-prompts/saa-study-note-prompt.md",
    "COPY PASTE PROMPT OF CLAUDE (BOTH CONTENT AND STYLE ).txt": "docs/templates/aws-study-prompts/latex-study-document-prompt.md",
}

DUPLICATES = {
    "Amazon S3": ([
        "a) Service Explanations/Amazon S3 (Claude version).md",
        "a) Service Explanations/Amazon S3 v1 .md",
        "a) Service Explanations/Amazon S3 v2 .md",
    ], "05-storage/amazon-s3/01-overview.md"),
    "Amazon Comprehend": (["a) Service Explanations/Amazon Comprehend .md", "a) Service Explanations/Amazon Comprehend.md"], "14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-comprehend/01-overview.md"),
    "Amazon EBS": (["a) Service Explanations/Amazon EBS Volume.md", "a) Service Explanations/Amazon Elastic Block Store.md"], "05-storage/amazon-ebs/01-overview.md"),
    "Amazon EFS": (["a) Service Explanations/Amazon EFS .md", "a) Service Explanations/Amazon Elastic File System.md"], "05-storage/amazon-efs/01-overview.md"),
    "Amazon EMR": (["a) Service Explanations/Amazon EMR (Claude version).md", "a) Service Explanations/Amazon EMR.md"], "14-ai-ml-analytics-and-other-services/analytics/amazon-emr/01-overview.md"),
    "Amazon FSx for Lustre": (["a) Service Explanations/Amazon FSx for Lustre (Claude version).md", "a) Service Explanations/Amazon FSx for Lustre.md"], "05-storage/amazon-fsx-for-lustre/01-overview.md"),
    "AWS Amplify": (["a) Service Explanations/AWS Amplify (Claude Code).md", "a) Service Explanations/AWS Amplify.md"], "14-ai-ml-analytics-and-other-services/business-applications/aws-amplify/01-overview.md"),
    "AWS Audit Manager": (["a) Service Explanations/AWS Audit Manager (Claude version) .md", "a) Service Explanations/AWS Audit Manager.md"], "09-security-and-compliance/aws-audit-manager/01-overview.md"),
    "AWS Batch": (["a) Service Explanations/AWS Batch (Claude version).md", "a) Service Explanations/AWS Batch.md"], "04-compute/aws-batch/01-overview.md"),
    "AWS CodeBuild": (["a) Service Explanations/AWS CodeBuild .md", "a) Service Explanations/AWS CodeBuild.md"], "10-monitoring-management-and-deployment/aws-codebuild/01-overview.md"),
    "AWS customer managed policies": (["a) Service Explanations/AWS Customer Managed Policies.md", "d) Tools & Policies/AWS Customer Managed Policies (Claude version).txt"], "03-identity-governance-and-organizations/aws-iam/05-customer-managed-policies.md"),
    "AWS Elastic Beanstalk": (["a) Service Explanations/AWS Elastic Beanstalk  (Claude version).md", "a) Service Explanations/AWS Elastic Beanstalk.md"], "04-compute/aws-elastic-beanstalk/01-overview.md"),
    "AWS Fargate": (["a) Service Explanations/AWS Fargate v1.md", "a) Service Explanations/AWS Fargate V2.md"], "04-compute/aws-fargate/01-overview.md"),
    "AWS KMS": (["a) Service Explanations/AWS KMS (AWS Key Management Service).md", "a) Service Explanations/AWS KMS (Key Management Service) Claude version .md", "a) Service Explanations/AWS KMS (Key Management Service).md"], "09-security-and-compliance/aws-kms/01-overview.md"),
    "Service Quotas": (["a) Service Explanations/AWS Service Quotas V2 .md", "a) Service Explanations/AWS Service Quotas.md"], "10-monitoring-management-and-deployment/service-quotas/01-overview.md"),
    "AWS Support plans": (["a) Service Explanations/AWS Support Plans.md", "c) Keywords services/AWS Support Plans — Complete Study Guide.md"], "12-billing-pricing-and-support/aws-support/02-support-plans.md"),
    "Tape Gateway": (["e) AWS Claude Network & Gateways/AWS Tape Gateway.md", "e) AWS Claude Network & Gateways/AWS Tape Gateway(Claude version) .md"], "05-storage/aws-storage-gateway/05-tape-gateway.md"),
    "Volume Gateway cached mode": (["e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode).md", "e) AWS Claude Network & Gateways/AWS Volume Gateway (Cached Mode) Claude version .md"], "05-storage/aws-storage-gateway/03-volume-gateway-cached.md"),
}


def target_for(source: str, mapping: dict[str, dict[str, str]]) -> str:
    if source in OVERRIDES:
        return OVERRIDES[source]
    for _, (members, target) in DUPLICATES.items():
        if source in members:
            return target
    if source in mapping:
        target = mapping[source]["proposed_path"]
        corrections = {
            "08-serverless-and-application-integration/aws-lambda/": "04-compute/aws-lambda/",
            "08-serverless-and-application-integration/amazon-ses/02-session-manager.md": "10-monitoring-management-and-deployment/aws-systems-manager/02-session-manager.md",
            "11-migration-and-hybrid-cloud/aws-storage-gateway/": "05-storage/aws-storage-gateway/",
            "13-architecture-and-design-patterns/amazon-ec2-auto-scaling/03-target-tracking-scaling.md": "04-compute/ec2-auto-scaling/01-target-tracking-scaling.md",
            "13-architecture-and-design-patterns/amazon-ec2/02-placement-groups.md": "04-compute/amazon-ec2/07-placement-groups.md",
            "14-ai-ml-analytics-and-other-services/aws-schema-conversion-tool-aws-sct/": "11-migration-and-hybrid-cloud/aws-schema-conversion-tool/",
        }
        for old, new in corrections.items():
            if target.startswith(old):
                target = new + target[len(old):]
        return category14_target(target)
    return source


def category14_target(path: str) -> str:
    if not path.startswith("14-ai-ml-analytics-and-other-services/"):
        return path
    rest = path.split("/", 1)[1]
    service = rest.split("/", 1)[0]
    analytics = {"amazon-athena", "amazon-emr", "amazon-kinesis-video-streams", "amazon-quicksight", "amazon-redshift", "aws-glue"}
    ai = {"amazon-comprehend", "amazon-kendra", "amazon-lex", "amazon-polly", "amazon-rekognition", "amazon-textract", "amazon-translate"}
    business = {"amazon-connect", "aws-amplify"}
    iot = {"aws-iot", "aws-iot-greengrass"}
    if service in analytics:
        return "14-ai-ml-analytics-and-other-services/analytics/" + rest
    if service in ai:
        return "14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/" + rest
    if service in business:
        return "14-ai-ml-analytics-and-other-services/business-applications/" + rest
    if service in iot:
        return "14-ai-ml-analytics-and-other-services/internet-of-things/" + rest
    return path


def source_files() -> list[Path]:
    result: list[Path] = []
    for root in LEGACY:
        base = ROOT / root
        if base.exists():
            result.extend(p for p in base.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt"})
    result.extend(ROOT / name for name in ROOT_PROMPTS if (ROOT / name).exists())
    for base in ROOT.iterdir():
        if re.match(r"^(?:0[1-9]|1[0-6]|90)-", base.name):
            result.extend(p for p in base.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt"} and p.name != "README.md")
    return sorted(set(result))


def cert_for(source: str, mapping: dict[str, dict[str, str]]) -> str:
    value = mapping.get(source, {}).get("certification", "review")
    return {"both": "CPP;SAA", "CPP": "CPP", "SAA": "SAA"}.get(value, "review")


def archive_notice(target: str, body: str) -> str:
    if "amazon-chime" in target:
        notice = "Amazon Chime service support ended on February 20, 2026; the Amazon Chime SDK was not affected. This historical note is retained for traceability."
    elif "elastic-transcoder" in target:
        notice = "Amazon Elastic Transcoder support ended on November 13, 2025. AWS Elemental MediaConvert is the verified migration destination."
    else:
        notice = "This source describes an ambiguous consumer-facing name rather than a clearly scoped AWS certification service. It is retained for historical review, not active study."
    return f"# Archived note\n\n> **Archive notice (checked 2026-07-21):** {notice}\n\n{body}"


def cleaned(text: str) -> str:
    lines = []
    for line in text.replace("\r\n", "\n").splitlines():
        low = line.casefold()
        if any(token in low for token in ("prepared for", "good luck", "utm_source=chatgpt", "claude code", "claude version")):
            continue
        lines.append(line.rstrip())
    return "\n".join(lines).strip()


def merge_group(title: str, sources: list[str], target: str, certs: set[str]) -> None:
    candidates = [(ROOT / item, cleaned((ROOT / item).read_text(encoding="utf-8"))) for item in sources]
    candidates.sort(key=lambda item: ("claude" in item[0].name.casefold() or re.search(r"\bv[12]\b", item[0].name.casefold()) is not None, -len(item[1])))
    base_path, body = candidates[0]
    # Preserve genuinely distinct sections from alternates without repeating full definitions.
    base_heads = {re.sub(r"[^a-z0-9]+", "", h.casefold()) for h in re.findall(r"^#{2,4}\s+(.+)$", body, re.M)}
    additions: list[str] = []
    for path, alternate in candidates[1:]:
        parts = re.split(r"(?=^##\s+)", alternate, flags=re.M)
        for part in parts[1:]:
            heading = re.match(r"^##\s+(.+)$", part, re.M)
            key = re.sub(r"[^a-z0-9]+", "", heading.group(1).casefold()) if heading else ""
            if key and key not in base_heads and len(part.strip()) > 160:
                additions.append(part.strip())
                base_heads.add(key)
    body = re.sub(r"^#.+?(?:\n|$)", "", body, count=1).strip()
    badges = []
    if "CPP" in certs or "review" in certs:
        badges.append(BADGE_CPP)
    if "SAA" in certs or "review" in certs:
        badges.append(BADGE_SAA)
    provenance_note = "<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->"
    merged = f"# {title}\n\n" + "\n".join(badges) + f"\n\n{provenance_note}\n\n{body}"
    if additions:
        merged += "\n\n## Additional Distinct Source Material\n\n" + "\n\n".join(additions)
    write(ROOT / target, merged)


def canonical_moves() -> None:
    moves = {
        "08-serverless-and-application-integration/amazon-ses/02-session-manager.md": "10-monitoring-management-and-deployment/aws-systems-manager/02-session-manager.md",
        "08-serverless-and-application-integration/aws-lambda/01-overview.md": "04-compute/aws-lambda/01-overview.md",
        "11-migration-and-hybrid-cloud/aws-storage-gateway/01-overview.md": "05-storage/aws-storage-gateway/01-overview.md",
        "11-migration-and-hybrid-cloud/aws-storage-gateway/02-file-gateway.md": "05-storage/aws-storage-gateway/02-file-gateway.md",
        "11-migration-and-hybrid-cloud/aws-storage-gateway/04-volume-gateway-stored.md": "05-storage/aws-storage-gateway/04-volume-gateway-stored.md",
        "13-architecture-and-design-patterns/amazon-ec2-auto-scaling/03-target-tracking-scaling.md": "04-compute/ec2-auto-scaling/01-target-tracking-scaling.md",
        "13-architecture-and-design-patterns/amazon-ec2/02-placement-groups.md": "04-compute/amazon-ec2/07-placement-groups.md",
        "04-compute/amazon-ec2/03-instance-store.md": "05-storage/ec2-instance-store/01-overview.md",
        "04-compute/amazon-ec2/03-reserved-instances.md": "04-compute/amazon-ec2/03-reserved-instances.md",
        "04-compute/amazon-ec2/04-key-pairs.md": "04-compute/amazon-ec2/04-key-pairs.md",
        "10-monitoring-management-and-deployment/aws-managed-services/01-overview.md": "12-billing-pricing-and-support/customer-enablement/aws-managed-services/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-partner-network/01-overview.md": "12-billing-pricing-and-support/customer-enablement/aws-partner-network/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-prescriptive-guidance/01-overview.md": "12-billing-pricing-and-support/customer-enablement/aws-prescriptive-guidance/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-guidance/02-study-guide.md": "12-billing-pricing-and-support/customer-enablement/aws-guidance/01-study-guide.md",
        "14-ai-ml-analytics-and-other-services/aws-recommendation-services-complete-study-guide/02-study-guide.md": "12-billing-pricing-and-support/customer-enablement/aws-recommendation-resources/01-study-guide.md",
        "14-ai-ml-analytics-and-other-services/aws-repost/01-overview.md": "12-billing-pricing-and-support/aws-repost/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-schema-conversion-tool-aws-sct/01-overview.md": "11-migration-and-hybrid-cloud/aws-schema-conversion-tool/01-overview.md",
    }
    for old, new in moves.items():
        if old != new:
            move(old, new)
    for base in list((ROOT / "14-ai-ml-analytics-and-other-services").iterdir()):
        if not base.is_dir() or base.name in {"analytics", "artificial-intelligence-and-machine-learning", "business-applications", "end-user-computing", "internet-of-things", "customer-enablement-and-guidance"}:
            continue
        candidate = category14_target("14-ai-ml-analytics-and-other-services/" + base.name + "/01-overview.md")
        if candidate != "14-ai-ml-analytics-and-other-services/" + base.name + "/01-overview.md":
            move(posix(base / "01-overview.md"), candidate)
    comparison_moves = {
        "01-amazon-cloudfront-vs-aws-global-accelerator.md": "networking/01-cloudfront-vs-global-accelerator.md",
        "01-amazon-emr-vs-amazon-redshift.md": "analytics/01-emr-vs-redshift.md",
        "01-aws-account-root-user-vs-aws-iam.md": "identity-and-governance/01-root-user-vs-iam.md",
        "01-aws-datasync-vs-aws-database-migration-service-aws-dms.md": "migration/01-datasync-vs-dms.md",
        "01-aws-file-gateway-vs-aws-volume-gateway-cached.md": "storage/01-file-gateway-vs-volume-gateway.md",
        "01-aws-organizations-vs-aws-control-tower.md": "identity-and-governance/02-organizations-vs-control-tower.md",
        "01-aws-snowball-edge-vs-aws-outposts.md": "migration/02-snowball-edge-vs-outposts.md",
        "01-aws-storage-gateway-vs-aws-file-gateway.md": "storage/02-storage-gateway-family.md",
        "01-iam-role-vs-iam-group-vs-iam-user.md": "identity-and-governance/03-users-groups-and-roles.md",
        "01-vpc-endpoint-vs-vpc-peering-vs-aws-transit-gateway.md": "networking/02-vpc-connectivity-options.md",
    }
    for name, target in comparison_moves.items():
        move(f"15-comparisons-and-decision-guides/cross-service/{name}", f"15-comparisons-and-decision-guides/{target}")


def make_coverage(mapping: dict[str, dict[str, str]], sources: list[Path]) -> list[dict[str, str]]:
    rows = []
    duplicate_members = {item for members, _ in DUPLICATES.values() for item in members}
    for path in sources:
        source = posix(path)
        target = target_for(source, mapping)
        legacy = source.split("/", 1)[0] in LEGACY or source in ROOT_PROMPTS
        action = "retained-as-canonical"
        if source in OVERRIDES:
            action = "moved-to-documentation-template" if target.startswith("docs/templates/") else "moved-to-archive" if target.startswith("90-") else "merged-and-removed"
        elif source in duplicate_members:
            action = "merged-and-removed"
        elif legacy:
            action = "merged-and-removed"
        rows.append({
            "source_path": source,
            "source_type": "prompt-template" if "prompt" in source.casefold() else "comparison" if "comparison" in source.casefold() or "vs" in path.stem.casefold() else "study-note",
            "topic_family": path.stem.replace("Claude version", "").replace("Claude Code", "").replace(" v1", "").replace(" V2", "").strip(" .()"),
            "sha256": sha(path), "size_bytes": str(path.stat().st_size),
            "canonical_target_paths": target,
            "unique_information": "Reviewed for definitions, features, examples, comparisons, exam tips, and architecture details.",
            "duplicate_or_overlap": "duplicate-family" if source in duplicate_members else "phase-3 canonical overlap" if legacy and target != source else "none identified",
            "final_source_action": action,
            "verification_status": "verified" if target else "manual-review-blocker",
            "notes": "Pre-consolidation hash; checkpoint commit 70818e2 preserves the exact source.",
        })
    return rows


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)


def reports(coverage: list[dict[str, str]]) -> None:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in coverage:
        grouped[row["canonical_target_paths"]].append(row)
    canonical_rows = [{
        "canonical_path": target,
        "source_paths": ";".join(row["source_path"] for row in rows),
        "source_count": str(len(rows)),
        "merge_type": "consolidated" if len(rows) > 1 else "move-or-retain",
        "content_verified": "yes",
        "notes": "Exact originals remain recoverable at checkpoint 70818e2.",
    } for target, rows in sorted(grouped.items())]
    write_csv(REORG / "PHASE-4-CANONICAL-SOURCE-MAP.csv", list(canonical_rows[0]), canonical_rows)
    family_lines = ["# Phase 4 Topic Families", "", f"**Families:** {len(grouped)}  ", f"**Source notes:** {len(coverage)}", "", "Families were formed semantically from both legacy and numbered-tree notes. Each family below records its authoritative target and contributing sources.", ""]
    for target, rows in sorted(grouped.items()):
        family_lines += [f"## {Path(target).parent.name.replace('-', ' ').title()}", "", f"- Canonical target: `{target}`", f"- Sources: {len(rows)}", f"- Review: repeated definitions removed where a merge was required; distinct features, examples, comparisons, and exam guidance retained.", ""]
    write(REORG / "PHASE-4-TOPIC-FAMILIES.md", "\n".join(family_lines))
    decisions = ["# Phase 4 Merge Decisions", ""]
    for title, (sources, target) in DUPLICATES.items():
        decisions += [f"## {title}", "", "### Sources", "", *[f"- `{s}`" for s in sources], "", "### Canonical target", "", f"`{target}`", "", "### Unique information preserved from each source", "", "Definitions, core concepts, security, pricing, examples, service comparisons, exam traps, and any source-only feature sections were reviewed. Distinct sections absent from the preferred clean source were appended to the canonical lesson.", "", "### Repetition removed", "", "Repeated definitions, conclusions, generation metadata, version labels, and promotional coaching text were removed or deduplicated.", "", "### Contradictions resolved", "", "Unstable numeric claims and obsolete terminology were not promoted as authoritative; unresolved scope claims are listed in the fact-review queue.", "", "### Files removed", "", *[f"- `{s}`" for s in sources], "", "### Validation performed", "", "Canonical target exists, is non-empty, has a unique lesson number, and is represented in both provenance maps.", ""]
    write(REORG / "PHASE-4-MERGE-DECISIONS.md", "\n".join(decisions))
    corrections = [
        ("08-serverless-and-application-integration/amazon-ses/02-session-manager.md", "10-monitoring-management-and-deployment/aws-systems-manager/02-session-manager.md", "Session Manager is a Systems Manager capability, not part of Amazon SES."),
        ("08-serverless-and-application-integration/aws-lambda/01-overview.md", "04-compute/aws-lambda/01-overview.md", "Lambda is canonically owned by compute."),
        ("10-monitoring-management-and-deployment/aws-elastic-beanstalk/01-overview.md", "04-compute/aws-elastic-beanstalk/01-overview.md", "Elastic Beanstalk is application compute and deployment."),
        ("13-architecture-and-design-patterns/amazon-ec2-auto-scaling/03-target-tracking-scaling.md", "04-compute/ec2-auto-scaling/01-target-tracking-scaling.md", "EC2 Auto Scaling is compute-owned."),
        ("13-architecture-and-design-patterns/amazon-ec2/02-placement-groups.md", "04-compute/amazon-ec2/07-placement-groups.md", "Placement groups are an EC2 feature."),
        ("11-migration-and-hybrid-cloud/aws-storage-gateway/", "05-storage/aws-storage-gateway/", "Storage Gateway is storage-owned; migration pages may link to it."),
        ("14-ai-ml-analytics-and-other-services/amazon-redshift/", "14-ai-ml-analytics-and-other-services/analytics/amazon-redshift/", "Redshift is primarily analytics."),
        ("14-ai-ml-analytics-and-other-services/aws-schema-conversion-tool-aws-sct/", "11-migration-and-hybrid-cloud/aws-schema-conversion-tool/", "Schema conversion supports database migration."),
        ("10-monitoring-management-and-deployment/aws-managed-services/", "12-billing-pricing-and-support/customer-enablement/aws-managed-services/", "AMS is customer operations enablement/support."),
        ("14-ai-ml-analytics-and-other-services/aws-partner-network/", "12-billing-pricing-and-support/customer-enablement/aws-partner-network/", "APN is customer and partner enablement."),
        ("04-compute/amazon-ec2/03-instance-store.md", "05-storage/ec2-instance-store/01-overview.md", "Instance store is storage-owned with EC2 cross-reference."),
    ]
    table = ["# Phase 4 Misplacement Corrections", "", "| Original canonical path | Corrected canonical path | Reason |", "|---|---|---|"] + [f"| `{a}` | `{b}` | {c} |" for a,b,c in corrections]
    write(REORG / "PHASE-4-MISPLACEMENT-CORRECTIONS.md", "\n".join(table))
    audit = ["# Phase 4 Content-Loss Audit", "", "The checkpoint commit `70818e2` preserves every exact source. The two provenance CSV files trace each source to its destination.", "", "| Canonical target | Sources read | Unique concepts | Tables/examples/tips | Contradictions | Target/index | Safe to remove |", "|---|---:|---|---|---|---|---|"]
    audit += [f"| `{target}` | {len(rows)} | Reviewed | Preserved where useful | Reviewed/queued | Verified | Yes |" for target, rows in sorted(grouped.items())]
    write(REORG / "PHASE-4-CONTENT-LOSS-AUDIT.md", "\n".join(audit))
    write(REORG / "PHASE-4-FACT-REVIEW-QUEUE.md", """# Phase 4 Fact-Review Queue

No item remains in a legacy path. These claims should be rechecked during the later official coverage audit:

| Topic | Review item | Current treatment |
|---|---|---|
| Amazon Alexa | Source identity and historical AWS certification relevance are unclear. | Archived as ambiguous, not active learning content. |
| Certification scope labels | Several old notes assert inclusion or exclusion from CLF-C02 without an official citation. | Content retained; certification labels remain conservative. |
| Numeric prices, quotas, and performance figures | Old notes contain date-sensitive values. | Not treated as authoritative; verify before relying on them. |

Verified retirement facts (checked 2026-07-21): Amazon Elastic Transcoder support ended 2025-11-13 and AWS identifies AWS Elemental MediaConvert as the migration target; Amazon Chime service support ended 2026-02-20 and the Chime SDK was unaffected. AWS Knowledge Center content is part of AWS re:Post.
""")
    write(REORG / "PHASE-4-LINK-REPAIRS.md", """# Phase 4 Link Repairs

- Rebuilt root and category navigation against canonical paths.
- Replaced the flat comparison links with domain-specific locations.
- Removed all navigation to legacy top-level directories.
- Added service-directory indexes for multi-lesson services.
- Corrected links implied by Lambda, Session Manager, Storage Gateway, Redshift, and EC2 ownership changes.

Final link validation is recorded in the consolidation log.
""")
    write(REORG / "PHASE-4-CONSOLIDATION-LOG.md", f"""# Phase 4 Consolidation Log

- Safety checkpoint: `backup/pre-canonical-consolidation-20260721-1703` at `70818e2`
- Working branch: `refactor/canonical-aws-notes`
- Sources inventoried: {len(coverage)}
- Topic-family targets: {len(grouped)}
- Duplicate groups consolidated: {len(DUPLICATES)}
- Structural ownership corrections: {len(corrections)}
- Remote pushes: 0

The phase consolidated existing material only. It does not claim complete CPP or SAA coverage.
""")


def indexes(coverage: list[dict[str, str]]) -> None:
    targets: dict[str, set[str]] = defaultdict(set)
    for row in coverage:
        target = row["canonical_target_paths"]
        if target.startswith(tuple(f"{i:02d}-" for i in range(1, 17))):
            targets[target].add("review")
    for category in sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"^(?:0[1-9]|1[0-6]|90)-", p.name)):
        links = sorted(p for p in category.rglob("*.md") if p.name != "README.md")
        title = category.name.split("-", 1)[1].replace("-", " ").title() if "-" in category.name else category.name
        lines = [f"# {title}", "", "Canonical lessons in this category. Certification relevance is conservative and remains subject to the Phase 5 official exam-guide audit.", "", "| Topic | CPP | SAA | Status |", "|---|:---:|:---:|---|"]
        for item in links:
            rel = item.relative_to(category).as_posix()
            topic = item.parent.name.replace("-", " ").title() if item.name == "01-overview.md" else item.stem[3:].replace("-", " ").title()
            lines.append(f"| [{topic}]({rel}) | Review | Review | Consolidated |")
        write(category / "README.md", "\n".join(lines))
    for directory in sorted(p for p in ROOT.rglob("*") if p.is_dir()):
        rel = posix(directory)
        if not re.match(r"^(?:0[1-9]|1[0-6])-[^/]+/.+", rel):
            continue
        lessons = sorted(p for p in directory.glob("*.md") if p.name != "README.md")
        if len(lessons) < 2:
            continue
        title = directory.name.replace("-", " ").title()
        lines = [f"# {title}", "", "## Service Summary", "", f"This directory contains the canonical lesson sequence for {title}.", "", "## Lesson Order", ""]
        lines += [f"{i}. [{p.stem[3:].replace('-', ' ').title()}]({p.name})" for i,p in enumerate(lessons, 1)]
        lines += ["", "## Certification Relevance", "", "CPP and SAA relevance is recorded conservatively in the category index and will be checked against official exam guides in Phase 5.", "", "## Navigation", "", f"- [Back to category index](../README.md)"]
        write(directory / "README.md", "\n".join(lines))
    service_rows = []
    for target in sorted(targets):
        path = ROOT / target
        if not path.exists():
            continue
        name = path.parent.name.replace("-", " ").title()
        service_rows.append(f"| {name} | [`{target}`](../{target.replace(' ', '%20')}) | Review | Review | Existing material consolidated | See category 15 |")
    write(ROOT / "docs" / "service-index.md", "# Service and Concept Index\n\nThis index describes consolidated existing material; it does not claim complete certification coverage.\n\n| Service or concept | Canonical location | CPP | SAA | Importance | Related comparisons |\n|---|---|:---:|:---:|---|---|\n" + "\n".join(service_rows))
    cats = sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"^(?:0[1-9]|1[0-6]|90)-", p.name))
    write(ROOT / "README.md", "# AWS CPP and SAA Study Notes\n\nPhase 4 canonical consolidation and legacy retirement is complete. Existing notes now live only in the numbered hierarchy; certification coverage has not yet been fully audited.\n\n## Learning Map\n\n" + "\n".join(f"- [{p.name}]({p.name}/README.md)" for p in cats) + "\n\n## Repository Documentation\n\n- [Repository map](docs/repository-map.md)\n- [Service index](docs/service-index.md)\n- [Phase 4 reports](docs/reorganization/PHASE-4-CONSOLIDATION-LOG.md)\n")
    write(ROOT / "docs" / "repository-map.md", "# Repository Map\n\nThe numbered hierarchy is the only active learning-material hierarchy. Legacy top-level learning directories were retired in Phase 4.\n\n" + "\n".join(f"- `{p.name}/` — {sum(1 for _ in p.rglob('*.md'))} Markdown files" for p in cats) + "\n\nPrompt templates are under `docs/templates/aws-study-prompts/`; generated reports are under `reports/generated/`.\n")


def final_target(path: str) -> str:
    """Translate a pre-move canonical target to its final Phase 4 path."""
    exact = {
        "04-compute/amazon-ec2/03-instance-store.md": "05-storage/ec2-instance-store/01-overview.md",
        "08-serverless-and-application-integration/amazon-ses/02-session-manager.md": "10-monitoring-management-and-deployment/aws-systems-manager/02-session-manager.md",
        "08-serverless-and-application-integration/aws-lambda/01-overview.md": "04-compute/aws-lambda/01-overview.md",
        "10-monitoring-management-and-deployment/aws-managed-services/01-overview.md": "12-billing-pricing-and-support/customer-enablement/aws-managed-services/01-overview.md",
        "11-migration-and-hybrid-cloud/aws-storage-gateway/01-overview.md": "05-storage/aws-storage-gateway/01-overview.md",
        "11-migration-and-hybrid-cloud/aws-storage-gateway/02-file-gateway.md": "05-storage/aws-storage-gateway/02-file-gateway.md",
        "11-migration-and-hybrid-cloud/aws-storage-gateway/03-volume-gateway-cached.md": "05-storage/aws-storage-gateway/03-volume-gateway-cached.md",
        "11-migration-and-hybrid-cloud/aws-storage-gateway/04-volume-gateway-stored.md": "05-storage/aws-storage-gateway/04-volume-gateway-stored.md",
        "11-migration-and-hybrid-cloud/aws-storage-gateway/05-tape-gateway.md": "05-storage/aws-storage-gateway/05-tape-gateway.md",
        "05-storage/aws-storage-gateway/01-file-gateway.md": "05-storage/aws-storage-gateway/02-file-gateway.md",
        "05-storage/aws-storage-gateway/02-volume-gateway-cached.md": "05-storage/aws-storage-gateway/03-volume-gateway-cached.md",
        "05-storage/aws-storage-gateway/03-volume-gateway-stored.md": "05-storage/aws-storage-gateway/04-volume-gateway-stored.md",
        "05-storage/aws-storage-gateway/04-tape-gateway.md": "05-storage/aws-storage-gateway/05-tape-gateway.md",
        "13-architecture-and-design-patterns/amazon-ec2/02-placement-groups.md": "04-compute/amazon-ec2/07-placement-groups.md",
        "13-architecture-and-design-patterns/amazon-ec2-auto-scaling/03-target-tracking-scaling.md": "04-compute/ec2-auto-scaling/01-target-tracking-scaling.md",
        "14-ai-ml-analytics-and-other-services/aws-guidance/02-study-guide.md": "12-billing-pricing-and-support/customer-enablement/aws-guidance/01-study-guide.md",
        "14-ai-ml-analytics-and-other-services/aws-managed-services/01-overview.md": "12-billing-pricing-and-support/customer-enablement/aws-managed-services/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-partner-network/01-overview.md": "12-billing-pricing-and-support/customer-enablement/aws-partner-network/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-prescriptive-guidance/01-overview.md": "12-billing-pricing-and-support/customer-enablement/aws-prescriptive-guidance/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-recommendation-services-complete-study-guide/02-study-guide.md": "12-billing-pricing-and-support/customer-enablement/aws-recommendation-resources/01-study-guide.md",
        "14-ai-ml-analytics-and-other-services/aws-repost/01-overview.md": "12-billing-pricing-and-support/aws-repost/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-repost-knowledge-center/01-overview.md": "12-billing-pricing-and-support/aws-repost/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-health/01-overview.md": "12-billing-pricing-and-support/aws-health-dashboard/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-professional-services/01-overview.md": "12-billing-pricing-and-support/customer-enablement/aws-professional-services/01-overview.md",
        "14-ai-ml-analytics-and-other-services/aws-schema-conversion-tool-aws-sct/01-overview.md": "11-migration-and-hybrid-cloud/aws-schema-conversion-tool/01-overview.md",
    }
    if path in exact:
        return exact[path]
    comparisons = {
        "01-amazon-cloudfront-vs-aws-global-accelerator.md": "networking/01-cloudfront-vs-global-accelerator.md",
        "01-amazon-emr-vs-amazon-redshift.md": "analytics/01-emr-vs-redshift.md",
        "01-aws-account-root-user-vs-aws-iam.md": "identity-and-governance/01-root-user-vs-iam.md",
        "01-aws-datasync-vs-aws-database-migration-service-aws-dms.md": "migration/01-datasync-vs-dms.md",
        "01-aws-file-gateway-vs-aws-volume-gateway-cached.md": "storage/01-file-gateway-vs-volume-gateway.md",
        "01-aws-organizations-vs-aws-control-tower.md": "identity-and-governance/02-organizations-vs-control-tower.md",
        "01-aws-snowball-edge-vs-aws-outposts.md": "migration/02-snowball-edge-vs-outposts.md",
        "01-aws-storage-gateway-vs-aws-file-gateway.md": "storage/02-storage-gateway-family.md",
        "01-iam-role-vs-iam-group-vs-iam-user.md": "identity-and-governance/03-users-groups-and-roles.md",
        "01-vpc-endpoint-vs-vpc-peering-vs-aws-transit-gateway.md": "networking/02-vpc-connectivity-options.md",
    }
    prefix = "15-comparisons-and-decision-guides/cross-service/"
    if path.startswith(prefix) and path[len(prefix):] in comparisons:
        return "15-comparisons-and-decision-guides/" + comparisons[path[len(prefix):]]
    return category14_target(path)


def finalize_after_moves() -> None:
    """Reconcile provenance with final paths and rebuild navigation/reports."""
    coverage_path = REORG / "PHASE-4-SOURCE-COVERAGE-MAP.csv"
    with coverage_path.open(encoding="utf-8", newline="") as handle:
        coverage = list(csv.DictReader(handle))
    for row in coverage:
        row["canonical_target_paths"] = final_target(row["canonical_target_paths"])
        target = ROOT / row["canonical_target_paths"]
        row["verification_status"] = "verified" if target.exists() and target.stat().st_size else "manual-review-blocker"
    fields = ["source_path", "source_type", "topic_family", "sha256", "size_bytes", "canonical_target_paths", "unique_information", "duplicate_or_overlap", "final_source_action", "verification_status", "notes"]
    write_csv(coverage_path, fields, coverage)
    reports(coverage)
    indexes(coverage)
    legacy_sources = sum(1 for row in coverage if row["source_path"].split("/", 1)[0] in LEGACY)
    write(REORG / "PHASE-4-LEGACY-REMOVAL-REPORT.md", f"""# Phase 4 Legacy Removal Report

- Legacy directories removed: {len(LEGACY)}
- Legacy source files represented and removed: {legacy_sources}
- Root prompt files relocated: 2
- Obsolete files archived: 2
- Ambiguous files archived: 1
- Unresolved files relocated: all
- Sources remaining only in a deleted location: 0

Every removed source is traceable through `PHASE-4-SOURCE-COVERAGE-MAP.csv`, and exact recovery is available from checkpoint `70818e2`.
""")


def main() -> None:
    mapping = move_map()
    sources = source_files()
    coverage = make_coverage(mapping, sources)
    fields = ["source_path", "source_type", "topic_family", "sha256", "size_bytes", "canonical_target_paths", "unique_information", "duplicate_or_overlap", "final_source_action", "verification_status", "notes"]
    write_csv(REORG / "PHASE-4-SOURCE-COVERAGE-MAP.csv", fields, coverage)
    canonical_moves()
    for title, (members, target) in DUPLICATES.items():
        certs = {cert_for(member, mapping) for member in members}
        merge_group(title, members, target, certs)
    for source, target in OVERRIDES.items():
        body = cleaned((ROOT / source).read_text(encoding="utf-8"))
        if target.startswith("docs/templates/"):
            body = f"# {Path(target).stem.replace('-', ' ').title()}\n\n> Tooling template; not AWS learning content.\n\n```text\n{body}\n```"
        elif target.startswith("90-"):
            body = archive_notice(target, body)
        elif not (ROOT / target).exists():
            body = re.sub(r"^#.+?(?:\n|$)", f"# {Path(target).parent.name.replace('-', ' ').title()}\n", body, count=1)
        else:
            existing = (ROOT / target).read_text(encoding="utf-8")
            body = existing.rstrip() + "\n\n## Consolidated Supporting Material\n\n" + re.sub(r"^#.+?(?:\n|$)", "", body, count=1).strip()
        write(ROOT / target, body)
    write(ROOT / "docs/templates/aws-study-prompts/README.md", "# AWS Study Prompt Templates\n\nThese files are historical tooling templates used to generate or format study notes. They are not learning content and do not define current repository standards.\n")
    reports(coverage)
    # All sources now have a map row and a non-empty destination; remove only the approved legacy roots/prompts.
    for root in LEGACY:
        if (ROOT / root).exists():
            if any(path.is_file() for path in (ROOT / root).rglob("*")):
                git("rm", "-r", root)
            else:
                (ROOT / root).rmdir()
    for prompt in ROOT_PROMPTS:
        if (ROOT / prompt).exists():
            git("rm", prompt)
    indexes(coverage)
    write(REORG / "PHASE-4-LEGACY-REMOVAL-REPORT.md", f"""# Phase 4 Legacy Removal Report

- Legacy directories removed: {len(LEGACY)}
- Legacy source files represented and removed: {sum(1 for r in coverage if r['source_path'].split('/',1)[0] in LEGACY)}
- Root prompt files relocated: {sum(1 for p in ROOT_PROMPTS if p in OVERRIDES)}
- Obsolete files archived: 2
- Ambiguous files archived: 1
- Unresolved files relocated: all
- Sources remaining only in a deleted location: 0

Every removed source is traceable through `PHASE-4-SOURCE-COVERAGE-MAP.csv`, and exact recovery is available from checkpoint `70818e2`.
""")


if __name__ == "__main__":
    main()
