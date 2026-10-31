"""Report duplicate, versioned, case-only, trailing-space, and similar filenames."""

from __future__ import annotations

import difflib
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"(?:^|[\s_.()\-])(v1|v2|final|new|claude[\s_-]+version|claude[\s_-]+code)(?:$|[\s_.()\-])", re.I)


def files() -> list[Path]:
    """Return repository files while excluding Git internals and generated output."""
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.relative_to(ROOT).parts
        and "__pycache__" not in path.relative_to(ROOT).parts
        and path.relative_to(ROOT).parts[:2] != ("reports", "generated")
    )


def normalized(name: str) -> str:
    """Normalize a filename for duplicate comparison."""
    value = unicodedata.normalize("NFKC", Path(name).stem).casefold().strip()
    value = VERSION_RE.sub(" ", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def report_group(label: str, paths: list[Path]) -> None:
    """Print one candidate group."""
    print(f"{label}:")
    for path in paths:
        print(f"  - {path.relative_to(ROOT).as_posix()}")


def main() -> int:
    """Detect active version markers and per-directory canonical collisions."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    paths = files()
    groups: list[tuple[str, list[Path]]] = []
    active = [path for path in paths if path.relative_to(ROOT).parts and re.match(r"^(?:0[1-9]|1[0-6])-", path.relative_to(ROOT).parts[0])]
    for path in active:
        if VERSION_RE.search(path.name):
            groups.append(("Version-suffixed active filename", [path]))
    by_directory: dict[Path, list[Path]] = defaultdict(list)
    for path in active:
        if path.suffix.lower() == ".md" and path.name != "README.md":
            by_directory[path.parent].append(path)
    for members in by_directory.values():
        normalized_groups: dict[str, list[Path]] = defaultdict(list)
        numbers: dict[str, list[Path]] = defaultdict(list)
        for path in members:
            normalized_groups[normalized(path.name)].append(path)
            match = re.match(r"^(\d{2})-", path.name)
            if match:
                numbers[match.group(1)].append(path)
        for same in normalized_groups.values():
            if len(same) > 1:
                groups.append(("Same normalized filename in one directory", same))
        for same in numbers.values():
            if len(same) > 1:
                groups.append(("Duplicate lesson number in one directory", same))
        overviews = [path for path in members if path.name.endswith("overview.md")]
        if len(overviews) > 1:
            groups.append(("Multiple overview files in one service directory", overviews))
    if groups:
        for label, members in groups:
            report_group(label, members)
        print(f"Duplicate scan found {len(groups)} candidate group(s); review is required.")
        return 1
    print(f"Duplicate scan passed: {len(paths)} file(s), no candidates found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
