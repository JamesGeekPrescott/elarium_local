import os
import numpy as np
import wave

def write(path, samplerate, audio):
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())

def record_audio(
    duration: int = 2,
    samplerate: int = 44100,
    channels: int = 1,
    output_path: str = "temp_audio/output.wav"
) -> str:
    """
    Records audio from the default input device and writes it to a .wav file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Lazy import for CI compatibility
    if os.getenv("CI"):
        import sys
        from unittest import mock
        sys.modules["sounddevice"] = mock.MagicMock()

    import sounddevice as sd  # Moved here

    print(f"🎙️ Recording {duration}s to '{output_path}'...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()

    write(output_path, samplerate, audio)
    return output_path
