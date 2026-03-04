# Package Conflict Report

_Generated: 2026-03-04 18:01 UTC_

| | Count |
|---|---:|
| ✅ Conflicts resolved — re-run `make_alpha_testing.py` | 0 |
| ❌ Conflicts still broken | 10 |
| ⚠️ Python version restrictions | 16 |
| 🔖 Missing stable release on PyPI | 9 |

---

## 1. Dependency Conflicts

Packages in [`lists/unstable.list`](lists/unstable.list) excluded from `constraints-testing.txt`.

### ❌ Still Conflicting — action needed

**`hivemind-audio-binary-protocol>=2.1.5a1`**  
Would add: `hivemind-audio-binary-protocol>=2.1.3,<3.0.0`
```
Because hivemind-audio-binary-protocol==2.1.3 depends on hivemind-core>=1.0.0,<4.0.0 and only hivemind-audio-binary-protocol<=2.1.3 is available, we can conclude that hivemind-audio-binary-protocol>=2.1.3 depends on
```

**`ovos-solver-aiml-plugin>=0.0.2a2`**  
Would add: `ovos-solver-aiml-plugin>=0.0.1,<1.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

**`ovos-solver-rivescript-plugin>=0.0.2a2`**  
Would add: `ovos-solver-rivescript-plugin>=0.0.1,<1.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

**`ovos-stt-plugin-whisper-lm>=0.0.6a4`**  
Would add: `ovos-stt-plugin-whisper-lm>=0.0.5,<1.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

**`ovos-tts-plugin-ahotts>=0.1.2a2`**  
Would add: `ovos-tts-plugin-ahotts>=0.1.1,<1.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

**`ovos-tts-plugin-cotovia>=0.4.5a2`**  
Would add: `ovos-tts-plugin-cotovia>=0.4.3,<1.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

**`ovos-tts-plugin-edge-tts>=0.2.3a1`**  
Would add: `ovos-tts-plugin-edge-tts>=0.2.2,<1.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

**`ovos-tts-plugin-google-tx>=1.0.4a5`**  
Would add: `ovos-tts-plugin-google-tx>=1.0.3,<2.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

**`ovos-tts-plugin-server>=0.0.5a2`**  
Would add: `ovos-tts-plugin-server>=0.0.4,<1.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

**`ovos-vad-plugin-noise>=0.1.3a2`**  
Would add: `ovos-vad-plugin-noise>=0.1.2,<1.0.0`
```
Because only ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version < '3.15'}<=0.0.1 is available and ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
```

---

## 2. Python Version Restrictions

Present in testing but excluded on newer Python via `; python_version < "X.Y"` marker.
**Action:** update the transitive dependency to publish wheels for the excluded versions.

| Package | Alpha version | Supported | Excluded |
|---------|:-------------:|-----------|----------|
| `ovos-audio-transformer-plugin-speechbrain-langdetect` | 0.0.0a9 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-chromadb-embeddings-plugin` | 0.0.0 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-flashrank-reranker-plugin` | 0.0.0 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-gguf-embeddings-plugin` | 0.0.0 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-m2v-pipeline` | 0.0.10a1 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-stt-plugin-citrinet` | 0.1.1a1 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-stt-plugin-fasterwhisper` | 0.4.1a1 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-stt-plugin-mms` | 0.2.0 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-stt-plugin-nos` | 0.2.0 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-stt-plugin-wav2vec` | 0.3.3a2 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-translate-plugin-nllb` | 0.0.2a2 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-tts-plugin-nos` | 0.7.5 | 3.10, 3.11, 3.12, 3.13 | 3.14, 3.15 |
| `ovos-tts-plugin-piper` | 0.2.5 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-vad-plugin-silero` | 0.1.1a2 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |
| `ovos-ww-plugin-openwakeword` | 0.4.1 | 3.10, 3.11 | 3.12, 3.13, 3.14, 3.15 |
| `ovos-ww-plugin-precise-onnx` | 0.1.1a2 | 3.10, 3.11, 3.12, 3.13, 3.14 | 3.15 |

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
