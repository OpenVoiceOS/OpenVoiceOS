# Release Channels

OVOS follows [semantic versioning](https://semver.org/) (SemVer) and a rolling release model with three channels: **stable**, **testing**, and **alpha**.

The channels are managed through [pip constraints files](https://pip.pypa.io/en/stable/user_guide/#constraints-files) hosted in this repository. A constraints file restricts which package versions pip is allowed to install — it does not install anything on its own.

## Channels at a glance

| Channel | File | Who it's for |
|---|---|---|
| **Stable** | `constraints-stable.txt` | Most users — production use |
| **Testing** | `constraints-testing.txt` | Early adopters — want new features without going fully bleeding-edge |
| **Alpha** | `constraints-alpha.txt` / `--pre` | Developers and testers |

## Stable

- Contains **bug fixes only** — no new features, no breaking changes.
- Versions are pinned to patch-level ranges (`>=X.Y.Z,<X.(Y+1).0`), meaning only patch upgrades are allowed.
- Safe for daily use and production deployments.

```bash
pip install ovos-core[mycroft] -c constraints-stable.txt
```

## Testing

- Contains **bug fixes and new features**, roughly equivalent to a release candidate.
- Versions are pinned to major-version ranges (`>=X.Y.Z,<(X+1).0.0`), meaning any non-breaking upgrade within the current major is allowed.
- Packages with unresolved dependency conflicts are excluded (see `lists/unstable.list`).
- Suitable for users who want the latest features and are comfortable with occasional rough edges.

```bash
pip install ovos-core[mycroft] -c constraints-testing.txt
```

## Alpha

- Contains the **latest published pre-release** versions.
- Versions are lower-bounded only (`>=X.Y.Z`), with no upper cap.
- May include breaking changes, unfinished features, or known bugs.
- Requires `--pre` so pip considers pre-release versions.

```bash
pip install ovos-core[mycroft] --pre
```

Or with the alpha constraints file for tighter lower bounds:

```bash
pip install ovos-core[mycroft] --pre -c constraints-alpha.txt
```

## How channels are updated

- **Alpha** is updated frequently, often automatically, as new pre-releases are published to PyPI.
- **Testing** is synced from alpha using [`make_alpha_testing.py`](../make_alpha_testing.py), which promotes packages only once a stable release exists and no dependency conflicts are detected.
- **Stable** is updated during formal named releases (codename releases).

See [docs/maintainers.md](maintainers.md) for the full release workflow.

## What is `lists/unstable.list`?

Some packages are excluded from the testing and stable channels because they introduce dependency conflicts with other OVOS packages. These are listed in `lists/unstable.list` and tracked in [`docs/conflicts.md`](conflicts.md).

A package on this list is not broken — it just can't coexist with the current dependency graph. It will be re-evaluated automatically on each testing sync and re-added when the conflict is resolved upstream.
