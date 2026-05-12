"""
7 Days to Die — Dye Palette Audit
==================================

Parses EV_VividDyes/Config/item_modifiers.xml, extracts every custom dye's
TintColor, then checks every unordered colour pair using perceptual metrics:

  • ΔE00 (CIEDE2000)       — primary gate
  • Rec.601 grayscale gap  — secondary readability signal
  • HSL hue gap            — heuristic for same-brightness collisions

Pair classification (report-only; script always exits 0):
  PASS  ΔE00 ≥ target  (default 30)
  WARN  ΔE00 ≥ min     (default 25)
  FAIL  ΔE00 < min     (default 25)

The script logs every pair to the console, sorted by ΔE00 ascending, followed
by a summary block.  No files are written or modified.

Usage
-----
    python scripts/check_dye_palette.py
    python scripts/check_dye_palette.py --xml path/to/item_modifiers.xml
    python scripts/check_dye_palette.py --min-delta-e 25 --target-delta-e 30 --min-gray-gap 30 --min-hue-gap 25
"""

from __future__ import annotations

import argparse
import itertools
import math
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_XML = REPO_ROOT / "Mods" / "EV_VividDyes" / "Config" / "item_modifiers.xml"

# ── colour math ────────────────────────────────────────────────────────────────


def _srgb_to_linear(c: float) -> float:
    """Convert one sRGB 0-255 channel to linear light."""
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _rgb_to_xyz_d65(r: int, g: int, b: int) -> tuple[float, float, float]:
    """sRGB (0-255) → CIE XYZ D65, Y normalised to 100."""
    rl = _srgb_to_linear(r)
    gl = _srgb_to_linear(g)
    bl = _srgb_to_linear(b)
    x = (rl * 0.4124564 + gl * 0.3575761 + bl * 0.1804375) * 100
    y = (rl * 0.2126729 + gl * 0.7151522 + bl * 0.0721750) * 100
    z = (rl * 0.0193339 + gl * 0.1191920 + bl * 0.9503041) * 100
    return x, y, z


def _f_lab(t: float) -> float:
    d = 6 / 29
    return t ** (1 / 3) if t > d ** 3 else t / (3 * d * d) + 4 / 29


def _xyz_to_lab(x: float, y: float, z: float) -> tuple[float, float, float]:
    """CIE XYZ D65 (Y=100 scale) → CIELAB."""
    xn, yn, zn = 95.047, 100.0, 108.883
    fx, fy, fz = _f_lab(x / xn), _f_lab(y / yn), _f_lab(z / zn)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def rgb_to_lab(r: int, g: int, b: int) -> tuple[float, float, float]:
    return _xyz_to_lab(*_rgb_to_xyz_d65(r, g, b))


def ciede2000(
    lab1: tuple[float, float, float],
    lab2: tuple[float, float, float],
) -> float:
    """CIEDE2000 colour difference (ΔE00) between two CIELAB colours."""
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2

    C1 = math.sqrt(a1 * a1 + b1 * b1)
    C2 = math.sqrt(a2 * a2 + b2 * b2)
    C_avg = (C1 + C2) / 2
    C_avg7 = C_avg ** 7
    G = 0.5 * (1 - math.sqrt(C_avg7 / (C_avg7 + 25 ** 7)))

    a1p = a1 * (1 + G)
    a2p = a2 * (1 + G)
    C1p = math.sqrt(a1p * a1p + b1 * b1)
    C2p = math.sqrt(a2p * a2p + b2 * b2)

    def hprime(ap: float, bp: float) -> float:
        if ap == 0 and bp == 0:
            return 0.0
        h = math.degrees(math.atan2(bp, ap))
        return h if h >= 0 else h + 360

    h1p = hprime(a1p, b1)
    h2p = hprime(a2p, b2)

    dLp = L2 - L1
    dCp = C2p - C1p

    if C1p * C2p == 0:
        dhp = 0.0
    elif abs(h2p - h1p) <= 180:
        dhp = h2p - h1p
    elif h2p - h1p > 180:
        dhp = h2p - h1p - 360
    else:
        dhp = h2p - h1p + 360

    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))

    Lp_avg = (L1 + L2) / 2
    Cp_avg = (C1p + C2p) / 2

    if C1p * C2p == 0:
        hp_avg = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hp_avg = (h1p + h2p) / 2
    elif h1p + h2p < 360:
        hp_avg = (h1p + h2p + 360) / 2
    else:
        hp_avg = (h1p + h2p - 360) / 2

    T = (
        1
        - 0.17 * math.cos(math.radians(hp_avg - 30))
        + 0.24 * math.cos(math.radians(2 * hp_avg))
        + 0.32 * math.cos(math.radians(3 * hp_avg + 6))
        - 0.20 * math.cos(math.radians(4 * hp_avg - 63))
    )

    SL = 1 + 0.015 * (Lp_avg - 50) ** 2 / math.sqrt(20 + (Lp_avg - 50) ** 2)
    SC = 1 + 0.045 * Cp_avg
    SH = 1 + 0.015 * Cp_avg * T

    Cp_avg7 = Cp_avg ** 7
    RC = 2 * math.sqrt(Cp_avg7 / (Cp_avg7 + 25 ** 7))
    d_theta = 30 * math.exp(-((hp_avg - 275) / 25) ** 2)
    RT = -math.sin(math.radians(2 * d_theta)) * RC

    return math.sqrt(
        (dLp / SL) ** 2
        + (dCp / SC) ** 2
        + (dHp / SH) ** 2
        + RT * (dCp / SC) * (dHp / SH)
    )


def rec601_gray(r: int, g: int, b: int) -> float:
    return 0.299 * r + 0.587 * g + 0.114 * b


def hsl_hue(r: int, g: int, b: int) -> float:
    """HSL hue in degrees [0, 360)."""
    rf, gf, bf = r / 255, g / 255, b / 255
    cmax = max(rf, gf, bf)
    cmin = min(rf, gf, bf)
    delta = cmax - cmin
    if delta == 0:
        return 0.0
    if cmax == rf:
        h = ((gf - bf) / delta) % 6
    elif cmax == gf:
        h = (bf - rf) / delta + 2
    else:
        h = (rf - gf) / delta + 4
    return h * 60


def hsl_saturation(r: int, g: int, b: int) -> float:
    rf, gf, bf = r / 255, g / 255, b / 255
    cmax = max(rf, gf, bf)
    cmin = min(rf, gf, bf)
    delta = cmax - cmin
    lightness = (cmax + cmin) / 2
    if delta == 0:
        return 0.0
    return delta / (1 - abs(2 * lightness - 1))


def w3c_luminance(r: int, g: int, b: int) -> float:
    """W3C relative luminance [0, 1]."""
    return 0.2126 * _srgb_to_linear(r) + 0.7152 * _srgb_to_linear(g) + 0.0722 * _srgb_to_linear(b)


def hue_diff(h1: float, h2: float) -> float:
    """Smallest angular difference between two hue values in degrees."""
    diff = abs(h1 - h2) % 360
    return min(diff, 360 - diff)


# ── dye model ──────────────────────────────────────────────────────────────────

_CAMEL_RE = re.compile(r"(?<=[a-z])(?=[A-Z])")


def _dye_label(mod_name: str) -> str:
    """modDyeBloodNeon → Blood Neon"""
    return _CAMEL_RE.sub(" ", mod_name.removeprefix("modDye"))


@dataclass
class Dye:
    id: str
    display_name: str
    rgb: tuple[int, int, int]
    icon_rgb: tuple[int, int, int]
    # derived
    hex: str = field(init=False)
    gray: float = field(init=False)
    hue: float = field(init=False)
    saturation: float = field(init=False)
    lab: tuple[float, float, float] = field(init=False)
    luminance: float = field(init=False)

    def __post_init__(self) -> None:
        r, g, b = self.rgb
        self.hex = f"#{r:02X}{g:02X}{b:02X}"
        self.gray = rec601_gray(r, g, b)
        self.hue = hsl_hue(r, g, b)
        self.saturation = hsl_saturation(r, g, b)
        self.lab = rgb_to_lab(r, g, b)
        self.luminance = w3c_luminance(r, g, b)


def _parse_rgb(value: str) -> tuple[int, int, int] | None:
    try:
        parts = [int(x.strip()) for x in value.split(",")]
        if len(parts) != 3:
            return None
        r, g, b = parts
        if not all(0 <= c <= 255 for c in (r, g, b)):
            return None
        return r, g, b
    except (ValueError, AttributeError):
        return None


def load_dyes(xml_path: Path) -> list[Dye]:
    """Parse item_modifiers.xml and return the list of custom dyes."""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    dyes: list[Dye] = []
    seen_ids: set[str] = set()

    for item_mod in root.iter("item_modifier"):
        name = item_mod.get("name", "")
        if not name.startswith("modDye") or name == "modDyeWhite":
            continue

        # TintColor lives inside <item_property_overrides name="*">
        tint_rgb: tuple[int, int, int] | None = None
        icon_rgb: tuple[int, int, int] | None = None

        overrides = item_mod.find("item_property_overrides")
        if overrides is not None:
            for prop in overrides.findall("property"):
                pname = prop.get("name", "")
                if pname == "TintColor":
                    tint_rgb = _parse_rgb(prop.get("value", ""))
                elif pname == "CustomIconTint":
                    icon_rgb = _parse_rgb(prop.get("value", ""))

        # Top-level CustomIconTint fallback
        if icon_rgb is None:
            for prop in item_mod.findall("property"):
                if prop.get("name") == "CustomIconTint":
                    icon_rgb = _parse_rgb(prop.get("value", ""))
                    break

        if tint_rgb is None:
            print(f"  WARN  {name}: missing TintColor — skipped")
            continue
        if icon_rgb is None:
            icon_rgb = tint_rgb

        if name in seen_ids:
            print(f"  WARN  {name}: duplicate ID — using first occurrence")
            continue
        seen_ids.add(name)

        dyes.append(Dye(id=name, display_name=_dye_label(name), rgb=tint_rgb, icon_rgb=icon_rgb))

    return dyes


# ── pair evaluation ────────────────────────────────────────────────────────────

@dataclass
class PairResult:
    dye_a: Dye
    dye_b: Dye
    delta_e: float
    gray_diff: float
    hue_diff_deg: float
    status: str
    notes: list[str]


def evaluate_pair(
    a: Dye,
    b: Dye,
    min_de: float,
    target_de: float,
    min_gray_gap: float,
    min_hue_gap: float,
) -> PairResult:
    de = ciede2000(a.lab, b.lab)
    gd = abs(a.gray - b.gray)
    hd = hue_diff(a.hue, b.hue)

    notes: list[str] = []
    if gd < min_gray_gap:
        notes.append(f"Δgray={gd:.0f}<{min_gray_gap:.0f}")
    if hd < min_hue_gap and a.saturation > 0.5 and b.saturation > 0.5:
        notes.append(f"Δhue={hd:.0f}°<{min_hue_gap:.0f}°")

    if de < min_de:
        status = "FAIL"
    elif de < target_de:
        status = "WARN"
    else:
        status = "PASS"

    return PairResult(a, b, de, gd, hd, status, notes)


# ── output helpers ─────────────────────────────────────────────────────────────

_W = 22  # display-name column width


def _row(r: PairResult) -> str:
    note_str = ("  !" + " !".join(r.notes)) if r.notes else ""
    return (
        f"  {r.status}  "
        f"{r.dye_a.display_name:<{_W}} {r.dye_a.hex}  vs  "
        f"{r.dye_b.display_name:<{_W}} {r.dye_b.hex}  "
        f"ΔE00={r.delta_e:5.1f}  Δgray={r.gray_diff:5.1f}  Δhue={r.hue_diff_deg:5.1f}°"
        f"{note_str}"
    )


# ── main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit EV_VividDyes dye palette for perceptual colour separation."
    )
    parser.add_argument(
        "--xml",
        type=Path,
        default=DEFAULT_XML,
        metavar="PATH",
        help="Path to item_modifiers.xml (default: auto-detected from repo root)",
    )
    parser.add_argument("--min-delta-e",  type=float, default=25.0, metavar="N", help="FAIL threshold (default 25)")
    parser.add_argument("--target-delta-e", type=float, default=30.0, metavar="N", help="PASS threshold (default 30)")
    parser.add_argument("--min-gray-gap", type=float, default=30.0, metavar="N", help="Grayscale gap warning threshold (default 30)")
    parser.add_argument("--min-hue-gap",  type=float, default=25.0, metavar="N", help="Hue-angle gap warning threshold (default 25°)")
    args = parser.parse_args()

    xml_path: Path = args.xml.resolve()
    if not xml_path.is_file():
        raise SystemExit(f"File not found: {xml_path}")

    try:
        shown = xml_path.relative_to(REPO_ROOT)
    except ValueError:
        shown = xml_path

    print(f"Loading dyes from: {shown}\n")
    dyes = load_dyes(xml_path)

    if not dyes:
        raise SystemExit("No custom dyes found in the specified file.")

    print(f"Loaded {len(dyes)} dye(s):")
    for d in dyes:
        print(f"  {d.display_name:<{_W}} {d.hex}  gray={d.gray:5.1f}  hue={d.hue:5.1f}°  sat={d.saturation:.2f}  L*={d.lab[0]:5.1f}")

    n_expected = len(dyes) * (len(dyes) - 1) // 2
    print(f"\nChecking {n_expected} unordered pairs ...\n")

    results: list[PairResult] = [
        evaluate_pair(a, b, args.min_delta_e, args.target_delta_e, args.min_gray_gap, args.min_hue_gap)
        for a, b in itertools.combinations(dyes, 2)
    ]
    results.sort(key=lambda r: r.delta_e)

    print(f"─── Pair results ({len(results)} pairs, sorted by ΔE00 asc) " + "─" * 40)
    for r in results:
        print(_row(r))

    # ── summary ──────────────────────────────────────────────────────────────
    n_pass = sum(1 for r in results if r.status == "PASS")
    n_warn = sum(1 for r in results if r.status == "WARN")
    n_fail = sum(1 for r in results if r.status == "FAIL")

    print()
    print("─── Summary " + "─" * 70)
    print(f"  Dyes loaded   : {len(dyes)}")
    print(f"  Pairs checked : {len(results)}")
    print(f"  PASS (ΔE00 ≥ {args.target_delta_e:.0f}) : {n_pass}")
    print(f"  WARN (ΔE00 ≥ {args.min_delta_e:.0f}) : {n_warn}")
    print(f"  FAIL (ΔE00 < {args.min_delta_e:.0f}) : {n_fail}")

    worst = results[:10]
    print(f"\n  Worst {len(worst)} pairs by ΔE00:")
    for r in worst:
        print(f"    [{r.status}]  {r.dye_a.display_name} vs {r.dye_b.display_name}  ΔE00={r.delta_e:.1f}")

    flagged = [r for r in results if r.notes]
    if flagged:
        print(f"\n  Pairs with additional risk flags ({len(flagged)}):")
        for r in flagged:
            print(f"    [{r.status}]  {r.dye_a.display_name} / {r.dye_b.display_name}: " + ", ".join(r.notes))

    print()
    print("  Audit complete.  Script is report-only — no files were modified.")

    # Always exit 0 (report-only mode).


if __name__ == "__main__":
    main()
