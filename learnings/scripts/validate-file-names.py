"""Validate canonical repository paths without modifying any files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_RE = re.compile(r"^(?:0[1-9]|1[0-6]|90)-[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN_RE = re.compile(
    r"(?:^|[\s_.()\-])(v1|v2|final|new|claude[\s_-]+version|claude[\s_-]+code)(?:$|[\s_.()\-])",
    re.IGNORECASE,
)
MANDATED_CONTROL_RECORDS = {
    "docs/content-implementation/PHASE-6-BATCH-2-FINAL-RECONCILIATION.csv",
    "docs/content-implementation/PHASE-6-BATCH-2-FINAL-RECONCILIATION.md",
    "docs/content-implementation/PHASE-6-FINAL-BACKLOG-RECONCILIATION.csv",
    "docs/content-implementation/PHASE-6-FINAL-COVERAGE-RECONCILIATION.md",
    "docs/content-implementation/PHASE-6-FINAL-VALIDATION.md",
    "docs/release/FINAL-HANDOFF-BLOCKERS.md",
    "docs/release/FINAL-HANDOFF-CHANGELOG.md",
    "docs/release/FINAL-COMMIT-EXECUTION-LOG.md",
    "docs/release/FINAL-MERGE-READINESS-REPORT.md",
    "docs/release/FINAL-PULL-REQUEST-BODY.md",
    "docs/release/FINAL-PR-REVIEW-CHECKLIST.md",
    "docs/release/FINAL-RELEASE-CANDIDATE-HANDOFF.md",
    "docs/release/FINAL-SECURITY-AND-HYGIENE-REVIEW.md",
    "docs/release/FINAL-STAGING-MANIFEST.txt",
    "docs/release/FINAL-VALIDATION-RESULTS.md",
}
ROOT_FILES = {
    "README.md", "AGENTS.md", "CONTRIBUTING.md", ".gitattributes",
    ".gitignore", ".markdownlint.json",
}
DOC_FILES = {
    "docs/README.md", "docs/repository-map.md", "docs/certification-labels.md",
    "docs/content-standards.md", "docs/file-naming-standard.md",
    "docs/source-policy.md", "docs/reorganization/PHASE-2-CHANGELOG.md",
}
SCRIPT_FILES = {
    "scripts/README.md", "scripts/validate-file-names.py",
    "scripts/validate-markdown-links.py", "scripts/detect-duplicate-filenames.py",
    "scripts/generate-repository-report.py",
}


def is_category(part: str) -> bool:
    """Return whether a path segment is a canonical root category."""
    return bool(CATEGORY_RE.fullmatch(part))


def foundation_paths() -> list[Path]:
    """Return only Phase 2 foundation files and category contents."""
    paths = [ROOT / name for name in ROOT_FILES]
    paths.extend(ROOT / name for name in DOC_FILES)
    paths.extend(ROOT / name for name in SCRIPT_FILES)
    for path in ROOT.iterdir():
        if path.is_dir() and is_category(path.name):
            paths.extend(item for item in path.rglob("*") if item.is_file())
    return sorted({path for path in paths if path.exists()})


def all_paths() -> list[Path]:
    """Return all repository files except Git internals."""
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.relative_to(ROOT).parts
        and "__pycache__" not in path.relative_to(ROOT).parts
    )


def validate(path: Path, foundation_only: bool) -> list[str]:
    """Return naming errors for one path."""
    rel = path.relative_to(ROOT)
    errors: list[str] = []
    mandated_phase7_record = rel.parts[:2] == ("docs", "final-review")
    category_content = bool(rel.parts and is_category(rel.parts[0]))
    for index, part in enumerate(rel.parts):
        if part != part.rstrip():
            errors.append("trailing whitespace in path segment")
        if "(" in part or ")" in part:
            errors.append("parentheses in path")
        if "--" in part or "__" in part:
            errors.append("duplicate separator")
        if FORBIDDEN_RE.search(part) and rel.as_posix() not in MANDATED_CONTROL_RECORDS and not mandated_phase7_record:
            errors.append("forbidden version marker")
        canonical_segment = category_content and index > 0
        if canonical_segment and part != "README.md" and any(char.isupper() for char in part):
            errors.append("uppercase canonical path segment")
        if canonical_segment and " " in part:
            errors.append("space in canonical path")
    if category_content and path.suffix.lower() != ".md":
        errors.append("non-Markdown file in note category")
    if not foundation_only and " " in rel.as_posix():
        errors.append("space in legacy or canonical path")
    return sorted(set(errors))


def main() -> int:
    """Run validation and return a process exit code."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--foundation-only", action="store_true")
    mode.add_argument("--all", action="store_true")
    args = parser.parse_args()
    paths = foundation_paths() if args.foundation_only else all_paths()
    failures = [(path, validate(path, args.foundation_only)) for path in paths]
    if args.all:
        legacy_names = {
            "a) Service Explanations", "b) Service Comparisons", "c) Keywords services",
            "d) Tools & Policies", "e) AWS Claude Network & Gateways", "f) EC2",
            "g)ELB & ASG", "h) RDS",
        }
        for name in legacy_names:
            if (ROOT / name).exists():
                failures.append((ROOT / name, ["legacy top-level directory remains"]))
        for directory in (path for path in ROOT.rglob("*") if path.is_dir()):
            rel = directory.relative_to(ROOT)
            if not rel.parts or not is_category(rel.parts[0]):
                continue
            lessons = [item for item in directory.glob("*.md") if item.name != "README.md"]
            numbers: dict[str, list[Path]] = {}
            for lesson in lessons:
                match = re.match(r"^(\d{2})-", lesson.name)
                if match:
                    numbers.setdefault(match.group(1), []).append(lesson)
                if lesson.stat().st_size == 0:
                    failures.append((lesson, ["empty Markdown file"]))
                text = lesson.read_text(encoding="utf-8")
                if re.search(r"^#{1,6}\s*$", text, re.MULTILINE):
                    failures.append((lesson, ["empty lesson heading"]))
                if "prompt" in lesson.name.casefold():
                    failures.append((lesson, ["prompt template inside learning category"]))
            for number, members in numbers.items():
                if len(members) > 1:
                    for member in members:
                        failures.append((member, [f"duplicate lesson number {number} in directory"]))
            if len([item for item in lessons if item.name.endswith("overview.md")]) > 1:
                for item in lessons:
                    if item.name.endswith("overview.md"):
                        failures.append((item, ["multiple canonical overview files in one service directory"]))
    failures = [(path, errors) for path, errors in failures if errors]
    if failures:
        for path, errors in failures:
            print(f"ERROR: {path.relative_to(ROOT).as_posix()}: {', '.join(errors)}")
        print(f"Naming validation failed: {len(failures)} path(s).")
        return 1
    print(f"Naming validation passed: {len(paths)} path(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
