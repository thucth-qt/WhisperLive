import sys
sys.path.append("/home/thucth/thucth/deployment/WhisperLive")

from whisper_live_sdk.client import TranscriptionClient, BatchTranscriptionClient

client = TranscriptionClient(
  "localhost",
  9090,
#   lang="vi",
  lang="en",
  translate=False,
  model="medium",
  use_vad=False,
  save_output_recording=False,                         # Only used for microphone input, False by Default
  output_recording_filename=None  # Only used for microphone input
)


# batch_client = BatchTranscriptionClient(
#     host="localhost",
#     port=9090,
#     lang="en",
#     translate=False,
#     model="medium",
#     use_vad=False,
# )
# # transcript = batch_client.transcribe("/home/thucth/thucth/deployment/WhisperLive/assets/preamble.wav")
# transcript = batch_client("/home/thucth/thucth/deployment/WhisperLive/assets/preamble.wav")
# print(f"Transcript: {transcript}")

# client()
client("/home/thucth/thucth/deployment/WhisperLive/assets/preamble.wav")
# client("/home/thucth/thucth/deployment/WhisperLive/assets/recorded_audio.wav")
# client("/home/thucth/thucth/deployment/WhisperLive/assets/call-vn-1-2KZS2JX4UB-1715192135128.wav")
# client("/home/thucth/thucth/deployment/WhisperLive/assets/jfk.flac")
# client(hls_url="http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_1xtra/bbc_1xtra.isml/bbc_1xtra-audio%3d96000.norewind.m3u8")
