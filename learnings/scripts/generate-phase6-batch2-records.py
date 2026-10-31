#!/usr/bin/env python3
"""Generate Phase 6 Batch 2 control records from the Phase 5 authority backlog."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKLOG = ROOT / "docs/certification-audit/PHASE-6-CONTENT-BACKLOG.csv"
OUT = ROOT / "docs/content-implementation"
BATCH = "Batch 2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else ""


def read_rows() -> list[dict[str, str]]:
    with BACKLOG.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
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
        item = {field: row.get(field, "") for field in fields}
        if row["batch"] == BATCH:
            item["selected"] = "true"
            item["selection_reason"] = "Explicit Batch 2 assignment in the Phase 5 authority backlog."
            item["status"] = "selected"
        elif row["batch"] == "Batch 1":
            item["selected"] = "false"
            item["selection_reason"] = "Completed in Phase 6 Batch 1; retained as satisfied dependency history."
            item["status"] = "already-completed"
        else:
            item["selected"] = "false"
            item["selection_reason"] = f"Explicitly assigned to {row['batch']}; outside Batch 2."
            item["status"] = "deferred-to-later-batch"
        output.append(item)
    write_csv(OUT / "PHASE-6-BATCH-2-SCOPE.csv", fields, output)


def build_pre(rows: list[dict[str, str]]) -> None:
    fields = [
        "backlog_id", "topic", "target_path", "current_paths", "recommended_action",
        "exists_before", "sha256_before", "planned_sections", "official_sources",
        "dependencies", "risk_level", "implementation_status", "notes",
    ]
    sections = {
        "AWS-007": "families; sizing; lifecycle; storage/network; HA; security; cost; selection; scenarios; knowledge check; references",
        "AWS-008": "ALB/NLB/GWLB; listeners; target groups; health; cross-zone; TLS; HA; cost; scenarios; references",
        "AWS-009": "ASG capacity; launch templates; target tracking; step/scheduled; health; warmup; Multi-AZ; trade-offs; references",
        "AWS-010": "invocation; scaling/concurrency; integrations; security; failure/retries; cost; scenarios; references",
        "AWS-011": "ECS/EKS/Fargate/ECR; EC2 capacity; selection; scaling; operations; cost; scenarios; references",
        "AWS-012": "object design; durability/availability; security; versioning; replication; events; performance; cost; references",
        "AWS-013": "volume types; IOPS/throughput; snapshots; encryption; AZ scope; cost; scenarios; references",
        "AWS-014": "ephemeral behavior; performance; failure; suitable data; EBS comparison; references",
        "AWS-015": "Regional/One Zone; mount targets; NFS; performance/throughput; lifecycle; security; cost; references",
        "AWS-016": "FSx families; protocols; performance; HA; integrations; selection table; references",
        "AWS-017": "S3 File/Volume/Tape Gateway; cache; recovery; connectivity; selection; cost; references",
        "AWS-018": "plans; rules; vaults; assignments; cross-account/Region; Vault Lock; restore testing; cost; references",
        "AWS-019": "EC2/Lambda/containers and S3/EBS/EFS/instance-store decision tables; scenarios; references",
    }
    sources = {
        "AWS-007": "Amazon EC2 User Guide; EC2 security guidance; exam guides",
        "AWS-008": "Elastic Load Balancing documentation and load-balancer guides",
        "AWS-009": "EC2 Auto Scaling launch template and scaling-policy documentation",
        "AWS-010": "AWS Lambda Developer Guide",
        "AWS-011": "AWS container service decision guide; ECS, EKS, Fargate, and ECR documentation",
        "AWS-012": "Amazon S3 User Guide and security/replication documentation",
        "AWS-013": "Amazon EBS User Guide",
        "AWS-014": "Amazon EC2 instance store documentation",
        "AWS-015": "Amazon EFS User Guide",
        "AWS-016": "Amazon FSx documentation and family user guides",
        "AWS-017": "AWS Storage Gateway User Guide",
        "AWS-018": "AWS Backup Developer Guide",
        "AWS-019": "Official EC2, Lambda, container, S3, EBS, EFS, and instance-store documentation",
    }
    output = []
    for row in rows:
        if row["batch"] != BATCH:
            continue
        target = ROOT / row["target_path"]
        exists = target.is_file()
        output.append({
            "backlog_id": row["backlog_id"], "topic": row["topic"],
            "target_path": row["target_path"], "current_paths": row["current_paths"],
            "recommended_action": row["recommended_action"],
            "exists_before": str(exists).lower(), "sha256_before": sha256(target),
            "planned_sections": sections[row["backlog_id"]],
            "official_sources": sources[row["backlog_id"]],
            "dependencies": row["dependencies"],
            "risk_level": "high" if row["estimated_effort"] == "L" else "medium",
            "implementation_status": "planned",
            "notes": "Checksum captured before modification." if exists else "Target did not exist at preflight.",
        })
    write_csv(OUT / "PHASE-6-BATCH-2-PRE-IMPLEMENTATION.csv", fields, output)


def main() -> None:
    rows = read_rows()
    if len(rows) != 54 or len({row["backlog_id"] for row in rows}) != 54:
        raise SystemExit("Unexpected Phase 5 backlog shape.")
    if sum(row["batch"] == BATCH for row in rows) != 13:
        raise SystemExit("Expected exactly 13 Batch 2 rows.")
    build_scope(rows)
    build_pre(rows)


if __name__ == "__main__":
    main()
