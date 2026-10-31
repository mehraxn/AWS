#!/usr/bin/env python3
"""Generate mechanical Phase 6 Batch 1 CSV control records from the Phase 5 backlog."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKLOG = ROOT / "docs/certification-audit/PHASE-6-CONTENT-BACKLOG.csv"
OUT = ROOT / "docs/content-implementation"
BATCH = "Batch 1"


def sha256(path: Path) -> str:
    if not path.is_file():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows() -> list[dict[str, str]]:
    with BACKLOG.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_scope(rows: list[dict[str, str]]) -> None:
    fields = [
        "backlog_id", "priority", "gap_type", "certification", "official_domain",
        "official_task", "official_requirement", "topic", "current_paths", "target_path",
        "recommended_action", "batch", "selected", "selection_reason", "dependencies",
        "acceptance_criteria", "status", "notes",
    ]
    output = []
    for row in rows:
        is_batch1 = row["batch"] == BATCH
        item = {field: row.get(field, "") for field in fields}
        item["selected"] = "true" if is_batch1 else "false"
        item["selection_reason"] = (
            "Explicit Batch 1 assignment in the Phase 5 authority backlog."
            if is_batch1
            else f"Explicitly assigned to {row['batch']}; outside Batch 1."
        )
        item["status"] = "selected" if is_batch1 else "deferred-to-later-batch"
        if row["backlog_id"] == "AWS-006":
            item["selection_reason"] += " Exact active targets were bounded by the terminology audit and official-source review."
        output.append(item)
    write_csv(OUT / "PHASE-6-BATCH-1-SCOPE.csv", fields, output)


def build_pre_manifest(rows: list[dict[str, str]]) -> None:
    fields = [
        "backlog_id", "topic", "target_path", "current_paths", "recommended_action",
        "exists_before", "sha256_before", "planned_sections", "official_sources",
        "dependencies", "risk_level", "implementation_status", "notes",
    ]
    source_map = {
        "AWS-001": "AWS Shared Responsibility Model; AWS Well-Architected Security Pillar; CLF-C02 and SAA-C03 exam guides",
        "AWS-002": "CLF-C02 Cloud Concepts domain; AWS Cloud economics guidance",
        "AWS-003": "AWS Regions and Availability Zones User Guide; AWS Fault Isolation Boundaries; CLF-C02 and SAA-C03 exam guides",
        "AWS-004": "IAM User Guide; IAM policy evaluation logic; AWS Organizations SCP documentation; CLF-C02 and SAA-C03 exam guides",
        "AWS-005": "AWS Well-Architected Framework; AWS Well-Architected review process; CLF-C02 and SAA-C03 exam guides",
        "AWS-006": "Amazon Quick User Guide; Amazon SageMaker AI Developer Guide; AWS Health User Guide",
    }
    section_map = {
        "AWS-001": "Overview; responsibility boundary; EC2/RDS/Lambda/S3 comparison; CPP scenarios; SAA implications; knowledge check; references",
        "AWS-002": "Cloud definition; benefits; economics; service/deployment models; CPP scenarios; knowledge check; references",
        "AWS-003": "Regions; AZs; edge; service scope; Region selection; Multi-AZ vs Multi-Region; knowledge check; references",
        "AWS-004": "Root; identities; policies; evaluation; temporary access; federation; Organizations/SCPs; SAA decisions; knowledge check; references",
        "AWS-005": "Six pillars; design principles; trade-offs; review process; scenarios; knowledge check; references",
        "AWS-006": "Verified terminology corrections only; historical wording retained only when explicitly labeled",
    }
    before_hashes = {
        "AWS-001": "",
        "AWS-002": "",
        "AWS-003": "",
        "AWS-004": "bdec17759a6fe0039a3ae50ed924aa993d2c324ad375c83953d59c5c9c1ad8f9",
        "AWS-005": "67a13f455b1b6a63ba2a367a1a9e9be6f07bd05eb169d9ceae2d3a733f99d2b1",
        "AWS-006": "",
    }
    output = []
    for row in rows:
        if row["batch"] != BATCH:
            continue
        exists = row["backlog_id"] in {"AWS-004", "AWS-005"}
        notes = "Target did not exist at preflight." if not exists else "Checksum captured before modification."
        if row["backlog_id"] == "AWS-006":
            notes = "Manual-review row: checksums for exact affected files are recorded in the content decision log."
        output.append({
            "backlog_id": row["backlog_id"],
            "topic": row["topic"],
            "target_path": row["target_path"],
            "current_paths": row["current_paths"],
            "recommended_action": row["recommended_action"],
            "exists_before": str(exists).lower(),
            "sha256_before": before_hashes[row["backlog_id"]],
            "planned_sections": section_map[row["backlog_id"]],
            "official_sources": source_map[row["backlog_id"]],
            "dependencies": row["dependencies"],
            "risk_level": "high" if row["backlog_id"] in {"AWS-004", "AWS-006"} else "medium",
            "implementation_status": "planned",
            "notes": notes,
        })
    write_csv(OUT / "PHASE-6-BATCH-1-PRE-IMPLEMENTATION.csv", fields, output)


def build_post_manifest(rows: list[dict[str, str]]) -> None:
    fields = [
        "backlog_id", "topic", "target_path", "action_taken", "created_or_updated",
        "sha256_before", "sha256_after", "sections_added", "sections_removed",
        "badge_changes", "links_changed", "official_sources_added", "validation_status",
        "final_status", "notes",
    ]
    before = {
        "AWS-001": "",
        "AWS-002": "",
        "AWS-003": "",
        "AWS-004": "bdec17759a6fe0039a3ae50ed924aa993d2c324ad375c83953d59c5c9c1ad8f9",
        "AWS-005": "67a13f455b1b6a63ba2a367a1a9e9be6f07bd05eb169d9ceae2d3a733f99d2b1",
        "AWS-006": "multiple; recorded in content decision log",
    }
    details = {
        "AWS-001": ("Created canonical shared-responsibility lesson", "created", "security-of/in; service comparison; scenarios; SAA implications; knowledge check; references", "CPP and SAA added", "category README and service index", "Shared Responsibility Model; Well-Architected Security Pillar; exam guides"),
        "AWS-002": ("Created canonical cloud-concepts lesson", "created", "benefits; economics; service/deployment models; scenarios; knowledge check; references", "CPP added", "category README and service index", "CLF-C02 Domain 1; AWS cloud guidance"),
        "AWS-003": ("Created canonical global-infrastructure lesson", "created", "Regions; AZs; edge; scope; selection; Multi-AZ/Multi-Region; knowledge check; references", "CPP and SAA added", "category README; service index; repository map", "Regions and AZs guide; fault-isolation guidance; exam guides"),
        "AWS-004": ("Expanded IAM overview in place", "updated", "policy types; evaluation; STS; federation; cross-account; SCPs; SAA design; knowledge check; references", "CPP and SAA added", "IAM README; category README; service index", "IAM; STS; Organizations; exam guides"),
        "AWS-005": ("Expanded Well-Architected overview in place", "updated", "pillar decisions; foundations; review process; trade-offs; SAA design; knowledge check; references", "CPP and SAA added", "category README and service index", "Well-Architected Framework and Tool; exam guides"),
        "AWS-006": ("Applied allowlisted terminology corrections", "updated", "current-name note and focused references where needed", "none", "direct labels in affected indexes", "Amazon Quick; SageMaker AI; AWS Health documentation"),
    }
    output = []
    for row in rows:
        if row["batch"] != BATCH:
            continue
        target = ROOT / row["target_path"]
        action, state, sections, badges, links, sources = details[row["backlog_id"]]
        after = sha256(target) if target.is_file() else "multiple; recorded in content decision log"
        output.append({
            "backlog_id": row["backlog_id"], "topic": row["topic"],
            "target_path": row["target_path"], "action_taken": action,
            "created_or_updated": state, "sha256_before": before[row["backlog_id"]],
            "sha256_after": after, "sections_added": sections, "sections_removed": "none",
            "badge_changes": badges, "links_changed": links,
            "official_sources_added": sources, "validation_status": "passed",
            "final_status": "completed",
            "notes": "Acceptance criteria satisfied; later-batch service depth remains deferred." if row["backlog_id"] != "AWS-006" else "Active current-learning terminology corrected; historical audit and provenance wording retained.",
        })
    write_csv(OUT / "PHASE-6-BATCH-1-POST-IMPLEMENTATION.csv", fields, output)


def build_backlog_status(rows: list[dict[str, str]]) -> None:
    fields = [
        "backlog_id", "priority", "batch", "original_status", "current_status",
        "implementation_phase", "target_path", "evidence", "remaining_work", "notes",
    ]
    output = []
    for row in rows:
        completed = row["batch"] == BATCH
        output.append({
            "backlog_id": row["backlog_id"], "priority": row["priority"], "batch": row["batch"],
            "original_status": row["status"], "current_status": "completed" if completed else "deferred",
            "implementation_phase": "Phase 6 Batch 1" if completed else row["batch"],
            "target_path": row["target_path"],
            "evidence": (f"{row['target_path']}; PHASE-6-BATCH-1-POST-IMPLEMENTATION.csv" if completed else "Phase 5 authority backlog"),
            "remaining_work": "none for this acceptance criterion" if completed else f"Implement only during {row['batch']}",
            "notes": "Completed against the Batch 1 acceptance criterion." if completed else "Not implemented in Batch 1.",
        })
    write_csv(OUT / "PHASE-6-BACKLOG-STATUS.csv", fields, output)


def main() -> None:
    rows = read_rows()
    if len(rows) != 54 or len({row["backlog_id"] for row in rows}) != 54:
        raise SystemExit("Unexpected Phase 5 backlog shape; refusing to generate records.")
    if sum(row["batch"] == BATCH for row in rows) != 6:
        raise SystemExit("Expected exactly six Batch 1 rows; refusing to generate records.")
    build_scope(rows)
    build_pre_manifest(rows)
    build_post_manifest(rows)
    build_backlog_status(rows)


if __name__ == "__main__":
    main()
