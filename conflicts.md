# Package Conflict Report

_Generated: 2026-03-04 18:17 UTC_

| | Count |
|---|---:|
| ✅ Conflicts resolved — re-run `make_alpha_testing.py` | 1 |
| ❌ Conflicts still broken | 9 |
| ⚠️ Python version restrictions | 16 |
| 🔖 Missing stable release on PyPI | 9 |

---

## 1. Dependency Conflicts

Packages in [`lists/unstable.list`](lists/unstable.list) excluded from `constraints-testing.txt`.

### ✅ Resolved — re-run `make_alpha_testing.py` to include

| Package | Would add to testing |
|---------|----------------------|
| `ovos-tts-plugin-server` | `ovos-tts-plugin-server>=0.0.5,<1.0.0` |

### ❌ Still Conflicting — action needed

**`hivemind-audio-binary-protocol>=2.1.5a1`**  
Would add: `hivemind-audio-binary-protocol>=2.1.3,<3.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because hivemind-audio-binary-protocol==2.1.3
      depends on hivemind-core>=1.0.0,<4.0.0 and only
      hivemind-audio-binary-protocol<=2.1.3 is available, we can
      conclude that hivemind-audio-binary-protocol>=2.1.3 depends on
      hivemind-core>=1.0.0,<4.0.0.
      And because you require hivemind-core>=4.0.0 and
      hivemind-audio-binary-protocol>=2.1.3, we can conclude that your
      requirements are unsatisfiable.

      hint: Pre-releases are available for `hivemind-audio-binary-protocol`
      in the requested range (e.g., 2.1.5a1), but pre-releases weren't enabled
      (try: `--prerelease=allow`)
```

**`ovos-solver-aiml-plugin>=0.0.2a2`**  
Would add: `ovos-solver-aiml-plugin>=0.0.1,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}<=0.0.1 is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 depends on ovos-plugin-manager>=2.1.1.
      And because ovos-solver-aiml-plugin==0.0.1 depends
      on ovos-plugin-manager>=0.0.26,<2.0.0 and only
      ovos-solver-aiml-plugin<=0.0.1 is available, we can
      conclude that ovos-solver-aiml-plugin>=0.0.1 and
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 and ovos-solver-aiml-plugin>=0.0.1, we can conclude
      that your requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-solver-aiml-plugin` in the
      requested range (e.g., 0.0.2a2), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-solver-rivescript-plugin>=0.0.2a2`**  
Would add: `ovos-solver-rivescript-plugin>=0.0.1,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}<=0.0.1 is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 depends on ovos-plugin-manager>=2.1.1.
      And because ovos-solver-rivescript-plugin==0.0.1
      depends on ovos-plugin-manager>=0.0.26,<2.0.0 and only
      ovos-solver-rivescript-plugin<=0.0.1 is available, we can
      conclude that ovos-solver-rivescript-plugin>=0.0.1 and
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 and ovos-solver-rivescript-plugin>=0.0.1, we can
      conclude that your requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-solver-rivescript-plugin` in
      the requested range (e.g., 0.0.2a2), but pre-releases weren't enabled
      (try: `--prerelease=allow`)
```

**`ovos-stt-plugin-whisper-lm>=0.0.6a4`**  
Would add: `ovos-stt-plugin-whisper-lm>=0.0.5,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}<=0.0.1 is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 depends on ovos-plugin-manager>=2.1.1.
      And because ovos-stt-plugin-whisper-lm==0.0.5
      depends on ovos-plugin-manager>=1.0.0,<2.0.0 and only
      ovos-stt-plugin-whisper-lm<=0.0.5 is available, we can
      conclude that ovos-stt-plugin-whisper-lm>=0.0.5 and
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 and ovos-stt-plugin-whisper-lm>=0.0.5, we can conclude
      that your requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-stt-plugin-whisper-lm` in the
      requested range (e.g., 0.0.6a4), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-tts-plugin-ahotts>=0.1.2a2`**  
Would add: `ovos-tts-plugin-ahotts>=0.1.1,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}<=0.0.1 is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 depends on ovos-plugin-manager>=2.1.1.
      And because ovos-tts-plugin-ahotts==0.1.1 depends on
      ovos-plugin-manager>=1.0.0,<2.0.0 and only ovos-tts-plugin-ahotts<=0.1.1
      is available, we can conclude that ovos-tts-plugin-ahotts>=0.1.1 and
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 and ovos-tts-plugin-ahotts>=0.1.1, we can conclude that
      your requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-tts-plugin-ahotts` in the
      requested range (e.g., 0.1.2a2), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-tts-plugin-cotovia>=0.4.5a2`**  
Would add: `ovos-tts-plugin-cotovia>=0.4.3,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}<=0.0.1 is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 depends on ovos-plugin-manager>=2.1.1.
      And because ovos-tts-plugin-cotovia==0.4.3 depends on
      ovos-plugin-manager>=1.0.0,<2.0.0 and only ovos-tts-plugin-cotovia<=0.4.3
      is available, we can conclude that ovos-tts-plugin-cotovia>=0.4.3 and
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 and ovos-tts-plugin-cotovia>=0.4.3, we can conclude
      that your requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-tts-plugin-cotovia` in the
      requested range (e.g., 0.4.5a2), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-tts-plugin-edge-tts>=0.2.3a1`**  
Would add: `ovos-tts-plugin-edge-tts>=0.2.2,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}<=0.0.1 is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 depends on ovos-plugin-manager>=2.1.1.
      And because ovos-tts-plugin-edge-tts==0.2.2 depends
      on ovos-plugin-manager>=1.0.0,<2.0.0 and only
      ovos-tts-plugin-edge-tts<=0.2.2 is available, we can
      conclude that ovos-tts-plugin-edge-tts>=0.2.2 and
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 and ovos-tts-plugin-edge-tts>=0.2.2, we can conclude
      that your requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-tts-plugin-edge-tts` in the
      requested range (e.g., 0.2.3a1), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-tts-plugin-google-tx>=1.0.4a5`**  
Would add: `ovos-tts-plugin-google-tx>=1.0.3,<2.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}<=0.0.1 is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 depends on ovos-plugin-manager>=2.1.1.
      And because ovos-tts-plugin-google-tx==1.0.3 depends
      on ovos-plugin-manager>=1.0.0,<2.0.0 and only
      ovos-tts-plugin-google-tx<=1.0.3 is available, we can
      conclude that ovos-tts-plugin-google-tx>=1.0.3 and
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 and ovos-tts-plugin-google-tx>=1.0.3, we can conclude
      that your requirements are unsatisfiable.

      hint: Pre-releases are available for `ovos-tts-plugin-google-tx` in the
      requested range (e.g., 1.0.4a5), but pre-releases weren't enabled (try:
      `--prerelease=allow`)
```

**`ovos-vad-plugin-noise>=0.1.3a2`**  
Would add: `ovos-vad-plugin-noise>=0.1.2,<1.0.0`
```
Using Python 3.10.20 environment at: .venvs/py3.10
  × No solution found when resolving dependencies:
  ╰─▶ Because only
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}<=0.0.1 is available and
      ovos-audio-transformer-plugin-speechbrain-langdetect==0.0.1
      depends on ovos-plugin-manager>=2.1.1, we can conclude that
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 depends on ovos-plugin-manager>=2.1.1.
      And because ovos-vad-plugin-noise==0.1.2 depends on
      ovos-plugin-manager>=0.0.11,<2.0.0 and only ovos-vad-plugin-noise<=0.1.2
      is available, we can conclude that ovos-vad-plugin-noise>=0.1.2 and
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 are incompatible.
      And because you require
      ovos-audio-transformer-plugin-speechbrain-langdetect{python_full_version
      < '3.15'}>=0.0.1 and ovos-vad-plugin-noise>=0.1.2, we can conclude that
      your requirements are unsatisfiable.

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
