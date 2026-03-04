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
- [Maintainer's Guide](MAINTAINERS.md)

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

See [MAINTAINERS.md](MAINTAINERS.md) for the full maintainer documentation covering the release workflow, scripts, and conventions used to manage this repository.
