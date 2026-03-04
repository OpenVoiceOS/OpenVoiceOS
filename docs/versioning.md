# Versioning and Commit Conventions

All OVOS repositories follow **Semantic Versioning** and **Conventional Commits**. This isn't just style — these two standards are the foundation of the automated release pipeline that keeps dozens of packages in sync without manual bookkeeping.

---

## Semantic Versioning (SemVer)

Every OVOS package version is `MAJOR.MINOR.PATCH`:

| Segment | When it changes | What it means |
|---|---|---|
| `MAJOR` | Breaking changes | Users or downstream code must adapt |
| `MINOR` | New features, backwards-compatible | Safe to upgrade, new things available |
| `PATCH` | Bug fixes only | Safe to upgrade, nothing new |

Pre-release versions use the `aN` suffix (e.g. `1.2.0a1`). These land in the **alpha** channel and are gated from testing/stable until a final release is cut.

### Why this matters for the release channels

The version ranges in the constraints files are derived directly from SemVer:

| Channel | Version range | Reasoning |
|---|---|---|
| Stable | `>=X.Y.Z,<X.(Y+1).0` | Only patch upgrades — no new features, no risk |
| Testing | `>=X.Y.Z,<(X+1).0.0` | New features allowed, no breaking changes |
| Alpha | `>=X.Y.Z` | No upper cap — take everything including pre-releases |

This means a correctly versioned release automatically lands in the right channel. A `PATCH` bump is safe for stable; a `MINOR` bump flows to testing; a `MAJOR` bump requires explicit action and human review before propagating downstream.

---

## Conventional Commits

All commits across OVOS repositories use the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>[(scope)][!]: <short description>

[optional body]

[optional footer]
```

### Commit types

| Type | What it signals | SemVer impact |
|---|---|---|
| `fix` | A bug fix | `PATCH` bump |
| `feat` | A new feature | `MINOR` bump |
| `feat!` or `BREAKING CHANGE:` footer | A breaking change | `MAJOR` bump |
| `chore` | Maintenance, dependency updates | No version bump |
| `docs` | Documentation only | No version bump |
| `refactor` | Code restructuring, no behaviour change | No version bump |
| `test` | Adding or fixing tests | No version bump |
| `ci` | CI/CD configuration | No version bump |
| `perf` | Performance improvement | No version bump |

The `!` after the type (e.g. `feat!:`, `fix!:`) is the conventional way to signal a breaking change when the change would otherwise look minor.

### Examples

```
feat(tts): add support for VITS engine
```
→ MINOR bump, flows to testing channel.

```
fix(listener): handle empty VAD frames without crashing
```
→ PATCH bump, flows to stable channel.

```
feat!: remove deprecated mycroft-core compatibility shim
```
→ MAJOR bump, held at alpha until manually promoted.

```
chore(deps): update ovos-bus-client to 0.1.2
```
→ No version bump, no release triggered.

---

## How it all connects

The combination of SemVer and Conventional Commits enables a fully automated flow:

```
commit pushed
    │
    ▼
CI reads commit type
    │
    ├─ fix/chore/docs/etc ──► patch release (or no release)
    ├─ feat              ──► minor release
    └─ feat! / BREAKING  ──► major release
                                │
                                ▼
                        pre-release (aN) published to PyPI
                                │
                                ▼
                        lands in constraints-alpha.txt
                                │
                                ▼
                    make_alpha_testing.py promotes to testing
                    once stable release exists + no conflicts
                                │
                                ▼
                    formal codename release ──► constraints-stable.txt
```

No human has to decide which version number to assign or which channel a release belongs to — the commit message carries that information from the moment the code is written.

---

## Applying this in your own plugin or skill

If you're writing an OVOS plugin or skill and want it to participate in the constraints pipeline:

1. Use Conventional Commits in your repository.
2. Set up automated releases (e.g. with [release-please](https://github.com/googleapis/release-please) or a similar tool) so that merging to `main` publishes to PyPI automatically.
3. Open a PR to add your package to the appropriate `lists/*.list` file in this repository.
4. Once added, the automation handles promotion between channels.

The OVOS core team is happy to help — see the community links in the [main README](../README.md).
