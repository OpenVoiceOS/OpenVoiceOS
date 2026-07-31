# OpenVoiceOS

**OpenVoiceOS (OVOS)** is a free, open-source, privacy-respecting voice assistant platform. Run it on a Raspberry Pi, a desktop, or a server, fully offline if you want, and fully customizable.

> **New here?** The fastest way to get started is with a pre-built distro below. No manual setup is required.

---

## Get Started in Minutes

OVOS distros are ready-to-use bundles with everything pre-configured for specific hardware or platforms:

| Distro | Best for |
|---|---|
| [**ovos-installer**](https://github.com/OpenVoiceOS/ovos-installer) | **Recommended**: any Linux machine, interactive install script |
| [**raspOVOS**](https://github.com/OpenVoiceOS/raspOVOS) | Raspberry Pi image *(may lag behind the latest release)* |
| [**ovos-buildroot**](https://github.com/OpenVoiceOS/ovos-buildroot) | The original OVOS image, on hiatus but not abandoned, with a comeback planned |

ovos-installer is the reference distro and the best supported path for new users. raspOVOS is a convenient Pi image, but it does not always track the latest OVOS release.

Pick one, follow its README, and you have a working voice assistant without touching anything in this repository.

---

## Install Manually with pip

If you prefer to manage your own Python environment, you can install OVOS directly with pip.

**Recommended starting point**: a full local voice assistant.

```bash
pip install ovos-core[mycroft,plugins,skills-essential] -c https://raw.githubusercontent.com/OpenVoiceOS/ovos-releases/main/constraints-stable.txt
```

**Everything included**: the kitchen-sink install.

```bash
pip install ovos-core[mycroft,lgpl,plugins,skills-essential,skills-audio,skills-gui,skills-internet,skills-media,skills-desktop] -c https://raw.githubusercontent.com/OpenVoiceOS/ovos-releases/main/constraints-stable.txt
```

The `-c` flag pins all OVOS packages to tested, compatible versions from the **stable** release channel.

> Want to understand what `mycroft`, `plugins`, `skills-*` and other options mean?
> See [docs/installation.md](docs/installation.md) for the full breakdown.

---

## Release Channels

| Channel | Stability | How to use |
|---|---|---|
| **Stable** | Production-ready, patch fixes only | Add `-c constraints-stable.txt` |
| **Testing** | New features, well-tested | Add `-c constraints-testing.txt` |
| **Alpha** | Bleeding edge, may break | Add `--pre` |

Details: [docs/release-channels.md](docs/release-channels.md)

---

## Build Your Own Stack

OVOS is modular. Install only the services you need:

| Service | What it does |
|---|---|
| [ovos-messagebus](https://github.com/OpenVoiceOS/ovos-messagebus) | Message bus, the backbone connecting all services |
| [ovos-core](https://github.com/OpenVoiceOS/ovos-core) | Skill handling and intent processing |
| [ovos-dinkum-listener](https://github.com/OpenVoiceOS/ovos-dinkum-listener) | Microphone, wake word, speech-to-text |
| [ovos-audio](https://github.com/OpenVoiceOS/ovos-audio) | Text-to-speech and audio output |
| [ovos-gui](https://github.com/OpenVoiceOS/ovos-gui) | GUI support for touchscreens and displays |
| [ovos-PHAL](https://github.com/OpenVoiceOS/ovos-PHAL) | Hardware abstraction (LEDs, buttons, and more) |

For example, a [HiveMind](https://github.com/JarbasHiveMind) satellite only needs the listener. No audio stack is required.

---

## Community & Support

- **Docs**: [ovos-technical-manual](https://openvoiceos.github.io/ovos-technical-manual/)
- **Chat**: [Matrix / Element](https://matrix.to/#/#openvoiceos:matrix.org)
- **Forum**: [GitHub Discussions](https://github.com/orgs/OpenVoiceOS/discussions)
- **Issues**: Open an issue in the relevant component repository

---

## This Repository

This repo hosts the **constraints files**, version-pinning files that ensure all OVOS packages install together without conflicts. You do not need to clone or understand this repo to use OVOS. It is used automatically when you pass `-c constraints-*.txt` to pip.

- [docs/installation.md](docs/installation.md): pip extras, channels, and install recipes
- [docs/release-channels.md](docs/release-channels.md): how stable/testing/alpha work
- [docs/versioning.md](docs/versioning.md): semantic versioning and conventional commits across OVOS repos
- [docs/distro-packaging.md](docs/distro-packaging.md): guide for distros and system packagers shipping OVOS
- [docs/maintainers.md](docs/maintainers.md): how to maintain and release new constraint files
