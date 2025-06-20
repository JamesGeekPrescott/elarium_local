Elarium is a local-first, modular voice assistant powered by Python, TDD, and audio AI components.


### Module Contracts
- [Recorder – `record_audio()`](docs/record_audio_behavior_contract.md)

## Features

### 🎙️ Whisper Transcription

This project includes a wrapper around [`whisper.cpp`](https://github.com/ggerganov/whisper.cpp) using the `whisper-cli.exe` binary.

#### Usage
The function `transcribe(audio_path)`:
- Accepts a `.wav` audio file path
- Returns timestamped transcription output
- Wraps the local `whisper-cli.exe` binary

#### Requirements
- whisper-cli.exe must be compiled and present at:  
  `whisper.cpp/build/bin/Release/whisper-cli.exe`
- Model file (e.g. `ggml-base.bin`) must be downloaded and placed in `whisper.cpp/`
- Audio input must be mono `.wav`

#### Status: ✅ Working
- Verified via pytest: `3/3 tests passing`
- See [Behavior Contract](docs/transcribe_whisper_contract.md)