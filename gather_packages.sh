uv pip compile --pre \
  lists/core.list \
  lists/utils.list \
  lists/dialog_transf.list  \
  lists/intent_transf.list  \
  lists/media.list  \
  lists/mic.list  \
  lists/ocp.list  \
  lists/phal.list  \
  lists/pipeline.list  \
  lists/skills.list  \
  lists/stt.list  \
  lists/translate.list  \
  lists/tts.list  \
  lists/tts_transf.list  \
  lists/utterance_transf.list  \
  lists/vad.list  \
  lists/ww.list \
  lists/audio_transf.list \
  lists/gui.list \
  lists/keywords.list \
  lists/embeddings.list \
  lists/solvers.list \
  lists/hivemind.list \
  lists/servers.list \
  -c https://raw.githubusercontent.com/OpenVoiceOS/ovos-releases/refs/heads/main/constraints-alpha.txt \
  -o resolved-constraints.txt
