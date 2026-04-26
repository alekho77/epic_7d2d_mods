"""
7 Days to Die \u2014 Release Notes Builder
======================================

Consumes ``dist/manifest.json`` produced by ``package_mods.py`` and writes
``dist/RELEASE_NOTES.md`` \u2014 a nicely formatted changelog body ready to be
used as the release body by ``softprops/action-gh-release``.

Behaviour
---------
- For every packaged mod it extracts the ``### vX.Y.Z`` block matching the
  mod's current version from its README.md ``## Changelog`` section.
- If the matching block cannot be located, it falls back to a terse line
  pointing the reader to the mod's README.
- The top of the file also surfaces the release title and an archive table
  (name \u2192 size) so the release page is self-descriptive.

Usage
-----
    python scripts/build_release_notes.py \\
        --manifest dist/manifest.json \\
        --output   dist/RELEASE_NOTES.md \\
        [--tag v2026.04.23]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODS_DIR = REPO_ROOT / "Mods"


def extract_changelog_entry(readme_path: Path, version: str) -> str | None:
    """Return the Markdown body of the ``### vX.Y.Z`` block for ``version``.

    The block starts at a line like ``### v1.2.1`` (optionally followed by
    trailing text) and ends at the next ``### ``/``## ``/``---`` boundary.
    """
    if not readme_path.is_file():
        return None

    text = readme_path.read_text(encoding="utf-8")

    # Locate the Changelog section first to avoid matching unrelated headings.
    changelog_match = re.search(r"^##\s+Changelog\s*$", text, re.MULTILINE)
    if not changelog_match:
        return None
    changelog_body = text[changelog_match.end():]

    pattern = re.compile(
        rf"^###\s+v{re.escape(version)}\b.*?$(?P<body>.*?)"
        r"(?=^###\s+v|^##\s+|^---\s*$)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(changelog_body)
    if not m:
        return None

    return m.group("body").strip()


def format_size(size_bytes: int) -> str:
    kb = size_bytes / 1024
    if kb < 1024:
        return f"{kb:.1f} KB"
    return f"{kb / 1024:.2f} MB"


def build_notes(manifest: list[dict], tag: str) -> str:
    lines: list[str] = []

    if len(manifest) == 1:
        mod = manifest[0]
        title = f"{mod.get('display_name') or mod['name']} v{mod['version']}"
    elif tag:
        title = f"EpicVales Mod Pack {tag}"
    else:
        title = "EpicVales Mod Pack"

    lines.append(f"# {title}")
    lines.append("")
    lines.append(
        "Drop-in modlets for **7 Days to Die**. Download the archive for the"
        " mod you want and extract it into your game's `Mods/` folder."
    )
    lines.append("")

    # Archive table \u2014 always useful, even for single-mod releases.
    lines.append("## \U0001F4E6 Archives")
    lines.append("")
    lines.append("| Mod | Version | Archive | Size |")
    lines.append("| --- | --- | --- | ---: |")
    for mod in manifest:
        display = mod.get("display_name") or mod["name"]
        lines.append(
            f"| {display} | v{mod['version']} | `{mod['archive']}` |"
            f" {format_size(mod['size_bytes'])} |"
        )
    lines.append("")

    lines.append("## \U0001F4CB What's in this release")
    lines.append("")

    for mod in manifest:
        display = mod.get("display_name") or mod["name"]
        folder = mod["folder"]
        version = mod["version"]

        lines.append(f"### {display} \u2014 v{version}")
        lines.append("")

        description = (mod.get("description") or "").strip()
        if description:
            lines.append(f"_{description}_")
            lines.append("")

        readme_path = MODS_DIR / folder / "README.md"
        entry = extract_changelog_entry(readme_path, version)
        if entry:
            lines.append(entry)
        else:
            lines.append(
                f"See [`{folder}/README.md`](Mods/{folder}/README.md) for the"
                " full changelog."
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "**Installation:** extract the `EV_*` folder from the archive into"
        " `<7DaysToDie>/Mods/`. Server-side-friendly modlets only need to be"
        " installed on the dedicated server \u2014 see each mod's README for"
        " details."
    )
    lines.append("")
    lines.append(
        "**Author:** Aleksei Khozin \u00b7 **Community:**"
        " [EpicVales Steam Group](https://steamcommunity.com/groups/epic-vales)"
        " \u00b7 **Source:**"
        " [GitHub](https://github.com/alekho77/epic_7d2d_mods)"
    )
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build Markdown release notes from dist/manifest.json."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=REPO_ROOT / "dist" / "manifest.json",
        help="Path to the manifest.json produced by package_mods.py.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "dist" / "RELEASE_NOTES.md",
        help="Where to write the generated release notes.",
    )
    parser.add_argument(
        "--tag",
        type=str,
        default="",
        help="Git tag driving this release (used only for titling).",
    )
    args = parser.parse_args()

    manifest_path: Path = args.manifest.resolve()
    if not manifest_path.is_file():
        raise SystemExit(f"Manifest not found: {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, list) or not manifest:
        raise SystemExit("Manifest is empty \u2014 nothing to release.")

    notes = build_notes(manifest, args.tag)

    output_path: Path = args.output.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(notes, encoding="utf-8")

    try:
        shown = output_path.relative_to(REPO_ROOT)
    except ValueError:
        shown = output_path
    print(f"Wrote release notes: {shown} ({len(manifest)} mod(s))")


if __name__ == "__main__":
    main()
