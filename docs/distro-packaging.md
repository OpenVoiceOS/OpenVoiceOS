# Guide for Distro Packagers

Thank you. Every distro that ships OVOS helps grow the ecosystem and puts open, private voice AI into the hands of more people. Packaging and maintaining software for a distribution takes real effort, and we want to make it as easy as possible.

This document collects practical advice for packaging OVOS for Linux distributions (Debian/Ubuntu, Fedora/RHEL, Arch, NixOS, Alpine, and others) or for embedding it in a custom OS image.

## Which channel to use

> **Note:** OVOS codename releases have not landed yet. The formal stable/testing/alpha split described in [release-channels.md](release-channels.md) is the target model. The current state of each channel reflects where the project is in that transition.

**Right now, `constraints-stable.txt` reflects an older, unmaintained snapshot.** It is not "stable" in the sense of being the most polished or actively supported version. It becomes meaningful once the first codename release is cut.

Until then, use the channel that matches your distro's update model:

| Distro model | Recommended channel | Constraints file |
|---|---|---|
| Rolling release | **Alpha** | `--pre` (no constraints file needed, or use `constraints-alpha.txt`) |
| Fixed / point release | **Testing** | `constraints-testing.txt` |
| *(future)* Pinned to a codename | Stable | `constraints-stable.txt` |

**Testing is the recommended channel for most distros today.** It tracks packages that have a stable PyPI release. It passes conflict detection across Python 3.10 to 3.14. It gets regular updates as new features land. It is the closest thing to "production-ready" OVOS until codename releases begin.

```
https://raw.githubusercontent.com/OpenVoiceOS/ovos-releases/main/constraints-testing.txt
```

Rolling-release distros (Arch, NixOS unstable, and similar) are a natural fit for the alpha channel, which tracks the latest published versions with no upper bound.

## Pin to a named release, not `main`

Once codename releases begin, use the versioned constraints file URL rather than the `main` branch. This stops your package from silently picking up constraint changes after your QA cycle is done.

> Named releases and their tags are announced in [ovos-releases](https://github.com/OpenVoiceOS/ovos-releases/issues/5). Watch that issue to be notified when the first one lands.

## Install only what your target needs

OVOS is modular. Resist the temptation to install everything. A minimal install is easier to audit, has a smaller attack surface, and starts faster.

A good baseline for a headless voice assistant:
```
ovos-core[mycroft,plugins,skills-essential]
```

Add extras deliberately:
- `skills-gui` only if you ship a display and a GUI client (for example ovos-shell)
- `skills-internet` only if your target has reliable internet access
- `skills-media` only if you ship OCP / media playback
- `lgpl` only if you explicitly want Padatious intent parsing

See [installation.md](installation.md) for the full extras reference.

## Use a virtualenv or isolated prefix

OVOS has a large dependency tree. Installing it into the system Python (`/usr/lib/python3/`) risks conflicts with other system packages. We recommend one of:

- A dedicated virtualenv under `/opt/ovos/` or `/usr/lib/ovos/`
- A `--prefix` install into an isolated path
- A container or systemd-nspawn image

This also keeps upgrades clean: replace the venv rather than upgrade in place.

## Ship systemd service units

Each OVOS service is a long-running process. Systemd units make them manageable and observable. The upstream repos include example units under `systemd/` in the relevant repositories. We recommend:

- `ovos-messagebus.service` — start first, required by all others
- `ovos-core.service` — depends on messagebus
- `ovos-dinkum-listener.service` — depends on core
- `ovos-audio.service` — depends on core
- `ovos-gui.service` — depends on core (only if shipping GUI)
- `ovos-PHAL.service` — depends on core (only if hardware abstraction is needed)

Use `After=` and `Requires=` to express the dependency order. All services connect through the messagebus, so if the bus is down, everything waits.

## Configuration paths

OVOS follows XDG conventions when running as a regular user:

| Purpose | Default path |
|---|---|
| User config | `~/.config/mycroft/mycroft.conf` |
| System config | `/etc/mycroft/mycroft.conf` |
| Data / models | `~/.local/share/mycroft/` |
| Log files | `~/.local/state/mycroft/` (or journald via systemd) |

For a system-wide installation running as a dedicated service user (for example `ovos`), set `$XDG_CONFIG_HOME`, `$XDG_DATA_HOME`, and `$XDG_STATE_HOME` in the unit's `[Service]` section to point to appropriate system paths like `/etc/ovos/`, `/var/lib/ovos/`, and `/var/log/ovos/`.

## Avoid bundling conflicting packages

A few common system packages conflict with OVOS dependencies if both are installed into the same Python environment:

- `python3-mycroft-*` — legacy Mycroft packages use the same namespace as some OVOS packages
- Very old versions of `pydantic`, `aiohttp`, or `click` installed system-wide

If you must install into the system Python, check [conflicts.md](conflicts.md) in this repo for known problem packages, and test with `pip check` after install.

## Test before shipping

Run a basic sanity check after building your package:

```bash
python -c "import ovos_core; print(ovos_core.__version__)"
pip check   # should report no conflicts
```

For a more thorough test, start the messagebus and core in a throw-away environment and verify they connect:

```bash
ovos-messagebus &
ovos-core &
# wait a few seconds, then check logs for "Connected to messagebus"
```

## Keeping up with releases

- **Watch this repository** for constraint file updates. `constraints-testing.txt` is updated regularly through automated CI.
- Subscribe to [ovos-releases#5](https://github.com/OpenVoiceOS/ovos-releases/issues/5) to be notified when the first codename release lands. That is the signal to start pinning to versioned constraints files.
- [conflicts.md](conflicts.md) is updated weekly and is a useful signal for packages you should hold back or avoid.

## Tell us you're shipping OVOS

We would like to know about your distro. Open an issue or start a discussion in [ovos-core](https://github.com/OpenVoiceOS/ovos-core/discussions) and let us know. We can:

- Link to your distro from our documentation
- Notify you early about breaking changes
- Help with packaging questions

## Getting help

- **Matrix / Element**: [#OpenVoiceOS:matrix.org](https://matrix.to/#/#OpenVoiceOS:matrix.org), the most active community channel
- **GitHub Discussions**: [ovos-core discussions](https://github.com/OpenVoiceOS/ovos-core/discussions)
- **Issues**: Open issues in the specific component repo you have trouble with

We are a friendly community and happy to help distro packagers get things right. Thank you again for your work.

---
[← Versioning](versioning.md) · [Home](README.md) · [Maintainers →](maintainers.md)
