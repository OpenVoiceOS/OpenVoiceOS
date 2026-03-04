#!/usr/bin/env python3
"""Report package conflicts and issues that need human intervention.

Reads constraints-alpha.txt, constraints-testing.txt, and lists/unstable.list
and produces a structured report covering:

  1. Universal dependency conflicts  — in unstable.list, excluded from testing.
     Action: fix the package's dependencies and make a new release.

  2. Python version restrictions     — present in testing but only for older
     Pythons (;python_version<"X.Y" marker).
     Action: update transitive dependencies to add wheels for newer Python.

  3. No stable release on PyPI       — alpha pre-release exists but no stable
     version; package is absent from testing entirely.
     Action: cut a stable (non-pre-release) release.
"""

import json
import re
import subprocess
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ALPHA_FILE = Path("constraints-alpha.txt")
TESTING_FILE = Path("constraints-testing.txt")
UNSTABLE_FILE = Path("lists/unstable.list")
VENV_BASE = Path(".venvs")
PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13", "3.14", "3.15"]

_pypi_cache: dict[str, str | None] = {}


# ---------------------------------------------------------------------------
# Shared parsing helpers (duplicated intentionally — standalone script)
# ---------------------------------------------------------------------------

def normalize_name(name: str) -> str:
    return name.lower().replace("_", "-")


def parse_line(line: str):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    m = re.match(r"([A-Za-z0-9_\-]+)(.*)", line)
    if not m:
        return None
    return m.group(1), m.group(2).strip()


def is_prerelease(version: str) -> bool:
    return bool(re.search(r"[a-zA-Z]", version))


def version_tuple(v: str) -> tuple:
    parts = re.match(r"(\d+)\.(\d+)\.?(\d*)", v)
    if not parts:
        return (0, 0, 0)
    return tuple(int(x) if x else 0 for x in parts.groups())


def load_packages(path: Path) -> dict:
    packages = {}
    if not path.exists():
        return packages
    for line in path.read_text().splitlines():
        parsed = parse_line(line)
        if parsed is None:
            continue
        raw_name, spec = parsed
        packages[normalize_name(raw_name)] = (raw_name, spec)
    return packages


def load_name_list(path: Path) -> set:
    if not path.exists():
        return set()
    names = set()
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            names.add(normalize_name(line))
    return names


def get_latest_stable(package_name: str) -> str | None:
    norm = normalize_name(package_name)
    if norm in _pypi_cache:
        return _pypi_cache[norm]
    url = f"https://pypi.org/pypi/{norm}/json"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read())
        stable = [
            v for v, files in data["releases"].items()
            if files and not is_prerelease(v)
        ]
        result = str(max(stable, key=version_tuple)) if stable else None
    except Exception:
        result = None
    _pypi_cache[norm] = result
    return result


# ---------------------------------------------------------------------------
# Conflict detail via uv
# ---------------------------------------------------------------------------

def compute_testing_spec(norm: str, alpha_info: tuple | None) -> str | None:
    """Compute the constraint line make_alpha_testing.py would generate for this package."""
    if not alpha_info:
        return None
    raw, spec = alpha_info
    m = re.match(r">=([^\s,]+)", spec)
    if not m:
        return None
    alpha_min = m.group(1)
    if is_prerelease(alpha_min):
        stable = get_latest_stable(raw)
        if stable is None:
            return None
        alpha_min = stable
    major = re.match(r"(\d+)", alpha_min)
    if not major:
        return None
    upper = f"<{int(major.group(1)) + 1}.0.0"
    return f"{normalize_name(raw)}>={alpha_min},{upper}"


def try_add_to_testing(package_spec: str, venv_path: str) -> tuple[bool, str]:
    """
    Try adding package_spec to the current testing constraints.
    Returns (resolves, conflict_summary).
    """
    context_lines = []
    if TESTING_FILE.exists():
        context_lines = [
            l.strip() for l in TESTING_FILE.read_text().splitlines()
            if l.strip() and not l.startswith("#")
        ]
    context_lines.append(package_spec)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("\n".join(context_lines) + "\n")
        tmp = f.name
    try:
        result = subprocess.run(
            ["uv", "pip", "install", "--python", venv_path, "--dry-run", "-r", tmp],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            return True, ""
        return False, (result.stderr + result.stdout).strip() or "(uv output unavailable)"
    finally:
        Path(tmp).unlink(missing_ok=True)


def first_available_venv() -> str | None:
    for ver in PYTHON_VERSIONS:
        venv = VENV_BASE / f"py{ver}"
        if venv.exists():
            return str(venv)
    return None


# ---------------------------------------------------------------------------
# Collect data
# ---------------------------------------------------------------------------

def parse_testing_markers(path: Path) -> dict[str, str | None]:
    """Return {norm_name: python_version_limit_or_None} for all testing entries."""
    result = {}
    if not path.exists():
        return result
    for raw_line in path.read_text().splitlines():
        raw_line = raw_line.strip()
        if not raw_line or raw_line.startswith("#"):
            continue
        name_part = re.split(r"[>=<;]", raw_line)[0].strip()
        norm = normalize_name(name_part)
        marker_match = re.search(r'python_version\s*<\s*"([^"]+)"', raw_line)
        result[norm] = marker_match.group(1) if marker_match else None
    return result


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def main():
    alpha = load_packages(ALPHA_FILE)
    unstable = load_name_list(UNSTABLE_FILE)
    testing_markers = parse_testing_markers(TESTING_FILE)
    testing_names = set(testing_markers)

    venv = first_available_venv()

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    md = []
    a = md.append

    # ------------------------------------------------------------------
    # Collect data for all sections up-front so summary table is first
    # ------------------------------------------------------------------

    # Section 1: probe each unstable package against current testing
    resolved_now = []
    still_broken = []
    for norm in sorted(unstable):
        alpha_info = alpha.get(norm)
        raw_name = alpha_info[0] if alpha_info else norm
        testing_spec = compute_testing_spec(norm, alpha_info)
        if testing_spec is None:
            still_broken.append((raw_name, alpha_info, None, "cannot compute testing spec (no stable on PyPI)"))
            continue
        if venv:
            resolves, reason = try_add_to_testing(testing_spec, venv)
        else:
            resolves, reason = False, "(no venv available to test)"
        if resolves:
            resolved_now.append((raw_name, testing_spec))
        else:
            still_broken.append((raw_name, alpha_info, testing_spec, reason))

    # Section 2: python version restrictions
    restricted = {
        norm: limit
        for norm, limit in testing_markers.items()
        if limit is not None
    }

    # Section 3: alpha packages with no stable PyPI release
    skipped = []
    for norm, (raw, spec) in alpha.items():
        if norm in testing_names or norm in unstable:
            continue
        m = re.match(r">=([^\s,]+)", spec)
        if not m:
            continue
        alpha_min = m.group(1)
        if is_prerelease(alpha_min):
            skipped.append((raw, spec, alpha_min))

    # ------------------------------------------------------------------
    # Render Markdown
    # ------------------------------------------------------------------
    a(f"# Package Conflict Report")
    a(f"")
    a(f"_Generated: {now}_")
    a(f"")
    a(f"| | Count |")
    a(f"|---|---:|")
    a(f"| ✅ Conflicts resolved — re-run `make_alpha_testing.py` | {len(resolved_now)} |")
    a(f"| ❌ Conflicts still broken | {len(still_broken)} |")
    a(f"| ⚠️ Python version restrictions | {len(restricted)} |")
    a(f"| 🔖 Missing stable release on PyPI | {len(skipped)} |")
    a(f"")

    # --- Section 1 ---
    a(f"---")
    a(f"")
    a(f"## 1. Dependency Conflicts")
    a(f"")
    a(f"Packages in [`lists/unstable.list`](lists/unstable.list) excluded from `constraints-testing.txt`.")
    a(f"")

    if not unstable:
        a(f"_None._")
    else:
        if resolved_now:
            a(f"### ✅ Resolved — re-run `make_alpha_testing.py` to include")
            a(f"")
            a(f"| Package | Would add to testing |")
            a(f"|---------|----------------------|")
            for raw_name, spec in resolved_now:
                a(f"| `{raw_name}` | `{spec}` |")
            a(f"")

        if still_broken:
            a(f"### ❌ Still Conflicting — action needed")
            a(f"")
            for raw_name, alpha_info, testing_spec, reason in still_broken:
                alpha_ver = alpha_info[1] if alpha_info else "(not in alpha)"
                a(f"**`{raw_name}{alpha_ver}`**  ")
                if testing_spec:
                    a(f"Would add: `{testing_spec}`")
                a(f"```")
                a(reason)
                a(f"```")
                a(f"")

    # --- Section 2 ---
    a(f"---")
    a(f"")
    a(f"## 2. Python Version Restrictions")
    a(f"")
    a(f"Present in testing but excluded on newer Python via `; python_version < \"X.Y\"` marker.")
    a(f"**Action:** update the transitive dependency to publish wheels for the excluded versions.")
    a(f"")

    if not restricted:
        a(f"_None._")
    else:
        vt = lambda v: tuple(int(p) for p in v.split("."))
        a(f"| Package | Alpha version | Supported | Excluded |")
        a(f"|---------|:-------------:|-----------|----------|")
        for norm in sorted(restricted):
            limit = restricted[norm]
            alpha_info = alpha.get(norm)
            raw_name = alpha_info[0] if alpha_info else norm
            alpha_ver = (alpha_info[1] if alpha_info else "").lstrip(">=")
            supported = ", ".join(v for v in PYTHON_VERSIONS if vt(v) < vt(limit))
            excluded = ", ".join(v for v in PYTHON_VERSIONS if vt(v) >= vt(limit))
            a(f"| `{raw_name}` | {alpha_ver} | {supported} | {excluded} |")
    a(f"")

    # --- Section 3 ---
    a(f"---")
    a(f"")
    a(f"## 3. No Stable Release on PyPI")
    a(f"")
    a(f"Exist in alpha as a pre-release; absent from testing because no stable version is available.")
    a(f"**Action:** cut a stable (non-pre-release) release.")
    a(f"")

    if not skipped:
        a(f"_None._")
    else:
        a(f"| Package | Alpha version | Latest stable |")
        a(f"|---------|:-------------:|:-------------:|")
        for raw, spec, alpha_min in sorted(skipped):
            latest_stable = get_latest_stable(raw)
            note = latest_stable if latest_stable else "—"
            a(f"| `{raw}` | {alpha_min} | {note} |")
    a(f"")

    output = "\n".join(md)
    print(output)

    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("conflicts.md")
    out_path.write_text(output)
    print(f"Report written to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
