# Package Conflict Report

_Generated: 2026-03-16 10:08 UTC_

| | Count |
|---|---:|
| ✅ Conflicts resolved — re-run `make_alpha_testing.py` | 0 |
| ❌ Conflicts still broken | 8 |
| ⚠️ Python version restrictions | 2 |
| 🔖 Missing stable release on PyPI | 9 |

---

## 1. Dependency Conflicts

Packages in [`lists/unstable.list`](lists/unstable.list) excluded from `constraints-testing.txt`.

### ❌ Still Conflicting — action needed

**`ovos-solver-aiml-plugin>=0.0.2a2`**  
Would add: `ovos-solver-aiml-plugin>=0.0.1,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only ovos-audio-transformer-plugin-speechbrain-langdetect<=0.0.1
      is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 depends on
      ovos-plugin-manager>=2.1.1.
      And because ovos-solver-aiml-plugin==0.0.1 depends
      on ovos-plugin-manager>=0.0.26,<2.0.0 and only
      ovos-solver-aiml-plugin<=0.0.1 is available, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-solver-aiml-plugin>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-solver-aiml-plugin>=0.0.1, we can conclude that your requirements
      are unsatisfiable.

      hint: Pre-releases are available for `ovos-solver-aiml-plugin` in the
      requested range (e.g., 0.0.2a2), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-solver-rivescript-plugin>=0.0.2a2`**  
Would add: `ovos-solver-rivescript-plugin>=0.0.1,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only ovos-audio-transformer-plugin-speechbrain-langdetect<=0.0.1
      is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 depends on
      ovos-plugin-manager>=2.1.1.
      And because ovos-solver-rivescript-plugin==0.0.1
      depends on ovos-plugin-manager>=0.0.26,<2.0.0 and only
      ovos-solver-rivescript-plugin<=0.0.1 is available, we can conclude
      that ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-solver-rivescript-plugin>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-solver-rivescript-plugin>=0.0.1, we can conclude that your
      requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-solver-rivescript-plugin` in
      the requested range (e.g., 0.0.2a2), but pre-releases weren't enabled
      (try: `--prerelease=allow`)
```

**`ovos-stt-plugin-whisper-lm>=0.0.6a4`**  
Would add: `ovos-stt-plugin-whisper-lm>=0.0.5,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only ovos-audio-transformer-plugin-speechbrain-langdetect<=0.0.1
      is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 depends on
      ovos-plugin-manager>=2.1.1.
      And because ovos-stt-plugin-whisper-lm==0.0.5
      depends on ovos-plugin-manager>=1.0.0,<2.0.0 and only
      ovos-stt-plugin-whisper-lm<=0.0.5 is available, we can conclude
      that ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-stt-plugin-whisper-lm>=0.0.5 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-stt-plugin-whisper-lm>=0.0.5, we can conclude that your
      requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-stt-plugin-whisper-lm` in the
      requested range (e.g., 0.0.6a4), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-tts-plugin-ahotts>=0.1.2a2`**  
Would add: `ovos-tts-plugin-ahotts>=0.1.1,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only ovos-audio-transformer-plugin-speechbrain-langdetect<=0.0.1
      is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 depends on
      ovos-plugin-manager>=2.1.1.
      And because ovos-tts-plugin-ahotts==0.1.1 depends
      on ovos-plugin-manager>=1.0.0,<2.0.0 and only
      ovos-tts-plugin-ahotts<=0.1.1 is available, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-tts-plugin-ahotts>=0.1.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-tts-plugin-ahotts>=0.1.1, we can conclude that your requirements
      are unsatisfiable.

      hint: Pre-releases are available for `ovos-tts-plugin-ahotts` in the
      requested range (e.g., 0.1.2a2), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-tts-plugin-cotovia>=0.4.5a2`**  
Would add: `ovos-tts-plugin-cotovia>=0.4.3,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only ovos-audio-transformer-plugin-speechbrain-langdetect<=0.0.1
      is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 depends on
      ovos-plugin-manager>=2.1.1.
      And because ovos-tts-plugin-cotovia==0.4.3 depends
      on ovos-plugin-manager>=1.0.0,<2.0.0 and only
      ovos-tts-plugin-cotovia<=0.4.3 is available, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-tts-plugin-cotovia>=0.4.3 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-tts-plugin-cotovia>=0.4.3, we can conclude that your requirements
      are unsatisfiable.

      hint: Pre-releases are available for `ovos-tts-plugin-cotovia` in the
      requested range (e.g., 0.4.5a2), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-tts-plugin-edge-tts>=0.2.3a1`**  
Would add: `ovos-tts-plugin-edge-tts>=0.2.2,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only ovos-audio-transformer-plugin-speechbrain-langdetect<=0.0.1
      is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 depends on
      ovos-plugin-manager>=2.1.1.
      And because ovos-tts-plugin-edge-tts==0.2.2 depends
      on ovos-plugin-manager>=1.0.0,<2.0.0 and only
      ovos-tts-plugin-edge-tts<=0.2.2 is available, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-tts-plugin-edge-tts>=0.2.2 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-tts-plugin-edge-tts>=0.2.2, we can conclude that your requirements
      are unsatisfiable.

      hint: Pre-releases are available for `ovos-tts-plugin-edge-tts` in the
      requested range (e.g., 0.2.3a1), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-tts-plugin-google-tx>=1.0.4a5`**  
Would add: `ovos-tts-plugin-google-tx>=1.0.3,<2.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only ovos-audio-transformer-plugin-speechbrain-langdetect<=0.0.1
      is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 depends on
      ovos-plugin-manager>=2.1.1.
      And because ovos-tts-plugin-google-tx==1.0.3 depends
      on ovos-plugin-manager>=1.0.0,<2.0.0 and only
      ovos-tts-plugin-google-tx<=1.0.3 is available, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-tts-plugin-google-tx>=1.0.3 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-tts-plugin-google-tx>=1.0.3, we can conclude that your requirements
      are unsatisfiable.

      hint: Pre-releases are available for `ovos-tts-plugin-google-tx` in the
      requested range (e.g., 1.0.4a5), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-vad-plugin-noise>=0.1.3a2`**  
Would add: `ovos-vad-plugin-noise>=0.1.2,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only ovos-audio-transformer-plugin-speechbrain-langdetect<=0.0.1
      is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 depends on
      ovos-plugin-manager>=2.1.1.
      And because ovos-vad-plugin-noise==0.1.2 depends
      on ovos-plugin-manager>=0.0.11,<2.0.0 and only
      ovos-vad-plugin-noise<=0.1.2 is available, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-vad-plugin-noise>=0.1.2 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect>=0.0.1 and
      ovos-vad-plugin-noise>=0.1.2, we can conclude that your requirements
      are unsatisfiable.

      hint: Pre-releases are available for `ovos-vad-plugin-noise` in the
      requested range (e.g., 0.1.3a2), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

---

## 2. Python Version Restrictions

Present in testing but excluded on newer Python via `; python_version < "X.Y"` marker.
**Action:** update the transitive dependency to publish wheels for the excluded versions.

| Package | Alpha version | Supported | Excluded |
|---------|:-------------:|-----------|----------|
| `ovos-tts-plugin-nos` |  | 3.10, 3.11, 3.12, 3.13 | 3.14, 3.15 |
| `ovos-ww-plugin-openwakeword` | 0.4.1 | 3.10, 3.11 | 3.12, 3.13, 3.14, 3.15 |

---

## 3. No Stable Release on PyPI

Exist in alpha as a pre-release; absent from testing because no stable version is available.
**Action:** cut a stable (non-pre-release) release.

| Package | Alpha version | Latest stable |
|---------|:-------------:|:-------------:|
| `ovos-google-translate-plugin` | 0.0.0a2 | — |
| `ovos-lang-detector-classics-plugin` | 0.0.1a1 | — |
| `ovos-media-plugin-mplayer` | 0.1.0a3 | — |
| `ovos-media-plugin-qt5` | 0.1.0a2 | — |
| `ovos-media-plugin-simple` | 0.0.2a5 | — |
| `ovos-media-plugin-vlc` | 0.1.0a4 | — |
| `ovos-stt-plugin-azure` | 0.0.0a2 | — |
| `ovos-tts-plugin-beepspeak` | 0.0.1a1 | — |
| `ovos-tts-plugin-matxa-multispeaker-cat` | 0.0.1a5 | — |

---

## 4. Resolved Package Snapshots

Exact versions uv would install for each constraints file (Python 3.10, transitive deps included).

<details>
<summary><strong>Alpha</strong> (constraints-alpha.txt) — 166 packages</summary>

| Package | Version |
|---------|---------|
| `hivemind-audio-binary-protocol` | 2.1.5 |
| `hivemind-bus-client` | 0.4.6a1 |
| `hivemind-core` | 4.0.0 |
| `hivemind-http-protocol` | 0.0.2a2 |
| `hivemind-plugin-manager` | 0.4.0 |
| `hivemind-redis-database` | 0.0.2 |
| `hivemind-websocket-protocol` | 0.0.4a1 |
| `ovos-adapt-parser` | 1.0.9 |
| `ovos-audio` | 1.2.1a1 |
| `ovos-audio-plugin-mpv` | 0.2.1 |
| `ovos-audio-plugin-simple` | 0.1.4a3 |
| `ovos-audio-transformer-plugin-speechbrain-langdetect` | 0.0.0a9 |
| `ovos-bidirectional-translation-plugin` | 0.1.3a2 |
| `ovos-bus-client` | 1.5.0 |
| `ovos-chromadb-embeddings-plugin` | 0.0.0 |
| `ovos-color-parser` | 0.0.9a4 |
| `ovos-common-query-pipeline-plugin` | 1.1.10a1 |
| `ovos-config` | 2.1.4a5 |
| `ovos-core` | 2.1.4a2 |
| `ovos-date-parser` | 0.7.0a5 |
| `ovos-ddg-solver-plugin` | 0.0.2a3 |
| `ovos-dialog-normalizer-plugin` | 0.0.2a2 |
| `ovos-dinkum-listener` | 0.5.1a10 |
| `ovos-flashrank-reranker-plugin` | 0.0.0 |
| `ovos-gguf-embeddings-plugin` | 0.0.0 |
| `ovos-gguf-translate` | 0.0.2a2 |
| `ovos-google-translate-plugin` | 0.0.0a2 |
| `ovos-gui` | 1.3.5a2 |
| `ovos-gui-plugin-shell-companion` | 1.0.7a1 |
| `ovos-i2c-detection` | 0.0.6a2 |
| `ovos-lang-detector-classics-plugin` | 0.0.1a1 |
| `ovos-lang-detector-fasttext-plugin` | 0.1.2 |
| `ovos-lang-parser` | 0.0.3a3 |
| `ovos-m2v-pipeline` | 0.0.10a1 |
| `ovos-mark1-utils` | 0.0.1 |
| `ovos-media-plugin-chromecast` | 0.1.4a2 |
| `ovos-media-plugin-mplayer` | 0.1.0a3 |
| `ovos-media-plugin-qt5` | 0.1.0a2 |
| `ovos-media-plugin-simple` | 0.0.2a5 |
| `ovos-media-plugin-spotify` | 0.2.8a1 |
| `ovos-media-plugin-vlc` | 0.1.0a4 |
| `ovos-messagebus` | 0.0.11a3 |
| `ovos-microphone-plugin-alsa` | 0.1.4a1 |
| `ovos-microphone-plugin-files` | 0.0.2a4 |
| `ovos-microphone-plugin-sounddevice` | 0.0.3a4 |
| `ovos-number-parser` | 0.5.2a2 |
| `ovos-ocp-files-plugin` | 0.13.1 |
| `ovos-ocp-m3u-plugin` | 0.0.2a2 |
| `ovos-ocp-news-plugin` | 0.1.3a1 |
| `ovos-ocp-pipeline-plugin` | 1.1.19a3 |
| `ovos-ocp-rss-plugin` | 0.1.3a1 |
| `ovos-ocp-youtube-plugin` | 0.0.7a1 |
| `ovos-openai-plugin` | 2.0.7a1 |
| `ovos-padatious` | 1.4.5a1 |
| `ovos-persona` | 0.7.3a1 |
| `ovos-phal` | 0.2.12 |
| `ovos-phal-plugin-alsa` | 0.1.6 |
| `ovos-phal-plugin-connectivity-events` | 0.1.4a2 |
| `ovos-phal-plugin-hotkeys` | 0.1.1 |
| `ovos-phal-plugin-ipgeo` | 0.1.8a1 |
| `ovos-phal-plugin-mk1` | 0.1.3 |
| `ovos-phal-plugin-mk2-fan-control` | 0.0.1 |
| `ovos-phal-plugin-network-manager` | 1.3.5 |
| `ovos-phal-plugin-oauth` | 0.1.3 |
| `ovos-phal-plugin-system` | 1.3.5a1 |
| `ovos-phal-plugin-wallpaper-manager` | 0.2.6 |
| `ovos-phal-plugin-wifi-setup` | 1.1.1a1 |
| `ovos-plugin-common-play` | 1.3.1 |
| `ovos-plugin-manager` | 2.2.3a1 |
| `ovos-plugin-vlc` | 0.0.2 |
| `ovos-simple-listener` | 0.2.0a1 |
| `ovos-skill-alerts` | 0.1.29a2 |
| `ovos-skill-application-launcher` | 0.5.15a2 |
| `ovos-skill-audio-recording` | 0.2.8a4 |
| `ovos-skill-boot-finished` | 0.5.1a3 |
| `ovos-skill-camera` | 1.0.5a8 |
| `ovos-skill-cmd` | 0.2.12a1 |
| `ovos-skill-color-picker` | 0.0.8a1 |
| `ovos-skill-confucius-quotes` | 0.1.14a2 |
| `ovos-skill-count` | 0.0.3a1 |
| `ovos-skill-date-time` | 1.1.6a4 |
| `ovos-skill-days-in-history` | 0.3.11 |
| `ovos-skill-ddg` | 0.3.7a4 |
| `ovos-skill-diagnostics` | 0.0.9a2 |
| `ovos-skill-dictation` | 0.2.20a4 |
| `ovos-skill-fallback-unknown` | 0.1.9 |
| `ovos-skill-fuster-quotes` | 0.0.5a3 |
| `ovos-skill-hello-world` | 0.2.3a2 |
| `ovos-skill-homescreen` | 3.0.3 |
| `ovos-skill-icanhazdadjokes` | 0.3.8a2 |
| `ovos-skill-ip` | 0.2.8 |
| `ovos-skill-iss-location` | 0.2.17a4 |
| `ovos-skill-laugh` | 1.0.3a3 |
| `ovos-skill-local-media` | 0.2.13a3 |
| `ovos-skill-moviemaster` | 0.0.13a1 |
| `ovos-skill-naptime` | 0.3.16a3 |
| `ovos-skill-news` | 0.4.7a1 |
| `ovos-skill-number-facts` | 0.1.12 |
| `ovos-skill-parrot` | 0.1.26a3 |
| `ovos-skill-personal` | 0.1.20a5 |
| `ovos-skill-pyradios` | 0.1.6a1 |
| `ovos-skill-randomness` | 1.0.0a1 |
| `ovos-skill-screenshot` | 0.0.8a4 |
| `ovos-skill-somafm` | 0.1.6a4 |
| `ovos-skill-speedtest` | 0.3.7a3 |
| `ovos-skill-spelling` | 0.2.6 |
| `ovos-skill-volume` | 0.1.17a6 |
| `ovos-skill-wallpapers` | 1.0.12a3 |
| `ovos-skill-weather` | 1.0.8a9 |
| `ovos-skill-wikihow` | 0.3.3 |
| `ovos-skill-wikipedia` | 0.8.14a3 |
| `ovos-skill-wolfie` | 0.5.9a2 |
| `ovos-skill-word-of-the-day` | 0.2.0 |
| `ovos-skill-wordnet` | 0.2.7a2 |
| `ovos-skill-youtube-music` | 0.1.8a1 |
| `ovos-solver-aiml-plugin` | 0.0.2a2 |
| `ovos-solver-bm25-plugin` | 0.1.1a2 |
| `ovos-solver-failure-plugin` | 0.0.4a2 |
| `ovos-solver-gguf-plugin` | 0.1.1a2 |
| `ovos-solver-rivescript-plugin` | 0.0.2a2 |
| `ovos-solver-yes-no-plugin` | 0.2.9a3 |
| `ovos-stt-plugin-azure` | 0.0.0a2 |
| `ovos-stt-plugin-chromium` | 0.1.2 |
| `ovos-stt-plugin-citrinet` | 0.1.1a1 |
| `ovos-stt-plugin-fasterwhisper` | 0.4.1a1 |
| `ovos-stt-plugin-mms` | 0.2.0 |
| `ovos-stt-plugin-nos` | 0.2.0 |
| `ovos-stt-plugin-onnx-asr` | 0.0.1 |
| `ovos-stt-plugin-server` | 0.1.4a1 |
| `ovos-stt-plugin-sherpa-onnx` | 0.0.1 |
| `ovos-stt-plugin-vosk` | 0.2.7 |
| `ovos-stt-plugin-wav2vec` | 0.3.3a2 |
| `ovos-stt-plugin-whisper` | 0.1.5a1 |
| `ovos-stt-plugin-whisper-lm` | 0.0.6a4 |
| `ovos-stt-plugin-whispercpp` | 0.0.1 |
| `ovos-translate-plugin-nllb` | 0.0.2a2 |
| `ovos-translate-server-plugin` | 0.0.6a1 |
| `ovos-tts-plugin-ahotts` | 0.1.2a2 |
| `ovos-tts-plugin-beepspeak` | 0.0.1a1 |
| `ovos-tts-plugin-coqui` | 0.2.0 |
| `ovos-tts-plugin-cotovia` | 0.4.5a2 |
| `ovos-tts-plugin-edge-tts` | 0.2.3a1 |
| `ovos-tts-plugin-espeakng` | 0.0.2 |
| `ovos-tts-plugin-google-tx` | 1.0.4a5 |
| `ovos-tts-plugin-marytts` | 0.1.0 |
| `ovos-tts-plugin-matxa-multispeaker-cat` | 0.0.1a5 |
| `ovos-tts-plugin-mimic` | 0.2.9a2 |
| `ovos-tts-plugin-pico` | 0.0.4a2 |
| `ovos-tts-plugin-piper` | 0.2.5 |
| `ovos-tts-plugin-polly` | 0.2.3a2 |
| `ovos-tts-plugin-server` | 0.0.5 |
| `ovos-utils` | 0.8.5 |
| `ovos-utterance-corrections-plugin` | 0.1.3a1 |
| `ovos-utterance-normalizer` | 0.2.4a1 |
| `ovos-utterance-plugin-cancel` | 0.2.6a1 |
| `ovos-vad-plugin-noise` | 0.1.3a2 |
| `ovos-vad-plugin-silero` | 0.1.1a2 |
| `ovos-vad-plugin-webrtcvad` | 0.0.1 |
| `ovos-wikipedia-solver` | 0.1.4a5 |
| `ovos-wolfram-alpha-solver` | 0.0.5a1 |
| `ovos-workshop` | 7.0.10a1 |
| `ovos-ww-plugin-openwakeword` | 0.4.1 |
| `ovos-ww-plugin-precise-onnx` | 0.1.1a2 |
| `ovos-ww-plugin-vosk` | 0.1.10 |
| `ovos-yaml-editor` | 0.1.0a3 |
| `ovoscope` | 0.13.1 |

</details>

<details>
<summary><strong>Testing</strong> (constraints-testing.txt) — 150 packages</summary>

| Package | Version |
|---------|---------|
| `hivemind-audio-binary-protocol` | 2.1.5 |
| `hivemind-bus-client` | 0.4.4 |
| `hivemind-core` | 4.0.0 |
| `hivemind-http-protocol` | 0.0.1 |
| `hivemind-plugin-manager` | 0.4.0 |
| `hivemind-redis-database` | 0.0.2 |
| `hivemind-websocket-protocol` | 0.0.3 |
| `ovos-adapt-parser` | 1.0.9 |
| `ovos-audio` | 1.2.0 |
| `ovos-audio-plugin-mpv` | 0.2.1 |
| `ovos-audio-plugin-simple` | 0.1.3 |
| `ovos-audio-transformer-plugin-speechbrain-langdetect` | 0.0.1 |
| `ovos-bidirectional-translation-plugin` | 0.1.2 |
| `ovos-bus-client` | 1.5.0 |
| `ovos-chromadb-embeddings-plugin` | 0.0.0 |
| `ovos-color-parser` | 0.0.8 |
| `ovos-common-query-pipeline-plugin` | 1.1.9 |
| `ovos-config` | 1.2.2 |
| `ovos-core` | 2.1.1 |
| `ovos-date-parser` | 0.6.5 |
| `ovos-ddg-solver-plugin` | 0.0.1 |
| `ovos-dialog-normalizer-plugin` | 0.0.1 |
| `ovos-dinkum-listener` | 0.5.0 |
| `ovos-flashrank-reranker-plugin` | 0.0.0 |
| `ovos-gguf-embeddings-plugin` | 0.0.0 |
| `ovos-gguf-translate` | 0.0.1 |
| `ovos-gui` | 1.3.4 |
| `ovos-gui-plugin-shell-companion` | 1.0.6 |
| `ovos-i2c-detection` | 0.0.5 |
| `ovos-lang-detector-fasttext-plugin` | 0.1.2 |
| `ovos-lang-parser` | 0.0.2 |
| `ovos-m2v-pipeline` | 0.0.9 |
| `ovos-mark1-utils` | 0.0.1 |
| `ovos-media-plugin-chromecast` | 0.1.3 |
| `ovos-media-plugin-spotify` | 0.2.7 |
| `ovos-messagebus` | 0.0.10 |
| `ovos-microphone-plugin-alsa` | 0.1.3 |
| `ovos-microphone-plugin-files` | 0.0.1 |
| `ovos-microphone-plugin-sounddevice` | 0.0.2 |
| `ovos-number-parser` | 0.5.1 |
| `ovos-ocp-files-plugin` | 0.13.1 |
| `ovos-ocp-m3u-plugin` | 0.0.1 |
| `ovos-ocp-news-plugin` | 0.1.2 |
| `ovos-ocp-pipeline-plugin` | 1.1.18 |
| `ovos-ocp-rss-plugin` | 0.1.2 |
| `ovos-ocp-youtube-plugin` | 0.0.6 |
| `ovos-openai-plugin` | 2.0.6 |
| `ovos-padatious` | 1.4.3 |
| `ovos-persona` | 0.7.1 |
| `ovos-phal` | 0.2.12 |
| `ovos-phal-plugin-alsa` | 0.1.6 |
| `ovos-phal-plugin-connectivity-events` | 0.1.3 |
| `ovos-phal-plugin-hotkeys` | 0.1.1 |
| `ovos-phal-plugin-ipgeo` | 0.1.7 |
| `ovos-phal-plugin-mk1` | 0.1.3 |
| `ovos-phal-plugin-mk2-fan-control` | 0.0.1 |
| `ovos-phal-plugin-network-manager` | 1.3.5 |
| `ovos-phal-plugin-oauth` | 0.1.3 |
| `ovos-phal-plugin-system` | 1.3.4 |
| `ovos-phal-plugin-wallpaper-manager` | 0.2.6 |
| `ovos-phal-plugin-wifi-setup` | 1.1.0 |
| `ovos-plugin-common-play` | 1.3.1 |
| `ovos-plugin-manager` | 2.2.0 |
| `ovos-plugin-vlc` | 0.0.2 |
| `ovos-simple-listener` | 0.1.0 |
| `ovos-skill-alerts` | 0.1.28 |
| `ovos-skill-application-launcher` | 0.5.14 |
| `ovos-skill-audio-recording` | 0.2.7 |
| `ovos-skill-boot-finished` | 0.5.0 |
| `ovos-skill-camera` | 1.0.4 |
| `ovos-skill-cmd` | 0.2.11 |
| `ovos-skill-color-picker` | 0.0.7 |
| `ovos-skill-confucius-quotes` | 0.1.13 |
| `ovos-skill-count` | 0.0.2 |
| `ovos-skill-date-time` | 1.1.5 |
| `ovos-skill-days-in-history` | 0.3.11 |
| `ovos-skill-ddg` | 0.3.6 |
| `ovos-skill-diagnostics` | 0.0.8 |
| `ovos-skill-dictation` | 0.2.19 |
| `ovos-skill-fallback-unknown` | 0.1.9 |
| `ovos-skill-fuster-quotes` | 0.0.4 |
| `ovos-skill-hello-world` | 0.2.1 |
| `ovos-skill-homescreen` | 3.0.3 |
| `ovos-skill-icanhazdadjokes` | 0.3.7 |
| `ovos-skill-ip` | 0.2.8 |
| `ovos-skill-iss-location` | 0.2.16 |
| `ovos-skill-laugh` | 1.0.2 |
| `ovos-skill-local-media` | 0.2.12 |
| `ovos-skill-moviemaster` | 0.0.12 |
| `ovos-skill-naptime` | 0.3.15 |
| `ovos-skill-news` | 0.4.6 |
| `ovos-skill-number-facts` | 0.1.12 |
| `ovos-skill-parrot` | 0.1.25 |
| `ovos-skill-personal` | 0.1.19 |
| `ovos-skill-pyradios` | 0.1.5 |
| `ovos-skill-randomness` | 0.1.2 |
| `ovos-skill-screenshot` | 0.0.7 |
| `ovos-skill-somafm` | 0.1.5 |
| `ovos-skill-speedtest` | 0.3.6 |
| `ovos-skill-spelling` | 0.2.6 |
| `ovos-skill-volume` | 0.1.16 |
| `ovos-skill-wallpapers` | 1.0.9 |
| `ovos-skill-weather` | 1.0.6 |
| `ovos-skill-wikihow` | 0.3.3 |
| `ovos-skill-wikipedia` | 0.8.13 |
| `ovos-skill-wolfie` | 0.5.8 |
| `ovos-skill-word-of-the-day` | 0.2.0 |
| `ovos-skill-wordnet` | 0.2.6 |
| `ovos-skill-youtube-music` | 0.1.7 |
| `ovos-solver-bm25-plugin` | 0.1.0 |
| `ovos-solver-failure-plugin` | 0.0.3 |
| `ovos-solver-gguf-plugin` | 0.1.0 |
| `ovos-solver-yes-no-plugin` | 0.2.8 |
| `ovos-stt-plugin-chromium` | 0.1.2 |
| `ovos-stt-plugin-citrinet` | 0.1.0 |
| `ovos-stt-plugin-fasterwhisper` | 0.4.0 |
| `ovos-stt-plugin-mms` | 0.2.0 |
| `ovos-stt-plugin-nos` | 0.2.0 |
| `ovos-stt-plugin-onnx-asr` | 0.0.1 |
| `ovos-stt-plugin-server` | 0.1.3 |
| `ovos-stt-plugin-sherpa-onnx` | 0.0.1 |
| `ovos-stt-plugin-vosk` | 0.2.7 |
| `ovos-stt-plugin-wav2vec` | 0.3.0 |
| `ovos-stt-plugin-whisper` | 0.1.4 |
| `ovos-stt-plugin-whispercpp` | 0.0.1 |
| `ovos-translate-plugin-nllb` | 0.0.1 |
| `ovos-translate-server-plugin` | 0.0.5 |
| `ovos-tts-plugin-coqui` | 0.2.0 |
| `ovos-tts-plugin-espeakng` | 0.0.2 |
| `ovos-tts-plugin-marytts` | 0.1.0 |
| `ovos-tts-plugin-mimic` | 0.2.8 |
| `ovos-tts-plugin-nos` | 0.7.5 |
| `ovos-tts-plugin-pico` | 0.0.3.post1 |
| `ovos-tts-plugin-piper` | 0.2.5 |
| `ovos-tts-plugin-polly` | 0.2.1 |
| `ovos-tts-plugin-server` | 0.0.5 |
| `ovos-utils` | 0.8.4 |
| `ovos-utterance-corrections-plugin` | 0.1.2 |
| `ovos-utterance-normalizer` | 0.2.3 |
| `ovos-utterance-plugin-cancel` | 0.2.5 |
| `ovos-vad-plugin-silero` | 0.1.0 |
| `ovos-vad-plugin-webrtcvad` | 0.0.1 |
| `ovos-wikipedia-solver` | 0.1.3 |
| `ovos-wolfram-alpha-solver` | 0.0.4 |
| `ovos-workshop` | 7.0.6 |
| `ovos-ww-plugin-openwakeword` | 0.4.1 |
| `ovos-ww-plugin-precise-onnx` | 0.1.0 |
| `ovos-ww-plugin-vosk` | 0.1.10 |
| `ovos-yaml-editor` | 0.0.2 |
| `ovoscope` | 0.13.1 |

</details>

<details>
<summary><strong>Stable</strong> (constraints-stable.txt) — 108 packages</summary>

| Package | Version |
|---------|---------|
| `ovos-adapt-parser` | 1.0.9 |
| `ovos-audio` | 0.4.0 |
| `ovos-audio-plugin-mpv` | 0.2.1 |
| `ovos-audio-plugin-simple` | 0.1.3 |
| `ovos-bidirectional-translation-plugin` | 0.1.2 |
| `ovos-bus-client` | 1.3.7 |
| `ovos-classifiers` | 0.0.0a59 |
| `ovos-color-parser` | 0.0.8 |
| `ovos-common-query-pipeline-plugin` | 1.1.7 |
| `ovos-config` | 1.2.2 |
| `ovos-core` | 1.3.1 |
| `ovos-date-parser` | 0.6.4 |
| `ovos-dialog-normalizer-plugin` | 0.0.1 |
| `ovos-dinkum-listener` | 0.4.0 |
| `ovos-gui` | 1.3.4 |
| `ovos-gui-plugin-shell-companion` | 1.0.6 |
| `ovos-lang-parser` | 0.0.2 |
| `ovos-mark1-utils` | 0.0.1 |
| `ovos-media-plugin-chromecast` | 0.1.3 |
| `ovos-media-plugin-spotify` | 0.2.7 |
| `ovos-messagebus` | 0.0.10 |
| `ovos-microphone-plugin-alsa` | 0.1.3 |
| `ovos-microphone-plugin-sounddevice` | 0.0.2 |
| `ovos-number-parser` | 0.3.2 |
| `ovos-ocp-files-plugin` | 0.13.1 |
| `ovos-ocp-m3u-plugin` | 0.0.2 |
| `ovos-ocp-news-plugin` | 0.1.2 |
| `ovos-ocp-pipeline-plugin` | 1.1.14 |
| `ovos-ocp-rss-plugin` | 0.1.2 |
| `ovos-ocp-youtube-plugin` | 0.0.6 |
| `ovos-openai-plugin` | 2.0.6 |
| `ovos-padatious` | 1.4.3 |
| `ovos-persona` | 0.6.24 |
| `ovos-phal` | 0.2.12 |
| `ovos-phal-plugin-alsa` | 0.1.6 |
| `ovos-phal-plugin-balena-wifi` | 1.2.2 |
| `ovos-phal-plugin-connectivity-events` | 0.1.3 |
| `ovos-phal-plugin-hotkeys` | 0.1.1 |
| `ovos-phal-plugin-ipgeo` | 0.1.7 |
| `ovos-phal-plugin-mk1` | 0.1.3 |
| `ovos-phal-plugin-network-manager` | 1.3.4 |
| `ovos-phal-plugin-oauth` | 0.1.3 |
| `ovos-phal-plugin-system` | 1.3.4 |
| `ovos-phal-plugin-wallpaper-manager` | 0.2.6 |
| `ovos-phal-plugin-wifi-setup` | 1.1.8 |
| `ovos-plugin-common-play` | 1.2.1 |
| `ovos-plugin-manager` | 0.9.0 |
| `ovos-skill-alerts` | 0.1.24 |
| `ovos-skill-application-launcher` | 0.5.13 |
| `ovos-skill-audio-recording` | 0.2.7 |
| `ovos-skill-boot-finished` | 0.5.0 |
| `ovos-skill-camera` | 1.0.4 |
| `ovos-skill-cmd` | 0.2.11 |
| `ovos-skill-color-picker` | 0.0.7 |
| `ovos-skill-confucius-quotes` | 0.1.13 |
| `ovos-skill-date-time` | 0.4.20 |
| `ovos-skill-days-in-history` | 0.3.11 |
| `ovos-skill-ddg` | 0.3.6 |
| `ovos-skill-diagnostics` | 0.0.8 |
| `ovos-skill-dictation` | 0.2.15 |
| `ovos-skill-fallback-unknown` | 0.1.6 |
| `ovos-skill-hello-world` | 0.2.1 |
| `ovos-skill-homescreen` | 3.0.3 |
| `ovos-skill-icanhazdadjokes` | 0.3.7 |
| `ovos-skill-ip` | 0.2.8 |
| `ovos-skill-iss-location` | 0.2.16 |
| `ovos-skill-laugh` | 0.2.3 |
| `ovos-skill-local-media` | 0.2.12 |
| `ovos-skill-moviemaster` | 0.0.12 |
| `ovos-skill-naptime` | 0.3.15 |
| `ovos-skill-news` | 0.4.5 |
| `ovos-skill-number-facts` | 0.1.12 |
| `ovos-skill-parrot` | 0.1.20 |
| `ovos-skill-personal` | 0.1.19 |
| `ovos-skill-pyradios` | 0.1.5 |
| `ovos-skill-randomness` | 0.1.2 |
| `ovos-skill-screenshot` | 0.0.7 |
| `ovos-skill-somafm` | 0.1.5 |
| `ovos-skill-speedtest` | 0.3.6 |
| `ovos-skill-spelling` | 0.2.6 |
| `ovos-skill-volume` | 0.1.16 |
| `ovos-skill-wallpapers` | 1.0.9 |
| `ovos-skill-weather` | 0.1.18 |
| `ovos-skill-wikihow` | 0.3.3 |
| `ovos-skill-wikipedia` | 0.8.13 |
| `ovos-skill-wolfie` | 0.5.8 |
| `ovos-skill-wordnet` | 0.2.6 |
| `ovos-skill-youtube-music` | 0.1.7 |
| `ovos-solver-bm25-plugin` | 0.0.1 |
| `ovos-solver-failure-plugin` | 0.0.3 |
| `ovos-solver-yes-no-plugin` | 0.2.8 |
| `ovos-stt-plugin-chromium` | 0.1.2 |
| `ovos-stt-plugin-server` | 0.1.1 |
| `ovos-stt-plugin-vosk` | 0.2.3 |
| `ovos-translate-server-plugin` | 0.0.2 |
| `ovos-tts-plugin-server` | 0.0.2 |
| `ovos-utils` | 0.8.5 |
| `ovos-utterance-corrections-plugin` | 0.1.2 |
| `ovos-utterance-normalizer` | 0.2.3 |
| `ovos-utterance-plugin-cancel` | 0.2.5 |
| `ovos-vad-plugin-noise` | 0.1.2 |
| `ovos-vad-plugin-silero` | 0.0.5 |
| `ovos-wikipedia-solver` | 0.1.3 |
| `ovos-wolfram-alpha-solver` | 0.0.4 |
| `ovos-workshop` | 3.4.0 |
| `ovos-ww-plugin-openwakeword` | 0.4.1 |
| `ovos-ww-plugin-precise-lite` | 0.1.3 |
| `ovos-ww-plugin-vosk` | 0.1.4 |

</details>
