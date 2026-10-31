"""Validate local Markdown links while ignoring external destinations and code fences."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_RE = re.compile(r"^(?:0[1-9]|1[0-6]|90)-")
INLINE_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
REFERENCE_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
FOUNDATION_DOCS = {
    "docs/README.md", "docs/repository-map.md", "docs/certification-labels.md",
    "docs/content-standards.md", "docs/file-naming-standard.md",
    "docs/source-policy.md", "docs/reorganization/PHASE-2-CHANGELOG.md",
}
ROOT_DOCS = {"README.md", "AGENTS.md", "CONTRIBUTING.md"}


def markdown_files(foundation_only: bool) -> list[Path]:
    """Select Markdown files for the requested validation scope."""
    if not foundation_only:
        return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    selected: set[Path] = {ROOT / item for item in ROOT_DOCS | FOUNDATION_DOCS}
    selected.update((ROOT / "scripts").glob("*.md"))
    for path in ROOT.iterdir():
        if path.is_dir() and CATEGORY_RE.match(path.name):
            selected.update(path.rglob("*.md"))
    return sorted(path for path in selected if path.exists())


def visible_lines(text: str) -> list[tuple[int, str]]:
    """Return lines outside fenced code blocks."""
    result: list[tuple[int, str]] = []
    fence: str | None = None
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        marker = "```" if stripped.startswith("```") else "~~~" if stripped.startswith("~~~") else None
        if marker:
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence is None:
            result.append((number, line))
    return result


def slugify(text: str) -> str:
    """Approximate GitHub's heading anchor generation."""
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", text).strip("-")


def anchors(path: Path) -> set[str]:
    """Collect approximate heading anchors for a Markdown file."""
    found: set[str] = set()
    counts: dict[str, int] = {}
    for _, line in visible_lines(path.read_text(encoding="utf-8")):
        match = HEADING_RE.match(line)
        if match:
            base = slugify(match.group(1))
            count = counts.get(base, 0)
            found.add(base if count == 0 else f"{base}-{count}")
            counts[base] = count + 1
    return found


def destinations(path: Path) -> list[tuple[int, str]]:
    """Extract inline links and reference definitions outside code fences."""
    found: list[tuple[int, str]] = []
    for number, line in visible_lines(path.read_text(encoding="utf-8")):
        found.extend((number, match.group(1)) for match in INLINE_LINK_RE.finditer(line))
        reference = REFERENCE_DEF_RE.match(line)
        if reference:
            found.append((number, reference.group(1)))
    return found


def validate_link(source: Path, raw: str) -> str | None:
    """Return an error message for a broken local link, otherwise None."""
    value = raw.strip().strip("<>").split(maxsplit=1)[0]
    if not value or value.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return None
    target_text, _, fragment = value.partition("#")
    target = source if not target_text else source.parent / unquote(target_text)
    target = target.resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return "target escapes repository"
    if target.is_dir() and not fragment:
        return None
    if target.is_dir():
        target = target / "README.md"
    if not target.exists():
        return f"missing target {value}"
    if fragment and target.suffix.lower() == ".md":
        normalized_fragment = slugify(unquote(fragment))
        if normalized_fragment not in anchors(target):
            return f"missing anchor #{fragment}"
    return None


def main() -> int:
    """Run local-link validation and return a process exit code."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--foundation-only", action="store_true")
    mode.add_argument("--all", action="store_true")
    args = parser.parse_args()
    failures: list[str] = []
    files = markdown_files(args.foundation_only)
    for path in files:
        for line, destination in destinations(path):
            error = validate_link(path, destination)
            if error:
                failures.append(f"{path.relative_to(ROOT).as_posix()}:{line}: {error}")
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        print(f"Link validation failed: {len(failures)} broken local link(s).")
        return 1
    print(f"Link validation passed: {len(files)} Markdown file(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
