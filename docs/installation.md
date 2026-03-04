# Installing OVOS with pip

This guide covers manual pip installation. If you just want to get started quickly, use a [distro](../README.md#get-started-in-minutes) instead.

## Prerequisites

- Python 3.10 or newer
- pip 22+

## Basic install

```bash
pip install ovos-core[mycroft,plugins,skills-essential] -c constraints-stable.txt
```

This gives you a working voice assistant with all core services, common plugins, and the essential built-in skills.

## Choosing a release channel

Always pass a constraints file to ensure compatible versions are selected. See [release-channels.md](release-channels.md) for details.

| Channel | Constraints flag |
|---|---|
| Stable | `-c constraints-stable.txt` |
| Testing | `-c constraints-testing.txt` |
| Alpha | `--pre` (no constraints file needed) |

You can use raw URLs instead of local files:

```bash
pip install ovos-core[mycroft] -c https://raw.githubusercontent.com/OpenVoiceOS/ovos-releases/main/constraints-stable.txt
```

## OVOS Extras

OVOS uses pip "extras" to let you install only what you need. Pass them in square brackets after the package name.

| Extra | What it installs |
|---|---|
| `mycroft` | All core services as separate processes (listener, audio, GUI, PHAL, messagebus) |
| `lgpl` | Optional LGPL-licensed dependencies, e.g. [Padatious](https://github.com/MycroftAI/padatious) intent parser |
| `plugins` | A broad set of community plugins for STT, TTS, wake word, etc. |
| `skills-essential` | Core built-in skills (date/time, volume, settings, etc.) |
| `skills-audio` | Skills that produce or require audio |
| `skills-gui` | Skills that use the OVOS GUI framework |
| `skills-internet` | Skills that require an internet connection |
| `skills-media` | OCP (OpenVoiceOS Common Play) media playback skills |
| `skills-desktop` | Desktop integration skills |

### Common recipes

**Minimal headless assistant** (no GUI, no internet skills):
```bash
pip install ovos-core[mycroft,plugins,skills-essential]
```

**Full desktop assistant**:
```bash
pip install ovos-core[mycroft,plugins,skills-essential,skills-gui,skills-internet,skills-desktop]
```

**Media-focused device**:
```bash
pip install ovos-core[mycroft,plugins,skills-essential,skills-media,skills-audio]
```

**Everything**:
```bash
pip install ovos-core[mycroft,lgpl,plugins,skills-essential,skills-audio,skills-gui,skills-internet,skills-media,skills-desktop]
```

## Installing individual services

You don't have to use the `mycroft` extra. You can install each OVOS service separately and run them independently. This is useful if you're building a custom setup, a HiveMind satellite, or want to keep the footprint small.

```bash
pip install ovos-messagebus        # message bus (required by all services)
pip install ovos-core              # skill and intent handling
pip install ovos-dinkum-listener   # microphone, wake word, STT
pip install ovos-audio             # TTS and audio output
pip install ovos-gui               # GUI service
pip install ovos-PHAL              # hardware abstraction
```

Each package has its own configuration and can be started independently as a systemd service or process.

## Verifying the install

After installing, confirm the core service is available:

```bash
python -c "import ovos_core; print(ovos_core.__version__)"
```

To start all services at once (if using the `mycroft` extra):

```bash
ovos-core
```

Or start services individually:

```bash
ovos-messagebus &
ovos-core &
ovos-dinkum-listener &
ovos-audio &
```
