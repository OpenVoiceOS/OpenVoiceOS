# OVOS Constraints and Release Channels

OVOS is a **modular** system, meaning that you don’t have to install all of its components. Depending on your needs, you can install only the specific modules you want, saving both space and dependencies. The different components of OVOS are grouped into **extras** — optional feature sets that you can choose to install.

> ⚠️ this repository only enters in effect after the first [codename release](https://github.com/OpenVoiceOS/ovos-releases/issues/5), constraints files are a work in progress and subject to change

## Table of Contents

- [Distros](#distros)
- [Release Channels](#release-channels)
- [Installation Commands for Each Channel](#installation-commands-for-each-channel)
- [OVOS from Scratch](#ovos-from-scratch)
- [What are OVOS Extras?](#what-are-ovos-extras)
- [Summary](#summary)
- [Maintainer's Guide](#maintainers-guide)

### Distros

OVOS distros are projects that ship OVOS, but that are opinionated about which components and skills should be available by default and pre-configured.

- [**raspOVOS**](https://github.com/OpenVoiceOS/raspOVOS) - rasperry pi image
- [**ovos-installer**](https://github.com/OpenVoiceOS/ovos-installer) - install OVOS on top of multiple OS
- [**ovos-buildroot**](https://github.com/OpenVoiceOS/ovos-buildroot) - under development

These distros provide an easier way to get started with OVOS on specific hardware or platforms. The configurations come pre-set with commonly used services, making it quicker to deploy OVOS on different devices.

### Release Channels

OVOS follows [**semantic versioning**](https://semver.org/) (SemVer) and a **rolling release model** with three primary release channels: **stable**, **testing**, and **alpha**.

These channels are managed via the [constraints files](https://pip.pypa.io/en/stable/user_guide/#constraints-files) hosted in this repository

> ℹ️ constraints files are similar to `requirements.txt`, but they specify *allowed versions* instead of *required versions*, packages in constraints files are not automatically installed

1. **Stable Channel**
   - The **stable** release channel includes **only bug fixes**, no breaking changes or new features. It’s safe for general use.
   - **Installation**: Use the `constraints-stable.txt` file to install the stable releases.

2. **Testing Channel**
   - The **testing** release channel includes **bug fixes and new features**, but it may not be as thoroughly tested as the stable releases.
   - **Installation**: Use the `constraints-testing.txt` file to install the testing releases.

3. **Alpha Channel**
   - The **alpha** channel includes the latest experimental features that are **still in development**. These are not recommended for production use.
   - **Installation**: Use the `--pre` flag to install alpha releases.



### Installation Commands for Each Channel

#### Stable Release Installation

To install the stable release with the desired extras, use:

```bash
pip install ovos-core[mycroft] -c constraints-stable.txt
```

#### Testing Release Installation

To install the testing release with the desired extras, use:

```bash
pip install ovos-core[mycroft] -c constraints-testing.txt
```

#### Alpha Release Installation

To install the latest alpha release with the desired extras, use:

```bash
pip install ovos-core[mycroft] --pre
```

### OVOS from scratch

Instead of using distros you can costumize OVOS by manually installing only select services relevant to your use case

- **[messagebus](https://github.com/OpenVoiceOS/ovos-messagebus)** - provides a communication layer between all services
- **[core](https://github.com/OpenVoiceOS/ovos-core)** - handles anything related to skills
- **[audio](https://github.com/OpenVoiceOS/ovos-audio)** - handles anything related to audio output (TTS, sounds, music...)
- **[listener](https://github.com/OpenVoiceOS/ovos-dinkum-listener)** - handles anything related to audio input (WakeWord, VAD, STT...)
- **[gui](https://github.com/OpenVoiceOS/ovos-gui)** - provides UI information for GUI client apps (eg, ovos-shell)
- **[PHAL](https://github.com/OpenVoiceOS/ovos-PHAL)** - Platform/Hardware Abstraction Layer plugins

For example, if you're setting up a Hivemind server, you can omit the audio stack to save resources.


### What are OVOS Extras?

OVOS packages are divided into different **extras** that define the components you wish to install. Each extra is a group of related functionality, and you can choose which ones to install based on your use case. For example:

- **mycroft**: Includes all the individual services, equivalent to the Mycroft-core monolithic architecture (e.g., ovos-audio, ovos-dinkum-listener, ovos-gui, ovos-PHAL, ovos-messagebus).
- **lgpl**: Includes optional dependencies that are LGPL-licensed (e.g., Padatious).
- **plugins**: Includes various plugins for additional functionality.
- **skills-essential**: Includes essential skills.
- **skills-audio**: Includes skills that require audio input/output capabilities.
- **skills-gui**: Includes skills that require GUI.
- **skills-internet**: Includes skills that require internet connection.
- **skills-media**: Includes OCP skills (media playback).
- **skills-desktop**: Includes desktop-related skills.

For a **full installation** of OVOS with all the optional modules, you can use the following command:

```bash
pip install ovos-core[mycroft,lgpl,plugins,skills-essential,skills-audio,skills-gui,skills-internet,skills-media,skills-desktop]
```

However, **you don’t need to install everything**. You can customize your installation by selecting only the extras you need, depending on the features you want to use.

For example, if you want minimal functionality, you can install just those:

```bash
pip install ovos-core[mycroft,plugins,skills-essential]
```

This flexibility allows you to tailor the installation to your requirements, without unnecessary components.


### Summary

- **OVOS is modular**, and you can choose which components (extras) to install based on your needs.
- **Stable Channel**: Bug fixes only (use `constraints-stable.txt`).
- **Testing Channel**: Bug fixes and new features (use `constraints-testing.txt`).
- **Alpha Channel**: Latest experimental features (use `--pre`).
- Use the base command or customize your installation to fit your requirements by selecting only the necessary extras.

---

## Maintainer's Guide

This section documents the scripts, automations, and conventions used to maintain the constraints files in this repository.

### Repository Layout

```
ovos-releases/
├── lists/                        # Package input lists, organized by category
│   ├── core.list                 # Core OVOS services
│   ├── stt.list                  # Speech-to-text plugins
│   ├── tts.list                  # Text-to-speech plugins
│   ├── ww.list                   # Wake-word plugins
│   ├── vad.list                  # Voice activity detection
│   ├── skills.list               # Skills
│   ├── pipeline.list             # Intent pipeline plugins
│   ├── phal.list                 # PHAL plugins
│   ├── ocp.list                  # OCP (media) plugins
│   ├── gui.list                  # GUI-related packages
│   ├── hivemind.list             # HiveMind packages
│   ├── ... (other categories)
│   ├── deprecated.list           # Packages no longer tracked
│   └── unstable.list             # Packages excluded from testing/stable
├── gather_packages.sh            # Step 1 — resolve all lists into resolved-constraints.txt
├── release_alpha.py              # Step 2a — generate constraints-alpha.txt
├── release.py                    # Step 2b — generate constraints-stable.txt
├── release_testing.py            # Step 2c — generate constraints-testing.txt
├── make_alpha_testing.py         # Alternative Step 2 — sync testing from alpha (smarter)
├── test_constraints.sh           # Step 3 — validate a constraints file across Python versions
├── constraints-alpha.txt         # Generated output (do not edit manually)
├── constraints-stable.txt        # Generated output (do not edit manually)
├── constraints-testing.txt       # Generated output (do not edit manually)
└── renovate.json                 # Renovate bot configuration
```

### Package Lists (`lists/`)

Each `.list` file in `lists/` contains packages belonging to a functional category. Lines beginning with `#` are comments. Version specifiers are allowed and serve as **minimum-version hints** to help the dependency resolver avoid pulling in very old versions.

Example entry in `lists/core.list`:
```
ovos_core>=2.1.0
ovos-plugin-manager>=1.0.0
```

**`lists/deprecated.list`** — packages that have been removed from OVOS tracking. The `make_alpha_testing.py` script appends here automatically when a package disappears from alpha.

**`lists/unstable.list`** — packages explicitly excluded from `constraints-testing.txt` and `constraints-stable.txt`. Add a package here when it is known to be broken or not ready for testing/stable promotion.

### Step-by-Step Release Workflow

#### Prerequisites

- [`uv`](https://github.com/astral-sh/uv) must be installed (`pip install uv` or via the official installer).
- Python 3.10+ is required for the release scripts.

#### Step 1 — Resolve all packages

```bash
bash gather_packages.sh
```

This runs `uv pip compile --pre` over all the `lists/*.list` files, constrained by the current `constraints-alpha.txt` hosted on GitHub. The result is written to **`resolved-constraints.txt`** — a fully pinned snapshot of the entire OVOS dependency graph with exact `==` versions.

> This file is an intermediate artifact. It is not committed and should not be used directly for installation.

#### Step 2 — Generate constraints files

There are two approaches depending on context:

**Option A — Full regeneration from a fresh pip resolve**

Use this when doing a formal release from a freshly resolved environment:

```bash
python release_alpha.py    # writes constraints-alpha.txt
python release.py          # writes constraints-stable.txt
python release_testing.py  # writes constraints-testing.txt
```

All three scripts read `resolved-constraints.txt` and apply different version-range rules:

| Script | Output file | Version range logic |
|---|---|---|
| `release_alpha.py` | `constraints-alpha.txt` | `>=X.Y.Z` — lower bound only (includes `ovos-*` and `hivemind-*`) |
| `release_testing.py` | `constraints-testing.txt` | `>=X.Y.Z,<(X+1).0.0` — allows any non-breaking upgrade within the current major |
| `release.py` | `constraints-stable.txt` | `>=X.Y.Z,<X.(Y+1).0` — tight range, patch-level upgrades only; `onnxruntime` is pinned to `<=1.20.1` for Raspberry Pi compatibility |

**Option B — Sync testing from alpha (recommended for routine updates)**

```bash
python make_alpha_testing.py
```

This is the smarter, incremental approach. It reads `constraints-alpha.txt` and `constraints-testing.txt` and produces an updated `constraints-testing.txt` by:

- **Deprecating** packages that disappeared from alpha (appends them to `lists/deprecated.list` and drops them from testing).
- **Skipping** packages listed in `lists/unstable.list`.
- **Preserving** existing lower bounds from testing (avoiding regression), but updating upper bounds based on the new alpha version.
- **Lowering** pre-release lower bounds by one minor version so users on the previous minor still satisfy the constraint.
- **Querying PyPI** for a stable release when both alpha and testing lower bounds are pre-release — if no stable exists the package is skipped.
- **Adding** new packages that appear in alpha (only if they already have a stable PyPI release).

#### Step 3 — Validate

```bash
bash test_constraints.sh                        # tests constraints-testing.txt (default)
bash test_constraints.sh constraints-stable.txt # tests a specific file
```

This script creates isolated `uv` virtual environments for each supported Python version (3.10 – 3.15) under `.venvs/` and performs a dry-run install to verify there are no resolution conflicts. It prints `PASS`, `FAIL`, or `SKIP` for each version and exits non-zero if any version fails.

> Python versions that are not installed locally are automatically skipped.

#### Step 4 — Commit

Only the generated constraints files and any changes to `lists/` need to be committed. `resolved-constraints.txt` and `.venvs/` should not be committed.

```bash
git add constraints-alpha.txt constraints-stable.txt constraints-testing.txt lists/
git commit -m "Update constraints files"
```

### Adding a New Package

1. Find the appropriate category file under `lists/` (or create one if needed).
2. Add the package name, optionally with a minimum version hint:
   ```
   ovos-new-plugin>=0.1.0
   ```
3. Run the full workflow (Steps 1–3 above) to regenerate constraints files.

### Removing / Deprecating a Package

1. Delete the entry from the relevant `.list` file.
2. Run `make_alpha_testing.py` — it will automatically detect the removal and append the package to `lists/deprecated.list`.
3. Manually remove the package from `constraints-alpha.txt` if needed and re-run the workflow.

### Marking a Package as Unstable

If a package is temporarily broken or not ready for testing/stable:

1. Add its normalized name (lowercase, hyphens) to `lists/unstable.list`.
2. Re-run `make_alpha_testing.py` — the package will be skipped when building `constraints-testing.txt`.

### Renovate Bot

`renovate.json` configures [Renovate](https://docs.renovatebot.com/) to automatically open pull requests when dependencies for the github actions workflows defined in this repository have new versions available. 

### Constraints File Format Reference

| Channel | File | Version spec | Notes |
|---|---|---|---|
| Alpha | `constraints-alpha.txt` | `pkg>=X.Y.Z` | Minimum only; `--pre` flag required at install time |
| Testing | `constraints-testing.txt` | `pkg>=X.Y.Z,<(X+1).0.0` | Allows feature releases within current major |
| Stable | `constraints-stable.txt` | `pkg>=X.Y.Z,<X.(Y+1).0` | Patch-only upgrades |

These files are used as pip [constraints files](https://pip.pypa.io/en/stable/user_guide/#constraints-files): they restrict the versions pip is allowed to select but do not cause packages to be installed on their own.
