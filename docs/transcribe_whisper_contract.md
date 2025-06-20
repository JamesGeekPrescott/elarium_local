# Behavior Contract: `transcribe()`

## Description
Transcribes a `.wav` audio file using `whisper-cli.exe` and returns the result as a string, including timestamped segments.

## Signature
```python
def transcribe(audio_path: str) -> str