#!/usr/bin/env python3
"""Scan all chapter .qmd files and extract photo captions.

Outputs a Markdown file (data/captions.md) listing every ![caption](path)
image reference, organized by chapter. Useful as a quick-reference
"caption editing cheat sheet."

Usage:
    python scripts/list-captions.py
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"
OUTPUT_FILE = PROJECT_ROOT / "data" / "captions.md"

# Match Markdown image syntax: ![caption](path)
IMG_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def extract_captions(qmd_path: Path) -> list[dict]:
    """Extract all image captions from a .qmd file."""
    results = []
    for line_num, line in enumerate(qmd_path.read_text(encoding="utf-8").splitlines(), 1):
        for match in IMG_PATTERN.finditer(line):
            caption = match.group(1)
            path = match.group(2)
            results.append({"line": line_num, "caption": caption, "path": path})
    return results


def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    chapters = sorted(CHAPTERS_DIR.glob("ch*.qmd"))
    total = 0
    lines = ["# Photo Captions — All Chapters\n"]
    lines.append("Quick-reference index of every photo and its caption.\n")
    lines.append("Edit captions in the `.qmd` files (search for `![`).\n")
    lines.append("Regenerate this file: `python scripts/list-captions.py`\n")

    for ch in chapters:
        captions = extract_captions(ch)
        if not captions:
            continue
        total += len(captions)
        lines.append(f"\n## {ch.stem} ({len(captions)} photos)\n")
        lines.append("| Line | Caption | File |")
        lines.append("|------|---------|------|")
        for c in captions:
            # Escape pipes in caption text
            safe_caption = c["caption"].replace("|", "\\|")
            # Show just the filename portion for readability
            filename = Path(c["path"]).name.replace("%20", " ")
            lines.append(f"| {c['line']} | {safe_caption} | {filename} |")

    lines.insert(4, f"\n**Total: {total} photos across {len(chapters)} chapters.**\n")

    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE} — {total} captions from {len(chapters)} chapters.")


if __name__ == "__main__":
    main()
