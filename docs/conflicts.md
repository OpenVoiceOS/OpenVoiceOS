# Package Conflict Report

_Generated: 2026-08-03 12:27 UTC_

| | Count |
|---|---:|
| ✅ Conflicts resolved — re-run `make_alpha_testing.py` | 8 |
| ❌ Conflicts still broken | 0 |
| ⚠️ Python version restrictions | 2 |
| 🔖 Missing stable release on PyPI | 22 |

---

## 1. Dependency Conflicts

Packages in [`lists/unstable.list`](lists/unstable.list) excluded from `constraints-testing.txt`.

### ✅ Resolved — re-run `make_alpha_testing.py` to include

| Package | Would add to testing |
|---------|----------------------|
| `ovos-solver-aiml-plugin` | `ovos-solver-aiml-plugin>=0.0.1,<1.0.0` |
| `ovos-solver-rivescript-plugin` | `ovos-solver-rivescript-plugin>=0.0.1,<1.0.0` |
| `ovos-stt-plugin-whisper-lm` | `ovos-stt-plugin-whisper-lm>=0.0.5,<1.0.0` |
| `ovos-tts-plugin-ahotts` | `ovos-tts-plugin-ahotts>=0.1.1,<1.0.0` |
| `ovos-tts-plugin-cotovia` | `ovos-tts-plugin-cotovia>=0.4.3,<1.0.0` |
| `ovos-tts-plugin-edge-tts` | `ovos-tts-plugin-edge-tts>=0.2.2,<1.0.0` |
| `ovos-tts-plugin-google-tx` | `ovos-tts-plugin-google-tx>=1.0.3,<2.0.0` |
| `ovos-vad-plugin-noise` | `ovos-vad-plugin-noise>=0.1.2,<1.0.0` |

---

## 2. Python Version Restrictions

Present in testing but excluded on newer Python via `; python_version < "X.Y"` marker.
**Action:** update the transitive dependency to publish wheels for the excluded versions.

| Package | Alpha version | Supported | Excluded |
|---------|:-------------:|-----------|----------|
| `ovos-tts-plugin-nos` |  | 3.10, 3.11, 3.12, 3.13 | 3.14, 3.15 |
| `ovos-ww-plugin-openwakeword` | 0.4.5a2 | 3.10, 3.11 | 3.12, 3.13, 3.14, 3.15 |

---

## 3. No Stable Release on PyPI

Exist in alpha as a pre-release; absent from testing because no stable version is available.
**Action:** cut a stable (non-pre-release) release.

| Package | Alpha version | Latest stable |
|---------|:-------------:|:-------------:|
| `hivemind-json-db-plugin` | 0.0.4a3 | 0.0.2 |
| `hivemind-ovos-agent-plugin` | 0.3.3a1 | 0.1.0 |
| `hivemind-sqlite-database` | 0.4.0a7 | 0.2.1 |
| `ovos-agentic-loop` | 0.2.2a1 | 0.1.0 |
| `ovos-ddg-plugin` | 1.0.1a1 | — |
| `ovos-google-translate-plugin` | 0.0.4a2 | — |
| `ovos-lang-detector-classics-plugin` | 0.0.2a1 | — |
| `ovos-media-plugin-mplayer` | 0.2.0a3 | — |
| `ovos-media-plugin-qt5` | 0.1.0a2 | — |
| `ovos-media-plugin-simple` | 0.1.0a1 | — |
| `ovos-media-plugin-vlc` | 0.2.0a2 | — |
| `ovos-option-matcher-fuzzy-plugin` | 0.0.2a1 | 0.0.1 |
| `ovos-spec-tools` | 1.6.0a2 | — |
| `ovos-stt-plugin-azure` | 0.0.0a4 | — |
| `ovos-stt-plugin-rover` | 0.1.0a2 | 0.0.1 |
| `ovos-transcription-validator-plugin` | 0.1.2a3 | 0.1.0 |
| `ovos-tts-plugin-beepspeak` | 0.1.0a2 | — |
| `ovos-tts-plugin-matxa-multispeaker-cat` | 0.0.1a5 | — |
| `ovos-wikipedia-plugin` | 1.0.1a2 | — |
| `ovos-wolfram-alpha-plugin` | 1.0.0a3 | — |
| `ovos-wordnet-plugin` | 0.1.1a1 | 0.1.0 |
| `ovos-yes-no-plugin` | 0.3.1a2 | 0.3.0 |

---

## 4. Resolved Package Snapshots

Exact versions uv would install for each constraints file (Python 3.10, transitive deps included).

<details>
<summary><strong>Alpha</strong> (constraints-alpha.txt) — 176 packages</summary>

| Package | Version |
|---------|---------|
| `hivemind-audio-binary-protocol` | 2.1.7a1 |
| `hivemind-bus-client` | 0.11.0a1 |
| `hivemind-core` | 4.10.15a1 |
| `hivemind-http-protocol` | 0.0.5a1 |
| `hivemind-json-db-plugin` | 0.0.4a3 |
| `hivemind-ovos-agent-plugin` | 0.3.3a1 |
| `hivemind-plugin-manager` | 0.9.0a3 |
| `hivemind-redis-database` | 0.1.0a7 |
| `hivemind-sqlite-database` | 0.4.0a7 |
| `hivemind-websocket-protocol` | 0.2.2a2 |
| `ovos-adapt-parser` | 1.6.1a1 |
| `ovos-agentic-loop` | 0.2.2a1 |
| `ovos-audio` | 2.1.1a2 |
| `ovos-audio-plugin-mpv` | 0.2.1 |
| `ovos-audio-plugin-simple` | 0.1.4a3 |
| `ovos-audio-transformer-plugin-speechbrain-langdetect` | 0.0.2a1 |
| `ovos-bidirectional-translation-plugin` | 0.1.3a4 |
| `ovos-bus-client` | 2.7.3a1 |
| `ovos-chromadb-embeddings-plugin` | 0.3.0a4 |
| `ovos-color-parser` | 0.11.2a1 |
| `ovos-common-query-pipeline-plugin` | 1.1.15a1 |
| `ovos-config` | 2.3.8a2 |
| `ovos-core` | 2.2.4a1 |
| `ovos-date-parser` | 0.29.0 |
| `ovos-ddg-plugin` | 1.0.1a1 |
| `ovos-ddg-solver-plugin` | 0.0.2a3 |
| `ovos-dialog-normalizer-plugin` | 0.0.3a2 |
| `ovos-dinkum-listener` | 0.8.2a3 |
| `ovos-flashrank-reranker-plugin` | 0.0.0 |
| `ovos-gguf-embeddings-plugin` | 0.0.0 |
| `ovos-gguf-translate` | 0.0.2a2 |
| `ovos-google-translate-plugin` | 0.0.4a2 |
| `ovos-gui` | 1.4.1a2 |
| `ovos-i2c-detection` | 0.0.6a2 |
| `ovos-lang-detector-classics-plugin` | 0.0.2a1 |
| `ovos-lang-detector-fasttext-plugin` | 0.1.3a4 |
| `ovos-lang-parser` | 0.7.1a4 |
| `ovos-m2v-pipeline` | 0.5.4a2 |
| `ovos-mark1-utils` | 0.0.1 |
| `ovos-media-plugin-chromecast` | 0.1.4a12 |
| `ovos-media-plugin-mplayer` | 0.2.0a3 |
| `ovos-media-plugin-qt5` | 0.1.0a2 |
| `ovos-media-plugin-simple` | 0.1.0a1 |
| `ovos-media-plugin-spotify` | 0.2.8a8 |
| `ovos-media-plugin-vlc` | 0.2.0a2 |
| `ovos-messagebus` | 0.2.1a2 |
| `ovos-microphone-plugin-alsa` | 0.1.4a6 |
| `ovos-microphone-plugin-files` | 0.0.2a9 |
| `ovos-microphone-plugin-sounddevice` | 0.0.3a9 |
| `ovos-number-parser` | 0.19.8a2 |
| `ovos-ocp-files-plugin` | 0.13.2a3 |
| `ovos-ocp-m3u-plugin` | 0.0.4a5 |
| `ovos-ocp-news-plugin` | 0.1.3a5 |
| `ovos-ocp-pipeline-plugin` | 1.1.28a2 |
| `ovos-ocp-rss-plugin` | 0.1.3a6 |
| `ovos-ocp-youtube-plugin` | 0.0.8a2 |
| `ovos-openai-plugin` | 2.0.7a8 |
| `ovos-option-matcher-fuzzy-plugin` | 0.0.2a1 |
| `ovos-padatious` | 2.0.1a2 |
| `ovos-persona` | 0.9.0a16 |
| `ovos-phal` | 0.2.16a2 |
| `ovos-phal-plugin-alsa` | 0.1.9a1 |
| `ovos-phal-plugin-connectivity-events` | 0.1.6a2 |
| `ovos-phal-plugin-hotkeys` | 0.1.3a2 |
| `ovos-phal-plugin-ipgeo` | 0.1.9a2 |
| `ovos-phal-plugin-mk1` | 0.1.5a2 |
| `ovos-phal-plugin-mk2-fan-control` | 0.0.3a2 |
| `ovos-phal-plugin-network-manager` | 1.3.7a2 |
| `ovos-phal-plugin-oauth` | 0.1.7a2 |
| `ovos-phal-plugin-system` | 1.3.8a2 |
| `ovos-phal-plugin-wallpaper-manager` | 0.2.8a2 |
| `ovos-plugin-common-play` | 1.3.5a1 |
| `ovos-plugin-manager` | 2.11.1a2 |
| `ovos-plugin-vlc` | 0.0.2 |
| `ovos-simple-listener` | 0.3.1a2 |
| `ovos-skill-alerts` | 0.2.2a2 |
| `ovos-skill-application-launcher` | 0.6.0a4 |
| `ovos-skill-audio-recording` | 0.2.11a1 |
| `ovos-skill-boot-finished` | 0.5.5a3 |
| `ovos-skill-camera` | 1.1.0a2 |
| `ovos-skill-cmd` | 0.2.14a4 |
| `ovos-skill-color-picker` | 0.1.0a2 |
| `ovos-skill-confucius-quotes` | 0.3.1a2 |
| `ovos-skill-count` | 0.0.6a2 |
| `ovos-skill-date-time` | 1.1.14a2 |
| `ovos-skill-days-in-history` | 0.3.12a6 |
| `ovos-skill-ddg` | 0.3.9a3 |
| `ovos-skill-diagnostics` | 0.0.12a3 |
| `ovos-skill-dictation` | 0.2.24a1 |
| `ovos-skill-fallback-unknown` | 0.1.12a2 |
| `ovos-skill-fuster-quotes` | 0.0.7a3 |
| `ovos-skill-hello-world` | 0.2.6a3 |
| `ovos-skill-homescreen` | 3.0.4a2 |
| `ovos-skill-icanhazdadjokes` | 0.3.11a3 |
| `ovos-skill-ip` | 0.3.0a4 |
| `ovos-skill-iss-location` | 0.2.18a6 |
| `ovos-skill-laugh` | 1.0.6a1 |
| `ovos-skill-local-media` | 0.2.15a3 |
| `ovos-skill-moviemaster` | 0.0.15a2 |
| `ovos-skill-naptime` | 0.4.0a4 |
| `ovos-skill-news` | 0.4.9a2 |
| `ovos-skill-number-facts` | 0.1.13a6 |
| `ovos-skill-parrot` | 0.1.31a3 |
| `ovos-skill-personal` | 0.1.25a2 |
| `ovos-skill-pyradios` | 0.1.6a7 |
| `ovos-skill-randomness` | 1.1.0a3 |
| `ovos-skill-screenshot` | 0.0.10a4 |
| `ovos-skill-somafm` | 0.1.6a8 |
| `ovos-skill-speedtest` | 0.3.8a6 |
| `ovos-skill-spelling` | 0.2.7a3 |
| `ovos-skill-volume` | 0.1.22a4 |
| `ovos-skill-wallpapers` | 1.0.14a6 |
| `ovos-skill-weather` | 1.0.12a3 |
| `ovos-skill-wikihow` | 0.3.7a2 |
| `ovos-skill-wikipedia` | 0.8.17a4 |
| `ovos-skill-wolfie` | 0.7.1a3 |
| `ovos-skill-word-of-the-day` | 0.2.6a1 |
| `ovos-skill-wordnet` | 0.5.0a2 |
| `ovos-skill-youtube-music` | 0.1.10a2 |
| `ovos-solver-aiml-plugin` | 0.0.2a6 |
| `ovos-solver-bm25-plugin` | 0.1.1a3 |
| `ovos-solver-failure-plugin` | 0.0.6a2 |
| `ovos-solver-gguf-plugin` | 0.1.1a2 |
| `ovos-solver-rivescript-plugin` | 0.0.2a2 |
| `ovos-spec-tools` | 1.6.0a2 |
| `ovos-stt-plugin-azure` | 0.0.0a4 |
| `ovos-stt-plugin-chromium` | 0.1.2 |
| `ovos-stt-plugin-citrinet` | 0.1.1a12 |
| `ovos-stt-plugin-fasterwhisper` | 0.4.1a6 |
| `ovos-stt-plugin-mms` | 0.2.0 |
| `ovos-stt-plugin-nos` | 0.2.0 |
| `ovos-stt-plugin-onnx-asr` | 0.3.0a2 |
| `ovos-stt-plugin-rover` | 0.1.0a2 |
| `ovos-stt-plugin-server` | 0.1.5a4 |
| `ovos-stt-plugin-sherpa-onnx` | 0.0.2a1 |
| `ovos-stt-plugin-vosk` | 0.2.8a2 |
| `ovos-stt-plugin-wav2vec` | 0.3.3a8 |
| `ovos-stt-plugin-whisper` | 0.1.5a2 |
| `ovos-stt-plugin-whisper-lm` | 0.0.6a11 |
| `ovos-stt-plugin-whispercpp` | 0.0.2a2 |
| `ovos-transcription-validator-plugin` | 0.1.2a3 |
| `ovos-translate-plugin-nllb` | 0.0.2a5 |
| `ovos-translate-server-plugin` | 0.0.8a3 |
| `ovos-tts-plugin-ahotts` | 0.2.0a2 |
| `ovos-tts-plugin-beepspeak` | 0.1.0a2 |
| `ovos-tts-plugin-coqui` | 0.2.2a9 |
| `ovos-tts-plugin-cotovia` | 0.5.0a2 |
| `ovos-tts-plugin-edge-tts` | 0.3.2a2 |
| `ovos-tts-plugin-espeakng` | 0.1.0a2 |
| `ovos-tts-plugin-google-tx` | 1.0.5a4 |
| `ovos-tts-plugin-marytts` | 0.2.0a2 |
| `ovos-tts-plugin-matxa-multispeaker-cat` | 0.0.1a5 |
| `ovos-tts-plugin-mimic` | 0.4.0a2 |
| `ovos-tts-plugin-pico` | 0.1.0a2 |
| `ovos-tts-plugin-piper` | 0.2.6a2 |
| `ovos-tts-plugin-polly` | 0.3.0a2 |
| `ovos-tts-plugin-server` | 0.0.6a3 |
| `ovos-utils` | 0.13.9a2 |
| `ovos-utterance-corrections-plugin` | 0.1.3a6 |
| `ovos-utterance-normalizer` | 0.2.5a2 |
| `ovos-utterance-plugin-cancel` | 0.3.3a2 |
| `ovos-vad-plugin-noise` | 0.1.3a7 |
| `ovos-vad-plugin-silero` | 0.1.3a2 |
| `ovos-vad-plugin-webrtcvad` | 0.0.3a4 |
| `ovos-wikipedia-plugin` | 1.0.1a2 |
| `ovos-wikipedia-solver` | 0.1.4a5 |
| `ovos-wolfram-alpha-plugin` | 1.0.0a3 |
| `ovos-wolfram-alpha-solver` | 0.0.5a1 |
| `ovos-wordnet-plugin` | 0.1.1a1 |
| `ovos-workshop` | 8.3.0a1 |
| `ovos-ww-plugin-openwakeword` | 0.4.5a2 |
| `ovos-ww-plugin-precise-onnx` | 0.1.1a8 |
| `ovos-ww-plugin-vosk` | 0.1.11a3 |
| `ovos-yaml-editor` | 0.1.0a3 |
| `ovos-yes-no-plugin` | 0.3.1a2 |
| `ovoscope` | 1.6.4a1 |

</details>

<details>
<summary><strong>Testing</strong> (constraints-testing.txt) — 150 packages</summary>

| Package | Version |
|---------|---------|
| `hivemind-audio-binary-protocol` | 2.1.5 |
| `hivemind-bus-client` | 0.4.4 |
| `hivemind-core` | 4.0.0 |
| `hivemind-http-protocol` | 0.0.1 |
| `hivemind-plugin-manager` | 0.5.0 |
| `hivemind-redis-database` | 0.0.3 |
| `hivemind-websocket-protocol` | 0.0.3 |
| `ovos-adapt-parser` | 1.0.9 |
| `ovos-audio` | 1.2.0 |
| `ovos-audio-plugin-mpv` | 0.2.1 |
| `ovos-audio-plugin-simple` | 0.1.3 |
| `ovos-audio-transformer-plugin-speechbrain-langdetect` | 0.0.1 |
| `ovos-bidirectional-translation-plugin` | 0.1.2 |
| `ovos-bus-client` | 1.5.0 |
| `ovos-chromadb-embeddings-plugin` | 0.0.0 |
| `ovos-color-parser` | 0.11.0 |
| `ovos-common-query-pipeline-plugin` | 1.1.9 |
| `ovos-config` | 2.1.1 |
| `ovos-core` | 2.1.1 |
| `ovos-date-parser` | 0.29.0 |
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
| `ovos-messagebus` | 0.2.1a2 |
| `ovos-microphone-plugin-alsa` | 0.1.3 |
| `ovos-microphone-plugin-files` | 0.0.1 |
| `ovos-microphone-plugin-sounddevice` | 0.0.2 |
| `ovos-number-parser` | 0.19.7 |
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
| `ovos-skill-laugh` | 1.0.5 |
| `ovos-skill-local-media` | 0.2.12 |
| `ovos-skill-moviemaster` | 0.0.12 |
| `ovos-skill-naptime` | 0.3.15 |
| `ovos-skill-news` | 0.4.6 |
| `ovos-skill-number-facts` | 0.1.12 |
| `ovos-skill-parrot` | 0.1.25 |
| `ovos-skill-personal` | 0.1.19 |
| `ovos-skill-pyradios` | 0.1.5 |
| `ovos-skill-randomness` | 1.0.1 |
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
| `ovos-skill-word-of-the-day` | 0.2.5 |
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
| `ovos-utterance-plugin-cancel` | 0.2.8 |
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
| `ovos-utterance-plugin-cancel` | 0.2.8 |
| `ovos-vad-plugin-noise` | 0.1.2 |
| `ovos-vad-plugin-silero` | 0.0.5 |
| `ovos-wikipedia-solver` | 0.1.3 |
| `ovos-wolfram-alpha-solver` | 0.0.4 |
| `ovos-workshop` | 3.4.0 |
| `ovos-ww-plugin-openwakeword` | 0.4.1 |
| `ovos-ww-plugin-precise-lite` | 0.1.3 |
| `ovos-ww-plugin-vosk` | 0.1.4 |

</details>
