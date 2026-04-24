"""
7 Days to Die — Mod Packager for NexusMods
==========================================

Scans the /Mods folder for all modlets (any subfolder containing a
ModInfo.xml), reads each ModInfo.xml to extract name and version,
and produces individual zip archives ready for upload to nexusmods.com.

Usage
-----
    python scripts/package_mods.py [--output-dir DIR] [--mods MOD1,MOD2]

Output
------
    dist/<Name>_v<Version>.zip  — one archive per mod, containing the
    mod folder at root level so users can extract directly into the
    game's Mods/ directory.

    dist/manifest.json — summary of all packaged mods.
"""

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from packaging.version import Version
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODS_DIR = REPO_ROOT / "Mods"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "dist"

# Matches a single-mod release tag, e.g. "EV_EpicCash-v1.2.1" or
# "ZZ_EV_ProjectZCash-v1.0.0". The <mod> group is the mod folder name.
SINGLE_MOD_TAG_RE = re.compile(r"^(?P<mod>[A-Za-z0-9_]+)-v(?P<version>\d+\.\d+\.\d+)$")

# Files/patterns excluded from the archive (not needed in-game)
EXCLUDE_NAMES = {"NEXUS_DESCRIPTION.txt", ".git", ".gitignore", "__pycache__"}


def parse_mod_info(mod_path: Path) -> dict:
    """Read ModInfo.xml and return a dict with name, version, display_name, description."""
    mod_info_path = mod_path / "ModInfo.xml"
    if not mod_info_path.exists():
        return {}

    tree = ET.parse(mod_info_path)
    root = tree.getroot()

    def get_value(tag: str) -> str:
        el = root.find(tag)
        return el.get("value", "") if el is not None else ""

    return {
        "name": get_value("Name"),
        "display_name": get_value("DisplayName"),
        "description": get_value("Description"),
        "author": get_value("Author"),
        "version": get_value("Version"),
        "website": get_value("Website"),
    }


def collect_mod_files(mod_path: Path) -> list[Path]:
    """Collect all files in the mod folder, excluding non-distributable files."""
    files = []
    for root, dirs, filenames in os.walk(mod_path):
        # Filter out excluded directories in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_NAMES]
        for fname in filenames:
            if fname in EXCLUDE_NAMES:
                continue
            files.append(Path(root) / fname)
    return files


def package_mod(mod_path: Path, output_dir: Path) -> dict | None:
    """Package a single mod into a zip archive. Returns metadata or None on error."""
    folder_name = mod_path.name
    info = parse_mod_info(mod_path)

    if not info:
        print(f"  SKIP  {folder_name} — no ModInfo.xml found")
        return None

    if not info["name"] or not info["version"]:
        print(f"  SKIP  {folder_name} — missing Name or Version in ModInfo.xml")
        return None

    if Version(info["version"]) < Version("1.0.0"):
        print(f"  SKIP  {folder_name} — version {info['version']} is below 1.0.0 (still in development)")
        return None

    archive_name = f"{info['name']}_v{info['version']}.zip"
    archive_path = output_dir / archive_name

    files = collect_mod_files(mod_path)
    if not files:
        print(f"  SKIP  {folder_name} — no files to package")
        return None

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in files:
            # Archive path: EV_ModName/Config/items.xml etc.
            arcname = file_path.relative_to(mod_path.parent)
            zf.write(file_path, arcname)

    size_kb = archive_path.stat().st_size / 1024

    print(f"  OK    {archive_name} ({size_kb:.1f} KB, {len(files)} files)")

    return {
        "folder": folder_name,
        "archive": archive_name,
        "size_bytes": archive_path.stat().st_size,
        "file_count": len(files),
        **info,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Package 7D2D mods from /Mods into zip archives for NexusMods."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to write zip archives (default: {DEFAULT_OUTPUT_DIR.relative_to(REPO_ROOT)})",
    )
    parser.add_argument(
        "--mods",
        type=str,
        default="",
        help="Comma-separated list of mod folder names to package (default: all mods in /Mods)",
    )
    parser.add_argument(
        "--tag",
        type=str,
        default="",
        help=(
            "Git tag driving this release. If it matches '<ModFolder>-v<X.Y.Z>' only that"
            " mod is packaged and its version is verified against ModInfo.xml. Other"
            " tag shapes (e.g. '2026.04.23.7') package every mod in /Mods."
        ),
    )
    args = parser.parse_args()

    output_dir: Path = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Resolve mod selection: explicit --mods wins, otherwise try --tag, otherwise all.
    single_mod_name: str | None = None
    single_mod_expected_version: str | None = None
    if not args.mods and args.tag:
        m = SINGLE_MOD_TAG_RE.match(args.tag)
        if m:
            single_mod_name = m.group("mod")
            single_mod_expected_version = m.group("version")
            args.mods = single_mod_name

    # Discover mods
    if args.mods:
        mod_names = [m.strip() for m in args.mods.split(",") if m.strip()]
        mod_dirs = []
        for name in mod_names:
            mod_path = MODS_DIR / name
            if mod_path.is_dir():
                mod_dirs.append(mod_path)
            else:
                print(f"  WARN  {name} — folder not found, skipping")
    else:
        mod_dirs = sorted(
            p for p in MODS_DIR.iterdir()
            if p.is_dir()
            and not p.name.startswith(".")
            and (p / "ModInfo.xml").is_file()
        )

    if not mod_dirs:
        print("No mods found to package.")
        sys.exit(1)

    print(f"Packaging {len(mod_dirs)} mod(s) into {output_dir.relative_to(REPO_ROOT)}/\n")

    manifest = []
    errors = 0

    for mod_path in mod_dirs:
        result = package_mod(mod_path, output_dir)
        if result:
            manifest.append(result)
        else:
            errors += 1

    # When a single-mod tag drove this run, verify the tag version matches ModInfo.xml.
    if single_mod_name and single_mod_expected_version:
        actual = manifest[0]["version"] if manifest else None
        if actual != single_mod_expected_version:
            print(
                f"\nERROR  Tag version v{single_mod_expected_version} does not match"
                f" {single_mod_name}/ModInfo.xml version {actual!r}."
            )
            sys.exit(2)

    # Write manifest
    manifest_path = output_dir / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\nDone: {len(manifest)} packaged, {errors} skipped.")
    print(f"Manifest: {manifest_path.relative_to(REPO_ROOT)}")

    if errors > 0 and not manifest:
        sys.exit(1)


if __name__ == "__main__":
    main()
