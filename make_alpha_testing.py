#!/usr/bin/env python3
"""Sync constraints-testing.txt from constraints-alpha.txt.

Rules:
- Packages removed from alpha (checked against testing + stable) → dropped from
  testing, appended to lists/deprecated.list
- Packages in both testing + alpha:
    - Lower bound preserved from testing (lowered by one minor if it is a
      pre-release); if both testing AND alpha lower bounds are pre-release and
      no higher stable exists on PyPI, the package is skipped.
    - Upper bound set to <(major+1).0.0 based on the alpha lower bound.
- Packages new in alpha:
    - If alpha lower bound is stable → added with that version as lower bound.
    - If alpha lower bound is pre-release → PyPI is queried for a higher
      stable version; if found it is used; otherwise the package is skipped.
- Conflict resolution: uv --dry-run is run against each available Python venv
  in ascending version order.
    - Packages failing on the lowest Python version → universal conflict,
      removed and written to lists/unstable.list (regenerated each run).
    - Packages failing only on higher Python versions → get a
      ;python_version<"X.Y" environment marker.
"""

import json
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ALPHA_FILE = Path("constraints-alpha.txt")
STABLE_FILE = Path("constraints-stable.txt")
TESTING_FILE = Path("constraints-testing.txt")
DEPRECATED_FILE = Path("lists/deprecated.list")
UNSTABLE_FILE = Path("lists/unstable.list")
VENV_BASE = Path(".venvs")
PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13", "3.14", "3.15"]

MAX_CONFLICT_ITERATIONS = 30

_pypi_cache: dict[str, str | None] = {}
_requires_cache: dict[tuple[str, str], list[str]] = {}


def normalize_name(name: str) -> str:
    return name.lower().replace("_", "-")


def parse_line(line: str):
    """Return (raw_name, spec) for a requirement line, else None."""
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    m = re.match(r"([A-Za-z0-9_\-]+)(.*)", line)
    if not m:
        return None
    return m.group(1), m.group(2).strip()


def parse_min_version(spec: str) -> str:
    m = re.match(r">=([^\s,]+)", spec)
    if not m:
        raise ValueError(f"Cannot parse min version from: {spec!r}")
    return m.group(1)


def is_prerelease(version: str) -> bool:
    return bool(re.search(r"[a-zA-Z]", version))


def version_tuple(v: str) -> tuple:
    """Convert 'X.Y.Z' to (X, Y, Z) for simple stable-version comparison."""
    parts = re.match(r"(\d+)\.(\d+)\.?(\d*)", v)
    if not parts:
        return (0, 0, 0)
    return tuple(int(x) if x else 0 for x in parts.groups())


def next_major_upper_bound(version: str) -> str:
    m = re.match(r"(\d+)", version)
    if not m:
        raise ValueError(f"Cannot parse major from: {version!r}")
    return f"<{int(m.group(1)) + 1}.0.0"


def lower_prerelease_min(version: str) -> str:
    """Return X.(Y-1).0 for a pre-release like X.Y.Za; clamp minor to 0."""
    m = re.match(r"(\d+)\.(\d+)\.", version)
    if not m:
        return version
    major, minor = int(m.group(1)), int(m.group(2))
    return f"{major}.{max(minor - 1, 0)}.0"


def get_latest_stable(package_name: str) -> str | None:
    """Query PyPI for the latest stable (non-pre-release) version, or None."""
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


def get_requires_dist(package_name: str, version: str) -> list[str]:
    """Unconditional Requires-Dist entries for an exact package==version release."""
    norm = normalize_name(package_name)
    key = (norm, version)
    if key in _requires_cache:
        return _requires_cache[key]
    url = f"https://pypi.org/pypi/{norm}/{version}/json"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read())
        reqs = data.get("info", {}).get("requires_dist") or []
    except Exception:
        reqs = []
    _requires_cache[key] = reqs
    return reqs


def dependency_upper_bound(reqs: list[str], target_norm: str) -> tuple | None:
    """Strictest '<X.Y.Z' bound any unconditional requirement in reqs places on
    target_norm, or None if there is no such bound."""
    bound = None
    for req in reqs:
        req = req.split(";", 1)[0].strip()  # drop environment markers/extras
        m = re.match(r"([A-Za-z0-9_.\-]+)\s*\(?([^)]*)\)?", req)
        if not m:
            continue
        name, spec = m.groups()
        if normalize_name(name) != target_norm:
            continue
        for part in spec.split(","):
            um = re.match(r"<\s*([0-9][\w.]*)", part.strip())
            if um:
                candidate = version_tuple(um.group(1))
                if bound is None or candidate < bound:
                    bound = candidate
    return bound


def load_packages(path: Path) -> dict:
    packages = {}
    for line in path.read_text().splitlines():
        parsed = parse_line(line)
        if parsed is None:
            continue
        raw_name, spec = parsed
        packages[normalize_name(raw_name)] = (raw_name, spec)
    return packages


def load_name_list(path: Path) -> set:
    """Return a set of normalized package names from a plain list file."""
    if not path.exists():
        return set()
    names = set()
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            names.add(normalize_name(line))
    return names


# ---------------------------------------------------------------------------
# Conflict resolution helpers
# ---------------------------------------------------------------------------

def get_available_venvs() -> list[tuple[str, str]]:
    """Return list of (version, venv_path) sorted ascending, for existing venvs."""
    result = []
    for ver in PYTHON_VERSIONS:
        venv = VENV_BASE / f"py{ver}"
        if venv.exists():
            result.append((ver, str(venv)))
    return result


def line_pkg_name(line: str) -> str:
    """Return the normalized package name from a requirement line (ignores markers)."""
    return normalize_name(re.split(r"[>=<;]", line)[0].strip())


def is_excluded_for_version(line: str, py_ver: str) -> bool:
    """Return True if the line's python_version marker excludes py_ver."""
    if ";" not in line:
        return False
    marker = line.split(";", 1)[1].strip()
    m = re.search(r'python_version\s*<\s*"([^"]+)"', marker)
    if m:
        limit = tuple(int(p) for p in m.group(1).split("."))
        current = tuple(int(p) for p in py_ver.split("."))
        return current >= limit
    return False


def active_candidates(lines: list[str], py_ver: str) -> set[str]:
    """Normalized names of lines NOT excluded by a python_version marker for py_ver."""
    return {
        line_pkg_name(line)
        for line in lines
        if not is_excluded_for_version(line, py_ver)
    }


def run_dry_install(lines: list[str], venv_path: str | None) -> subprocess.CompletedProcess:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("\n".join(lines) + "\n")
        tmp_path = f.name
    cmd = ["uv", "pip", "install", "--dry-run", "-r", tmp_path]
    if venv_path is not None:
        cmd[3:3] = ["--python", venv_path]
    try:
        return subprocess.run(cmd, capture_output=True, text=True)
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def find_conflict_package(error_output: str, candidates: set[str]) -> str | None:
    """Return the package from candidates most likely responsible for the conflict."""
    error_lower = error_output.lower()

    # Prefer packages named after "Because [only] <pkg>==" in uv output
    for m in re.finditer(r"because\s+(?:only\s+)?([a-z0-9][a-z0-9_\-]+)==", error_lower):
        pkg = normalize_name(m.group(1))
        if pkg in candidates:
            return pkg

    # Also check "Because <pkg>>=" form (e.g. "Because foo>=1.0 depends on bar")
    for m in re.finditer(r"because\s+([a-z0-9][a-z0-9_\-]+)>=", error_lower):
        pkg = normalize_name(m.group(1))
        if pkg in candidates:
            return pkg

    # Fallback: first occurrence of any candidate in the error text
    found = [(error_lower.find(pkg), pkg) for pkg in sorted(candidates) if pkg in error_lower]
    if found:
        return min(found)[1]

    return None


def resolve_conflicts(output_lines: list[str]) -> tuple[list[str], set[str]]:
    """
    Resolve dependency conflicts across all available Python venvs.

    Processing order (ascending Python version):
    - First venv failures → universal conflict; package removed and added to
      unstable set.
    - Later venv failures → version-specific; a ;python_version<"X.Y" marker
      is appended to the package entry so it is still available on older
      Pythons.

    Returns (resolved_lines, unstable_norms).
    """
    venvs = get_available_venvs()
    if not venvs:
        print("WARNING: no .venvs found; skipping conflict resolution")
        return output_lines, set()

    lines = list(output_lines)
    unstable: set[str] = set()

    for idx, (py_ver, venv_path) in enumerate(venvs):
        is_baseline = idx == 0

        for iteration in range(MAX_CONFLICT_ITERATIONS):
            result = run_dry_install(lines, venv_path)
            if result.returncode == 0:
                break

            candidates = active_candidates(lines, py_ver)
            error = result.stderr + result.stdout
            pkg = find_conflict_package(error, candidates)

            if pkg is None:
                print(f"WARNING: cannot identify conflict for Python {py_ver}:\n{error[:500]}")
                break

            if is_baseline:
                # Universal conflict — remove entirely
                print(f"Universal unstable: {pkg}")
                unstable.add(pkg)
                lines = [l for l in lines if line_pkg_name(l) != pkg]
            else:
                # Version-specific — add a python_version marker
                print(f"Python {py_ver}+ restricted: {pkg}")
                new_lines = []
                for line in lines:
                    if line_pkg_name(line) == pkg and ";" not in line:
                        line = f'{line};python_version<"{py_ver}"'
                    new_lines.append(line)
                lines = new_lines
        else:
            print(f"WARNING: hit iteration limit for Python {py_ver}")

    return lines, unstable


def validate_bumps(lines: list[str], bumped: dict[str, str]) -> list[str]:
    """Roll back any PyPI-stable floor bump that a package already pinned
    elsewhere in this same testing set declares an upper bound against.

    A raised floor is only useful if the rest of testing can still depend on
    it (e.g. bumping ovos-workshop past what the pinned ovos-core's own
    Requires-Dist allows produces a testing channel that conflicts with
    itself). This checks each *other* package's real PyPI metadata for its
    pinned floor release, rather than asking a resolver to solve the whole
    163-package graph, because several testing members (ovos-agentic-loop,
    at the time of writing) only publish releases that themselves depend on
    pre-release-only versions of something else -- a full-graph solve would
    reject those unrelated to any bump and make every bump look unsafe.
    """
    if not bumped:
        return lines

    pinned_floor: dict[str, str] = {}
    for line in lines:
        m = re.search(r">=\s*([^\s,;]+)", line)
        if m and not is_prerelease(m.group(1)):
            pinned_floor[line_pkg_name(line)] = m.group(1)

    result = list(lines)
    for target_norm, original_line in bumped.items():
        bumped_line = next(line for line in result if line_pkg_name(line) == target_norm)
        floor_match = re.search(r">=\s*([^\s,;]+)", bumped_line)
        new_floor = version_tuple(floor_match.group(1))
        capped_by = None
        for consumer_norm, consumer_floor in pinned_floor.items():
            if consumer_norm == target_norm:
                continue
            bound = dependency_upper_bound(get_requires_dist(consumer_norm, consumer_floor), target_norm)
            if bound is not None and new_floor >= bound:
                capped_by = consumer_norm
                break
        if capped_by:
            print(f"Reverting PyPI stable bump for {target_norm}: {capped_by} caps it below the bumped floor")
            result = [original_line if line_pkg_name(line) == target_norm else line for line in result]
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    alpha = load_packages(ALPHA_FILE)
    testing = load_packages(TESTING_FILE) if TESTING_FILE.exists() else {}
    stable = load_packages(STABLE_FILE) if STABLE_FILE.exists() else {}

    # --- packages dropped from alpha → deprecated ---
    deprecated_norm = set()
    if DEPRECATED_FILE.exists():
        for line in DEPRECATED_FILE.read_text().splitlines():
            parsed = parse_line(line)
            if parsed:
                deprecated_norm.add(normalize_name(parsed[0]))

    newly_deprecated = []
    for norm, (raw, _) in testing.items():
        if norm not in alpha and norm not in deprecated_norm:
            newly_deprecated.append(normalize_name(raw))
    for norm, (raw, _) in stable.items():
        if norm not in alpha and norm not in deprecated_norm and normalize_name(raw) not in newly_deprecated:
            newly_deprecated.append(normalize_name(raw))

    if newly_deprecated:
        with DEPRECATED_FILE.open("a") as f:
            for pkg in newly_deprecated:
                f.write(pkg + "\n")
        print(f"Deprecated ({len(newly_deprecated)}): {', '.join(newly_deprecated)}")

    # --- build candidate testing entries ---
    output_lines = []
    seen = set()
    bumped: dict[str, str] = {}  # norm -> original (pre-bump) requirement line

    for norm, (raw, spec) in testing.items():
        if norm not in alpha:
            continue  # dropped
        min_ver = parse_min_version(spec)
        alpha_min = parse_min_version(alpha[norm][1])
        if is_prerelease(min_ver) and is_prerelease(alpha_min):
            latest = get_latest_stable(raw)
            if latest is None:
                print(f"Skipped (no stable on PyPI): {normalize_name(raw)}")
                continue
            min_ver = latest
            print(f"PyPI stable found for {normalize_name(raw)}: >={min_ver}")
        elif is_prerelease(min_ver):
            min_ver = lower_prerelease_min(min_ver)
        else:
            # Already pinned to a stable release; a newer stable one may have
            # published on PyPI since testing was last synced. Raise the
            # floor as a candidate; validate_bumps() below reverts it if the
            # rest of testing cannot actually resolve with it.
            latest = get_latest_stable(raw)
            if latest is not None and version_tuple(latest) > version_tuple(min_ver):
                print(f"PyPI stable bump candidate for {normalize_name(raw)}: {min_ver} -> {latest}")
                upper = next_major_upper_bound(alpha_min)
                bumped[normalize_name(raw)] = f"{normalize_name(raw)}>={min_ver},{upper}"
                min_ver = latest
        seen.add(norm)
        upper = next_major_upper_bound(alpha_min)
        output_lines.append(f"{normalize_name(raw)}>={min_ver},{upper}")

    # --- revert any PyPI-stable floor bump the rest of already-testing-pinned
    # packages can't satisfy, before packages new to this run get a chance to
    # introduce unrelated conflicts (e.g. a missing wheel for some other
    # platform) that would otherwise mask or get blamed for a real one ---
    output_lines = validate_bumps(output_lines, bumped)

    for norm, (raw, spec) in alpha.items():
        if norm in seen:
            continue
        alpha_min = parse_min_version(spec)
        if is_prerelease(alpha_min):
            latest = get_latest_stable(raw)
            if latest is None:
                print(f"Skipped new (no stable on PyPI): {normalize_name(raw)}")
                continue
            alpha_min = latest
            print(f"PyPI stable found for new {normalize_name(raw)}: >={alpha_min}")
        upper = next_major_upper_bound(alpha_min)
        output_lines.append(f"{normalize_name(raw)}>={alpha_min},{upper}")
        print(f"Added: {normalize_name(raw)}>={alpha_min},{upper}")

    # --- auto-detect and resolve dependency conflicts across all Python versions ---
    output_lines, auto_unstable = resolve_conflicts(output_lines)

    # Regenerate unstable.list from auto-detected set (reproducible)
    UNSTABLE_FILE.parent.mkdir(parents=True, exist_ok=True)
    if auto_unstable:
        UNSTABLE_FILE.write_text("\n".join(sorted(auto_unstable)) + "\n")
        print(f"unstable.list ({len(auto_unstable)}): {', '.join(sorted(auto_unstable))}")
    else:
        UNSTABLE_FILE.write_text("")

    TESTING_FILE.write_text("\n".join(output_lines) + "\n")
    print(f"Written {len(output_lines)} entries to {TESTING_FILE}")

    # --- sanity check against stable: warn only, never fail the sync ---
    new_testing = load_packages(TESTING_FILE)
    for norm, (raw, spec) in stable.items():
        if norm not in new_testing:
            if norm in auto_unstable:
                continue  # deliberate exclusion, not staleness -- nothing to warn about
            print(f"WARNING: {normalize_name(raw)} is in stable but missing from testing")
            continue
        stable_floor = version_tuple(parse_min_version(spec))
        testing_floor = version_tuple(parse_min_version(new_testing[norm][1]))
        if testing_floor < stable_floor:
            print(
                f"WARNING: {normalize_name(raw)} testing floor {'.'.join(map(str, testing_floor))} "
                f"is below stable floor {'.'.join(map(str, stable_floor))}"
            )


if __name__ == "__main__":
    sys.exit(main())
