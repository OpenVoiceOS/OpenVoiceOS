# Versioning and Commit Conventions

All OVOS repositories follow **Semantic Versioning** and **Conventional Commits**. These two standards are the foundation of the automated release pipeline that keeps dozens of packages in sync without manual bookkeeping.

## Semantic Versioning (SemVer)

Every OVOS package version is `MAJOR.MINOR.PATCH`:

| Segment | When it changes | What it means |
|---|---|---|
| `MAJOR` | Breaking changes | Users or downstream code must adapt |
| `MINOR` | New features, backwards-compatible | Safe to upgrade, new things available |
| `PATCH` | Bug fixes only | Safe to upgrade, nothing new |

Pre-release versions use the `aN` suffix (for example `1.2.0a1`). These land in the **alpha** channel and are gated from testing and stable until a final release is cut.

### Why this matters for the release channels

The version ranges in the constraints files come directly from SemVer:

| Channel | Version range | Reasoning |
|---|---|---|
| Stable | `>=X.Y.Z,<X.(Y+1).0` | Only patch upgrades, no new features, no risk |
| Testing | `>=X.Y.Z,<(X+1).0.0` | New features allowed, no breaking changes |
| Alpha | `>=X.Y.Z` | No upper cap, take everything including pre-releases |

A correctly versioned release lands in the right channel automatically. A `PATCH` bump is safe for stable. A `MINOR` bump flows to testing. A `MAJOR` bump requires explicit action and human review before it propagates downstream.

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
| `refactor` | Code restructuring, no behavior change | No version bump |
| `test` | Adding or fixing tests | No version bump |
| `ci` | CI/CD configuration | No version bump |
| `perf` | Performance improvement | No version bump |

The `!` after the type (for example `feat!:`, `fix!:`) signals a breaking change when the change would otherwise look minor.

### Examples

```
feat(tts): add support for VITS engine
```
This is a MINOR bump. It flows to the testing channel.

```
fix(listener): handle empty VAD frames without crashing
```
This is a PATCH bump. It flows to the stable channel.

```
feat!: remove deprecated mycroft-core compatibility shim
```
This is a MAJOR bump. It is held at alpha until manually promoted.

```
chore(deps): update ovos-bus-client to 0.1.2
```
This triggers no version bump and no release.

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

No human has to decide which version number to assign or which channel a release belongs to. The commit message carries that information from the moment the code is written.

## Applying this in your own plugin or skill

If you write an OVOS plugin or skill and want it to participate in the constraints pipeline:

1. Use Conventional Commits in your repository.
2. Set up automated releases (for example with [release-please](https://github.com/googleapis/release-please) or a similar tool) so that merging to `main` publishes to PyPI automatically.
3. Open a PR to add your package to the appropriate `lists/*.list` file in this repository.
4. Once added, the automation handles promotion between channels.

The OVOS core team is happy to help. See the community links in the [main README](../README.md).

---
[← Release channels](release-channels.md) · [Home](README.md) · [Distro packaging →](distro-packaging.md)
