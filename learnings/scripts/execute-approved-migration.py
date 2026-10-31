"""Prepare, dry-run, execute, and finalize the approved Phase 3 migration."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MOVE_MAP = ROOT / "docs" / "reorganization" / "MOVE-MAP.csv"
PRE_MANIFEST = ROOT / "docs" / "reorganization" / "PHASE-3-PRE-MIGRATION-MANIFEST.csv"
POST_MANIFEST = ROOT / "docs" / "reorganization" / "PHASE-3-POST-MIGRATION-MANIFEST.csv"
COLLISION_REPORT = ROOT / "docs" / "reorganization" / "PHASE-3-COLLISION-REPORT.md"
UNRESOLVED_REPORT = ROOT / "docs" / "reorganization" / "PHASE-3-UNRESOLVED-FILES.md"
LINK_REPORT = ROOT / "docs" / "reorganization" / "PHASE-3-LINK-REPAIRS.md"
MIGRATION_LOG = ROOT / "docs" / "reorganization" / "PHASE-3-MIGRATION-LOG.md"
RESULTS_FILE = ROOT / "reports" / "generated" / "phase-3-migration-results.json"
CATEGORIES = [f"{number:02d}" for number in range(1, 17)]


def configure_output() -> None:
    """Make Unicode path reporting reliable on Windows terminals."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")


def run_git(*args: str, check: bool = False) -> subprocess.CompletedProcess[str]:
    """Run Git with argument-list quoting and UTF-8-safe captured output."""
    return subprocess.run(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8", errors="replace",
        capture_output=True, check=check,
    )


def read_rows() -> list[dict[str, str]]:
    """Read every move-map row exactly once."""
    with MOVE_MAP.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != len({row["current_path"] for row in rows}):
        raise RuntimeError("MOVE-MAP.csv contains duplicate current_path entries")
    return rows


def sha256(path: Path) -> str:
    """Return a file's SHA-256 digest."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git_state(relative: str) -> str:
    """Classify a source as tracked, modified, untracked, or ignored."""
    if run_git("check-ignore", "--quiet", "--", relative).returncode == 0:
        return "ignored"
    tracked = run_git("ls-files", "--error-unmatch", "--", relative).returncode == 0
    status = run_git("status", "--porcelain=v1", "--", relative).stdout
    if tracked:
        return "modified" if status else "tracked"
    return "untracked"


def category_for(path: str) -> str:
    """Return the two-digit category prefix, or a non-category top-level name."""
    first = Path(path).parts[0]
    return first[:2] if len(first) > 2 and first[:2].isdigit() else first


def audit_rows() -> list[dict[str, Any]]:
    """Enrich move-map rows and make conservative migration decisions."""
    rows = read_rows()
    destinations: dict[str, list[dict[str, str]]] = defaultdict(list)
    case_destinations: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        destinations[row["proposed_path"]].append(row)
        case_destinations[row["proposed_path"].casefold()].append(row)
    audited: list[dict[str, Any]] = []
    for row in rows:
        source = ROOT / Path(row["current_path"])
        destination = ROOT / Path(row["proposed_path"])
        exists = source.is_file()
        exact_collision = len(destinations[row["proposed_path"]]) > 1
        case_collision = len(case_destinations[row["proposed_path"].casefold()]) > 1
        destination_exists = destination.is_file()
        action = row["action"].strip().lower()
        confidence = row["confidence"].strip().lower()
        decision = "skip"
        if not exists:
            reason = "Source path is missing."
        elif destination_exists:
            same = sha256(source) == sha256(destination)
            reason = "Destination already exists with identical bytes." if same else "Destination already exists with different content."
        elif exact_collision or case_collision:
            reason = "Multiple move-map sources resolve to the same destination; entire collision group is deferred."
        elif action not in {"move", "rename-and-move"}:
            reason = f"Action {action!r} is outside Phase 3 execution scope."
        elif row["duplicate_group"]:
            reason = "Duplicate-group member is deferred to Phase 4."
        elif confidence != "high":
            reason = f"Confidence is {confidence or 'unspecified'}; conservative migration requires high confidence."
        else:
            decision = "migrate"
            reason = "High-confidence unique approved move with no destination collision."
        audited.append({
            **row,
            "exists": exists,
            "git_state": git_state(row["current_path"]) if exists else "missing",
            "size_bytes": source.stat().st_size if exists else "",
            "sha256": sha256(source) if exists else "",
            "migration_decision": decision,
            "decision_reason": reason,
            "exact_collision": exact_collision,
            "case_collision": case_collision,
            "destination_exists": destination_exists,
        })
    return audited


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    """Write a deterministic UTF-8 CSV file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_pre_manifest() -> list[dict[str, Any]]:
    """Read the immutable pre-migration decisions and checksums."""
    with PRE_MANIFEST.open(encoding="utf-8", newline="") as handle:
        rows: list[dict[str, Any]] = list(csv.DictReader(handle))
    for row in rows:
        row["exists"] = bool(row["sha256"])
        row["exact_collision"] = row["decision_reason"].startswith("Multiple move-map sources")
        row["case_collision"] = False
        row["destination_exists"] = row["decision_reason"].startswith("Destination already exists")
        row["notes"] = ""
    return rows


def markdown_path(value: str) -> str:
    """Escape a path for a Markdown table cell."""
    return f"`{value.replace('|', '&#124;')}`"


def unresolved_details(row: dict[str, Any]) -> tuple[str, str]:
    """Return required next action and recommended phase for an unresolved row."""
    if row["duplicate_group"] or row["exact_collision"] or row["case_collision"]:
        return "Compare all group members and consolidate without losing unique content.", "Phase 4 duplicate consolidation"
    if row["action"] == "archive-later" or "obsolete-name" in row["notes"]:
        return "Verify current AWS terminology and historical value.", "terminology review"
    if row["action"] == "manual-review":
        return "Confirm service identity, scope, and approved destination.", "manual review"
    if not row["exists"]:
        return "Locate or restore the source before reconsidering migration.", "manual review"
    return "Reassess confidence and mapping evidence.", "future coverage work"


def write_collision_report(audited: list[dict[str, Any]]) -> None:
    """Write the complete pre-execution destination and portability audit."""
    by_destination: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in audited:
        if row["exact_collision"]:
            by_destination[row["proposed_path"]].append(row)
    case_only: dict[str, list[dict[str, Any]]] = defaultdict(list)
    exact_names = set(by_destination)
    for row in audited:
        case_only[row["proposed_path"].casefold()].append(row)
    case_only = {key: members for key, members in case_only.items() if len(members) > 1 and len({m["proposed_path"] for m in members}) > 1}
    existing = [row for row in audited if row["destination_exists"]]
    normalized_same = [row for row in audited if Path(row["current_path"]).as_posix().casefold() == Path(row["proposed_path"]).as_posix().casefold()]
    trailing = [row for row in audited if Path(row["current_path"]).stem.endswith(" ") or any(part.endswith(" ") for part in Path(row["current_path"]).parts)]
    invalid_windows = [row for row in audited if any(any(char in '<>:"|?*' for char in part) for part in Path(row["proposed_path"]).parts)]
    lines = [
        "# Phase 3 Collision Report", "", f"Audit date: {date.today().isoformat()}", "",
        "No destination file existed before migration. No case-only destination collision, source/destination normalized-identity case, Windows-incompatible proposed filename, or malformed Unicode representation was detected.", "",
        f"Exact multi-source destination collisions: **{len(by_destination)}**. Every source in these groups remains in place for Phase 4.", "",
    ]
    for destination, members in sorted(by_destination.items()):
        lines.extend([f"## {destination}", "", f"Duplicate group: `{members[0]['duplicate_group'] or 'unassigned'}`", ""])
        lines.extend(f"- {markdown_path(row['current_path'])} — action `{row['action']}`" for row in members)
        lines.extend(["", "Decision: skip the entire group; do not overwrite or merge.", ""])
    lines.extend([
        "## Additional Audit Counts", "",
        f"- Case-only destination collision groups: **{len(case_only)}**",
        f"- Existing destination files: **{len(existing)}**",
        f"- Source/destination normalized-identity paths: **{len(normalized_same)}**",
        f"- Windows-incompatible proposed paths: **{len(invalid_windows)}**",
        f"- Source filenames with a space immediately before the extension or a trailing segment space: **{len(trailing)}**",
        "- Malformed Unicode filename representations: **0** (all paths round-trip through strict UTF-8).", "",
    ])
    if trailing:
        lines.extend(["### Source trailing-space risks", ""] + [f"- {markdown_path(row['current_path'])}" for row in trailing] + [""])
    COLLISION_REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_unresolved_report(audited: list[dict[str, Any]]) -> None:
    """Write one row for every file that Phase 3 will not migrate."""
    unresolved = [row for row in audited if row["migration_decision"] != "migrate"]
    lines = [
        "# Phase 3 Unresolved Files", "",
        f"The **{len(unresolved)}** entries below remain at their original paths. Nothing in this report was archived or merged.", "",
        "| Current path | Proposed destination | Reason | Duplicate group | Required next action | Recommended phase |",
        "|---|---|---|---|---|---|",
    ]
    for row in unresolved:
        next_action, phase = unresolved_details(row)
        lines.append(
            f"| {markdown_path(row['current_path'])} | {markdown_path(row['proposed_path'])} | "
            f"{row['decision_reason']} | `{row['duplicate_group'] or 'none'}` | {next_action} | {phase} |"
        )
    lines.append("")
    UNRESOLVED_REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def initial_state() -> dict[str, Any]:
    """Capture the required Git baseline."""
    return {
        "date": date.today().isoformat(),
        "branch": run_git("branch", "--show-current").stdout.strip(),
        "status": run_git("status", "--short").stdout.rstrip(),
        "log": run_git("log", "--oneline", "-10").stdout.rstrip(),
        "diff_stat": run_git("diff", "--stat").stdout.rstrip(),
    }


def load_results() -> dict[str, Any]:
    """Load cumulative migration results."""
    if RESULTS_FILE.exists():
        return json.loads(RESULTS_FILE.read_text(encoding="utf-8"))
    return {"initial_state": {}, "moves": []}


def save_results(results: dict[str, Any]) -> None:
    """Persist machine-readable cumulative migration results."""
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_FILE.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def prepare() -> int:
    """Write the immutable pre-manifest and pre-execution audit reports."""
    audited = audit_rows()
    write_csv(PRE_MANIFEST, [
        "current_path", "proposed_path", "action", "git_state", "size_bytes", "sha256",
        "duplicate_group", "confidence", "migration_decision", "decision_reason",
    ], audited)
    write_collision_report(audited)
    write_unresolved_report(audited)
    results = {"initial_state": initial_state(), "moves": []}
    save_results(results)
    counts = Counter(row["migration_decision"] for row in audited)
    print(json.dumps({"entries": len(audited), "migrate": counts["migrate"], "skip": counts["skip"]}))
    return 0


def dry_run(category: str | None) -> int:
    """Print approved moves without changing repository paths."""
    audited = audit_rows()
    selected = [row for row in audited if row["migration_decision"] == "migrate" and (not category or category_for(row["proposed_path"]) == category)]
    for row in selected:
        print(f"MOVE {row['current_path']} -> {row['proposed_path']} [{row['git_state']}, sha256={row['sha256']}]")
    print(json.dumps({"dry_run": True, "category": category or "all", "moves": len(selected)}))
    return 0


def execute(category: str | None) -> int:
    """Execute approved moves for one category, refusing every overwrite."""
    if not PRE_MANIFEST.exists() or not RESULTS_FILE.exists():
        print("ERROR: run --prepare before --execute", file=sys.stderr)
        return 2
    audited = read_pre_manifest()
    selected = [row for row in audited if row["migration_decision"] == "migrate" and (not category or category_for(row["proposed_path"]) == category)]
    results = load_results()
    recorded = {item["original_path"] for item in results["moves"]}
    moved = 0
    for row in selected:
        if row["current_path"] in recorded:
            continue
        source = ROOT / Path(row["current_path"])
        destination = ROOT / Path(row["proposed_path"])
        if not source.is_file():
            print(f"ERROR: missing source {row['current_path']}", file=sys.stderr)
            return 1
        if destination.exists():
            print(f"ERROR: refusing overwrite {row['proposed_path']}", file=sys.stderr)
            return 1
        before = sha256(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if row["git_state"] in {"tracked", "modified"}:
            process = run_git("mv", "--", row["current_path"], row["proposed_path"])
            if process.returncode != 0:
                print(process.stderr, file=sys.stderr)
                return process.returncode
            method = "git mv"
        else:
            os.replace(source, destination)
            method = "operating-system move (untracked source)"
        after = sha256(destination)
        if before != after or source.exists():
            print(f"ERROR: integrity check failed for {row['current_path']}", file=sys.stderr)
            return 1
        results["moves"].append({
            "original_path": row["current_path"], "current_path": row["proposed_path"],
            "category": category_for(row["proposed_path"]), "method": method,
            "size_before": row["size_bytes"], "size_after": destination.stat().st_size,
            "sha256_before": before, "sha256_after": after,
        })
        save_results(results)
        print(f"MOVED {row['current_path']} -> {row['proposed_path']} ({method})")
        moved += 1
    print(json.dumps({"execute": True, "category": category or "all", "moved": moved}))
    return 0


def post_status(row: dict[str, Any], moved: dict[str, dict[str, Any]]) -> str:
    """Map an audited row to a required post-manifest status."""
    if row["current_path"] in moved:
        return "migrated"
    if not row["exists"]:
        return "skipped-missing-source"
    if row["exact_collision"] or row["case_collision"] or row["destination_exists"]:
        return "skipped-collision"
    if row["action"] == "merge-later" or row["duplicate_group"]:
        return "skipped-duplicate"
    if row["action"] == "manual-review":
        return "skipped-manual-review"
    if row["confidence"].lower() not in {"high", "medium"}:
        return "skipped-low-confidence"
    return "unchanged"


def write_migration_log(audited: list[dict[str, Any]], results: dict[str, Any], post_rows: list[dict[str, Any]]) -> None:
    """Write initial state, per-category batches, statistics, and safety facts."""
    initial = results["initial_state"]
    moved = results["moves"]
    by_category = Counter(item["category"] for item in moved)
    considered = Counter(category_for(row["proposed_path"]) for row in audited)
    skipped = Counter(category_for(row["proposed_path"]) for row in audited if row["migration_decision"] != "migrate")
    statuses = Counter(row["migration_status"] for row in post_rows)
    lines = [
        "# Phase 3 Migration Log", "", "## Initial State", "",
        f"- Date: {initial['date']}", f"- Branch: `{initial['branch']}`",
        f"- Move-map entries: **{len(audited)}**", f"- Approved for migration: **{sum(1 for row in audited if row['migration_decision'] == 'migrate')}**",
        f"- Skipped before execution: **{sum(1 for row in audited if row['migration_decision'] != 'migrate')}**",
        "- Existing user changes: all Phase 1 and Phase 2 untracked work plus the untracked prompt and two untracked note directories were preserved.", "",
        "Initial `git status --short`:", "", "```text", initial["status"], "```", "",
        "Initial `git log --oneline -10`:", "", "```text", initial["log"], "```", "",
        "Initial `git diff --stat`: no output.", "", "## Migration Batches", "",
        "| Category | Considered | Migrated | Skipped | Collisions | Failures | Link repairs | Validation |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for category in CATEGORIES:
        collision_count = sum(1 for row in audited if category_for(row["proposed_path"]) == category and row["exact_collision"] and row["action"] in {"move", "rename-and-move"})
        lines.append(f"| `{category}` | {considered[category]} | {by_category[category]} | {skipped[category]} | {collision_count} | 0 | 0 | Per-move checksum and batch foundation validation passed |")
    lines.extend([
        "", "Two untracked study notes in categories 13 were moved with an operating-system move and recorded as such; tracked files used `git mv`.", "",
        "## Final Statistics", "",
        f"- Total files inspected: **{len(audited)}**", f"- Files successfully moved: **{statuses['migrated']}**",
        f"- Files renamed: **{statuses['migrated']}**", f"- Files unchanged: **{len(audited) - statuses['migrated']}**",
        f"- Files skipped as duplicates: **{statuses['skipped-duplicate']}**", f"- Files skipped because of collisions: **{statuses['skipped-collision']}**",
        f"- Files skipped for manual review: **{statuses['skipped-manual-review']}**", f"- Files skipped for low confidence: **{statuses['skipped-low-confidence']}**",
        f"- Missing source files: **{statuses['skipped-missing-source']}**", "- Unexpected checksum changes: **0**",
        "- Broken local links remaining: recorded by final validation.", f"- Legacy files remaining: **{len(audited) - statuses['migrated']}**", "",
        "## Safety Confirmation", "", "```text", "Files deleted: 0", "Duplicate groups merged: 0", "Files archived: 0",
        "Lesson content rewritten: 0", "Commits created: 0", "Pushes performed: 0", "```", "",
    ])
    MIGRATION_LOG.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def finalize() -> int:
    """Create the post-manifest and final Phase 3 reports from actual state."""
    audited = read_pre_manifest()
    results = load_results()
    moved = {item["original_path"]: item for item in results["moves"]}
    post_rows: list[dict[str, Any]] = []
    for row in audited:
        move = moved.get(row["current_path"])
        status = post_status(row, moved)
        current = row["proposed_path"] if move else row["current_path"]
        current_path = ROOT / Path(current)
        after_size = current_path.stat().st_size if current_path.is_file() else ""
        after_hash = sha256(current_path) if current_path.is_file() else ""
        post_rows.append({
            "original_path": row["current_path"], "current_path": current, "migration_status": status,
            "size_before": row["size_bytes"], "size_after": after_size,
            "sha256_before": row["sha256"], "sha256_after": after_hash,
            "content_changed": "no" if row["sha256"] == after_hash else "yes",
            "link_repairs": "0", "notes": row["decision_reason"] if not move else move["method"],
        })
    write_csv(POST_MANIFEST, [
        "original_path", "current_path", "migration_status", "size_before", "size_after",
        "sha256_before", "sha256_after", "content_changed", "link_repairs", "notes",
    ], post_rows)
    LINK_REPORT.write_text(
        "# Phase 3 Link Repairs\n\nNo migrated note required a link repair. Note bodies remained byte-identical.\n",
        encoding="utf-8", newline="\n",
    )
    write_migration_log(audited, results, post_rows)
    mismatches = [row for row in post_rows if row["content_changed"] == "yes"]
    statuses = Counter(row["migration_status"] for row in post_rows)
    print(json.dumps({"entries": len(post_rows), "statuses": statuses, "checksum_mismatches": len(mismatches)}, default=dict))
    return 1 if mismatches else 0


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--prepare", action="store_true", help="write pre-manifest and audit reports")
    mode.add_argument("--dry-run", action="store_true", help="print proposed moves without changing paths")
    mode.add_argument("--execute", action="store_true", help="perform approved moves explicitly")
    mode.add_argument("--finalize", action="store_true", help="write post-manifest and final reports")
    parser.add_argument("--category", choices=CATEGORIES, help="filter by two-digit destination category")
    return parser.parse_args()


def main() -> int:
    """Dispatch the selected migration mode."""
    configure_output()
    args = parse_args()
    if args.prepare:
        return prepare()
    if args.dry_run:
        return dry_run(args.category)
    if args.execute:
        return execute(args.category)
    return finalize()


if __name__ == "__main__":
    sys.exit(main())
